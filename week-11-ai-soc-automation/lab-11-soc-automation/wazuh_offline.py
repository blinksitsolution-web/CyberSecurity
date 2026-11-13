#!/usr/bin/env python3
"""Summarise a saved Wazuh-style alert export.

Does not call the network. A live API belongs in the lab guide, with your own token.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def lab_file(path: Path) -> Path:
    base = Path(__file__).resolve().parent
    requested = Path(path)
    candidate = requested.resolve() if requested.is_absolute() else (base / requested).resolve()
    if not candidate.is_relative_to(base):
        raise ValueError(f"{path} is outside the lab folder")
    return candidate


def summarise(path: Path) -> dict:
    payload = json.loads(lab_file(path).read_text(encoding="utf-8"))
    alerts = payload.get("alerts", [])
    return {
        "data_label": payload.get("data_label", "unlabelled"),
        "count": len(alerts),
        "techniques": sorted({item.get("technique", "") for item in alerts}),
        "ids": [item.get("id") for item in alerts],
        "human_review": "Confirm the agent, the time, and whether the account change was authorised before you close the alert.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarise a saved alert JSON file")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    print(json.dumps(summarise(args.path), indent=2))


if __name__ == "__main__":
    main()
