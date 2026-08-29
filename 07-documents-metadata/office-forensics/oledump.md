---
name: oledump.py
slug: oledump
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://blog.didierstevens.com/programs/oledump-py/
categories: [documents-metadata, office-forensics]
tags: [ole, streams, vba, yara, malware-handling]
status: active
status_checked: 2026-08-26
---

# oledump.py

## What question does it answer?
What is actually stored inside this OLE file, stream by stream - and can I look at a
hostile sample without ever unpacking it onto my disk?

## When to reach for it
Two situations. First, when you want the **container** rather than a parsed summary:
oledump lists every stream with its size and lets you dump any one of them, so you see
embedded objects and odd streams that a macro-focused tool skips over. Second - and
this is the reason to keep it around - it reads samples **directly out of a
password-protected ZIP**, so a suspicious document can stay zipped with the usual
`infected` password while you work on it.

[oletools](oletools.md) is the friendlier first pass and its `olevba` gives a better
macro report. Reach for oledump when that report is not enough, or when handling
hygiene matters.

## Install
```bash
# Standalone Python script - download and unzip, no package manager involved.
curl -O https://didierstevens.com/files/software/oledump_V0_0_85.zip
unzip oledump_V0_0_85.zip && python3 oledump.py -m     # -m prints the built-in manual
```

## Usage
```bash
python3 oledump.py suspect.doc                  # list streams; 'M' marks one holding VBA
python3 oledump.py -s 8 -v suspect.doc          # dump stream 8, decompressing the VBA
python3 oledump.py -s 3 -S suspect.doc          # strings from one stream
python3 oledump.py -y maldoc.yara suspect.doc   # scan every stream with YARA rules
```

## Output
One line per stream: index, indicator letters, size, and name. `M` means the stream
contains VBA macros and `O` an OLE object - that index is what you then pass to `-s`.
Add `-c` for hashes of each stream, `-M` for the document metadata, and `-i` for extra
detail on a selected item. `-e` extracts an embedded file rather than printing it.

## Gotchas
- **OLE only.** `.doc`, `.xls`, `.ppt` and other Compound File Binary Format containers.
  Modern `.docx`/`.xlsx` are ZIPs of XML - use
  [docx as ZIP](docx-as-zip.md) or [oletools](oletools.md) for those.
- **VBA source is compressed inside the stream.** Without `-v` you get binary noise and
  may wrongly conclude there is nothing there.
- This is analysis tooling for hostile documents. Read macros, never run them, and work
  in a VM. Documenting or building the payloads themselves is out of scope for this
  reference.
- `-y` needs the `yara-python` module installed separately, and YARA scanning does not
  combine with `-s`.
- It is a single script from a personal site with no package or signature. Check the
  version on the author's page before trusting a copy you already had.

## Alternatives
- [oletools](oletools.md) - `olevba`/`oleid` triage; start here
- [docx as ZIP](docx-as-zip.md) - the modern OOXML equivalent, no tooling needed
- [binwalk](../pdf-forensics/binwalk.md) - when you suspect something appended rather than embedded
