---
name: ExoneraTor
slug: exonerator
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://metrics.torproject.org/exonerator.html
categories: [network-and-ip, reputation]
tags: [tor, relay, attribution, exit-node]
status: unverified
status_checked: 2026-08-26
---

# ExoneraTor

## What question does it answer?
I have an IP and a date from a log. Was that IP a Tor relay at that moment - meaning
the traffic may not have originated with whoever holds the address?

## When to reach for it
Before you attribute anything to an IP found in a log. ExoneraTor is the Tor
Project's own service and answers one narrow question authoritatively, using
archived relay consensus data. A positive result substantially weakens any
inference from the IP to a person: if it was an exit relay, the traffic was almost
certainly relayed on someone else's behalf. The name is literal - it exists to
exonerate relay operators.

## Install
```bash
# Nothing to install - web only.
```

## Usage
```text
https://metrics.torproject.org/exonerator.html
# Enter the IP address and the date (UTC) from your log, then read the verdict.
```

## Output
A statement of whether a Tor relay was running on that address on that date, and if
so, the relay's fingerprint and whether it permitted exit traffic.

## Gotchas
- **Get the date and timezone right.** Consensus data is per-date in UTC; an
  off-by-one date can flip the answer. Record the log timestamp with its timezone.
- Being a relay is not being an exit. A middle or guard relay does not emit traffic
  to the wider internet, so the implication differs.
- A negative result only rules out Tor - the IP could still be a VPN, proxy, or
  compromised host. It narrows attribution; it does not confirm it.

## Alternatives
- [AbuseIPDB](abuseipdb.md) / [VirusTotal](virustotal.md) - general reputation context
- [ipinfo.io](../registries-asn/ipinfo-io.md) - hosting/VPN detection on paid tiers
