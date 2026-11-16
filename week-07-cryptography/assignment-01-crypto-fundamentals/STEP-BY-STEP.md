---
title: "Lab 07b — Cryptography assignment"
---

::: title-page
# Lab 07b — Cryptography assignment

**Course:** Maxim Nyansa Cybersecurity Bootcamp, Ghana  
**Trainee:** James Ackah Blay · Aiyinasi, Ghana  
**Assignment date:** 16 November 2026  
**Week:** 7 — Cryptography and secure communications  
**Estimated time:** 4 hours  
**Difficulty:** Intermediate. Classical cipher, then real attack names, then one local ECB exercise.

::: tutor
**Tutor note.** Do the brute force and the ECB demo yourself. The worked write-up is in ANSWERS.md. Screenshot lines in this guide are empty until you capture your own terminal. Do not paste output you have not run.
:::
:::

## 1. What you will be able to do

| Objective | Job skill |
| --- | --- |
| Break a Caesar ciphertext by trying every shift and saying why one answer is English | Know when a cipher is too small to matter |
| Argue for and against hiding a crypto design | Kerckhoffs's principle, in a vendor conversation |
| Compare symmetric and asymmetric cryptography | Explain hybrid encryption the way TLS uses it |
| Classify five published attacks without replaying them | Read an advisory and say what kind of break it is |
| Recover a fictional secret from a local ECB oracle | See why ECB is not an AEAD mode |

## 2. Setup

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd week-07-cryptography/assignment-01-crypto-fundamentals
python3 -m pytest test_caesar.py test_ecb_byte_at_a_time.py
```

You need Python 3.11 or newer. The `cryptography` package provides AES. No network call is required. Pandoc and WeasyPrint are only needed if you rebuild this PDF:

```bash
python3 build_pdf.py
```

## 3. Scenario

The bootcamp set five questions on 16 November 2026. They are copied in `ASSIGNMENT.md`. Your job is to answer them in your own notes, then keep the terminal evidence next to `ANSWERS.md`. The ECB question is a thinking exercise about a made-up server. The program in this folder is that server. It is not a host on the internet.

## 4. Tasks

### Task 1 — Caesar, all 25 shifts

```bash
python3 caesar.py brute "XLMW MW E WIGVIX QIWWEKI"
python3 caesar.py decrypt --shift 4 "XLMW MW E WIGVIX QIWWEKI"
```

::: checkpoint
**You should now see** 25 lines. One of them is ordinary English. The decrypt command prints that same sentence. Write the shift number in your notes and one sentence on why the other shifts lost: they do not contain the short English words.
:::

Save the terminal text yourself. Do not copy a score out of `ANSWERS.md` into a screenshot.

### Task 2 — Read the assignment and draft question 2

Open `ASSIGNMENT.md`. For the design-document question, write at least two arguments for each of the three options before you read `ANSWERS.md`. Then compare. Your paragraph should mention Kerckhoffs's principle: the design can be public; the key must not.

::: checkpoint
**You should now see** six arguments of your own, plus a sentence that says hiding the design is not the security boundary.
:::

### Task 3 — Symmetric and asymmetric

In your notes, list two advantages of asymmetric encryption and one of symmetric encryption. Name hybrid encryption and TLS in one sentence. The model answer is in `ANSWERS.md` if you want to check the wording after you have written yours.

### Task 4 — Classify the five attacks

Open each source linked in `ASSIGNMENT.md`. Fill this table yourself. Do not download exploit code.

| Attack | Setting | Methodology | One sentence from the source, in your words |
| --- | --- | --- | --- |
| EFF DES cracker |  |  |  |
| Bar Mitzvah |  |  |  |
| CRIME |  |  |  |
| ROBOT |  |  |  |
| GPP cpassword |  |  |  |

Settings you may use: known plaintext, chosen plaintext, chosen ciphertext, none needed. Methodologies: key brute force, cryptanalytic, circumventing an otherwise secure cipher. ROBOT needs a short nuance: it is a padding oracle, so it is cryptanalytic, and it only works because the server reveals padding failures.

Do not copy Microsoft's published AES key into the repository. The fact that it was published is the answer. The key bytes are not.

::: checkpoint
**You should now see** five filled rows and no pasted key material.
:::

### Task 5 — Local ECB demo

```bash
python3 ecb_byte_at_a_time.py --secret SECRETS
```

::: checkpoint
**You should now see** `secret_length=7`, `recovered=b'SECRETS'`, and `match=True`. The key is not printed. If `match` is false, stop and read the traceback. Do not point this program at any host.
:::

Read the "Question 5" section of `ANSWERS.md` only after the command succeeds, and check that your understanding of the 15-byte prefix matches the diagram there.

### Task 6 — Tests

```bash
python3 -m pytest test_caesar.py test_ecb_byte_at_a_time.py
```

::: checkpoint
**You should now see** six passing tests. That includes a secret that contains a zero byte, so trailing zeros are not being thrown away by accident.
:::

## 5. Troubleshooting

| What you see | What it means |
| --- | --- |
| `No module named pytest` or `cryptography` | The virtual environment is not active, or `pip install -r requirements.txt` was not run |
| Caesar output is not English | The quotes around the ciphertext were lost and the shell split the words. Quote the whole string |
| `match=False` | The secret you passed is not the one you think, or the script was edited. Re-run the tests |
| PDF build fails | Install `pandoc` and `weasyprint`. The assignment itself does not need the PDF |

## 6. Stretch

**Vigenère.** A Vigenère cipher uses a keyword, so the shift changes every letter. Take the keyword `LAB` and the plaintext `SECRET`. Write the shifts by hand (L, A, B, L, A, B) and the ciphertext. One keyword is enough to see why a single frequency count no longer picks a unique shift.

**ECB picture, local only.** Make a small PPM image on your own machine, keep the header, and encrypt only the pixel bytes with `openssl enc -aes-128-ecb` and again with `-aes-128-cbc`. Look at the two pictures. ECB repeats blocks, so a pattern in the picture survives. CBC does not. Use a throwaway key. Do not commit the key. GCM, if you try it, also hides the pattern and adds a tag. That is the mode you would actually choose.

## 7. Evidence to capture

Replace each line with a file you produced. Leave it blank rather than inventing a screenshot.

- Caesar brute-force output:
- Your six arguments for question 2:
- Your classification table:
- ECB demo output (`match=True`):
- pytest output:

## 8. Reflection

1. Why is "try all 25 shifts" a complete attack on Caesar and not on AES?
2. Which of the five published attacks still left the cipher's mathematics standing?
3. What would go wrong if the ECB oracle had used a random IV in front of the secret?

## 9. Interview questions

1. State Kerckhoffs's principle in one sentence.
2. Why does TLS use both asymmetric and symmetric cryptography?
3. What is the difference between known plaintext and chosen ciphertext?
4. Why is AES-ECB a bad way to encrypt a structured secret?
5. Why is a published key a design failure even when the cipher is AES-256?

## 10. How this will be read

| Criterion | Strong | Enough | Not yet |
| --- | --- | --- | --- |
| Caesar | You can explain the winning shift without the table in front of you | The command output is yours and names shift 4 | A screenshot of someone else's terminal |
| Design secrecy | Kerckhoffs is applied to option 3, and each option still has two arguments | Six arguments are present | Only "obscurity is bad" |
| Attack table | The ROBOT nuance is in your words | Five rows match the setting and methodology | A copied exploit |
| ECB | You can say what the 15-byte prefix is for | `match=True` on a secret you chose | The script aimed at a real server |
