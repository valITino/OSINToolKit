---
name: pagodo
slug: pagodo
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/opsdisk/pagodo
categories: [web-exploration, dorking]
tags: [dorks, ghdb, automation, proxied]
status: active
status_checked: 2026-08-29
---

# pagodo

## What question does it answer?
I want to run hundreds of GHDB dorks against one domain instead of pasting them into a
search box one at a time. Can that be automated without immediately being blocked?

## When to reach for it
When the dork list is long enough that doing it by hand is not realistic, and you accept
what automation costs. pagodo is two parts: `ghdb_scraper.py` pulls the current GHDB
corpus, and `pagodo.py` runs those dorks and collects results. It is the maintained
successor to the idea [inurlbr](inurlbr.md) represented badly - it handles delays, and
it takes HTTP(S) and SOCKS5 proxies natively, so it does not need wrapping in
proxychains.

Be clear that this is a throughput tool, not a better search. The results are the same
ones you would get by hand; what changes is how many you can ask for before Google stops
answering.

## Install
```bash
git clone https://github.com/opsdisk/pagodo && cd pagodo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python3 ghdb_scraper.py -j -s                      # fetch the current GHDB corpus
python3 pagodo.py -g dorks.txt -d example.com -l 20 -s -e 35.0
python3 pagodo.py -g dorks.txt -d example.com -p socks5h://127.0.0.1:9050
```

## Output
Matching URLs per dork, written to a save file with `-s`. The useful artifact is the
mapping from dork to hits - it tells you *which pattern* found the exposure, which is
what you cite when reporting it.

## Gotchas
- **Scraping Google search results may breach their Terms of Service.** The project says
  so in its own README. That is a decision to make deliberately, and on an authorised
  engagement it is worth confirming your client is content with it.
- **Blocking is the binding constraint, not the tool.** Google serves CAPTCHAs and then
  errors to anything that looks automated. Delays (`-e`) and proxies help; they do not
  make the problem go away, and results silently thin out rather than failing loudly.
- **Scope every run with `-d`.** Without a domain you are searching the whole index and
  collecting other people's exposures, which your authorisation does not cover. See
  [../../LEGAL.md](../../LEGAL.md).
- Proxying through Tor makes blocking *more* likely, not less - exit nodes are heavily
  rate-limited by search engines.
- The corpus is only as current as your last `ghdb_scraper.py` run, and much of the GHDB
  is stale regardless. Empty results are normal.
- Discovery only. A hit tells you a page is indexed; going further is a separate
  activity needing separate authorisation.

## Alternatives
- [Dorking by hand](README.md) - more reliable, and no terms-of-service question
- [GHDB](ghdb.md) - the corpus itself, to pick patterns from
- [inurlbr](inurlbr.md) - the older multi-engine attempt, kept as tier 3 for context
