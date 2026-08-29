---
name: Robtex
slug: robtex
tier: 2
contact: passive
type: api
cost: freemium
platforms: [web, linux, macos, windows]
url: https://www.robtex.com/
categories: [dns-and-subdomains, reverse-dns]
tags: [passive-dns, reverse-ip, asn, history]
status: active
status_checked: 2026-08-26
---

# Robtex

## What question does it answer?
I have an IP, a nameserver, or a mail server. What hostnames point at it now, what
pointed at it before, and when did that change?

## When to reach for it
When you want the reverse pivot from a database rather than from live queries. Robtex
has been indexing passive DNS for years, so it answers two things a live PTR lookup
cannot: what **used to** resolve here, and which names share this nameserver or mail
server. Tracking infrastructure that moved - a domain that migrated off a host, a
registrar swap - is where it earns its place.

Its free API needs no key and no account, which makes it the reverse-DNS source you can
script immediately.

## Install
```bash
# Nothing to install - free REST API, no key required.
```

## Usage
```bash
curl -s 'https://freeapi.robtex.com/ipquery/8.8.8.8'                   # AS, route, geo, PTR, shared hosts
curl -s 'https://freeapi.robtex.com/pdns/reverse/8.8.8.8'              # hostnames pointing here, with dates
curl -s 'https://freeapi.robtex.com/pdns/reverse-historic/8.8.8.8'     # what used to point here
curl -s 'https://freeapi.robtex.com/pdns/reverse/ns1.example.com?type=ns'  # pivot on a nameserver
```

## Output
`ipquery` returns one JSON object: ASN, BGP route, geolocation, `act` (forward/PTR) and
`pas` (hostnames pointing at the address). The `/pdns/` endpoints return NDJSON, one
record per line, each with `rrname`, `rrdata`, `rrtype`, `time_first`, `time_last`, and
`count` - those timestamps are the reason to come here. `?format=` also accepts csv,
xml, yaml, and markdown.

## Gotchas
- **Use `/pdns/` timestamps, never `ipquery`'s `t` field.** The `t` values in `act`/`pas`
  are the response generation time, not a last-seen date - two calls seconds apart
  return different values for identical records. A timeline built on it is garbage.
- **A malformed query returns HTTP 200 with an empty result**, indistinguishable from a
  genuine "nothing found". Check whether the arrays are populated; do not branch on
  status.
- Reverse results look capped around 200 records - treat a full-looking list as a
  sample, not an inventory.
- On anycast or resolver addresses the "pointing here" list is dominated by parked
  junk and malware domains. Co-resolution is not a relationship.
- Private and bogon addresses return leaked internal DNS. Real, but analytically
  meaningless - filter them out of automated pivots.
- The web UI requires JavaScript and is ad-supported and analytics-instrumented; your
  queries are logged by a third party. The documented free limit is low, so back off on
  429 even if a burst succeeds.

## Alternatives
- [HackerTarget reverse DNS](hackertarget-reversedns.md) - simpler, plain text, one curl
- [hakrevdns](hakrevdns.md) - live PTR queries when you need now rather than history
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - passive DNS history with a reputation view
