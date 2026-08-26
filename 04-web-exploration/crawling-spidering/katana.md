---
name: katana
slug: katana
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/projectdiscovery/katana
categories: [web-exploration, crawling-spidering]
tags: [crawler, javascript, headless, endpoints]
status: unverified
status_checked: 2026-08-26
---

# katana

## What question does it answer?
What URLs and endpoints does this site actually expose - including the ones that only
appear when JavaScript runs?

## When to reach for it
The modern crawler, and the right choice for single-page applications. Its headless
mode drives a real browser, so it sees routes and API calls that a plain HTTP crawler
misses entirely. It also parses JavaScript files for endpoint strings. Use it to
build the URL inventory that feeds screenshotting, fuzzing, or manual review.

## Install
```bash
go install github.com/projectdiscovery/katana/cmd/katana@latest
```

## Usage
```bash
katana -u https://example.com                        # standard crawl
katana -u https://example.com -headless -jc          # headless browser + parse JS for endpoints
katana -u https://example.com -d 3 -rl 20 -o urls.txt # depth cap, rate limit, save
echo https://example.com | katana -silent | gowitness file -f -   # pipeline into screenshots
```

## Output
A stream of discovered URLs, one per line, ready to pipe. `-jsonl` gives structured
records including the source that referenced each URL, which helps you show where a
finding came from.

## Gotchas
- Crawling is **active** - every discovered URL is a request to the target. Use
  `-rl` and `-d` to bound it, and get authorisation for anything sustained.
- Headless mode is much heavier on both your machine and the target; reserve it for
  sites that genuinely need it.
- Crawlers follow links, including logout and destructive-action links. Scope with
  `-fs`/exclusion filters when the target has authenticated state.
- Respect `robots.txt` as an ethical baseline even though the tool need not.

## Alternatives
- [Photon](photon.md) - extracts emails, keys, and files while crawling
- [Wayback CDX](../../06-history-and-archives/web-archive/wayback-cdx-api.md) - historical URLs, zero contact
- [gowitness](../monitoring-visual/gowitness.md) - screenshot what you found
