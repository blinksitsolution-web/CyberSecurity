from pathlib import Path

from threat_intel_summary import summarise

SAMPLE = Path(__file__).resolve().parent / "sample-feed.json"


def test_sample_feed_is_grouped_and_labelled():
    report = summarise(SAMPLE)
    assert report["data_label"] == "synthetic-lab-feed"
    assert report["total"] == 4
    assert report["counts_by_type"] == {"domain": 1, "ipv4": 2, "sha256": 1}
    assert "203.0.113.10" in report["values_by_type"]["ipv4"]
    assert len(report["human_review"]) >= 3
