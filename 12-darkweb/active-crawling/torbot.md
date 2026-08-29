---
name: TorBot
slug: torbot
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/DedSecInside/TorBot
categories: [darkweb, active-crawling]
tags: [tor, onion, crawler, link-graph, contact-extraction]
status: active
status_checked: 2026-08-29
---

# TorBot

## What question does it answer?
I have a .onion address. What does it link out to one or two hops deep, which
of those pages are alive right now, and do any of them carry an email address
or phone number I can pivot on?

## When to reach for it
The default first crawl once you hold an address and want adjacency rather than
one page: it walks the link tree, records a status per node and pulls contact
strings as it goes. Not for triaging search hits - that is
[darkdump](darkdump.md), one front page each - nor for fingerprinting, which is
[OnionScan](onionscan.md) and the rewrite it names. And not when a crawl must
stay inside one host: TorBot has no scope filter and no delay, so point
[katana](../../04-web-exploration/crawling-spidering/katana.md) at a SOCKS proxy
instead.

## Install
```bash
pip install torbot   # PyPI 4.3.0 (2026-07-28), Python >=3.9, `torbot` script
sudo apt install tor  # TorBot never starts Tor; it expects 127.0.0.1:9050
# dev-branch extras 4.3.0 lacks: clone the repo, venv, then pip install -e .
```

## Usage
```bash
torbot -u http://<v3addr>.onion --depth 1 --visualize table
# one hop of outbound links as a table; --depth defaults to 1
torbot -u http://<v3addr>.onion --depth 2 --save json
# writes the tree to '<page title> - Depth 2.json' - check where it landed
torbot --host 127.0.0.1 --port 9150 -u http://<v3addr>.onion --info
# emails, file links, robots.txt, scripts - via Tor Browser's SOCKS port
```

## Output
One row per node - Title / URL / Status / Phone Numbers / Emails / Category -
colour-coded green 2xx, amber 3xx, red for the rest. `--visualize tree` prints
the same nodes as an ASCII tree, `--save json` as treelib JSON. Read it as
reachability plus adjacency: which mirrors answer, what links to what, and where
contact strings surface.

## Gotchas
- **The Category column is junk here.** A TF-IDF classifier trained on a bundled
  1,408-row clearnet dataset of 16 generic labels, with no marketplace, forum or
  ransomware class; a test run labelled example.com "Business/Corporate" and a
  bare 301 page "Computers and Technology". Never cite it in a report.
- **No scope, no delay, no robots.txt.** It takes every absolute http(s) href
  with no host filter - depth 1 on example.com followed off-site to iana.org -
  so `--depth 2` fans out across other onions and the clearweb, unpaused and
  conspicuous in the operator's logs.
- **The PyPI build does not match its own README.** `analyze`, `--save result`,
  `--keyword` and the LLM flags landed after the 4.3.0 tag, which offers only
  `--save {tree,json}`; check `torbot --help` before copying from the docs.
- **`--disable-socks5` sends unproxied requests.** Never combine it with an
  onion target or anything you must not reach from your own IP.
- `--save` writes into the installed package directory, not your cwd, named from
  the page title, so an empty-looking crawl may be a failed write. Depth costs:
  sequential fetches, 60 s each, and a timed-out circuit reads as a dead page.
- **Active contact, with real legal exposure.** The operator sees your requests,
  User-Agent and crawl pattern, and a crawl stores whatever is served. Illegal
  material appears unbidden; possessing it is an offence in most jurisdictions
  whatever your intent, and finding it brings reporting duties -
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [darkdump](darkdump.md) - search engines first, then one front page per hit
- [OnionScan](onionscan.md) - fingerprint a service instead of mapping its links
- [katana](../../04-web-exploration/crawling-spidering/katana.md) - scoped,
  maintained crawler pointed at a SOCKS proxy
- [torsocks](../access-and-opsec/torsocks.md) - torify a crawler with no proxy
  support of its own
