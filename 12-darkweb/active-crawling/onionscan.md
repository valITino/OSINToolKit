---
name: OnionScan
slug: onionscan
tier: 3
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/s-rah/onionscan
categories: [darkweb, active-crawling]
tags: [tor, onion, fingerprinting, correlation, legacy, v2-only]
status: broken
status_checked: 2026-08-29
---

# OnionScan

## What question does it answer?
I have a .onion address. Is the operator leaking themselves - a status page, an
open directory, EXIF in an uploaded image, a PGP key, an analytics ID, an
SSH/FTP/SMTP/Bitcoin banner that also appears on a clearweb host?

## Why this is tier 3
Broken, not merely old. Last commit 2017-02-25, last release 2016-10-29, and
`utils/validation.go` hard-codes `[a-z2-7]{16}\.onion` as a gate on the whole
pipeline: a source build on 2026-08-29 met a v3 address with `ERROR: Unknown
hidden service type` and ran nothing, while v2 services left the network in
October 2021. Use the maintained Go rewrite at
https://github.com/nao1215/onionscan, and keep this one open at
`doc/what-is-scanned-for.md`, the best checklist of operator mistakes there is.

For recognition and for that checklist, not for scanning: every course in this
space cites it, so you need to know why the command they hand you fails.

## Install
```bash
# `go get` is refused since Go 1.17; `go install ...@latest` dies on x/crypto.
git clone https://github.com/s-rah/onionscan && cd onionscan
rm -rf .git && go mod init github.com/s-rah/onionscan   # then hand-pin in
# go.mod: tiedot, goexif, x/crypto v0.21.0, x/net v0.23.0, and finally
go mod tidy && go build -o onionscan .   # builds clean on Go 1.24.7
```

## Usage
```bash
./onionscan --torProxyAddress=127.0.0.1:9050 <16char-v2>.onion   # basic run
./onionscan --verbose --jsonReport <16char-v2>.onion   # the report as JSON
./onionscan --mode analysis --webport 8080   # Correlation Lab UI over the
# database earlier scans built - it reads that database and scans nothing
```

## Output
Plain text by default: the address, then `No risks were found.` or a risk list.
`--jsonReport` carries the real product: `online`, a boolean detector per
protocol scanned, `pgpKeys[]`, `certificates[]`, `sshKey`/`sshBanner`,
`bitcoinServices{}`. Which identifier also appears elsewhere is the finding.

## Gotchas
- **It rejects every onion address that exists**, and patching that gate does
  not save it: the link extractor uses the same regex, so a modern page yields
  zero onion links and the Correlation Lab draws an empty graph that reads like
  a genuine negative. Issue #157 has asked for v3 support since 2018.
- **Intrusive, not merely active.** It probes directories, fetches common paths
  and banner-grabs SSH/FTP/SMTP/VNC/MongoDB/XMPP/IRC/Bitcoin, and
  `--fingerprint=false` is louder still. Written authorisation, as anywhere.
- `--webport` defaults to 8080 and opens that listener even in scan mode unless
  set to 0 - an unexpected socket on your analysis host.
- Nothing is submitted anywhere and no account is needed, but a scan pulls down
  whatever the service serves: illegal material appears unbidden, possessing it
  is an offence in most jurisdictions whatever your intent, and finding it
  brings reporting and evidence-handling duties -
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [TorBot](torbot.md) - the crawl and link tree, and it handles v3 addresses
- [docker-onion-nmap](onion-nmap.md) - which advertised ports actually answer
- [WhatWeb](../../04-web-exploration/fingerprinting/whatweb.md) - a page's
  technology fingerprint, driven through a SOCKS proxy
