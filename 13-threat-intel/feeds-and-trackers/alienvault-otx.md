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
It is free, huge and live, and its indicator endpoints answer without a key -
but the community-pulse model makes it unreliable for "is this bad?". Anyone can
publish a pulse with no review, and measured on 2026-08-29 a Tor exit node
carried 50 pulses of recycled scanner-log dumps while an IP published as a live
C2 on ThreatFox the same day carried zero. Both false positives and false
negatives are structural, and the official Python SDK has been untouched since
2021. Decide known-bad with [URLhaus](urlhaus.md) for distribution URLs and
[ThreatFox](threatfox.md) for C2 indicators, then come here as a bibliography.

## When to reach for it
After a verdict, not instead of one - when you have an indicator and want the
published analysis around it. A good pulse hands you the campaign's other
infrastructure for free, which is the real reason to open it. Skip it for triage
volume, for phishing URLs, and for anything where you would have to defend the
source in writing; for hosting history use
[passive DNS](../../03-dns-and-subdomains/passive-dns/dnsdb.md) instead.

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

# Domain sections: general, geo, url_list, passive_dns, malware, whois,
# http_scans. The browser view of the same data, where author and date are
# easiest to eyeball: https://otx.alienvault.com/indicator/ip/198.51.100.7
```

## Output
JSON. The block that matters is `pulse_info`: a count plus pulses carrying name,
`author.username`, created, modified, TLP, tags, adversary and malware_families,
alongside `base_indicator`, a reputation integer, geo and a `sections` list
naming the other endpoints available for this indicator. Read it as a
bibliography, never a verdict: open each pulse and ask whether it is published
analysis or an automated log dump - "Webscanners 2018-02-09 thru current day",
created 2018 and modified daily ever since, is the second kind.

## Gotchas
- **Pulse count is not a score**, and treating it as one is the trap. High means
  popular with bulk uploaders; zero means nobody bothered. See the tier-3 note
  above for the measurement.
- **Pulses are copied and re-copied.** One indicator in ten pulses is usually
  ten people re-importing one original list, not independent corroboration, and
  a pulse created in 2018 but "modified" today is an append-only auto-feed.
  Read `author.username` and the description before citing anything.
- **The useful endpoints are not anonymous.** `passive_dns` returns "Anonymous
  access to this endpoint is limited", and the pulse and subscription endpoints
  return 403, so budget for a free account and an `X-OTX-API-KEY` header.
- **Look-ups are passive; submissions are not.** `submit_url` and `submit_file`
  make the platform fetch and detonate what you send, and the default TLP is
  white - a submission is publication. See [../../LEGAL.md](../../LEGAL.md).
- **The branding has moved twice** (AlienVault to AT&T to LevelBlue) while the
  hostname has not. Expect the domain to shift and third-party write-ups to
  describe an API version that has drifted. The SDK is unmaintained since
  2021-04-02 - pin it if you must depend on it.

## Alternatives
- [ThreatFox](threatfox.md) - decide first whether a C2 indicator is known-bad
- [URLhaus](urlhaus.md) - malware distribution URLs, with a policed scope
- [AbuseIPDB](../../02-network-and-ip/reputation/abuseipdb.md) - crowd reports
  on an IP, with the same crowd caveats
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - vendor
  verdicts and pivots on the same artifact
