from pathlib import Path

from tcpdump_summary import parse_capture, summarise

SAMPLE = Path(__file__).resolve().parent / "samples" / "lab-handshake.txt"


def test_sample_handshake_has_syn_synack_ack():
    rows = parse_capture(SAMPLE)
    summary = summarise(rows)
    assert summary["packets"] == 3
    assert summary["flags"]["S"] == 1
    assert summary["flags"]["S."] == 1
    assert summary["flags"]["."] == 1
    assert rows[0]["dst"] == "192.168.56.10"
    assert rows[0]["dport"] == "22"
