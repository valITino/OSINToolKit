---
name: massdns
slug: massdns
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/blechschmidt/massdns
categories: [dns-and-subdomains, active-enum]
tags: [dns, bulk-resolution, performance, ptr]
status: active
status_checked: 2026-08-26
---

# massdns

## What question does it answer?
I have a list of millions of candidate names, or a whole netblock. Which of them
actually resolve, and can I find out in minutes rather than days?

## When to reach for it
When resolution itself is the bottleneck. massdns is a raw high-performance stub
resolver: you give it names and a list of resolvers, it fires queries as fast as the
network allows. It generates nothing - no wordlists, no permutations - so it is the
engine underneath other tools rather than a starting point.

Use [puredns](puredns.md) if you want massdns's speed **with** wildcard detection and
result validation, which is almost always what you actually want. Come here directly
for bulk PTR sweeps of a netblock, or for DNS cache snooping with `--norecurse`.

## Install
```bash
git clone https://github.com/blechschmidt/massdns && cd massdns
make                    # use 'make nolinux' on macOS/BSD; binary lands in ./bin/massdns
```

## Usage
```bash
./bin/massdns -r lists/resolvers.txt -t A -o S -w results.txt domains.txt   # bulk A lookups
./scripts/ptr.py | ./bin/massdns -r lists/resolvers.txt -t PTR -w ptr.txt   # sweep PTR space
./scripts/subbrute.py example.com lists/names.txt | ./bin/massdns -r lists/resolvers.txt -t A -o S -w out.txt
./bin/massdns -r lists/resolvers.txt -t A --norecurse -o J -w snoop.json names.txt  # cache snooping
```

## Output
`-o` picks the format: `S` simple text (name, type, value plus the resolver that
answered), `L` a bare domain list, `F` full text, `J` newline-delimited JSON. The
resolver IP is included in the output on purpose - it is how you spot one bad resolver
poisoning a slice of your results.

## Gotchas
- **Your resolver list is the whole game.** Public resolvers rate-limit, lie, and
  hijack NXDOMAIN. The bundled `lists/resolvers.txt` ages badly; a stale or
  unvalidated list produces confident, wrong answers.
- **No wildcard handling.** On a wildcard domain every name "resolves" and you get a
  useless result set. [puredns](puredns.md) exists to solve exactly this.
- Sending tens of thousands of queries per second is **intrusive** and will be read as
  an attack. Bound it with `-s` and get written authorisation -
  see [../../LEGAL.md](../../LEGAL.md).
- It drops privileges to `nobody` when started as root; do not use `--root`.
- `--norecurse` cache snooping queries third-party resolvers, not your target - useful,
  but know whose infrastructure you are touching.

## Alternatives
- [puredns](puredns.md) - massdns plus wildcard filtering and validation
- [dnsx](../query-tools/dnsx.md) - slower, but handles many record types and pipelines cleanly
- [fierce](fierce.md) - discovery of the surrounding netblock rather than raw speed
