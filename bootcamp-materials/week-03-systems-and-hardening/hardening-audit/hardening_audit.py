#!/usr/bin/env python3
"""Read-only hardening audit for a Linux-style file tree.

The script only opens files for reading and only calls stat. It does not
change permissions, install packages, or restart services. Point --root at
/ on your Ubuntu lab VM, or at a copy of config files. A missing file is
SKIP: absence is not a pass.
"""

from __future__ import annotations

import argparse
import json
import os
import stat
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Check:
    check_id: str
    title: str
    status: str
    detail: str


def _read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def _sshd_value(text: str, key: str) -> str | None:
    found = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) == 2 and parts[0].lower() == key.lower():
            found = parts[1].split("#", 1)[0].strip()
    return found


def _ssh_permit_root(root: Path) -> Check:
    path = root / "etc" / "ssh" / "sshd_config"
    text = _read_text(path)
    if text is None:
        return Check(
            "ssh-permit-root",
            "SSH root login",
            "skip",
            f"Could not read {path}",
        )
    value = _sshd_value(text, "PermitRootLogin")
    if value is None:
        return Check(
            "ssh-permit-root",
            "SSH root login",
            "review",
            "PermitRootLogin is unset. OpenSSH defaults can change; set it explicitly to no.",
        )
    if value.lower() in {"no", "prohibit-password"}:
        return Check(
            "ssh-permit-root",
            "SSH root login",
            "pass",
            f"PermitRootLogin {value}",
        )
    return Check(
        "ssh-permit-root",
        "SSH root login",
        "fail",
        f"PermitRootLogin {value}. Prefer no, and use a normal admin account.",
    )


def _ssh_password_auth(root: Path) -> Check:
    path = root / "etc" / "ssh" / "sshd_config"
    text = _read_text(path)
    if text is None:
        return Check(
            "ssh-password-auth",
            "SSH password authentication",
            "skip",
            f"Could not read {path}",
        )
    value = _sshd_value(text, "PasswordAuthentication")
    if value is None:
        return Check(
            "ssh-password-auth",
            "SSH password authentication",
            "review",
            "PasswordAuthentication is unset. Record the decision in the baseline.",
        )
    if value.lower() == "no":
        return Check(
            "ssh-password-auth",
            "SSH password authentication",
            "pass",
            "PasswordAuthentication no. Key-based login is in use or planned.",
        )
    return Check(
        "ssh-password-auth",
        "SSH password authentication",
        "review",
        "PasswordAuthentication yes. Acceptable on a private lab only if passwords are strong and root login is off.",
    )


def _mode_check(path: Path, check_id: str, title: str, forbid_world: str) -> Check:
    try:
        mode = path.stat().st_mode
    except OSError:
        return Check(check_id, title, "skip", f"Could not stat {path}")
    world_read = bool(mode & stat.S_IROTH)
    world_write = bool(mode & stat.S_IWOTH)
    pretty = oct(mode & 0o777)
    if forbid_world == "write" and world_write:
        return Check(check_id, title, "fail", f"{path} is world-writable ({pretty})")
    if forbid_world == "read" and world_read:
        return Check(check_id, title, "fail", f"{path} is world-readable ({pretty})")
    return Check(check_id, title, "pass", f"{path} mode {pretty}")


def _world_writable(root: Path) -> Check:
    base = root / "home"
    if not base.is_dir():
        return Check(
            "home-world-writable",
            "World-writable files under home",
            "skip",
            f"{base} is not a directory",
        )
    found: list[str] = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [name for name in dirnames if name not in {".git", ".venv"}]
        for name in filenames:
            path = Path(dirpath) / name
            try:
                mode = path.stat().st_mode
            except OSError:
                continue
            if mode & stat.S_IWOTH:
                found.append(str(path))
            if len(found) >= 20:
                break
        if len(found) >= 20:
            break
    if found:
        preview = ", ".join(found[:5])
        return Check(
            "home-world-writable",
            "World-writable files under home",
            "fail",
            f"Found {len(found)} world-writable file(s). First: {preview}",
        )
    return Check(
        "home-world-writable",
        "World-writable files under home",
        "pass",
        f"No world-writable files under {base}",
    )


def _pass_max_days(root: Path) -> Check:
    path = root / "etc" / "login.defs"
    text = _read_text(path)
    if text is None:
        return Check("pass-max-days", "Password maximum age", "skip", f"Could not read {path}")
    value = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2 and parts[0] == "PASS_MAX_DAYS":
            value = parts[1]
    if value is None:
        return Check(
            "pass-max-days",
            "Password maximum age",
            "review",
            "PASS_MAX_DAYS is not set",
        )
    try:
        days = int(value)
    except ValueError:
        return Check("pass-max-days", "Password maximum age", "review", f"Unreadable value {value}")
    if days <= 0:
        return Check(
            "pass-max-days",
            "Password maximum age",
            "review",
            "PASS_MAX_DAYS is 0 or negative, which usually means passwords do not expire",
        )
    if days > 365:
        return Check(
            "pass-max-days",
            "Password maximum age",
            "review",
            f"PASS_MAX_DAYS {days} is longer than a year. Record why in the baseline.",
        )
    return Check("pass-max-days", "Password maximum age", "pass", f"PASS_MAX_DAYS {days}")


def audit(root: Path) -> list[Check]:
    """Run every check under root. root is only read."""
    root = Path(root)
    return [
        _ssh_permit_root(root),
        _ssh_password_auth(root),
        _mode_check(
            root / "etc" / "passwd",
            "passwd-not-world-writable",
            "passwd is not world-writable",
            "write",
        ),
        _mode_check(
            root / "etc" / "shadow",
            "shadow-not-world-readable",
            "shadow is not world-readable",
            "read",
        ),
        _world_writable(root),
        _pass_max_days(root),
    ]


def render_text(checks: list[Check]) -> str:
    lines = ["Read-only hardening audit", "Status is pass, fail, review, or skip.", ""]
    for check in checks:
        lines.append(f"[{check.status.upper()}] {check.check_id}: {check.detail}")
    counts: dict[str, int] = {}
    for check in checks:
        counts[check.status] = counts.get(check.status, 0) + 1
    summary = ", ".join(f"{key}={counts[key]}" for key in sorted(counts))
    lines.extend(["", f"Summary: {summary}"])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only Linux hardening audit")
    parser.add_argument(
        "--root",
        default="/",
        help="Filesystem root to read. Use / on the lab VM, or a fixture in tests.",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    checks = audit(Path(args.root))
    if args.format == "json":
        print(json.dumps([asdict(item) for item in checks], indent=2))
    else:
        print(render_text(checks))


if __name__ == "__main__":
    main()
