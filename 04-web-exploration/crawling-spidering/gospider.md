---
name: GoSpider
slug: gospider
tier: 3
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/jaeles-project/gospider
categories: [web-exploration, crawling-spidering]
tags: [crawler, urls, wayback, legacy]
status: stale
status_checked: 2026-08-29
---

# GoSpider

## What question does it answer?
I have a domain. What does the site link to, and what did Wayback, Common Crawl
and AlienVault OTX already know about it - with every finding labelled by how it
was found, in one stream I can grep?

## Why this is tier 3
It installs and runs, but upstream is frozen: last commit 22 March 2024, last
release v1.1.6 in June 2021, and two of its four passive sources are dead in the
code as shipped. [katana](katana.md) does the live crawl better, with headless
rendering and current maintenance, while
[gau](../../06-history-and-archives/web-archive/gau.md) and waybackurls cover the
archive half with data that did not stop in 2019.

## When to reach for it
When you want one pass that separates forms, JavaScript-derived paths, subdomains
and S3 bucket names from ordinary links. Not for a JavaScript-heavy site - no
headless mode, so use katana - nor for judging archive coverage, where gau is
correct. For a flat URL list to pipe onward, [hakrawler](hakrawler.md) is lighter.

## Install
```bash
GO111MODULE=on go install github.com/jaeles-project/gospider@latest
# Built clean under go1.24.7 on 2026-08-29, despite go.mod declaring go 1.16.
```

## Usage
```bash
gospider -q -s "https://example.com/"                  # bare URLs, no [tag] prefix
gospider -s "https://example.com/" -o out -c 10 -d 1   # concurrency, depth (0 = all)
gospider -s "https://example.com/" -o out --other-source --include-subs  # + archives
```

## Output
One line per discovery on stdout, appended identically to `<out>/<hostname with
dots as underscores>` and prefixed by how it was found: `[url] - [code-NNN]`,
`[href]`, `[form]`, `[upload-form]`, `[javascript]`, `[linkfinder]`,
`[subdomains]`, `[aws-s3]`, `[sitemap]`, `[other-sources]`. Split on the tag:
`grep '^\[url\] - \[code-2'` is the live-page inventory, the form tags are the
interaction surface, `[subdomains]` and `[aws-s3]` are pivots. `--json` gives one
JSON object per line, the form to diff between runs.

## Gotchas
- **The passive sources have decayed.** Common Crawl is queried against a hardcoded
  December 2019 index and VirusTotal calls the retired v2 API, so only Wayback CDX
  and AlienVault OTX still work as shipped.
- **`--other-source` can hang for ever and fail silently** - no client timeout,
  errors swallowed, nothing printed in 200 seconds against example.com. An empty
  result is indistinguishable from "nothing exists"; never report absence from it.
- **`--robots` is on by default and crawls what robots.txt forbids** - it matches
  Disallow as well as Allow lines, then visits them; a real terms-of-service and
  authorisation exposure, so pass `--robots=false`. `--sitemap` likewise
  brute-forces twelve fixed paths and visits all it finds inside.
- Defaults are shallow (`-d 1`, `-c 5`), so an empty result is usually depth. The
  README's own `-c 10 -t 20` mirrors many hosts in parallel - intrusive rather
  than active, and needing authorisation, see [../../LEGAL.md](../../LEGAL.md).
- **`-o` appends rather than overwrites**: a re-run concatenates onto the first
  file, so a naive diff compares run 1 against run 1+2.
- `[href]` lines are raw attribute values (`data:`, `mailto:`, off-host links) and
  `[linkfinder]` paths are strings from JavaScript that were often never requested
  - verify both. TLS verification is off, so bad certificates also pass unremarked.

## Alternatives
- [katana](katana.md) - maintained, headless, the live crawl done properly
- [hakrawler](hakrawler.md) - lighter when all you want is a flat URL list
- [Photon](photon.md) - when the crawl is for extracting OSINT artifacts
- [gau](../../06-history-and-archives/web-archive/gau.md) - the archive half, current
