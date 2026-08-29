# Scraping

Crawling maps what a site links to. Scraping takes the content away and keeps
it: a mirror you can grep offline, a table of records, the readable text without
the navigation, the video before it is deleted. In an investigation the copy
matters as much as the finding - sites change, and a screenshot is not a
dataset.

Crawling and scraping overlap; the split in this repo is by intent. See
[../crawling-spidering/](../crawling-spidering/) when the question is "what
exists here", and this directory when the answer is "and I need to keep it".

## Contact level, honestly

- Fetching a handful of pages at human speed is `active`.
- Mirroring an entire site, or running a spider at full rate, is `intrusive` in
  everything but name: it is indistinguishable from a scraping attack in the
  target's logs, it can knock over a small site, and it is exactly the behaviour
  rate limits exist to stop. Throttle it, and have authorisation before you
  point it at anything you do not own.
- Pulling the same content from an archive instead touches nothing at all. If
  [Wayback](../../06-history-and-archives/web-archive/) has what you need, take
  it from there.

## Rules that keep the output usable as evidence

- **Record the fetch, not just the file.** Timestamp, URL, HTTP status, and a
  hash of what you stored. A mirror with no provenance proves nothing later.
- **Keep the raw response.** Extraction is lossy and you will want to re-parse
  it when the question changes.
- **Respect robots.txt as a default,** and note deliberately when you do not and
  why. It is not law, but ignoring it silently is hard to defend afterwards.
- **Scraped personal data is still personal data.** Public availability is not a
  lawful basis, and a scraped corpus of profiles is regulated - see
  [../../LEGAL.md](../../LEGAL.md).
- **Automating a search engine or a social platform breaches its terms** and
  usually its rate limits. Expect blocks, and never route them through an
  account you care about.

## Choosing the tool

| I want | Reach for |
|---|---|
| An offline copy I can browse and grep | A site mirroring tool |
| Structured records from many pages | A crawling framework with extraction rules |
| Just the article text, minus the furniture | A text-extraction library |
| A page that only exists after JavaScript runs | A headless browser |
| A video, its subtitles and its metadata | A media downloader |

## Tools here

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [HTTrack Website Copier](httrack.md) | I have a site that may change or vanish. Can I take a complete offline copy of it - and, on the current engine, a WARC/WACZ of... | 2 | intrusive |
| [Playwright](playwright.md) | The page is empty in `curl` and full in my browser. How do I get the DOM after JavaScript runs, and capture what a visitor... | 2 | active |
| [Scrapy](scrapy.md) | I have a site holding thousands of records - listings, profiles, filings - behind paginated HTML. How do I pull them into JSON or... | 2 | active |
| [trafilatura](trafilatura.md) | I have a page of HTML and I need the article out of it: the body text without the navigation, cookie banner, share buttons and... | 2 | active |
| [yt-dlp](yt-dlp.md) | I have a video URL that may be deleted, edited or made private. How do I preserve it and everything around it - channel ID... | 2 | active |
| [snscrape](snscrape.md) | I have a handle or a channel name and no API key. Can I still pull that account's posts - and, more often now, is a dataset that... | 3 | active |
<!-- END:TOOLS -->

## Related

- [../crawling-spidering/README.md](../crawling-spidering/README.md) - discovery rather than capture
- [../monitoring-visual/README.md](../monitoring-visual/README.md) - watching a page change over time
- [../../06-history-and-archives/web-archive/README.md](../../06-history-and-archives/web-archive/README.md) - somebody else's copy, taken without contact
- [../../07-documents-metadata/README.md](../../07-documents-metadata/README.md) - what the files you pulled down are made of
