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
I have a list of hosts or subdomains. Which of them actually serve HTTP, on
what status code and title, running what server and technology - and what
favicon or body hash can I pivot on to find the rest of the estate?

## When to reach for it
The filter between subdomain enumeration and everything downstream: give it a
few thousand candidate names and it says which answer at all. Its second job is
the one worth learning - it emits pivotable fingerprints in bulk (favicon mmh3,
body hash, JARM) that nothing else here produces at that scale.

Not the tool for depth on one target. [WhatWeb](whatweb.md) has a larger plugin
set and shows the evidence behind each match, [BuiltWith](builtwith.md) adds
history httpx cannot see, and [urlscan.io](urlscan-io.md) answers what a page
actually *does* when a browser loads it.

## Install
```bash
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest  # needs Go >= 1.25
sudo apt install httpx-toolkit   # Kali/Debian: package and binary are httpx-toolkit
brew install httpx               # macOS and Linux
# Never `pip install httpx` - that is an unrelated Python HTTP client library.
```

## Usage
```bash
cat subs.txt | httpx -title -status-code -web-server -tech-detect -silent  # core pass
httpx -l subs.txt -favicon -hash mmh3 -jarm -json -o probe.jsonl   # pivotable hashes
httpx -l subs.txt -ip -cname -asn -cdn -fr -rl 20 -o live.txt      # polite 20 req/s
httpx -l onions.txt -proxy socks5://127.0.0.1:9050 -nfs -title -timeout 30  # via Tor
```

## Output
One bracketed line per live host, fields in flag order:
`https://docs.example.com [200] [Docs] [Ruby on Rails,React,Varnish]`. Redirect
chains show as a comma list of codes, `-favicon` prints the mmh3 hash, `-asn`
prints `[AS13335, CLOUDFLARENET, US]`. Use `-json` for anything past eyeballing.

Read it twice: as a filter keeping only hosts that answered, then as a
clustering key - identical favicon mmh3, body hash or JARM values across
unrelated hostnames group hosts built from one template or served by one box.
Feed a favicon hash to [Shodan](../../02-network-and-ip/device-search/shodan.md)
as `http.favicon.hash:<value>`; see
[favicon-hash.md](../../05-certificates-tls/origin-unmasking/favicon-hash.md).

## Gotchas
- **The name collides twice.** `pip install httpx` gets an unrelated Python
  library, and on Kali/Debian both package and command are `httpx-toolkit`
  because `python3-httpx` owns `/usr/bin/httpx` - a script written against
  `httpx` silently runs the wrong program. Kali also lags, at 1.9.0.
- **`-random-agent` defaults to true.** Every request carries a different
  User-Agent unless you pin one with `-H`, so you cannot afterwards state
  exactly what you sent - a problem if the probe must stand up in a report.
- **Redirects are not followed without `-fr`**, so a host that 301s reads as
  `[301]` with the stub's title and you write it off as empty. httpx also tries
  https then http, showing only the winner; `-nf` displays both.
- **150 req/s over 50 threads by default** is a scan, not a probe: lower it with
  `-rl` and `-t`. `-path`, `-x all`, `-probe-all-ips` and `-ss` multiply
  requests per host and make the run intrusive; see
  [../../LEGAL.md](../../LEGAL.md).
- `-tech-detect` is Wappalyzer-dataset matching: it reports what the response
  advertises, so behind a CDN you fingerprint the edge and versions are
  trivially faked - check [WAFW00F](wafw00f.md). `-title` on an interstitial
  gives the interstitial's title; `-fpt login,captcha,parked` drops those.
- There is no `-socks-proxy` flag any more, only the unified `-proxy`. Against
  `.onion` targets `-ip`, `-cname`, `-asn` and `-cdn` come back empty; that is
  not evidence of "no CDN".
- Nothing is uploaded by default, but it update-checks on start-up unless you
  pass `-duc`, and `-auth`, `-pd` and `-tid` push results to ProjectDiscovery
  Cloud. Know which are on before probing.
- A host answering is not a host in scope: subdomain lists routinely hold
  third-party SaaS names CNAMEd to a vendor you have no authorisation to touch.

## Alternatives
- [WhatWeb](whatweb.md) - deeper detection and match evidence on one target
- [WAFW00F](wafw00f.md) - names the product in front, where `-cdn` sees ranges
- [BuiltWith](builtwith.md) - passive, with technology history and tracking IDs
- [gowitness](../monitoring-visual/gowitness.md) - screenshot what httpx kept
