---
name: masscan
slug: masscan
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/robertdavidgraham/masscan
categories: [network-and-ip, port-scanning]
tags: [port-scanning, large-scale, syn, rate-limited]
status: active
status_checked: 2026-08-29
---

# masscan

## What question does it answer?
I have a whole netblock and nmap would take days. Which addresses have this port open,
in minutes?

## When to reach for it
When the range is large and the question is narrow. masscan transmits asynchronously
with its own TCP/IP stack, so it sweeps a /16 for one port far faster than a
connect-based scanner. That speed comes from doing much less: it tells you a port
answered and nothing else.

So it is the front half of a pipeline, never the whole thing. Sweep with masscan to
find the live surface, then hand those hosts to [nmap](nmap.md) for service, version and
OS detection. Reach for [naabu](naabu.md) instead when the list is hosts rather than
ranges and you want that hand-off wired up for you.

## Install
```bash
sudo apt install masscan                 # Kali/Debian package it
# or build: sudo apt install libpcap-dev && make && ls bin/masscan
```

## Usage
```bash
sudo masscan 192.0.2.0/24 -p80,443 --rate 1000 -oJ out.json   # bounded sweep, JSON out
sudo masscan -iL targets.txt -p1-65535 --rate 500 --excludefile never-scan.txt
sudo masscan 192.0.2.0/24 -p80 --banners --rate 200           # grab banners too
```

## Output
`-oL/-oJ/-oD/-oG/-oB/-oX/-oU` write List, JSON, ndjson, Grepable, Binary, XML or
Unicornscan format. Each record is an address, a port and a state - no service name, no
version. `--banners` adds whatever the service volunteers, which is the only
identification masscan offers.

## Gotchas
- **`--rate` is the dangerous knob.** It is packets per second and it will happily
  saturate your uplink, melt a home router, or read as a denial-of-service attack.
  Start low. A number you copied from a blog post is not a safe default.
- **It is intrusive and needs written authorisation** naming the ranges and the window -
  see [../../LEGAL.md](../../LEGAL.md). Scanning ranges you were not given is an offence
  in many jurisdictions regardless of intent.
- **Use `--excludefile` as a safety rail**, not an afterthought. One typo in a CIDR is
  the difference between the target and someone else's network.
- Because it runs its own TCP stack, the host kernel knows nothing about the
  connections and answers replies with RSTs. Firewall off the source port masscan uses,
  or results degrade.
- **It does not identify services.** An open 443 is an open 443, not "HTTPS" and
  certainly not a version. Confirm with nmap before writing anything down.
- Host order is randomised by default, so a partial run gives you a scattered sample of
  the range rather than a contiguous prefix.
- Requires root or `CAP_NET_RAW`.

## Alternatives
- [nmap](nmap.md) - slower, but it tells you what is actually listening
- [naabu](naabu.md) - similar speed with an nmap hand-off built in
- [Shodan](../device-search/shodan.md) / [Censys](../device-search/censys.md) - the same question with zero contact
