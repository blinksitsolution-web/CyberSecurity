# Database security checklist

## Goal

Review injection risk and the countermeasures that belong in a beginner lab: least privilege, parameterised queries, and careful handling of sensitive data. Thursday's assignment is the checklist. Friday pairs it with the recovery plan.

## What was built

- `checklist.csv` — controls, all `not-reviewed` until you look.
- `db_access.py` — an in-memory SQLite database. Login uses `?` placeholders. A classic injection string is stored and compared as text, so it does not become SQL.
- `test_db_access.py` — proves the safe login rejects that string, and that the analyst role cannot create users.

The README does not include a function that concatenates input into a query. The failure mode to remember is: if the application builds SQL by gluing strings together, the database may treat user text as commands. The fix in this folder is to keep user text in parameters.

## How to reproduce

```bash
python3 -m pytest test_db_access.py
python3 db_access.py --role analyst --action create_user
```

The second command should print `deny`. Then set checklist rows to `met` only where a test or your class database shows the control. The sample code is not a finding about a company.

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
