---
name: ONYPHE
slug: onyphe
tier: 2
contact: passive
type: cli
cost: freemium
platforms: [linux, macos, web]
url: https://search.onyphe.io/
categories: [network-and-ip, device-search]
tags: [device-search, oql, banners, aggregation]
status: active
status_checked: 2026-08-29
---

# ONYPHE

## What question does it answer?
I have a banner, a TLS certificate, an HTTP title or a device class. Which hosts
match it according to a European scanner running its own weekly sweep, and can I get
the answer back aggregated rather than as ten thousand raw rows?

## When to reach for it
When the question is "how many, grouped by what", not "show me every host". OQL pipes
results through server-side functions, so `| uniq domain | addcount` returns ranked
distinct domains in one call. It also sweeps from three vantage points, so geo-fenced
and split-horizon infrastructure shows up as rows that disagree.

Reach elsewhere for freshness: the weekly sweep means short-lived assets belong to
[Shodan](shodan.md) or [Censys](censys.md), and history depth is purchased here
(7 to 30 days), so long look-backs are not what this tool is for.

## Install
```bash
git clone https://github.com/onyphe/cli.git && cd cli && ./install.sh  # Debian/Kali
# elsewhere: cpanm the Perl deps, then perl Build.PL && ./Build && sudo ./Build install
printf 'api_endpoint = https://www.onyphe.io/api/v2\napi_key = YOUR_APIKEY\n' > ~/.onyphe.ini
# free key: https://search.onyphe.io/signup
```

## Usage
```bash
onyphe -search 'protocol:ssh | uniq domain | addcount'   # domains ranked by count
onyphe -search 'category:datascan app.http.title:confluence'   # who else runs this
onyphe -search 'category:datascan domain:google.com !organization:google'   # hosts in
        # a domain NOT owned by the expected org (! is NOT): shadow IT, lookalikes
curl -H 'Authorization: bearer KEY' 'https://www.onyphe.io/api/v2/search/?q=category:datascan+protocol:rdp'  # no Perl needed
```

## Output
JSON: an envelope (`count`, `status`, `took`, `page`, `page_size`, `max_page`) around
a `results` array. Read `@category` first - one query returns datascan, resolver and
vulnscan objects with different fields - then `@timestamp`, because two records for
one host may disagree only because different vantage points saw it at different times.
`| uniq X | addcount` returns an aggregation whose count column is the finding, and
one call is a page, not the population.

## Gotchas
- **The domain moved and the redirect is half-broken.** www.onyphe.io 301s to
  www.onyphe.com, but deep links 404 (/pricing, /docs/getting-started). App, docs and
  sign-up live at search.onyphe.io, the API at onyphe.io, the company at
  www.onyphe.com - old bookmarks land on dead pages.
- The Free View does give API access, but only "standard filters against standard
  categories"; advanced ones are plan-gated, so a query copied from the OQL docs can
  return zero because of your licence. Check `/api/v2/user` before calling it absence.
- **History depth is purchased**: 7 days on Catfish, 14 on Sealion, 30 on Shark, so
  `-monthago:3` from the docs quietly reaches nothing on a short plan. Prices are
  unpublished and the rate limit averages 1 request/second. Sweeps are weekly, not
  continuous: a host that appeared, was abused and vanished inside the week is
  invisible, while one dead yesterday is still listed.
- **OQL is its own dialect**, not Lucene and not Shodan syntax: `category:` is all but
  mandatory, filters AND by default, `!` is NOT, `?` is OR, functions are dash-prefixed
  (`-since`, `-wildcard`). A pasted Shodan query parses cleanly and matches nothing.
- The Perl CLI was last committed in May 2025 (v4.19.1) and has a long dependency
  chain; if the build fights you, drive `/api/v2/` with curl. The documented
  `api_endpoint` also 301s, and a client that drops the Authorization header across
  that redirect fails with an auth error rather than a redirect one.
- Querying is passive, but ONYPHE also sells Attack Surface products that actively
  probe. Know which you drive before pointing it at someone else's estate, and treat
  resolver and WHOIS rows as personal data - see [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Shodan](shodan.md) - continuous scanning when weekly cadence is too coarse
- [Censys](censys.md) - certificate-led pivots and longer host history
- [Netlas.io](netlas.md) - Lucene instead of OQL, with a published free quota
- [FOFA](fofa.md) - Chinese vantage point where ONYPHE's European sweep is thin
