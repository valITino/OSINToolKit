---
name: subfinder
slug: subfinder
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/projectdiscovery/subfinder
categories: [dns-and-subdomains, passive-enum]
tags: [subdomains, passive, aggregation]
status: unverified
status_checked: 2026-08-26
---

# subfinder

## What question does it answer?
I have a domain. What subdomains exist, gathered from every passive source at once,
without sending a single packet to the target?

## When to reach for it
The default passive subdomain tool, and the modern replacement for
[Sublist3r](sublist3r.md). It queries dozens of sources (CT logs, passive DNS
providers, search APIs) concurrently and de-duplicates the result. Reach for it when
you want a fast, clean name list to feed into resolution, screenshots, or
[Amass](../../01-orchestrators/aggregators/amass.md) for deeper asset mapping.

## Install
```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

## Usage
```bash
subfinder -d example.com                       # passive enumeration, names to stdout
subfinder -d example.com -all -o subs.txt      # use every configured source
subfinder -dL domains.txt -silent | httpx      # pipeline: names, then which are live
```

## Output
A plain list of unique subdomain names, one per line - built to pipe. `-oJ` gives
JSON with the source that found each name, which is useful when you need to justify
a finding's provenance.

## Gotchas
- Passive only. It reports names that *were* seen, so some will not resolve any
  more - resolve separately before treating a name as live infrastructure.
- Coverage depends heavily on API keys in
  `$HOME/.config/subfinder/provider-config.yaml`; without them the best sources are
  silent. See [../../99-resources/api-keys/README.md](../../99-resources/api-keys/README.md).
- Sources overlap imperfectly - run [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md)
  and [Amass](../../01-orchestrators/aggregators/amass.md) too on an important target.

## Alternatives
- [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md) - the single richest passive source
- [Amass](../../01-orchestrators/aggregators/amass.md) - deeper asset model, slower
- [DNSDumpster](dnsdumpster.md) - browser-based, with a visual map
