---
name: ipinfo.io
slug: ipinfo-io
tier: 2
contact: passive
type: api
cost: freemium
platforms: [web]
url: https://ipinfo.io/
categories: [network-and-ip, registries-asn]
tags: [asn, org, geolocation, api]
status: unverified
status_checked: 2026-08-26
---

# ipinfo.io

## What question does it answer?
I have an IP. In one call: who owns it, what ASN it belongs to, roughly where it
is, and is it a hosting provider rather than an end user?

## When to reach for it
The quickest single lookup for enriching an IP, and the easiest to script over a
list. It consolidates what would otherwise be a `whois` plus a geo lookup plus an
ASN check. Reach for [bgp.he.net](bgp-he-net.md) when you need routing detail, and
the [RIR databases](rir-databases.md) when you need the authoritative allocation.

## Install
```bash
# Nothing to install. A free token raises the rate limit substantially.
```

## Usage
```bash
curl -s https://ipinfo.io/8.8.8.8/json                      # full record
curl -s https://ipinfo.io/8.8.8.8/org                        # just the ASN + org
curl -s "https://ipinfo.io/8.8.8.8/json?token=$IPINFO_TOKEN" # authenticated
```

## Output
JSON with the IP, hostname (reverse DNS), city/region/country, approximate
lat/long, and an `org` field combining ASN and organisation name. Paid tiers add
privacy-detection (VPN/proxy/Tor), carrier, and company data.

## Gotchas
- **City-level geolocation is an estimate.** Country is usually right; a precise
  coordinate is not evidence of where a person is. See
  [../geolocation/README.md](../geolocation/README.md).
- The free tier is rate-limited per IP; get a free token before scripting a batch.
  See [../../99-resources/api-keys/README.md](../../99-resources/api-keys/README.md).
- The `org` field is convenient but coarse - confirm against the RIR record before
  asserting ownership.

## Alternatives
- [whois](whois.md) - authoritative registration detail
- [iplocation.net](../geolocation/iplocation-net.md) - compare several geo providers at once
