---
name: Rapid7 Nexpose
slug: nexpose
tier: 2
contact: intrusive
type: gui
cost: paid
platforms: [linux, windows]
url: https://www.rapid7.com/products/nexpose/
categories: [network-and-ip, vuln-scanners]
tags: [vulnerability-scanning, risk-scoring, on-premise, authorisation-required]
status: active
status_checked: 2026-08-26
---

# Rapid7 Nexpose

## What question does it answer?
My scan returned four thousand "critical" findings. Which of them actually matter
enough to fix first?

## When to reach for it
For the prioritisation, which is what distinguishes it. Nexpose's **Real Risk Score**
replaces the flat CVSS 1-10 scale with a 1-1000 score that folds in exploit and malware
availability and the age of the vulnerability - Rapid7's own framing is that a plain
CVSS score produces thousands of criticals and no way to sequence them. When the
deliverable is a remediation plan rather than an inventory, that ordering is the product.

It is the **on-premise** scanner in Rapid7's line; InsightVM is the cloud-managed
platform built on the same engine. Choose Nexpose when the data must stay in your
environment.

## Install
```bash
# Commercial download and licence from Rapid7; installer for Linux and Windows.
# The console runs as a service and presents a web UI on https://localhost:3780
```

## Usage
```text
https://localhost:3780/    Create a Site (targets + scan template + credentials),
                           choose a scan template, run it, then work the results
                           by Real Risk Score rather than by CVSS.
```

## Output
Findings per asset with the Real Risk Score, CVSS, exploit and malware-kit availability,
and remediation steps, plus policy-compliance results where a policy template was used.
Reports export for both technical and executive audiences.

## Gotchas
- **There is no free community edition any more.** The old Nexpose Community Edition is
  gone; the entry point today is a time-limited commercial trial. Budget accordingly, or
  use [Greenbone / OpenVAS](greenbone-openvas.md).
- **Intrusive, and it needs written authorisation** naming the targets and the window.
  Credentialed scanning also means giving a scanner privileged access to hosts. See
  [../../LEGAL.md](../../LEGAL.md).
- **Real Risk Score is a vendor model, not an objective measure.** It is genuinely more
  actionable than raw CVSS, but it is Rapid7's opinion. Say which scale you are quoting
  when you report a number, because 1-1000 and 1-10 look confusingly similar.
- Rapid7 also ships Metasploit and the two integrate. **Exploitation is out of scope for
  this reference** - Nexpose's role here ends at identifying and ranking exposure.
- Nexpose and InsightVM share an engine but not a licence or a workflow. Documentation
  found for one may not apply to the other; check which product a page describes.
- Scanning fragile or embedded devices can knock them over. Scope conservatively.
- A finding is evidence, not proof. Verify before it reaches a report.

## Alternatives
- [Tenable Nessus](nessus.md) - the closest commercial equivalent, different scoring
- [Greenbone / OpenVAS](greenbone-openvas.md) - free and open source
- [nuclei](nuclei.md) - fast templated checks when you do not need a full assessment
