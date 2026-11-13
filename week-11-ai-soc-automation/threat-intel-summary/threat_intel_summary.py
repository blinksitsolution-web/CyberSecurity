#!/usr/bin/env python3
"""Summarise a local JSON threat-intel exercise file.

This reads a file you already have. It does not download indicators and it
does not block, scan, or contact anything.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

HUMAN_REVIEW = [
    "Is this file synthetic, or from a source you are allowed to store?",
    "Which values also appear in your own lab logs?",
    "What must stay manual: blocking, emailing a victim, or testing a system?",
    "What would you ask a senior analyst before acting?",
]


def summarise(path: Path) -> dict:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    grouped: dict[str, list[str]] = defaultdict(list)
    for item in payload.get("items", []):
        grouped[str(item.get("type", "unknown"))].append(str(item.get("value", "")))
    return {
        "data_label": payload.get("data_label", "unlabelled"),
        "source": payload.get("source", ""),
        "total": sum(len(values) for values in grouped.values()),
        "counts_by_type": {key: len(values) for key, values in sorted(grouped.items())},
        "values_by_type": {key: values for key, values in sorted(grouped.items())},
        "human_review": HUMAN_REVIEW,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarise a local indicator exercise file")
    parser.add_argument("json_path", type=Path)
    args = parser.parse_args()
    print(json.dumps(summarise(args.json_path), indent=2))


if __name__ == "__main__":
    main()
