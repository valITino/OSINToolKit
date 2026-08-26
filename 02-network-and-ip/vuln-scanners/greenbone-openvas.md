---
name: Greenbone / OpenVAS
slug: greenbone-openvas
tier: 2
contact: intrusive
type: gui
cost: free
platforms: [linux]
url: https://www.greenbone.net/
categories: [network-and-ip, vuln-scanners]
tags: [vulnerability-scan, cve, reporting, authenticated-scan]
status: unverified
status_checked: 2026-08-26
---

# Greenbone / OpenVAS

## What question does it answer?
I am authorised to assess this network. What known vulnerabilities does a full,
systematic scan find, in a form I can hand to whoever has to fix them?

## When to reach for it
When the deliverable is a formal vulnerability report over a whole estate, not a
quick check. Greenbone's Community Edition (the scanner historically known as
OpenVAS) maintains a large feed of network vulnerability tests, supports
credentialed scanning for accurate patch-level findings, and produces
severity-ranked reports. Reach for [nuclei](nuclei.md) instead when you want speed
and targeted checks rather than exhaustive coverage.

## Install
```bash
sudo apt install gvm         # Kali packages it as GVM
sudo gvm-setup               # initialises the DB and downloads the feeds (slow)
sudo gvm-start               # then open the web UI on localhost
```

## Usage
```text
1. Create a Target (hosts or ranges, plus credentials for an authenticated scan).
2. Create a Task bound to that target with a scan configuration.
3. Run it, then read the report by severity.
4. Export to PDF/XML for the write-up.
```

## Gotchas
- **Intrusive by definition** - it actively probes services and can crash fragile
  or embedded devices. Written authorisation, a maintenance window, and an agreed
  scope. See [../../LEGAL.md](../../LEGAL.md).
- **First setup is slow.** The initial feed sync takes a long time and needs disk;
  scans on a large range take hours.
- Findings are CVE-matched from version banners unless you scan with credentials -
  expect false positives from backported patches, which is exactly what
  authenticated scanning fixes.
- Exploitation is out of scope here; use the report to prioritise remediation.

## Output
Severity-ranked findings per host with CVE references, the evidence that triggered
each, and remediation guidance, exportable as PDF/XML/CSV.

## Alternatives
- [nuclei](nuclei.md) - fast, templated, easier to scope
- [nmap](../port-scanning/nmap.md) - service discovery without vulnerability matching
