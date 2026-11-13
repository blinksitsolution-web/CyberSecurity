#!/usr/bin/env python3
"""Build trainee PDFs from each lab's LAB-*.md source.

Requires pandoc and weasyprint:
  sudo apt-get install pandoc weasyprint

Answer keys named TUTOR-ANSWER-KEY.md are not built into PDFs.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = Path(__file__).resolve().parent / "lab.css"


def page_count(pdf: Path) -> int:
    """Count pages in a WeasyPrint PDF, whose page objects are compressed."""
    import re
    import zlib

    data = pdf.read_bytes()
    pages = 0
    for match in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", data, re.S):
        try:
            text = zlib.decompress(match.group(1))
        except zlib.error:
            continue
        pages += text.count(b"/Type /Page")
        pages -= text.count(b"/Type /Pages")
    return max(pages, 0)


def trainee_source(path: Path) -> Path:
    """Accept only week-*/lab-*/LAB-*.md inside this repository."""
    requested = path if path.is_absolute() else ROOT / path
    candidate = requested.resolve()
    if not candidate.is_relative_to(ROOT):
        raise ValueError(f"{path} is outside the repository")
    relative = candidate.relative_to(ROOT)
    if len(relative.parts) != 3:
        raise ValueError(f"{path} is not a lab guide")
    week, lab, name = relative.parts
    if not (week.startswith("week-") and lab.startswith("lab-") and name.startswith("LAB-") and name.endswith(".md")):
        raise ValueError(f"{path} is not a trainee LAB-*.md file")
    return candidate


def build_one(source: Path) -> Path:
    pdf = source.with_suffix(".pdf")
    header = ROOT / "labs" / ".header" / f"{source.stem}.html"
    header.parent.mkdir(parents=True, exist_ok=True)
    header.write_text(
        "<style>@page { @bottom-left { content: \""
        + source.stem.replace('"', "")
        + "\"; font-family: Liberation Sans, sans-serif; font-size: 8pt; color: #5c6b7a; } }</style>\n",
        encoding="utf-8",
    )
    command = [
        "pandoc",
        str(source),
        "--from",
        "markdown+fenced_divs+pipe_tables",
        "--pdf-engine=weasyprint",
        "--css",
        str(CSS),
        "--include-in-header",
        str(header),
        "--metadata",
        "lang=en",
        "-o",
        str(pdf),
    ]
    subprocess.run(command, check=True)
    return pdf


def main() -> None:
    parser = argparse.ArgumentParser(description="Build lab trainee PDFs")
    parser.add_argument("sources", nargs="*", type=Path, help="Optional LAB-*.md paths")
    args = parser.parse_args()
    requested = [Path(item) for item in args.sources] or sorted(ROOT.glob("week-*/lab-*/LAB-*.md"))
    if not requested:
        print("No LAB-*.md sources found", file=sys.stderr)
        sys.exit(1)
    if not CSS.is_file():
        print(f"Missing {CSS}", file=sys.stderr)
        sys.exit(1)
    try:
        sources = [trainee_source(path) for path in requested]
    except ValueError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
    for source in sources:
        pdf = build_one(source)
        text_check = source.read_text(encoding="utf-8")
        if "TUTOR ANSWER KEY" in text_check:
            print(f"Refusing to build {source}: answer key text is in the trainee source", file=sys.stderr)
            sys.exit(1)
        print(f"{pdf.relative_to(ROOT)}  pages={page_count(pdf)}")


if __name__ == "__main__":
    main()
