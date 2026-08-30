---
name: Intelligence X
slug: intelligence-x
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web, linux, macos, windows]
url: https://intelx.io/
categories: [darkweb, onion-discovery]
tags: [tor, onion, leaks, pastes, archive, selector-search]
status: active
status_checked: 2026-08-29
---

# Intelligence X

## What question does it answer?
I have a selector - an email address, a domain, a .onion host, an IP or a
Bitcoin address. Where has it appeared in archived pastes, leak dumps, stealer
logs and Intelligence X's own Tor and I2P crawl?

## When to reach for it
When you need to pivot a known selector into onion addresses, or to read a
hidden-service page that is already gone - IntelX holds an archived copy, so you
never touch the service. For keyword discovery use [Ahmia](ahmia.md) instead.

## Install
```bash
pip install intelx   # 0.8.1, published 2026-05-31; Go, PHP, JS and a Maltego
# transform live in the same SDK repo. The web UI needs only a free account (50
# lookups/day); the API needs your own key from intelx.io/account?tab=developer.
```

## Usage
```bash
intelx.py -search riseup.net -buckets "pastes, darknet.tor"
# the invocation that does onion discovery: darknet.tor is the Tor crawl
intelx.py -search riseup.net -limit 100   # widen past the default result cap
intelx.py -search cia.gov --phonebook emails   # reverse lookup pulling emails,
# URLs and subdomains tied to a domain (paid)
```
```text
https://intelx.io/?s=example.com   # documented no-API web pattern: takes an
# email, domain, IP, CIDR or Bitcoin address
```

## Output
A faceted list: title, description, date, date-added, media type and bucket,
with an Expert Information block carrying System ID, Storage ID, Simhash, access
level and size. Read it bucket-first: a hit in `darknet.tor` means the crawler
saw that string on a hidden service and archived the page. Then read date-added
- the only timestamp you can defend.

## Gotchas
- **The onion-discovery half is the paid half.** Both darknet buckets are marked
  PRO; a free 50-lookups/day account gets the public web and leak buckets only,
  and Researcher is EUR 2,500/year with the API tier at EUR 7,000.
- **Selector-only.** Keywords, company names and slang return "Invalid Search
  Term", which investigators routinely misread as "no results".
- Public API keys are discontinued: any tool shipping an embedded IntelX key is
  broken. Get your own, and do not commit it.
- Two limits: a daily quota, and a concurrent-search cap that answers "Maximum
  Concurrent Searches". Parallel scripts trip the second one first.
- **It is an archive.** A `darknet.tor` hit proves the crawler saw that content
  once, not that the service is live. Coverage is unpublished too, so absence is
  not evidence of absence.
- Passive towards the target, but queries are logged against your own account.
- Downloading items pulls third-party personal data, sometimes illegal material,
  onto your machine - an offence in most jurisdictions whatever your intent,
  with reporting and data-protection duties: [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Ahmia](ahmia.md) - free keyword search over live onions, no selector rules
- [dark.fail](dark-fail.md) - signed canonical address for a named service
- [Pastebin](../../09-code-paste-forums/paste-sites/pastebin.md) - the paste
  corner of the same problem, searched directly
