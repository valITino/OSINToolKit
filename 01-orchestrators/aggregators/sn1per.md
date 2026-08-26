---
name: Sn1per
slug: sn1per
tier: 3
contact: intrusive
type: cli
cost: freemium
platforms: [linux]
url: https://github.com/1N3/Sn1per
categories: [orchestrators, aggregators]
tags: [automation, scanning, out-of-scope, wrapper]
status: unverified
status_checked: 2026-08-26
---

# Sn1per

## What question does it answer?
What does a fully automated recon-and-attack-surface sweep of this target produce, by
chaining dozens of other tools together?

## Why this is tier 3
Sn1per is a wrapper that orchestrates many third-party tools into one automated run.
Two reasons it sits at tier 3 here:

1. **It crosses this repo's scope boundary.** Its workflows include exploitation
   testing, not just discovery and attribution. This repo documents discovery tools;
   exploitation is deliberately out of scope, so Sn1per cannot be recommended as a
   default.
2. **It is loud and hard to scope.** The automation makes it easy to run a far more
   intrusive scan than you intended against a target - a serious problem when the
   boundary between authorised and unauthorised is what keeps you legal.

If you want broad automated coverage, [BBOT](../recursive-scanners/bbot.md) and
[SpiderFoot](../recursive-scanners/spiderfoot.md) give you that with scoping controls
and without the exploitation layer.

## Install
```bash
# See the project repository. A paid Professional edition exists.
```

## Usage
```bash
# Modes chain many tools automatically. Read what a mode does BEFORE running it.
```

## Output
Aggregated reports from the underlying tools, organised per target.

## Gotchas
- **Intrusive, and more so than you expect.** Written authorisation, with a scope that
  explicitly covers automated scanning. See [../../LEGAL.md](../../LEGAL.md).
- Wrapping many tools means inheriting all their failure modes at once; diagnosing a
  bad result means knowing every underlying tool anyway.
- Exploitation features are **out of scope for this repo** - not documented here.
- Its maintenance and free/paid split have shifted over time; verify before use.

## Alternatives
- [BBOT](../recursive-scanners/bbot.md) - broad, scriptable, scopeable
- [SpiderFoot](../recursive-scanners/spiderfoot.md) - broad with a correlation graph
- [nuclei](../../02-network-and-ip/vuln-scanners/nuclei.md) - templated checks you can read first
