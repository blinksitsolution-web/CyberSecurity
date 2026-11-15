from pathlib import Path

from compliance_report import summarise

SAMPLE = Path(__file__).resolve().parent / "sample-controls.csv"


def test_sample_counts_are_explicit():
    report = summarise(SAMPLE)
    assert report["total"] == 8
    assert report["counts"] == {
        "met": 2,
        "partial": 2,
        "gap": 2,
        "not-reviewed": 2,
    }
    assert report["unknown_status"] == []
    assert report["needs_human_review"] == 6


def test_unknown_status_is_not_counted_as_met(tmp_path):
    path = tmp_path / "controls.csv"
    path.write_text(
        "control_id,status,evidence,data_label\n"
        "C-1,done,none,synthetic\n"
        "C-2,met,policy file,synthetic\n"
    )
    report = summarise(path)
    assert report["counts"]["met"] == 1
    assert report["unknown_status"] == ["C-1"]
