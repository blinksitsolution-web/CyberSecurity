# Lab key-management policy

- Owner of this policy: [Your name]
- Applies to: the home lab and this repository
- Date:

## Decisions

| Topic | Rule |
| --- | --- |
| What counts as a key or secret | Passwords, VM keys, API tokens, dashboard passwords, and private keys. Public certificates are not secret. |
| Where secrets live | [Write the place. A password manager is a reasonable default. A slide deck is not.] |
| Where secrets must not live | Git, screenshots, class chat, and prompts to a public AI tool |
| Who can read them |  |
| How a lab key is created | Use the tool's generator, as `Fernet.generate_key` and `cert_inspect.py` do. Do not make up a short password and call it a key |
| How long a lab certificate is valid | The practice script defaults to 30 days. Your choice: |
| Rotation | Replace a secret if it is exposed, if a teammate who knew it leaves the team, or at the end of the bootcamp |
| Retirement | Delete the old copy you control, and note the date. You cannot delete a copy someone else already has |

## Data at rest and in transit

- At rest, prefer disk encryption for any laptop that holds personal data. Record the decision for the lab VM even if you leave the VM disk unencrypted because it holds no personal data.
- In transit, use TLS for dashboards and logins. Week 7's explainer is the companion note.
- SSH private keys stay on the laptop. `PermitRootLogin no` from Week 3 still applies.

## Exception

An exception needs a name, a reason, and an end date. "It was quicker" is not an exception.
