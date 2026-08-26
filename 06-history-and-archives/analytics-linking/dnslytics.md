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
When [SpyOnWeb](spyonweb.md) comes back thin, and when the question has a time
dimension. DNSlytics runs Reverse Analytics and Reverse Adsense over its own index and
keeps roughly eight years of historical AdSense records, so it answers "who else does
this publisher own" *and* "who did they used to be" - the second question being the one
that usually cracks an attribution.

Its distinctive extra is **ads.txt**. Ad-monetised sites publish a file declaring which
ad networks may sell their inventory, keyed to a publisher account. DNSlytics indexes
millions of them with five years of history, which links sites that share a monetisation
account even when the page-level trackers have been cleaned up.

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

## Output
A list of domains sharing the identifier, with first- and last-seen dates on the
premium tiers. The free tier shows results but caps page views and withholds the
historical depth.

## Gotchas
- **It only reads the homepage and `ads.txt`.** DNSlytics says so itself. A tracking ID
  that appears only on an inner page, a subdomain, or a checkout flow will not be in the
  index - so a negative result is weak evidence, not clean.
- **The historical data is the paid part.** Eight years of AdSense records, the ads.txt
  archive, and full reports are premium; the free tier is a preview.
- **A shared analytics ID is strong evidence, a shared AdSense ID slightly weaker.**
  Agencies, resellers, and template vendors legitimately reuse both across unrelated
  clients. Establish that the identifier is unique to your subject before drawing a line.
- Google Tag (`G-`) and legacy Universal Analytics (`UA-`) identifiers are different
  namespaces; a site migrated between them may appear in one index and not the other.
- Identifiers get rotated. Absence today says nothing about last year, which is exactly
  why the historical view is worth paying for when a case turns on it.
- Corroborate a link before reporting it: shared infrastructure is a lead that needs a
  second, independent signal.

## Alternatives
- [SpyOnWeb](spyonweb.md) - the free first check for the same question
- [Robtex](../../03-dns-and-subdomains/reverse-dns/robtex.md) - infrastructure rather than tracker linkage
- [BuiltWith](../../04-web-exploration/fingerprinting/builtwith.md) - the full technology profile of one site
