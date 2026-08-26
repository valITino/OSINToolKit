---
name: pdfimages
slug: pdfimages
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://poppler.freedesktop.org/
categories: [documents-metadata, pdf-forensics]
tags: [pdf, images, extraction, exif]
status: unverified
status_checked: 2026-08-26
---

# pdfimages

## What question does it answer?
What images are embedded in this PDF, and what metadata do **they** carry - camera,
GPS, timestamps - that the PDF itself does not?

## When to reach for it
When a document contains photographs or scans. The embedded image is often the richer
evidence: a PDF report may carry no useful metadata while a photo pasted into page
four still holds the camera model and GPS coordinates from the phone that took it.
Extract the images, then run [ExifTool](../metadata-extraction/exiftool.md) over the
results.

## Install
```bash
sudo apt install poppler-utils      # provides pdfimages, pdftotext, pdfinfo
```

## Usage
```bash
mkdir out && pdfimages -all document.pdf out/img       # extract in original formats
pdfimages -list document.pdf                            # inventory before extracting
exiftool -a -u -g1 out/*                                # then read their metadata
```

## Output
One file per embedded image, named with your prefix and an index. `-list` prints an
inventory: page, dimensions, colour space, compression, and size - useful for spotting
an unexpectedly high-resolution image.

## Gotchas
- **Always pass `-all`.** Without it, pdfimages re-encodes images to PPM/PBM, which
  **strips the EXIF data you came for.** `-all` preserves the original embedded stream
  (JPEG stays JPEG), keeping metadata intact. This single flag is the difference
  between finding GPS coordinates and finding nothing.
- Images may be split into tiles or masked; what you extract can look different from
  what the page renders.
- Scanned pages are images - extract and consider OCR if the text matters.

## Alternatives
- [pdf-parser.py](pdf-parser.md) - object-level extraction of anything, not just images
- [binwalk](binwalk.md) - embedded files in arbitrary containers
- [ExifTool](../metadata-extraction/exiftool.md) - the next step after extraction
