---
name: TinEye
slug: tineye
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://tineye.com/
categories: [people-and-identity, reverse-image]
tags: [reverse-image, provenance, first-seen, exact-match]
status: unverified
status_checked: 2026-08-26
---

# TinEye

## What question does it answer?
Where did this exact image first appear, and how has it been used and modified since?

## When to reach for it
For **provenance**, which is a different question from similarity. TinEye matches the
image itself rather than its subject, and it can sort results by oldest first - which
is how you establish that a photo presented as new was published years earlier, or
find the original before it was cropped and recaptioned. That makes it the tool for
debunking recycled imagery. For finding a *different* photo of the same person, use
[Yandex](yandex-images.md).

## Install
```bash
# Nothing to install - web only. Browser extensions exist for right-click searching.
```

## Usage
```text
https://tineye.com/     # upload the file or paste an image URL
# Sort results by "Oldest" to find the earliest known appearance.
```

## Output
Pages hosting matching images, with the match count, image dimensions, and the crawl
date. The comparison view shows how a result differs from your input - crops, edits,
and overlays become obvious.

## Gotchas
- It finds **the same image**, not the same subject. A different photograph of the same
  person will not match - that is a limitation, not a failure.
- "Oldest result" is the oldest **TinEye crawled**, not the true origin. It is strong
  evidence of prior existence, not proof of first publication.
- Free use is rate-limited; heavy or automated use needs a paid API.
- An image that appears nowhere is meaningful too - it may be original, private, or
  recently created.

## Alternatives
- [Yandex Images](yandex-images.md) - similarity and faces
- [Google Lens](google-lens.md) - objects, landmarks and text rather than exact copies
- [Wayback CDX](../../06-history-and-archives/web-archive/wayback-cdx-api.md) - confirm when a page carrying the image existed
