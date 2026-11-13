# Threat-intelligence summary

## Goal

Summarise a set of indicators you were given, and write down what a person must still decide. Thursday's assignment is this prototype. The script reads a local JSON file. It does not download a feed, block an address, or contact a host.

## What was built

- `sample-feed.json` — four synthetic indicators, including `203.0.113.10`, which matches the sample brute-force log on purpose, and a `.invalid` domain name.
- `threat_intel_summary.py` — counts by type and prints review questions.
- `test_threat_intel_summary.py` — checks the sample.

The SHA-256 in the file is the hash of an empty file. It is a format example, not a malware hash.

## How to reproduce

```bash
python3 -m pytest test_threat_intel_summary.py
python3 threat_intel_summary.py sample-feed.json
```

Answer the `human_review` questions in your evidence notes. If a value also appears in `samples/auth.log`, say so, and say that both files were written that way for the exercise.

If you later use a real feed, you need the right to store it, a place that is not a public git repo, and a person who decides any action. An AI summary of a feed has the same limit: it can group text, and it cannot authorise a block.

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
