# Encryption and hashing practice

## Goal

Compare hashing, a message authentication code, password hashing, and symmetric encryption by running them. Monday is encryption practice. Wednesday is hashing. Use the libraries. Do not invent a cipher.

## What was built

`crypto_practice.py` uses:

- SHA-256 for a file or a byte string. Same input, same hash. It is not encryption.
- HMAC-SHA256 so a hash is tied to a key.
- scrypt for passwords, with a random salt. A single fast hash is the wrong tool for passwords.
- Fernet from the `cryptography` package for symmetric encryption you can reverse with the key.

## How to reproduce

From the repository root, with the virtual environment activated:

```bash
pip install -r requirements.txt
pytest week-07-cryptography/encryption-hashing-practice
python3 week-07-cryptography/encryption-hashing-practice/crypto_practice.py README.md
```

The printed line is the SHA-256 of that file on your machine. It will differ if the file differs. Record the command and the hash in your evidence only after you run it.

In the notes below the commands, answer in your own words: when would you hash, when would you use HMAC, and when would you encrypt?

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
