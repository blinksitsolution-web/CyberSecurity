# Secure code review

## Goal

Finish a safe review and present the fixes. This is Friday's weekly deliverable. It pulls the week's notes into one report and holds the code the tests run.

## What was built

- `safe_input.py` — HTML encoding, username checks, and positive ids.
- `test_safe_input.py` — the checks you can re-run.
- `review-report.md` — a findings table. The first row records the teaching fix already in `safe_input.py`. Further rows are blank.

The unsafe patterns are described in the report as review notes. There is no vulnerable server in this folder.

## How to reproduce

```bash
python3 -m pytest test_safe_input.py
python3 safe_input.py '<b>hello</b>'
```

You should see the angle brackets encoded. Then fill the report with anything else you reviewed in the class sandbox, clearly labelled as class sandbox or as this repo.

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
