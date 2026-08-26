---
name: MerkleMap
slug: merklemap
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://merklemap.com/
categories: [certificates-tls, ct-log-search]
tags: [ct-logs, subdomains, certificates, search]
status: unverified
status_checked: 2026-08-26
---

# MerkleMap

## What question does it answer?
What certificates and hostnames exist for this domain in the Certificate Transparency
logs - especially the ones crt.sh did not return?

## When to reach for it
As the second CT search, not the first. Different CT indexers ingest different logs
and normalise results differently, so **MerkleMap and
[crt.sh](crt-sh.md) reliably return overlapping but non-identical sets**. When
subdomain coverage matters, run both. MerkleMap is also the practical fallback when
crt.sh is timing out, which it often is.

## Install
```bash
# Nothing to install - web search, with an API for scripted use.
```

## Usage
```text
https://merklemap.com/search?query=example.com     # domain and subdomain search
# Wildcard-style queries surface names across the whole zone.
```

## Output
Matching certificates with their subject and SAN hostnames, issuer, and validity
dates. Extract the hostnames, de-duplicate, and resolve them to see which are live.

## Gotchas
- Same fundamental limits as any CT search: it shows names that were **certified**,
  not names that resolve today, and internal hosts that never got a public
  certificate are invisible.
- **The Cloudflare shared-SAN trap applies here too** - Universal SSL certificates
  group unrelated domains onto one certificate, so a shared SAN is not evidence of
  shared ownership. See [crt.sh](crt-sh.md).
- Heavier or API use is metered; check the current free allowance before scripting.

## Alternatives
- [crt.sh](crt-sh.md) - the free default, run both
- [Censys](../../02-network-and-ip/device-search/censys.md) - certificates joined to live hosts
- [subfinder](../../03-dns-and-subdomains/passive-enum/subfinder.md) - aggregates CT with other sources
