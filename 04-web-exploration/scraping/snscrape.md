---
name: snscrape
slug: snscrape
tier: 3
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/JustAnotherArchivist/snscrape
categories: [web-exploration, scraping]
tags: [social-media, twitter, telegram, abandoned, legacy]
status: broken
status_checked: 2026-08-29
---

# snscrape

## What question does it answer?
I have a handle or a channel name and no API key. Can I still pull that
account's posts - and, more often now, is a dataset that claims snscrape as its
source actually credible?

## Why this is tier 3
Abandoned since June 2023 and broken for the thing it was famous for. Tested
today, module by module: every `twitter-*` scraper raises `ScraperException`
against a hardcoded 2023 GraphQL hash on twitter.com; the `reddit-*` modules
call the defunct public `api.pushshift.io`; `mastodon-profile` crashes with
`AttributeError` on markup that has since changed; `instagram-user` returned
429. Only `telegram-channel` still returned data. No free drop-in replacement
exists: for X, the paid API or an authenticated browser session driven by
[playwright.md](playwright.md); for Reddit, the official API via PRAW or a
PullPush-style mirror; for Mastodon and Bluesky, each instance's own open API,
which needs no scraping; for Telegram, this tool or Telethon. It stays here for
recognition - it is cited in thousands of papers, and results attributed to it
after mid-2023 do not add up.

## When to reach for it
Two honest uses: collecting from a public Telegram channel, where the module
still works, and reproducing a failure on demand to show a client or an editor
that a cited dataset could not have been gathered the way it claims. For
anything else start from the
[social-media directory](../../08-people-and-identity/social-media/README.md) or
from [an archived copy](../../06-history-and-archives/web-archive/README.md).

## Install
```bash
pip3 install snscrape   # installs cleanly: verified today, Python 3.11.15, 0.7.0.20230622
# The README's git+https dev install is the same code - master's last commit is 2023-06-22
```

## Usage
```bash
snscrape --version   # 0.7.0.20230622 is the last-ever release, not a maintained build
snscrape --jsonl --max-results 100 telegram-channel <channel>
# the one module verified working today; --with-entity emits the channel object first
snscrape -vv --retry 0 --with-entity twitter-user <handle>
# the canonical historical command, now dead: -vv --retry 0 prints the failing URL at once
```

## Output
One URL per line by default; `--jsonl` gives one JSON object per item (for
Telegram: url, date, content, outlinks, media, forwarding metadata). In practice
most modules now emit a traceback on stderr and nothing on stdout, and the
traceback is the finding. A `ScraperException` naming twitter.com or
api.pushshift.io means the module is structurally dead, not throttled; an
`AttributeError` means the HTML moved under an unmaintained parser; a 429 is the
platform refusing an unauthenticated scraper.

## Gotchas
- **Datasets in the wild are dated.** Any snscrape-derived Twitter corpus stops
  around mid-2023. A report citing it for later tweets is a finding in itself.
- **Retrying will not help.** No proxy, delay or IP rotation fixes a hardcoded
  2023 endpoint. The Reddit failure is the same class, different cause.
- **Mastodon fails as a bare `AttributeError`**, which reads like a bug in your
  wrapper rather than a dead scraper. Test each module standalone.
- **The repo is not archived**, so GitHub still presents a live-looking project
  whose README lists eight working networks. Only the commit dates say otherwise.
- **No key and no account means no ToS gate**, which is why the exposure for
  automated collection against a platform's terms, and for the personal data you
  end up holding, is yours personally - see [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [playwright.md](playwright.md) - an authenticated browser session, with the account risk
- [yt-dlp.md](yt-dlp.md) - platform media and its metadata envelope, still maintained
- [Web archives](../../06-history-and-archives/web-archive/README.md) - archived profile pages, no contact
