from crypto_practice import (
    decrypt_text,
    encrypt_text,
    hash_password,
    hmac_sha256,
    new_fernet_key,
    sha256_bytes,
    signatures_match,
    verify_password,
)


def test_sha256_is_stable():
    assert sha256_bytes(b"lab") == sha256_bytes(b"lab")
    assert sha256_bytes(b"lab") != sha256_bytes(b"Lab")


def test_hmac_changes_when_key_changes():
    first = hmac_sha256(b"key-a", b"alert")
    second = hmac_sha256(b"key-b", b"alert")
    assert first != second
    assert signatures_match(first, hmac_sha256(b"key-a", b"alert"))
    assert not signatures_match(first, second)


def test_password_hash_uses_salt_and_verifies():
    stored = hash_password("correct horse battery")
    again = hash_password("correct horse battery")
    assert stored != again
    assert verify_password("correct horse battery", stored)
    assert not verify_password("wrong horse battery", stored)
    assert not verify_password("correct horse battery", "not-a-hash")


def test_fernet_round_trip():
    key = new_fernet_key()
    token = encrypt_text(key, "ticket 15 is confidential")
    assert token != b"ticket 15 is confidential"
    assert decrypt_text(key, token) == "ticket 15 is confidential"
