---
name: archive.today
slug: archive-today
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://archive.today/
categories: [history-and-archives, web-archive]
tags: [snapshot, on-demand, javascript, contested]
status: active
status_checked: 2026-08-26
---

# archive.today

## What question does it answer?
This page is about to be edited or deleted, and the Wayback Machine will not capture it.
Can I still get a timestamped copy?

## When to reach for it
For pages the Internet Archive will not take. archive.today **renders JavaScript** and
stores a flattened visual copy, so single-page apps and social posts archive correctly
rather than as an empty shell, and it does not honour `robots.txt` or retroactive
exclusion requests - so it captures material Wayback declines and keeps it after a site
owner objects.

**Read the Gotchas before using it.** Since January 2026 this is no longer a neutral
utility: Wikipedia banned it, and merely loading its pages can conscript your browser
into an attack on a third party. Use [Wayback](wayback-cdx-api.md) as your default and
come here deliberately, for a specific page Wayback cannot hold, on a machine and
network where that risk is acceptable.

## Install
```bash
# Nothing to install - web only, no account, and no API.
```

## Usage
```text
https://archive.today/                       # paste a URL to capture, or search snapshots
https://archive.today/newest/<URL>            # most recent snapshot of a page
https://archive.today/<YYYY>/<URL>            # snapshots from a given year
```

## Output
A permanent short URL for the snapshot, plus a rendered screenshot and a text copy, with
the capture timestamp shown - which is what makes it citable.

## Gotchas
- **In January 2026 Wikipedia banned archive.today for webpage archival**, after a DDoS
  that the service itself orchestrated: its CAPTCHA page was modified so that visitors'
  browsers repeatedly hammered a third party's blog. At the time it was the
  second-largest archiving service across Wikimedia projects. Treat visiting it as an
  operational risk to your own machine and network, not just a browsing choice. It had
  also been blacklisted once before, in 2013.
- **Its evidentiary standing is now contested.** A snapshot from a service banned by a
  major platform for hostile behaviour is weaker in a report than it was, and opposing
  counsel or an editor can say so. Where a Wayback capture exists, cite that instead.
- **Different resolvers return different addresses for it.** Checked the same day,
  Cloudflare's `1.1.1.1` returned `104.36.80.106` and Google's `8.8.8.8` returned
  `107.189.8.227`. "It is down" often means "your resolver disagrees".
- **It blocks datacenter and automated clients**, resetting connections outright, so a
  link checker reporting failure here says nothing. There is **no API** - its Memento
  support was retired - and scraping it means fighting an actively hostile anti-bot layer.
- **Submitting a URL makes archive.today fetch the target** from its infrastructure. The
  target's logs still record a visit, and an operator watching for archive requests will
  know they were seen.
- Ownership is opaque, and in October 2025 the FBI subpoenaed its registrar to identify
  the domain's owner. Weigh that before submitting sensitive URLs.
- `archive.today`, `.ph`, `.is`, `.li` and `.vn` are mirrors of one archive.

## Alternatives
- [Wayback CDX API](wayback-cdx-api.md) - the default: scriptable, broader, uncontested
- [gau](gau.md) - every historical URL for a domain, from several archive sources
- [gowitness](../../04-web-exploration/monitoring-visual/gowitness.md) - take your own screenshots, under your own control
