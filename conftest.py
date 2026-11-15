"""Put each scaffold exercise on the import path for pytest.

The exercises under bootcamp-materials are course worksheets, not portfolio findings.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "bootcamp-materials"

PROJECTS = [
    BASE / "week-01-foundations" / "lab-01-risk-register-and-cia",
    BASE / "week-02-tcp-ip-networking" / "addressing-practice",
    BASE / "week-03-systems-and-hardening" / "hardening-audit",
    BASE / "week-05-application-security" / "secure-code-review",
    BASE / "week-06-database-security" / "database-security-checklist",
    BASE / "week-07-cryptography" / "encryption-hashing-practice",
    BASE / "week-07-cryptography" / "certificate-inspection",
    BASE / "week-08-identity-access-management" / "password-mfa-policy",
    BASE / "week-11-ai-soc-automation" / "compliance-automation",
    BASE / "week-11-ai-soc-automation" / "soc-alert-triage",
    BASE / "week-11-ai-soc-automation" / "sigma-rules",
    BASE / "week-11-ai-soc-automation" / "threat-intel-summary",
    BASE / "week-12-incident-response-capstone" / "mock-assessment",
]

for project in PROJECTS:
    entry = str(project)
    if entry not in sys.path:
        sys.path.insert(0, entry)
