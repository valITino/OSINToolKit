---
name: hakrawler
slug: hakrawler
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/hakluke/hakrawler
categories: [web-exploration, crawling-spidering]
tags: [crawler, urls, pipeline, fast]
status: active
status_checked: 2026-08-26
---

# hakrawler

## What question does it answer?
I have a URL (or a thousand). What links, subdomains, and JavaScript files does it
reference, right now, in one pipe?

## When to reach for it
When you want a fast first sweep and nothing else. hakrawler does one thing - read
URLs on stdin, crawl, print discovered URLs on stdout - which makes it the natural
middle of a shell pipeline rather than a tool you sit and configure. It is deliberately
smaller than [katana](katana.md): no headless browser, no JavaScript execution, so it
is quicker and lighter but blind to anything a single-page app renders client-side.

Start here to get a URL inventory in seconds; escalate to katana when the site turns
out to be a SPA.

## Install
```bash
go install github.com/hakluke/hakrawler@latest      # the recommended install
# Kali's 'apt install hakrawler' is an older build - see Gotchas
```

## Usage
```bash
echo https://example.com | hakrawler                       # crawl one site, depth 2 by default
cat hosts.txt | hakrawler -d 3 -subs                       # deeper, and include subdomains
echo https://example.com | hakrawler -u | tee urls.txt      # unique URLs only, saved
echo https://example.com | hakrawler | grep -Ei '\.js($|\?)'  # just the JavaScript to review
```

## Output
Plain URLs, one per line, ready for `sort -u`, a screenshotter, or a fuzzer. It emits
what it found and nothing else - there is no report mode, which is the point.

## Gotchas
- Crawling is **active**: every URL printed was a request to the target. Bound the
  depth and get authorisation for anything sustained -
  see [../../LEGAL.md](../../LEGAL.md).
- **No JavaScript execution.** On a React/Vue/Angular site it will find almost nothing;
  that is not a bug, it is the trade-off. Use [katana](katana.md) `-headless` there.
- It follows whatever it finds, including logout and state-changing links. Do not point
  it at an authenticated session you care about.
- Output is unfiltered and duplicates are common; `-u` for unique, or pipe to `sort -u`.
- **Do not install it from Kali's repo.** The project's own README says the packaged
  version is older, missing features, and may be buggy, and recommends `go install`
  or the Docker image instead.

## Alternatives
- [katana](katana.md) - headless crawling and JavaScript endpoint parsing
- [Photon](photon.md) - pulls emails, keys, and files out while it crawls
- [Wayback CDX](../../06-history-and-archives/web-archive/wayback-cdx-api.md) - historical URLs with zero contact
