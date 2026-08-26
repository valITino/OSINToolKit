---
name: pdf-parser.py
slug: pdf-parser
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://blog.didierstevens.com/programs/pdf-tools/
categories: [documents-metadata, pdf-forensics]
tags: [pdf, objects, structure, revisions]
status: unverified
status_checked: 2026-08-26
---

# pdf-parser.py

## What question does it answer?
What is actually inside this PDF at the object level - embedded files, JavaScript,
previous revisions, and content the viewer does not show me?

## When to reach for it
When the rendered page is not the whole story. A PDF is a collection of objects, and
plenty of them never appear on screen: superseded text from an earlier revision,
embedded attachments, hidden layers. pdf-parser walks that structure directly, which
is how you find the paragraph someone "removed" before publishing. Start with
[ExifTool](../metadata-extraction/exiftool.md) for metadata, then come here for
structure.

## Install
```bash
# Download pdf-parser.py from blog.didierstevens.com/programs/pdf-tools/
python3 pdf-parser.py --help          # Kali packages it as pdf-parser
```

## Usage
```bash
python3 pdf-parser.py -a document.pdf              # statistics: object types and counts
python3 pdf-parser.py -s JavaScript document.pdf    # search for objects by keyword
python3 pdf-parser.py -o 12 -d out.bin document.pdf # dump object 12's raw content
python3 pdf-parser.py -f document.pdf               # decode stream filters where possible
```

## Output
Object listings with type, references, and stream contents. The statistics view is the
triage step: an unexpected `/JavaScript`, `/EmbeddedFile`, or `/OpenAction` is worth
a look, and object counts that exceed what a simple document needs suggest revisions.

## Gotchas
- Reading a malicious PDF's structure is far safer than opening it in a viewer - but
  do it in a VM anyway ([OPSEC](../../00-methodology/opsec/README.md)), and never
  execute anything you extract.
- Object numbers repeat across incremental updates; that duplication is the signal.
  Cross-check with [`qpdf --show-xref`](qpdf.md).
- Deeply corrupted or heavily obfuscated PDFs may need `--raw` or manual work.
- Analysing embedded JavaScript to find exploits is out of scope here; note its
  presence and move on.

## Alternatives
- [qpdf](qpdf.md) - cross-reference table and incremental-update detection
- [pdfimages](pdfimages.md) - pull the embedded images out
- [binwalk](binwalk.md) - find files embedded in any container
