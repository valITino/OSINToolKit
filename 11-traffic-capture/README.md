# 11 - Traffic Capture

You have a .pcap, or you can capture. See who talks to whom, extract artifacts, and fingerprint the client from its TLS handshake.

## Subcategories

- [capture/](capture/) - Wireshark, tshark - capture and field extraction
- [analysis/](analysis/) - NetworkMiner - auto-extract artifacts
- [tls-fingerprinting/](tls-fingerprinting/) - JA3/JA4 - identify the client

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [Wireshark / tshark](capture/wireshark-tshark.md) | I have a .pcap (or a live interface). What is actually on the wire - which hosts talk to which, over what protocols, carrying... | 1 | passive |
| [NetworkMiner](analysis/networkminer.md) | What **things** are in this capture - which hosts, what files were transferred, what images were viewed, what credentials crossed... | 2 | passive |
<!-- END:TOOLS -->
