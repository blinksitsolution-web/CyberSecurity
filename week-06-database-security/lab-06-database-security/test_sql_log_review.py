from pathlib import Path

from sql_log_review import review

SAMPLE = Path(__file__).resolve().parent / "samples" / "db-statements.log"


def test_parameterised_line_is_kept_and_tautology_is_flagged():
    flagged = review(SAMPLE)
    assert len(flagged) == 1
    assert "$1" not in flagged[0]
    assert "orders" not in flagged[0]
