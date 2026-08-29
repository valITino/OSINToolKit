---
name: naabu
slug: naabu
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/projectdiscovery/naabu
categories: [network-and-ip, port-scanning]
tags: [port-scanning, pipeline, nmap-handoff, syn]
status: active
status_checked: 2026-08-29
---

# naabu

## What question does it answer?
I have a list of hosts from enumeration. Which ports are open, and can the result go
straight into nmap without me copying addresses around?

## When to reach for it
When port scanning is a stage in a chain rather than the whole job. naabu reads hosts on
stdin like the rest of the ProjectDiscovery tooling, so subdomain enumeration flows into
it and its output flows onward. Its distinguishing feature is `-nmap-cli`: it finds the
open ports fast, then invokes nmap **only against those ports**, which gets you real
service detection without paying nmap's cost across the full range.

Use [masscan](masscan.md) when the input is large CIDR blocks rather than hostnames.
Use [nmap](nmap.md) alone when you have a handful of hosts and want its full arsenal.

## Install
```bash
sudo apt install naabu                                          # Kali packages it
go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest # needs libpcap for SYN mode
```

## Usage
```bash
echo example.com | naabu -silent -top-ports 100
naabu -l hosts.txt -p 80,443,8080 -rate 500 -json -o ports.json
naabu -l hosts.txt -top-ports 1000 -nmap-cli 'nmap -sV -oX services.xml'
subfinder -silent -d example.com | naabu -silent -exclude-ports 80,443
```

## Output
`host:port` per line, silent by default so it pipes. `-json` gives structured records.
With `-nmap-cli` the nmap invocation you supply runs against the discovered ports and
its output lands wherever you told nmap to put it - that XML is the artifact worth
keeping.

## Gotchas
- **Port scanning is intrusive** whatever the rate. Written authorisation naming the
  hosts and window - see [../../LEGAL.md](../../LEGAL.md).
- **SYN mode needs root or `CAP_NET_RAW`** and libpcap. Without privileges it silently
  falls back to CONNECT scanning, which is slower and far more visible in the target's
  logs - check which mode you actually got.
- `-rate` defaults are polite but not zero-impact. Fragile and embedded devices fall
  over at rates a server shrugs off.
- **`-nmap-cli` runs whatever you hand it.** Build that string yourself; never
  interpolate untrusted input into it.
- Results are ports, not services. `-nmap-cli` is what turns them into evidence you can
  cite.
- Host discovery is on by default; `-Pn` semantics differ from nmap's, so read
  `-host-discovery` options before assuming a silent host is down.

## Alternatives
- [nmap](nmap.md) - the authority on what is actually listening
- [masscan](masscan.md) - faster across large ranges, no nmap hand-off
- [Shodan](../device-search/shodan.md) / [Censys](../device-search/censys.md) - existing scan data, zero contact
