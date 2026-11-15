# Compliance automation

## Goal

Count a control sheet and produce a summary a human still has to read. Monday's assignment is this prototype. The script does not judge whether evidence is good. It counts the status words you typed.

## What was built

- `sample-controls.csv` — eight synthetic rows. The counts are 2 met, 2 partial, 2 gap, 2 not-reviewed. Those numbers describe the sample file, not your lab.
- `compliance_report.py` — the counter.
- `test_compliance_report.py` — locks the sample counts so a quiet edit to the CSV is noticed.

Allowed statuses: `met`, `partial`, `gap`, `not-reviewed`. Anything else is listed as unknown and is not treated as met.

## Practical platform: GRC Lab

Do this practical in the [GRC Lab](https://grclab.purplecop.io/lab). When you finish an exercise there, save your own evidence in this folder. Do not invent screenshots or exports.

- Date you used the GRC Lab:
- What you completed there:
- Screenshot or export file in this folder:
- What you still need to finish in the files here:

## How to reproduce

```bash
python3 -m pytest test_compliance_report.py
python3 compliance_report.py sample-controls.csv --markdown
```

Copy `sample-controls.csv` to a new file, replace the rows with your Week 4 gap checklist, and run the script on the copy. Keep `data_label` honest.

If you use an AI tool to draft a finding sentence, paste only the status and the control id, not personal data. Then edit the sentence yourself. The script's reminder is the rule: a count is not an audit opinion.

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
