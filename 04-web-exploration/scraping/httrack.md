---
name: HTTrack Website Copier
slug: httrack
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://www.httrack.com/
categories: [web-exploration, scraping]
tags: [mirroring, offline-copy, warc, wacz, evidence]
status: active
status_checked: 2026-08-29
---

# HTTrack Website Copier

## What question does it answer?
I have a site that may change or vanish. Can I take a complete offline copy of
it - and, on the current engine, a WARC/WACZ of the original bytes - so what I
read today is still readable and citable next year?

## When to reach for it
When the whole site is the artefact: a defunct shopfront, a claim page, a forum
you expect to be pulled. It is wrong for a single page (fetch it and run
[trafilatura](trafilatura.md)), wrong for structured records
([Scrapy](scrapy.md)), and useless on anything rendered client-side - it runs
no JavaScript, so a single-page app mirrors as an empty shell. Check
[the archives](../../06-history-and-archives/web-archive/README.md) first: if
someone already captured it, take the copy that touches nobody.

## Install
```bash
sudo apt install httrack   # kali-rolling has 3.49.23-1; webhttrack is the GUI
httrack --help 2>&1 | grep -i warc  # packaged builds lag: confirm flags exist
# Current engine: httrack-3.49.25.tar.gz, httrack.com/page/2/en/index.html
```

## Usage
```bash
httrack "http://www.all.net/" -O "/tmp/www.all.net" "+*.all.net/*" -v
# users-guide example: one site, one output dir, stay in scope, log to screen
httrack "https://target.example/" -O /cases/001 -%r --warc-file target --warc-cdx --wacz
# evidence mode: ISO-28500 WARC/1.1 bytes, a CDXJ index, packaged as WACZ
httrack "https://target.example/" -O /cases/001 -%d --update
# re-crawl the case; hts-changes.json lists new, changed, unchanged and gone
httrack "https://target.example/" -O /cases/001 -c1 -%c1 -A25000 -%G5:10 -F "you@example.org"
# polite: one socket, 1 conn/sec, 25 KB/s, 5-10s random pause, identify yourself
```

## Output
A tree under `-O`: an `index.html` entry point, the rehydrated site,
`hts-cache/` with the exact option set used, and `hts-log.txt`. Read the log
first - the 403s, redirect loops, robots exclusions and truncations are recorded
only there, and a mirror that looks complete in a browser routinely is not.
`-%r` adds a WARC file, `--warc-cdx` a CDXJ index, `--wacz` one package. The
tree is for reading; the WARC is for citing.

## Gotchas
- **The download page is not the repo.** Windows stable is httrack-3.49.2.exe
  from May 2017; the engine went 3.49.16 to 3.49.25 in August 2026 alone.
- **The mirror is not the bytes the server sent.** HTTrack rewrites links so the
  copy browses offline, and that rewriting is exactly what an opposing party
  attacks. Use `-%r` for anything that must survive scrutiny.
- **Defaults are genuinely intrusive**: 8 sockets and 5 connections/second
  across a whole site is attack-shaped traffic, and wholesale mirroring breaches
  most terms of service. Throttle, and hold written authorisation - see
  [../../LEGAL.md](../../LEGAL.md), which also covers mirrored personal data.
- **robots.txt has a carve-out.** A sitemap named with `--sitemap-url` or
  declared in robots.txt is fetched even under a Disallow; only the guessed
  `/sitemap.xml` respects it. `-s0` is a deliberate act - justify it in notes.
- Cgi-bin and JS-built filenames are a documented limit: a gap there is tool
  behaviour, not evidence the content never existed.

## Alternatives
- [Playwright](playwright.md) - JavaScript-rendered pages HTTrack cannot see
- [Scrapy](scrapy.md) - records in JSON, rather than a browsable tree
- [katana](../crawling-spidering/katana.md) - map URLs without keeping the bytes
- [Web archives](../../06-history-and-archives/web-archive/README.md) - someone else's copy, no contact
