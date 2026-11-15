# Workstation baseline checklist

## Goal

Write the secure configuration you want on a training workstation, then use it as the standard you audit against. Tuesday drafts it. Wednesday applies it. Friday validates it.

## What was built

`baseline-checklist.csv` is a starter baseline for the Ubuntu lab server and the Windows endpoint. Every row begins as `not-checked`. A pass in this file is something you have seen yourself.

The checklist is original study material inspired by common hardening themes. It is not a copy of the CIS Benchmarks, and ticking every box does not certify the machine.

## How to reproduce

1. For each row, do the check on your VM or write why it does not apply.
2. Put the status in the `status` column: `pass`, `gap`, `not-applicable`, or leave `not-checked`.
3. Point `evidence` at a file or a command you actually ran.
4. Use the read-only audit in the next folder for the Linux rows it knows how to read. The script does not replace this checklist.

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
