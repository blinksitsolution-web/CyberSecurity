#!/usr/bin/env python3
"""Week 7 practice: hashing, HMAC, password hashing, and Fernet encryption.

Uses the standard library and the cryptography package. It does not invent
a cipher. Password storage uses scrypt, not a single fast hash.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import os
from pathlib import Path

from cryptography.fernet import Fernet


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def hmac_sha256(key: bytes, message: bytes) -> str:
    return hmac.new(key, message, hashlib.sha256).hexdigest()


def signatures_match(expected_hex: str, actual_hex: str) -> bool:
    """Compare two hex digests without stopping at the first difference."""
    return hmac.compare_digest(expected_hex, actual_hex)


def hash_password(password: str, salt: bytes | None = None) -> str:
    """Return a stored scrypt string. A new random salt is used by default."""
    if salt is None:
        salt = os.urandom(16)
    # n=2**14 is comfortable for this exercise. Follow current guidance for production.
    n, r, p = 2**14, 8, 1
    digest = hashlib.scrypt(password.encode("utf-8"), salt=salt, n=n, r=r, p=p, dklen=32)
    return f"scrypt${n}${r}${p}${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        scheme, n_text, r_text, p_text, salt_hex, digest_hex = stored.split("$")
    except ValueError:
        return False
    if scheme != "scrypt":
        return False
    digest = hashlib.scrypt(
        password.encode("utf-8"),
        salt=bytes.fromhex(salt_hex),
        n=int(n_text),
        r=int(r_text),
        p=int(p_text),
        dklen=len(bytes.fromhex(digest_hex)),
    )
    return hmac.compare_digest(digest.hex(), digest_hex)


def new_fernet_key() -> bytes:
    return Fernet.generate_key()


def encrypt_text(key: bytes, plaintext: str) -> bytes:
    return Fernet(key).encrypt(plaintext.encode("utf-8"))


def decrypt_text(key: bytes, token: bytes) -> str:
    return Fernet(key).decrypt(token).decode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Print the SHA-256 of a file")
    parser.add_argument("path")
    args = parser.parse_args()
    print(sha256_file(Path(args.path)))


if __name__ == "__main__":
    main()
