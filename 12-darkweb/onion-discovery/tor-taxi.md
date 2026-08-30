---
name: Tor.taxi
slug: tor-taxi
tier: 3
contact: passive
type: web
cost: free
platforms: [web]
url: https://tor.taxi/
categories: [darkweb, onion-discovery]
tags: [tor, onion, directory, pgp, warrant-canary]
status: active
status_checked: 2026-08-29
---

# Tor.taxi

## What question does it answer?
I have a site name, or only a category - onion search engines, forums, email
hosts, information sites. Which addresses does this directory list, and do they
match the one I already hold?

## Why this is tier 3
Alive, PGP-signed and broader than dark.fail (about 55 addresses across eleven
categories), but situational: there is no per-link or page-level "last checked"
value anywhere, only red and orange link colouring, so nothing taken from it can
be dated, while dark.fail stamps its refreshes in UTC. Use it to corroborate.

Use it as a second opinion on an address, and for the categories
[dark.fail](dark-fail.md) leaves out - its Search Engines section is itself a
source of further onion-discovery engines. Use it after dark.fail, not instead.

## Install
```bash
# None: static clearweb page, no JavaScript, no account. You need GnuPG to
# check the signed files, and Tor Browser to open anything listed:
sudo apt install gnupg          # see ../access-and-opsec/tor-browser.md
```

## Usage
```text
https://tor.taxi/   # the directory: v3 onions in named categories, one of
  # which points at further onion search engines
https://tor.taxi/mirrors.txt   # PGP-signed list of the only two canonical
  # locations - check any tor.taxi-branded domain a search engine handed you
https://tor.taxi/canary.txt   # PGP-signed warrant canary carrying a Monero
  # block hash, last signed 1 June 2026 under a 120-day refresh promise
https://tor.taxi/journal   # narrative history of which services existed when
```

## Output
A single no-JavaScript page, entries grouped into named categories, each a site
name linking to a v3 onion. Availability is colour only - red for prolonged
downtime, orange for a DDoS or maintenance. Read it as a name-to-address map
plus a rough health signal, then corroborate the address against dark.fail or
the operator's own signed mirrors before acting on it.

## Gotchas
- **Nothing here can be dated.** Colour says "down for a while" with no
  timestamp; cross-check dark.fail before putting a status in a report.
- **Check the canary before trusting the listings.** It promises a refresh
  within 120 days; a stale canary means the integrity guarantee has lapsed.
- **Extensive typosquatting.** Hyphenated and .org lookalikes rank in search
  results and are absent from the signed `mirrors.txt`; anything not in that
  file is a clone, and clones are where substituted addresses come from.
- Curated by hand with no published criteria: presence is not endorsement and
  absence proves nothing.
- **It lists live criminal services.** Fetching the directory is passive;
  opening a listing is active, logged by the operator, may be unlawful whatever
  your intent, and can put illegal material in front of you unbidden, which
  brings reporting duties. Clear it first - [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [dark.fail](dark-fail.md) - fewer entries, signed, and timestamped
- [Ahmia](ahmia.md) - keyword search and a bulk seed list, no name needed
- [Intelligence X](intelligence-x.md) - archived onion content, by selector
