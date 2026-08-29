---
name: FOFA
slug: fofa
tier: 2
contact: passive
type: cli
cost: freemium
platforms: [linux, macos, windows, web]
url: https://en.fofa.info/
categories: [network-and-ip, device-search]
tags: [device-search, banners, favicon-hash, fingerprint-pivot]
status: active
status_checked: 2026-08-29
---

# FOFA

## What question does it answer?
I have a favicon, a scrap of body HTML, a certificate or a page title, and Shodan
and Censys return almost nothing. Which hosts share that fingerprint according to
a scanner with a very different vantage point?

## When to reach for it
A second opinion, not a first stop. FOFA's coverage skews towards Chinese IP space
and Chinese-market products, so it holds deployments [shodan.md](shodan.md) and
[censys.md](censys.md) miss - and misses assets they hold. Reach for it when a
Shodan pivot returns a thin cluster, or for a `body=` or `icon_hash=` pivot in a
syntax Shodan lacks. Do not reach for it if you cannot hand a Chinese vendor your
target list, or if you need a workable free API: [netlas.md](netlas.md) is that.

## Install
```bash
go install github.com/FofaInfo/GoFOFA/cmd/fofa@latest && export FOFA_KEY='your_key'
# No Go toolchain? The REST API takes the query base64-encoded in qbase64:
curl "https://fofa.info/api/v1/search/all?key=$FOFA_KEY&qbase64=$(printf '%s' 'ip="1.1.1.1"' | base64)"
```

## Usage
```bash
fofa account   # always first: credits are spent per query, so read the balance
               # (fofa_point, isvip, remain_api_query) before a broad search
fofa search -fields host,ip,port,protocol,lastupdatetime \
  'body="loading-wrap" && body="balls" && is_domain=true && cert.is_valid=true && country="US"'
               # vendor's own example: one HTML fingerprint, narrowed to assets
               # holding a domain and a valid cert, not throwaway boxes
fofa icon ./data/favicon.ico   # hash an icon you ALREADY hold locally, then pivot:
                               # fofa search 'icon_hash="-247388890"'
```

## Output
CSV, one asset per line: `ip,port` by default, or exactly the `-fields` columns in
order (`168.119.197.62:6379,...,redis,2024-08-23 12:00:00`). `-format json` gives
newline-delimited objects, `fofa count port=80` a bare integer. Read a result set as
an infrastructure cluster, not a host list - the finding is that N hosts share one
fingerprint. Always pull `lastupdatetime`: it is the only signal that a pivot is live
rather than a fossil. Services FOFA cannot identify are labelled `unknown`.

## Gotchas
- **Filters are gated by membership tier** (44 syntaxes free, 60 Professional, 62
  Business), so a query lifted from a blog post can come back empty because your key
  cannot run that filter. An empty result is not absence until you check that.
- The free tier is 300 query credits and 3,000 results a month, labelled
  "(Non-commercial only)", and API access is **not** listed among its features on the
  pricing page. Assume the CLI needs a paid key; confirm with `fofa account`.
- Rate limit is 1 request/second (2/s on Corporate V2), so scripted pivots need
  throttling. The REST API accepts only `qbase64`, never `q=`, and errors return in
  Chinese even on the English site: `[-700] 账号无效` is "invalid account".
- **Jurisdiction and opsec.** FOFA is run from China and every query is tied to your
  account and email. Decide whether that is acceptable before you type, and never
  paste client-identifying strings in. On personal data GDPR still applies to what
  you collect - see [../../LEGAL.md](../../LEGAL.md).
- Not every subcommand is passive: `fofa icon https://target/favicon.ico`,
  `--checkActive` and `jsRender` all make real requests to the target. Hash local
  files instead. Exploitation features of any banner search are out of scope here.
- `fofa.so` still serves an old build; the live fronts are fofa.info and en.fofa.info.
  `pip install fofa` (fofapro/fofa-py) looks official but was last committed in
  January 2024, so treat GoFOFA as the maintained client.

## Alternatives
- [shodan.md](shodan.md) - broader Western coverage; run both, expect disagreement
- [censys.md](censys.md) - stronger certificate and SAN pivots
- [zoomeye.md](zoomeye.md) - the other Chinese scanner, overlapping vantage point
- [../../05-certificates-tls/origin-unmasking/favicon-hash.md](../../05-certificates-tls/origin-unmasking/favicon-hash.md) - `icon_hash` is a third encoding
