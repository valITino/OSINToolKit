---
name: Netlas.io
slug: netlas
tier: 2
contact: passive
type: cli
cost: freemium
platforms: [linux, macos, windows, web]
url: https://netlas.io/
categories: [network-and-ip, device-search]
tags: [device-search, lucene, certificates, whois]
status: active
status_checked: 2026-08-29
---

# Netlas.io

## What question does it answer?
I have an IP, a domain or an organisation name and no budget. Which hosts,
certificates, domains or WHOIS records match this query in someone else's scan
data, and can I drive that from a script?

## When to reach for it
When the budget is zero and the work still has to be scriptable. Netlas issues an
API key on a free account, splits its data into five indices (response, cert,
domain, whois-ip, whois-domain) and takes Apache Lucene syntax. The domain index
gives subdomain enumeration out of scan data, with no DNS traffic to the target.

It is not the deepest dataset: [Shodan](shodan.md) and [Censys](censys.md)
carry longer history and richer host detail, CVE and tag filters sit behind the
Business plan, and 50 requests a day rules Netlas out for a large mapping job.

## Install
```bash
pip install netlas          # SDK and CLI (pipx install netlas also documented)
brew tap netlas-io/netlas && brew install netlas    # CLI only, no Python
netlas savekey "YOUR_API_KEY"    # once; key from https://app.netlas.io/profile/
```

## Usage
```bash
netlas host "1.1.1.1"   # all Netlas holds on one IP or domain, scriptable
netlas count -d response "port:7001"   # size the set BEFORE searching: on 50
            # requests/day you cannot afford to page into a four-million-host answer
netlas search --datatype domain "domain:*.netlas.io"   # subdomains from scan data
            # alone - no DNS query reaches the target
netlas search -d cert -f json 'certificate.subject_dn:example.com'   # who else
            # presents a cert naming this organisation (3 requests/min limit here)
```

## Output
YAML by default, `-f json` for machine parsing; a response-index hit nests the useful
fields under `data` (`data.ip`, `data.port`, `data.path`, `data.protocol`). Read each
row as one observed service response, not one host - the same IP recurs once per port
and path, so deduplicate on `ip` before reporting host counts.

## Gotchas
- An account and API key are mandatory for the CLI, SDK and API; there is no
  anonymous mode, and the key lives at https://app.netlas.io/profile/.
- **The free tier's 50 requests/day counts pages, not queries.** One broad search
  paged at 20 results a page eats the whole day, and you are capped at 2,500
  results/month and 200 per download besides. Count first, then search.
- **CVE and tag filters need the Business plan.** On a free key such a query returns
  a capability you never had, not fewer hosts - do not read it as "nothing here".
- Certificate queries are throttled to 3 requests/minute against 60 elsewhere, so a
  cert-pivot loop at speed gets HTTP 429 with `Retry-After`. The SDK backs off for
  you; hand-rolled curl does not.
- **Lucene has edges that silently return nothing**: wildcards and regex do not work
  inside quoted phrases, KEYWORD fields are case-sensitive where TEXT fields are not,
  and a KEYWORD regex must match the whole value - so an empty result is very often a
  syntax fault rather than an absence.
- Search endpoints hard-cap at 10,000 results, so treat a search view as a sample and
  use the Download endpoints for a full set - which your plan also caps. Records are
  timestamped snapshots; note when each was observed.
- Netlas also sells a Private Scanner and Attack Surface Discovery that do real
  scanning. Querying the dataset is passive; switching those on contacts the target
  and changes the legal position. WHOIS rows carry personal data, so GDPR applies to
  what you keep - see [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Shodan](shodan.md) - deeper host detail and history, thinner free tier
- [Censys](censys.md) - the stronger certificate dataset if you can pay
- [ONYPHE](onyphe.md) - server-side aggregation instead of raw rows
- [FOFA](fofa.md) - a different vantage point when Netlas coverage looks thin
