"""Put each week's Python project on the import path for pytest."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

PROJECTS = [
    ROOT / "week-01-foundations" / "lab-01-risk-register-and-cia",
    ROOT / "week-02-tcp-ip-networking" / "addressing-practice",
    ROOT / "week-03-systems-and-hardening" / "hardening-audit",
    ROOT / "week-05-application-security" / "secure-code-review",
    ROOT / "week-06-database-security" / "database-security-checklist",
    ROOT / "week-07-cryptography" / "encryption-hashing-practice",
    ROOT / "week-07-cryptography" / "certificate-inspection",
    ROOT / "week-08-identity-access-management" / "password-mfa-policy",
    ROOT / "week-11-ai-soc-automation" / "compliance-automation",
    ROOT / "week-11-ai-soc-automation" / "soc-alert-triage",
    ROOT / "week-11-ai-soc-automation" / "sigma-rules",
    ROOT / "week-11-ai-soc-automation" / "threat-intel-summary",
    ROOT / "week-12-incident-response-capstone" / "mock-assessment",
]

for project in PROJECTS:
    entry = str(project)
    if entry not in sys.path:
        sys.path.insert(0, entry)
