"""Put the Week 7 assignment on the import path for pytest."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSIGNMENT = ROOT / "week-07-cryptography" / "assignment-01-crypto-fundamentals"
if str(ASSIGNMENT) not in sys.path:
    sys.path.insert(0, str(ASSIGNMENT))
