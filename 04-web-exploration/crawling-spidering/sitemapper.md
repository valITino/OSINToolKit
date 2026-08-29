---
name: Visual Site Mapper (sitemapper-nodejs)
slug: sitemapper
tier: 3
contact: active
type: web
cost: free
platforms: [linux, macos]
url: https://github.com/alentum/sitemapper-nodejs
categories: [web-exploration, crawling-spidering]
tags: [sitemap, link-graph, legacy, self-hosted]
status: broken
status_checked: 2026-08-29
---

# Visual Site Mapper (sitemapper-nodejs)

## What question does it answer?
I have an old methodology write-up or link list naming "Visual Site Mapper" as the
way to see a site's link graph. Is that service, or the code behind it, still
usable? No - the hosted site returns 503 and the repository has two commits, both
from December 2016.

## Why this is tier 3
Recognition only. Despite how it is usually listed, this repository is not a Node
crawler that emits an XML sitemap: it is the AGPL-3.0 server source of the Visual
Site Mapper web service - an Express front end plus a MongoDB-backed crawler
worker - untouched since 2 December 2016. For the crawl-then-diff workflow this
directory is about, use [katana](katana.md) or [hakrawler](hakrawler.md), or
SiteOne Crawler (`https://github.com/janreges/siteone-crawler`), maintained and
writing `sitemap.xml` and `sitemap.txt`.

## When to reach for it
Do not reach for it to do work. Read this entry when the name surfaces in someone
else's methodology, confirm it is dead, and move on. Nothing free and maintained
reproduces its visual link graph, so if you want the picture rather than the
inventory it is a paid sitemap service or drawing it yourself from crawler output.

## Install
```bash
git clone https://github.com/alentum/sitemapper-nodejs.git   # only distribution
# Not on npm (private package.json, no bin) and no releases. Needs MongoDB, PM2,
# 2015-era npm and bower deps, and gulp 3.9, which builds on no supported Node.
```

## Usage
```bash
# Upstream documents nothing; these are read off pm2-apps.json and package.json.
npm install && bower install && gulp build  # gulp 3.9 fails on any modern Node
pm2 start pm2-apps.json   # needs mongod: starts "web" (Express) and "worker"
curl -sI https://www.visualsitemapper.com/  # the hosted instance: 503 on 2026-08-29
```

## Output
Not observed: the hosted service 503s and the application would not stand up. From
the repository layout, `worker/` crawls and stores the page-and-link graph in
MongoDB while `web/` renders it as a force-directed graph, pages as nodes and
links as edges. It was read for outliers rather than inventory - the weakly
connected pages at the edge. Nothing about it is diffable: no sitemap, no CLI.

## Gotchas
- **It is not what link lists say it is**, and `npm install sitemapper` installs an
  unrelated package (a parser for existing sitemap files). Neither is evidence for
  the other; writing this tool up from the description alone documents a fiction.
- **Two commits, both 2 December 2016**, and the repository is not archived, so it
  looks alive at a glance. Nothing merged, tagged or released since.
- **The service is down though DNS still resolves** - HTTPS reset, HTTP 503, and
  reports put it offline since about May 2023. A live record proves nothing.
- Even when it worked it mapped a capped number of pages and only linked ones: an
  orientation picture, never an inventory. Orphaned pages are absent by definition.
- **Self-hosting changes the contact level**: Alentum's servers did the fetching,
  whereas the worker crawls from your own infrastructure and needs authorisation
  like any crawl (see [../../LEGAL.md](../../LEGAL.md)). AGPL-3.0 also obliges you
  to offer source to anyone you expose an instance to.
- This repo's entry at
  [../monitoring-visual/visualsitemapper.md](../monitoring-visual/visualsitemapper.md)
  still describes the hosted service as usable; it pre-dates the outage.

## Alternatives
- [katana](katana.md) - a maintained crawl that yields a URL list you can diff
- [hakrawler](hakrawler.md) - fastest route to a flat list of what a site links to
- [Photon](photon.md) - crawl output organised into artifact types, still working
