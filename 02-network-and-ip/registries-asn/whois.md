---
name: whois
slug: whois
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://www.rfc-editor.org/rfc/rfc3912
categories: [network-and-ip, registries-asn]
tags: [registration, ownership, asn, domain]
status: unverified
status_checked: 2026-08-26
---

# whois

## What question does it answer?
I have a domain, an IP, or an ASN. Who registered it, when, through whom, and what
contact details are on record?

## When to reach for it
The first lookup on any new identifier, and one of the few tools that takes all
three object types. Registry data is authoritative for *registration* facts
(dates, registrar, nameservers, allocated org) even where personal contact fields
are redacted. Use [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md)
when you want the same lookups in a browser without a client.

## Install
```bash
sudo apt install whois        # Kali/Debian default; macOS ships a whois
```

## Usage
```bash
whois example.com             # domain: registrar, dates, nameservers, status
whois 8.8.8.8                 # IP: allocated org, netblock, abuse contact
whois AS15169                 # ASN: the organisation holding the AS number
whois -h whois.arin.net 8.8.8.8   # query a specific registry directly
```

## Output
Key/value records from the responsible registry. For domains: registrar, creation
and expiry dates, nameservers, and EPP status codes. For IPs and ASNs: the
allocated organisation, netblock range, and abuse contact - the abuse address is
often the most actionable field.

## Gotchas
- **GDPR redacts registrant name, email, and address for many EU domains.**
  "REDACTED FOR PRIVACY" is the norm, not a red flag. See [../../LEGAL.md](../../LEGAL.md).
- Privacy/proxy services (WhoisGuard and similar) hide the real registrant on any
  TLD. Historical WHOIS may predate the privacy - see
  [../../06-history-and-archives/ip-whois-history/README.md](../../06-history-and-archives/ip-whois-history/README.md).
- Output format varies by registry and TLD; some ccTLDs return almost nothing or
  require their own web form.
- Registrant-supplied fields were never verified. Treat a name as a lead.

## Alternatives
- [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md) - browser-based, many lookups on one page
- [ipinfo.io](ipinfo-io.md) - ASN, org, and geo in one clean API call
- [bgp.he.net](bgp-he-net.md) - the routing view of an ASN
