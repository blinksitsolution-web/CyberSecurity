# Hardening audit

## Goal

Check a training workstation without changing it. The script reports pass, fail, review, or skip. Skip means the file was not there to read. Skip is not a pass.

## What was built

- `hardening_audit.py` reads a Linux-style tree. It never writes.
- `audit-windows.ps1` prints Windows firewall, Defender, password-policy, and SMBv1 state. It does not change them.
- `test_hardening_audit.py` builds a fake tree and checks the results.

The Linux checks cover SSH root login, SSH passwords, `passwd` and `shadow` permissions, world-writable files under `home`, and `PASS_MAX_DAYS`.

## How to reproduce

From this folder:

```bash
python3 -m pytest test_hardening_audit.py
python3 hardening_audit.py --root /
```

On the Ubuntu VM, `--root /` reads the live machine. Save the text in `evidence/ubuntu-audit.txt`. On Windows, in PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\audit-windows.ps1
```

Save that output yourself. This repository was not run on your Windows VM, so it contains no Windows results.

If a check says review, write the decision in the baseline checklist. A lab may keep password SSH. Root login should still be off.

## Evidence to add yourself

Do not invent results. Fill these lines only with what you did.

- Date completed:
- What you did:
- File in `evidence/`:
- Feedback:

## What I learned

Answer in your own words.

1. What was this deliverable for?
2. What is finished, and what is still open?
3. What is clearer than it was at the start of the week?
4. What would you do on a SOC shift because of this?
5. Which evidence file is yours?
