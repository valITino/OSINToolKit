---
name: wig
slug: wig
tier: 3
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/jekyc/wig
categories: [web-exploration, fingerprinting]
tags: [fingerprinting, legacy, cms-detection]
status: stale
status_checked: 2026-08-26
---

# wig

## What question does it answer?
What CMS and web platform is this site running, guessed from static file checksums
and page markers?

## Why this is tier 3
The project has seen little maintenance for years and **needs a source patch to run
on modern Python at all** (see Gotchas). Its fingerprint database has aged, so it
misses current CMS versions that [WhatWeb](whatweb.md) and [CMSeeK](../cms-scanners/cmseek.md)
detect without ceremony. Keep it in mind only when its md5-of-static-file approach
finds something the header-based tools miss - otherwise reach for the alternatives.

## Install
```bash
git clone https://github.com/jekyc/wig.git
cd wig && python3 setup.py install     # apply the patch below first on Python 3.13+
```

## Usage
```bash
wig http://example.com          # fingerprint a single target
wig -a http://example.com        # do not stop at the first match
```

## Output
Detected platforms and versions with a confidence indication, plus any interesting
files, headers, and subdomains it noticed along the way.

## Gotchas
- **On Python >= 3.13, patch `request2.py`: in `HTMLStripper.__init__` add
  `self.scripting = False`.** Without this it fails on startup, because the base
  `HTMLParser` no longer sets that attribute for it.
- Fingerprints are checksums of known static files; a customised, minified, or
  CDN-fronted deployment defeats them.
- Version output can be a wide range rather than one number - read it as a range.

## Alternatives
- [WhatWeb](whatweb.md) - maintained, broader, the direct replacement
- [CMSeeK](../cms-scanners/cmseek.md) - CMS-focused detection
- [BuiltWith](builtwith.md) - passive, no contact with the target
