---
name: bgp.he.net
slug: bgp-he-net
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://bgp.he.net/
categories: [network-and-ip, registries-asn]
tags: [bgp, asn, peers, prefixes, routing]
status: unverified
status_checked: 2026-08-26
---

# bgp.he.net

## What question does it answer?
I have an ASN, IP, or organisation. What prefixes does it actually announce to the
internet, who does it peer with, and where does its traffic transit?

## When to reach for it
When allocation is not enough and you need the **routing** truth. Registry data
says what was assigned; BGP says what is announced right now. Hurricane Electric's
looking glass is the fastest free way to see an AS's prefixes, upstreams, peers,
and the DNS/IPv6 footprint attached to it. Good for scoping an organisation's real
network edge before any active work.

## Install
```bash
# Nothing to install - web only.
```

## Usage
```text
https://bgp.he.net/AS15169          # prefixes, peers, and upstreams for an ASN
https://bgp.he.net/ip/8.8.8.8        # which ASN and prefix an IP falls under
https://bgp.he.net/net/8.8.8.0/24    # the prefix view
# The site also supports searching by organisation name.
```

## Output
Per-ASN pages listing announced IPv4/IPv6 prefixes, adjacent ASNs split into peers
and upstreams/downstreams, and related DNS records. Per-prefix pages show the
origin AS and announcement history.

## Gotchas
- Announced prefixes change; this is a live view, so record what you saw and when
  ([documentation](../../00-methodology/documentation/README.md)).
- An announced prefix can be larger than the organisation's actual usage, and
  hosting providers announce space used by thousands of unrelated customers - do
  not infer ownership of a host from the ASN alone.
- Peering relationships shown are inferred from public route collectors and are
  not a complete picture of commercial arrangements.

## Alternatives
- [RIR databases](rir-databases.md) - the allocation record behind the announcement
- [ipinfo.io](ipinfo-io.md) - the same ASN answer in one API call
