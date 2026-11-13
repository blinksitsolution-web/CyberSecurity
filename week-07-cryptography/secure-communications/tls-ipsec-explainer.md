# TLS, IPsec, and a small demo

## Data in transit

Encryption at rest protects a file on a disk. Encryption in transit protects bytes on a path between two programs. You usually want both when the data is sensitive. They fail in different places: a stolen laptop, or a network you do not control.

## TLS

TLS wraps an application protocol. HTTPS is HTTP inside TLS. The server presents a certificate. The client checks the name, the dates, and whether it trusts the issuer. The two sides then share keys for the session. You can explain that much without describing an attack against the handshake.

What you can show in this lab:

1. Generate `lab-wazuh.crt` with `cert_inspect.py`.
2. Show that the subject and issuer match, so the name is self-signed.
3. Say, out loud, that a browser should warn on that certificate unless you have chosen to trust it for the lab.
4. Show the not-after date, and say what you will do when it passes.

## IPsec

IPsec protects IP packets. It can authenticate and encrypt traffic between networks or hosts, often as a VPN. TLS is tied to one application session, such as a browser and a site. IPsec is tied to the IP layer and can cover many applications once the tunnel exists. Neither replaces the other in every design. A SOC note cares about where the tunnel ends, because logs on the far side may see the inner addresses and logs in the middle may only see the tunnel.

## Mini demo checklist

| Step | Done? | What you showed |
| --- | --- | --- |
| Public certificate generated or a real lab certificate inspected |  |  |
| Subject, issuer, dates, and SAN read out |  |  |
| One sentence on why self-signed is a lab choice |  |  |
| One sentence on TLS versus IPsec |  |  |

## In my own words

Replace this paragraph. Two to five sentences are enough.
