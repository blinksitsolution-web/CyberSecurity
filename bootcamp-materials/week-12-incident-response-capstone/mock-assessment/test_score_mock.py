import csv
from pathlib import Path

from score_mock import score

HERE = Path(__file__).resolve().parent


def _write_answers(path: Path, rows: list[tuple[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["id", "answer"])
        writer.writerows(rows)


def test_perfect_score_matches_the_key(tmp_path):
    with (HERE / "answer-key.csv").open(newline="", encoding="utf-8") as handle:
        key_rows = [(row["id"], row["answer"]) for row in csv.DictReader(handle)]
    answers = tmp_path / "answers.csv"
    _write_answers(answers, key_rows)
    result = score(HERE / "questions.csv", HERE / "answer-key.csv", answers)
    assert result["total"] == 40
    assert result["correct_count"] == 40
    assert result["percent"] == 100.0
    assert result["unanswered"] == []


def test_blank_and_wrong_are_separate(tmp_path):
    answers = tmp_path / "answers.csv"
    _write_answers(answers, [("q01", "a"), ("q02", "")])
    result = score(HERE / "questions.csv", HERE / "answer-key.csv", answers)
    assert "q01" in result["incorrect"]
    assert "q02" in result["unanswered"]
    assert result["correct_count"] == 0
