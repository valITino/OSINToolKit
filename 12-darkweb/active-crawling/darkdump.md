---
name: darkdump
slug: darkdump
tier: 3
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/josh0xA/darkdump
categories: [darkweb, active-crawling]
tags: [tor, onion, search-engines, triage, scraping]
status: active
status_checked: 2026-08-29
---

# darkdump

## What question does it answer?
I have a keyword, a brand or an email address. Which onions come back for it
across six dark-web search engines, which of those are answering right now, and
what is on each one's front page - contact strings, document links, meta tags?

## Why this is tier 3
Maintained (Darkdump-4, 2026-04-07) but only half of it belongs here: its centre
of gravity is discovery - six passive search engines, the job
[Ahmia](../onion-discovery/ahmia.md) covers. The only part that touches a target
is `-s`: one `requests.get` per result's homepage, no recursion, so no crawling
or fingerprinting. Use it for triage, then [TorBot](torbot.md).

Reach for it when you hold a term rather than an address, and want one command
that searches and then peeks at every hit.

## Install
```bash
git clone https://github.com/josh0xA/darkdump && cd darkdump   # not on PyPI
chmod +x install.sh && ./install.sh   # Linux/macOS only; makes darkdump-cli
sudo apt install tor                   # socks5h://localhost:9050 is all it uses
```

## Usage
```bash
darkdump-cli -q "acme corp" -a 10   # Ahmia over the clearweb: passive, no Tor
darkdump-cli -q "acme corp" -a 10 -s -p   # -s fetches each hit over Tor
darkdump-cli -q "acme corp" -a 20 -e notevil -p -u -o results.json
# a different engine over its onion, metadata dedupe, JSON to disk
```

## Output
A numbered block per result - title, the engine's description, the onion URL -
and with `-s` a scrape block under each: `Metadata`, `Links Found` (a count),
`Emails Found`, `Documents Found`, plus a local HTML contact sheet with `-i`.
`-o` writes JSON, CSV or text by extension. Read it as a candidate list plus
triage: what is up, and which onion shows a contact string worth pulling.

## Gotchas
- **`Dead onion, skipping...` means nothing specific.** A bare `except` wraps
  the scrape, so a timeout or parse error prints it. Never record it as dead.
- **Every engine's results are silently filtered** against Ahmia's hashed
  blocklist, including engines that filter nothing themselves. Removed hits are
  never counted or named: your result set is smaller than the engine returned.
- Four of the six engines are third-party indexes of unknown freshness, all five
  non-Ahmia engines need `-p`, and every parser is scraped HTML - so an engine
  redesign returns zero results rather than an error.
- **Your query goes to the engine operators.** No accounts, but searching a
  target's name discloses your interest to five parties. Ignore the README's
  torrc `ControlPort` step - no code uses one, so it is exposure for nothing.
- Requirements are pinned to 2024 releases and the scrape path pulls nltk
  corpora on first use, so install into a virtualenv. The image gallery joins
  relative `src` values naively: a missing image is not an absent one. The 2026
  commits are README edits, so treat the code as about a year old.
- **Results and fetched pages surface illegal material unbidden.** Possessing it
  is an offence in most jurisdictions whatever your intent, and finding it
  brings reporting duties - [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [TorBot](torbot.md) - depth, a link tree and per-node status codes
- [Ahmia](../onion-discovery/ahmia.md) - one index you can reason about
- [OnionSearch](../onion-discovery/onionsearch.md) - the older sweep it replaced
