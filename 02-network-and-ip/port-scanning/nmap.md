---
name: nmap
slug: nmap
tier: 1
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://nmap.org/
categories: [network-and-ip, port-scanning]
tags: [port-scan, service-detection, os-detection, nse]
status: unverified
status_checked: 2026-08-26
---

# nmap

## What question does it answer?
I have a host or an IP range. What ports are open, what services and versions are
behind them, and roughly what operating system is it?

## When to reach for it
The quasi-standard for port and service discovery; nothing has really replaced it.
Reach for it when you are authorised to touch the target and need ground truth
about exposed services. For passive alternatives that never touch the host, use
[Shodan](../device-search/shodan.md) or [Censys](../device-search/censys.md)
first - they answer "what is exposed" from existing scan data.

## Install
```bash
sudo apt install nmap        # Kali default; also brew install nmap / from nmap.org
```

## Usage
```bash
nmap -sV -Pn example.com                    # service/version detection, skip ping
nmap -sV -sC -p- example.com                # all ports + default NSE scripts
nmap -A -T4 10.0.0.0/24                      # aggressive: OS, version, traceroute on a range
```

## Output
A per-host list of ports with state (open/closed/filtered), the detected service
and version, and - with `-A`/`-O` - an OS guess and traceroute. `-oA base` writes
normal, greppable, and XML formats at once for later parsing.

## Gotchas
- Port scanning is **intrusive**. Unauthorised scanning is an offence in many
  jurisdictions - have written authorisation. See [../../LEGAL.md](../../LEGAL.md).
- `-Pn` when ICMP is blocked or hosts appear down; otherwise nmap may skip a live
  host. `-T4`/`-T5` are loud and can trip IDS or destabilise fragile devices.
- The brute-force and exploit NSE categories (`--script brute`, exploitation
  scripts) are **out of scope** for this repo; use nmap here for discovery only.

## Alternatives
- [Shodan](../device-search/shodan.md) / [Censys](../device-search/censys.md) - passive, no target contact
- [masscan](masscan.md) - sweeps a whole netblock for one port in minutes
- [naabu](naabu.md) - fast discovery that hands the open ports straight back to nmap
- [nuclei](../vuln-scanners/nuclei.md) - templated checks once you know what is exposed
