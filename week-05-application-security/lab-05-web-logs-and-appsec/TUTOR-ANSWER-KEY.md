# Tutor answer key — Lab 05

Not part of the trainee PDF.

`safe_input.py '<b>hello</b>'` prints encoded angle brackets. The tests pass.

`web_log_review.py samples/access.log` flags two lines, both `search` requests that contain a script tag either raw or percent-encoded. `/health`, the ordinary `notebook` search, and `app.css` are not flagged.

The impact sentence: untrusted text placed into HTML can run as a script in the reader's browser. The fix in this repo is encoding on the way out. Do not expect a list of further requests. Juice Shop, if used, must show `127.0.0.1:3000` and then be stopped. No challenge solutions are required or provided.
