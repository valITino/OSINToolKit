---
name: ThreatFox
slug: threatfox
tier: 2
contact: passive
type: web
cost: freemium
platforms: [linux, macos, windows, web]
url: https://threatfox.abuse.ch/
categories: [threat-intel, feeds-and-trackers]
tags: [c2, ioc-lookup, malware-families, malpedia, abuse-ch]
status: active
status_checked: 2026-08-29
---

# ThreatFox

## What question does it answer?
I have an IP, domain or URL that looks like callback infrastructure. Is it a
published C2 or payload-delivery indicator, for which malware family, and on
whose word?

## When to reach for it
When the artifact is a beacon destination rather than a download link: an
`ip:port` from a memory dump, a domain from a config, a URL from a proxy log.
The prize is not the yes/no but `malware_printable`, `malware_alias` and the
Malpedia link, which turn one artifact into a family name and a reading list
for [MalwareBazaar](../file-and-hash/malwarebazaar.md). Not a history service:
indicators older than six months are expired out, so for what an IP did last
year use [passive DNS](../../03-dns-and-subdomains/passive-dns/circl-pdns.md).

## Install
```bash
# Nothing to install: plain HTTP POST. Free Auth-Key: https://auth.abuse.ch/
```

## Usage
```bash
API=https://threatfox-api.abuse.ch/api/v1/
# Single indicator. exact_match avoids the default substring-wildcard search.
curl -H "Auth-Key: $ABUSECH_KEY" -X POST $API \
  -d '{"query":"search_ioc","search_term":"198.51.100.7","exact_match":true}'
# Recent IOC firehose. days is capped at 7; older data comes from the exports.
curl -H "Auth-Key: $ABUSECH_KEY" -X POST $API -d '{"query":"get_iocs","days":7}'
# Several artifacts at once, without one round-trip per indicator.
curl -s https://threatfox.abuse.ch/export/csv/recent/ | grep -Ff artifacts.txt
```

## Output
JSON or CSV per IOC: ioc_value, ioc_type (`ip:port`, domain, url, md5_hash),
threat_type (`botnet_cc`, `payload_delivery`), malware_printable with
malware_alias and a Malpedia link, first_seen_utc, last_seen_utc,
confidence_level, is_compromised, reference, tags, anonymous, reporter. Read
`confidence_level` and `is_compromised` together: a real 2026-08-29 row -
`tappancsrendelo.hu`, payload_delivery, js.clearfake, confidence 90,
`is_compromised: True` - is a hacked legitimate site, not attacker-owned.

## Gotchas
- **The query API hard-fails without a key**: no `Auth-Key` header returns
  `{"error": "Unauthorized"}`. The `/export/` dumps were still keyless on
  2026-08-29, but the docs say otherwise. The key portal `auth.abuse.ch` served
  an expired certificate that day, blocking new keys - re-check, not `curl -k`.
- **Since 2025-05-01, indicators older than six months are expired** and are not
  returned by the API or the exports. They stay searchable in the web UI flagged
  as expired, so an API miss on an old artifact means "aged out", not "unseen".
- **`is_compromised: True` marks victims, not adversaries**, and covers a large
  share of payload_delivery rows. Naming that domain's owner as the threat actor
  is the most damaging misread of this feed.
- **confidence_level is set by the submitter** and many rows carry reporter
  `anonymous`, so a 100 is often one person's assertion. Matching an `ip:port`
  entry on the IP alone false-positives on shared and reassigned cloud ranges.
- **Submissions are public** and attributed to your handle unless flagged
  anonymous; either way the indicator publishes at once, telling the operator
  their infrastructure is burned. Commercial use may need the paid Spamhaus API.

## Alternatives
- [URLhaus](urlhaus.md) - malware distribution URLs from the same pipeline
- [MalwareBazaar](../file-and-hash/malwarebazaar.md) - the sample behind the C2
- [AlienVault OTX](alienvault-otx.md) - who wrote up the campaign, afterwards
- [AbuseIPDB](../../02-network-and-ip/reputation/abuseipdb.md) - who complained
