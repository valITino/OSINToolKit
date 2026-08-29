---
name: CertWatch
slug: certwatch
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://binsec.tools/certwatch/
categories: [certificates-tls, ct-log-search]
tags: [ct-logs, subdomains, cross-tld, browser-only]
status: active
status_checked: 2026-08-26
---

# CertWatch

## What question does it answer?
I have an organisation's name rather than one domain. Which certificates has it
requested **across every TLD** - the .net, the .de, the country brands I do not know
about yet?

## When to reach for it
For the cross-TLD search, which is the thing it does that the usual CT tools do not.
Alongside a normal domain lookup it offers a "Domain without TLD" mode: give it
`example` and it returns matches under example.com, example.net, example.de and so on.
That turns a single brand name into an inventory of an organisation's separately
registered domains, which is exactly the pivot you want early in a scoping exercise.

Use [crt.sh](crt-sh.md) as your default CT source - it is broader and scriptable. Come
here when you specifically need the brand-across-TLDs view.

## Install
```bash
# Nothing to install - browser only, no account needed.
```

## Usage
```text
https://binsec.tools/certwatch/
  Search method "Domain"            + example.com   -> subdomains under that domain
  Search method "Domain without TLD" + example      -> matches across every TLD
```

## Output
A list of hostnames seen in Certificate Transparency logs for the query. Results are
capped at 10,000 records with no obvious pagination, so a large or long-lived
organisation will be silently truncated.

## Gotchas
- **There is no API.** The search is a POST-only form protected by a CSRF token whose
  field names carry a per-session random prefix, so it cannot be driven by a URL
  pattern or a simple curl. Treat it as a browser-only lookup; automate against
  [crt.sh](crt-sh.md) instead.
- **Do not look for it at `certwatch.binsec.io`** - that host does not resolve. The tool
  lives at `binsec.tools`; the vendor page is at `binsec.com`.
- The operator does not publish which CT logs it queries or how fresh the index is.
  Treat a result as a lead and cross-check anything load-bearing against a second CT
  source.
- The 10,000 cap means **absence proves nothing** on a large domain.
- Despite the name it is a one-shot search, not a subscribe-and-alert monitor.
- It is a third-party hosted service in Germany; the domains you search are visible to
  its operator. See [../../00-methodology/opsec/README.md](../../00-methodology/opsec/README.md).

## Alternatives
- [crt.sh](crt-sh.md) - the default: broader, has a real API, scriptable
- [MerkleMap](merklemap.md) - fast search with an API and its own index
- [Censys](../../02-network-and-ip/device-search/censys.md) - certificates joined to the hosts serving them
