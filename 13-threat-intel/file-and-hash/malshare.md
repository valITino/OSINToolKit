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
I have a hash. Was this file actually collected in the wild - from which URL,
under which filenames - and can I get a copy without asking a vendor for
permission?

## When to reach for it
For provenance, and for bulk. MalShare records the source URL a sample was
collected from and the names it travelled under - the detail that turns a lone
hash into a distribution story, and one few free sources record at all. The
daily hash lists also make it cheap to diff your own corpus against yesterday's.

Do not reach for it for a verdict - no engines, no scores, no family labels.
Use [MalwareBazaar](malwarebazaar.md) for family and campaign context,
[Hybrid Analysis](hybrid-analysis.md) for behaviour, VirusTotal for consensus.

## Install
```bash
# Nothing to install: a query-string HTTP API. Register free for a key at
# https://malshare.com/register.php, then keep it out of your shell history.
export MALSHARE_KEY=<your-key>
```
The official toolkit `MalShare/MalShare-Toolkit` was last committed to on
2019-09-24 and has no packaging; do not build on it.

## Usage
```bash
API=https://malshare.com/api.php?api_key=$MALSHARE_KEY

# Is this file known here, and what is recorded about it (MD5, SHA1 or SHA256)?
curl -s "$API&action=details&hash=<hash>"

# Provenance pivot. Syntax: [md5|sha1|sha256|source|type]:(query).
curl -s "$API&action=search&query=source:pastebin.com"

# How much of the 2000/day allowance is left - check this before any loop.
curl -s "$API&action=getlimit"

# Last 24h of hashes as plain text, for diffing against your own corpus.
curl -s "$API&action=getlistraw"
```

## Output
JSON for `details`, `getlist`, `getsources` and `hashlookup`; plain text lists
for `getlistraw`, `getsourcesraw` and `search`; raw bytes for `getfile`. The
documented dataset is hashes (MD5, SHA1, SHA256), file type, the source URLs
samples were collected from, and file names - nothing more. Read it for
provenance, never for a verdict: it answers "was this collected in the wild,
from where, and calling itself what". The corpus stood at 10.8M samples on
2026-08-29, collecting since 2013, and is 37.6% PE32 and 29.7% HTML - which
tells you what kind of question it can answer.

## Gotchas
- **The false-positive trap, in MalShare's own words:** "not all files in our
  system are malicious and our data feeds are considered as is." No AV results,
  no family labels. Presence is evidence of collection, not of maliciousness -
  never write "found in MalShare, therefore malicious".
- **The key travels in the URL query string**, so it lands in shell history,
  proxy logs and any `Referer`. Keep it in an environment variable and assume
  anything that logs URLs has it.
- **One 2,000-call daily allowance covers everything** - searches, lookups and
  downloads all draw on it; check `action=getlimit` before a loop.
- **`getfile` returns the raw, unwrapped executable** - no ZIP, no password. It
  will trip your own EDR and on Windows it is one double-click from running.
  MalwareBazaar's encrypted ZIP is the safer route to the same bytes; handle and
  store either per [../../LEGAL.md](../../LEGAL.md).
- **`action=download_url` is not passive.** It makes MalShare fetch, and
  optionally crawl, a URL you name - a live request to the target's server, with
  the result published. Keep it out of any workflow where the operator must not
  learn you are looking.
- **Uploading here is the least private option in this directory** - samples
  become downloadable in bulk by anybody holding a free key.
- **Terms that bite:** the web sample page is captcha-gated so the API is the
  only programmatic path; do not share your key or republish content without
  crediting MalShare; keys may be revoked without notice.
- **Coverage is collection-driven, not curated** - it skews to what crawlers
  and contributors pulled from open directories, pastes and URLs, so malware
  that never touched a public URL is absent. A miss says nothing about novelty.

## Alternatives
- [MalwareBazaar](malwarebazaar.md) - family labels, YARA and campaign pivots
- [Hybrid Analysis](hybrid-analysis.md) - what the sample does when it runs
- [Jotti's malware scan](jotti.md) - a small second-opinion engine check
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - engine count
