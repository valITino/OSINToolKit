---
name: crt.sh
slug: crt-sh
tier: 1
contact: passive
type: web
cost: free
platforms: [web]
url: https://crt.sh/
categories: [certificates-tls, ct-log-search]
tags: [ct-logs, subdomains, certificates, san]
status: unverified
status_checked: 2026-08-26
---

# crt.sh

## What question does it answer?
I have a domain. What subdomains and hostnames has it ever requested certificates
for - including ones that no longer resolve - without me touching the target?

## When to reach for it
Often the single best passive subdomain source. Every publicly trusted
certificate is logged to Certificate Transparency, and crt.sh indexes those logs,
so a query returns names the organisation certified even if they were never linked
or are long dead. No brute forcing, no contact with the target. Pair it with
active resolution afterward to see which names still live.

## Install
```bash
# Nothing to install - it is a website with a JSON endpoint.
curl -s 'https://crt.sh/?q=%25.example.com&output=json' | jq -r '.[].name_value' | sort -u
```

## Usage
```bash
# Web: https://crt.sh/?q=%.example.com   (%25 = URL-encoded %)
curl -s 'https://crt.sh/?q=%25.example.com&output=json' > certs.json
jq -r '.[].name_value' certs.json | tr ',' '\n' | sed 's/\*\.//' | sort -u   # unique names
```

## Output
Rows of logged certificates: issuer, validity dates, and the certificate's SANs
(the hostnames). The `name_value` field is where subdomains live; split it on
newlines/commas and de-duplicate.

## Gotchas
- **It frequently times out. Expect to refresh repeatedly** - the Postgres backend
  is often overloaded. For bulk work, retry with backoff or query the CT logs
  another way ([MerkleMap](merklemap.md), [Censys](../../02-network-and-ip/device-search/censys.md)).
- **Cloudflare Universal SSL groups unrelated domains under shared SANs.** A shared
  SAN is **not** evidence of shared ownership - do not infer a relationship from it.
- Wildcard entries (`*.example.com`) hide the specific names; combine with active
  enumeration to expand them.

## Alternatives
- [MerkleMap](merklemap.md) - different CT index, catches names crt.sh misses
- [Censys](../../02-network-and-ip/device-search/censys.md) - correlate certs with live hosts
- [subfinder](../../03-dns-and-subdomains/passive-enum/subfinder.md) - aggregates crt.sh with other passive sources
