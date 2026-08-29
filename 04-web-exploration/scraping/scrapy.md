---
name: Scrapy
slug: scrapy
tier: 2
contact: active
type: library
cost: free
platforms: [linux, macos, windows]
url: https://scrapy.org/
categories: [web-exploration, scraping]
tags: [framework, python, structured-data, throttling, feed-export]
status: active
status_checked: 2026-08-29
---

# Scrapy

## What question does it answer?
I have a site holding thousands of records - listings, profiles, filings -
behind paginated HTML. How do I pull them into JSON or CSV with retries,
throttling and resumability, instead of a script that dies at page 40 and leaves
me unsure what it missed?

## When to reach for it
When the shape of the answer is a table and the volume justifies building a
spider. Below a few hundred pages a `curl` loop is honest and faster to write.
For the pages themselves, mirror with [httrack.md](httrack.md); for readable
article text, pipe HTML into [trafilatura.md](trafilatura.md). Scrapy renders no
JavaScript - selectors that work in devtools return empty lists with no error -
so a client-side site needs scrapy-playwright or [playwright.md](playwright.md).
For "what URLs exist here" rather than "what data is in them",
[katana](../crawling-spidering/katana.md) is the smaller tool.

## Install
```bash
python3 -m venv .venv && . .venv/bin/activate  # the docs strongly recommend a venv
pip install Scrapy   # Python 3.10+; conda install -c conda-forge scrapy on Windows
```

## Usage
```bash
scrapy shell 'https://quotes.toscrape.com/page/1/'
# a live `response` object: prove every CSS/XPath selector here before writing a spider
scrapy startproject tutorial
# scaffolds the project - its settings.py sets ROBOTSTXT_OBEY=True and DOWNLOAD_DELAY=1
scrapy crawl quotes -O quotes.json
# -O overwrites; lowercase -o appends, and appending to .json yields invalid JSON
scrapy crawl quotes -O out.json -a tag=humor
# -a passes a runtime argument in, so one spider serves many targets
```

## Output
Feed exports in JSON, JSON Lines, CSV or XML at the `-o`/`-O` path, one object
per item; since 2.18.0 exporters emit fields in declaration order, so a defined
Item class gives a stable column order across runs. Read the stats dict on
stderr beside the data: `item_scraped_count` against the count you expected, and
`downloader/response_status_count/403` and `/404` to tell "the site has fewer
records" from "it started refusing us halfway". A `finish_reason` of
`closespider_timeout` or `memusage_exceeded` means the dataset is truncated.

## Gotchas
- **Two sets of defaults, and this catches people.** The library defaults are
  `ROBOTSTXT_OBEY=False` and `DOWNLOAD_DELAY=0`; the `settings.py` from
  `startproject` sets `True` and `1`. Read the actual settings file before
  claiming you respected robots.txt.
- **`CONCURRENT_REQUESTS` defaults to 16.** With no delay that is high-rate
  mirroring - intrusive by any honest reading, enough to degrade a small target
  or get you blocked. Enable `AUTOTHROTTLE_ENABLED` for anything unsized.
- **The default User-Agent is `Scrapy/VERSION (+https://scrapy.org)`** - you
  announce yourself as a scraper in every request. Changing it is a
  terms-of-service decision, not a technical one, and automating a search engine
  or a social platform breaches its terms whatever the header says.
- **It captures records, not provenance.** Raw responses are not retained by
  default, so a scraped CSV is a derived artefact; add the HTTP cache middleware
  or a separate WARC capture if a page must be citable later.
- The homepage changelog lagged at 2.17.0 while PyPI shipped 2.18.0; take the
  version from PyPI. Scraped profiles are personal data - [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [trafilatura.md](trafilatura.md) - article text and metadata, no spider to write
- [httrack.md](httrack.md) - keep the pages themselves rather than fields
- [playwright.md](playwright.md) - when the records only exist after JavaScript runs
