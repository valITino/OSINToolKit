---
name: CMSeeK
slug: cmseek
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/Tuhinshubhra/CMSeeK
categories: [web-exploration, cms-scanners]
tags: [cms, detection, wordpress, joomla, drupal]
status: unverified
status_checked: 2026-08-26
---

# CMSeeK

## What question does it answer?
I have a URL. Which CMS is behind it, which version, and what can I learn about its
users and themes without hammering the site?

## When to reach for it
The detection-first CMS tool: it recognises a large number of content management
systems (far more than the WordPress/Joomla/Drupal big three), so it is the right
first move when you do not yet know what you are looking at. Once you know it is
WordPress, [WPScan](wpscan.md) goes deeper; if you only need the tech stack,
[WhatWeb](../fingerprinting/whatweb.md) is lighter.

## Install
```bash
git clone https://github.com/Tuhinshubhra/CMSeeK.git
cd CMSeeK && pip install -r requirements.txt
python3 cmseek.py --help
```

## Usage
```bash
python3 cmseek.py -u https://example.com          # detect the CMS on one target
python3 cmseek.py -l targets.txt                   # a list of targets
python3 cmseek.py -u https://example.com --follow-redirect
```

## Output
The detected CMS and version where it can determine one, plus CMS-specific
enumeration (themes, plugins, sometimes usernames). Results are written to a
per-target JSON file under the tool's `Result/` directory.

## Gotchas
- Detection relies on fingerprints that change between CMS releases; a "not detected"
  result on a heavily customised or CDN-fronted site is common and does not mean
  there is no CMS.
- Enumeration beyond detection sends many requests - that is **active** shading into
  intrusive. Scope it and get authorisation before going past detection.
- The project's maintenance cadence has been uneven; verify current behaviour before
  depending on it. Status here is `unverified` deliberately.

## Alternatives
- [WPScan](wpscan.md) - much deeper, WordPress only
- [CMSmap](cmsmap.md) - multi-CMS with vulnerability lookups
- [WhatWeb](../fingerprinting/whatweb.md) - general fingerprinting, lighter touch
