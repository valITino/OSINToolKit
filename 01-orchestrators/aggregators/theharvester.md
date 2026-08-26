---
name: theHarvester
slug: theharvester
tier: 1
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/laramies/theHarvester
categories: [orchestrators, aggregators]
tags: [email, subdomain, hosts, employees]
status: unverified
status_checked: 2026-08-26
---

# theHarvester

## What question does it answer?
I have a company or domain. What emails, subdomains, hostnames, and employee
names are already exposed across search engines and public data sources?

## When to reach for it
The fast first sweep. One command pulls from dozens of sources (search engines,
certificate data, PGP servers, and more) and prints a consolidated list. Reach
for it before the heavier orchestrators when you just want the low-hanging
exposure. When you need persistence or correlation, graduate to
[recon-ng](../modular-frameworks/recon-ng.md) or
[SpiderFoot](../recursive-scanners/spiderfoot.md).

## Install
```bash
pipx install theHarvester    # Kali default
```

## Usage
```bash
theHarvester -d example.com -b all              # all sources
theHarvester -d example.com -l 500 -b bing      # cap results, single source
theHarvester -d example.com -b crtsh -f out     # CT-log subdomains, save HTML/XML/JSON
```

## Output
Grouped lists: emails, hosts/subdomains, IPs, and (from some sources) employee
names and URLs. `-f` writes an HTML report plus machine-readable XML/JSON.

## Gotchas
- `-d` (domain), `-l` (limit), and `-b` (sources) are the three you always set;
  `-b all` is the usual starting point.
- Several sources need API keys in `~/.theHarvester/api-keys.yaml` to return
  anything useful; without them those sources quietly contribute nothing.
- Search-engine sources rate-limit and occasionally return partial or empty sets;
  re-run or narrow `-b` if a source looks dead.

## Alternatives
- [recon-ng](../modular-frameworks/recon-ng.md) - persistent, database-backed casework
- [SpiderFoot](../recursive-scanners/spiderfoot.md) / [BBOT](../recursive-scanners/bbot.md) - broader recursive coverage
- [subfinder](../../03-dns-and-subdomains/passive-enum/subfinder.md) - subdomains only, deeper
