---
name: RIR databases (ARIN / RIPE / APNIC)
slug: rir-databases
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://www.arin.net/resources/registry/whois/rws/
categories: [network-and-ip, registries-asn]
tags: [arin, ripe, apnic, netblocks, allocation]
status: unverified
status_checked: 2026-08-26
---

# RIR databases (ARIN / RIPE / APNIC)

## What question does it answer?
I have an organisation name. Which IP ranges and ASNs are allocated to it - and,
given one of its IPs, what else sits in the same allocation?

## When to reach for it
When you need to go from a company to its network footprint, or to establish the
authoritative boundaries of a netblock. The Regional Internet Registries hold the
allocation records; their web interfaces and APIs support richer queries than a
plain `whois` client, including organisation search on ARIN's Whois-RWS.

## Install
```bash
# Nothing to install - web interfaces plus REST APIs.
```

## Usage
```bash
# ARIN Whois-RWS, JSON:
curl -s -H 'Accept: application/json' 'https://whois.arin.net/rest/net/NET-8-8-8-0-1'

# RIPE database search:
curl -s 'https://rest.db.ripe.net/search.json?query-string=193.0.6.139'
```

Web: `whois.arin.net` (North America), `apps.db.ripe.net` (Europe/Middle East),
`wq.apnic.net` (Asia-Pacific); LACNIC and AFRINIC cover the rest.

## Output
Allocation records: the netblock range, the organisation it is assigned to, parent
and child allocations, and role/abuse contacts. ARIN's organisation search maps a
company name to every network registered under it.

## Gotchas
- **Query the right registry.** An IP allocated in Europe will not be authoritative
  in ARIN's database; you get a referral at best. Match the region to the RIR.
- **RIPE takes IPs and other network objects, not domain names.** Domain
  registration lives with the registrar, not the RIR.
- Allocation to an ISP does not mean the ISP operates the host - downstream
  assignment is common and often invisible.
- EU personal-data rules limit what contact detail is published.

## Alternatives
- [whois](whois.md) - the CLI front end to the same data
- [bgp.he.net](bgp-he-net.md) - what is actually announced, versus what is allocated
- [ipinfo.io](ipinfo-io.md) - quick org/ASN answer without picking a registry
