---
name: yt-dlp
slug: yt-dlp
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/yt-dlp/yt-dlp
categories: [web-exploration, scraping]
tags: [video, media-preservation, metadata, subtitles, comments]
status: active
status_checked: 2026-08-29
---

# yt-dlp

## What question does it answer?
I have a video URL that may be deleted, edited or made private. How do I
preserve it and everything around it - channel ID, upload date, description,
thumbnails, subtitles, comments - with a record of what I took?

## When to reach for it
Whenever the artefact is hosted media. Even when you do not want the bytes,
`--skip-download` makes it the fastest way to snapshot a platform's own claims
about an upload. It is not a general scraper: for page text use
[trafilatura](trafilatura.md), for site structure [HTTrack Website Copier](httrack.md),
and for image galleries it reaches almost nothing. Coverage is per-extractor, so
an unsupported site falls back to generic extraction that grabs the wrong
element, or nothing.

## Install
```bash
python3 -m pip install -U "yt-dlp[default]"   # Python 3.10+; or the standalone binary
sudo apt install ffmpeg   # "highly recommended": required to merge separate A/V streams
```

## Usage
```bash
yt-dlp --skip-download --write-info-json --no-clean-info-json --write-comments \
  --write-thumbnail --write-description --write-subs --write-auto-subs "<URL>"
# metadata-first capture: the whole evidentiary envelope, none of the video bytes
yt-dlp -J "<URL>" > case-001.json
# one JSON blob to stdout, nothing written: uploader, upload_date, timestamp, counts
yt-dlp -F "<URL>"   # list every format, so you can state which rendition you preserved
yt-dlp --download-archive archive.txt --write-info-json "<CHANNEL-URL>"
# monitoring over time: the archive file means re-runs only pull what is new
```

## Output
Files named by the output template: the media, a sidecar `.info.json`, a
`.description`, a thumbnail, and `.vtt`/`.srt` subtitles. The `.info.json` is
the real artefact - id, title, uploader, uploader_id, channel_id, upload_date,
timestamp, duration, counts, full description, the formats array, and with
`--write-comments` an array carrying per-comment author, author_id, timestamp
and parent id. Read `upload_date`/`timestamp` as the platform's claim, keep your
own capture time separately, and cross-check `channel_id` rather than the
display name - names change, IDs do not.

## Gotchas
- **YouTube demands PO Tokens on most clients.** Per the project's own guide
  they are needed for streaming on web, mweb, android, ios and more, and without
  one requests may return HTTP 403 "or result in your account or IP address
  being blocked". Tokens now bind to single video IDs, so manual extraction is
  impractical and the answer is a PO Token Provider plugin.
- **Your distro's package is almost certainly broken.** Extractors are patched
  daily. Run `yt-dlp -U` immediately before a capture and record the version.
- **`--clean-info-json` is the default** and silently drops internal metadata.
  Pass `--no-clean-info-json` or you are archiving a redacted record.
- **`--cookies-from-browser` sends your logged-in identity.** The platform sees
  an authenticated account, that account carries the terms-of-service exposure,
  and the capture is attributable to you. Never use an account tied to your real
  identity on work you need to be deniable.
- **The help text warns the info JSON "may contain personal information".**
  Comment arrays hold names, IDs and timestamps for third parties who are not
  your subject, and are sometimes fetched even without the flag - see
  [../../LEGAL.md](../../LEGAL.md).
- It is not chain of custody by itself: hash the media and the `.info.json` at
  capture time, and record your wall-clock time next to the platform's.

## Alternatives
- [Playwright](playwright.md) - capture the page around the video, and its network log
- [HTTrack Website Copier](httrack.md) - the surrounding site as a mirror plus WARC
- [snscrape](snscrape.md) - post text rather than media, but see why it is tier 3
