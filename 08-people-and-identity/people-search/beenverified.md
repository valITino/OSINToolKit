---
name: BeenVerified
slug: beenverified
tier: 2
contact: passive
type: web
cost: paid
platforms: [web]
url: https://www.beenverified.com/
categories: [people-and-identity, people-search]
tags: [people-search, us-records, data-broker, paid]
status: active
status_checked: 2026-08-26
---

# BeenVerified

## What question does it answer?
I have a US name, phone, email, or address and I need a public-records report. What will
it actually cost me, and what am I forbidden to use it for?

## When to reach for it
Reach for it last. BeenVerified aggregates federal, state, and county records - court
records, property data, contact history, criminal and traffic records - into a single
report, and it does not tier features: every plan gets everything, so the only variable
is price and term.

The catch is that **there is no free tier at all**. Every search returns a teaser until
you have an active membership, so unlike [Spokeo](spokeo.md) or
[ThatsThem](thatsthem.md) you cannot confirm you have the right person before paying.
Exhaust the free sources first and come here only when a specific record type -
typically property or county court data - is what you actually need.

## Install
```bash
# Nothing to install - web only.
```

## Usage
```text
https://www.beenverified.com/          # people, reverse phone, email, or address search
https://www.beenverified.com/fcra/     # read this before deciding it fits your purpose
https://www.beenverified.com/svc/optout/search/optouts   # removal request
```

## Output
A background report: contact information, address history, property records, court and
criminal records where held, and relatives. Reports can be set to alert you when they
change.

## Gotchas
- **No free tier.** A roughly $1 seven-day trial converts to $36.89 a month, or $71.94
  a quarter - the most expensive of the consumer options here, around double Spokeo's
  observed monthly rate. Trials auto-convert silently; both plans auto-renew.
- **Both plans cap at 100 reports a month**, and the trial caps at 100 for the whole
  trial. Bulk enumeration is not possible.
- **Not a consumer reporting agency.** Its own FCRA page explicitly forbids using it for
  employment screening, hiring household workers, tenant screening, or educational
  qualification. Treat that as a hard boundary, not boilerplate -
  see [../../LEGAL.md](../../LEGAL.md).
- **Standard aggregator accuracy failures**: addresses years out of date, disconnected
  phone numbers, records for deceased people, and same-name merges that fuse two people
  into one report. Every field is a lead, never attribution.
- **Opting out is nine forms, not one.** BeenVerified is one of nine brands under The
  Lifetime Value Company - PeopleLooker, PeopleSmart, NeighborWho, Ownerly,
  ReversePhone, NumberGuru and others share infrastructure. Propagation across the
  family is claimed but not guaranteed; check each.
- No EU erasure workflow. Californian subjects are better served by one Delete Act DROP
  submission than by the site's own form.
- The site sits behind bot protection and resists automated collection - a `BLOCKED`
  result from a link checker here means nothing about its health.

## Alternatives
- [ThatsThem](thatsthem.md) - free, and enough to confirm identity before you spend
- [Spokeo](spokeo.md) - a genuinely useful free skeleton, cheaper subscription
- [public-records](../public-records/README.md) - the authoritative sources these resell
