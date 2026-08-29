---
name: OnionSearch
slug: onionsearch
tier: 3
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/megadose/OnionSearch
categories: [darkweb, onion-discovery]
tags: [tor, onion, search-engine, scraper, csv, legacy]
status: stale
status_checked: 2026-08-29
---

# OnionSearch

## What question does it answer?
I have a keyword and a list of onion search engines. Which of them return a hit
for it, collected into one CSV - and, read honestly in 2026, which of those
engines still exist at all?

## When to reach for it
Only for a one-command sweep of the historical onion search engines, read
sceptically. For discovery today query [Ahmia](ahmia.md) or use darkdump; for a
site you can already name, use [dark.fail](dark-fail.md).

## Why this is tier 3
Last functional commit October 2022, last PyPI release October 2021, and nine of
its seventeen engines are provably unreachable: eight are 16-character v2
addresses, refused by Tor since 0.4.6.x in October 2021, and darksearch.io has
no DNS record as of 2026-08-29. The pip build is worse - its `ahmia` entry is
the dead v2 address. Keep it for name recognition and as a historical map of the
onion search engines; today use darkdump (https://github.com/josh0xA/darkdump).

## Install
```bash
pip install git+https://github.com/megadose/OnionSearch.git  # master, v3 Ahmia
pip3 install onionsearch   # PyPI 1.3 from 2021-10-22, ships the dead v2 Ahmia
# The README's `python3 setup.py install` is dead advice - setuptools 80 (2025)
# removed it. No apt, no Docker image. Bring your own Tor SOCKS proxy on
# 127.0.0.1:9050 (--proxy to change), or every engine says "Connection refused".
```

## Usage
```bash
onionsearch "acme corp" --engines ahmia onionland tor66 haystack --limit 5
# the only sane modern invocation: restrict to engines that could still exist
onionsearch "computer" --continuous_write True --fields engine name link domain
# stream results to disk as they arrive and add a bare-domain column; add
# --mp_units 1 so one hung onion cannot scramble the progress bars
```

## Output
A CSV, default `output_$SEARCH_$DATE.txt`, columns "engine", "name of the link",
"url", plus a domain column with `--fields ... domain`; progress is tqdm bars on
stderr. Pivot on the engine column: if one or two engines gave you every row,
that is one source with duplicates, not corroboration. Deduplicate on domain.

## Gotchas
- **Empty results mean dead engines, not an absent target.** Nine of seventeen
  cannot answer, and they surface as connection errors, never as "retired".
- **pip and GitHub ship different code.** Check with `grep '"ahmia"'
  <site-packages>/onionsearch/core.py`; it must show the 56-character v3 address
  starting `juhanurmihxlp77`, not a 16-character v2 one.
- **This is active contact.** Every query is a live request to third-party onion
  engines of unknown provenance whose operators see your search terms, so
  searching a target's name discloses your interest.
- `--continuous_write` is argparse `type=bool`, so any value is truthy, even
  `False`; `core.py` runs argparse at import, so it is not importable either.
- Results point at services hosting illegal material, which appears unbidden
  when you open one; downloading it is an offence in most jurisdictions whatever
  your intent, and finding it brings reporting duties -
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Ahmia](ahmia.md) - the one engine in the table that is definitely alive
- [dark.fail](dark-fail.md) - signed addresses when you know the site's name
- [Intelligence X](intelligence-x.md) - archived onion content, by selector
