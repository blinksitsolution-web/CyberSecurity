# Input validation

## Goal

Review how a training app should treat input. Tuesday's assignment is a short findings note. The runnable checks live in `../secure-code-review/safe_input.py` so there is one implementation to test.

## What was built

`findings.md` explains allow-listing and leaves a table for your sandbox notes. `is_safe_username` and `parse_positive_id` are the reference behaviour: a username is a short token, and an id is a positive integer with no extra characters.

## How to reproduce

1. Read `safe_input.py` and run `pytest` from the secure-code-review folder.
2. In `findings.md`, record one input you expected to accept and one you expected to reject.
3. If your class sandbox uses a different rule, write that rule down and say how it differs. Do not weaken the tests to match a guess.

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
