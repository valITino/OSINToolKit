---
name: HackerTarget reverse DNS API
slug: hackertarget-reversedns
tier: 2
contact: passive
type: api
cost: freemium
platforms: [web]
url: https://hackertarget.com/reverse-dns-lookup/
categories: [dns-and-subdomains, reverse-dns]
tags: [reverse-dns, ptr, shared-hosting, api]
status: unverified
status_checked: 2026-08-26
---

# HackerTarget reverse DNS API

## What question does it answer?
I have an IP. What hostnames point at it - including domains that have nothing to do
with the one I started from?

## When to reach for it
When you want the answer in one curl and nothing installed. This is the classic
IP-to-hostnames pivot: given an address from a DNS lookup or a log, it returns the
names associated with it, which often exposes an organisation's other sites on the
same host. Its value is convenience; for depth use a passive DNS provider.

## Install
```bash
# Nothing to install - plain HTTP, no key needed for light use.
```

## Usage
```bash
curl "https://api.hackertarget.com/reversedns/?q=8.8.8.8"        # names for one IP
curl "https://api.hackertarget.com/reversedns/?q=8.8.8.0/24"      # across a range
curl "https://api.hackertarget.com/hostsearch/?q=example.com"     # hosts for a domain
```

## Output
Plain text, one result per line - trivially greppable and pipeable. An error string
in the body (rather than an HTTP error) is how it signals rate limiting, so check the
content, not just the status code.

## Gotchas
- **Free use is rate-limited per source IP** and the limit is low; sustained use
  needs a paid key. The API returns a text error message rather than failing loudly.
- PTR records are set by whoever controls the IP's reverse zone, which is often the
  hosting provider, not your target - a name here is a lead, not proof of ownership.
- Shared hosting means dozens of unrelated domains on one address. Do not infer a
  relationship between them.

## Alternatives
- [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md) - reverse IP in a browser
- [dig](../query-tools/dig.md) - `dig -x` for a single authoritative PTR lookup
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - passive DNS history for an IP
