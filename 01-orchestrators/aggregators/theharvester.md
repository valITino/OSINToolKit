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
sudo apt install theharvester        # Kali packages it - the simplest route

# Or from source (upstream uses uv; there is no root theHarvester.py launcher):
git clone https://github.com/laramies/theHarvester.git
cd theHarvester && uv sync && uv run theHarvester -h
```
The PyPI name is not the project - install from Kali or from source.

## Usage
```bash
theHarvester -d example.com -b all                     # every source
theHarvester -d example.com -b subdomains -l 500        # a capability group, capped
theHarvester -d example.com -b crtsh,certspotter -f out # CT-log subdomains, save report
```

`-b` takes source names **or** capability groups (`subdomains`, `emails`, `ips`,
`asns`, `urls`, `people`, `breaches`, `all`). Run `theHarvester -h` for the source
list your version actually has - sources are added and removed regularly.

## Output
Grouped lists: emails, hosts/subdomains, IPs, and (from some sources) employee
names and URLs. `-f` writes an HTML report plus machine-readable XML/JSON.

## Gotchas
- `-d` (domain), `-l` (limit), and `-b` (sources) are the three you always set;
  `-b all` is the usual starting point.
- **Source names change between versions.** `bing`, for example, is no longer in
  the catalogue. An invalid name is a hard error, so check `-h` rather than
  copying a source list out of an old tutorial.
- Several sources need API keys in `~/.theHarvester/api-keys.yaml` to return
  anything useful; without them those sources quietly contribute nothing.
- Search-engine sources rate-limit and occasionally return partial or empty sets;
  re-run or narrow `-b` if a source looks dead.

## Alternatives
- [recon-ng](../modular-frameworks/recon-ng.md) - persistent, database-backed casework
- [SpiderFoot](../recursive-scanners/spiderfoot.md) / [BBOT](../recursive-scanners/bbot.md) - broader recursive coverage
- [subfinder](../../03-dns-and-subdomains/passive-enum/subfinder.md) - subdomains only, deeper
