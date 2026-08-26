---
name: Yandex Images
slug: yandex-images
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://yandex.com/images/
categories: [people-and-identity, reverse-image]
tags: [reverse-image, faces, geolocation, similarity]
status: unverified
status_checked: 2026-08-26
---

# Yandex Images

## What question does it answer?
I have a photo. Where else does this image - or a visually similar one, or this
person's face - appear online?

## When to reach for it
First, for anything involving **faces or places**. Yandex's reverse image search is
widely regarded as the strongest at visual similarity rather than exact-copy matching,
which is precisely what you need when the same person appears in a different photo, or
when you are trying to identify a building or street. [TinEye](tineye.md) is better for
finding exact reuse and first-appearance dates; Google Lens sits between the two.

## Install
```bash
# Nothing to install - web only.
```

## Usage
```text
https://yandex.com/images/     # use the camera icon to upload a file or paste a URL
```

If the full frame returns nothing useful, **crop and retry**: isolate the face, the
sign, the logo, or the building. Cropping to the distinctive element is the single
most effective technique in reverse image search, and it frequently turns a dead
search into a hit.

## Output
Visually similar images with the pages hosting them, plus Yandex's guess at the
subject and, often, sites with the same image at other resolutions.

## Gotchas
- **Similar is not identical.** A visual match is a lead requiring corroboration -
  never assert identity from a reverse image hit alone.
- Uploading an image sends it to a third party. Do not upload sensitive, victim, or
  client images ([OPSEC](../../00-methodology/opsec/README.md)); consider whether a
  crop is enough.
- Run several engines - each indexes different corners of the web, and Yandex, TinEye,
  Google Lens, and Bing routinely disagree.
- Check the file's own metadata with
  [ExifTool](../../07-documents-metadata/metadata-extraction/exiftool.md) **before**
  uploading anywhere - it may answer the question outright.

## Alternatives
- [TinEye](tineye.md) - exact matches, oldest-first, good for provenance
- [../../07-documents-metadata/geo-media/README.md](../../07-documents-metadata/geo-media/README.md) - placing an image from its content
