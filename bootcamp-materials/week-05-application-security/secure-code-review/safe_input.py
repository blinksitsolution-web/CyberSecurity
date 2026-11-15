#!/usr/bin/env python3
"""Safe handling for untrusted text in the Week 5 training sandbox.

The functions below are the fixes. The README shows the unsafe patterns
only as short examples of what to reject in a code review.
"""

from __future__ import annotations

import argparse
import re

_USERNAME = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{2,31}$")


def escape_html(value: str) -> str:
    """Encode the five characters that change HTML meaning."""
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#x27;")
    )


def is_safe_username(value: str) -> bool:
    """Allow a short lab username. Reject spaces, quotes, and markup."""
    return bool(_USERNAME.fullmatch(value))


def parse_positive_id(value: str) -> int:
    """Accept a base-10 id such as 1 or 42. Reject signs, spaces, and text."""
    if not re.fullmatch(r"[1-9][0-9]{0,8}", value):
        raise ValueError("id must be a positive integer")
    return int(value)


def main() -> None:
    parser = argparse.ArgumentParser(description="Encode text for HTML output")
    parser.add_argument("text")
    args = parser.parse_args()
    print(escape_html(args.text))


if __name__ == "__main__":
    main()
