---
name: VisualSiteMapper
slug: visualsitemapper
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://www.visualsitemapper.com/
categories: [web-exploration, monitoring-visual]
tags: [sitemap, visual, structure, orphan-pages]
status: unverified
status_checked: 2026-08-26
---

# VisualSiteMapper

## What question does it answer?
How is this site structured - which pages are central, which are barely linked, and
where does the link graph cluster?

## When to reach for it
For orientation on an unfamiliar site, and specifically to spot the outliers. A
visual link graph makes weakly-connected pages obvious in a way a crawl log does not,
and those loosely-linked corners are often where the interesting material sits.
Quick, requires nothing, and produces a picture worth pasting into a report.

## Install
```bash
# Nothing to install - web only.
```

## Usage
```text
https://www.visualsitemapper.com/     # enter the domain and let the map build
```

## Output
An interactive graph of pages as nodes and links as edges, with more heavily linked
pages positioned centrally.

## Gotchas
- It maps a **limited number of pages** and follows only what is linked - it is an
  overview, not an inventory. Use a crawler ([katana](../crawling-spidering/katana.md))
  for completeness.
- Truly orphaned pages, by definition, are not linked and will not appear. For those
  use [Wayback CDX](../../06-history-and-archives/web-archive/wayback-cdx-api.md) or
  authorised content discovery.
- The service fetches the target itself, so your IP is not the one crawling, but the
  target may still see the service's crawl.
- Octopus.do and similar sitemap tools cover the same ground.

## Alternatives
- [katana](../crawling-spidering/katana.md) - a real crawl, scriptable
- [gowitness](gowitness.md) - what each page looks like, in bulk
