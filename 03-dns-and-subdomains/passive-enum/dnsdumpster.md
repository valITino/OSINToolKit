---
name: DNSDumpster
slug: dnsdumpster
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://dnsdumpster.com/
categories: [dns-and-subdomains, passive-enum]
tags: [subdomains, dns-map, export, visual]
status: unverified
status_checked: 2026-08-26
---

# DNSDumpster

## What question does it answer?
I have a domain and want a quick, visual picture of its DNS footprint - subdomains,
mail servers, and the hosts they map to - without installing anything.

## When to reach for it
The no-setup option, and a good sanity check against your CLI results. One query
returns subdomains, A/MX/TXT records, and the ASN/netblock each host sits in, plus a
graph of the relationships and an export. Useful early, when you are orienting, and
useful for handing a non-technical colleague a picture.

## Install
```bash
# Nothing to install - web only.
```

## Usage
```text
https://dnsdumpster.com/     # enter the domain; review the table, map, and export
```

## Output
Tables of DNS records grouped by type, each host annotated with its IP, reverse DNS,
ASN, and country; a relationship graph; and a downloadable export of the findings.

## Gotchas
- Results are capped and the free service is rate-limited - it is a first look, not
  a complete enumeration. Confirm with
  [subfinder](subfinder.md) and [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md).
- Data comes from the operator's own collection, so freshness varies; verify a
  critical name by resolving it yourself with [dig](../query-tools/dig.md).
- Free access has changed over time (accounts and API tiers have come and gone) -
  check the current terms before relying on it in a workflow.

## Alternatives
- [subfinder](subfinder.md) - scriptable and more complete
- [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md) - CT-log names, free and deep
