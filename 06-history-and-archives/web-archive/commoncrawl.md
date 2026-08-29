---
name: Common Crawl
slug: commoncrawl
tier: 2
contact: passive
type: api
cost: free
platforms: [web, linux, macos, windows]
url: https://commoncrawl.org/
categories: [history-and-archives, web-archive]
tags: [crawl-data, cdx-index, warc, bulk, parquet]
status: active
status_checked: 2026-08-29
---

# Common Crawl

## What question does it answer?
I have a domain. Which of its URLs did an independent crawl of the whole web see
in a given month, and can I read the page bytes it stored - without sending a
single packet to the target?

## When to reach for it
When you want a third party's own copy of the web at a fixed point in time, or a
question bigger than one site: every host under a TLD, every PDF on a domain.
Each monthly crawl has its own CDX index (CC-MAIN-2026-34 ran 7-20 August 2026,
2.14 billion pages), so two crawls bracket a change to a month. Wrong tool for
"what did this page say last Tuesday" - use [Wayback CDX API](wayback-cdx-api.md)
- and overkill for a plain URL list, which [gau](gau.md) already sources here.

## Install
```bash
# The index is plain HTTP - nothing to install for a one-off query.
pip install cdx_toolkit   # maintained client (0.9.39, June 2026), CLI is `cdxt`
# Avoid ikreymer/cdx-index-client: no commit since Oct 2018, examples target 2015.
aws s3 cp --no-sign-request s3://commoncrawl/crawl-data/CC-MAIN-2026-34/cc-index.paths.gz .
```

## Usage
```bash
# The index is PER CRAWL. List them first - there is no all-time endpoint.
curl -s 'https://index.commoncrawl.org/collinfo.json' | jq -r '.[].id' | head
# Every URL the August 2026 crawl saw under a domain (one JSON object per line).
curl -s -A 'osint-research (you@example.org)' \
  'https://index.commoncrawl.org/CC-MAIN-2026-34-index?url=example.com%2F*&output=json' \
  | jq -r '.url' | sort -u
# Same via the maintained client, sweeping the last three crawls:
cdxt --crawl 3 --limit 1000 --filter '=status:200' iter 'example.com/*'
cdxt --cc --limit 50 warc 'example.com/*'   # fetch the archived bodies as WARC
```

## Output
One record per capture: `urlkey` (SURT, `org,iana)/`), `timestamp`, `url`, `mime`,
`mime-detected`, `status`, `digest`, `length`, `offset`, `filename`, `languages`.
`url` + `timestamp` + `status` is the existence proof: this URL answered 200 on
that date, witnessed by neither you nor the site owner. `digest` is the change
detector - one that flips between crawls dates the edit to that month. `filename`
+ `offset` + `length` address a byte range in the crawl's WARC set under
`data.commoncrawl.org`, so you can pull the exact HTML the crawler saw.

## Gotchas
- **It is a sample, not a census.** The FAQ: "we do not generally archive any
  entire website but a randomly selected subset of it." Absence of a URL is not
  evidence the page never existed - cross-check [Wayback CDX API](wayback-cdx-api.md).
- **URL-keyed, not full text.** It matches URL/SURT prefixes only; searching page
  *content* means the WET extracted-text files or SQL over the columnar Parquet
  index (`s3://commoncrawl/cc-index/table/cc-main/warc/`) in Athena or Spark.
- **No all-crawls endpoint.** A domain missing from August may be there in June.
  Iterate `collinfo.json` or use `cdxt --crawl`, which silently caps at one year
  of indexes and 1000 records unless given `--from`/`--to`/`--limit`.
- **Heavy rate limiting; 503s are routine.** Upstream asks for under 10 requests
  per second, one thread per IP, a real User-Agent and 10-second retry backoff.
- **CCBot obeys robots.txt and there is an opt-out registry**, so zero records may
  mean the site blocked the crawler. Bodies over the fetch limit (5 MiB since
  March 2025) are truncated, so hashes of long pages will not match the original.
- Open data still carries duties: a local copy of scraped third-party pages has
  the same copyright and data-protection exposure as anywhere else. See
  [../../LEGAL.md](../../LEGAL.md) when personal data is in scope.

## Alternatives
- [Wayback CDX API](wayback-cdx-api.md) - one site's whole timeline, fresher, and the cross-check when this returns nothing
- [gau](gau.md) - merges Common Crawl with Wayback and OTX when a URL list is all you need
- [waybackpack](waybackpack.md) - every capture of one page on disk, not one crawl's index
