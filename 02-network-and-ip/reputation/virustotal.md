---
name: VirusTotal
slug: virustotal
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://www.virustotal.com/
categories: [network-and-ip, reputation]
tags: [reputation, malware, passive-dns, multi-engine]
status: unverified
status_checked: 2026-08-26
---

# VirusTotal

## What question does it answer?
I have a file hash, URL, domain, or IP. Do security vendors consider it malicious,
and what else is associated with it?

## When to reach for it
The default second opinion on any indicator, and more than a malware scanner: the
Relations tab holds passive DNS (which domains resolved to this IP, and when),
referring files, and communicating samples. That pivot data is often more valuable
to an investigator than the detection verdict itself.

## Install
```bash
# Web needs nothing. The public API needs a free key and is heavily rate-limited.
```

## Usage
```bash
# Web: https://www.virustotal.com/gui/ip-address/8.8.8.8
curl -s -H "x-apikey: $VT_KEY" https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8
curl -s -H "x-apikey: $VT_KEY" https://www.virustotal.com/api/v3/domains/example.com/resolutions
```

## Output
Per-vendor verdicts with a detection ratio, plus community comments and votes. For
domains and IPs, the Relations view gives historical resolutions, subdomains,
sibling domains, and files seen communicating with the indicator.

## Gotchas
- **Detections are not truth.** A handful of hits on an obscure engine is often a
  false positive; zero hits does not mean clean. Read which engines flagged it.
- **Uploading a file makes it available to VirusTotal's customers.** Never upload a
  sensitive document, a client's file, or anything confidential - search the hash
  instead. This is an OPSEC decision, not a formality.
- The public API is roughly a few requests per minute and a few hundred per day -
  enough for triage, not for bulk enrichment.
- Submitting a URL causes VirusTotal to fetch it, which is contact with the target.

## Alternatives
- [AbuseIPDB](abuseipdb.md) - crowd-sourced abuse reports
- [IPVoid](ipvoid.md) - blacklist aggregation
- [urlscan.io](../../04-web-exploration/fingerprinting/urlscan-io.md) - sandboxed page analysis
