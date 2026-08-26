---
name: metagoofil
slug: metagoofil
tier: 3
contact: passive
type: cli
cost: free
platforms: [linux]
url: https://github.com/opsdisk/metagoofil
categories: [documents-metadata, harvest-from-web]
tags: [documents, metadata, harvesting, broken]
status: broken
status_checked: 2026-08-26
---

# metagoofil

## What question does it answer?
What documents has this organisation published, and what usernames, software, and
paths are in their metadata?

## Why this is tier 3
The idea is excellent - harvest an org's public documents, extract metadata in bulk,
build a list of internal usernames and software versions. The execution is not:
**it reportedly returns empty results on both the laramies and opsdisk repos.** It
depends on scraping search-engine results, and search engines have changed their
handling of automated queries, so the harvesting stage yields nothing and everything
downstream is empty.

Do the job manually instead - the workflow below is reliable and takes minutes.

## Install
```bash
# Kali packages metagoofil, but see the status above before relying on it.
git clone https://github.com/opsdisk/metagoofil.git
```

## Usage
```bash
# The intended usage:
metagoofil -d example.com -t pdf,docx -l 100 -o docs/

# The manual replacement that actually works:
#  1. Dork for the files:      site:example.com filetype:pdf
#  2. Download what you find:  wget -i urls.txt
#  3. Extract in bulk:         exiftool -a -u -g1 docs/*
```

## Output
Intended: downloaded documents plus a summary of extracted usernames, software, and
paths. In practice, expect an empty result set.

## Gotchas
- **Both maintained forks are reported to return nothing.** Verify with a known-good
  target before spending time on it; assume the manual route.
- The concept is passive, but automated search-engine scraping breaches those engines'
  terms - another reason the manual dork-and-download route is preferable.
- Extracted usernames are genuinely valuable when you get them: they often match
  internal account naming conventions.

## Alternatives
- [Dorking](../../04-web-exploration/dorking/README.md) plus `wget` plus [ExifTool](../metadata-extraction/exiftool.md) - the working manual pipeline
- [Photon](../../04-web-exploration/crawling-spidering/photon.md) - crawls and collects file links
- [FOCA](foca.md) - the Windows GUI equivalent, also tier 3
