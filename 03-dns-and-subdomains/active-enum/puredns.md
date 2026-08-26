---
name: puredns
slug: puredns
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/d3mondev/puredns
categories: [dns-and-subdomains, active-enum]
tags: [dns, brute-force, wildcard, validation]
status: active
status_checked: 2026-08-26
---

# puredns

## What question does it answer?
I brute forced a domain and got thousands of hits. Which of them are real, and which
are just a wildcard record answering everything?

## When to reach for it
This is the one to reach for when the domain has a wildcard, which in practice is most
of them. puredns wraps [massdns](massdns.md) for speed but adds the part that makes the
output trustworthy: it detects wildcard roots, filters the names that only resolve
because of them, and then re-validates every survivor against a small set of trusted
resolvers. Raw massdns gives you speed; puredns gives you speed you can act on.

## Install
```bash
# massdns first - puredns shells out to it
git clone https://github.com/blechschmidt/massdns && cd massdns && make && sudo make install
go install github.com/d3mondev/puredns/v2@latest
```

## Usage
```bash
puredns bruteforce all.txt example.com                    # wordlist against one domain
puredns bruteforce all.txt -d domains.txt                 # ...against many domains
cat subdomains.txt | puredns resolve -q | httprobe        # validate a list, pipe onward
puredns resolve domains.txt --write valid.txt --write-wildcards wildcards.txt
```

## Output
Validated domains on stdout. `-q` strips everything but the names so it pipes cleanly.
The three `--write` flags are what you want for casework: `--write` the clean list,
`--write-wildcards` the wildcard roots it identified (useful evidence in itself), and
`--write-massdns` the underlying massdns records so you can recover the A and CNAME
values later without re-querying.

## Gotchas
- **Resolver quality decides result quality.** puredns looks for `resolvers.txt` in the
  working directory, then `~/.config/puredns/`. Trusted resolvers default to `8.8.8.8`
  and `8.8.4.4`; if you change them with `--resolvers-trusted`, re-validate your output
  and adjust `--rate-limit-trusted`.
- Requires massdns on `PATH` - a missing massdns is the usual first-run failure.
- Wildcard detection can be defeated by **DNS load balancing**, where each query returns
  a different address; the project documents this as a known limitation.
- Brute forcing is **intrusive**. Written authorisation - see
  [../../LEGAL.md](../../LEGAL.md).
- Go 1.x only supports the last two major releases; an old toolchain fails the install.

## Alternatives
- [massdns](massdns.md) - the engine, when you want raw resolution and no filtering
- [dnsmap](dnsmap.md) - no configuration at all, when you just want an answer
- [subfinder](../passive-enum/subfinder.md) - get the passive names first, then validate them here
