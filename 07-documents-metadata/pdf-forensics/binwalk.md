---
name: binwalk
slug: binwalk
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/ReFirmLabs/binwalk
categories: [documents-metadata, pdf-forensics]
tags: [embedded-files, carving, signatures, firmware]
status: unverified
status_checked: 2026-08-26
---

# binwalk

## What question does it answer?
Is there another file hidden inside this one - an archive, an image, or a document
appended to or embedded in the container I am looking at?

## When to reach for it
When a file is bigger than it should be, or when you suspect something is concealed
inside it. binwalk scans for known file signatures anywhere in a byte stream, so it
finds content that the parent format's own tools ignore: a ZIP appended to a JPEG, a
document embedded in a PDF, files inside firmware. It is format-agnostic, which is
exactly why it catches what format-specific tools miss.

## Install
```bash
sudo apt install binwalk      # Kali default
```

## Usage
```bash
binwalk document.pdf                     # signature scan: what is in there and at what offset
binwalk -e suspicious.bin                 # extract what it recognises
binwalk -E firmware.bin                   # entropy graph: flat high entropy = encrypted/compressed
strings -n 8 document.pdf | less          # the crude complement, still useful
```

## Output
A table of offset, hexadecimal offset, and the signature description. `-e` writes
extracted content to a `_filename.extracted/` directory.

## Gotchas
- **Signature matching produces false positives** - short magic bytes occur by chance
  in compressed data. Treat a hit as a lead and confirm the extracted bytes are really
  that format.
- **Extraction runs parsers over untrusted input.** Do it in a VM, never on your host
  ([OPSEC](../../00-methodology/opsec/README.md)).
- Extraction depends on external helper utilities being installed; a missing helper
  means silently skipped content.
- The project was rewritten (v3 in Rust) - flags and behaviour differ from older
  write-ups, so check `binwalk --help` for your version.

## Alternatives
- [pdf-parser.py](pdf-parser.md) - structured extraction from PDFs specifically
- [oletools](../office-forensics/oletools.md) - embedded objects in Office documents
- [ExifTool](../metadata-extraction/exiftool.md) - often reports embedded content too
