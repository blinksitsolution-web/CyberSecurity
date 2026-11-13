from pathlib import Path

from log_triage import find_brute_force, find_new_admins, parse_auth_log, parse_windows_csv, triage

SAMPLES = Path(__file__).resolve().parent / "samples"


def test_linux_sample_flags_one_source_and_sudo():
    events = parse_auth_log(SAMPLES / "auth.log")
    brute = find_brute_force(events)
    admins = find_new_admins(events)
    assert len(brute) == 1
    assert brute[0]["source_ip"] == "203.0.113.10"
    assert brute[0]["count"] >= 5
    assert {item["account"] for item in admins} == {"newadmin"}
    assert admins[0]["group"] == "sudo"


def test_two_failures_do_not_alert():
    events = parse_auth_log(SAMPLES / "auth.log")
    quiet = [event for event in events if event.get("ip") == "198.51.100.8"]
    assert quiet
    assert find_brute_force(quiet) == []


def test_windows_sample_flags_administrators_only():
    events = parse_windows_csv(SAMPLES / "windows-security.csv")
    admins = find_new_admins(events)
    assert len(admins) == 1
    assert admins[0]["account"] == "newadmin"
    assert admins[0]["group"] == "Administrators"
    brute = find_brute_force(events)
    assert [item["source_ip"] for item in brute] == ["203.0.113.10"]


def test_triage_keeps_the_synthetic_label():
    report = triage(SAMPLES / "auth.log", SAMPLES / "windows-security.csv")
    assert report["data_label"] == "synthetic-lab-sample"
    assert report["failed_logons"] >= 8
    assert report["brute_force"]
    assert report["new_admins"]
