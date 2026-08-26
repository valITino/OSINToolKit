---
name: Sublist3r
slug: sublist3r
tier: 3
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/aboul3la/Sublist3r
categories: [dns-and-subdomains, passive-enum]
tags: [subdomains, legacy, search-engines]
status: stale
status_checked: 2026-08-26
superseded_by: subfinder
---

# Sublist3r

## What question does it answer?
What subdomains exist for this domain, according to search engines and a handful of
public sources?

## Why this is tier 3
The **codebase dates from around 2015** and has seen little maintenance since. Its
sources have aged badly: search engines that it depends on have changed their
interfaces and rate limiting, so runs frequently return partial results or nothing at
all. [subfinder](subfinder.md), [Amass](../../01-orchestrators/aggregators/amass.md),
and [BBOT](../../01-orchestrators/recursive-scanners/bbot.md) all query far more
sources and are actively maintained - they outperform it on any target. Community
forks exist and vary in quality.

Keep it in mind only because it is referenced constantly in older material.

## Install
```bash
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r && pip install -r requirements.txt
```

## Usage
```bash
python3 sublist3r.py -d example.com              # passive enumeration
python3 sublist3r.py -d example.com -o subs.txt   # save results
```

## Output
A list of discovered subdomains grouped by the engine that found them, and a plain
list to file.

## Gotchas
- Search-engine sources break and rate-limit; **an empty result usually means the
  sources failed, not that the domain has no subdomains.** That failure mode is the
  main reason not to rely on it.
- Its bundled brute-force option (subbrute) is intrusive - the passive mode is not.
- Python dependency friction on current interpreters is common.

## Alternatives
- [subfinder](subfinder.md) - the direct modern replacement
- [Amass](../../01-orchestrators/aggregators/amass.md) - deeper asset mapping
- [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md) - free CT-log source, no install
