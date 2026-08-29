---
name: VisualSiteMapper
slug: visualsitemapper
tier: 3
contact: passive
type: web
cost: free
platforms: [web]
url: https://www.visualsitemapper.com/
categories: [web-exploration, monitoring-visual]
tags: [sitemap, visual, structure, legacy, shut-down]
status: broken
status_checked: 2026-08-29
---

# VisualSiteMapper

## What question does it answer?
Older methodology write-ups name VisualSiteMapper as the quick way to see a
site's link graph - which pages are central, which are barely linked. Is it
still there? No.

## Why this is tier 3
The service is shut down. As of 2026-08-29 `http://www.visualsitemapper.com/`
answers `301 Moved Permanently` with
`Location: https://github.com/alentum/sitemapper-nodejs`, and the HTTPS site
does not complete a connection at all: the author has replaced the product with
a pointer to its own source. That source is the service's server code - an
Express front end and a MongoDB-backed crawler worker, AGPL-3.0, two commits,
last touched in December 2016 - not a drop-in sitemap generator, and running it
means standing up the whole stack yourself.

It stays in the repo because it is still listed as live in plenty of OSINT
roundups. If you find it recommended, this is why it does nothing.

## Install
```bash
# Nothing to install, and nothing to use. The hosted service redirects to:
#   https://github.com/alentum/sitemapper-nodejs   (server source, 2016, AGPL-3.0)
```

## Usage
```text
https://www.visualsitemapper.com/     # redirects to the repository; no map is built
```

## Output
None. Previously an interactive graph of pages as nodes and links as edges, with
heavily linked pages positioned centrally.

## Gotchas
- **The redirect is the tell.** A tool page that sends you to its own source
  repository is a discontinued product, not a maintained one - check for that
  pattern before trusting any long-lived free web tool in a methodology list.
- Even when it ran, it mapped a limited number of pages and followed only what
  was linked: an overview, never an inventory.
- Self-hosting the 2016 source means an unmaintained Node and MongoDB stack
  exposed to whatever it crawls. Treat it as archive material.

## Alternatives
- [katana](../crawling-spidering/katana.md) - a maintained crawl you can diff
- [hakrawler](../crawling-spidering/hakrawler.md) - fast flat list of linked URLs
- [Photon](../crawling-spidering/photon.md) - crawl output split into artifact types
- [gowitness](gowitness.md) - the visual overview, as screenshots of every host
