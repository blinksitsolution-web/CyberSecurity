# Application review report

- Reviewer: [Your name]
- Date:
- In scope: `safe_input.py` and the class sandbox you name here
- Out of scope: any system you do not have permission to test

## Findings

| ID | Where | Issue | Impact | Fix | Status |
| --- | --- | --- | --- | --- | --- |
| F-01 | `escape_html` in this folder | Untrusted text must not be inserted into HTML as raw markup | A script in that text can run in the reader's browser | Encode the five HTML characters before display. Covered by `test_safe_input.py` | Fixed in the sample code |
| F-02 |  |  |  |  |  |
| F-03 |  |  |  |  |  |

F-01 is a description of the sample fix. It is not a vulnerability you found on a running site.

## Fixes I would show the class

1. Validate shape with an allow-list where you can.
2. Encode on the way out, for the context you are in.
3. Fail closed on configuration: no debug errors, no default passwords, no secrets in git.

## Class sandbox notes

Sandbox name, if your trainer provided one:

What you were allowed to do:

What you saw:
