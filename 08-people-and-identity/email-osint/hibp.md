---
name: Have I Been Pwned
slug: hibp
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://haveibeenpwned.com/
categories: [people-and-identity, email-osint]
tags: [breach, exposure, email, credentials]
status: unverified
status_checked: 2026-08-26
---

# Have I Been Pwned

## What question does it answer?
I have an email address. Which public data breaches has it appeared in, and what
categories of data were exposed each time?

## When to reach for it
The authoritative, ethical answer to breach exposure. Troy Hunt's service aggregates
breach corpora and reports which ones contain a given address, along with what each
breach leaked. For an investigator it does two things: confirms an address is real and
in circulation, and reveals **which services the person used** - each breach is
evidence of an account on that platform, sometimes going back years.

## Install
```bash
# Web search is free. The API requires a low-cost subscription key.
```

## Usage
```bash
# Web: https://haveibeenpwned.com/  (enter the address)
curl -s -H "hibp-api-key: $HIBP_KEY" \
  "https://haveibeenpwned.com/api/v3/breachedaccount/target@example.com?truncateResponse=false"
```

## Output
A list of breaches with the service name, breach date, date added, and the data
classes exposed (email addresses, passwords, phone numbers, physical addresses).
Passwords themselves are never returned.

## Gotchas
- **It tells you an address appeared in a breach, not what the password was.** HIBP
  deliberately does not expose credentials, and using leaked credentials is out of
  scope for this repo and generally unlawful.
- Coverage is limited to breaches that have been loaded; a clean result means "not in
  a known, loaded breach", nothing more.
- The API needs a paid key (a few dollars a month - one of the best-value keys here;
  see [../../99-resources/api-keys/README.md](../../99-resources/api-keys/README.md)).
- Breach dates indicate when data was taken, which is often long before it surfaced -
  useful for timelining an account's age.

## Alternatives
- [holehe](holehe.md) - current registrations rather than historical breaches
- [hunter.io](hunter-io.md) - an organisation's address format, to derive addresses to check
- [../../09-code-paste-forums/paste-sites/README.md](../../09-code-paste-forums/paste-sites/README.md) - where dumps surface first
