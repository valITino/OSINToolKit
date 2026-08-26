---
name: urlscan.io
slug: urlscan-io
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://urlscan.io/
categories: [web-exploration, fingerprinting]
tags: [sandbox, screenshot, phishing, resources]
status: unverified
status_checked: 2026-08-26
---

# urlscan.io

## What question does it answer?
What does this URL actually do when a browser loads it - what does it look like, what
does it request, where does it redirect - without me visiting it?

## When to reach for it
Essential for phishing and suspicious-link triage. urlscan loads the page in its own
browser and records everything: a screenshot, the full resource and domain list, the
redirect chain, and the certificates involved. Searching its archive of previous
scans is fully passive and often answers the question without a new scan at all -
somebody has usually scanned that phishing domain already.

## Install
```bash
# Nothing to install. A free API key raises limits and enables scripted submission.
```

## Usage
```text
https://urlscan.io/search/?q=domain:example.com     # search existing scans - passive
https://urlscan.io/                                  # submit a new scan (see visibility note)
```

```bash
curl -s "https://urlscan.io/api/v1/search/?q=page.domain:example.com" | jq '.results[].task.url'
```

## Output
A report per scan: screenshot, the full list of requested domains and files, the
redirect chain, IPs and ASNs contacted, TLS certificates, and any detected
brand-impersonation verdicts. Everything is linkable, which makes it good evidence
for a write-up.

## Gotchas
- **Searching is passive; submitting is not.** A submission fetches the target from
  urlscan's infrastructure, and a **public** scan is visible to everyone -
  including the operator of the site you are investigating. Choose Unlisted or
  Private when the investigation is sensitive. See
  [../../00-methodology/opsec/README.md](../../00-methodology/opsec/README.md).
- Phishing pages often cloak: they serve benign content to datacentre IPs and the
  real page to targets. A clean scan is not proof of a clean site.
- Scans are point-in-time; a fast-rotating phishing kit may look different an hour
  later.

## Alternatives
- [WhatWeb](whatweb.md) - direct fingerprinting when you can touch the target
- [gowitness](../monitoring-visual/gowitness.md) - bulk screenshots you control
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - reputation verdicts on the URL
