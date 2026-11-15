# Cross-site scripting awareness

## Goal

Recognise reflected cross-site scripting and name the safeguard. Wednesday's lab is a review in a safe sandbox, not a hunt across websites you do not own.

## What was built

`review-notes.md` explains the failure in plain language and points at `escape_html` in `../secure-code-review/safe_input.py`. The unit test uses a well-known teaching string and checks that the encoded result no longer contains raw angle brackets.

This folder does not contain a page that reflects input, a browser exploit, or a list of payloads.

## How to reproduce

1. Read the notes.
2. Run the safe-input tests and look at the assertion for `escape_html`.
3. Write, in your own words, where encoding has to happen and what a Content-Security-Policy header adds.
4. If your trainer shows a local sandbox, record what you saw in the evidence lines. Do not point that sandbox at another person's site.

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
