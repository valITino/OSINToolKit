---
name: ZoomEye
slug: zoomeye
tier: 2
contact: passive
type: api
cost: freemium
platforms: [web, linux, macos, windows]
url: https://www.zoomeye.ai/
categories: [network-and-ip, device-search]
tags: [device-search, banners, apac-coverage, cli]
status: active
status_checked: 2026-08-26
---

# ZoomEye

## What question does it answer?
Shodan and Censys found nothing on this host. Does a scanner with different coverage
see it?

## When to reach for it
As the third opinion. Internet-wide scanners do not see the same internet: each runs its
own crawlers from its own vantage points on its own schedule, so a host absent from one
index is routinely present in another. ZoomEye is operated out of China and its coverage
of Chinese and wider APAC address space is materially better than the US-based
alternatives, which makes it the one to check when an investigation touches that
infrastructure.

Treat it as a coverage check rather than a replacement. Run it when a negative result
from Shodan or Censys matters to your conclusion.

## Install
```bash
pip3 install zoomeye                 # official CLI and SDK from Knownsec
zoomeye init -apikey "YOUR-API-KEY"  # API key auth only
```

## Usage
```bash
zoomeye search "telnet"                                  # basic dork search
zoomeye search "telnet" -facets product,port             # aggregate the whole result set
zoomeye search "telnet" -pagesize 50 -save               # export results locally
zoomeye info                                             # remaining quota on your account
```

## Output
Host records with banners, service and product identification, port, location and ASN.
The `-facets` option is the distinctive one: it returns aggregate counts across the full
result set - by product, service, device, os, port, country, city - so you can see the
shape of a population without paging through it.

## Gotchas
- **Use `zoomeye.ai`, not `zoomeye.org`.** The `.org` domain is degraded - it returned a
  Cloudflare origin error and its API host refuses connections, while `zoomeye.ai` and
  `api.zoomeye.ai` answer normally. Older guides all point at the wrong one.
- **An API key is mandatory**, including for the CLI, and the free tier's query allowance
  is small. Check `zoomeye info` before planning a large sweep.
- **Your queries go to a third party**, and in this case one subject to Chinese
  jurisdiction. Searching a target's infrastructure tells that operator what you are
  looking at. Weigh that against your case - see
  [../../00-methodology/opsec/README.md](../../00-methodology/opsec/README.md).
- Banners are collected on a crawl schedule, so a record may be weeks old. A service
  listed here may be long gone, and a missing one may simply not have been scanned.
- **This is a database lookup, not a scan** - passive, and the target sees nothing from
  you. But acting on what you find is a different contact level entirely.
- Full dork syntax lives in ZoomEye's own documentation, which sits behind an account
  and a bot check; the CLI above is the reliable route in.

## Alternatives
- [Shodan](shodan.md) - the broadest index and the best tooling
- [Censys](censys.md) - certificate-centric, strongest for pivoting on TLS
- [nmap](../port-scanning/nmap.md) - when you are authorised to look for yourself
