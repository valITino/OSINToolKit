---
name: fierce
slug: fierce
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/mschwager/fierce
categories: [dns-and-subdomains, active-enum]
tags: [dns, brute-force, netblock, discovery]
status: unverified
status_checked: 2026-08-26
---

# fierce

## What question does it answer?
I have a domain and I am authorised to probe it. Which hostnames actually resolve,
and what non-contiguous IP space does this organisation occupy?

## When to reach for it
When passive enumeration has run out and you need resolution plus discovery of the
address space around the hits. fierce's distinguishing feature is that it looks at
the neighbourhood: after finding a host, it can sweep nearby addresses and reverse
-resolve them, which surfaces the scattered netblocks an organisation uses rather
than just the names you guessed.

Always run [subfinder](../passive-enum/subfinder.md) and
[crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md) first - passive results
are free and give you real names instead of dictionary guesses.

## Install
```bash
pipx install fierce          # Kali packages it as well
```

## Usage
```bash
fierce --domain example.com                          # default wordlist, resolve and sweep
fierce --domain example.com --subdomain-file names.txt
fierce --domain example.com --dns-servers 9.9.9.9    # choose the resolver
```

## Output
Resolved hostnames with their addresses, the nameservers consulted, and the nearby
IP ranges it identified, with any reverse-DNS names found in them.

## Gotchas
- **Brute forcing DNS is intrusive** and generates a lot of queries against the
  target's nameservers. Written authorisation - see [../../LEGAL.md](../../LEGAL.md).
- Wildcard DNS makes every guess "resolve" and will fill your output with noise -
  check for a wildcard before trusting a large result set.
- Reverse-DNS names in adjacent space belong to whoever holds that space, which may
  be a shared hosting provider rather than your target.

## Alternatives
- [subfinder](../passive-enum/subfinder.md) - passive, no authorisation needed
- [Amass](../../01-orchestrators/aggregators/amass.md) - passive and active in one asset model
