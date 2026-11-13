from pathlib import Path

from timeline_check import check


def test_empty_template_is_not_ok():
    errors = check(Path(__file__).resolve().parent / "timeline.csv")
    assert errors == ["timeline has no filled rows yet"]


def test_order_and_missing_source(tmp_path: Path):
    path = tmp_path / "timeline.csv"
    path.write_text(
        "time_utc,action,source\n"
        "2026-12-21T09:00:00Z,Failed logons in auth.log,auth.log\n"
        "2026-12-21T08:00:00Z,Snapshot,VirtualBox\n",
        encoding="utf-8",
    )
    errors = check(path, root=tmp_path)
    assert any("backwards" in item for item in errors)

    path.write_text(
        "time_utc,action,source\n"
        "2026-12-21T09:00:00Z,Snapshot,VirtualBox before-lab-12\n"
        "2026-12-21T09:20:00Z,Removed lab12user,command output\n",
        encoding="utf-8",
    )
    assert check(path, root=tmp_path) == []
