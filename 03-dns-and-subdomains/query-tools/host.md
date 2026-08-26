---
name: host
slug: host
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://bind9.readthedocs.io/en/latest/manpages.html
categories: [dns-and-subdomains, query-tools]
tags: [dns, quick-lookup, spf, txt]
status: unverified
status_checked: 2026-08-26
---

# host

## What question does it answer?
I want one DNS answer, right now, without reading a full response packet.

## When to reach for it
When you want speed over detail. `host` prints a plain-English line per record,
which is ideal for a quick check mid-investigation or inside a shell loop. Switch to
[dig](dig.md) the moment you need TTLs, response flags, or to see which section an
answer came from.

It is the fastest way to pull the TXT records that carry mail policy, which is why
it appears throughout the email chapter.

## Install
```bash
sudo apt install dnsutils     # Kali/Debian; macOS ships host
```

## Usage
```bash
host example.com                     # A, AAAA, and MX in one line each
host -t TXT example.com              # SPF and verification records
host -t TXT _dmarc.example.com       # DMARC policy
host 8.8.8.8                         # reverse lookup
```

## Output
One readable line per record: `example.com has address 93.184.216.34`,
`example.com mail is handled by 10 mail.example.com`. Nothing about TTLs or
authority - by design.

## Gotchas
- Active, like any DNS query - it reaches a resolver and usually the target's
  nameservers.
- The default output hides detail you may need; a missing record and a failed query
  can look similar. Use `dig` when the answer matters.
- `nslookup` is the traditional third option, but its output format and deprecation
  status vary by platform - prefer `host` or `dig`.

## Alternatives
- [dig](dig.md) - full detail, resolver selection
- [MXToolbox](../../10-email-investigation/header-analysis/mxtoolbox.md) - the same records via a web UI, with interpretation
