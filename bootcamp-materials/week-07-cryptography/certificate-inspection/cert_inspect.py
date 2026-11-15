#!/usr/bin/env python3
"""Inspect a PEM certificate, or write a public lab certificate.

The private key for --generate-public stays in memory and is not written.
Do not commit private keys.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def generate_public_cert(path: Path, common_name: str = "lab-wazuh.home", days: int = 30) -> None:
    """Write a self-signed certificate. The matching private key is discarded."""
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, common_name)])
    now = datetime.now(timezone.utc)
    certificate = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(minutes=5))
        .not_valid_after(now + timedelta(days=days))
        .add_extension(
            x509.SubjectAlternativeName([x509.DNSName(common_name)]),
            critical=False,
        )
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .sign(key, hashes.SHA256())
    )
    path.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))


def inspect_certificate(path: Path) -> dict:
    certificate = x509.load_pem_x509_certificate(Path(path).read_bytes())
    sans: list[str] = []
    try:
        extension = certificate.extensions.get_extension_for_class(x509.SubjectAlternativeName)
        sans = extension.value.get_values_for_type(x509.DNSName)
    except x509.ExtensionNotFound:
        sans = []
    algorithm = certificate.signature_hash_algorithm
    now = datetime.now(timezone.utc)
    return {
        "subject": certificate.subject.rfc4514_string(),
        "issuer": certificate.issuer.rfc4514_string(),
        "serial": str(certificate.serial_number),
        "not_before": certificate.not_valid_before_utc.isoformat(),
        "not_after": certificate.not_valid_after_utc.isoformat(),
        "currently_valid": certificate.not_valid_before_utc <= now <= certificate.not_valid_after_utc,
        "self_signed_name": certificate.subject == certificate.issuer,
        "sans": sans,
        "signature_hash": algorithm.name if algorithm else None,
        "note": "self_signed_name only compares subject and issuer. It is not a trust decision.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect or create a public lab certificate")
    parser.add_argument("path", type=Path)
    parser.add_argument("--generate-public", action="store_true")
    parser.add_argument("--common-name", default="lab-wazuh.home")
    args = parser.parse_args()
    if args.generate_public:
        generate_public_cert(args.path, args.common_name)
        print(f"Wrote public certificate to {args.path}. No private key was saved.")
    print(json.dumps(inspect_certificate(args.path), indent=2))


if __name__ == "__main__":
    main()
