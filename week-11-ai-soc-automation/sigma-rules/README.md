# Sigma rules

## Goal

Write a few detection rules a SIEM can share, and map each one to MITRE ATT&CK. Sigma is a vendor-neutral rule format. These four rules are lab rules for the sample logs. They are not tuned for a production SOC, and this checker does not implement the full Sigma specification.

## What was built

| Rule file | What it selects | ATT&CK |
| --- | --- | --- |
| `rules/linux-ssh-failed-password.yml` | SSH failed-password lines | T1110.001 Password Guessing |
| `rules/linux-user-added-to-sudo.yml` | An account added to `sudo` | T1098 Account Manipulation |
| `rules/windows-failed-logon-4625.yml` | Windows event 4625 | T1110 Brute Force |
| `rules/windows-admin-group-4732.yml` | Event 4732 for the Administrators group | T1098 Account Manipulation |

`sigma_check.py` requires a title, id, status, description, log source, detection, level, and an `attack.t####` tag.

The Linux failed-password rule selects the event. The threshold of five failures in ten minutes lives in `log_triage.py`, because a one-line keyword rule does not count. Say that clearly if you present the rule.

## How to reproduce

```bash
python3 -m pytest test_sigma_check.py
python3 sigma_check.py rules/*.yml
```

The rule author is James Ackah Blay. If you convert a rule for Wazuh, follow the current Wazuh or Sigma documentation and keep the converted rule next to the evidence of a log you actually collected. Do not claim a detection fired unless your dashboard showed it.

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
