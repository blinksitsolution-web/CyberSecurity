# Backup and logging checklist

## Backup

| Question | Your answer |
| --- | --- |
| What is being copied? |  |
| Where does the copy go? |  |
| How often? |  |
| Who can read the copy? |  |
| When did you last restore it? |  |
| Did the restored file match? How do you know? |  |

A backup you have never restored stays at status `gap` on the workstation baseline.

## Logging

A useful lab log line usually tells you when, who, where from, and what service. If one of those is missing, write the gap. Do not invent the missing field.

| Question | Your answer |
| --- | --- |
| Which file or event log did you open? |  |
| Is it synthetic sample data or from your VM? |  |
| Quote one line you actually saw |  |
| What would a failed logon look like in this source? |  |
| Where will Week 11 send these events? | Wazuh, once the agent is enrolled. Until then, say so. |

## Restore notes

Commands you ran:

Result:
