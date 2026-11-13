# Lab 1 — CIA, risk register, and ethics

Trainee guide (PDF): [LAB-01-risk-register-and-cia.pdf](LAB-01-risk-register-and-cia.pdf). Rebuild it with `python3 labs/build_pdfs.py` from the repository root. The tutor answer key is not inside the PDF.

**Week 1 practical.** 5–9 October 2026. This is the hands-on session for the CIA triad, risk statements, a 5 by 5 matrix, treatments, and the ethical and legal cases (including Ghana's Act 1038, Act 843, Act 772, and the Bank of Ghana Cyber and Information Security Directive).

Your answers stay in the worksheet files. The folder `examples/` is a finished sample for a fictional shop. It is not your result.

Companion notes, if you want the shorter templates as well: [risk register](../risk-register/) and [ethics case studies](../ethics-case-studies/).

## Objectives

By the end of this lab you can:

1. Classify information by confidentiality, integrity, and availability.
2. Write a risk as an asset, a threat, a vulnerability, and a consequence.
3. Score likelihood and impact from 1 to 5 and read a 5 by 5 matrix.
4. Choose a treatment: mitigate, avoid, transfer, or accept.
5. Discuss four legal and ethical situations without treating the discussion as legal advice.
6. Run a small Python scorer that multiplies likelihood by impact and flags high scores.

## Prerequisites

- The Week 1 words: asset, threat, vulnerability, control, CIA.
- Python 3.11 or newer. No extra package is required for the scorer. `pytest` is only for the tests, from the repository `requirements.txt`.
- No virtual machine. This lab is paper, a spreadsheet, and one script.
- About two to three hours. The risk register fits the Wednesday practical. The cases fit the Friday ethics session.

## Practical platform: GRC Lab

Do the risk-register and CIA work in the [GRC Lab](https://grclab.purplecop.io/lab), then bring your own evidence back to this folder. This page does not describe the site. Do not invent screenshots or exports.

- Date you used the GRC Lab:
- What you completed there:
- Screenshot or export saved in this folder:
- What you still need to finish in the worksheets here:

## Scenario

**Palm Court Stationery and Print** is a fictional shop in Takoradi. It is not a real business, and it is not your result.

Auntie Esi Mensah owns the shop. Her nephew Kwame helps after school. They photocopy, print, laminate, sell school books, and offer mobile-money cash-in and cash-out as an agent for a provider. Six people work there at the busiest hour.

What the shop actually has:

- One laptop on the counter. It holds customer names and phone numbers for print orders, and it is often left signed in.
- A shared till password that everyone at the counter knows.
- WhatsApp on Esi's phone, including passport photos taken for customers. The photos are not deleted.
- A mobile-money float. The agent PIN is written on a slip at the counter.
- One USB stick in the cash drawer, described as "the backup". Nobody has restored a file from it.
- Shop Wi-Fi. The password is on a sticky note. Customers use the same network as the till laptop.

## How the files fit together

| File | Who writes in it |
| --- | --- |
| `cia-exercise.md` | You |
| `risk-register-worksheet.md` | You, in sentences |
| `risk-register-worksheet.csv` | You, in the columns the script reads |
| `risk-matrix.md` | You, after you have scores |
| `ethics-questions.md` | You and your team |
| `score_risks.py` | Already written. You run it. |
| `examples/` | Nobody. It is the sample solution. |
| `submission-checklist.md` | You, when you think you are finished |

## Tasks

### Task 1 — Classify six items with CIA

Open `cia-exercise.md`. For each item from Palm Court, say which of confidentiality, integrity, or availability is hit first, and one sentence why. An item can matter to more than one property. Pick the first one.

Do this before you score anything. The class of the information changes how bad the impact is.

### Task 2 — Write six risk statements

Open `risk-register-worksheet.md` and the matching `risk-register-worksheet.csv`. Use the same six ids, R-01 to R-06, in both files.

A risk statement has four parts:

1. **Asset** — the thing you are worried about.
2. **Threat** — what could cause harm.
3. **Vulnerability** — the weakness that lets the threat through.
4. **Existing control** — what the shop already does. "None" is an honest answer.

Then name the CIA property from Task 1.

Suggested assets, which you may reword: the customer list, the shared password, the passport photos, the mobile-money PIN and float, the print files and order book, the shop Wi-Fi. You do not have to use these six if you can defend a different six from the same shop.

Leave likelihood and impact blank until Task 3.

### Task 3 — Score the 5 by 5 matrix

Read `risk-matrix.md`. Score each risk:

- **Likelihood:** 1 rare, 2 unlikely, 3 possible, 4 likely, 5 almost expected if nothing changes.
- **Impact:** 1 nuisance, 2 a bad hour, 3 a real loss for a customer or a day's takings, 4 serious harm to a person or the shop, 5 harm you would escalate the same day.

**Score = likelihood × impact.** The script does this multiplication. Do not invent a score you cannot explain in the notes column.

Bands used in this lab:

| Score | Band |
| --- | --- |
| 1–5 | Low |
| 6–11 | Medium |
| 12–19 | High |
| 20–25 | Critical |

High and critical are the flagged risks. The cut-off is **12**.

Put the numbers in the CSV. In `risk-matrix.md`, copy each id into the cell for its likelihood and impact.

### Task 4 — Choose a treatment

For every scored row, set `treatment` to one of:

| Treatment | Meaning in this shop |
| --- | --- |
| mitigate | Add or fix a control |
| avoid | Stop the risky practice |
| transfer | Share the impact, for example through the mobile-money provider's process or insurance |
| accept | Someone named accepts the remaining risk, and the reason is written down |

A blank treatment is not the same as accept. Accept needs an owner.

### Task 5 — Run the scorer

From this folder:

```bash
python3 score_risks.py risk-register-worksheet.csv
```

You should see your ids on the matrix, a line for each scored risk, and a flagged list. Blank rows stay under "Not scored yet". They are not zeros.

Check the tests, which use the example file and a blank fixture, not your worksheet:

```bash
python3 -m pytest test_score_risks.py
```

From the repository root, `pytest` includes this lab.

If you want to see a finished report, run the scorer on `examples/example-risk-register.csv` **after** you have tried your own. That file is marked example data.

### Task 6 — Ethics and legal cases

Open `ethics-questions.md` and answer with your team. The four cases use Palm Court plus one case about this lab itself.

These notes are not legal advice. When you name an Act, say what you think it is about in your own words, and write down what you would ask the trainer.

- **Act 1038 (Cybersecurity Act, 2020)** establishes the Cyber Security Authority and regulates cybersecurity activities, including critical information infrastructure and some cybersecurity services.
- **Act 843 (Data Protection Act, 2012)** regulates personal data. Passport photos and phone numbers are personal data.
- **Act 772 (Electronic Transactions Act, 2008)** includes offences such as unauthorised access to electronic records.
- **Bank of Ghana Cyber and Information Security Directive** applies to institutions the Bank of Ghana regulates. A small agent shop is not the bank. The shop still handles someone else's float and must follow the provider's rules. Read the current directive on [bog.gov.gh](https://www.bog.gov.gh/) before you quote an article number. A revised directive was published in 2026.

Official texts are linked in [the Week 1 law notes](../ethics-case-studies/ghana-law-notes.md).

### Task 7 — Submit

Use `submission-checklist.md`. Do not replace your worksheet with the example file.

## What I learned

Answer in your own words.

1. Which Palm Court asset was hardest to classify, and why?
2. Where did your score disagree with a teammate's, and what changed your mind?
3. Which Act or directive did you almost apply to the wrong organisation?
4. What would you do on a SOC shift with a risk that has no owner?
5. Which file in this folder is your work, and which file is the example?

## Evidence to add yourself

Do not invent results. The script's output on your CSV is evidence. A screenshot of the example file is not.

- Date completed:
- What you did:
- File in `evidence/`:
- Feedback:
