---
name: Jotti's malware scan
slug: jotti
tier: 3
contact: active
type: web
cost: free
platforms: [web]
url: https://virusscan.jotti.org/
categories: [threat-intel, file-and-hash]
tags: [multi-engine, hash-lookup, second-opinion, legacy]
status: active
status_checked: 2026-08-29
---

# Jotti's malware scan

## What question does it answer?
I have a file, or only its hash. Have these thirteen engines ever seen this
exact file - and if I have to scan something, can I do it somewhere smaller and
quieter than VirusTotal?

## Why this is tier 3
Not because it is broken - Jotti is alive and scanning today - but because it
is narrow and superseded on every axis this directory cares about. Thirteen
engines against VirusTotal's roughly seventy; a hash index covering only files
previously scanned through Jotti, so misses are meaningless; no family tags, no
YARA, no sandbox pull-through, no C2, so no campaign context at all; and no free
API. The roster is dated too: Cyren is still listed although Cyren Ltd. was
declared insolvent and ceased operating in February 2023.

Use [MalwareBazaar](malwarebazaar.md) for family and campaign context,
[Hybrid Analysis](hybrid-analysis.md) for behaviour, and VirusTotal for engine
breadth. Jotti earns an entry for recognition and for two narrow real uses.

## When to reach for it
Two cases. As a free, no-account, passive second-opinion hash check against a
corpus almost nobody else indexes - a hit is a genuine extra data point. And as
a lower-profile scanner when policy forbids VirusTotal, accepting that the file
still reaches thirteen vendors and human analysts. Anything else - breadth,
family, behaviour, infrastructure - belongs to the other three tools here; if
the sample must stay unseen, Jotti is upload-first by design and wrong for you.

## Install
None. Web only, no account, and no free API - the API page advertises a paid
bulk-scanning service you obtain by contacting Jotti, so any guide claiming a
free Jotti API is wrong. Everything below is a browser or a curl request.

## Usage
```text
https://virusscan.jotti.org/en-US/search/hash/44d88612fea8a8f36de82e1278abb02f
# PASSIVE hash lookup, plain GET: MD5, SHA1, SHA256 or SHA512. Returns an
# existing report, or an empty form page meaning "not in Jotti's index".

https://virusscan.jotti.org/en-US/filescanjob/<jobid>
# The permanent PUBLIC report URL an upload returns - any holder can read it.
```
```bash
# LAST RESORT: this hands the file to 13 vendors. Max 5 files, 250 MB each.
curl -sL -F 'sample-file[]=@sample.bin' -F 'submit=Submit' \
  https://virusscan.jotti.org/en-US/submit-file
```

## Output
An HTML report: name, size, the libmagic type string, Jotti's own first-seen
date, MD5, SHA1, a status line ("Scan finished. 1/13 scanners reported
malware."), the scan date, then a row per engine with its signature-database
date and either "Found nothing" or a detection name. Read the per-engine dates
first - a clean from an engine whose definitions are stale is not a clean, and
in a live scan on 2026-08-29 twelve engines were current while one lagged a day.
Then the ratio, then the detection names, which are the family hints worth
pivoting on elsewhere. First-seen is Jotti-local, never a global first sighting.

## Gotchas
- **Uploading is a disclosure event, not a lookup.** The privacy policy is
  explicit that files are stored, shared with anti-malware companies and read by
  security analysts, and the resulting report sits at a public URL retrievable
  by hash. Operators who watch multiscanners for their own hashes will see it.
  The hash search is the only passive half of this tool.
- **A miss proves nothing.** The index covers only files scanned through Jotti -
  even the canonical EICAR MD5 returns no record. Never write "unknown to Jotti"
  as evidence that a file is novel.
- **Ratios are not comparable to VirusTotal's:** thirteen engines, and Linux
  builds, which the FAQ admits give different results from the same vendors'
  desktop products. Discount the Cyren row entirely.
- **Reports show only MD5 and SHA1**, no SHA256, though the search box accepts
  both - you cannot copy a SHA256 out of a report. Results are also
  asynchronous: a fetch straight after an upload shows a queue position, so you
  have to re-fetch the job URL.
- **Files are never returned to you** and no rate limit is published, so there
  is no documented allowance either. Jotti is not a sample repository: do not
  let it hold your only copy, and store what you keep in line with
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [MalwareBazaar](malwarebazaar.md) - family, tags and campaign pivots
- [Hybrid Analysis](hybrid-analysis.md) - behaviour, processes and C2
- [MalShare](malshare.md) - where the file was collected in the wild
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - engine count
