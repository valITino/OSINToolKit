---
name: Canarytokens
slug: canarytokens
tier: 2
contact: active
type: web
cost: free
platforms: [web]
url: https://canarytokens.org/
categories: [people-and-identity, ip-luring]
tags: [tripwire, tokens, alerting, defensive]
status: unverified
status_checked: 2026-08-26
---

# Canarytokens

## What question does it answer?
Did someone open this document, visit this URL, or access this resource - and from
what IP and client?

## When to reach for it
The defensively-framed tripwire, and the one to use if you use any of these. You
generate a token (a URL, a DNS name, a Word or PDF document, an AWS key, an image),
place it somewhere, and receive an alert with the visitor's IP and user agent when it
is triggered. Legitimate uses are strong: seeding your own network or documents to
detect intrusion, or confirming that a leaked file is being opened.

Its framing matters. [IPLogger and Grabify](iplogger-grabify.md) do a similar thing
with none of the defensive context and considerably more legal risk - prefer this.

## Install
```bash
# Nothing to install - generate tokens at canarytokens.org, or self-host the open-source version.
```

## Usage
```text
1. Choose a token type (URL, DNS, Word/PDF document, cloned-site, and others).
2. Set the alert email or webhook and a memo saying where you placed it.
3. Place the token; the memo is what tells you which one fired months later.
```

## Output
An alert containing the timestamp, source IP, user agent, and your memo. Document
tokens also indicate the application that opened them.

## Gotchas
- **The IP you get may not be the subject's.** Corporate proxies, VPNs, mail-scanning
  gateways, and link-preview bots all trigger tokens - and a security product opening
  the document is a very common false positive.
- **Placing a token where a third party will trigger it is an active interaction with
  a person** and can engage privacy or computer-misuse law depending on jurisdiction
  and intent. Use on your own assets, or with authorisation. See
  [../../LEGAL.md](../../LEGAL.md).
- Always write a memo. An unattributed alert months later is useless.
- Tokens can be spotted by a careful subject, which tips them off.

## Alternatives
- [IPLogger / Grabify](iplogger-grabify.md) - tier 3, legally sensitive
- [../../10-email-investigation/tracking/README.md](../../10-email-investigation/tracking/README.md) - the email-specific version
