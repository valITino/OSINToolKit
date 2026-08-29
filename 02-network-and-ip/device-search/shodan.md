---
name: Shodan
slug: shodan
tier: 2
contact: passive
type: web
cost: freemium
platforms: [linux, macos, windows, web]
url: https://www.shodan.io/
categories: [network-and-ip, device-search]
tags: [device-search, banners, exposure, iot]
status: unverified
status_checked: 2026-08-26
---

# Shodan

## What question does it answer?
What is exposed on this host, netblock, or organisation - without me scanning it -
and where else on the internet does this same banner, certificate, or product appear?

## When to reach for it
Before [nmap](../port-scanning/nmap.md), always. Shodan continuously scans the
internet and stores banners, so you get the exposure picture with zero contact with
the target. It is also the tool for the reverse question: given a distinctive banner
or favicon hash, find every other host running the same thing - which is how you
find an adversary's other infrastructure.

## Install
```bash
pipx install shodan          # CLI; then: shodan init <API_KEY>
```

## Usage
```bash
shodan host 8.8.8.8                          # everything known about one IP
shodan search 'org:"Example Inc" port:3389'   # exposed RDP in an organisation
shodan search 'ssl.cert.subject.CN:"example.com"'  # hosts serving that certificate
```

Useful filters: `city:`, `country:`, `geo:`, `net:`, `os:`, `port:`, `org:`,
`product:`, `hostname:`, `ssl:`.

## Output
Per-host records: open ports, service banners with product and version, TLS
certificate details, location and ASN, and a timestamp for when it was last seen.
Search returns matching hosts across the whole dataset.

## Gotchas
- **Data is as of the last scan, not now.** A result may be stale by days or weeks;
  confirm before acting on it, and record the `timestamp` field.
- Most filters and the API require a paid membership. The one-time membership fee is
  the best-value paid key in this repo - see
  [../../99-resources/api-keys/README.md](../../99-resources/api-keys/README.md).
- Querying Shodan is passive, but be careful with what you *do* with a result:
  connecting to a discovered service is contact with the target.
- Banners can be spoofed or reflect a proxy rather than the origin.

## Alternatives
- [Censys](censys.md) - certificate-centric view of the same problem
- [nmap](../port-scanning/nmap.md) - authoritative but intrusive
- [nuclei](../vuln-scanners/nuclei.md) - templated checks against what you found
- [ZoomEye](zoomeye.md) - different crawler coverage; check it when Shodan finds nothing
