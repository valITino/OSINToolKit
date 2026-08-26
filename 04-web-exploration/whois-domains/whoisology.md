---
name: Whoisology
slug: whoisology
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://whoisology.com/
categories: [web-exploration, whois-domains]
tags: [reverse-whois, archive, pivot, pre-gdpr]
status: active
status_checked: 2026-08-26
---

# Whoisology

## What question does it answer?
I have one WHOIS record. Which other domains share its registrant email, name,
organisation, or address - and who owned them at a given point in the past?

## When to reach for it
This is the affordable answer to the registrant pivot. Every field on a Whoisology
record is a link: click a registrant email and you get every domain in the archive tied
to that address, split by Registrant, Administrative, Technical, and Billing role. The
role split matters - a technical contact shared across otherwise unrelated domains
often exposes the agency or operator behind them.

Its second trick is time travel. Archives are semi-annual snapshots running from
December 2012 to the present, and you can pin a reverse lookup to a specific snapshot to
ask who owned what in, say, 2015. Everything runs against its own archive, so the target
never sees the query.

## Install
```bash
# Nothing to install - web only. A JSON API exists on paid tiers.
```

## Usage
```text
https://whoisology.com/<domain>                        # archived record, every field clickable
https://whoisology.com/email/<address>                 # reverse lookup by email
https://whoisology.com/organization/<org+name>         # also /name/, /phone/, /street/, /city/
https://whoisology.com/organization/archive_53/<org+name>/1   # pinned to one snapshot
```

## Output
An archived WHOIS record with hyperlinked fields, and reverse pages listing associated
domains grouped by contact role, with an archive selector for choosing a period. Paid
tiers add downloadable change-log reports of up to 1,000 results.

## Gotchas
- **The free tier shows you that matches exist but not what they are.** Anonymous
  reverse lookups replace the domain list with a membership prompt, and you get three
  pages an hour against the latest archive only - no history.
- **The data is semi-annual snapshots, not live.** A registrant change from last month
  will not appear. This is an archive for historical attribution, not a
  current-ownership oracle - use [whois](../../02-network-and-ip/registries-asn/whois.md)
  for that.
- **Pivoting on a privacy-service value is useless.** "Whois Privacy Corp" and its
  equivalents are shared by millions of domains. Confirm the value is unique to your
  subject before drawing any line.
- Post-GDPR snapshots are mostly redacted. As with every service of this kind, the
  investigative value is concentrated **before May 2018**.
- Paid tiers run $30/month (Beginner) to $270/month (Legendary); redaction removal and
  keyword search are premium-only.
- The site publishes no company name or ownership beyond a copyright line. Your queries
  are logged by an operator you cannot identify - worth weighing on sensitive casework.

## Alternatives
- [DomainTools](domaintools.md) - deeper and fresher archive, far more expensive
- [viewdns.info](viewdns.md) - free reverse IP and IP history without an account
- [../../06-history-and-archives/ip-whois-history/README.md](../../06-history-and-archives/ip-whois-history/README.md) - the wider history toolkit
