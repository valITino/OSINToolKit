---
name: DNSDB (Farsight / DomainTools)
slug: dnsdb
tier: 2
contact: passive
type: api
cost: paid
platforms: [linux, macos, web]
url: https://docs.domaintools.com/api/dnsdb/
categories: [dns-and-subdomains, passive-dns]
tags: [passive-dns, resolution-history, dnsdbq, farsight, timeline]
status: active
status_checked: 2026-08-29
---

# DNSDB (Farsight / DomainTools)

## What question does it answer?
I have a name or an IP and I need the complete record, not a sample: everything
it resolved to and everything that ever lived on that address, back to June 2010
across 400+ sensors, with dates precise enough to defend a timeline in a report.

## When to reach for it
When the timeline is the finding - a takedown, an attribution, a report someone
will contest - and a partial answer is worse than none. Nothing free comes close
to the depth; nothing else needs a budget approved before you can query it.

## Install
```bash
sudo apt-get install libcurl4-openssl-dev libjansson-dev
git clone https://github.com/dnsdb/dnsdbq.git   # repo moved out of farsightsec/
cd dnsdbq && make install clean
umask 077; echo 'APIKEY="YOURAPIKEYHERE"' > ~/.dnsdb-query.conf
dnsdbq -I -p text       # confirm the key works and read your quota
```

## Usage
```bash
# What this name resolved to, oldest first, tuples still live in 2024 or later.
# Time fencing is always UTC, whatever your shell timezone says.
dnsdbq -r example.com/A -A 2024-01-01 -s -k first -j | jq .

# Reverse: every name seen on this IP. CIDR takes a COMMA: -i 23.21.237.0,24
dnsdbq -i 104.244.13.104 -l 0 -j

# Raw API, no client - the canonical curl from the DomainTools documentation.
curl -H "Accept: application/x-ndjson" -H "X-API-Key: $DNSDB_API_KEY" \
  "https://api.dnsdb.info/dnsdb/v2/lookup/rdata/ip/104.244.13.104?limit=1000"
```

## Output
Newline-delimited JSON in the Streaming API Framing protocol:
`{"cond":"begin"}`, one `{"obj":{...}}` per RRset, then `{"cond":"succeeded"}`
or `{"cond":"limited"}`. Each object carries `count`, `time_first`/`time_last`
(or `zone_time_*`), `rrname`, `rrtype`, `bailiwick` - the zone that answered -
and an `rdata` array. The time pair places the mapping on a timeline; `count`
separates production infrastructure from one-off lookups.

## Gotchas
- **The bookmarked product pages are gone** (`/products/dnsdb` 404s). Work from
  `docs.domaintools.com/api/dnsdb/`, or `scout.dnsdb.info` for the web UI.
- **Paid, no free tier, no self-service.** Trial keys come through sales;
  academics and unpaid anti-abuse volunteers can get free or discounted keys.
- **2010-06-24 is the floor of the dataset**, the NMSG cutover - not the date
  the domain started using that host. Reading it as a start date invents history.
- **Read the final `cond` and your `results_max`.** `{"cond":"limited"}` means a
  partial answer, and `results_max` on the key silently overrides `?limit=`.
  Check `/dnsdb/v2/rate_limit` (free) and size big pulls with `-V summarize`.
- **`dnsdbq -a` is an OPSEC leak**: ASN annotation fires a live DNS lookup per
  address, which the vendor's own docs call an "intolerable information leak".
- Quotas come in three shapes (daily, block, unlimited) with a burst limit as
  tight as 5 requests per 360 seconds; over quota is 429, too many streams 503.
  `time_*` (sensors) and `zone_time_*` (zone files) are different evidence, and
  the web UI caps at 10,000 results against 1,000,000 for the API and CLI.

## Alternatives
- [mnemonic PassiveDNS](mnemonic-pdns.md) - free and keyless for a quick pivot
- [Validin](validin.md) - free tier, about four years deep, adds host pivots
- [CIRCL Passive DNS](circl-pdns.md) - free to vetted partners, CSIRT coverage
