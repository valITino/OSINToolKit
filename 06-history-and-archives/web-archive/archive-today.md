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
tags: [snapshot, on-demand, evidence, javascript]
status: active
status_checked: 2026-08-26
---

# archive.today

## What question does it answer?
This page is about to be edited or deleted. Can I make a timestamped copy right now
that the operator cannot reach into and change?

## When to reach for it
When you need a snapshot *on demand* and one the target cannot retract. Two properties
make it the standard complement to the
[Wayback Machine](wayback-cdx-api.md):

It **renders JavaScript** and stores a flattened visual copy, so single-page apps,
social posts, and anything assembled client-side archive correctly rather than as an
empty shell. And it does not honour `robots.txt` or retroactive exclusion requests, so
it captures pages the Internet Archive will not, and keeps them after a site owner
objects. For evidence preservation that is the whole point.

Use it the moment you find something that matters, before you finish reading it.

## Install
```bash
# Nothing to install - web only, no account, no API.
```

## Usage
```text
https://archive.today/                       # paste a URL to capture, or to search existing snapshots
https://archive.today/newest/<URL>            # jump to the most recent snapshot of a page
https://archive.today/<YYYY>/<URL>            # snapshots from a given year
```

## Output
A permanent short URL for the snapshot, plus a rendered screenshot and a text copy of
the page. The snapshot page shows the capture timestamp, which is what makes it citable
in a report.

## Gotchas
- **Different DNS resolvers return different addresses for it**, and that is why the
  "archive.today is down" reports are so inconsistent. Checked here on the same day,
  Cloudflare's `1.1.1.1` returned `104.36.80.106` while Google's `8.8.8.8` returned
  `107.189.8.227`. If the site will not load, try another resolver before concluding
  anything.
- **It aggressively blocks datacenter and automated clients** - connections from
  VPN, cloud, and proxy addresses are frequently reset outright. That is not evidence
  the service is down, and a link checker reporting failure here means nothing.
- **There is no API.** Captures and lookups are browser work; you cannot script this the
  way you can script [Wayback CDX](wayback-cdx-api.md).
- `archive.today`, `archive.ph`, `archive.is`, `archive.li` and `archive.vn` are mirrors
  of the same archive. If one is unreachable, try another.
- **Submitting a URL makes archive.today fetch the target**, from its infrastructure
  rather than yours. Convenient for OPSEC, but the target's logs still record a visit -
  and a sophisticated operator watching for archive requests will know they were seen.
- Some sites detect and serve it a paywall or block page; the snapshot then preserves
  the block, not the content.
- Record the snapshot URL and its timestamp in your notes at capture time - see
  [../../00-methodology/documentation/README.md](../../00-methodology/documentation/README.md).

## Alternatives
- [Wayback CDX API](wayback-cdx-api.md) - scriptable, historical, and vastly broader
- [gau](gau.md) - every historical URL for a domain, from several archive sources
- [gowitness](../../04-web-exploration/monitoring-visual/gowitness.md) - take your own screenshots at scale
