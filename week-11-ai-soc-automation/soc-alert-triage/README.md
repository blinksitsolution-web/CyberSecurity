# SOC alert triage

## Goal

Automate the first sort of two lab detections: a burst of failed logons from one source, and a new member of an administrator group. Tuesday's assignment is the SOC alarm prototype. The cyber kill chain is used here as a label for where the alert sits, not as a set of steps to carry out.

## What was built

- `samples/auth.log` — synthetic syslog. Six failures from `203.0.113.10`, two from `198.51.100.8`, and `newadmin` added to `sudo`.
- `samples/windows-security.csv` — synthetic Security events. Five 4625s from `203.0.113.10`, one from another address, and 4732 adding `newadmin` to Administrators. A Backup Operators change is present so it does not alert.
- `log_triage.py` — the parser. Default threshold is 5 failures inside 10 minutes.
- `test_log_triage.py` — expected findings for those files.

`203.0.113.0/24` and `198.51.100.0/24` are documentation ranges. They are not machines for you to contact.

Brute force is mapped to ATT&CK technique T1110. A new admin group member is mapped to T1098. The Sigma rules in the next folder select the same events. This script applies the threshold.

## How to reproduce

```bash
python3 -m pytest test_log_triage.py
python3 log_triage.py --auth-log samples/auth.log --windows-csv samples/windows-security.csv
```

The JSON field `data_label` stays `synthetic-lab-sample` unless you pass `--label`. When you point the script at an export from your VM, set the label to something like `my-lab` and strip personal data before you commit the file.

Kill-chain placement, for the write-up: failed logons are an attempt to gain access. Adding an admin account is a way to keep access. You are detecting those behaviours, not performing them.

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
