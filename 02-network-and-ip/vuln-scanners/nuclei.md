---
name: nuclei
slug: nuclei
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/projectdiscovery/nuclei
categories: [network-and-ip, vuln-scanners]
tags: [templates, misconfiguration, exposure, scanning]
status: unverified
status_checked: 2026-08-26
---

# nuclei

## What question does it answer?
I have a list of hosts or URLs I am authorised to test. Which known
misconfigurations, exposed panels, and default installs are present across all of
them?

## When to reach for it
When you need breadth fast across many targets and want checks that are auditable.
nuclei runs YAML templates - each one a declarative request plus a matcher - against
a target list, so you can read exactly what a check does before running it and write
your own. It is much faster to run than a full scanner like
[Greenbone/OpenVAS](greenbone-openvas.md) and fits naturally at the end of a
discovery pipeline.

Within this repo's scope, use the discovery-flavoured templates: exposed panels,
directory listings, default credentials pages, information disclosure, technology
detection. Exploitation templates are out of scope.

## Install
```bash
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
nuclei -update-templates
```

## Usage
```bash
nuclei -u https://example.com -t http/technologies/    # fingerprinting only, low impact
nuclei -l hosts.txt -t http/exposures/ -severity low,medium
nuclei -l hosts.txt -tags exposure -rl 20 -c 10        # rate-limited, bounded concurrency
```

## Output
One line per finding: template ID, severity, matched URL, and the extracted
evidence. `-json` gives structured output for triage.

## Gotchas
- **This is intrusive.** It sends crafted requests to the target. Written
  authorisation before you run it against anything you do not own - see
  [../../LEGAL.md](../../LEGAL.md).
- Default settings are fast enough to disrupt fragile applications. Use `-rl`
  (rate limit) and `-c` (concurrency) deliberately.
- Community templates vary in quality; false positives are common on
  matcher-only checks. Verify a finding manually before reporting it.
- **Read a template before running it.** Some do far more than probe.

## Alternatives
- [Greenbone/OpenVAS](greenbone-openvas.md) - deeper, slower, credentialed scanning
- [WhatWeb](../../04-web-exploration/fingerprinting/whatweb.md) - fingerprinting without the scan
