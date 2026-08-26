---
name: gowitness
slug: gowitness
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/sensepost/gowitness
categories: [web-exploration, monitoring-visual]
tags: [screenshots, triage, bulk, reporting]
status: unverified
status_checked: 2026-08-26
---

# gowitness

## What question does it answer?
I have hundreds of hosts or URLs. What does each one actually look like, so I can
spot the interesting ones without opening hundreds of tabs?

## When to reach for it
Immediately after enumeration. Turning a list of subdomains into a wall of
screenshots is the fastest triage step in web investigation - default installs,
forgotten admin panels, and parked domains are obvious at a glance and invisible in a
text list. It is the automated form of "document everything", and the screenshots
double as evidence.

## Install
```bash
go install github.com/sensepost/gowitness@latest    # needs a Chrome/Chromium binary present
```

## Usage
```bash
gowitness scan file -f subdomains.txt          # screenshot every host in a list
gowitness scan single -u https://example.com    # one target
gowitness report server                          # browse the results in a local web UI
```

Subcommand names have changed between major versions - run `gowitness --help` and
match the syntax to your installed version.

## Output
PNG screenshots on disk plus a database of results (status, title, technologies), and
a local report UI that shows them as a browsable grid.

## Gotchas
- **Active**: each screenshot is a full page load from your IP, including all
  third-party resources. That is real contact - consider
  [OPSEC](../../00-methodology/opsec/README.md) before pointing it at a sensitive
  target, and note that loading an attacker's page in a browser has its own risk.
- It drives a headless browser, so it is resource-hungry; cap concurrency on large
  lists.
- Screenshots for evidence need context - record the URL and timestamp alongside, per
  [documentation](../../00-methodology/documentation/README.md).

## Alternatives
- [urlscan.io](../fingerprinting/urlscan-io.md) - sandboxed, does not use your IP
- [VisualPing](visualping.md) - watch one page over time instead
