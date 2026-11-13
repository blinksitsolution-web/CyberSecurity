# Password and MFA policy

## Goal

Write password and MFA rules for the lab, and map a simple single sign-on picture. Tuesday's assignment includes this policy. The checker only tests a password you type against those rules. It does not guess passwords.

## What was built

- `policy.md` — the policy template.
- `password_policy.py` — length, a mix of character types, a tiny banned list of obvious examples, and a username check.
- `test_password_policy.py` — three cases.

The banned list is not a cracking wordlist. It exists so a password such as `changeme` fails in the unit test.

## How to reproduce

```bash
python3 -m pytest test_password_policy.py
python3 password_policy.py --password 'Harbour-Lab-2026!' --username analyst
```

Use a password you can discard. Do not put a real account password in the command line if your shell history is shared. Fill the MFA section of the policy even if the lab VMs only have passwords today. The policy can say "MFA is required for the dashboard once it is available" without pretending it is already on.

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
