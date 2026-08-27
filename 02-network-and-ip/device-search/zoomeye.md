---
name: ZoomEye
slug: zoomeye
tier: 2
contact: passive
type: api
cost: freemium
platforms: [web, linux, macos, windows]
url: https://www.zoomeye.ai/
categories: [network-and-ip, device-search]
tags: [device-search, banners, apac-coverage, cli]
status: active
status_checked: 2026-08-26
---

# ZoomEye

## What question does it answer?
Shodan and Censys found nothing on this host. Does a scanner with different coverage
see it?

## When to reach for it
As the third opinion. Internet-wide scanners do not see the same internet: each runs its
own crawlers from its own vantage points on its own schedule, so a host absent from one
index is routinely present in another. ZoomEye is operated by Knownsec and its coverage
of Chinese and wider APAC address space is materially better than the US-based
alternatives, which makes it the one to check when an investigation touches that
infrastructure.

Treat it as a coverage check rather than a replacement. Run it when a negative result
from [Shodan](shodan.md) or [Censys](censys.md) matters to your conclusion.

## Install
```bash
pip install zoomeyeai              # NOT 'zoomeye' - that package targets the dead .org API
zoomeyeai init -apikey "YOUR-KEY"  # API key auth only
```

## Usage
```bash
zoomeyeai init -apikey "YOUR-KEY"          # subcommands: init, info, search
zoomeyeai search '<dork>' -facets product,country   # aggregate over the whole result set
zoomeyeai search '<dork>' -sub_type v4 -pagesize 50 # restrict to IPv4, page size
zoomeyeai info                                       # remaining quota
```
Check the operator reference in ZoomEye's own docs before writing a dork - see Gotchas.

## Output
Host records with banners, service and product identification, port, location and ASN.
`-facets` is the distinctive option: it returns aggregate counts across the full result
set - by product, device, service, os, port, country, subdivisions, city - so you can
see the shape of a population without paging through it. `-sub_type` selects v4, v6 or
web data.

## Gotchas
- **`zoomeye.org` is dead** - it returns HTTP 521 and its API host refuses connections.
  Use `zoomeye.ai`. This matters beyond bookmarks: the legacy `zoomeye` PyPI package
  hardcodes the `.org` API and no longer works. The maintained package is `zoomeyeai`,
  whose console script is also `zoomeyeai` even though its own help text still prints
  "zoomeye".
- **Do not copy dorks out of old tutorials.** The query language changed between the
  `.org` and `.ai` generations, and almost every guide online still shows the v1
  `app:`/`port:`/`country:` colon form. The current operator reference lives only in
  ZoomEye's own documentation, which renders client-side and is account-gated - I could
  not read it to confirm the v2 operator list, so check it there rather than trusting
  this file or any other for exact syntax.
- Some response fields are gated by subscription tier, so a missing field can mean "not
  licensed" rather than "not present". Confirm against your own plan.
- Records come from ZoomEye's stored scan history, not a live probe. **Read
  `update_time`**: a record can be months stale, and the host may have changed hands.
- **Your queries go to a third party** subject to Chinese jurisdiction. Searching a
  target's infrastructure tells that operator what you are looking at - see
  [../../00-methodology/opsec/README.md](../../00-methodology/opsec/README.md).
- This is a database lookup, not a scan: passive, and the target sees nothing from you.

## Alternatives
- [Shodan](shodan.md) - the broadest index and the best tooling
- [Censys](censys.md) - certificate-centric, strongest for pivoting on TLS
- [nmap](../port-scanning/nmap.md) - when you are authorised to look for yourself
