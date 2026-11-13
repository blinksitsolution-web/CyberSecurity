# Password and MFA policy

- Owner: [Your name]
- Applies to: lab accounts and anything that protects the home SOC lab
- Date:

## Passwords

| Rule | Choice |
| --- | --- |
| Minimum length | 12, matching `password_policy.py` |
| Character mix | Lower case, upper case, a digit, and a symbol |
| Username inside the password | Not allowed |
| Obvious passwords | Rejected. The script's list is only a few examples |
| Where the password is stored | A password manager, not git |
| Shared passwords | Not allowed for personal or admin accounts |
| How you change a suspected leak | Replace it the same day and note which systems used it |

## MFA

MFA means more than one factor type: something you know, something you have, or something you are. Two passwords are still one type.

| System | Factors you will require | Available in the lab today? |
| --- | --- | --- |
| Laptop login |  |  |
| Wazuh dashboard | Password plus a second factor when the product and the lab can support it |  |
| Email used for the bootcamp |  |  |
| Cloud account, if you open one in Week 9 |  |  |

Biometrics, such as a fingerprint, are a factor you are. They need a fallback when the sensor fails, and they are personal data under Act 843 if a system stores the template. Say whether your lab stores one. If it does not, write "not used".

## Single sign-on, in one picture

SSO lets a person sign in once and reach several services. The lab may not have SSO. Draw the picture anyway, using a fictional school identity provider, and mark it **not deployed**.

| Step | System | What is exchanged |
| --- | --- | --- |
| 1 | Person | Proves identity to the identity provider |
| 2 | Identity provider | Gives the application a yes, and a small set of claims |
| 3 | Application | Lets the person in based on the claims, not on a second password |

OAuth 2.0 is about delegated access: an app receives limited permission to act. OpenID Connect adds a sign-in identity on top of that pattern. The user-journey project is where you map one flow in more detail.
