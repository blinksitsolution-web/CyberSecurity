# Tabletop — new admin on the lab server

**This is fiction for the classroom.** It is not a report of an incident at Maxim Nyansa or on your laptop.

## Situation

It is Thursday afternoon. The lab lead opens the practice dashboard and sees two things on `wazuh`, the Ubuntu VM:

- Many failed SSH attempts from a single address in the last ten minutes.
- A log line that says a new account was added to the `sudo` group.

Nobody in the room remembers creating that account. The Windows VM also has a normal user logged in.

## Roles

| Role | Job in the room |
| --- | --- |
| Incident lead | Keeps the group on one decision at a time |
| IT / lab | Says what the VMs can do, and what they cannot prove |
| Communications | Drafts what you would tell the trainer, without drama |
| Scribe | Fills the decision log |
| Management | Decides when to pause the lab |

## Injects

Read one at a time.

1. You only have the two sentences in the situation. What do you believe, what is still unknown, and who is in charge for the next 15 minutes?
2. A teammate wants to "try the same thing back" against the address to see who it is. What do you say, given the Week 1 rule on authority?
3. Someone suggests isolating the Ubuntu VM from the host-only network. What breaks if you do that, and what do you preserve first?
4. The new sudo account might have been a classmate's experiment. How do you check without wiping the logs?
5. The failed attempts include a username that looks like a student's real name. What do you tell the trainer, and what stays out of the class chat?

## After the discussion

- Which decisions needed evidence you do not have?
- Which Week 11 detection would have made inject 1 clearer, if it were deployed?
- What will you change in the lab before Week 12?
