# Week 7 assignment — cryptography fundamentals

**Source:** Maxim Nyansa cybersecurity bootcamp, Week 7 assignment, received 16 November 2026.  
**Trainee:** James Ackah Blay.

The questions below are the assignment as set. Worked answers are in `ANSWERS.md`. The steps to reproduce them are in `STEP-BY-STEP.md`.

## Question 1 — Caesar cipher

Decrypt `XLMW MW E WIGVIX QIWWEKI`. Spaces stay unchanged.

## Question 2 — Security by obscurity

A company sells a cryptographic product and has a technical design document. The options are:

1. Publish the document publicly.
2. Share it with paying customers under a non-disclosure agreement.
3. Keep it secret even from customers.

Give at least two arguments in favour of each option.

## Question 3 — Symmetric and asymmetric encryption

Give at least two advantages of asymmetric encryption over symmetric encryption, and at least one advantage of symmetric encryption over asymmetric encryption.

## Question 4 — Classify five attacks

For each attack, name the setting (known plaintext, chosen plaintext, chosen ciphertext, or none needed) and the methodology (key brute force, cryptanalytic, or circumventing an otherwise secure cipher).

1. EFF DES cracker — <https://www.eff.org/press/releases/eff-des-cracker-machine-brings-honesty-crypto-debate>
2. RC4 "Bar Mitzvah" — <https://blackhat.com/docs/asia-15/materials/asia-15-Mantin-Bar-Mitzvah-Attack-Breaking-SSL-With-13-Year-Old-RC4-Weakness-wp.pdf>
3. CRIME — <https://arstechnica.com/information-technology/2012/09/crime-hijacks-https-sessions/>
4. ROBOT — <https://robotattack.org/>
5. Windows Group Policy Preferences password decryption — <https://adsecurity.org/?p=384>

## Question 5 — Breaking ECB

A server computes AES-ECB(K, P || S || zero-padding to 16) for an attacker-chosen prefix P, a fixed unknown secret S, and a fixed unknown key K. The attacker may query the server as many times as they like. Devise an attack that recovers S.
