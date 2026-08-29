---
name: AlienVault OTX (LevelBlue Open Threat Exchange)
slug: alienvault-otx
tier: 3
contact: passive
type: web
cost: free
platforms: [linux, macos, windows, web]
url: https://otx.alienvault.com/
categories: [threat-intel, feeds-and-trackers]
tags: [pulses, community-ioc, campaign-context, bibliography, levelblue]
status: active
status_checked: 2026-08-29
---

# AlienVault OTX (LevelBlue Open Threat Exchange)

## What question does it answer?
I have an indicator another feed already flagged. Who wrote it up, in what
report, and what else did they list in the same pulse?

## Why this is tier 3
Free, huge and live, and its indicator endpoints answer without a key - but the
community-pulse model makes it unreliable for "is this bad?". Anyone can publish
a pulse with no review: on 2026-08-29 a Tor exit node carried 50 pulses of
recycled scanner-log dumps, while an IP published as a live C2 on ThreatFox that
day carried zero. False positives and false negatives are both structural, and
the Python SDK has been untouched since 2021-04-02. Decide known-bad with
[URLhaus](urlhaus.md) or [ThreatFox](threatfox.md); come here for the write-ups.

## When to reach for it
When you want the published analysis around an indicator: a good pulse hands you
the campaign's other infrastructure for free, which is the real reason to open
it. Not for triage volume, not for phishing URLs, and not where you would have
to defend the source in writing. For hosting history use
[passive DNS](../../03-dns-and-subdomains/passive-dns/dnsdb.md).

## Install
```bash
pip install OTXv2          # v1.5.12, 2021 vintage; still imports on Python 3.11
# Not required: the REST API is plain HTTP. Free key: otx.alienvault.com/api
```

## Usage
```bash
# No key needed. Read the pulse names, never the count.
curl -s https://otx.alienvault.com/api/v1/indicators/IPv4/198.51.100.7/general \
  | jq '.pulse_info.count, .pulse_info.pulses[].name'
# The section actually worth having; anonymous callers are refused here.
curl -s -H "X-OTX-API-KEY: $OTX_KEY" \
  https://otx.alienvault.com/api/v1/indicators/domain/example.com/passive_dns
# Sections: general, geo, url_list, passive_dns, malware, whois, http_scans.
```

## Output
JSON. The block that matters is `pulse_info`: a count plus pulses carrying name,
`author.username`, created, modified, TLP, tags, adversary and malware_families,
beside a reputation integer and geo. Read it as a bibliography, never a verdict:
is each pulse published analysis, or an automated log dump like "Webscanners
2018-02-09 thru current day", created 2018 and modified daily ever since?

## Gotchas
- **Pulse count is not a score**, it is upload volume: high means popular with
  bulk uploaders, zero means nobody bothered (see the tier-3 note), and ten
  pulses on one indicator is usually ten re-imports of one list rather than
  corroboration. Read `author.username` and the description before citing.
- **The useful endpoints are not anonymous.** `passive_dns` returns "Anonymous
  access to this endpoint is limited", and the pulse and subscription endpoints
  return 403, so budget for a free account and an `X-OTX-API-KEY` header.
- **Look-ups are passive; submissions are not.** `submit_url` and `submit_file`
  make the platform fetch and detonate what you send, at default TLP white - a
  submission is publication. See [../../LEGAL.md](../../LEGAL.md).
- **The branding has moved twice** (AlienVault to AT&T to LevelBlue) while the
  hostname has not - expect the domain to shift and old write-ups to be stale.

## Alternatives
- [ThreatFox](threatfox.md) - decide first whether a C2 indicator is known-bad
- [URLhaus](urlhaus.md) - malware distribution URLs, with a policed scope
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - vendor
  verdicts and pivots on the same artifact, when you need a defensible source
