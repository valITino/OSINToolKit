---
name: tcpdump
slug: tcpdump
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://www.tcpdump.org/
categories: [traffic-capture, capture]
tags: [pcap, capture, bpf, headless]
status: active
status_checked: 2026-08-26
---

# tcpdump

## What question does it answer?
I am on a box with no GUI and I need the traffic. What is crossing this interface, and
can I get a pcap off it for someone else to analyse?

## When to reach for it
For capture, on a server, over SSH. tcpdump is on essentially every Unix host already,
which makes it the tool you actually have when you need one. Use it to **record**; use
[Wireshark / tshark](wireshark-tshark.md) to read what you recorded. Its BPF filter
syntax is the same language Wireshark uses for *capture* filters, so what you learn
here transfers.

## Install
```bash
sudo apt install tcpdump       # already present on most Unix systems; Kali ships 4.99.6
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/tcpdump   # optional: capture without root
```

## Usage
```bash
sudo tcpdump -i eth0 -n -w capture.pcap         # record to disk, no name resolution
sudo tcpdump -i eth0 -n 'port 53'               # watch DNS live; BPF capture filter
tcpdump -n -r capture.pcap 'host 192.0.2.10'    # read back - no privileges needed
sudo tcpdump -i eth0 -n -C 100 -W 10 -w ring.pcap   # 10 rotating files of 100MB
```

## Output
Without `-w`, one line per packet: timestamp, source, destination, protocol, flags,
length. With `-w`, a pcap file and nothing on screen. On exit it prints a
**"N packets dropped by kernel"** counter - check it every time, because a non-zero
value means your capture is incomplete and a "missing" connection may be an artifact.
Raise `-B` if so.

## Gotchas
- **`-nn` is not different from `-n` on modern tcpdump.** A single `-n` already
  suppresses hostname *and* port-name lookup; the two produce identical output on
  4.99.x. Tutorials still teach the distinction. Do keep `-n` though: without it
  tcpdump does reverse lookups that are slow and that leak your investigation to the
  target's DNS infrastructure.
- **`-s0` is a legacy no-op.** The default snaplen is 262144 bytes, and `-s 0` just
  sets that same default. The old warning applied to tcpdump before 4.0, when the
  default was 68 bytes. Truncated packets show as `[|proto]`.
- **On Debian and Ubuntu the output file is not owned by root.** The packaged build
  drops privileges by default, so `sudo tcpdump -w x.pcap` yields a file owned by
  `tcpdump:tcpdump`. Pass `-Z root` if you need root ownership - it bites scripts that
  cannot later read their own output, and it is a chain-of-custody wrinkle.
- **A capture filter is irreversible.** What the BPF expression on a `-w` excludes is
  gone forever. Capture broadly, filter narrowly on `-r`. And BPF is not Wireshark
  display-filter syntax: `host x and port 443`, never `ip.addr == x`.
- Live capture needs root or `CAP_NET_RAW`; reading a saved file needs nothing. Note
  `setcap` grants that to every user on the box and is lost on package upgrade.
- `-z postrotate-command` runs an arbitrary command on each rotation - a legitimate
  archiving feature and a command-execution surface. Never point it at untrusted input.
- **A capture is evidence and usually contains personal data.** Capturing traffic you
  are not authorised to capture is a criminal offence in most jurisdictions. See
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Wireshark / tshark](wireshark-tshark.md) - read and dissect what tcpdump recorded
- [Zeek](../analysis/zeek.md) - turn the capture into structured protocol logs
- [NetworkMiner](../analysis/networkminer.md) - pull files and artifacts out of the pcap
