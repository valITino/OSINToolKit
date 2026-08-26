---
name: Photon
slug: photon
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/s0md3v/Photon
categories: [web-exploration, crawling-spidering]
tags: [crawler, osint, emails, secrets, files]
status: unverified
status_checked: 2026-08-26
---

# Photon

## What question does it answer?
While crawling this site, what OSINT falls out of it - emails, social handles, API
keys, document links, subdomains?

## When to reach for it
When the crawl is the means and the extraction is the point. Photon is built for
OSINT rather than for coverage: it sorts what it finds into categories as it goes, so
you finish with ready-made lists of emails and files instead of a pile of URLs to
grep. Pair it with [katana](katana.md) when you also need JavaScript-heavy routes.

## Install
```bash
git clone https://github.com/s0md3v/Photon.git
cd Photon && pip3 install -r requirements.txt
```

## Usage
```bash
python3 photon.py -u https://example.com                 # crawl and categorise
python3 photon.py -u https://example.com -l 3 -t 10       # depth 3, 10 threads
python3 photon.py -u https://example.com --dns            # also collect DNS data
```

## Output
A directory named after the target containing one file per category: `emails.txt`,
`files.txt`, `intel.txt`, `robots.txt`, `external.txt`, and more. The file list is
the useful hand-off to [ExifTool](../../07-documents-metadata/metadata-extraction/exiftool.md).

## Gotchas
- Crawling is **active**. Depth and thread count directly control how much noise you
  make - start low.
- Its "secrets" extraction is regex-based and produces false positives; verify a hit
  before treating it as a live credential, and never test a found credential without
  authorisation (out of scope here).
- The project has not moved much in recent years; verify it runs in your environment.
  Status is `unverified` deliberately.

## Alternatives
- [katana](katana.md) - better coverage, JavaScript-aware
- [theHarvester](../../01-orchestrators/aggregators/theharvester.md) - emails without crawling the site
- [TruffleHog](../../09-code-paste-forums/secret-scanning/trufflehog.md) - secrets, done properly
