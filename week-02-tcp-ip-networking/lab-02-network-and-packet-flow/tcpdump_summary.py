#!/usr/bin/env python3
"""Summarise a text tcpdump for the lab network.

This reads a file you saved. It does not open a network interface.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

LINE = re.compile(
    r"IP (?P<src>\d+\.\d+\.\d+\.\d+)\.(?P<sport>\d+) > "
    r"(?P<dst>\d+\.\d+\.\d+\.\d+)\.(?P<dport>\d+): Flags \[(?P<flags>[^\]]*)\]"
)


def lab_file(path: Path, root: Path | None = None) -> Path:
    base = (root or Path(__file__).resolve().parent).resolve()
    requested = Path(path)
    candidate = requested.resolve() if requested.is_absolute() else (base / requested).resolve()
    if not candidate.is_relative_to(base):
        raise ValueError(f"{path} is outside the lab folder")
    return candidate


def parse_capture(path: Path, root: Path | None = None) -> list[dict]:
    rows = []
    for number, line in enumerate(lab_file(path, root).read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip() or line.startswith("#"):
            continue
        match = LINE.search(line)
        if not match:
            continue
        rows.append({"line": number, **match.groupdict()})
    return rows


def summarise(rows: list[dict]) -> dict:
    flags = {}
    for row in rows:
        flags[row["flags"]] = flags.get(row["flags"], 0) + 1
    return {"packets": len(rows), "flags": flags, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarise a saved tcpdump text file")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    summary = summarise(parse_capture(args.path))
    print(f"packets={summary['packets']}")
    for name, count in sorted(summary["flags"].items()):
        print(f"flags[{name}]={count}")


if __name__ == "__main__":
    main()
