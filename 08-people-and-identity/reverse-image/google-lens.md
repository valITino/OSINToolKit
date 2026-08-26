---
name: Google Lens
slug: google-lens
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://lens.google.com/
categories: [people-and-identity, reverse-image]
tags: [reverse-image, visual-similarity, ocr, geolocation]
status: active
status_checked: 2026-08-26
---

# Google Lens

## What question does it answer?
What is actually **in** this photo - the building, the sign, the product - and where else
does this scene appear?

## When to reach for it
When the image has not been republished anywhere, so an exact-match search fails.
[TinEye](tineye.md) finds copies of the same file; Lens matches *semantically* - it
recognises objects, landmarks, plants, products, and text, and surfaces visually similar
scenes rather than identical bytes. For a photo taken by your subject and never posted
elsewhere, that is the difference between no result and a lead.

Two specific strengths for investigation: it reads text out of images, so a sign,
receipt, or screenshot becomes searchable; and its landmark recognition is often the
fastest first guess when geolocating a photo. Follow up in
[geo-media](../../07-documents-metadata/geo-media/README.md).

## Install
```bash
# Nothing to install - web only.
```

## Usage
```text
https://lens.google.com/            # upload a file or paste an image URL
https://images.google.com/           # "Search by image" leads to the same engine
Chrome: right-click any image -> "Search with Google Lens"
```

## Output
Visually similar images and the pages carrying them, plus recognised objects, extracted
text, and - where it is confident - a named landmark, product, or species. Results are
ranked by visual similarity, not by first appearance.

## Gotchas
- **"Visually similar" is a much weaker claim than "the same image".** Lens will happily
  return a different building of the same style. For provenance - who published this
  first - use [TinEye](tineye.md), which sorts by oldest.
- **Results are not reproducible.** They vary by account, location, language, and over
  time, so a colleague may not see what you saw. Screenshot and timestamp anything you
  intend to rely on - see
  [../../00-methodology/documentation/README.md](../../00-methodology/documentation/README.md).
- **There is no public API** for the consumer product. Anything claiming to offer one is
  scraping, and will break.
- **Uploading an image sends it to Google.** For a photograph of a private individual, or
  a document from a case file, that is a disclosure decision, not a search. Consider
  cropping to the object of interest first.
- Deliberately weak on faces: Lens will not identify people, by design. Do not read its
  silence there as an absence of matches.
- Crop before you search. A tight crop on one distinctive element beats the whole frame,
  which tends to match on background and lighting instead.

## Alternatives
- [TinEye](tineye.md) - exact and near-duplicate matching, sortable by oldest
- [Yandex Images](yandex-images.md) - historically the strongest at faces and places
- [ExifTool](../../07-documents-metadata/metadata-extraction/exiftool.md) - read the file's own metadata first
