#!/usr/bin/env python3
"""Check an incident timeline CSV for order and sources.

Blank rows are ignored. A filled row needs a time, an action, and a source.
"""

from __future__ import annotations

import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path


def lab_file(path: Path, root: Path | None = None) -> Path:
    base = (root or Path(__file__).resolve().parent).resolve()
    requested = Path(path)
    candidate = requested.resolve() if requested.is_absolute() else (base / requested).resolve()
    if not candidate.is_relative_to(base):
        raise ValueError(f"{path} is outside the lab folder")
    return candidate


def check(path: Path, root: Path | None = None) -> list[str]:
    errors = []
    previous = None
    filled = 0
    with lab_file(path, root).open(newline="", encoding="utf-8") as handle:
        for line_number, row in enumerate(csv.DictReader(handle), start=2):
            when = (row.get("time_utc") or "").strip()
            action = (row.get("action") or "").strip()
            source = (row.get("source") or "").strip()
            if not when and not action and not source:
                continue
            filled += 1
            if not when or not action or not source:
                errors.append(f"line {line_number}: time, action, and source are all required")
                continue
            try:
                current = datetime.fromisoformat(when.replace("Z", "+00:00"))
            except ValueError:
                errors.append(f"line {line_number}: time is not ISO-8601")
                continue
            if previous and current < previous:
                errors.append(f"line {line_number}: time moves backwards")
            previous = current
    if filled == 0:
        errors.append("timeline has no filled rows yet")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Check an incident timeline")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    errors = check(args.path)
    if errors:
        print("timeline_blocked")
        for item in errors:
            print(f"- {item}")
        sys.exit(1)
    print("timeline_ok")


if __name__ == "__main__":
    main()
