---
name: AbuseIPDB
slug: abuseipdb
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://www.abuseipdb.com/
categories: [network-and-ip, reputation]
tags: [reputation, abuse, blacklist, reports]
status: unverified
status_checked: 2026-08-26
---

# AbuseIPDB

## What question does it answer?
I have an IP. Has anyone else reported it for attacking them, and for what kind of
abuse?

## When to reach for it
Triage. When an IP shows up in a log and you need to know within seconds whether it
is a known scanner, brute-forcer, or spam source. AbuseIPDB is crowd-sourced: system
administrators submit reports with categories, and the site aggregates them into a
confidence score. Pair it with [VirusTotal](virustotal.md) for a second opinion from
a different data model.

## Install
```bash
# Web lookup needs nothing. A free API key allows scripted checks.
```

## Usage
```bash
# Web: https://www.abuseipdb.com/check/8.8.8.8
curl -s -G https://api.abuseipdb.com/api/v2/check \
  --data-urlencode 'ipAddress=8.8.8.8' -d maxAgeInDays=90 \
  -H "Key: $ABUSEIPDB_KEY" -H 'Accept: application/json'
```

## Output
An abuse confidence score (0-100), the total number of reports and distinct
reporters, the ISP/country, and the report categories (SSH brute force, port scan,
web spam, and so on) with free-text comments.

## Gotchas
- The score reflects **reports, not verification.** Anyone can report an IP, and
  reports are sometimes retaliatory or mistaken. Read the categories and comments,
  not just the number.
- Shared and dynamic addresses (CGNAT, VPN exits, cloud IPs) accumulate reports from
  many unrelated users. A high score on a cloud IP tells you little about the current
  tenant.
- A score of zero is not a clean bill of health - it may just mean nobody reported.
- Free API keys have a daily check limit; see
  [../../99-resources/api-keys/README.md](../../99-resources/api-keys/README.md).

## Alternatives
- [VirusTotal](virustotal.md) - multi-engine verdicts and passive DNS
- [IPVoid](ipvoid.md) - checks many blacklists in one query
- [ExoneraTor](exonerator.md) - specifically whether it was a Tor relay
