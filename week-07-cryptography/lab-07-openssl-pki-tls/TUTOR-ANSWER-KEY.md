# Tutor answer key — Lab 07

Not part of the trainee PDF.

Two SHA-256 digests differ after one character changes. `server.crt` subject contains `lab-wazuh.home` and the issuer contains `Lab CA`, so `self_signed_name` is false. The CA certificate itself is self-named. Neither fact means the laptop trusts the CA. A browser warning is the expected result.

Private keys stay in `$HOME/lab-07-work`. The unit test creates keys only in a temporary directory.

TLS is per application session. IPsec is per IP packet and often a tunnel. His explainer paragraph must be his words.
