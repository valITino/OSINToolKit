---
name: ExifTool
slug: exiftool
tier: 1
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://exiftool.org/
categories: [documents-metadata, metadata-extraction]
tags: [metadata, exif, gps, formats]
status: unverified
status_checked: 2026-08-26
---

# ExifTool

## What question does it answer?
I have a file - a photo, a PDF, a Word doc, almost anything. What metadata is
inside it: who made it, with what, when, and where?

## When to reach for it
Always, first, for any file. ExifTool reads (and writes) metadata across hundreds
of formats and is the reference implementation - if a field exists, it reads it.
It is the starting point before format-specific forensics like
[pdf-parser.py](../pdf-forensics/pdf-parser.md) or
[oletools](../office-forensics/oletools.md).

## Install
```bash
sudo apt install libimage-exiftool-perl     # Kali/Debian
brew install exiftool                        # macOS
```

## Usage
```bash
exiftool photo.jpg                           # all tags, human-readable
exiftool -a -u -g1 report.pdf                # all tags incl. duplicates/unknown, grouped
exiftool -gps:all -n image.jpg               # GPS coordinates as raw decimals
exiftool -time:all -a -G0:1 file.docx         # every timestamp with its group
```

## Output
Tag/value pairs. `-g1` groups by category (EXIF, XMP, PDF, ICC). GPS tags give
lat/long you can drop into a map; timestamps often reveal timezone and device;
producer/creator tags can tie a document to software or an author.

## Gotchas
- Absence of metadata is itself a finding - social platforms and "clean" exports
  strip it (see [mat2](mat2.md) for how). Do not conclude "no camera" from a
  scrubbed file.
- Timestamps can be local or UTC depending on the field; note the group and do not
  assume a timezone.
- Writing tags (`-TAG=value`) modifies the file; work on a copy and keep the
  original for chain of custody.

## Alternatives
- [mat2](mat2.md) - the inverse: strip metadata safely
- [pdf-parser.py](../pdf-forensics/pdf-parser.md) - PDF structure beyond metadata
- [exiv2](exiv2.md) - images only, but it extracts embedded previews
- [oletools](../office-forensics/oletools.md) - legacy Office internals
