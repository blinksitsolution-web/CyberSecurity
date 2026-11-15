#!/usr/bin/env python3
"""Triage synthetic or lab-owned authentication logs.

Flags a burst of failed logons from one source, and a new member of an
admin group. It reads the files you pass. It does not watch a network.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

MONTHS = {
    name: index
    for index, name in enumerate(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        start=1,
    )
}
SYSLOG_RE = re.compile(
    r"^(?P<mon>\w{3})\s+(?P<day>\d+)\s+(?P<time>\d{2}:\d{2}:\d{2})\s+\S+\s+(?P<msg>.*)$"
)
FAILED_RE = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\S+)"
)
ACCEPTED_RE = re.compile(r"Accepted \S+ for (?P<user>\S+) from (?P<ip>\S+)")
GROUP_RE = re.compile(r"add '(?P<user>[^']+)' to group '(?P<group>[^']+)'", re.IGNORECASE)
USERMOD_RE = re.compile(
    r"usermod\s+-aG\s+(?P<group>\S+)\s+(?P<user>\S+)",
    re.IGNORECASE,
)
ADMIN_GROUPS = {"sudo", "admin", "wheel", "administrators"}


def _parse_syslog_time(match: re.Match[str], year: int) -> datetime:
    month = MONTHS[match.group("mon")]
    day = int(match.group("day"))
    hour, minute, second = (int(part) for part in match.group("time").split(":"))
    return datetime(year, month, day, hour, minute, second)


def parse_auth_log(path: Path, year: int = 2026) -> list[dict]:
    events: list[dict] = []
    for line_number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip() or line.startswith("#"):
            continue
        header = SYSLOG_RE.match(line)
        if not header:
            continue
        when = _parse_syslog_time(header, year)
        message = header.group("msg")
        failed = FAILED_RE.search(message)
        if failed:
            events.append(
                {
                    "source": "linux-auth",
                    "kind": "failed_logon",
                    "time": when,
                    "user": failed.group("user"),
                    "ip": failed.group("ip"),
                    "line": line_number,
                }
            )
            continue
        accepted = ACCEPTED_RE.search(message)
        if accepted:
            events.append(
                {
                    "source": "linux-auth",
                    "kind": "accepted_logon",
                    "time": when,
                    "user": accepted.group("user"),
                    "ip": accepted.group("ip"),
                    "line": line_number,
                }
            )
            continue
        grouped = GROUP_RE.search(message)
        if grouped:
            events.append(
                {
                    "source": "linux-auth",
                    "kind": "group_add",
                    "time": when,
                    "user": grouped.group("user"),
                    "group": grouped.group("group"),
                    "line": line_number,
                }
            )
            continue
        modified = USERMOD_RE.search(message)
        if modified:
            events.append(
                {
                    "source": "linux-auth",
                    "kind": "group_add",
                    "time": when,
                    "user": modified.group("user"),
                    "group": modified.group("group"),
                    "line": line_number,
                }
            )
    return events


def parse_windows_csv(path: Path) -> list[dict]:
    events: list[dict] = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        for line_number, row in enumerate(csv.DictReader(handle), start=2):
            when = datetime.fromisoformat(row["TimeCreated"].replace("Z", "+00:00")).replace(tzinfo=None)
            event_id = int(row["EventID"])
            kind = {
                4625: "failed_logon",
                4624: "accepted_logon",
                4720: "account_created",
                4732: "group_add",
            }.get(event_id, "other")
            events.append(
                {
                    "source": "windows-security",
                    "kind": kind,
                    "time": when,
                    "event_id": event_id,
                    "user": row.get("TargetUserName") or row.get("MemberName") or "",
                    "member": row.get("MemberName") or "",
                    "group": row.get("GroupName") or "",
                    "ip": row.get("IpAddress") or "",
                    "line": line_number,
                }
            )
    return events


def find_brute_force(events: list[dict], threshold: int = 5, window_minutes: int = 10) -> list[dict]:
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for event in events:
        if event["kind"] != "failed_logon" or not event.get("ip"):
            continue
        grouped[(event["source"], event["ip"])].append(event)
    findings = []
    window = timedelta(minutes=window_minutes)
    for (source, ip), rows in sorted(grouped.items()):
        rows.sort(key=lambda item: item["time"])
        start = 0
        for end, event in enumerate(rows):
            while event["time"] - rows[start]["time"] > window:
                start += 1
            chunk = rows[start : end + 1]
            if len(chunk) >= threshold:
                findings.append(
                    {
                        "kind": "brute_force",
                        "source": source,
                        "source_ip": ip,
                        "count": len(chunk),
                        "usernames": sorted({item["user"] for item in chunk}),
                        "window_start": chunk[0]["time"].isoformat(sep=" "),
                        "window_end": chunk[-1]["time"].isoformat(sep=" "),
                        "technique": "T1110",
                    }
                )
                break
    return findings


def find_new_admins(events: list[dict]) -> list[dict]:
    findings = []
    for event in events:
        if event["kind"] != "group_add":
            continue
        group = str(event.get("group", ""))
        if group.lower() not in ADMIN_GROUPS:
            continue
        account = event.get("member") or event.get("user")
        findings.append(
            {
                "kind": "new_admin",
                "source": event["source"],
                "account": account,
                "group": group,
                "time": event["time"].isoformat(sep=" "),
                "line": event["line"],
                "technique": "T1098",
            }
        )
    return findings


def triage(
    auth_log: Path | None = None,
    windows_csv: Path | None = None,
    *,
    label: str = "synthetic-lab-sample",
    threshold: int = 5,
) -> dict:
    events: list[dict] = []
    if auth_log:
        events.extend(parse_auth_log(auth_log))
    if windows_csv:
        events.extend(parse_windows_csv(windows_csv))
    failures = [event for event in events if event["kind"] == "failed_logon"]
    return {
        "data_label": label,
        "event_count": len(events),
        "failed_logons": len(failures),
        "brute_force": find_brute_force(events, threshold=threshold),
        "new_admins": find_new_admins(events),
        "reminder": "Keep this label accurate. Sample files in samples/ are synthetic.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarise auth failures and new admin groups")
    parser.add_argument("--auth-log", type=Path)
    parser.add_argument("--windows-csv", type=Path)
    parser.add_argument("--label", default="synthetic-lab-sample")
    parser.add_argument("--threshold", type=int, default=5)
    args = parser.parse_args()
    if not args.auth_log and not args.windows_csv:
        parser.error("pass --auth-log or --windows-csv")
    report = triage(
        args.auth_log,
        args.windows_csv,
        label=args.label,
        threshold=args.threshold,
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
