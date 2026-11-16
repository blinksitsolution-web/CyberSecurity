#!/usr/bin/env python3
"""Caesar cipher for the Week 7 assignment.

Letters shift. Spaces and other characters stay put. Nothing here is suitable
for protecting a real message.
"""

from __future__ import annotations

import argparse

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
COMMON_WORDS = {
    "A",
    "I",
    "IS",
    "IT",
    "IN",
    "OF",
    "TO",
    "AND",
    "THE",
    "THIS",
    "THAT",
    "SECRET",
    "MESSAGE",
    "WITH",
}
# Rough English letter weights. Used only to rank Caesar shifts.
FREQUENCY = {
    "E": 12.7,
    "T": 9.1,
    "A": 8.2,
    "O": 7.5,
    "I": 7.0,
    "N": 6.7,
    "S": 6.3,
    "H": 6.1,
    "R": 6.0,
    "D": 4.3,
    "L": 4.0,
    "C": 2.8,
    "U": 2.8,
    "M": 2.4,
    "W": 2.4,
    "F": 2.2,
    "G": 2.0,
    "Y": 2.0,
    "P": 1.9,
    "B": 1.5,
    "V": 1.0,
    "K": 0.8,
    "J": 0.2,
    "X": 0.2,
    "Q": 0.1,
    "Z": 0.1,
}


def _shift_char(character: str, shift: int) -> str:
    if character.upper() not in ALPHABET:
        return character
    index = ALPHABET.index(character.upper())
    shifted = ALPHABET[(index + shift) % 26]
    return shifted.lower() if character.islower() else shifted


def encrypt(text: str, shift: int) -> str:
    """Move letters forward by shift places."""
    return "".join(_shift_char(character, shift) for character in text)


def decrypt(text: str, shift: int) -> str:
    """Move letters backward by shift places."""
    return encrypt(text, -shift)


def english_score(text: str) -> float:
    """Higher means the text looks more like English."""
    score = 0.0
    for word in text.upper().split():
        if word in COMMON_WORDS:
            score += 8.0
    letters = [character for character in text.upper() if character in ALPHABET]
    if not letters:
        return score
    for letter in letters:
        score += FREQUENCY.get(letter, 0.0) / len(letters)
    return score


def brute_force(ciphertext: str) -> list[dict]:
    """Try every non-zero shift. Best English score first."""
    rows = []
    for shift in range(1, 26):
        plain = decrypt(ciphertext, shift)
        rows.append({"shift": shift, "plaintext": plain, "score": english_score(plain)})
    rows.sort(key=lambda row: row["score"], reverse=True)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Caesar cipher practice")
    parser.add_argument("action", choices=("encrypt", "decrypt", "brute"))
    parser.add_argument("text")
    parser.add_argument("--shift", type=int, default=0)
    args = parser.parse_args()
    if args.action == "brute":
        for row in brute_force(args.text):
            print(f"shift={row['shift']:2d}  score={row['score']:.2f}  {row['plaintext']}")
        return
    if args.action == "encrypt":
        print(encrypt(args.text, args.shift))
        return
    print(decrypt(args.text, args.shift))


if __name__ == "__main__":
    main()
