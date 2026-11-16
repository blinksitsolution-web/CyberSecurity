#!/usr/bin/env python3
"""Local byte-at-a-time demonstration against AES-ECB.

The oracle lives in this process. It uses a random key and a fictional secret.
It does not open a socket. ECB is used only to show why that mode fails.
Do not use ECB for real data.
"""

from __future__ import annotations

import argparse
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

BLOCK = 16


def zero_pad(data: bytes) -> bytes:
    """Pad with zero bytes so the length is a multiple of the AES block."""
    extra = (-len(data)) % BLOCK
    return data + b"\x00" * extra


def aes_ecb_encrypt(key: bytes, data: bytes) -> bytes:
    """Encrypt already padded data. ECB is intentional and unsafe."""
    padded = zero_pad(data)
    # Teaching use of ECB. A real system should use an AEAD mode such as GCM.
    encryptor = Cipher(algorithms.AES(key), modes.ECB()).encryptor()  # NOSONAR
    return encryptor.update(padded) + encryptor.finalize()


class EcbOracle:
    """AES-ECB(K, attacker_prefix || secret || zero padding)."""

    def __init__(self, secret: bytes, key: bytes | None = None) -> None:
        if not isinstance(secret, bytes):
            raise TypeError("secret must be bytes")
        self.secret = secret
        self.key = key if key is not None else os.urandom(BLOCK)

    def encrypt(self, chosen_prefix: bytes) -> bytes:
        if not isinstance(chosen_prefix, bytes):
            raise TypeError("prefix must be bytes")
        return aes_ecb_encrypt(self.key, chosen_prefix + self.secret)


def discover_block_size(oracle: EcbOracle) -> int:
    """Grow the prefix until the ciphertext gains one block."""
    base = len(oracle.encrypt(b""))
    for added in range(1, 64):
        grown = len(oracle.encrypt(b"A" * added))
        if grown > base:
            return grown - base
    raise RuntimeError("could not detect the block size")


def secret_length(oracle: EcbOracle, block_size: int) -> int:
    """How many secret bytes sit under the zero padding.

    Zero padding hides its own length if you only strip trailing NUL bytes.
    Watching when the ciphertext grows tells us how many pad bytes were added,
    so a real 0x00 inside the secret is not thrown away.
    """
    base = len(oracle.encrypt(b""))
    for added in range(1, block_size + 1):
        if len(oracle.encrypt(b"A" * added)) > base:
            padding = added - 1
            return base - padding
    raise RuntimeError("could not measure the secret length")


def recover_secret(oracle: EcbOracle) -> bytes:
    """Recover the oracle secret one byte at a time."""
    block_size = discover_block_size(oracle)
    total = secret_length(oracle, block_size)
    known = b""
    for index in range(total):
        prefix_len = block_size - 1 - (len(known) % block_size)
        prefix = b"A" * prefix_len
        block_index = len(known) // block_size
        start = block_index * block_size
        end = start + block_size
        target = oracle.encrypt(prefix)[start:end]
        found = None
        for candidate in range(256):
            guess = oracle.encrypt(prefix + known + bytes([candidate]))[start:end]
            if guess == target:
                found = bytes([candidate])
                break
        if found is None:
            raise RuntimeError(f"no match at secret byte {index}")
        known += found
    return known


def main() -> None:
    parser = argparse.ArgumentParser(description="Recover a fictional ECB secret locally")
    parser.add_argument(
        "--secret",
        default="SECRETS",
        help="Fictional secret recovered by the local attack. Not a real key.",
    )
    args = parser.parse_args()
    secret = args.secret.encode("utf-8")
    oracle = EcbOracle(secret)
    recovered = recover_secret(oracle)
    print(f"block_size={BLOCK}")
    print(f"secret_length={len(secret)}")
    print(f"recovered={recovered!r}")
    print(f"match={recovered == secret}")
    print("The AES key stayed in this process and was not printed.")


if __name__ == "__main__":
    main()
