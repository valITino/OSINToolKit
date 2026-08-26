---
name: oletools
slug: oletools
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/decalage2/oletools
categories: [documents-metadata, office-forensics]
tags: [ole, macros, office, doc, metadata]
status: unverified
status_checked: 2026-08-26
---

# oletools

## What question does it answer?
What is inside this Office document - who authored it, what macros does it carry, and
what is embedded in its OLE streams?

## When to reach for it
For legacy binary Office formats (`.doc`, `.xls`, `.ppt`) and for any Office file with
macros. Modern `.docx` files are just ZIP archives you can unzip
(see [../README.md](../README.md)), but the older OLE compound format needs real
tooling - and that is where oletools earns its place. `olevba` is the standard way to
see what a macro does without running it.

## Install
```bash
pipx install oletools
```

## Usage
```bash
oleid suspicious.doc          # triage: macros, encryption, embedded objects, flags
olemeta suspicious.doc         # document metadata: author, company, timestamps
olevba suspicious.doc           # extract and analyse VBA macro source
oledump.py suspicious.doc       # enumerate OLE streams for manual inspection
```

## Output
`oleid` gives a risk-flag summary; `olemeta` gives authorship and timestamp fields;
`olevba` prints the macro source plus a table of suspicious keywords it noticed.
Author, company, and last-saved-by fields are the attribution payload.

## Gotchas
- **Never open the document to inspect it - that is the whole point of these tools.**
  Analyse statically, in a VM ([OPSEC](../../00-methodology/opsec/README.md)).
- `olevba`'s keyword flags are heuristics; a flagged document is not automatically
  malicious and a clean one is not automatically safe.
- Macros can be obfuscated or stored in unusual streams - a clean `olevba` on a
  suspicious file warrants `oledump.py` and a manual look.
- Reverse-engineering malicious payloads is out of scope here; record what is present
  and hand it to malware analysis.

## Alternatives
- [ExifTool](../metadata-extraction/exiftool.md) - metadata across all Office formats
- [binwalk](../pdf-forensics/binwalk.md) - embedded content in any container
- [../README.md](../README.md) - the unzip technique for modern .docx
