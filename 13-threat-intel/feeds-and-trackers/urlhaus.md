---
name: URLhaus
slug: urlhaus
tier: 2
contact: passive
type: web
cost: freemium
platforms: [linux, macos, windows, web]
url: https://urlhaus.abuse.ch/
categories: [threat-intel, feeds-and-trackers]
tags: [malware-urls, payload-hashes, asn-pivot, bulk-export, abuse-ch]
status: active
status_checked: 2026-08-29
---

# URLhaus

## What question does it answer?
I have a URL or a hostname out of a log. Has anyone already published it as a
malware distribution site, which family did it serve, and who reported it?

## When to reach for it
First, on any suspicious download URL, before you fetch anything yourself: the
corpus ships as a 3 MB CSV you grep locally, so the check costs the target
nothing. Then to widen - the ASN, country and TLD feeds turn one bad host into
every URLhaus URL in the same AS, and the payload dump joins URLs to the hashes
they served, the bridge into [MalwareBazaar](../file-and-hash/malwarebazaar.md).

Malware distribution only, by policy: phishing, exploit-kit landers and adware
get deleted, so a miss says nothing about a phishing URL - that goes to
[PhishTank](phishtank.md). For a C2 use [ThreatFox](threatfox.md); for what a
URL serves right now, [urlQuery](../url-analysis/urlquery.md).

## Install
```bash
git clone https://github.com/abusech/URLhaus   # optional python3 samples
# The data is plain HTTP. Free Auth-Key: https://auth.abuse.ch/
```

## Usage
```bash
# Last 30 days of malware URLs, regenerated every 5 min. Do not poll faster.
curl -s https://urlhaus.abuse.ch/downloads/csv_recent/ -o urlhaus_recent.csv

# One URL per line - match a proxy log locally, not one query per indicator.
curl -s https://urlhaus.abuse.ch/downloads/text/ | grep -Ff - proxy.log

# Every URLhaus URL inside one AS number (14061 = DigitalOcean). Max 1/10 min.
curl -s https://urlhaus.abuse.ch/feeds/asn/14061/

# Single-URL lookup, as the official lookup_url.py does it (needs the key).
curl -H "Auth-Key: $ABUSECH_KEY" -d "url=http://198.51.100.7/bin.sh" \
  https://urlhaus-api.abuse.ch/v1/url/
```

## Output
CSV or JSON: id, dateadded, url, url_status, last_online, threat, tags,
urlhaus_link, reporter - a row from 2026-08-29 gives id `3909815`, `online`,
`malware_download`, tags `32-bit,elf,mips,Mozi`, reporter `geenensp`. Read it
right to left: `reporter` is whose judgement you are trusting (many rows are
automated sensor feeds), `tags` give the family and architecture to pivot on,
`url_status` with `last_online` says whether this is live infrastructure or a
corpse, and `dateadded` decides whether the finding is reportable at all.

## Gotchas
- **abuse.ch was half-broken on 2026-08-29.** `urlhaus-api.abuse.ch` and
  `auth.abuse.ch` served an expired wildcard certificate, so every TLS client
  refused, while `urlhaus.abuse.ch` sat on a valid one. Re-check before writing
  the API off, and never work around it with `curl -k`.
- **Documentation and enforcement disagree.** The docs mark every dataset
  "Auth-Key required", yet `/downloads/csv_recent/`, `/downloads/text/` and the
  ClamAV signatures served keyless the same day - a courtesy that can be
  switched off without notice.
- **The dumps are windowed, not historical**: the full dump holds only URLs
  active now or added in the last 90 days, csv_recent 30 days, the RPZ and
  hostfile 48 hours; an aged-out IOC is missing from the export, not from
  history. `url_status` flips to offline within hours on fast-flux hosting, so
  re-pull before quoting and cite the dates beside the URL.
- **Submitting is publishing.** Your handle is attached to every URL you submit
  unless you set the anonymous flag, and the URL goes public immediately, which
  tells the operator the infrastructure is burned.
- **The blocking datasets are not the CSV**: the ClamAV, RPZ and hostfile
  exports exclude hostnames in the Tranco Top 1M, so malware parked on a popular
  shared host or CDN sits in the CSV and in none of them. Scripted web-UI
  access is bounced to a `/verify-ua/` robot check - automate against the API.

## Alternatives
- [ThreatFox](threatfox.md) - the C2 half of the same abuse.ch pipeline
- [PhishTank](phishtank.md) - phishing URLs, which URLhaus excludes by policy
- [MalwareBazaar](../file-and-hash/malwarebazaar.md) - the payload it served
- [urlQuery](../url-analysis/urlquery.md) - what the URL serves now, fetched
