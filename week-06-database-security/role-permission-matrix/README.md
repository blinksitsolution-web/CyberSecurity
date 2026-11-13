# Role and permission matrix, and recovery plan

## Goal

Give each job the smallest set of actions that still lets the work happen, and write how you would recover the database. Wednesday builds the matrix. Friday reviews recovery. The weekly submission pairs them.

## What was built

- `permission-matrix.csv` — analyst, admin, and dba against a few actions. The demo code enforces the same yes/no values.
- `recovery-plan.md` — a plan with blanks for the backup you have actually tested.

`export_all_customers` is denied for every role on purpose. That export is not a normal job.

## How to reproduce

1. Read the matrix beside `../database-security-checklist/db_access.py`.
2. Change a cell only if you also change the seed data and the test, and you can explain the new job need.
3. Fill the recovery plan. Leave the test-restore result blank until you have done it.

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
