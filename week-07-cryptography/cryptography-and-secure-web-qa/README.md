# Cryptography and secure web questions

Individual answers by James Ackah-Blay. The file properties record 9 October 2026. Week 7 of the bootcamp (cryptography and secure communications) runs 16–20 November 2026, so this is earlier written coursework filed here because the questions match that week: symmetric and asymmetric encryption, hashing, certificates, and secure communication. It is not the Week 7 lab set (key-management policy, certificate exercise, and mini demo), which is still ahead.

Full document: [cryptography-and-secure-web-qa.pdf](cryptography-and-secure-web-qa.pdf) (7 pages)

## Context

Five questions, answered with short writing and screenshots. The question prompts themselves are not printed on the pages, so the notes below follow what the pages show.

## Role

Individual. The file author is James Ackah Blay.

## Frameworks and methods

No standard such as NIST or ISO is cited. The pages show:

- MD5 checksum comparison in WinMD5Free v1.20
- A written comparison of symmetric and asymmetric encryption, using a staff IT auditor sending a document to a senior IT auditor
- A browser crypto toolkit screenshot with AES-256-GCM selected for password-based encryption, and a second screenshot for a public/private key pair
- A browser certificate viewer opened on jumia.com.gh
- A written path for loading https://blinkscollege.com
- A written description of WhatsApp message protection using the Signal Protocol and the Double Ratchet

## Deliverables and findings

**Checksums.** Three WinMD5Free dialogs. Two report "Matched!" and one reports "NOT Matched".

**Symmetric encryption.** His answer says the same secret key encrypts and decrypts. The screenshot shows AES-256-GCM chosen as the encryption method, a passphrase, and a downloaded encrypted file.

**Asymmetric encryption.** His answer says the recipient generates a public key and a private key, the sender encrypts with the public key, and the recipient decrypts with the private key. The page includes a key-generation screenshot.

**HTTPS and certificates.** His written check for an online purchase is to confirm the address uses HTTPS, then to check that the certificate is valid, including its issue date and expiry date. He included the browser certificate viewer for jumia.com.gh, with the subject, issuer, and validity period on screen. A later paragraph traces https://blinkscollege.com as: enter URL, resolve DNS, establish a connection, send the request, process the request, receive the response, render the page, and record activity. He names GET as a common request method.

**Messaging.** His WhatsApp answer describes four steps under the Signal Protocol: the device generates a key pair, the sender encrypts with the recipient's public key before the message leaves the device, the server forwards ciphertext without the private key, and the recipient decrypts locally. He then names the Double Ratchet as the mechanism that changes keys after every message.

## Skills demonstrated

Explaining symmetric and asymmetric encryption in plain language, checking an HTTPS certificate in the browser, comparing file hashes with WinMD5Free, and describing end-to-end messaging at the level of the Signal Protocol and the Double Ratchet. The pages do not include a key-management policy or a measured TLS configuration.
