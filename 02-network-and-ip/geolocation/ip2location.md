---
name: IP2Location
slug: ip2location
tier: 2
contact: passive
type: api
cost: freemium
platforms: [web, linux, macos, windows]
url: https://www.ip2location.com/
categories: [network-and-ip, geolocation]
tags: [geolocation, offline-database, proxy-detection, api]
status: active
status_checked: 2026-08-26
---

# IP2Location

## What question does it answer?
I have an IP - or ten thousand. Where does it geolocate, is it a proxy or VPN, and can
I answer that **without a third party seeing which addresses I am asking about**?

## When to reach for it
Two things make this the geolocation source worth keeping. First, the free **LITE**
databases are downloadable, so you can resolve a whole log file offline: no rate limit,
no latency, and - the part that matters in an investigation - no provider building a
list of the addresses you are interested in. Second, the companion IP2Proxy LITE
database answers "is this a VPN, proxy, or hosting IP?", which is usually the more
useful question than which city a datacentre sits in.

Use [iplocation.net](iplocation-net.md) when you want several providers' opinions side
by side. Come here when you want one answer, in bulk, under your own control.

## Install
```bash
# Nothing needed for the web lookup or the keyless API.
# LITE databases (CSV/BIN) from https://lite.ip2location.com/ - free account, attribution required.
pip install IP2Location          # official reader for the downloaded BIN files
```

## Usage
```bash
curl -s 'https://api.ip2location.io/?ip=8.8.8.8'        # no key needed, 1,000/day
curl -s 'https://api.ip2location.io/?ip=8.8.8.8&key=YOURKEY'   # free account: 50k/month
```
```text
https://www.ip2location.com/demo/8.8.8.8     # single lookup in a browser
```

## Output
JSON: `country_code`, `country_name`, `region_name`, `city_name`, `latitude`,
`longitude`, `zip_code`, `time_zone`, `asn`, `as`, and `is_proxy`. The keyless response
also carries a `message` field stating the remaining quota - check for it, because it is
how the free tier tells you it is throttling rather than failing.

## Gotchas
- **The LITE data is deliberately less accurate than the commercial database.** It is
  fine for country and ASN, weaker on city, and the paid product exists precisely
  because of that gap. Do not present a LITE city as a finding.
- **Attribution is required** by the LITE licence if you publish or redistribute
  anything derived from it.
- `is_proxy` in the free tier is a coarse flag. Detailed proxy type, and mobile-carrier
  and usage-type fields, are commercial-only.
- **Country and ASN are reasonably reliable; coordinates are not.** A latitude and
  longitude here is an estimate, frequently a country or city centroid, and never a
  street address. See the caveats in [iplocation.net](iplocation-net.md).
- The keyless endpoint is rate-limited per source IP and will start refusing quietly.
- Mobile carriers, VPNs, and cloud hosting break geolocation entirely - you are locating
  infrastructure, never a person.

## Alternatives
- [iplocation.net](iplocation-net.md) - several providers at once, to see them disagree
- [ipinfo.io](../registries-asn/ipinfo-io.md) - one clean scriptable answer
- [whois](../registries-asn/whois.md) - registered organisation, a fact rather than an estimate
