# Certificate inspection

## Goal

Inspect a certificate's subject, issuer, dates, and names. Thursday's exercise is this inspection. Trust is a separate question: a certificate can be well formed and still be the wrong one to trust.

## What was built

`cert_inspect.py` can write a **public** self-signed certificate for `lab-wazuh.home` and print the fields. The private key is kept in memory and is not written. `self_signed_name` only means the subject and issuer strings match. The script says so in its output.

## How to reproduce

```bash
python3 cert_inspect.py lab-wazuh.crt --generate-public --common-name lab-wazuh.home
```

Read the JSON. Check the dates, the common name, and the subject alternative name. Then delete `lab-wazuh.crt` or keep it as a public file. Do not go looking for a matching private key. There is not one on disk.

If your trainer gives you a public certificate from the lab dashboard, point the script at that file instead and save the JSON you received.

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
