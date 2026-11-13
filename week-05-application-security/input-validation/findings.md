# Input-validation notes

## Rule in this repo

- Usernames match `^[A-Za-z][A-Za-z0-9._-]{2,31}$`. They start with a letter and stay short.
- Ids match a positive integer such as `15`, not `0`, not `-3`, and not `12abc`.
- Rejecting a string is different from encoding it. Validation decides whether the value is acceptable. Encoding makes a value safe to display.

## What I tried

| Input | I expected | What the function did | Notes |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

## Unsafe pattern to reject in review

Building a sentence, a file path, or a query by gluing raw input into the middle of it. The safe pattern is: check the shape, then pass the value as data.

Your extra finding from class, if you have one:
