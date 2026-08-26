---
name: CMSmap
slug: cmsmap
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/Dionach/CMSmap
categories: [web-exploration, cms-scanners]
tags: [wordpress, joomla, drupal, fingerprinting]
status: unverified
status_checked: 2026-08-26
---

# CMSmap

## What question does it answer?
I have a site running WordPress, Joomla, Drupal, or Moodle. What version, plugins,
and themes is it running, and are any of them known to be vulnerable?

## When to reach for it
When you need a CMS assessment across more than one platform and want known-issue
lookups attached to what it finds. It enumerates plugins and themes and cross-checks
them against public vulnerability data. Use [CMSeeK](cmseek.md) first if you do not
yet know which CMS it is, and [WPScan](wpscan.md) instead when the answer is
WordPress and you want depth.

CMSmap's exploit-execution and credential-attack features are **out of scope** for
this repo - use it here for enumeration only.

## Install
```bash
git clone https://github.com/Dionach/CMSmap.git
cd CMSmap && pip3 install .
```

## Usage
```bash
cmsmap https://example.com                  # detect and enumerate
cmsmap https://example.com -f W             # force WordPress checks
cmsmap -i targets.txt -o results.txt         # batch, save output
```

## Output
The detected CMS and version, enumerated plugins and themes with versions, and
flagged findings ranked by severity, each with a reference to the public advisory.

## Gotchas
- **On Python 3.13, patch `cmsmap/lib/threadscanner.py`: add
  `from urllib.parse import quote` at the top, URL-encode the plugin path with
  `quote(plugin, safe="/")`, and comment out the original unencoded request line.**
  Without this the plugin enumeration fails on paths containing characters that must
  be escaped.
- Plugin and theme enumeration is **intrusive** - it requests hundreds of paths.
  Written authorisation before running it against a site you do not own; see
  [../../LEGAL.md](../../LEGAL.md).
- Version-matched vulnerability findings produce false positives when a maintainer
  has backported a fix without changing the version string. Verify before reporting.

## Alternatives
- [WPScan](wpscan.md) - deeper and better maintained for WordPress
- [CMSeeK](cmseek.md) - detection across many more CMSs
- [nuclei](../../02-network-and-ip/vuln-scanners/nuclei.md) - templated checks you can read first
