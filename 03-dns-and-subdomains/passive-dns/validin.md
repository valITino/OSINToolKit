---
name: Validin
slug: validin
tier: 2
contact: passive
type: api
cost: freemium
platforms: [web, linux, macos, windows]
url: https://www.validin.com/
categories: [dns-and-subdomains, passive-dns]
tags: [passive-dns, resolution-history, host-response, pivots, freemium]
status: active
status_checked: 2026-08-29
---

# Validin

## What question does it answer?
I have a domain or an IP. What did it resolve to over the last few years, what
else has lived on that address or netblock, and - unusually for something with a
free tier - what did the web server there actually serve, so I can pivot on a
favicon, body or header hash to the rest of the operator's infrastructure.

## When to reach for it
When you want resolution history and host fingerprints from one place, and a
handful of careful lookups is all you need: the free tier is a triage budget, not
an automation budget. Use [dnsdb.md](dnsdb.md) when the question reaches back
before roughly 2022, and [mnemonic-pdns.md](mnemonic-pdns.md) for a keyless answer.

## Install
```bash
# Nothing to install. Free Community account at https://app.validin.com/ , then
# copy the API key from your profile. Note the header value is literally BEARER.
export VALIDIN_KEY='...'
curl -s -H "Authorization: BEARER $VALIDIN_KEY" https://app.validin.com/api/ping
```

## Usage
```bash
V='https://app.validin.com/api/axon'; H="Authorization: BEARER $VALIDIN_KEY"

# A/AAAA/NS history for the domain and its subdomains, with readable dates.
curl -s -H "$H" "$V/domain/dns/history/example.com?wildcard=true&time_format=iso"

# Reverse: names seen on this IP; swap in 104.244.13.0/24 to sweep a netblock.
curl -s -H "$H" "$V/ip/dns/history/104.244.13.104?time_format=iso"

# Not passive DNS: favicon, body and header hash pivots from Validin's crawls.
curl -s -H "$H" "$V/domain/pivots/example.com"
```

## Output
One JSON object: `{query_opts, query_key, status, records, records_returned,
limited}`. `records` is keyed by record or association type (A, NS, NS_FOR, CERT,
WHOIS ...), each an array of `{key, value, value_type, first_seen, last_seen}`.
Read the seen pair as that mapping's observation window and `limited` before
anything else. The `_FOR` types are the reverse direction pre-computed: `NS_FOR`
answers "which domains used this nameserver", often the pivot that opens a case.

## Gotchas
- **The free tier is 10 queries a day and 50 a month, capped at 250 results, and
  truncation shows only as `"limited": true`.** `limit` defaults to 1000 in the
  spec but the tier cap wins silently, turning a cut-off list into a false "this
  IP only ever hosted N domains". Check `/api/profile/usage` before scripting.
- **`api.validin.com`, the host the integration docs tell you to allow, does not
  resolve.** Every working endpoint, and every server entry in Validin's OpenAPI
  specs, is `app.validin.com`; firewall rules copied from the docs permit the
  wrong host and block the right one.
- **Coverage claims disagree by three years**: the homepage says seven, the
  pricing table six, the plan blurb and the docs "over four". Treat four years as
  the defensible floor and do not quote seven in a report.
- **Crawl history is 21 days on Community and Professional**, full history being
  Enterprise-only, so the favicon and banner pivots work on live infrastructure
  and quietly fail on anything that went dark a month ago - while DNS history for
  that host goes back years. "No crawl data" is not "never existed".
- API access stays "Limited" on Professional as well as Community; only
  Enterprise is "Full". The record-type suffix goes *after* the domain
  (`/dns/history/example.com/A`), the reverse of most APIs, `exclude_nx` works
  only on the base endpoint, and failed auth returns 403 rather than 401.

## Alternatives
- [dnsdb.md](dnsdb.md) - paid, back to 2010, when depth is the point
- [mnemonic-pdns.md](mnemonic-pdns.md) - keyless, no account, quick pivots
- [favicon-hash](../../05-certificates-tls/origin-unmasking/favicon-hash.md) - the same hash pivot by hand
