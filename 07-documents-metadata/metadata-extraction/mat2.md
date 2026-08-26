---
name: mat2
slug: mat2
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://0xacab.org/jvoisin/mat2
categories: [documents-metadata, metadata-extraction]
tags: [anonymisation, metadata-removal, opsec, publishing]
status: unverified
status_checked: 2026-08-26
---

# mat2

## What question does it answer?
I am about to publish or hand over a file. What metadata would leak with it, and how
do I remove it without corrupting the document?

## When to reach for it
The defensive counterpart to [ExifTool](exiftool.md). Two uses in an investigation:
sanitising files you are about to release (a report, an exhibit, a screenshot), and
understanding what a subject's "cleaned" file has been through. mat2 is built for
this specific job - it works format-by-format and errs toward removing too much
rather than too little, which is the right bias when the alternative is deanonymising
a source.

## Install
```bash
sudo apt install mat2       # Kali/Debian
```

## Usage
```bash
mat2 --show document.pdf         # list the metadata without changing anything
mat2 document.pdf                 # write a cleaned document.cleaned.pdf, original untouched
mat2 --inplace photo.jpg          # clean in place
mat2 --list                       # supported formats
```

## Output
`--show` prints the metadata it found. A clean run writes a new `.cleaned` file
alongside the original by default, which is the safe behaviour - your evidence copy
stays intact.

## Gotchas
- Cleaning **rewrites the file**, changing its hash. Never clean a file that is
  evidence; work on copies and record the original hash first
  ([documentation](../../00-methodology/documentation/README.md)).
- Removal is not guaranteed complete for every format - some containers can hide data
  in ways no tool reliably strips. Verify with `exiftool -a -u -g1` afterwards.
- Cleaning cannot remove content *inside* the document: redaction is a separate
  problem, and black rectangles over text are not redaction.
- Investigative point: a file processed with a metadata stripper is itself a signal
  about the sender's sophistication.

## Alternatives
- [ExifTool](exiftool.md) - reads everything, and can also write/strip tags
- [qpdf](../pdf-forensics/qpdf.md) - PDF structure, including what was left behind
