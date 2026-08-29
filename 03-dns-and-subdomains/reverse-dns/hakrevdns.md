---
name: hakrevdns
slug: hakrevdns
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/hakluke/hakrevdns
categories: [dns-and-subdomains, reverse-dns]
tags: [reverse-dns, ptr, netblock, pipeline]
status: active
status_checked: 2026-08-26
---

# hakrevdns

## What question does it answer?
I have a netblock rather than a single address. What hostname does every IP in it
resolve back to, and which of those names belong to my target?

## When to reach for it
When you have moved from one IP to the range around it - after an ASN lookup, a
[BGP.HE](../../02-network-and-ip/registries-asn/bgp-he-net.md) query, or a cloud
provider's published ranges - and want names across the whole block. It reads addresses
on stdin and prints PTR results, so `prips` plus this turns a CIDR into a hostname list
in one pipe.

Prefer [HackerTarget](hackertarget-reversedns.md) for a handful of addresses with
nothing installed; prefer this when the list is long and you want to choose the
resolver you query.

## Install
```bash
go install github.com/hakluke/hakrevdns@latest   # no distro package exists; Go only
sudo apt install prips                            # CIDR expander for the pipeline
```

## Usage
```bash
echo 173.0.84.110 | hakrevdns -U                 # -U = use default resolvers (see Gotchas)
prips 192.0.2.0/24 | hakrevdns -U -d -t 32       # sweep a netblock, hostnames only
echo 173.0.84.110 | hakrevdns -r 9.9.9.9         # pin one specific resolver
prips 192.0.2.0/24 | hakrevdns -R resolvers.txt -d | sort -u
```

## Output
By default: the queried IP, then a tab, then the hostname **with its trailing dot**.
`-d` prints only the hostname and strips that dot, which is the form you want for
piping onward. IPs with no PTR produce no line at all, so input and output line counts
never match. Results arrive in goroutine order, not input order - pipe through `sort`
if you need stable output.

## Gotchas
- **You must pass a resolver flag or you silently get nothing.** With no `-U`, `-r`, or
  `-R`, the resolver list is empty, the lookup loop never runs, and the tool exits 0
  having printed nothing. The bare `prips ... | hakrevdns` form shown in its own README
  does not work.
- **`-d` means different things in the two halves of the pipeline.** In `prips`, `-d`
  sets the output delimiter and takes an argument; in hakrevdns it is a boolean meaning
  "domains only". `prips -d 192.0.2.0/24` will misparse the CIDR.
- **PTR records are set by whoever controls the reverse zone**, usually the hosting
  provider. `ec2-203-0-113-9.compute-1.amazonaws.com` identifies the host, not the
  tenant. Forward-confirm anything you intend to rely on.
- Silent failure modes overlap: you cannot tell "no PTR" from "resolver timed out".
- `-t` defaults to 8 and there is no rate limiting or backoff. `prips` will happily
  stream 16.7M addresses from a `/8` - bound the range before piping. See
  [../../LEGAL.md](../../LEGAL.md).
- prips is IPv4 only, which caps the whole pipeline at IPv4.

## Alternatives
- [HackerTarget reverse DNS](hackertarget-reversedns.md) - no install, ranges supported, rate-limited
- [Robtex](robtex.md) - the same pivot from a pre-indexed database, zero contact
- [dnsx](../query-tools/dnsx.md) - `-ptr` over a CIDR, plus every other record type
