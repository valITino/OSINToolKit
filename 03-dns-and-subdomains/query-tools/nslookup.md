---
name: nslookup
slug: nslookup
tier: 3
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://manpages.debian.org/trixie/bind9-dnsutils/nslookup.1.en.html
superseded_by: dig
categories: [dns-and-subdomains, query-tools]
tags: [dns, interactive, windows, builtin]
status: active
status_checked: 2026-08-26
---

# nslookup

## What question does it answer?
I am on a machine that has nothing installed - very often a Windows one. What does DNS
say about this name, right now?

## When to reach for it
When it is what you have. nslookup ships with Windows and with every BIND install, so
it is the DNS client available on a corporate desktop or a locked-down server where
[dig](dig.md) is not. Its interactive mode - run it with no arguments and you get a
`>` prompt - is genuinely pleasant for exploring by hand: change resolver, change
record type, fire several queries without retyping.

It is tier 3 because for anything scripted [dig](dig.md) is strictly better. That is a
parseability judgement, not an obsolescence one.

## Install
```bash
sudo apt install bind9-dnsutils     # Debian/Ubuntu/Kali; 'dnsutils' is now only a transitional name
# macOS and Windows: already present.
```

## Usage
```bash
nslookup example.com                        # A record via the system resolver
nslookup -type=MX example.com 1.1.1.1       # pick record type and resolver
nslookup -type=PTR 192.0.2.10               # reverse lookup
nslookup                                    # interactive: 'server 9.9.9.9', 'set type=NS', 'exit'
```

## Output
A `Server:`/`Address:` block naming the resolver that answered, then the records. A
`Non-authoritative answer:` header means you were served from a recursive resolver's
cache rather than by the zone's own nameserver. There is **no** structured or short
output mode - that absence is the whole reason to prefer dig in scripts.

## Gotchas
- **nslookup is not deprecated.** ISC announced that in early BIND 9 and then reversed
  it in 2004 with BIND 9.3; the current man page carries no deprecation notice. Pages
  still quoting the old banner are reproducing a twenty-year-old message.
- **Do not screen-scrape it.** No `+short` equivalent, no JSON, and the human format
  varies between implementations. Use `dig +short` for anything automated.
- It applies its own search-list and `ndots` handling, so an unqualified name can
  quietly get a domain suffix appended and answer a question you did not ask. Use
  fully-qualified names.
- Windows ships Microsoft's own implementation. Broadly similar, not flag-identical -
  verify syntax before writing cross-platform instructions.
- A default query hits a recursive resolver, not your target. Naming the target's own
  nameserver as the trailing argument puts your source IP in **their** logs - a real
  change in exposure. See [../../00-methodology/opsec/README.md](../../00-methodology/opsec/README.md).

## Alternatives
- [dig](dig.md) - the better tool whenever you have a choice
- [host](host.md) - a one-line answer with less ceremony
- [dnsx](dnsx.md) - when the question is about thousands of names, not one
