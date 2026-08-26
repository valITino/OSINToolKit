---
name: viewdns.info
slug: viewdns
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://viewdns.info/
categories: [web-exploration, whois-domains]
tags: [whois, reverse-ip, ip-history, toolbox]
status: unverified
status_checked: 2026-08-26
---

# viewdns.info

## What question does it answer?
I have a domain or IP and no tools installed. Who owns it, what else is on that
address, what did it resolve to before, and does it respond?

## When to reach for it
The one-page toolbox. viewdns bundles a couple of dozen free lookups - WHOIS, reverse
IP, IP history, DNS records, traceroute, port check, DNS propagation - which makes it
the fastest way to answer a quick question from any browser, including one that is
not your working machine. Its **IP history** and **reverse IP** lookups are the ones
worth remembering; they are otherwise paywalled almost everywhere.

## Install
```bash
# Nothing to install - web only. An API key exists for scripted use.
```

## Usage
```text
https://viewdns.info/reverseip/?host=example.com     # other domains on the same IP
https://viewdns.info/iphistory/?domain=example.com    # historical A records
https://viewdns.info/whois/?domain=example.com        # registration record
```

## Output
A simple table per tool. Reverse IP lists co-hosted domains; IP history lists past
addresses with the dates observed - the latter is often the single most useful free
lookup on the site.

## Gotchas
- **Reverse IP on shared hosting returns hundreds of unrelated domains.** Co-hosting
  is not a relationship. Check whether the IP belongs to a shared host before drawing
  any line between the domains.
- Free lookups are rate-limited and results are capped; some tools are truncated
  without an API key.
- Its port-check and traceroute tools contact the target from viewdns's
  infrastructure, not yours - convenient for OPSEC, but the target still sees a probe.
- Historical data completeness varies; absence is not evidence.

## Alternatives
- [whois](../../02-network-and-ip/registries-asn/whois.md) - authoritative registration data
- [HackerTarget reverse DNS](../../03-dns-and-subdomains/reverse-dns/hackertarget-reversedns.md) - scriptable reverse lookups
- [../../06-history-and-archives/ip-whois-history/README.md](../../06-history-and-archives/ip-whois-history/README.md) - deeper history sources
