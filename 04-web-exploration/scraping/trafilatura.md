---
name: trafilatura
slug: trafilatura
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://trafilatura.readthedocs.io/
categories: [web-exploration, scraping]
tags: [boilerplate-removal, article-text, metadata, sitemap, batch]
status: active
status_checked: 2026-08-29
---

# trafilatura

## What question does it answer?
I have a page of HTML and I need the article out of it: the body text without
the navigation, cookie banner, share buttons and ads, plus whatever the page
claims as its title, author and publication date.

## When to reach for it
When the unit of analysis is the text - comparing wording across mirrors,
feeding a corpus into search, reading 400 saved pages you cannot open by hand.
It is not really a crawler; it is what you run over the output of
[HTTrack Website Copier](httrack.md) or [Scrapy](scrapy.md). Do not make it your only
extractor on pages that matter: it returns confident metadata for pages that are
not articles at all (see Gotchas), so corroborate anything load-bearing against
the page itself or a second extractor.

## Install
```bash
pip install trafilatura   # Python 3.10+; ships the CLI and the library together
trafilatura --version     # verified here: Trafilatura 2.2.0 on Python 3.11.15
```

## Usage
```bash
trafilatura -u "https://example.org/article" --json --with-metadata
# single URL, one JSON object out, metadata fields included
curl -sSL "https://target.example/article" | trafilatura --markdown --with-metadata
# HTML on stdin: use this when you need your own TLS, proxy or cookie handling
trafilatura --input-file links.txt --output-dir converted/ --backup-dir html/ --xml
# batch a URL list and KEEP the raw HTML sources - --backup-dir is what makes it auditable
trafilatura --sitemap "https://target.example/" --list > links.txt
# harvest the URL inventory from the sitemap without downloading pages (--feed for RSS)
```

## Output
With `--json`, one object per document. Verified key set on 2.2.0: title,
author, hostname, date, fingerprint, id, license, comments, raw_text, text,
language, image, pagetype, filedate, source, source-hostname, excerpt,
categories, tags. `date` is the tool's guess at publication, `filedate` is your
capture date, and `fingerprint` is a content hash - how you spot the same
article syndicated across a dozen domains. `--markdown` gives a YAML
front-matter block above the body. Treat `text` and `date` as claims.

## Gotchas
- **It invents metadata on non-article pages, and this is the trap.** Verified
  here: on a 404 page it returned author "Wp-Block-Co-Authors-Plus-Coauthors
  Is-Layout-Flow" (a CSS class string) and date 2021-02-01 (read out of an image
  path `/files/2021/02/`); on a blog index it returned the nav menu as the body.
  Never report an author or a date from this tool without opening the page.
- `--only-with-metadata` does not save you: it filters on the *presence* of
  title, URL and date, not their correctness, and both fakes above count.
- **A short `text` is the tell.** On index, tag and error pages the body is the
  navigation menu. Check length against what you saw in the browser.
- **Its downloader ignores `REQUESTS_CA_BUNDLE`.** Verified here: behind a
  TLS-intercepting proxy, `-u` died with `SSLCertVerificationError` while piping
  `curl` output in worked. In any proxied environment, fetch it yourself.
- `--crawl` and `--sitemap` turn a page extractor into a crawler with no
  prominent politeness control. Rate-limit at your own layer, and remember that
  wholesale collection of personal data is regulated - [../../LEGAL.md](../../LEGAL.md).
- v2.0.0 broke the library API: `bare_extraction()` returns a Document, not a
  dict, and `no_fallback` became `fast`. 1.x snippets fail or drift silently,
  and `--fast` skips the fallback cascade - quicker, worse on awkward markup.

## Alternatives
- [Scrapy](scrapy.md) - when you want specific fields, not the whole article
- [HTTrack Website Copier](httrack.md) - keep the pages first, extract from the mirror after
- [Playwright](playwright.md) - get the rendered DOM to feed in on stdin
