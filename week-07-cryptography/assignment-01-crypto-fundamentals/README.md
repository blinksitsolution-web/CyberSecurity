# Assignment 01 — Cryptography fundamentals

Worked solution and local exercises for the Maxim Nyansa bootcamp Week 7 assignment, 16 November 2026. Trainee: James Ackah Blay.

The questions are in [ASSIGNMENT.md](ASSIGNMENT.md). The study answers are in [ANSWERS.md](ANSWERS.md). The guide to run everything is [STEP-BY-STEP.md](STEP-BY-STEP.md), also built as [LAB-07b-crypto-assignment.pdf](LAB-07b-crypto-assignment.pdf).

Command output in the guide describes what the scripts print. Screenshots are still placeholders until James captures his own terminal.

## Skills demonstrated

- Exhausting a Caesar cipher and recognising English.
- Applying Kerckhoffs's principle to a vendor design document.
- Comparing symmetric and asymmetric cryptography, including hybrid encryption.
- Classifying published breaks: DES brute force, RC4's Bar Mitzvah bias, CRIME, ROBOT, and Group Policy Preferences `cpassword`.
- Recovering a fictional secret from a local AES-ECB oracle, and seeing why zero padding confuses a naive trim of trailing zeros.

## Real-world relevance

| Topic | Where it shows up |
| --- | --- |
| Small keys fall to search | DES, 56-bit, EFF cracker (1998) |
| Stream-cipher bias | RC4 in TLS, Bar Mitzvah (Mantin, 2015) |
| Side channel beside a sound cipher | CRIME, TLS compression length |
| Padding oracle | ROBOT, RSA PKCS#1 v1.5 in TLS |
| Key shipped in the manual | ATT&CK T1552.006, Group Policy Preferences passwords |
| ECB repeats equal blocks | Disk and token formats that should have used an AEAD mode. ATT&CK T1600 covers weakening encryption |

Question 4 is classification only. This folder does not contain exploit code for CRIME, ROBOT, or `cpassword` decryption.

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd week-07-cryptography/assignment-01-crypto-fundamentals
python3 -m pytest test_caesar.py test_ecb_byte_at_a_time.py
python3 caesar.py brute "XLMW MW E WIGVIX QIWWEKI"
python3 ecb_byte_at_a_time.py --secret SECRETS
```

Rebuild the PDF, if Pandoc and WeasyPrint are installed:

```bash
python3 build_pdf.py
```

## Links

- Assignment questions: [ASSIGNMENT.md](ASSIGNMENT.md)
- Answers: [ANSWERS.md](ANSWERS.md)
- Trainee steps: [STEP-BY-STEP.md](STEP-BY-STEP.md) and [LAB-07b-crypto-assignment.pdf](LAB-07b-crypto-assignment.pdf)
- Earlier Week 7 writing: [Cryptography and secure web questions](../cryptography-and-secure-web-qa/)
