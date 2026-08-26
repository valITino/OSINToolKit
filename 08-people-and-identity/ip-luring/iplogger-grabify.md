---
name: IPLogger / Grabify
slug: iplogger-grabify
tier: 3
contact: active
type: web
cost: freemium
platforms: [web]
url: https://grabify.link/
categories: [people-and-identity, ip-luring]
tags: [ip-logging, legally-sensitive, tracking-links]
status: unverified
status_checked: 2026-08-26
superseded_by: canarytokens
---

# IPLogger / Grabify

## What question does it answer?
If I get someone to click a link I control, what is their IP address, approximate
location, device, and browser?

## Why this is tier 3
It works, and that is the problem. These services generate a tracking link that
records visitor details, usually disguised as a normal URL. They are tier 3 here for
two reasons:

1. **Legally sensitive.** Inducing a person to reveal their IP under a false pretext
   is an active interaction with them. Depending on jurisdiction and intent it can
   engage privacy law, deception provisions, or harassment law. It is also the
   standard technique of online harassment, and using it looks the same regardless of
   your motive.
2. **[Canarytokens](canarytokens.md) does the same job with defensible framing**,
   better documentation, self-hosting, and a memo trail - and is the version you can
   explain to a court or a client.

Use Canarytokens. This entry exists so you recognise these links when a subject or a
third party uses them, which is the more common investigative encounter.

## Install
```bash
# Nothing to install - hosted link generators.
```

## Usage
```text
Recognising one matters more than creating one:
- A shortened or unfamiliar domain in an unsolicited message is the usual delivery.
- Expanding a short link before clicking (unfurl services, or a sandbox such as
  urlscan.io) shows the redirect chain without exposing your own IP.
```

## Output
A log of visits: IP, timestamp, user agent, referrer, and inferred location.

## Gotchas
- **The IP is often not the person's.** Mobile carriers, corporate proxies, VPNs, and
  link-preview bots (messaging apps fetch links automatically) all pollute the result.
  A hit may be a scanner, not your subject.
- **Legal exposure is real** - see [../../LEGAL.md](../../LEGAL.md). Do not use these
  against a person without a lawful basis and, where relevant, authorisation.
- The services themselves log everything you do; you are trusting a third party with
  your investigation.
- Defensively: treat an unexpected shortened link as hostile and expand it in a
  sandbox.

## Alternatives
- [Canarytokens](canarytokens.md) - the defensible equivalent, use this instead
- [urlscan.io](../../04-web-exploration/fingerprinting/urlscan-io.md) - safely expand and inspect a suspicious link
