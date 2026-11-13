# Tutor answer key — Lab 06

Not part of the trainee PDF.

`counter` has `SELECT` and `INSERT` on `orders` and is not a superuser. `DROP TABLE` as `counter` is denied. The restored database `palmcourt_restore` contains `(1, notebook)` until he drops that copy.

`sql_log_review.py` flags one line: the statement that concatenates a tautology. The parameterised `INSERT` with `$1` is not flagged. He should not replay the flagged statement in `psql`.

Passwords stay out of git. A missing PostgreSQL install meets the lab only if the recovery plan says the commands were not run.
