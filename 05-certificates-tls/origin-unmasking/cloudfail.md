---
name: CloudFail
slug: cloudfail
tier: 3
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/m0rtem/CloudFail
categories: [certificates-tls, origin-unmasking]
tags: [cloudflare, origin, subdomains, legacy]
status: active
status_checked: 2026-08-29
---

# CloudFail

## What question does it answer?
Does this Cloudflare-fronted domain have a subdomain that was never proxied, pointing
straight at the origin?

## Why this is tier 3
CloudFail runs three phases: a DNSDumpster lookup for misconfigured records, a query
against the **Crimeflare** database, and a brute force over roughly 2,500 subdomains.

The middle phase is dead. Crimeflare no longer serves anything - `crimeflare.org`
answers HTTP 522 and its other hosts do not connect at all - so a third of the tool is
now a no-op that fails quietly. What still works is the part you could do yourself: DNS
lookups and a subdomain wordlist.

It stays here because the **premise** remains correct and is still the most productive
origin-discovery angle: operators put the apex behind the CDN and forget `mail`, `ftp`,
`dev`, `staging` or `cpanel`, which then resolve to the origin. You just do not need
this tool to check that.

## Install
```bash
git clone https://github.com/m0rtem/CloudFail && cd CloudFail
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python3 cloudfail.py -t example.com          # all three phases
python3 cloudfail.py -t example.com -T       # route requests over Tor
```

## Output
Subdomains found, each with the address it resolves to, and a note where an address
falls outside Cloudflare's published ranges - those are the candidate origins.

## Gotchas
- **The Crimeflare phase returns nothing and does not say so.** Do not read an empty
  result as "no origin found".
- **A non-Cloudflare address is a candidate, not the origin.** Verify it by requesting
  the site directly with the right `Host` header and comparing the response.
- Subdomain brute forcing is **intrusive** and needs authorisation - see
  [../../LEGAL.md](../../LEGAL.md).
- An origin found this way is often firewalled to Cloudflare's ranges anyway, so it
  answers you with nothing. That is the correct configuration, not a failed lookup.
- [subfinder](../../03-dns-and-subdomains/passive-enum/subfinder.md) plus
  [crt.sh](../ct-log-search/crt-sh.md) gives you a better subdomain list than its bundled
  2,500-word list, passively.

## Alternatives
- [Favicon hash pivoting](favicon-hash.md) - the technique that still works today
- [CloudFlair](cloudflair.md) - the certificate-based approach; also degraded
- [../../06-history-and-archives/ip-whois-history/README.md](../../06-history-and-archives/ip-whois-history/README.md) - the address the domain used before the CDN
