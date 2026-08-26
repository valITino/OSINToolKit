---
name: Zeek
slug: zeek
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://zeek.org/
categories: [traffic-capture, analysis]
tags: [pcap, protocol-logs, timeline, uid]
status: active
status_checked: 2026-08-26
---

# Zeek

## What question does it answer?
I have a large capture. What **happened** in it - as searchable, joinable logs I can
grep and timeline, rather than a million packets I have to scroll?

## When to reach for it
When the pcap is too big to read. Zeek replays a capture and writes one structured log
per protocol - `conn.log`, `dns.log`, `http.log`, `ssl.log`, `files.log` - so the work
becomes `grep`, `sort` and `awk` instead of clicking.

The feature worth learning it for: **every log line carries the same connection `uid`**.
Take the uid from a suspicious hash in `files.log` and pull the exact connection out of
`conn.log` and the hostname out of `dns.log`. That cross-log join is why analysts keep
Zeek beside Wireshark rather than instead of it.

## Install
```bash
brew install zeek       # macOS
# Debian/Ubuntu/Kali: NOT in the distro repos. Use the project's own OBS repository;
# pick your distro dir from https://download.opensuse.org/repositories/security:/zeek/
D=xUbuntu_24.04
echo "deb https://download.opensuse.org/repositories/security:/zeek/$D/ /" \
  | sudo tee /etc/apt/sources.list.d/security-zeek.list
curl -fsSL "https://download.opensuse.org/repositories/security:zeek/$D/Release.key" \
  | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
sudo apt update && sudo apt install zeek     # installs to /opt/zeek, not on PATH
```

## Usage
```bash
mkdir case-01 && cd case-01
/opt/zeek/bin/zeek -C -r ../capture.pcap                 # -C is not optional, see Gotchas
cat conn.log | zeek-cut -d ts id.orig_h id.resp_h id.resp_p service duration
cat dns.log  | zeek-cut query answers | sort | uniq -c | sort -rn
cat files.log | zeek-cut -d ts uid mime_type md5 filename
```

## Output
Tab-separated logs, each with a header block naming its columns. `zeek-cut` selects
columns by name from stdin - `-d` for readable local timestamps, `-u` for UTC, `-n` to
invert the selection. `notice.log` carries Zeek's flagged observations and `weird.log`
protocol anomalies.

## Gotchas
- **Always pass `-C` on an offline pcap.** NIC checksum offload means locally captured
  packets usually carry invalid checksums, and Zeek silently discards them. Without
  `-C` you get a near-empty `conn.log` and conclude the capture is empty.
- **`zeek-cut` cannot read JSON logs, and fails silently** - blank lines, exit 0. It
  parses the TSV `#fields` header. Use `jq` if you enabled `LogAscii::use_json`, and
  never strip the header or feed it grep-filtered fragments.
- **Not packaged by Debian, Ubuntu or Kali.** `apt install zeek` fails on a stock
  system, and `/opt/zeek/bin` is not added to `PATH` by the package.
- Zeek writes logs into the **current directory** and overwrites a previous run. One
  fresh directory per capture, or you will silently mix two cases.
- Old material says `bro -r` and `/usr/local/bro`; the binary and paths changed at 3.0.
- `notice.log` is not a verdict - it is what the policy scripts found interesting.
- Encrypted traffic yields metadata only: SNI, certificate subject, JA3-style
  fingerprints, never payload. The capture itself holds real personal data - see
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Wireshark / tshark](../capture/wireshark-tshark.md) - packet-level detail on one connection
- [NetworkMiner](networkminer.md) - artifacts and extracted files without the command line
- [tcpdump](../capture/tcpdump.md) - record the capture Zeek then reads
