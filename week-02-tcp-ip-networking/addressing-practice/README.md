# Addressing practice

## Goal

Practise IPv4 addresses, subnet identification, and a first comparison with IPv6. Tuesday is IPv4. Wednesday is IPv6. Friday ties it back to packet flow.

## What was built

- `worksheet.md` — questions with space for your answers.
- `answer-key.md` — look after you have tried.
- `net_addressing.py` — a calculator for a CIDR you type. It does not scan anything.

## How to reproduce

From this folder, after the root requirements are installed:

```bash
python3 net_addressing.py 192.168.56.10/24
python3 -m pytest test_net_addressing.py
```

From the repository root, `pytest` runs this test with the others.

Try the worksheet before you open the answer key. Then check two of your answers with the script so you can see the same result from the `ipaddress` library.

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
