---
name: gau
slug: gau
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/lc/gau
categories: [history-and-archives, web-archive]
tags: [urls, archive, commoncrawl, otx, pipeline]
status: unverified
status_checked: 2026-08-26
---

# gau

## What question does it answer?
Every known URL for this domain, gathered from **several** archive and threat-intel
sources at once - not just the Wayback Machine.

## When to reach for it
When coverage matters more than simplicity. gau ("get all urls") queries the Wayback
Machine, Common Crawl, and other providers such as AlienVault OTX, then merges the
results. Common Crawl in particular indexes pages Wayback missed, so gau routinely
returns URLs [waybackurls](waybackurls.md) does not. Use it as the broader sweep and
waybackurls when you want only the archive's own view.

## Install
```bash
go install github.com/lc/gau/v2/cmd/gau@latest
```

## Usage
```bash
gau example.com | sort -u > urls.txt                  # all sources, de-duplicated
gau --subs example.com                                 # include subdomains
gau --blacklist png,jpg,gif,css example.com            # drop static noise
gau --from 202301 example.com                          # only captures from 2023 onward
```

## Output
URLs on stdout, one per line, merged across sources. `--json` includes which provider
supplied each URL, which is worth keeping when provenance matters.

## Gotchas
- Sources have independent rate limits; large domains can take a while or return
  partial results. Re-run before concluding a set is complete.
- Like waybackurls, these are **historical** URLs - most may no longer resolve.
- Coverage varies by source and by how well-crawled the site was. Absence proves
  nothing.
- Some providers benefit from API keys for higher limits.

## Alternatives
- [waybackurls](waybackurls.md) - simpler, Wayback only
- [Wayback CDX API](wayback-cdx-api.md) - precise filtering and dedup
- [katana](../../04-web-exploration/crawling-spidering/katana.md) - crawl the live site instead
