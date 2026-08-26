---
name: DNSlytics
slug: dnslytics
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://dnslytics.com/
categories: [history-and-archives, analytics-linking]
tags: [analytics-id, adsense, ads-txt, reverse-lookup]
status: active
status_checked: 2026-08-26
---

# DNSlytics

## What question does it answer?
This site carries a Google Analytics ID, a Google Tag, or an AdSense ID. What other
domains carry the same one - now, and at any point in the last decade?

## When to reach for it
When [SpyOnWeb](spyonweb.md) comes back thin. DNSlytics runs Reverse Analytics (Google
tag IDs) and Reverse Adsense over its own index and will return up to 100,000 domains
for a single identifier - far past the point where the free alternatives stop.

Its distinctive extra is **ads.txt**. Ad-monetised sites publish a file declaring which
ad networks may sell their inventory, keyed to a publisher account. DNSlytics indexes
millions of them with years of history, which links sites sharing a monetisation account
even when the page-level trackers have been cleaned up. It also sits alongside Reverse
IP, NS, MX, SPF and PTR lookups and a Hosting History tool, so one identifier can be
walked across several kinds of infrastructure without changing sites.

## Install
```bash
# Nothing to install - web only. An API is available on paid plans.
```

## Usage
```text
https://dnslytics.com/reverse-analytics    # Analytics ID or Google Tag -> other domains
https://dnslytics.com/reverse-adsense      # AdSense publisher ID -> other domains
https://dnslytics.com/hosting-history      # how a domain's hosting has moved over time
https://dnslytics.com/reverse-ip           # co-hosted domains, with the usual caveats
```
```bash
# API (prepaid credits): ReverseGAnalytics and ReverseAdsense cost 6 each,
# ReverseHistory 20. Poll the free AccountInfo endpoint for your balance.
curl 'https://api.dnslytics.net/v1/accountinfo?apikey=YOURKEY'
```

## Output
A list of domains sharing the identifier, with first- and last-seen dates on the
premium tiers. The free tier shows results but caps page views and withholds the
historical depth.

## Gotchas
- **It only reads the homepage and `ads.txt`.** DNSlytics says so itself. A tracking ID
  that appears only on an inner page, a subdomain, or a checkout flow will not be in the
  index - so a negative result is weak evidence, not clean.
- **Reverse Analytics and Reverse Adsense return current domains only.** They no longer
  include domains that *used to* carry an ID; that needs the separate, much more
  expensive `ReverseHistory` endpoint. Do not assume a reverse lookup is historical.
- **Reverse PTR is fully premium-gated**, and other tools have individual fields marked
  premium. Full historical data and the larger result caps are paid; the entry
  subscription is advertised from around 30 cents a day.
- **API credits are prepaid and do not auto-renew** - at zero the API simply stops
  answering, and every page of a paginated result spends credits again. Rate limiting
  comes back as either 403 or 429, so handle both.
- **A shared analytics ID is strong evidence, a shared AdSense ID slightly weaker.**
  Agencies, resellers and template vendors legitimately reuse both across unrelated
  clients. Establish the identifier is unique to your subject before drawing a line.
- Google Tag (`G-`) and legacy Universal Analytics (`UA-`) IDs are different namespaces;
  a site that migrated may appear under one and not the other.
- Corroborate before reporting: shared infrastructure is a lead needing a second,
  independent signal.

## Alternatives
- [SpyOnWeb](spyonweb.md) - the free first check for the same question
- [Robtex](../../03-dns-and-subdomains/reverse-dns/robtex.md) - infrastructure rather than tracker linkage
- [BuiltWith](../../04-web-exploration/fingerprinting/builtwith.md) - the full technology profile of one site
