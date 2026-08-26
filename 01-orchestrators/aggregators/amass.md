---
name: OWASP Amass
slug: amass
tier: 1
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/owasp-amass/amass
categories: [orchestrators, aggregators]
tags: [attack-surface, dns, asn, netblocks]
status: unverified
status_checked: 2026-08-26
---

# OWASP Amass

## What question does it answer?
I have a domain or an organisation. What is its full DNS and network footprint -
subdomains, resolved IPs, ASNs, and netblocks - and how are those assets related?

## When to reach for it
When you want the deepest asset model, not just a flat subdomain list. Amass maps
relationships between names, addresses, ASNs, and netblocks, which makes it the
tool for scoping an organisation's real internet presence. Use its passive mode
for OPSEC-safe discovery; use active enumeration (with authorisation) when you
need resolution and brute forcing.

## Install
```bash
# Prefer a pinned release binary from the GitHub releases page.
go install -v github.com/owasp-amass/amass/v5/...@latest   # builds current v5
```

## Usage
```bash
amass enum -passive -d example.com                 # no target contact
amass enum -active -d example.com -brute            # resolve + brute (authorised targets)
amass intel -org "Example Inc"                      # org name -> ASNs/domains
amass viz -d3 -dir ./amass-db                       # visualise the collected graph
```

## Output
A local graph database of discovered assets and the subcommands to query and
visualise it. `enum` yields names and IPs; `intel` yields org-to-ASN mappings;
`viz` renders the relationships.

## Gotchas
- **The v4 to v5 upgrade changed the module/import path and some subcommand
  behaviour. Pin your version** and match your notes to it, or scripts silently
  break. Current line is v5.1.1 (Apr 2026).
- `-active` and `-brute` touch the target and can be intrusive at volume; default
  to `-passive` unless you are authorised.
- Full passive coverage benefits from API keys in the config file.

## Alternatives
- [subfinder](../../03-dns-and-subdomains/passive-enum/subfinder.md) - faster, passive-only subdomains
- [BBOT](../recursive-scanners/bbot.md) - recursive multi-tool that wraps enumeration
- [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md) - single best passive subdomain source
