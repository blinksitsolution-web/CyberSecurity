#!/usr/bin/env python3
"""Summarise a control-status CSV for the Week 11 compliance exercise.

The sample file is synthetic. The script counts statuses. It does not decide
that a control is met. A person reviews the evidence column first.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ALLOWED = ("met", "partial", "gap", "not-reviewed")


def summarise(path: Path) -> dict:
    counts = {status: 0 for status in ALLOWED}
    unknown: list[str] = []
    rows = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            status = (row.get("status") or "").strip().lower()
            control_id = row.get("control_id") or ""
            if status not in counts:
                unknown.append(control_id)
            else:
                counts[status] += 1
            rows.append(row)
    total = len(rows)
    return {
        "data_label": "see data_label column; sample file is synthetic",
        "total": total,
        "counts": counts,
        "unknown_status": unknown,
        "needs_human_review": counts["partial"] + counts["gap"] + counts["not-reviewed"] + len(unknown),
        "reminder": "Do not treat this count as an audit opinion. Read the evidence yourself.",
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Compliance status count",
        "",
        report["reminder"],
        "",
        f"Rows: {report['total']}",
        "",
        "| Status | Count |",
        "| --- | ---: |",
    ]
    for status, count in report["counts"].items():
        lines.append(f"| {status} | {count} |")
    if report["unknown_status"]:
        lines.append("")
        lines.append("Unknown status on: " + ", ".join(report["unknown_status"]))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Count control statuses in a CSV")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--markdown", action="store_true")
    args = parser.parse_args()
    report = summarise(args.csv_path)
    if args.markdown:
        print(render_markdown(report))
    else:
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
