---
name: WhatWeb
slug: whatweb
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/urbanadventurer/WhatWeb
categories: [web-exploration, fingerprinting]
tags: [fingerprinting, cli, plugins, headers]
status: unverified
status_checked: 2026-08-26
---

# WhatWeb

## What question does it answer?
I have a URL (or a list of them). What is running on it right now - server, CMS,
framework, JavaScript libraries, and versions?

## When to reach for it
The CLI counterpart to [BuiltWith](builtwith.md), and the better choice when you have
many targets or need current data rather than a crawl history. It requests the page
and matches the response against a large plugin set. Its aggression level is
explicit, which matters: level 1 is a single polite request, higher levels probe.

## Install
```bash
sudo apt install whatweb      # Kali default
```

## Usage
```bash
whatweb https://example.com                    # single target, default aggression
whatweb -a 1 -v https://example.com             # stealthy single request, verbose detail
whatweb -i hosts.txt --log-json=out.json        # batch a list, structured output
```

## Output
A one-line summary per target listing each detected technology with a confidence and,
where it can, a version - plus useful incidentals like country, redirect chain, and
interesting headers. `-v` expands each match to show what evidence triggered it.

## Gotchas
- **Aggression levels above 1 send extra requests** and start to look like scanning.
  Stay at level 1 unless you are authorised for more; see [../../LEGAL.md](../../LEGAL.md).
- Version numbers come from banners and page markers, both of which are trivially
  faked or stripped. Treat them as a hypothesis.
- A CDN or WAF in front of the origin means you are fingerprinting the edge, not the
  application.

## Alternatives
- [BuiltWith](builtwith.md) - passive, with history and tracking IDs
- [urlscan.io](urlscan-io.md) - full page behaviour, screenshots, and resources
- [CMSeeK](../cms-scanners/cmseek.md) - when you specifically need the CMS
