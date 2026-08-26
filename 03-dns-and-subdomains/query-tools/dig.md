---
name: dig
slug: dig
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://bind9.readthedocs.io/en/latest/manpages.html
categories: [dns-and-subdomains, query-tools]
tags: [dns, records, resolver, mx, txt]
status: unverified
status_checked: 2026-08-26
---

# dig

## What question does it answer?
I have a domain. What does DNS actually say about it - any record type, from any
resolver I choose?

## When to reach for it
The reference DNS client, and the one to learn properly. Unlike `host`, dig shows
the full response including flags, TTLs, and which section each record came from,
which matters when you are diagnosing rather than just looking up. Being able to
pick the resolver (`@server`) is the key trick: it reveals split-horizon answers
and lets you go straight to the authoritative nameserver.

## Install
```bash
sudo apt install dnsutils     # Kali/Debian; macOS ships dig
```

## Usage
```bash
dig example.com A +short                  # just the answer, scriptable
dig MX example.com @9.9.9.9                # mail servers, via a specific resolver
dig -x 8.8.8.8                             # reverse lookup: IP to PTR name
dig TXT example.com +short                 # SPF, DMARC, and verification records
dig example.com NS +short                  # authoritative nameservers
```

## Output
By default the full response: question, answer, authority, and additional sections,
with TTLs and the responding server. `+short` reduces it to the values alone.
A low TTL suggests a record that changes often; the authority section shows which
nameserver is responsible.

## Gotchas
- A DNS query touches the target's nameservers (or a resolver that will), so this is
  **active**. It is normal traffic, but it is not invisible.
- Answers vary by resolver and by geography - CDNs return different addresses to
  different clients. Query the authoritative NS when you need the canonical answer.
- Cached answers can be stale; TTL tells you how stale it might be.
- Zone transfer (`AXFR`) succeeds only on misconfigured servers; treat any attempt
  as active and scope-sensitive.

## Alternatives
- [host](host.md) - the same lookups, shorter output
- [subfinder](../passive-enum/subfinder.md) - enumerate names rather than query one
