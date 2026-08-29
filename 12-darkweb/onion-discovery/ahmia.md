---
name: Ahmia
slug: ahmia
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://ahmia.fi/
categories: [darkweb, onion-discovery]
tags: [tor, onion, search-engine, index, seed-list]
status: active
status_checked: 2026-08-29
---

# Ahmia

## What question does it answer?
I have a keyword - a victim name, a brand, a handle. Which indexed Tor hidden
services mention it, when was each last seen alive, and what is Ahmia's full
public list of known onion addresses?

## When to reach for it
First stop when you start from a keyword rather than an address, and the best
free bulk seed list on the clearweb: `/address/` hands you every onion Ahmia
indexes as plain text. Not for confirming the canonical address of a known
service - that is [dark.fail](dark-fail.md), which signs its listings - and
never for arguing a service does not exist: 10,251 indexed onions is nothing.

## Install
```bash
# Nothing: clearweb site, no account, no API key, no Tor client, no search API.
# The crawler behind it is self-hostable but needs your own Tor daemon and
# Elasticsearch - research infrastructure, not a drop-in CLI:
git clone https://github.com/ahmia/ahmia-crawler   # then venv + ./run.sh
```

## Usage
```text
https://ahmia.fi/search/?q=ransomware
  # keyword search - drive it from the homepage form in a browser, because the
  # form injects a hidden anti-bot field and a bare GET answers 302 Location: /
https://ahmia.fi/address/
  # plaintext dump of every indexed onion - 10,251 v3 addresses on 2026-08-29
https://ahmia.fi/add/onionsadded/
  # undocumented recently-submitted feed - 947 addresses on 2026-08-29
```
```bash
echo -n "targetaddress.onion" | md5sum   # grep the hash against
# https://ahmia.fi/blacklist/banned/ to see if Ahmia abuse-blocked that domain
```

## Output
Result blocks of title, the service's own meta description, the bare v3
hostname rendered unclickable, and a relative last-seen age ("1 week, 6 days"),
under a header giving the count, query time and collapsed near-duplicates. Read
the age first - it is the only liveness signal here. `/address/` and `/onions/`
are flat lists of `http://<56char>.onion/` with no metadata at all.

## Gotchas
- **Scripted search silently fails.** `/search/?q=` 302-redirects to `/` without
  the homepage token and cookie, robots.txt disallows it, and tools hardcoding a
  plain GET return zero hits rather than an error.
- **Absence proves nothing.** The index is small and deliberately filtered:
  abuse-blocklisted domains never appear, so a miss can mean "filtered".
- **Submitting an address publishes it.** Anything sent to `/add/` is crawled
  and appears in the public feeds - never submit a target's address.
- Titles and descriptions are the operator's own meta tags: advertising copy,
  not confirmation that a service does anything it claims.
- Clones of ahmia.fi exist; the homepage carries its own MITM warning and the
  only correct onion starts `juhanurmihxlp77` and ends `4csyd.onion`.
- Reading Ahmia is passive; opening a result in Tor Browser is **active** and
  logged by the operator. Indexed pages surface illegal material unbidden,
  downloading it is an offence in most jurisdictions whatever your intent, and
  finding it brings reporting duties - [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [dark.fail](dark-fail.md) - PGP-signed canonical addresses for known services
- [Tor.taxi](tor-taxi.md) - categorised directory, including other onion engines
- [Intelligence X](intelligence-x.md) - archived onion content, by selector
