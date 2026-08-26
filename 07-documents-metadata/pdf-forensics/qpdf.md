---
name: qpdf
slug: qpdf
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://qpdf.sourceforge.io/
categories: [documents-metadata, pdf-forensics]
tags: [pdf, xref, incremental-update, structure]
status: unverified
status_checked: 2026-08-26
---

# qpdf

## What question does it answer?
Has this PDF been edited after it was first saved - and if so, is the earlier version
still recoverable from inside the file?

## When to reach for it
This is the incremental-update question, and it is one of the highest-value checks in
document forensics. PDFs can be modified by **appending** changes rather than
rewriting the file, which leaves the original content physically present but
unreferenced. A redacted or corrected paragraph frequently still sits in the bytes.
qpdf exposes the cross-reference structure that reveals it.

## Install
```bash
sudo apt install qpdf        # Kali/Debian; brew install qpdf on macOS
```

## Usage
```bash
qpdf --show-xref document.pdf                       # the cross-reference table - read this first
qpdf --qdf --object-streams=disable document.pdf readable.pdf   # uncompressed, human-readable copy
qpdf --check document.pdf                            # structural problems and warnings
```

## Output
`--show-xref` lists every object with its generation and byte offset. `--qdf` writes a
decompressed, normalised copy you can open in a text editor to read object contents
directly.

## Gotchas
- **Duplicate object IDs at different offsets, or non-sequential offsets, indicate an
  incremental update with recoverable hidden content.** That is the tell. Follow it up
  by extracting the older object with
  [pdf-parser.py](pdf-parser.md) or reading the `--qdf` output.
- qpdf can rewrite PDFs; every write changes the hash. Work on copies and never
  overwrite evidence.
- `--check` warnings are common in valid PDFs from sloppy generators - a warning alone
  is not evidence of tampering.
- Content genuinely removed by a proper redaction workflow will not be recoverable.

## Alternatives
- [pdf-parser.py](pdf-parser.md) - dump the specific objects you identified here
- [ExifTool](../metadata-extraction/exiftool.md) - the document's metadata and timestamps
