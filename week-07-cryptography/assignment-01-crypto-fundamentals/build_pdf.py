#!/usr/bin/env python3
"""Build the Week 7 assignment PDF from STEP-BY-STEP.md.

Uses pandoc and weasyprint, same approach as the lab-guide builder.
Paths are fixed to this folder. The script does not accept a filename argument.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "STEP-BY-STEP.md"
CSS = HERE / "guide.css"
PDF = HERE / "LAB-07b-crypto-assignment.pdf"
HEADER = HERE / ".header.html"


def main() -> None:
    if not SOURCE.is_file() or not CSS.is_file():
        print("Missing STEP-BY-STEP.md or guide.css", file=sys.stderr)
        sys.exit(1)
    HEADER.write_text(
        "<style>@page { @bottom-left { content: \"LAB-07b\"; "
        "font-family: Liberation Sans, sans-serif; font-size: 8pt; color: #5c6b7a; } }</style>\n",
        encoding="utf-8",
    )
    subprocess.run(
        [
            "pandoc",
            str(SOURCE),
            "--from",
            "markdown+fenced_divs+pipe_tables",
            "--pdf-engine=weasyprint",
            "--css",
            str(CSS),
            "--include-in-header",
            str(HEADER),
            "--metadata",
            "title=Lab 07b — Cryptography assignment",
            "-o",
            str(PDF),
        ],
        check=True,
    )
    print(PDF.name)


if __name__ == "__main__":
    main()
