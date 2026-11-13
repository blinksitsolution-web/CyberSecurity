#!/usr/bin/env python3
"""Flag lab access-log lines that carry HTML markup in the request.

This reads a file. It does not send requests.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import unquote


def suspicious(request: str) -> bool:
    text = unquote(request).lower()
    return "<script" in text or "onerror=" in text


def lab_file(path: Path) -> Path:
    base = Path(__file__).resolve().parent
    requested = Path(path)
    candidate = requested.resolve() if requested.is_absolute() else (base / requested).resolve()
    if not candidate.is_relative_to(base):
        raise ValueError(f"{path} is outside the lab folder")
    return candidate


def review(path: Path) -> list[dict]:
    findings = []
    for number, line in enumerate(lab_file(path).read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip() or line.startswith("#"):
            continue
        if suspicious(line):
            findings.append({"line": number, "text": line})
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Review a saved access log")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    findings = review(args.path)
    print(f"flagged={len(findings)} data_label=check-the-file-header")
    for item in findings:
        print(f"{item['line']}: {item['text']}")


if __name__ == "__main__":
    main()
