import os
import stat

from hardening_audit import audit


def _write(path, text, mode=0o644):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    os.chmod(path, mode)


def test_fail_and_pass_are_read_from_files(tmp_path):
    _write(
        tmp_path / "etc" / "ssh" / "sshd_config",
        "PermitRootLogin yes\nPasswordAuthentication yes\n",
    )
    _write(tmp_path / "etc" / "passwd", "root:x:0:0:root:/root:/bin/bash\n", 0o644)
    _write(tmp_path / "etc" / "shadow", "root:!:1:0:99999:7:::\n", 0o644)
    _write(tmp_path / "etc" / "login.defs", "PASS_MAX_DAYS 90\n")
    home = tmp_path / "home" / "analyst"
    _write(home / "notes.txt", "lab", 0o666)

    before = sorted(p.relative_to(tmp_path).as_posix() for p in tmp_path.rglob("*"))
    checks = {item.check_id: item for item in audit(tmp_path)}
    after = sorted(p.relative_to(tmp_path).as_posix() for p in tmp_path.rglob("*"))

    assert before == after
    assert checks["ssh-permit-root"].status == "fail"
    assert checks["ssh-password-auth"].status == "review"
    assert checks["shadow-not-world-readable"].status == "fail"
    assert checks["passwd-not-world-writable"].status == "pass"
    assert checks["home-world-writable"].status == "fail"
    assert checks["pass-max-days"].status == "pass"


def test_hardened_fixture_passes_root_and_shadow(tmp_path):
    _write(
        tmp_path / "etc" / "ssh" / "sshd_config",
        "# comment\nPermitRootLogin no\nPasswordAuthentication no\n",
    )
    _write(tmp_path / "etc" / "shadow", "root:!:*\n", 0o640)
    _write(tmp_path / "home" / "analyst" / "notes.txt", "lab", 0o640)
    checks = {item.check_id: item for item in audit(tmp_path)}
    assert checks["ssh-permit-root"].status == "pass"
    assert checks["ssh-password-auth"].status == "pass"
    assert checks["shadow-not-world-readable"].status == "pass"
    assert checks["home-world-writable"].status == "pass"


def test_missing_files_are_skips(tmp_path):
    checks = {item.check_id: item for item in audit(tmp_path)}
    assert checks["ssh-permit-root"].status == "skip"
    assert checks["shadow-not-world-readable"].status == "skip"
    assert checks["home-world-writable"].status == "skip"
    assert stat.S_IWOTH  # imported permission bit stays available for the script
