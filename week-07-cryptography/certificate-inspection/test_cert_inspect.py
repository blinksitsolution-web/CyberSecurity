from cert_inspect import generate_public_cert, inspect_certificate


def test_generated_cert_is_public_and_self_named(tmp_path):
    path = tmp_path / "lab.crt"
    generate_public_cert(path, "lab-wazuh.home", days=30)
    text = path.read_text()
    assert "BEGIN CERTIFICATE" in text
    assert "PRIVATE KEY" not in text
    info = inspect_certificate(path)
    assert info["self_signed_name"] is True
    assert info["currently_valid"] is True
    assert "lab-wazuh.home" in info["sans"]
    assert "CN=lab-wazuh.home" in info["subject"]
    assert info["signature_hash"] == "sha256"
