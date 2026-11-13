# User journeys

Identification says which account this is. Authentication checks the proof. Authorisation decides what that account may do after the proof succeeds. A failed logon is still useful to a SOC. A successful logon to a new admin account is more serious, which is why Week 11 flags both patterns differently.

## Journey A — analyst opens the lab dashboard

| Step | What happens | Your lab, today |
| --- | --- | --- |
| 1. Identification | The person types an account name |  |
| 2. Authentication | Password, key, or a second factor |  |
| 3. Authorisation | The app decides whether this account may view alerts |  |
| 4. Logging | A success or a failure is recorded without the password |  |

## Journey B — paper exercise, delegated access

A fictional scheduling app asks a student to let it read a calendar. Roles in OAuth 2.0 language:

| Role | In this story |
| --- | --- |
| Resource owner | The student |
| Client | The scheduling app |
| Authorisation server | The identity provider that can say yes |
| Resource server | The calendar |

OpenID Connect would add an identity token so the app knows who signed in, not only that it may read a calendar.

| Question | Your answer |
| --- | --- |
| What is the smallest permission the app needs? |  |
| What should the student be able to revoke? |  |
| Which value must not be pasted into a ticket or a chat? |  |

This journey is not wired to a real provider. Do not create an OAuth client against a production identity service for this assignment.
