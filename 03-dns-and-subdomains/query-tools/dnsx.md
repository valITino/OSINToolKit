---
name: dnsx
slug: dnsx
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/projectdiscovery/dnsx
categories: [dns-and-subdomains, query-tools]
tags: [dns, bulk-resolution, ptr, asn, pipeline]
status: active
status_checked: 2026-08-26
---

# dnsx

## What question does it answer?
I have a list of hostnames or a netblock, not a single name. What does DNS say about
all of them, in a form I can pipe into the next tool?

## When to reach for it
When [dig](dig.md) is the right idea but the wrong shape. dig answers one question
beautifully; dnsx answers ten thousand and writes the answers one per line. It reads
hosts on stdin, so it slots into a chain between enumeration and whatever comes next,
and it resolves a whole ASN or CIDR to PTR records in a single command - which is the
fastest way to turn "I have an IP range" into "I have names".

## Install
```bash
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```

## Usage
```bash
subfinder -silent -d example.com | dnsx -silent -a -resp   # which names resolve, and to what
echo 192.0.2.0/24 | dnsx -silent -resp-only -ptr           # reverse-resolve a whole netblock
dnsx -l subs.txt -a -cname -mx -ns -json -o dns.json       # several record types, structured
dnsx -l subs.txt -a -resp -asn                             # resolve and tag each with its ASN
```

## Output
One line per result, silent by default so it pipes. `-resp` appends the answer to the
queried name; `-resp-only` prints just the answer. `-json` gives a structured record
per host with every requested type, which is the form worth keeping in a case file.
`-asn` adds the ASN and organisation inline - a free pivot to
[registries](../../02-network-and-ip/registries-asn/README.md).

## Gotchas
- **Wildcard DNS makes everything "resolve".** Use `-wd example.com` for manual
  wildcard filtering or `-auto-wildcard`; the two are mutually exclusive and JSON
  output is recommended with them.
- It is a resolver, not a discovery tool. `-w` brute forces from a wordlist, and that
  use is **intrusive** - authorisation applies, see [../../LEGAL.md](../../LEGAL.md).
  Plain resolution of names you already have is ordinary DNS traffic.
- Rate limiting is **disabled by default**. Set `-rl` before pointing it at anything
  you do not own, or you will hammer resolvers.
- Answers are only as good as the resolver. Public resolvers hijack NXDOMAIN and
  geo-split answers; supply your own with `-r` when accuracy matters.
- **`-recon` queries eleven record types including AXFR** and is slow enough to look
  hung on a large list. Name the types you actually want instead.
- dnsx also accepts an ASN (`AS17012`) as input, which it expands to that ASN's
  prefixes. That expansion needs an outbound lookup of its own and will return nothing
  silently where it is blocked - verify it works on your network before relying on it.

## Alternatives
- [dig](dig.md) - one name, full authoritative detail, no install
- [host](host.md) - the quick sanity check
- [massdns](../active-enum/massdns.md) - faster still at very large volumes, less friendly
