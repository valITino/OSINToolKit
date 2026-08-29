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
Maintained (Darkdump-4, 2026-04-07) but only half of it belongs here. Its centre
of gravity is discovery - six search engines, passive, because a third party
holds the index, the job [Ahmia](../onion-discovery/ahmia.md) covers. The only
part that touches a target is `-s`: one `requests.get` per result's homepage, no
recursion, no depth, no retained link list, so no crawling, link-graphing or
fingerprinting. Keep it as the triage step between discovery and a real crawl,
then hand to [TorBot](torbot.md) for the link tree, and to a maintained scanner
for fingerprinting - see [OnionScan](onionscan.md).

## When to reach for it
When you hold a term rather than an address and want one command that searches
and then peeks at every hit. Prefer Ahmia alone when you want a single index you
can reason about, and TorBot the moment one result is worth mapping properly.

## Install
```bash
git clone https://github.com/josh0xA/darkdump && cd darkdump   # not on PyPI
chmod +x install.sh && ./install.sh   # Linux/macOS only; makes darkdump-cli
sudo apt install tor                   # socks5h://localhost:9050 is all it uses
```

## Usage
```bash
darkdump-cli -q "acme corp" -a 10   # Ahmia over the clearweb: passive, no Tor
darkdump-cli -q "acme corp" -a 10 -s -p
# same search, then one front-page fetch per result over Tor: the active part
darkdump-cli -q "acme corp" -a 20 -e notevil -p -u -o results.json
# a different engine over its onion, metadata dedupe, JSON to disk
```

## Output
A numbered block per result - title, the engine's description, the onion URL -
and with `-s` a scrape block under each: `Metadata`, `Links Found` (a count),
`Emails Found`, `Documents Found`, plus a local HTML contact sheet with `-i`.
Failures print `Dead onion, skipping...`; `-o` writes JSON, CSV or text by
extension. A candidate list plus a one-page triage: what is up, and which onion
shows a contact string or document worth pulling.

## Gotchas
- **`Dead onion, skipping...` means nothing specific.** A bare `except` wraps
  the whole scrape, so a circuit failure, a timeout, a TLS error and a parse
  error all print that line. Never record a service as dead on it.
- **Every engine's results are silently filtered** against Ahmia's hashed
  blocklist, including engines that filter nothing themselves. Sensible, but
  removed hits are never counted or named: your result set is smaller than the
  engine returned and you are not told by how much.
- Four of the six engines are third-party indexes of unknown freshness, all five
  non-Ahmia engines need `-p`, and every parser is scraped HTML - so an engine
  redesign returns zero results rather than an error.
- **Your query text goes to the engine operators.** No keys and no accounts, but
  searching a target's name discloses your interest to five parties who are not
  the Tor Project. Ignore the README's torrc `ControlPort` step - no code in the
  repo uses a control port, so opening one is a pointless exposure.
- Requirements are pinned to 2024 releases and the scrape path pulls nltk
  corpora on first use, so install into a virtualenv. The image gallery joins
  relative `src` values naively: a missing image is not an absent one. The 2026
  commits are README edits, so treat the code as about a year old.
- **Results and fetched pages surface illegal material unbidden.** Possessing it
  is an offence in most jurisdictions whatever your intent, and finding it
  brings reporting duties - [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [TorBot](torbot.md) - depth, a link tree and per-node status codes
- [Ahmia](../onion-discovery/ahmia.md) - the one engine here worth reasoning
  about, queried directly
- [OnionSearch](../onion-discovery/onionsearch.md) - the older multi-engine
  sweep this replaced, still a map of which engines existed
