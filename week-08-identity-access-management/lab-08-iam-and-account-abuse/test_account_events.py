from pathlib import Path

from account_events import brute_force, load_events, new_admins

SAMPLE = Path(__file__).resolve().parent / "samples" / "security-events.csv"


def test_sample_flags_one_source_and_one_admin_group():
    rows = load_events(SAMPLE)
    assert brute_force(rows) == [{"ip": "203.0.113.10", "count": 5}]
    admins = new_admins(rows)
    assert len(admins) == 1
    assert admins[0]["member"] == "newadmin"
    assert admins[0]["group"] == "Administrators"
