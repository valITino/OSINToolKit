---
name: ThatsThem
slug: thatsthem
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://thatsthem.com/
categories: [people-and-identity, people-search]
tags: [people-search, reverse-lookup, us-records, free]
status: unverified
status_checked: 2026-08-26
---

# ThatsThem

## What question does it answer?
I have a name, phone number, email, or IP. What publicly aggregated records connect
to it - address, relatives, associated phone numbers?

## When to reach for it
The free option worth trying before anything paid. Most people-search sites tease a
result and then demand a subscription; ThatsThem shows a usable amount for free and
supports reverse lookups from several starting points, including email and IP. Use it
to generate leads you then verify in
[public records](../public-records/README.md) - never as a source of record itself.

## Install
```bash
# Nothing to install - web only.
```

## Usage
```text
https://thatsthem.com/            # search by name, phone, email, address, or IP
```

## Output
Aggregated records: names, ages, current and previous addresses, phone numbers,
possible relatives, and sometimes vehicle or property hints.

## Gotchas
- **Coverage is heavily US-centric.** For EU subjects, expect little or nothing - and
  note that GDPR restricts this kind of aggregation in the first place. See
  [../../LEGAL.md](../../LEGAL.md).
- **Data broker records are frequently wrong or stale** - mismatched relatives,
  addresses from a decade ago, conflated identities between people sharing a name.
  Treat every field as an unverified lead.
- IP-to-person association on these sites is especially unreliable; see
  [../../02-network-and-ip/geolocation/README.md](../../02-network-and-ip/geolocation/README.md).
- Searching for a person on a broker site may itself be logged.

## Alternatives
- [public-records](../public-records/README.md) - authoritative, verifiable sources
- [Spokeo](spokeo.md) - paid, but its free directory pages add relatives and location history
- [BeenVerified](beenverified.md) - paid brokerage with no free tier at all
- [Pipl](pipl.md) - enterprise identity resolution; no longer available to individuals
