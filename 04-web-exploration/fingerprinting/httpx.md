---
name: httpx
slug: httpx
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/projectdiscovery/httpx
categories: [web-exploration, fingerprinting]
tags: [probing, favicon-hash, jarm, tech-detect, bulk]
status: active
status_checked: 2026-08-29
---

# httpx

## What question does it answer?
I have a list of hosts or subdomains. Which serve HTTP, on what status code and
title, running what server - and what favicon or body hash can I pivot on?

## When to reach for it
The filter between subdomain enumeration and everything downstream: hand it a
few thousand candidate names and it says which answer at all. Its second job
matters more - it emits pivotable fingerprints in bulk (favicon mmh3, body
hash, JARM) that nothing else here produces at that scale.

## Install
```bash
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest  # Go >= 1.25
sudo apt install httpx-toolkit   # Kali/Debian: the binary is httpx-toolkit
brew install httpx               # macOS and Linux
```

## Usage
```bash
cat subs.txt | httpx -title -status-code -web-server -tech-detect -silent
httpx -l subs.txt -favicon -hash mmh3 -jarm -json -o probe.jsonl  # pivots
httpx -l subs.txt -ip -cname -asn -cdn -fr -rl 20 -o live.txt     # 20 req/s
httpx -l onions.txt -proxy socks5://127.0.0.1:9050 -nfs -title -timeout 30
```

## Output
One bracketed line per live host, fields in flag order:
`https://docs.example.com [200] [Docs] [Ruby on Rails,React,Varnish]`; `-asn`
adds `[AS13335, CLOUDFLARENET, US]`, `-favicon` the mmh3 hash. Use `-json` for
anything past eyeballing. Identical favicon mmh3, body hash or JARM across
unrelated hostnames clusters hosts built from one template or served by one box:
pivot a hash in [Shodan](../../02-network-and-ip/device-search/shodan.md) as
`http.favicon.hash:<value>`, or see
[Favicon hash pivoting](../../05-certificates-tls/origin-unmasking/favicon-hash.md).

## Gotchas
- **The name collides twice.** `pip install httpx` is an unrelated Python
  library; on Kali/Debian `python3-httpx` owns `/usr/bin/httpx`, so package and
  command are `httpx-toolkit` and a script calling `httpx` runs the wrong
  program. Kali also lags, at 1.9.0.
- **`-random-agent` defaults to true**, so pin a User-Agent with `-H` or you
  cannot afterwards state exactly what you sent in a report.
- **Redirects are not followed without `-fr`**: a host that 301s reads as
  `[301]` with the stub's title and you write it off. httpx also tries https
  then http and shows only the winner; `-nf` displays both.
- **150 req/s over 50 threads by default** is a scan, not a probe: lower it with
  `-rl` and `-t`. `-path`, `-x all`, `-probe-all-ips` and `-ss` multiply
  requests per host and make the run intrusive; see
  [../../LEGAL.md](../../LEGAL.md). A host answering is not a host in scope -
  subdomain lists hold third-party SaaS CNAMEd to vendors you cannot touch.
- `-tech-detect` is Wappalyzer-dataset matching: behind a CDN you fingerprint
  the edge and versions are trivially faked - check [WAFW00F](wafw00f.md). An
  interstitial yields its own title; `-fpt login,captcha,parked` drops those.
- No `-socks-proxy` flag any more, only `-proxy`. Against `.onion` targets
  `-ip`, `-cname`, `-asn` and `-cdn` come back empty; that is not "no CDN".
- It update-checks at start-up unless you pass `-duc`, and `-auth`, `-pd` and
  `-tid` push results to ProjectDiscovery Cloud; nothing else is uploaded.

## Alternatives
- [WhatWeb](whatweb.md) - deeper detection and match evidence on one target
- [WAFW00F](wafw00f.md) - names the product in front, where `-cdn` sees ranges
- [BuiltWith](builtwith.md) - passive, with technology history and tracking IDs
- [gowitness](../monitoring-visual/gowitness.md) - screenshot what httpx kept
