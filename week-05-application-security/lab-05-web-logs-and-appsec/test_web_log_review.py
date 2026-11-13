from pathlib import Path

from web_log_review import review

SAMPLE = Path(__file__).resolve().parent / "samples" / "access.log"


def test_sample_flags_markup_and_ignores_ordinary_gets():
    findings = review(SAMPLE)
    assert len(findings) == 2
    assert all("search" in item["text"] for item in findings)
    assert all("/health" not in item["text"] for item in findings)
