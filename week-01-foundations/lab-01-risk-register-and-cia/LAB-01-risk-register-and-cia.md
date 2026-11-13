::: title-page
# Lab 01 — Risk, CIA, and professional judgement

**Course:** Maxim Nyansa Cybersecurity Bootcamp, Ghana  
**Dates:** 5 October–25 December 2026  
**Trainee:** James Ackah Blay · Aiyinasi, Ghana  
**Week:** 1 — Foundations and professional orientation  
**Estimated time:** 3 hours  
**Difficulty:** Foundation. This is the language the later labs assume.

::: tutor
**Tutor note.** Do this work yourself. The GRC Lab is the practical platform. Record only what you actually did. A tutor answer key exists outside this guide. Opening it first will train you to copy, not to judge.
:::
:::

## 1. Learning objectives

| Objective | Job skill it maps to |
| --- | --- |
| Classify information by confidentiality, integrity, and availability | Triage: decide what an alert puts at risk |
| Write a risk as asset, threat, vulnerability, and control | Risk statements a SOC lead or GRC analyst can use |
| Score a 5 by 5 matrix and choose a treatment | Prioritisation, instead of treating every ticket as equal |
| Discuss legal and ethical limits in Ghana | Knowing when to stop, and what not to paste into a tool |
| Run a scorer and explain its output | Evidence: a command, a file, and a sentence a reviewer can check |

## 2. Prerequisites and setup

You need Python 3.11 or newer, a spreadsheet or text editor, and a browser. No virtual machine yet.

Practical platform: [GRC Lab](https://grclab.purplecop.io/lab). Complete the risk exercise there, then bring the evidence back to this folder. This guide does not describe that site's screens.

Files you will edit, all in this folder:

- `cia-exercise.md`
- `risk-register-worksheet.md` and `risk-register-worksheet.csv`
- `risk-matrix.md`
- `ethics-questions.md`
- `submission-checklist.md`

Leave `examples/` closed until you have finished your own scores.

## 3. Scenario

Palm Court Stationery and Print is a fictional shop in Takoradi. Auntie Esi Mensah owns it. Kwame helps after school. They print, sell school books, and offer mobile-money cash-in and cash-out as an agent.

The shop has one counter laptop with customer names and phone numbers, a shared till password, passport photos in a WhatsApp chat, a mobile-money PIN written on a slip, a USB stick called "the backup" that nobody has restored, and Wi-Fi whose password is on a sticky note. Customers use that same Wi-Fi as the till laptop.

This is not a real client. Do not visit a real shop to collect a customer list for this lab.

## 4. Tasks

### Task 1 — Classify six items

Open `cia-exercise.md`. For each item, name the property hit first: confidentiality, integrity, or availability. Add one sentence.

Confidentiality means the wrong person can see it. Integrity means it was changed or no longer matches the truth. Availability means people cannot use it when they need it.

::: checkpoint
**You should now see** six rows filled in your own words, including one item where you were tempted to name two properties and you still picked a first one.
:::

### Task 2 — Write six risk statements

Use the same ids, R-01 to R-06, in the Markdown worksheet and in the CSV. A statement has an asset, a threat, a vulnerability, and the control that exists today. "None" is allowed. Do not invent a control the shop does not have.

Suggested assets, which you may reword: the customer list, the shared password, the passport photos, the PIN and float, the print files, the shop Wi-Fi.

Leave likelihood and impact empty until Task 3.

### Task 3 — Score the matrix

Likelihood and impact are integers from 1 to 5. Score = likelihood × impact.

| Score | Band | What you do |
| --- | --- | --- |
| 1–5 | Low | Record it. A named person may accept it. |
| 6–11 | Medium | Owner and a treatment. |
| 12–19 | High | Do not leave the treatment blank. |
| 20–25 | Critical | Say what happens this week. |

Copy each id into `risk-matrix.md` in the cell for its likelihood and impact.

### Task 4 — Choose a treatment

On every scored row set `treatment` to mitigate, avoid, transfer, or accept. Accept is a decision with an owner and a reason. A blank cell is not accept.

### Task 5 — Run the scorer

From this folder:

```bash
python3 score_risks.py risk-register-worksheet.csv
```

The script only reads a CSV inside this lab folder. It does not change the file. A blank likelihood is "not scored". It is not zero.

::: checkpoint
**You should now see** your ids on the printed grid, a line `L# x I# = score band` for each scored row, and a flagged list of scores 12 and above. If the grid and `risk-matrix.md` disagree, the CSV and the grid have different numbers. Fix the one that does not match your written reason.
:::

### Task 6 — Ethics and the law, with your team

Answer `ethics-questions.md`. These notes are not legal advice.

- Act 1038 (Cybersecurity Act, 2020) establishes the Cyber Security Authority.
- Act 843 (Data Protection Act, 2012) regulates personal data. A passport photo and a phone number are personal data.
- Act 772 (Electronic Transactions Act, 2008) includes unauthorised access to electronic records.
- The Bank of Ghana Cyber and Information Security Directive applies to institutions the Bank regulates. This shop is not that institution. The shop still handles someone else's float and must follow the provider's agent rules. Read the current text on the Bank of Ghana site before you quote an article. A revised directive was published in 2026.

::: checkpoint
**You should now see** five case notes that say what you would refuse, not only what the law is called.
:::

### Task 7 — Evidence from the GRC Lab

Save a screenshot or export you produced in the GRC Lab into this folder. In `submission-checklist.md`, write the date and the file name. If you have not used the lab yet, leave the lines blank. Do not draw a fake screenshot.

## 5. Troubleshooting

| What you see | What to check |
| --- | --- |
| `No such file` | You are not in this lab folder. `pwd` should end in `lab-01-risk-register-and-cia`. |
| `outside the allowed folder` | Pass `risk-register-worksheet.csv`, not a path to another directory. |
| `must be from 1 to 5` | A cell contains 0, 6, or text. Likelihood and impact are 1 to 5 only. |
| Every row says "Not scored yet" | The numbers are in the Markdown file and not in the CSV. The script reads the CSV. |
| The grid looks empty | Blank cells are correct until Task 3. They are not a failure. |

## 6. Stretch task

Add a seventh risk that is about availability of the mobile-money service on payday. Score it. Say whether transfer to the provider is honest, or whether the shop still owns the customer conversation when the service is down.

## 7. Evidence for the portfolio

- The CSV with your scores and treatments.
- The command output from Task 5, saved as text you captured.
- The GRC Lab export, if you have one.
- `submission-checklist.md` with your name already printed and the date you add.

Do not submit the example CSV as your work.

## 8. Reflection

1. Which item was hardest to classify, and why?
2. Where would a teammate's score have changed your treatment?
3. Which law did you almost apply to the wrong organisation?

## 9. Interview questions this lab prepares

1. Explain confidentiality, integrity, and availability with one example each.
2. What is the difference between a threat and a vulnerability?
3. How do you decide what to work on first when several risks exist?
4. When is "accept" a real decision, and when is it an empty cell?
5. Why is pasting a customer list into a public chatbot a data-protection problem?

## 10. Grading rubric

| Criterion | Exceeds | Meets | Not yet |
| --- | --- | --- | --- |
| CIA | First property is named and the sentence matches it | Six rows filled with a property | Rows copied with no reason |
| Risk statements | Asset, threat, vulnerability, and today's control are distinct | Six statements are complete | Threat and vulnerability are the same sentence |
| Scoring | Every number has a reason, and the script matches the grid | Scores are in range and treatments are named | Numbers with no reason, or the example file submitted as yours |
| Ethics | Refusals are specific | All five cases have notes | Only Act numbers, no decision |
| Evidence | Your command output and any GRC Lab file are yours | Checklist is honest about what is missing | Invented output |
