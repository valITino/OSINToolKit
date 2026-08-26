---
name: Netcraft Site Report
slug: netcraft
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://sitereport.netcraft.com/
categories: [history-and-archives, ip-whois-history]
tags: [hosting, netblock, first-seen, free]
status: active
status_checked: 2026-08-26
---

# Netcraft Site Report

## What question does it answer?
How long has this site actually existed, and whose network is it really on?

## When to reach for it
For the **date first seen**, which is the field nothing else gives you for free.
Netcraft has surveyed the web since 1995, so its report puts a first-observed date on a
site - a lookup for `example.com` returns December 1995. When you are assessing whether
a domain is a freshly stood-up phishing property or a twenty-year-old business, that
single line settles it faster than anything else, and it costs nothing.

The rest of the report is a genuinely broad one-page profile: netblock owner and
delegation, hosting company and country, both IP families with their ASNs, nameservers
and registrar, TLS, SPF and DMARC, plus the web trackers embedded in the page.

## Install
```bash
# Nothing to install - web only, no account.
```

## Usage
```text
https://sitereport.netcraft.com/?url=example.com     # full report for one site
https://sitereport.netcraft.com/                      # or paste the URL into the form
```

## Output
Sections for Background (site title, rank, **date first seen**), Network (netblock owner,
hosting company and country, IPv4 and IPv6 with autonomous systems, reverse DNS,
nameserver, registrar), IP delegation, IP geolocation, SSL/TLS, SPF, DMARC, web
trackers, and site technology.

## Gotchas
- **"Date first seen" is when Netcraft first observed the site, not when the domain was
  registered.** They diverge, sometimes by years. For registration dates use
  [whois](../../02-network-and-ip/registries-asn/whois.md).
- The netblock owner is the **current** host. Behind a CDN it reads Cloudflare or Fastly
  and tells you nothing about the origin - see
  [Cloudflair](../../05-certificates-tls/origin-unmasking/cloudflair.md) for that problem.
- Several panels load via JavaScript, so a scripted fetch returns a partial page. Treat
  it as a browser tool.
- It reports the current state plus a first-seen date. It is **not** a full historical
  timeline - for dated record-by-record history use
  [SecurityTrails](securitytrails.md) or
  [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md).
- There is no public API on the free report; Netcraft's data products are a separate
  commercial offering.
- The web-trackers panel is a useful free cross-check on
  [analytics linking](../analytics-linking/README.md), but it reflects one crawl of one
  page.

## Alternatives
- [SecurityTrails](securitytrails.md) - dated historical DNS and WHOIS via API
- [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md) - free IP history table
- [BuiltWith](../../04-web-exploration/fingerprinting/builtwith.md) - deeper technology profile
