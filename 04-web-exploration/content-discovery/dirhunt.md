---
name: dirhunt
slug: dirhunt
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/Nekmo/dirhunt
categories: [web-exploration, content-discovery]
tags: [directory-analysis, passive-leaning, crawling]
status: unverified
status_checked: 2026-08-26
---

# dirhunt

## What question does it answer?
What directory structure does this site have, worked out **without** brute forcing
thousands of paths at it?

## When to reach for it
When brute forcing is off the table - no authorisation, a fragile target, or an
investigation where you must stay quiet. dirhunt is a directory *analyser*: it
crawls what is linked, reads directory index pages, and queries third-party sources
such as search engines and VirusTotal for known paths, rather than guessing. That
makes it far quieter than [gobuster](gobuster.md) or [feroxbuster](feroxbuster.md),
and it often finds real paths those tools would never guess.

## Install
```bash
pipx install dirhunt
```

## Usage
```bash
dirhunt https://example.com                          # analyse the site's structure
dirhunt https://example.com --exclude-flags 404,403   # hide the uninteresting responses
dirhunt https://example.com --threads 4                # keep it gentle
```

## Output
Discovered directories grouped and flagged by what they look like - index-of
listings, generic pages, redirects - with the source that revealed each. The
"index of" flags are where forgotten files usually are.

## Gotchas
- Marked `active` rather than intrusive because it crawls and queries rather than
  brute forces, but it does still request pages from the target. It is quiet, not
  invisible.
- Third-party sources mean coverage depends on what those services already know - a
  site nobody has indexed yields little.
- Maintenance cadence has been uneven; verify it still runs before relying on it.
  Status is `unverified` deliberately.

## Alternatives
- [Wayback CDX](../../06-history-and-archives/web-archive/wayback-cdx-api.md) - historical paths, fully passive
- [katana](../crawling-spidering/katana.md) / [Photon](../crawling-spidering/photon.md) - crawl what is linked
- [feroxbuster](feroxbuster.md) - when you are authorised to brute force
