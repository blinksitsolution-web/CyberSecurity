# XSS review notes

## What goes wrong

A web page builds HTML from text a user supplied. The browser cannot tell the difference between the page the author wrote and markup hidden in that text. If the text is allowed to stay as markup, the browser may run it as a script in a victim's session. That is cross-site scripting. The impact is whatever the script can do in that page: read data the page can see, or act as the user.

## The fix in this repo

`escape_html` turns `&`, `<`, `>`, `"`, and `'` into entities before the text is placed in HTML. The browser then shows the characters instead of treating them as a tag. Encode for the context you are in. HTML body encoding is not the same job as encoding for a URL or for JavaScript.

A Content-Security-Policy header is a second layer. It tells the browser which scripts are allowed to run. It does not replace encoding.

## Review questions

Answer after you have read the function.

1. Why is `&` replaced before `<`?
2. What still goes wrong if you encode the text but then decode it again before displaying it?
3. Where would you look in a SOC ticket if a user reported a strange pop-up on a site your team owns?

Your answers:

1.
2.
3.
