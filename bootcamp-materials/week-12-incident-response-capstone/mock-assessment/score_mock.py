#!/usr/bin/env python3
"""Score the Week 12 study quiz.

Compare your answers file with the key after you have tried the questions.
The quiz is original practice for this portfolio. It is not the bootcamp exam.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def _rows(path: Path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def score(questions_path: Path, key_path: Path, answers_path: Path) -> dict:
    questions = _rows(questions_path)
    key = {row["id"]: row["answer"].strip().lower() for row in _rows(key_path)}
    given = {
        row["id"]: (row.get("answer") or "").strip().lower()
        for row in _rows(answers_path)
    }
    correct: list[str] = []
    incorrect: list[str] = []
    unanswered: list[str] = []
    for row in questions:
        question_id = row["id"]
        response = given.get(question_id, "")
        if response == "":
            unanswered.append(question_id)
        elif response == key.get(question_id):
            correct.append(question_id)
        else:
            incorrect.append(question_id)
    total = len(questions)
    percent = round((100 * len(correct) / total), 1) if total else 0.0
    return {
        "total": total,
        "correct_count": len(correct),
        "incorrect": incorrect,
        "unanswered": unanswered,
        "percent": percent,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Score mock-assessment answers")
    parser.add_argument("--questions", type=Path, default=Path("questions.csv"))
    parser.add_argument("--key", type=Path, default=Path("answer-key.csv"))
    parser.add_argument("--answers", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(score(args.questions, args.key, args.answers), indent=2))


if __name__ == "__main__":
    main()
