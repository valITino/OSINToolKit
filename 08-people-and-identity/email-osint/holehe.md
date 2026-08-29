---
name: holehe
slug: holehe
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/megadose/holehe
categories: [people-and-identity, email-osint]
tags: [email, account-discovery, registration]
status: unverified
status_checked: 2026-08-26
---

# holehe

## What question does it answer?
I have an email address. Which online services is it registered with?

## When to reach for it
When an email is your only identifier and you need to know where the person has
accounts. holehe queries services' registration and password-reset endpoints and
infers, from how each responds, whether the address is already in use. That maps an
address to a set of platforms without ever logging in.

Its stated design is to avoid sending a notification to the address owner, but treat
that as a goal rather than a guarantee - see Gotchas.

## Install
```bash
pipx install holehe
```

## Usage
```bash
holehe target@example.com                      # check across all supported services
holehe target@example.com --only-used           # show only the services where it exists
holehe target@example.com --csv                 # save results
```

## Output
One line per service with a used/not-used/rate-limited verdict. Read the rate-limited
ones as unknown, not negative - that distinction matters and is easy to skim past.

## Gotchas
- **Active, and it touches third-party services on the subject's behalf.** Modules
  aim to be silent, but a service can change its behaviour and start emailing the
  account holder. Assume some risk of tipping off the subject
  ([OPSEC](../../00-methodology/opsec/README.md)).
- Detection modules break constantly as sites change; false negatives are common and a
  stale install is worse than useless. Update immediately before a run.
- Results are inference from response behaviour, not confirmation - corroborate before
  asserting an account exists.
- Personal data: have a lawful basis. See [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Have I Been Pwned](hibp.md) - breach exposure rather than current registration
- [Sherlock](../username-enum/sherlock.md) - the same question from a username
- [PGP keyservers](../../10-email-investigation/server-checks/pgp-keyservers.md) - a published key can tie the address to a name and to other addresses
- [theHarvester](../../01-orchestrators/aggregators/theharvester.md) - find addresses in the first place
