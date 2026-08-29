---
name: exiv2
slug: exiv2
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://exiv2.org/
categories: [documents-metadata, metadata-extraction]
tags: [exif, iptc, xmp, previews, images]
status: active
status_checked: 2026-08-26
---

# exiv2

## What question does it answer?
I have an image. What Exif, IPTC and XMP does it carry - and is there an embedded
preview that still shows the frame **before** it was cropped or edited?

## When to reach for it
For the preview extraction, mostly. Cameras and editors store a full JPEG preview and a
thumbnail alongside the main image, and those are frequently **not** regenerated when
someone crops, redacts, or adjusts the picture. Pulling them out can hand you the
original composition. exiv2 lists and extracts them in one command, which is its real
advantage over reaching for [ExifTool](exiftool.md) reflexively.

It is also the metadata library that digiKam, GIMP and much of the KDE stack embed, so
it is often already installed, and it is fast enough to run across a directory of
thousands of images.

## Install
```bash
sudo apt install exiv2      # Debian/Kali
brew install exiv2          # macOS
```

## Usage
```bash
exiv2 photo.jpg                       # default: summary of the Exif
exiv2 -p a photo.jpg                  # all Exif, IPTC and XMP tags
exiv2 -p p photo.jpg                  # list embedded previews, largest first
exiv2 -ep photo.jpg                   # extract those previews to files
exiv2 -p a --grep gps/i photo.jpg     # just the location tags, case-insensitive
```

## Output
`-p s` gives a short human summary; `-p a` the full tag list as key, type, value.
`-p p` lists each preview with its pixel dimensions, and `-ep` writes them out as
`photo-preview1.jpg` and so on. `-p S` shows the file's internal structure, `-p C`
dumps the ICC colour profile, and `-p h` gives a hex dump when you suspect the tags
themselves have been tampered with.

## Gotchas
- **Images only.** exiv2 handles JPEG, TIFF, PNG, WebP, HEIC/HEIF, JXL, PSD, and the
  RAW formats (CR2, CR3, NEF, ARW, ORF, RAF, DNG...). It does **not** read PDFs or
  Office documents - for those use [ExifTool](exiftool.md) or
  [docx as ZIP](../office-forensics/docx-as-zip.md).
- GIF, BMP and TGA are recognised but essentially unsupported - you get dimensions and
  nothing else.
- **`--grep` is case-sensitive; append `/i` for case-insensitive** (`--grep gps/i`).
  Do not reach for a `-i` flag to do it: `-i` is exiv2's *insert* action, and
  `--grep -i gps` silently consumes `-i` as the pattern and then treats `gps` as a
  filename - "gps: Failed to open the file".
- **GPS in Exif is what the camera recorded, not proof of where the photographer was.**
  Phones cache locations, and the tag is trivially editable.
- Beware the write actions. `rm`, `mo`, `ad` and `mv` modify files in place, and `mv`
  renames from the Exif timestamp. Work on copies - altering an evidential file
  destroys its integrity.
- Absence of metadata means little on its own: every social platform strips Exif on
  upload, so a bare image may simply have been posted somewhere.

## Alternatives
- [ExifTool](exiftool.md) - far broader format coverage; the default first move on any file
- [mat2](mat2.md) - the reverse: strip metadata before you publish
- [pdfimages](../pdf-forensics/pdfimages.md) - pull the images out of a PDF, then run this on them
