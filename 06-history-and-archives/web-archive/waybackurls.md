---
name: waybackurls
slug: waybackurls
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/tomnomnom/waybackurls
categories: [history-and-archives, web-archive]
tags: [wayback, urls, historical, pipeline]
status: unverified
status_checked: 2026-08-26
---

# waybackurls

## What question does it answer?
Every URL the Wayback Machine knows for this domain, on stdout, ready to pipe -
without me writing a CDX query.

## When to reach for it
When you want archived URLs inside a shell pipeline. It wraps the
[Wayback CDX API](wayback-cdx-api.md) in the simplest possible interface: domain in,
URLs out. That makes it the natural first stage before grepping for interesting
extensions, checking which paths still resolve, or feeding a fuzzer's wordlist with
paths the site genuinely used.

## Install
```bash
go install github.com/tomnomnom/waybackurls@latest
```

## Usage
```bash
echo example.com | waybackurls | sort -u > urls.txt        # every archived URL
echo example.com | waybackurls | grep -Ei '\.(pdf|docx|xlsx)$'   # documents to pull metadata from
cat domains.txt | waybackurls | grep -E '\?' | sort -u      # URLs with parameters
```

## Output
Plain URLs, one per line, unsorted and with duplicates - pipe through `sort -u`.
No status codes and no content: these are URLs that were *archived at some point*,
not URLs that work now.

## Gotchas
- **Archived does not mean live.** Check before acting on a URL; many will 404.
- Large domains produce enormous lists. Filter early, and remember the archive's own
  rate limits apply.
- It reads only the Wayback index. For broader coverage run [gau](gau.md), which
  queries several sources.
- Nothing here touches the target - but resolving the URLs afterwards does.

## Alternatives
- [gau](gau.md) - the same idea across more archive sources
- [Wayback CDX API](wayback-cdx-api.md) - direct control, filters, and dedup by digest
