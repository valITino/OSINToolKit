---
name: inurlbr
slug: inurlbr
tier: 3
contact: passive
type: cli
cost: free
platforms: [linux]
url: https://github.com/googleinurl/SCANNER-INURLBR
categories: [web-exploration, dorking]
tags: [dorking, automation, legacy, php]
status: unverified
status_checked: 2026-08-26
---

# inurlbr

## What question does it answer?
Can I run a dork across many search engines at once and automatically process the
results?

## Why this is tier 3
Automated dorking sounds useful, and inurlbr's multi-engine approach was its selling
point. It is tier 3 because the approach has aged badly: search engines actively block
automated querying, so results are unreliable, and the project (a PHP scanner) has
seen little maintenance. It also bundles exploit-oriented validation features that sit
**outside this repo's discovery-and-attribution scope**.

Manual dorking, varied across engines, is more reliable and does not breach the search
engines' terms in the same way. See [README.md](README.md) for the operators that
matter.

## Install
```bash
git clone https://github.com/googleinurl/SCANNER-INURLBR.git
# Requires PHP. Verify it runs before planning around it.
```

## Usage
```bash
# Intended: run a dork across engines and collect matching URLs.
# Prefer manual dorking - see README.md in this directory.
```

## Output
A list of URLs matching the dork, with optional post-processing of each result.

## Gotchas
- **Search engines block automated queries.** Expect CAPTCHAs, partial results, and
  silent failure - the main reason this is unreliable.
- Automating search queries breaches most engines' terms of service.
- Its result-validation features shade into exploitation testing, which is out of
  scope here; use it for retrieval only, if at all.
- Unmaintained PHP tooling brings its own dependency friction.

## Alternatives
- [Dorking by hand](README.md) - reliable and in-scope
- [GHDB](https://www.exploit-db.com/google-hacking-database) - curated dork patterns to adapt
- [theHarvester](../../01-orchestrators/aggregators/theharvester.md) - multi-source collection that is maintained
