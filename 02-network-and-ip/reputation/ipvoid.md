---
name: IPVoid
slug: ipvoid
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://www.ipvoid.com/
categories: [network-and-ip, reputation]
tags: [blacklist, reputation, dnsbl]
status: unverified
status_checked: 2026-08-26
---

# IPVoid

## What question does it answer?
I have an IP. Is it listed on any of the well-known blacklists, and what do basic
lookups say about it?

## When to reach for it
When you want blacklist coverage in one query rather than checking DNSBLs one at a
time. IPVoid runs an IP against a set of reputation and blocklist providers and
summarises the hits, alongside utility lookups (reverse DNS, geolocation, WHOIS).
Its sibling URLVoid does the same for domains.

## Install
```bash
# Nothing to install - web only. Some tools are behind an API plan.
```

## Usage
```text
https://www.ipvoid.com/ip-blacklist-check/    # blacklist status for an IP
https://www.urlvoid.com/                       # the same idea for a domain
```

## Output
A pass/fail table across the blacklist engines it queries, plus reverse DNS,
ASN/ISP, and country. The value is the aggregate: several independent listings is a
much stronger signal than one.

## Gotchas
- Blacklists specialise. A mail-focused DNSBL listing says the IP sent spam, not
  that it is scanning you - read what each list is actually for.
- Listings go stale. An IP can remain listed long after the abusive tenant left,
  which matters most on cloud and dynamic ranges.
- Free web use is rate-limited and some features require a paid plan.

## Alternatives
- [AbuseIPDB](abuseipdb.md) - report-based, with categories and comments
- [VirusTotal](virustotal.md) - multi-engine plus passive DNS pivots
- [MXToolbox](../../10-email-investigation/header-analysis/mxtoolbox.md) - mail-focused blacklist checks
