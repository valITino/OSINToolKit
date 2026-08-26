---
name: BuiltWith
slug: builtwith
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://builtwith.com/
categories: [web-exploration, fingerprinting]
tags: [tech-stack, analytics-ids, ip-history, profiling]
status: unverified
status_checked: 2026-08-26
---

# BuiltWith

## What question does it answer?
I have a domain. What is this site built with, what analytics and advertising IDs
does it carry, and what has its hosting looked like over time?

## When to reach for it
For the profile rather than the scan. BuiltWith works from its own crawl history, so
it answers passively and adds two things a live fingerprinter cannot: **technology
history** (what the site used to run) and the **tracking IDs** embedded in the page.
Those IDs are the pivot - feed them to
[SpyOnWeb](../../06-history-and-archives/analytics-linking/spyonweb.md) to find other
sites owned by the same operator.

## Install
```bash
# Nothing to install - web only. Free tier shows a useful subset.
```

## Usage
```text
https://builtwith.com/example.com      # full technology profile
# Note the Analytics and Advertising sections - the IDs there are the pivot.
```

## Output
Categorised technologies (server, CMS, frameworks, analytics, ads, CDN, email), with
first- and last-detected dates on paid tiers. Also IP and hosting history, and the
tracking identifiers found in the page source.

## Gotchas
- **Detection is inference from page markers** and lags reality - a technology may be
  listed long after removal, or missed entirely behind a CDN or a login wall.
- The detail-rich views (history, full ID lists, reverse lookups) are paywalled; the
  free tier is a summary.
- A shared ID is strong evidence of a shared operator, but check it - agencies and
  templates reuse IDs across unrelated clients.

## Alternatives
- [WhatWeb](whatweb.md) - CLI equivalent, live and current
- [urlscan.io](urlscan-io.md) - what the page actually loads, sandboxed
- [SpyOnWeb](../../06-history-and-archives/analytics-linking/spyonweb.md) - turn an ID into related sites
