import shutil
import subprocess
from pathlib import Path


def test_openssl_lab_ca_issues_a_server_certificate(tmp_path: Path):
    openssl = shutil.which("openssl")
    assert openssl
    work = tmp_path / "work"
    work.mkdir()
    subprocess.run([openssl, "genrsa", "-out", "ca.key", "2048"], cwd=work, check=True, capture_output=True)
    subprocess.run(
        [openssl, "req", "-x509", "-new", "-nodes", "-key", "ca.key", "-sha256", "-days", "30", "-subj", "/CN=Lab CA", "-out", "ca.crt"],
        cwd=work,
        check=True,
        capture_output=True,
    )
    subprocess.run([openssl, "genrsa", "-out", "server.key", "2048"], cwd=work, check=True, capture_output=True)
    subprocess.run(
        [openssl, "req", "-new", "-key", "server.key", "-subj", "/CN=lab-wazuh.home", "-out", "server.csr"],
        cwd=work,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [openssl, "x509", "-req", "-in", "server.csr", "-CA", "ca.crt", "-CAkey", "ca.key", "-CAcreateserial", "-out", "server.crt", "-days", "30", "-sha256"],
        cwd=work,
        check=True,
        capture_output=True,
    )
    subject = subprocess.run(
        [openssl, "x509", "-in", "server.crt", "-noout", "-subject", "-issuer"],
        cwd=work,
        check=True,
        capture_output=True,
        text=True,
    )
    text = subject.stdout
    assert "lab-wazuh.home" in text
    assert "Lab CA" in text
    assert not (Path(__file__).resolve().parent / "ca.key").exists()
