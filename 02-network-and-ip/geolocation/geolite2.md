---
name: MaxMind GeoLite2
slug: geolite2
tier: 2
contact: passive
type: library
cost: freemium
platforms: [linux, macos, windows]
url: https://dev.maxmind.com/geoip/geolite2-free-geolocation-data
categories: [network-and-ip, geolocation]
tags: [geolocation, mmdb, asn, accuracy-radius]
status: active
status_checked: 2026-08-26
---

# MaxMind GeoLite2

## What question does it answer?
Where does this IP geolocate - and **how far wrong is that answer likely to be**?

## When to reach for it
GeoLite2 is the dataset most other geolocation services are built on or benchmarked
against, so going to the source removes a layer of guessing. It runs entirely offline
from a downloaded `.mmdb` file, which means bulk lookups over a log with no rate limit
and no provider recording which addresses you asked about.

The reason to prefer it for casework is the **`accuracy_radius`** field. MaxMind
publishes, per record, the radius in kilometres within which the true location probably
falls. An IP resolvable only to a country returns coordinates near that country's centre
with a very large radius - which is precisely the artifact behind every "why does this
IP map to a farmhouse in Kansas" story. Report the radius alongside the coordinates and
the estimate stops being misleading.

## Install
```bash
sudo apt install geoipupdate mmdb-bin     # updater, plus the mmdblookup CLI
pip install geoip2                        # MaxMind's own Python reader
# Free account and licence key required: https://www.maxmind.com/en/geolite2/signup
# Put AccountID and LicenseKey in /etc/GeoIP.conf, then run: sudo geoipupdate
```

## Usage
```bash
mmdblookup --file GeoLite2-City.mmdb --ip 8.8.8.8                        # whole record
mmdblookup --file GeoLite2-City.mmdb --ip 8.8.8.8 location accuracy_radius  # trust this
mmdblookup --file GeoLite2-City.mmdb --ip 8.8.8.8 country iso_code
mmdblookup --file GeoLite2-ASN.mmdb  --ip 8.8.8.8                        # ASN and org
```

## Output
A nested record: country, subdivisions, city, postal code, `location` (latitude,
longitude, `accuracy_radius`, time zone), and registered country. `mmdblookup` prints a
typed, brace-delimited format that is **not JSON** - use `mmdbinspect` if you need JSON.
The separate ASN database gives the autonomous system number and organisation.

## Gotchas
- **Coordinates without the accuracy radius are misleading.** A large radius means the
  point is a centroid, not a place. Never present a GeoLite2 latitude and longitude as
  an address; see [../../LEGAL.md](../../LEGAL.md) on evidential claims.
- **Free access needs an account and a licence key** since 2019 - there is no anonymous
  download any more - and the licence carries attribution and redistribution terms.
- GeoLite2 is deliberately less accurate than the paid GeoIP2. The gap is largest at
  city level.
- **The data goes stale quickly.** Address space is reassigned constantly. Run
  `geoipupdate` on a schedule, and record which database build a finding came from.
- VPNs, mobile carriers, and cloud hosting defeat it entirely. GeoLite2 does not flag
  proxies - that is a separate MaxMind product.
- The registered country and the geolocated country often differ; both are in the
  record, and confusing them produces confident nonsense.

## Alternatives
- [IP2Location](ip2location.md) - comparable offline database, plus a proxy flag
- [iplocation.net](iplocation-net.md) - several providers at once, to see them disagree
- [ipinfo.io](../registries-asn/ipinfo-io.md) - one hosted answer, nothing to maintain
