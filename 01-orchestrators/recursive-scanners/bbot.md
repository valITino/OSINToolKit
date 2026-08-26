---
name: BBOT
slug: bbot
tier: 1
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/blacklanternsecurity/bbot
categories: [orchestrators, recursive-scanners]
tags: [subdomain-enum, recursive, modules, nuclei]
status: unverified
status_checked: 2026-08-26
---

# BBOT

## What question does it answer?
I have a domain (or IP, email, or org). What is the full attack surface, found
recursively, in one command I can drop into a script?

## When to reach for it
When you want [SpiderFoot](spiderfoot.md)'s breadth but faster and CLI-first.
BBOT is async and recursive: a discovered subdomain is fed back in as a new seed,
so one run chains subdomain enum, port scan, web fingerprinting, and email
harvesting. Presets (`subdomain-enum`, `email-enum`, `web-basic`) keep it to the
job at hand. In practice it typically surfaces 20-25% more subdomains than
older enumerators.

## Install
```bash
pipx install bbot
```

## Usage
```bash
bbot -t example.com -p subdomain-enum email-enum     # passive-leaning recon, two presets
bbot -t example.com -p subdomain-enum -rf passive    # restrict to passive modules
bbot -t example.com -f subdomain-enum web-screenshots # add screenshots of live hosts
```

## Output
Results stream to the terminal and to `~/.bbot/scans/<name>/` as newline-delimited
JSON plus per-type text files (subdomains, URLs, emails). The NDJSON is built for
`jq` and for feeding the next tool.

## Gotchas
- Default and aggressive presets are **active** and some (`nuclei`, `ffuf`-style
  content discovery) are **intrusive**. Read the preset before running it against
  a target you do not own; use `-rf passive` to stay off the target.
- Module coverage depends on API keys just like SpiderFoot; configure them in
  `~/.bbot/secrets.yml`.
- Recursion can balloon scope on large orgs. Set `--strict-scope` or a target
  allowlist.

## Alternatives
- [SpiderFoot](spiderfoot.md) - graph UI, gentler learning curve
- [OWASP Amass](../aggregators/amass.md) - deeper DNS/ASN asset model
- [subfinder](../../03-dns-and-subdomains/passive-enum/subfinder.md) - just passive subdomains, nothing else
