---
name: MalShare
slug: malshare
tier: 2
contact: passive
type: api
cost: free
platforms: [web, linux, macos, windows]
url: https://malshare.com/
categories: [threat-intel, file-and-hash]
tags: [malware-samples, provenance, hash-lookup, corpus, sample-download]
status: active
status_checked: 2026-08-29
---

# MalShare

## What question does it answer?
I have a hash. Was this file collected in the wild - from which URL, under which
filenames - and can I get a copy without asking a vendor?

## When to reach for it
For provenance, and for bulk. MalShare records the source URL a sample was
collected from and the names it travelled under - the detail that turns a lone
hash into a distribution story, and one few free sources record at all. The
daily hash lists also make it cheap to diff your own corpus against yesterday's.

## Install
```bash
# Nothing to install: a query-string HTTP API. The official MalShare-Toolkit
# repo, last committed 2019-09-24, has no packaging; do not build on it.
export MALSHARE_KEY=<key>   # free registration at malshare.com/register.php
```

## Usage
```bash
API=https://malshare.com/api.php?api_key=$MALSHARE_KEY
# Is this file known here, and what is recorded about it (MD5, SHA1 or SHA256)?
curl -s "$API&action=details&hash=<hash>"
# Provenance pivot. Syntax: [md5|sha1|sha256|source|type]:(query).
curl -s "$API&action=search&query=source:pastebin.com"
# Last 24h of hashes as plain text, for diffing against your own corpus.
curl -s "$API&action=getlistraw"
```

## Output
JSON for `details`, `getlist`, `getsources` and `hashlookup`; plain text for
`getlistraw`, `getsourcesraw` and `search`; raw bytes for `getfile`. The
documented dataset is hashes (MD5, SHA1, SHA256), file type, source URLs and
file names - nothing more: read it for provenance, never for a verdict. The
corpus stood at 10.8M samples on 2026-08-29, collecting since 2013, and is 37.6%
PE32 and 29.7% HTML - which tells you what kind of question it can answer.

## Gotchas
- **The false-positive trap, in MalShare's own words:** "not all files in our
  system are malicious and our data feeds are considered as is." No AV results,
  no family labels; presence is evidence of collection, not of maliciousness.
- **The key travels in the URL query string** - shell history, proxy logs, any
  `Referer`. Keep it in an environment variable, never share it (keys can be
  revoked without notice), and assume anything logging URLs has it.
- **One 2,000-call daily allowance covers everything** - searches, lookups and
  downloads all draw on it; check `action=getlimit` before a loop.
- **`getfile` returns the raw, unwrapped executable** - no ZIP, no password. It
  will trip your own EDR, and on Windows it is one double-click from running;
  MalwareBazaar's encrypted ZIP is the safer route to the same bytes. Store
  either per [../../LEGAL.md](../../LEGAL.md).
- **Uploading here is the least private option in this directory**: samples
  become downloadable in bulk by anybody with a free key. And
  **`action=download_url` is not passive**: it makes MalShare fetch, and
  optionally crawl, a URL you name - a live request to the target, published.
- **The web sample page is captcha-gated**, so the API is the only programmatic
  path, and republishing content requires crediting MalShare.
- **Coverage is collection-driven, not curated** - it skews to what crawlers and
  contributors pulled from open directories, pastes and URLs, so malware that
  never touched a public URL is absent. A miss says nothing about novelty.

## Alternatives
- [MalwareBazaar](malwarebazaar.md) - family labels, YARA and campaign pivots
- [Hybrid Analysis](hybrid-analysis.md) - what the sample does when it runs
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - engine count
