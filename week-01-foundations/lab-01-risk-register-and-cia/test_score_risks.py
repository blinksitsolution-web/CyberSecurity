from pathlib import Path

import pytest

from score_risks import band, flagged, load_risks, matrix_cells, render_report

EXAMPLE = Path(__file__).resolve().parent / "examples" / "example-risk-register.csv"
BLANK = """id,asset,threat,vulnerability,likelihood,impact
R-01,Laptop,Theft,No lock,,
R-02,PIN,Shoulder surfing,Written on a note,4,
"""


def test_bands_follow_the_lab_matrix():
    assert band(1) == "low"
    assert band(5) == "low"
    assert band(6) == "medium"
    assert band(11) == "medium"
    assert band(12) == "high"
    assert band(19) == "high"
    assert band(20) == "critical"
    assert band(25) == "critical"
    with pytest.raises(ValueError):
        band(0)


def test_example_solution_scores_and_flags_four_risks():
    risks = load_risks(EXAMPLE)
    assert all(risk["example"] for risk in risks)
    by_id = {risk["id"]: risk for risk in risks}
    assert by_id["R-01"]["score"] == 12
    assert by_id["R-03"]["score"] == 20
    assert by_id["R-03"]["band"] == "critical"
    assert by_id["R-05"]["band"] == "medium"
    assert [risk["id"] for risk in flagged(risks)] == ["R-01", "R-02", "R-03", "R-04"]
    assert matrix_cells(risks)[(4, 5)] == ["R-03", "R-04"]


def test_blanks_are_not_treated_as_zero(tmp_path):
    target = tmp_path / "blank.csv"
    target.write_text(BLANK, encoding="utf-8")
    before = target.read_bytes()
    risks = load_risks(target)
    assert all(risk["score"] is None for risk in risks)
    assert flagged(risks) == []
    report = render_report(risks, target)
    assert "None yet" in report
    assert "R-02: missing impact" in report
    assert target.read_bytes() == before


def test_rejects_a_score_outside_the_scale(tmp_path):
    path = tmp_path / "bad.csv"
    path.write_text(
        "id,asset,threat,vulnerability,likelihood,impact\n"
        "R-9,Laptop,Theft,Unlocked,6,3\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="1 to 5"):
        load_risks(path)


def test_report_names_a_high_asset():
    risks = load_risks(EXAMPLE)
    report = render_report(risks, EXAMPLE)
    assert "EXAMPLE DATA" in report
    assert "R-04 critical 20" in report
    assert "I5" in report and "L1" in report
