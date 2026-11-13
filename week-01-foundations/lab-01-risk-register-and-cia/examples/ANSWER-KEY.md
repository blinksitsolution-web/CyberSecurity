# Example solution — not your submission

**Read this after you have tried the lab.**

This is one finished example for the fictional shop Palm Court Stationery and Print. The scores are teaching numbers, not a measurement of a real business. Do not copy this file into `risk-register-worksheet.csv` and hand it in as your work. Another team can defend different scores if their reasons are clear.

The matching data is `example-risk-register.csv` in this folder. Every row is marked `example=yes`.

## CIA classifications

| ID | Property hit first | Why this example chose it |
| --- | --- | --- |
| C-1 Customer names and phone numbers | Confidentiality | The harm of a lost laptop is strangers seeing the list. |
| C-2 Exam papers waiting for collection | Integrity | A changed or swapped paper harms the school before anyone talks about theft. Confidentiality also matters. |
| C-3 Mobile-money cash-out on payday | Availability | If the service is down, people cannot collect money that day. |
| C-4 Passport photos in WhatsApp | Confidentiality | An identity document image is personal data and is easy to forward. |
| C-5 Price list on the wall | Integrity | It is already public. The useful question is whether the prices are right. Availability is a stretch here. |
| C-6 The day's float total | Integrity | The dangerous failure is a total that does not match the wallet. Confidentiality still matters. |

## Example risks

| ID | Asset | Threat | Vulnerability | Control today | CIA | L | I | Score | Band | Treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | Shop laptop with the customer list | Theft from the counter | No disk encryption, often left signed in | Screen lock only | Confidentiality | 3 | 4 | 12 | High | Mitigate: full-disk encryption and a habit of locking it |
| R-02 | Shared till password | A former helper or a customer reuses it | Everyone at the counter knows it | None | Confidentiality | 4 | 3 | 12 | High | Mitigate: one account each, the old password retired |
| R-03 | Passport photos in WhatsApp | The phone is lost or the chat is forwarded | No deletion date | Chat on one phone | Confidentiality | 4 | 5 | 20 | Critical | Mitigate: stop storing ID images in WhatsApp, tell customers, delete what is there |
| R-04 | Mobile-money PIN and float | Someone sees the PIN and moves the float | PIN written on the counter | Provider rules, unread | Integrity | 4 | 5 | 20 | Critical | Mitigate: remove the written PIN, only Esi and one deputy know it |
| R-05 | Print jobs and the order book | Files lost or quietly changed | USB backup never restored | USB in the drawer | Integrity | 2 | 4 | 8 | Medium | Mitigate: restore one file this week and record the result |
| R-06 | Shop Wi-Fi | A customer device shares the network with the till | Password on a sticky note, no guest network | The note on the wall | Confidentiality | 2 | 3 | 6 | Medium | Mitigate: a guest network, till laptop not on it |

R-04 is scored as integrity because the float can be moved and the records would lie. Confidentiality of the PIN is how that happens. Either property is defensible if the sentence says so.

## Matrix the script prints for the example file

|  | L1 | L2 | L3 | L4 | L5 |
| --- | --- | --- | --- | --- | --- |
| I5 | . | . | . | R-03, R-04 | . |
| I4 | . | R-05 | R-01 | . | . |
| I3 | . | R-06 | . | R-02 | . |
| I2 | . | . | . | . | . |
| I1 | . | . | . | . | . |

Flagged, because the score is 12 or above: R-01, R-02, R-03, R-04.

This table was checked against `python3 score_risks.py examples/example-risk-register.csv`. If you change the CSV, run the script again. Do not edit this table by hand and leave the CSV behind.

## Ethics — one way a class might answer

These are discussion points, not a court judgment.

1. **Laptop.** Refuse the after-hours look. Act 772 treats unauthorised access to an electronic record as an offence. Deleting the output does not create permission. Practise on the team's own lab later, inside a written scope.
2. **Passport photos.** A photo that identifies a person is personal data. Keeping it "in case we need a reprint", with no limit and a copy on a personal phone, fails purpose and security. Stop adding photos to WhatsApp, and delete the ones the shop no longer needs for an order in progress.
3. **PIN.** The float can be moved. That is an integrity failure, and customers are harmed. The Bank of Ghana directive applies to regulated institutions, not automatically to this agent shop. The shop still has to follow the provider's agent rules and should not leave the PIN on the counter.
4. **Chatbot.** The names and numbers have left the shop's control. Act 843 expects a reason to disclose personal data, and a public tool is a disclosure. Paste a fake row, or columns with the personal data removed.
5. **Real shop Wi-Fi.** A class scenario is not permission. Do not scan, photograph a real till, or collect a real customer list for this assignment. Later labs in this portfolio stay on the host-only network named in Week 2, and Week 10 still needs a signed scope.

## What this example refuses to claim

- Palm Court is not a client engagement.
- The scores are not a risk assessment you can show a real owner as if you had visited.
- Nothing here certifies the shop, and nothing here is legal advice.
