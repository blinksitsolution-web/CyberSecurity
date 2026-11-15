#!/usr/bin/env python3
"""Check that a lab Sigma rule has the fields this portfolio requires.

This is not the full Sigma specification. It keeps the lab rules honest:
a title, a log source, a detection, a severity, and a MITRE ATT&CK tag.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REQUIRED = ("title", "id", "status", "description", "logsource", "detection", "level", "tags")
LEVELS = {"informational", "low", "medium", "high", "critical"}
ATTACK_TAG = re.compile(r"^attack\.t\d{4}(\.\d{3})?$")


def validate_rule(data: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["rule file must be a mapping"]
    for key in REQUIRED:
        if key not in data or data[key] in (None, "", [], {}):
            errors.append(f"missing {key}")
    level = str(data.get("level", "")).lower()
    if level and level not in LEVELS:
        errors.append(f"unknown level {level}")
    logsource = data.get("logsource")
    if isinstance(logsource, dict) and "product" not in logsource:
        errors.append("logsource needs a product")
    detection = data.get("detection")
    if isinstance(detection, dict) and "condition" not in detection:
        errors.append("detection needs a condition")
    tags = data.get("tags") or []
    if isinstance(tags, list) and not any(ATTACK_TAG.match(str(tag)) for tag in tags):
        errors.append("needs an ATT&CK technique tag such as attack.t1110")
    return errors


def load_rule(path: Path) -> tuple[dict, list[str]]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return data, validate_rule(data)


def main() -> None:
    parser = argparse.ArgumentParser(description="Check lab Sigma rules")
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.paths:
        _data, errors = load_rule(path)
        if errors:
            failed = True
            print(f"FAIL {path}: {'; '.join(errors)}")
        else:
            print(f"OK {path}")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
