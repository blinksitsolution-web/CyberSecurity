#!/usr/bin/env python3
"""Flag failed-logon bursts and new local administrators in a CSV export.

Reads a file. Does not query a domain.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def lab_file(path: Path) -> Path:
    base = Path(__file__).resolve().parent
    requested = Path(path)
    candidate = requested.resolve() if requested.is_absolute() else (base / requested).resolve()
    if not candidate.is_relative_to(base):
        raise ValueError(f"{path} is outside the lab folder")
    return candidate


def load_events(path: Path) -> list[dict]:
    rows = []
    with lab_file(path).open(newline="", encoding="utf-8") as handle:
        for line_number, row in enumerate(csv.DictReader(handle), start=2):
            when = datetime.fromisoformat(row["TimeCreated"].replace("Z", "+00:00"))
            rows.append(
                {
                    "line": line_number,
                    "event_id": int(row["EventID"]),
                    "time": when,
                    "user": row.get("TargetUserName") or "",
                    "ip": row.get("IpAddress") or "",
                    "group": row.get("GroupName") or "",
                    "member": row.get("MemberName") or "",
                }
            )
    return rows


def brute_force(rows: list[dict], threshold: int = 5) -> list[dict]:
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        if row["event_id"] == 4625 and row["ip"]:
            counts[row["ip"]] += 1
    return [{"ip": ip, "count": count} for ip, count in sorted(counts.items()) if count >= threshold]


def new_admins(rows: list[dict]) -> list[dict]:
    return [
        {"member": row["member"], "group": row["group"], "line": row["line"]}
        for row in rows
        if row["event_id"] == 4732 and row["group"].lower() == "administrators"
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Review an exported security CSV")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    rows = load_events(args.path)
    print("data_label=synthetic-unless-you-say-otherwise")
    for item in brute_force(rows):
        print(f"brute_force ip={item['ip']} count={item['count']}")
    for item in new_admins(rows):
        print(f"new_admin member={item['member']} group={item['group']} line={item['line']}")


if __name__ == "__main__":
    main()
