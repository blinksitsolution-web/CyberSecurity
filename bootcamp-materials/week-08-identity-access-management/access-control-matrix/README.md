# Access-control matrix

## Goal

Translate job roles into the minimum permissions, and compare role-based access with attribute-based access. Wednesday and Thursday's assignments meet in this matrix.

## What was built

`access-matrix.csv` covers a small SOC-style team: analyst, senior analyst, and platform admin. Cells are `allow` or `deny`. A note column says whether a real system would also look at an attribute such as time or on-call status.

Separation of duties: the person who asks for a new admin account is not the only person who approves it.

## How to reproduce

1. Read the matrix and change a cell only with a sentence in the note.
2. Add yourself as a named person only if you want that in a public repository. Role names are enough.
3. Write one ABAC example in the README evidence lines: a rule that depends on context, not only on the job title.

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
