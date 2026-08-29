---
name: docker-onion-nmap
slug: onion-nmap
tier: 3
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/milesrichardson/docker-onion-nmap
categories: [darkweb, active-crawling]
tags: [tor, onion, port-scanning, proxychains, docker, legacy]
status: stale
status_checked: 2026-08-29
---

# docker-onion-nmap

## What question does it answer?
I have a .onion address and the web page is only part of it. What else answers
on that service - SSH, SMTP, an admin panel on a high port - and which of the
ports its operator published actually respond?

## Why this is tier 3
Three commits, all October 2017, no releases, and a Docker Hub image pushed
2017-10-23 and never rebuilt: nmap 7.60 and a Tor older than stable v3 client
support (0.3.2.9, January 2018), so the published `latest` very likely cannot
reach any onion that exists now - inference from the build date, untested here,
so check before relying on it. It is also only a wrapper; `bin/nmap` is three
lines. Get the same result on current software by running tor locally and
calling nmap yourself: `proxychains4 nmap -sT -Pn -n -p <ports> <addr>.onion`,
or nmap's own `--proxies socks4://127.0.0.1:9050`.

## When to reach for it
When you want the packaging - a container that boots Tor, waits for bootstrap
and proxies nmap - and you are willing to rebuild it. For anything about the web
layer use [TorBot](torbot.md); for what the service leaks about its operator,
[OnionScan](onionscan.md) and the rewrite it names. Port state on a hidden
service answers a narrow question, so do not reach here first.

## Install
```bash
docker run --rm -it milesrichardson/onion-nmap -p 80,443 <addr>.onion
# pulls the 2017 image; to get a current tor and nmap, rebuild it instead:
git clone https://github.com/milesrichardson/docker-onion-nmap
cd docker-onion-nmap && docker build -t onion-nmap .   # alpine:edge, unpinned
```

## Usage
```bash
# `onion-nmap` is your rebuild; upstream's image is milesrichardson/onion-nmap
docker run --rm -it onion-nmap -p 80,443 <addr>.onion   # named ports only
docker run --rm -it onion-nmap nc -z 80 <addr>.onion    # one-port reachability
docker run --rm -it onion-nmap curl -I http://<addr>.onion   # headers over Tor
docker run -e DEBUG_LEVEL=1 --rm -it onion-nmap -p 22,80,443 <addr>.onion
# DEBUG_LEVEL is the only environment variable; it shows tor_wait's retries
```

## Output
Bootstrap lines (`[tor_wait] Done. Tor booted.`), the proxychains chain, then an
ordinary nmap report: PORT / STATE / SERVICE, a host-is-up line with a latency
figure, and a scan summary. Read the port table and nothing else. An open port
that is not 80 or 443 is the finding - an exposed SSH, SMTP or admin service is
the kind of thing that later correlates with a clearweb host.

## Gotchas
- **`(224.0.0.1)` is not the service's address.** It is a proxychains
  placeholder from `remote_dns_subnet 224`. Recording it as the onion's IP is
  the classic false conclusion here; nothing in this tool unmasks anything.
- **"Closed" means "not published in the descriptor".** A hidden service answers
  only on the ports its operator mapped, so you cannot infer the host's firewall
  posture, OS or real network position from this scan.
- `bin/nmap` hard-codes `-sT -PN -n`: TCP connect only, no SYN scan, no OS
  detection, no UDP over Tor. Cheat-sheet flags needing raw packets do nothing.
- Roughly 2.7 s per port through a circuit, so a full-range sweep is hours long
  and closer to abuse than research. Scan a named handful.
- **Every README example uses a v2 address retired in 2021**, so copy-pasting
  upstream fails in a way that looks like a tool bug. Its dnsmasq and DNSPort
  explanation is a red herring too: .onion names resolve at the SOCKS proxy.
- **Intrusive contact.** The service's Tor daemon logs the rendezvous and the
  applications log your connections; a sweep is unmistakable. Scanning a service
  you do not own is unlawful in many jurisdictions whatever your anonymity, and
  what comes back can include illegal material - an offence to possess whatever
  your intent, and one that brings reporting duties -
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [OnionScan](onionscan.md) - operator-error fingerprinting, plus its rewrite
- [TorBot](torbot.md) - the web layer: links, titles, contact strings
- [nmap](../../02-network-and-ip/port-scanning/nmap.md) - the same scan with a
  current binary, via `--proxies socks4://127.0.0.1:9050`
