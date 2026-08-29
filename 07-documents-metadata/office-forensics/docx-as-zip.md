---
name: DOCX as ZIP
slug: docx-as-zip
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://ecma-international.org/publications-and-standards/standards/ecma-376/
categories: [documents-metadata, office-forensics]
tags: [ooxml, docx, zip, metadata, technique]
status: active
status_checked: 2026-08-26
---

# DOCX as ZIP

## What question does it answer?
I have a modern Office file and no forensics tooling. Who wrote it, on what
software, how long did they spend on it, and what does it reach out to?

## When to reach for it
When you want ground truth rather than a tool's interpretation of it. `.docx`,
`.xlsx`, and `.pptx` are ZIP archives of XML parts (OOXML, standardised as
ECMA-376), so `unzip` and a text editor read them with nothing installed. Reach for
this to confirm what [ExifTool](../metadata-extraction/exiftool.md) reported, to see
fields a parser skipped, or on a machine where you cannot install anything.

Use [oletools](oletools.md) instead for legacy `.doc`/`.xls`/`.ppt` - those are OLE
compound files, not ZIPs, and none of this applies.

## Install
```bash
sudo apt install unzip libxml2-utils    # unzip plus xmllint for readable formatting
```

## Usage
```bash
unzip -l suspect.docx                                    # list parts; note the ZIP timestamps
unzip -p suspect.docx docProps/core.xml | xmllint --format -   # author, editor, revision, dates
unzip -p suspect.docx docProps/app.xml  | xmllint --format -   # application, template, edit time
unzip -p suspect.docx word/_rels/document.xml.rels | grep 'TargetMode="External"'   # outbound links
```

## Output
`docProps/core.xml` holds `dc:creator` (original author), `cp:lastModifiedBy` (who
saved it last - often a different person), `cp:revision` (save count), and
`dcterms:created` / `dcterms:modified`.

`docProps/app.xml` is the richer one: `Application` names the exact product
(`Microsoft Macintosh Word` gives away the operating system), `AppVersion` its
version, `Template` the `.dotm` it was built from, `TotalTime` the accumulated
editing minutes, and `Company` / `Manager` are frequently left populated.

`word/_rels/document.xml.rels` lists every relationship. Entries with
`TargetMode="External"` are the ones that matter: remote images, hyperlinks, and
linked templates that cause the document to call out when opened.

## Gotchas
- **ZIP entry timestamps and the XML dates are independent and often disagree.** In one
  sample checked for this entry the ZIP entries read 2019 while `dcterms:created` read
  2013. Neither is authoritative; both are trivially forgeable. Report the discrepancy,
  do not resolve it.
- Every field here is user-supplied and editable. A name in `dc:creator` is a lead,
  not an identification.
- `TotalTime` is Word's own accumulated edit counter. A value of 0 or 1 on a long
  document suggests the content was pasted in or the file was generated, not typed.
- Files produced by LibreOffice, Google Docs export, or a library like python-docx
  carry that tool's fingerprint and populate far fewer fields.
- Unzipping is safe; **opening the document is not**. Extract embedded objects to an
  isolated directory and never let an external relationship resolve.

## Alternatives
- [oletools](oletools.md) - required for legacy OLE formats and for macros
- [ExifTool](../metadata-extraction/exiftool.md) - the same fields parsed for you, one command
- [mat2](../metadata-extraction/mat2.md) - the reverse: strip this before you publish
