# Least-privilege proposal

- Status: proposed
- System:
- Author: [Your name]
- Date:

## Problem

Daily work and administration are easy to collapse into one account. If that account is tricked or stolen, the attacker already has the keys. A new member of `sudo` or `Administrators` is also easy to miss if nobody is looking.

## Change

| | Before | After |
| --- | --- | --- |
| Account used for daily lab work |  | A normal user |
| Account used to install software |  | A separate admin account, used and then left |
| Who may add someone to sudo or Administrators |  | One person prepares, another approves |
| What gets logged |  | The group-add event the Week 11 rule is written for |

## What I will not do

I will not share the admin password to save time. I will not mark this proposal as done until the VM shows the two accounts, or until I write down why the lab VM cannot support them yet.

## Roll-back

If the separate admin account locks the team out, use the hypervisor console on the laptop, which does not depend on SSH or RDP. Record that you had to do that.
