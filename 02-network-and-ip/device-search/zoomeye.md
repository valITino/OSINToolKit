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
zoomeyeai search 'app="Cisco ASA SSL VPN" && country="CN"'   # v2 syntax uses '=', not ':'
zoomeyeai search 'cidr="192.0.2.0/24" && service="ssh"'
zoomeyeai search 'port=80' -facets product,country           # aggregate the whole result set
zoomeyeai info                                                # remaining quota
```

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
- **The v1 dork syntax in most tutorials is wrong now.** `app:`, `port:`, `country:` was
  the `.org` era. v2 uses `=`: `app="..."`, `port=80`, `country="CN"`. There is no
  `ver=` operator any more.
- **`=` is not exact.** A single `=` matches case-insensitively after tokenisation, so
  it behaves like a substring match and is a large false-positive source; `==` is the
  exact, case-sensitive form and `!=` negates. `&&`, `||` and parentheses work.
- **Several response fields are gated by plan** - body, hashes and industry
  classification need higher tiers - so a missing field may mean "not licensed" rather
  than "not present".
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
