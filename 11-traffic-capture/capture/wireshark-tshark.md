---
name: Wireshark / tshark
slug: wireshark-tshark
tier: 1
contact: passive
type: gui
cost: free
platforms: [linux, macos, windows]
url: https://www.wireshark.org/
categories: [traffic-capture, capture]
tags: [pcap, capture, tshark, analysis]
status: unverified
status_checked: 2026-08-26
---

# Wireshark / tshark

## What question does it answer?
I have a .pcap (or a live interface). What is actually on the wire - which hosts
talk to which, over what protocols, carrying what - and can I pull one field out
of thousands of packets?

## When to reach for it
The reference tool for packet capture and analysis. Use the Wireshark GUI to
explore an unfamiliar capture interactively (follow a stream, apply a display
filter, read the protocol tree). Switch to `tshark` on the command line when you
need to extract fields in bulk and pipe them to `sort`/`uniq`/`awk` - that beats
clicking through the GUI for repetitive work.

## Install
```bash
sudo apt install wireshark tshark      # Kali/Debian; add your user to the wireshark group
brew install --cask wireshark          # macOS
```

## Usage
```bash
tshark -r capture.pcapng -T fields -e dns.qry.name | sort | uniq -c | sort -rn   # top DNS queries
tshark -r capture.pcapng -Y 'http.request' -T fields -e http.host -e http.request.uri  # HTTP requests
tshark -r capture.pcapng -q -z conv,ip                                            # who talked to whom
```

## Output
The GUI gives a packet list, a decoded protocol tree, and stream-follow views.
tshark with `-T fields -e <field>` gives one value per line for scripting;
`-z` statistics give conversation and protocol summaries.

## Gotchas
- Capturing traffic that is not yours may be unlawful; capture is passive here,
  but only capture what you are authorised to.
- Display filters (`-Y`, Wireshark) differ from capture filters (`-f`, BPF). Use
  capture filters to limit what you record, display filters to explore what you
  already have.
- For TLS-encrypted payloads you need the session keys (`SSLKEYLOGFILE`); see
  [../tls-fingerprinting/README.md](../tls-fingerprinting/README.md).

## Alternatives
- [NetworkMiner](../analysis/networkminer.md) - auto-extracts files/artifacts from a pcap
- [tcpdump] - lighter capture on headless boxes (pairs with tshark for analysis)
