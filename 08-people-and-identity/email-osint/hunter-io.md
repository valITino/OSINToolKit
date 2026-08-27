---
name: hunter.io
slug: hunter-io
tier: 2
contact: passive
type: api
cost: freemium
platforms: [web, linux, macos, windows]
url: https://hunter.io/
categories: [people-and-identity, email-osint]
tags: [email-format, domain-search, verification, api]
status: active
status_checked: 2026-08-26
---

# hunter.io

## What question does it answer?
I have a company domain and a person's name. What address format does this organisation
use, and is the address I derived actually deliverable?

## When to reach for it
For the **email pattern**, which is the single most useful thing it returns. Domain
Search reports the format an organisation uses - `{first}.{last}@`, `{f}{last}@` and so
on - inferred from the addresses it has collected. That one line converts a name from
another source into a testable address, which is why it appears in almost every
corporate-recon workflow.

Email Verifier then tells you whether a derived address exists without sending anything
to it, which is the part that matters: it separates a plausible guess from a confirmed
mailbox.

## Install
```bash
# Nothing to install - REST API plus a web UI. Free account gives an API key.
export HUNTER_KEY=...
```

## Usage
```bash
curl "https://api.hunter.io/v2/domain-search?domain=example.com&api_key=$HUNTER_KEY"
curl "https://api.hunter.io/v2/email-finder?domain=example.com&first_name=Ada&last_name=Lovelace&api_key=$HUNTER_KEY"
curl "https://api.hunter.io/v2/email-verifier?email=ada@example.com&api_key=$HUNTER_KEY"
```

## Output
Domain Search returns the detected `pattern`, a list of known addresses with a
confidence score, and the sources where each was seen - **the sources are the part to
record**, because they let you corroborate independently. Email Verifier returns a
status (deliverable, risky, undeliverable) plus MX, SMTP and catch-all checks.

## Gotchas
- **The free tier is 50 credits a month** - roughly 50 addresses found or 100 verified.
  Paid plans start around $49/month. Fifty credits does not go far in real casework.
- **A confidence score is not confirmation**, and a derived address is a hypothesis. A
  `catch-all` domain accepts everything, so "deliverable" there means nothing at all -
  check the catch-all flag before believing a positive.
- **Deriving an address is discovery; mailing it is not.** Hunter is built as a cold-email
  platform and its outreach and sequence features are out of scope for this reference.
  Contacting a subject changes the nature of an investigation entirely - see
  [../../LEGAL.md](../../LEGAL.md).
- Its data is scraped from public web sources, so coverage skews to companies with a
  visible web presence and to English-language sites. Absence proves nothing.
- Addresses go stale as people leave. Treat every result as a lead with a date attached.
- Under GDPR, aggregating and processing named individuals' work addresses carries
  obligations even though the addresses are public.

## Alternatives
- [holehe](holehe.md) - which services an address is registered with
- [Have I Been Pwned](hibp.md) - which breaches an address appears in
- [theHarvester](../../01-orchestrators/aggregators/theharvester.md) - free, broad sweep across many sources
