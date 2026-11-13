#!/usr/bin/env python3
"""Flag synthetic log lines that are not parameterised statements.

Reads a file. Does not connect to a database.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def looks_injected(line: str) -> bool:
    lowered = line.lower()
    if line.startswith("#"):
        return False
    return " or " in lowered and "=" in lowered and "$1" not in lowered


def lab_file(path: Path) -> Path:
    base = Path(__file__).resolve().parent
    requested = Path(path)
    candidate = requested.resolve() if requested.is_absolute() else (base / requested).resolve()
    if not candidate.is_relative_to(base):
        raise ValueError(f"{path} is outside the lab folder")
    return candidate


def review(path: Path) -> list[str]:
    flagged = []
    for line in lab_file(path).read_text(encoding="utf-8").splitlines():
        if looks_injected(line):
            flagged.append(line)
    return flagged


def main() -> None:
    parser = argparse.ArgumentParser(description="Review a saved database log")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    flagged = review(args.path)
    print(f"flagged={len(flagged)} data_label=synthetic-unless-you-change-the-file")
    for line in flagged:
        print(line)


if __name__ == "__main__":
    main()
