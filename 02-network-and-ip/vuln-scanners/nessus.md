---
name: Tenable Nessus
slug: nessus
tier: 2
contact: intrusive
type: gui
cost: paid
platforms: [linux, macos, windows]
url: https://www.tenable.com/products/nessus
categories: [network-and-ip, vuln-scanners]
tags: [vulnerability-scanning, credentialed, compliance, authorisation-required]
status: active
status_checked: 2026-08-26
---

# Tenable Nessus

## What question does it answer?
I am authorised to assess these hosts. What known vulnerabilities and misconfigurations
are present, in a report a client will accept?

## When to reach for it
When the deliverable is a report someone else has to act on. Nessus is the commercial
reference point for vulnerability assessment - its plugin coverage is deep and current,
and its output is the format most clients and auditors already recognise. Given
credentials it authenticates to hosts and reads installed package versions and
configuration directly, which removes most of the guesswork that remote-only scanning
produces.

Use [Greenbone / OpenVAS](greenbone-openvas.md) when the budget is zero and you can
accept slower feed updates; use [nuclei](nuclei.md) when you want targeted templated
checks at speed rather than a full assessment.

## Install
```bash
# Download the .deb/.rpm for your platform, then activate with a licence code:
# https://www.tenable.com/downloads/nessus
sudo dpkg -i Nessus-*.deb && sudo systemctl start nessusd    # UI at https://localhost:8834
```

## Usage
```text
https://localhost:8834/    Scans -> New Scan -> pick a template (Basic Network Scan,
                           Advanced, Credentialed Patch Audit), set targets, add
                           credentials under Credentials, then Launch.
```

## Output
Findings per host, ranked by severity, each with the plugin that fired, the evidence it
saw, CVE references, and remediation guidance. Exports to PDF, HTML, CSV and `.nessus`
XML - the XML is the one to keep, because it is what other tools ingest.

## Gotchas
- **The free tier is far smaller than its reputation.** Nessus Essentials is now
  **5 IPs on a 30-day licence**, non-commercial only. The widely repeated "16 IPs, free
  forever" is out of date. Essentials Plus (paid, non-commercial) raises it to 20 IPs;
  verified students and instructors can get a free one-year Essentials Plus licence.
  Anything commercial requires Nessus Professional.
- **This is intrusive scanning and needs written authorisation** covering the exact
  targets and window. Credentialed scans additionally mean handing privileged
  credentials to a scanner. See [../../LEGAL.md](../../LEGAL.md).
- Scans can destabilise fragile hosts - printers, embedded devices, legacy SCADA. Use a
  conservative template and exclude anything you were not explicitly told to touch.
- **Findings are not verified exploitation.** A plugin fires on evidence, not proof; the
  false-positive rate on version-inference checks is real. Confirm before reporting.
- Exploitation is out of scope for this reference. Nessus reports what is vulnerable;
  what happens next belongs to an authorised engagement, not to this repo.
- Plugin feeds update constantly, so two scans days apart are not comparable. Record the
  feed date with the results.

## Alternatives
- [Greenbone / OpenVAS](greenbone-openvas.md) - free and open source, same job
- [Nexpose](nexpose.md) - the Rapid7 equivalent, different risk scoring
- [nuclei](nuclei.md) - fast, templated, community-driven checks
