---
name: waybackpack
slug: waybackpack
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/jsvine/waybackpack
categories: [history-and-archives, web-archive]
tags: [wayback, snapshots, bulk-download, diffing, python]
status: stale
status_checked: 2026-08-29
---

# waybackpack

## What question does it answer?
I have a URL. I need every version of it on disk, so I can diff them and find
the sentence that quietly changed - or the paragraph that was deleted.

## When to reach for it
When you want the page bodies, not a list of URLs. waybackpack is a thin client
over the same endpoint as [Wayback CDX API](wayback-cdx-api.md), but it fetches
each capture into a timestamped directory, which turns an archive into a diffable
local history. For domain-wide URL enumeration it is the wrong shape - use
[waybackurls](waybackurls.md) or [gau](gau.md); for two or three captures the
Wayback calendar is quicker. The project is stale (below) but still runs.

## Install
```bash
pip install waybackpack   # verified today: 0.6.4, pure Python, only needs requests
```

## Usage
```bash
waybackpack https://example.com/about --list  # size the job: print URLs, fetch nothing

# Every capture to disk, one directory per timestamp; --delay is politeness budget.
waybackpack https://example.com/about -d ./about-history --delay 1

# Diffing setup: --raw is the unmodified original bytes; --uniques-only drops captures
# the CDX API flags as duplicates, so one directory means one real change.
waybackpack https://example.com/terms -d ./terms --raw --uniques-only --delay 1

# A window, thinned to one capture per month, identifying yourself as upstream asks.
waybackpack https://example.com/pricing -d ./pricing --from-date 2019 --to-date 202312 \
  --collapse timestamp:6 --user-agent 'waybackpack; research; you@example.org' --delay 1
```

## Output
A tree keyed by 14-digit Wayback timestamp, then host, then the original path -
`about-history/19961102145216/www.example.com/index.html`, one sibling directory
per capture (`--list` prints to stdout instead and writes nothing). Sort those
directories and diff neighbours: the names are the evidence timeline, so a diff
of two adjacent captures brackets the change to that window. The valuable finds
are deletions - a named executive, a compliance claim, a price, a phone number
present in one capture and gone from the next.

## Gotchas
- **Not archived, but not moving either.** Last commit April 2025, last release
  v0.6.4 in May 2024. It runs today against the current CDX endpoint, but expect
  no fix if that API shifts.
- **`--raw` is a correctness decision, not a preference.** Without it only the
  toolbar, analytics and banner CSS are stripped; every link is still rewritten to
  `/web/<timestamp>/`, and diffs fill with spurious hits from those timestamps.
- **`--uniques-only` can hard-fail** when the CDX API does not honour
  `showDupeCount=true` - it raises rather than degrading. Dedupe on hash instead.
- **It is single-threaded and will happily hammer the Internet Archive.** There is
  no concurrency control beyond `--delay`/`--max-retries`, so always set a delay
  and a real contact address in `--user-agent`. Mirroring a whole site's history
  rather than one page turns passive collection into someone's load problem, and
  copyright and personal-data duties travel with the copy you keep - see
  [../../LEGAL.md](../../LEGAL.md).
- **A timestamp is a crawl date, not a publication date**: the change happened at
  some unknown moment between two captures. Date flags are prefix matches (`2019`,
  `202312`), not the minute precision the README implies.
- **Gaps mean nothing on their own**: robots.txt exclusions, retroactive
  exclusions and takedowns all produce holes. Captured 404s, parking pages and
  redirect interstitials land on disk as ordinary files, so eyeball a few.

## Alternatives
- [Wayback CDX API](wayback-cdx-api.md) - the endpoint underneath; query it directly when you want records rather than files
- [Common Crawl](commoncrawl.md) - archived bodies from a different crawler, to cross-check a gap
- [archive.today](archive-today.md) - when you need a snapshot taken now rather than one from the past
