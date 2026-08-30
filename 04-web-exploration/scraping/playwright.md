---
name: Playwright
slug: playwright
tier: 2
contact: active
type: library
cost: free
platforms: [linux, macos, windows]
url: https://playwright.dev/
categories: [web-exploration, scraping]
tags: [headless-browser, rendered-dom, screenshot, javascript, trace]
status: active
status_checked: 2026-08-29
---

# Playwright

## What question does it answer?
The page is empty in `curl` and full in my browser. How do I get the DOM after
JavaScript runs, and capture what a visitor actually sees - with a record of the
requests behind it, not just a picture?

## When to reach for it
When the content only exists after client-side rendering, when a capture must
show the page as rendered, or when a site varies by locale or geography. For
static HTML it is overkill - [Scrapy](scrapy.md), or `curl` into
[trafilatura](trafilatura.md), is faster and quieter. For a whole-site copy
use [HTTrack Website Copier](httrack.md); for screenshot sweeps across many hosts
[gowitness](../monitoring-visual/gowitness.md) is smaller. Playwright is what
you build on when none of those can see the content.

## Install
```bash
pip install pytest-playwright && playwright install  # Python; PyPI 1.62.0 needs 3.10+
npm init playwright@latest   # Node (22.x/24.x/26.x); add --with-deps on Linux containers
```

## Usage
```python
page.screenshot(path="capture.png", full_page=True)
# the standard "this is what the page looked like" artefact, whole scrollable page
page.locator(".header").screenshot(path="header.png")   # crop to one element
```
```bash
playwright codegen target.example --save-storage=auth.json
# log in by hand once, persist the session; replay later with --load-storage=auth.json
playwright codegen --timezone="Europe/Rome" --geolocation="41.890221,12.492348" \
  --lang="it-IT" bing.com/maps
# see the geo- and locale-varied page: how you prove a site serves different content by region
```

## Output
Screenshots and PDFs on disk, plus a live `page` object exposing the
post-JavaScript DOM (`page.content()`, locators, `page.request`). Test runs give
an HTML report (`npx playwright show-report`) and, with tracing on, a trace
replayed with per-step DOM snapshots, console output and the network log. Read
the trace, not the screenshot: a PNG has no headers, no URL bar and no server
timestamp, so alone it proves only that somebody produced an image.

## Gotchas
- **`auth.json` from `--save-storage` is a credential.** It holds live session
  cookies and will authenticate anyone who has it. Never commit it to a case
  repo, and treat a persistent profile the same way.
- **Loading a session means browsing as a real account.** Everything you touch is
  attributable to it and the platform's terms on automated access apply to it -
  an OPSEC and legal decision, not a config flag. See
  [../../LEGAL.md](../../LEGAL.md), which also covers scraped personal data.
- **There are two things called the Playwright CLI.** The `@playwright/test`
  package gives `codegen`, `test`, `show-report`, `install`; a separate
  `@playwright/cli` package gives the `playwright-cli screenshot --full-page`
  and `playwright-cli pdf` commands. Advice online conflates them constantly.
- **Automation is detected.** Cloudflare/Datadome-class defences fingerprint
  headless browsers, and you will cheerfully screenshot a challenge page
  believing you captured the target. Assert on content, not on a file existing.
- **`playwright install` pulls hundreds of megabytes** of Chromium, Firefox and
  WebKit, and on Linux needs `--with-deps` or launches fail with cryptic
  missing-library errors. Not a tool to drop on a locked-down box mid-case. The
  Python docs also still claim 3.8+ while PyPI 1.62.0 requires 3.10+.

## Alternatives
- [HTTrack Website Copier](httrack.md) - a whole-site mirror plus WARC, where no JavaScript is needed
- [trafilatura](trafilatura.md) - feed it the rendered DOM to get clean article text
- [gowitness](../monitoring-visual/gowitness.md) - bulk screenshots across many hosts
