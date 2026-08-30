---
name: CIRCL Passive DNS
slug: circl-pdns
tier: 2
contact: passive
type: api
cost: free
platforms: [linux, macos, windows]
url: https://www.circl.lu/services/passive-dns/
categories: [dns-and-subdomains, passive-dns]
tags: [passive-dns, cof, csirt, resolution-history, pypdns]
status: active
status_checked: 2026-08-29
---

# CIRCL Passive DNS

## What question does it answer?
I have a domain or an IP from an incident. What did it resolve to historically,
and what else lived on that address - as seen by a European CSIRT collecting
from malware analysis and partner feeds, in a format other providers share.

## When to reach for it
When the infrastructure is malicious or suspected to be: a dataset fed by
sandbox output sees command-and-control domains a commercial sensor network
never sees. Ordinary hosting is thinly covered, and access needs vetting first.

## Install
```bash
pip install pypdns     # `pdns` CLI and the pypdns library, 2.3.2 (Feb 2026)
# Credentials are NOT self-service: email CIRCL your affiliation and intended
# use of the data, per https://www.circl.lu/services/passive-dns/
export CIRCL_USER='...' CIRCL_PASS='...'
```

## Usage
```bash
# Raw REST call, HTTP basic auth - without credentials this is a flat 401.
curl -u "$CIRCL_USER:$CIRCL_PASS" https://www.circl.lu/pdns/query/circl.lu

# v2 runs an active resolver BY DEFAULT; this header switches it off.
curl -u "$CIRCL_USER:$CIRCL_PASS" -H 'dribble-disable-active-query: 1' \
  https://www.circl.lu/pdns/query/example.com

# Page past a truncation: -si prints x-dribble-cursor, fed back as the cursor.
curl -si -u "$CIRCL_USER:$CIRCL_PASS" -H 'dribble-filter-rrtype: CNAME' \
  -H 'dribble-paginate-cursor: 7346046680497455128' \
  https://www.circl.lu/pdns/query/cdn1.wixdns.net
```

## Output
Newline-delimited JSON in Passive DNS Common Output Format: one object per
tuple, `{rrtype, rrname, rdata, count, time_first, time_last}`, times as epoch
seconds. Metadata rides in the headers, not the body - `x-dribble-cursor` for
the next page, `x-dribble-errors` for truncation. Sort on `time_first` for the
timeline; `count` is weight, so once is a scan artefact and hundreds is hosting.

## Gotchas
- **Not open access.** Credentials go only to "trusted partners" who email CIRCL
  their affiliation and intended use; unauthenticated requests return 401. That
  purpose binds your use, and history tied to a person is personal data - see
  [../../LEGAL.md](../../LEGAL.md).
- **The active resolver is on by default**, so a lookup can trigger a live
  resolution of the name under investigation. If your rules say nothing touches
  the target, send `dribble-disable-active-query` on every request.
- **Truncation appears only in a header.** CIRCL's own example shows `maxset` at
  1000 against `total_value` 532915 - 0.2% of the data. Miss `x-dribble-errors`
  and you report a shared host as having 1000 domains.
- **Field orientation is a reading trap.** Querying `circl.lu` returns `rrname`
  = 185.194.93.14 and `rdata` = circl.lu, the reverse of the usual reading.
  Check which field holds your query string before automating a pivot.
- COF is an expired Internet-Draft, not a standard, so cross-provider field
  compatibility is convention only. CIDR queries are unsupported (a /24 is 256
  requests), and the bundled CLI takes `--password` in argv, leaking it to `ps`.

## Alternatives
- [mnemonic PassiveDNS](mnemonic-pdns.md) - no key at all, answers in one curl
- [DNSDB (Farsight / DomainTools)](dnsdb.md) - paid, back to 2010, the reference dataset
- [Validin](validin.md) - free tier that adds host-response pivots
