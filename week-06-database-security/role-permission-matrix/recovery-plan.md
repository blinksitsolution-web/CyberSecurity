# Database recovery plan

- System this plan is for:
- Where the backup is stored:
- How often it is taken:
- Who can read the backup:
- Encryption decision:

## Steps to practise

Write the commands you were taught for your engine. If you have not run them, leave the command lines blank and say so.

1. Confirm you are on the lab database, not a shared server.
2. Take a backup.
3. Make a harmless change you can afford to lose, such as a row in a copy.
4. Restore into a **copy**, not over the only good file, the first time you try.
5. Check a row you expected to see.

## Result

- Date of the last restore test:
- Did the row match?
- What you would do if the backup file itself was the thing that failed:

## What this plan does not cover

A deleted production database you do not own. This plan is for your lab engine and class exercises.
