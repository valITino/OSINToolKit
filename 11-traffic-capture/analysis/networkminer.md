---
name: NetworkMiner
slug: networkminer
tier: 2
contact: passive
type: gui
cost: freemium
platforms: [windows, linux]
url: https://www.netresec.com/?page=NetworkMiner
categories: [traffic-capture, analysis]
tags: [pcap, artifacts, file-extraction, forensics]
status: unverified
status_checked: 2026-08-26
---

# NetworkMiner

## What question does it answer?
What **things** are in this capture - which hosts, what files were transferred, what
images were viewed, what credentials crossed the wire - without me reading packets?

## When to reach for it
When you want artifacts, not packets. NetworkMiner reassembles a pcap into
host-centric objects and extracts transferred files, images, and sessions
automatically. That is a fundamentally different view from
[Wireshark](../capture/wireshark-tshark.md)'s packet list, and it is much faster for
"what was taken" questions in an incident.

## Install
```bash
# Download from netresec.com. Windows native; runs on Linux/macOS under Mono.
```

## Usage
```text
1. File > Open, select the .pcap/.pcapng.
2. Hosts tab: every endpoint with OS fingerprint, hostnames, and sessions.
3. Files tab: everything reassembled out of the capture, saved to disk.
4. Images tab: a contact sheet of transferred images.
```

## Output
Tabs per artifact type: hosts (with fingerprints and open ports), files, images,
messages, sessions, DNS queries, and parameters. Extracted files are written to disk
for further analysis with
[ExifTool](../../07-documents-metadata/metadata-extraction/exiftool.md).

## Gotchas
- **Extracted files come from untrusted traffic.** Handle them in a VM and never
  execute them ([OPSEC](../../00-methodology/opsec/README.md)).
- **Encrypted traffic yields nothing** beyond metadata - no file extraction from TLS
  without the keys. Most modern traffic is encrypted, which limits this considerably;
  see [../tls-fingerprinting/README.md](../tls-fingerprinting/README.md).
- The free edition omits several features (including some protocol parsers and OSINT
  lookups) that the paid Professional edition has.
- Reassembly can mis-handle truncated or heavily fragmented captures - verify a
  critical artifact in Wireshark.

## Alternatives
- [Wireshark / tshark](../capture/wireshark-tshark.md) - packet-level ground truth
- Zeek - scriptable protocol logging at scale
