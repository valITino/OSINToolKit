---
name: Wayback CDX API
slug: wayback-cdx-api
tier: 1
contact: passive
type: api
cost: free
platforms: [web]
url: https://web.archive.org/
categories: [history-and-archives, web-archive]
tags: [wayback, cdx, historical-urls, archive]
status: unverified
status_checked: 2026-08-26
---

# Wayback CDX API

## What question does it answer?
I have a domain. Every URL the Internet Archive ever captured for it - including
deleted pages, old endpoints, and forgotten files - what are they, as a greppable
list?

## When to reach for it
When you want history, not the live site: pages that were removed, a staging path
that leaked once, an old `robots.txt`, a since-deleted PDF. The CDX endpoint is the
underused, scriptable side of the Wayback Machine - it returns raw capture records
you can filter, where the browsable calendar cannot. Feed the output to
[waybackurls](waybackurls.md)/[gau](gau.md) workflows or grep it directly.

## Install
```bash
# Nothing to install - it is an HTTP endpoint.
```

## Usage
```bash
# Every captured URL under the domain, de-duplicated by content digest:
curl -s 'https://web.archive.org/cdx/search/cdx?url=example.com*&collapse=digest&output=text&fl=original' | sort -u

# Only captures of a given type, since a given year:
curl -s 'https://web.archive.org/cdx/search/cdx?url=example.com*&filter=mimetype:application/pdf&from=2018'
```

## Output
One line per capture with the fields you request (`fl=`): original URL, timestamp,
MIME type, HTTP status, digest. `collapse=digest` removes captures whose content
did not change, so you get distinct pages rather than thousands of near-duplicates.

## Gotchas
- **Google and Bing web cache were both discontinued in 2024. Wayback is the
  fallback** for "what did this page used to say." Plan around it.
- Large domains return huge result sets - always `collapse=digest` and filter by
  `mimetype`/`from`/`to`, or paginate, rather than pulling everything.
- A capture existing does not mean the resource is still live; cross-check before
  acting on an old URL.

## Alternatives
- [waybackurls](waybackurls.md) / [gau](gau.md) - CLI wrappers over the same data
- [SpyOnWeb](../analytics-linking/spyonweb.md) - link sites by shared analytics IDs over time
