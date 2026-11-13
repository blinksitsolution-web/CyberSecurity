from pathlib import Path

from wazuh_offline import summarise

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "alerts.json"


def test_fixture_keeps_two_techniques_and_a_human_line():
    report = summarise(FIXTURE)
    assert report["data_label"] == "synthetic-wazuh-export"
    assert report["count"] == 2
    assert report["techniques"] == ["T1098", "T1110.001"]
    assert "authorised" in report["human_review"]
