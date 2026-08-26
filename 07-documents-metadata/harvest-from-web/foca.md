---
name: FOCA
slug: foca
tier: 3
contact: passive
type: gui
cost: free
platforms: [windows]
url: https://github.com/ElevenPaths/FOCA
categories: [documents-metadata, harvest-from-web]
tags: [documents, metadata, windows, gui, legacy]
status: unverified
status_checked: 2026-08-26
---

# FOCA

## What question does it answer?
What documents has this organisation published, and what does their metadata reveal
about its internal network - usernames, servers, folder paths, software versions?

## Why this is tier 3
FOCA does the [metagoofil](metagoofil.md) job with a GUI and a genuinely good
network-inference feature: it aggregates metadata across many documents to sketch the
organisation's internal structure. Two things keep it at tier 3: it is **Windows-only
with a .NET GUI**, which does not fit a Linux investigation workflow or any automated
pipeline, and its development has been slow, so the same search-engine scraping
fragility that broke metagoofil applies.

Worth knowing about, and genuinely nice when you are already on Windows and have a
document-heavy target.

## Install
```text
Windows only. Build from the ElevenPaths GitHub repository or use a released binary.
```

## Usage
```text
1. Create a project and set the target domain.
2. Search for documents by extension via the configured search engines.
3. Download them, then run metadata extraction.
4. Review the aggregated users, folders, software, and inferred servers.
```

## Output
A document inventory with per-file metadata, plus aggregated views: discovered
usernames, printers, folder paths, software versions, and an inferred network diagram.

## Gotchas
- **Windows-only**, GUI-driven, not scriptable - the practical blocker for most
  workflows.
- Search-engine harvesting is fragile for the same reasons metagoofil fails; the
  download stage may return little.
- Aggregated "internal network" inferences are **guesses from metadata**, not
  observed facts. Corroborate before reporting them.

## Alternatives
- [ExifTool](../metadata-extraction/exiftool.md) - the extraction itself, done properly, on any platform
- [Dorking](../../04-web-exploration/dorking/README.md) + `wget` + ExifTool - the portable manual pipeline
