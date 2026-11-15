#!/usr/bin/env python3
"""Check a candidate password against the Week 8 lab policy.

This does not guess passwords and it does not read a wordlist from disk.
The banned list is a few obvious examples so the tests have something to reject.
"""

from __future__ import annotations

import argparse
import json

# Obvious examples only. A real banned list is maintained by the identity provider.
BANNED = {
    "password",
    "password1",
    "password123",
    "qwerty",
    "letmein",
    "admin",
    "welcome",
    "changeme",
}


def evaluate(password: str, *, min_length: int = 12, username: str | None = None) -> dict:
    reasons: list[str] = []
    if len(password) < min_length:
        reasons.append(f"shorter than {min_length} characters")
    if not any(character.islower() for character in password):
        reasons.append("needs a lowercase letter")
    if not any(character.isupper() for character in password):
        reasons.append("needs an uppercase letter")
    if not any(character.isdigit() for character in password):
        reasons.append("needs a digit")
    if not any(not character.isalnum() for character in password):
        reasons.append("needs a symbol")
    if password.lower() in BANNED:
        reasons.append("is on the small lab banned list")
    if username and username.lower() in password.lower():
        reasons.append("contains the username")
    return {"accepted": not reasons, "reasons": reasons, "min_length": min_length}


def main() -> None:
    parser = argparse.ArgumentParser(description="Check one password against the lab policy")
    parser.add_argument("--password", required=True)
    parser.add_argument("--username", default="")
    parser.add_argument("--min-length", type=int, default=12)
    args = parser.parse_args()
    result = evaluate(
        args.password,
        min_length=args.min_length,
        username=args.username or None,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
