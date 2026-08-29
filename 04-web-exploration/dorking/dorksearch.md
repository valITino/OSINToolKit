---
name: DorkSearch
slug: dorksearch
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://dorksearch.com/
categories: [web-exploration, dorking]
tags: [dorks, ghdb, query-builder, library, multi-engine]
status: active
status_checked: 2026-08-29
---

# DorkSearch

## What question does it answer?
I have a target and a rough idea of what I want to find, but not the operator
syntax. Can something build the dork for me, and hand me a vetted library to
pick from instead of my remembering GHDB entries?

## When to reach for it
When you are composing queries rather than running hundreds of them: a builder
that walks operator by operator, a library filtered by words in the query or
description, and an engine selector that opens the finished dork in Google,
Bing, DuckDuckGo, Brave, Startpage, Yahoo, Yandex or Baidu - the cheap way to
follow the vary-your-engine advice in the [operator list](README.md). It is not
automation and never runs a search for you; when the list is too long to click
through, that is [pagodo](pagodo.md)'s job, with the costs that implies.

## Install
```bash
# None - browser app, no account, no API key. Its SPA endpoints answer
# unauthenticated if you want the corpus offline.
```

## Usage
```text
https://dorksearch.com/builder?q=site%3Aexample.com+filetype%3Apdf&engine=Google
  # the app's own share-link format: prefill the builder, preselect the engine
curl -s 'https://dorksearch.com/api/dorks?type=Files%20Containing%20Passwords&is_core=true&page_size=100&page=1' | jq -r '.items[].query'
  # export one curated category (395 entries) as a list to scope with site: yourself
curl -s 'https://dorksearch.com/api/dorks?q=index+of&page_size=50&page=1' | jq -r '.items[].query'   # 2,306 matches
```

## Output
In the browser: the dork under construction, an engine selector, category
tiles, and a library modal toggling between the curated core set and the
extended community one. Clicking through opens the query in the chosen engine
in a new tab. Via the API: `{"total":889529,"items":[{"id":1,"query":"...",
"description":"...","is_core":true}]}`.

Read `is_core: true` as the GHDB-quality corpus and the rest as unvetted bulk.
The `description` is the submitter's original note, and often explains what the
dork was really for - read it first, because plenty describe exploiting
software rather than finding a document.

## Gotchas
- **The 889,529 headline is misleading.** Only the `is_core` subset - a few
  thousand entries mirroring GHDB's categories - is curated; the rest is
  bulk-scraped, "Cryptocurrency / Wallets" alone holding 69,658 unvetted
  entries. Filter on `is_core`, or read noise.
- **It builds queries, it does not run them.** The rate limiting, CAPTCHAs and
  terms-of-service exposure land on you and your IP the moment you click
  through; its own guidance is not to automate high-volume scanning.
- The core corpus inherits GHDB's problems - decades-old entries, dead CMS
  versions, patterns written for exploitation rather than discovery. A dork
  returning nothing usually means the software is extinct, not that the
  target is clean. Same caveat as [GHDB](ghdb.md).
- The `/api/dorks`, `/api/types` and `/api/ai/dork` endpoints are internal to
  the app: undocumented, unauthenticated, unversioned, behind Cloudflare and a
  client-rendered shell. Fine for a one-off export, not a foundation, and with
  no stated quota comes no guarantee - keep your own copy of what you need.
- The AI assist writes plausible-looking dorks validated against no engine, and
  one that quietly matches nothing looks exactly like a clean target.
- Scope every query with `site:`. Unscoped, you collect other people's
  exposures, and personal data in results carries GDPR obligations - see
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [GHDB](ghdb.md) - the upstream corpus, authoritative but without the builder
- [pagodo](pagodo.md) - when the list needs running, not composing
- [Dorking by hand](README.md) - the operators themselves, and the discipline
