# Model notes

| Model | How data hangs together | A beginner example |
| --- | --- | --- |
| Relational | Tables, rows, columns, and keys | Users, tickets, and a role column |
| Document | A document, often JSON, stored as a unit | One ticket with its comments inside it |
| Key-value | A key and a blob of value | A session id and the session data |

A DBMS is the software that stores the data, checks constraints, controls who can ask questions, and recovers after a crash. The database is the collection of data. The two words are easy to swap in conversation. In a report, keep them apart.

## Lab ticket map

Fill the columns. Leave a cell blank rather than inventing a column you do not need.

| Table | What one row is | Primary key | What it must not lose |
| --- | --- | --- | --- |
| users |  |  |  |
| tickets |  |  |  |
| permissions |  |  |  |

The demo in the security-checklist folder already creates `users` and `permissions` in memory so the tests have something to query.
