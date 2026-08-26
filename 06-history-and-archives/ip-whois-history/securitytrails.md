---
name: SecurityTrails
slug: securitytrails
tier: 2
contact: passive
type: api
cost: freemium
platforms: [web, linux, macos, windows]
url: https://securitytrails.com/corp/api
categories: [history-and-archives, ip-whois-history]
tags: [passive-dns, whois-history, api, subdomains]
status: active
status_checked: 2026-08-26
---

# SecurityTrails

## What question does it answer?
What did this domain resolve to **before**, who registered it before the record was
redacted, and what else has lived in the address space around it?

## When to reach for it
When you need history as data rather than as a web page. SecurityTrails keeps
historical DNS and WHOIS back to 2008 and exposes all of it over a JSON API, so a
timeline of a domain's A records - every hosting move, with dates - is one curl away.
That is the pivot that turns "the site is behind a CDN now" into "here is the origin it
used in 2019".

Its `associated` and `ips/nearby` endpoints extend the same idea sideways: domains
sharing a registrant, and the neighbouring addresses in a range.

## Install
```bash
# Nothing to install. Register for an API key, then:
export ST_KEY=...       # pass it in the APIKEY header, not the query string
```

## Usage
```bash
curl -H "APIKEY: $ST_KEY" 'https://api.securitytrails.com/v1/history/example.com/dns/a?page=1'
curl -H "APIKEY: $ST_KEY" 'https://api.securitytrails.com/v1/history/example.com/whois'
curl -H "APIKEY: $ST_KEY" 'https://api.securitytrails.com/v1/domain/example.com/subdomains'
curl -H "APIKEY: $ST_KEY" 'https://api.securitytrails.com/v1/ips/nearby/192.0.2.1'
```

## Output
JSON. Historical DNS returns dated record sets, paginated with `page`. Historical WHOIS
returns past registration records including registrant contacts and nameservers. Domain
lookups also report how many *other* domains share a given record, which is a quick
read on whether an IP is dedicated or shared.

## Gotchas
- **The free tier is small** - commonly cited as around 50 queries a month, with WHOIS
  excluded - and the figure is not published anywhere I could read directly. Treat it as
  approximate and check before planning around it. Real investigative volume is paid.
- **The DNS-history record type is a strict enum**: `a`, `aaaa`, `mx`, `ns`, `soa`,
  `txt`. There is no `cname` on that endpoint.
- **Reverse DNS history is shallow** - documented at around 120 days - even though
  domain and DNS history reach back to 2008. Do not assume one window applies to both.
- `securitytrails.com` sits behind a Cloudflare bot challenge and returns 403 to scripted
  clients. `api.securitytrails.com` does not. A 403 from the marketing site is not an
  API outage.
- Passing the key as `?apikey=` works but is discouraged by the vendor - it lands in
  proxy and server logs.
- Branding is split: the product still ships as SecurityTrails but is a Recorded Future
  property, and parts have been folded into that platform. Expect documentation to
  straddle both names.
- Passive DNS coverage is uneven. **Absence of a record is not proof an asset never
  existed.**

## Alternatives
- [Netcraft Site Report](netcraft.md) - free, one page, no key
- [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md) - free IP history in a browser
- [Robtex](../../03-dns-and-subdomains/reverse-dns/robtex.md) - free passive DNS with first/last-seen dates
