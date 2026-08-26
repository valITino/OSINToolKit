---
name: SpyOnWeb
slug: spyonweb
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://spyonweb.com/
categories: [history-and-archives, analytics-linking]
tags: [analytics-id, adsense, attribution, linking]
status: unverified
status_checked: 2026-08-26
---

# SpyOnWeb

## What question does it answer?
This site carries a Google Analytics or AdSense ID. What **other** sites carry the
same one - meaning the same person or organisation probably runs them?

## When to reach for it
One of the strongest attribution pivots in web investigation. Operators reuse tracking
accounts across their properties, so a shared identifier links sites that share no
infrastructure, no registrant, and no obvious branding. Get the IDs from the page
source or from [BuiltWith](../../04-web-exploration/fingerprinting/builtwith.md), then
look them up here.

The identifiers to grep for:

- `UA-XXXXXX` (legacy Google Analytics) and `G-XXXXXXX` (GA4)
- `pub-XXXXXXXX` / `ca-pub-XXXXXXXX` (Google AdSense)
- `&tag=` (Amazon Associates affiliate tag)

## Install
```bash
# Nothing to install - web lookup.
```

## Usage
```text
https://spyonweb.com/            # search by domain, IP, or a tracking ID directly
# Get the ID first:
curl -s https://example.com | grep -Eo 'UA-[0-9]+-[0-9]+|G-[A-Z0-9]+|(ca-)?pub-[0-9]+'
```

## Output
Sites sharing the queried identifier, IP, or DNS server, with the date the
association was observed.

## Gotchas
- **The database is historical and incomplete.** It reflects what was collected at
  some point, so it misses recent sites and may show associations that have ended.
  Absence of a result proves nothing.
- **Shared IDs have innocent explanations**: web agencies, templates, and CMS themes
  reuse tracking accounts across unrelated clients. Corroborate before asserting
  common ownership.
- GA4's `G-` identifiers are less consistently indexed by these services than legacy
  `UA-` ones.
- Free lookups are limited; deeper queries require a key.

## Alternatives
- [BuiltWith](../../04-web-exploration/fingerprinting/builtwith.md) - find the IDs, plus its own reverse lookups
- [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md) - reverse IP as a different linking method
- [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md) - certificate-based relationships
