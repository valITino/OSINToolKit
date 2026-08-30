---
name: mnemonic PassiveDNS
slug: mnemonic-pdns
tier: 2
contact: passive
type: api
cost: free
platforms: [web, linux, macos, windows]
url: https://passivedns.mnemonic.no/
categories: [dns-and-subdomains, passive-dns]
tags: [passive-dns, resolution-history, reverse-lookup, no-key, rest-api]
status: active
status_checked: 2026-08-29
---

# mnemonic PassiveDNS

## What question does it answer?
I have a domain, or the IP it resolves to today. What did that name resolve to
before, and what other names have answered from that address? mnemonic answers
both directions from its own sensors - no key, no packet sent to the target.

## When to reach for it
First, because it costs one curl: the quickest way to turn a name into a hosting
timeline, or an address into the names that lived on it. Reach past it once the
answer is load-bearing: the free slice is TLP:white only, sensors skew Nordic.

## Install
```bash
sudo apt install curl jq      # nothing else - it is a public REST API
curl -s 'https://api.mnemonic.no/pdns/v3/cnn.com?limit=1' | jq '.responseCode'
# Higher quota and non-TLP-white data need an Argus-API-Key from mss@mnemonic.no
```

## Usage
```bash
# Everything public mnemonic holds for a domain, both directions.
curl -s 'https://api.mnemonic.no/pdns/v3/cnn.com?limit=0' | jq '.count, .data[]'

# Reverse: every name mnemonic saw answering with this IP.
curl -s 'https://api.mnemonic.no/pdns/v3/140.82.121.4?limit=1000' \
  | jq -r '.data[] | "\(.query)\t\(.rrtype)\t\(.firstSeenTimestamp/1000|todate)"'

# POST form - takes rrClass/rrType as arrays; new parameters land here first.
curl -s -X POST https://api.mnemonic.no/pdns/v3/search \
  -H 'Content-Type: application/json' \
  -d '{"query":"cnn.com","rrClass":["in"],"rrType":["a"],"limit":0}'
```

## Output
One JSON envelope: `{responseCode, limit, offset, count, size, metaData, data}`.
Each element of `data` is an observed tuple - `query`, `answer`, `rrtype`,
`times`, TTLs, `tlp`, and `firstSeenTimestamp`/`lastSeenTimestamp` in
milliseconds. Sort on first-seen for the order a domain moved between hosts;
read last-seen to tell a live mapping from one that stopped years ago. `times`
is the confidence signal: four million observations is production, two a typo.

## Gotchas
- **Default limit is 25 and truncation is silent.** The envelope's `count` is
  the real total (I saw `count=1000` beside `size=3`). Compare the two, or pass
  `limit=0`, before saying "this IP only ever hosted N names".
- **Quota is 10 requests/minute and 1000/day unauthenticated.** Over it you get
  `responseCode 402` and `metaData.millisUntilResourcesAvailable` - back off on
  that value rather than retrying blindly.
- **The public slice is essentially forward resolution.** `rrType=ns` and
  `rrType=mx` returned count 0 for cnn.com and github.com while the unfiltered
  queries returned thousands. Never conclude "this domain had no MX".
- `/pdns/v3/<query>/seen` returned `401 User not authenticated` without a key
  despite being documented as public, and `/pdns/v3/cof/` returns
  `time_first: 0` on live data - any date read from the COF endpoint is wrong.
- A bare query matches **both** sides and does not expand subdomains. Sensor
  placement is undisclosed, so absence here is absence of evidence: corroborate
  before saying a name never pointed somewhere.

## Alternatives
- [DNSDB (Farsight / DomainTools)](dnsdb.md) - paid, but the longest defensible history
- [Validin](validin.md) - free tier, adds host-response pivots
- [CIRCL Passive DNS](circl-pdns.md) - CSIRT data, stronger on malicious hosting
