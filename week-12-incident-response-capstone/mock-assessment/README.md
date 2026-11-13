# 40-question mock assessment

## Goal

Revise the twelve weeks with an original study quiz, then score it. Tuesday and Wednesday in the timetable are integrated revision. Thursday is a 40-question mock. These questions were written for this portfolio. They are not the bootcamp's exam paper, and they are not a past paper.

## What was built

- `questions.csv` — 40 multiple-choice questions. The answer is not in this file.
- `answer-key.csv` — the letter and a one-line reason. Open it after you have answered.
- `my-answers.csv.example` — a blank answer sheet.
- `score_mock.py` — compares your sheet with the key.
- `test_score_mock.py` — checks the scorer, including a perfect score against the key.

## How to reproduce

1. Copy `my-answers.csv.example` to `my-answers.csv`. Leave that copy uncommitted if you want the score to stay private.
2. Put `a`, `b`, `c`, or `d` in the answer column. Leave a blank when you do not know.
3. From this folder:

```bash
python3 score_mock.py --answers my-answers.csv
```

4. Then read the `why` column for the ones you missed. Change the portfolio note, not just the letter, when a question shows a gap.

The questions on Ghana law are study prompts. The official Act or directive wins if a line here ever feels too short.

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
