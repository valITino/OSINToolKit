---
name: dnstwist
slug: dnstwist
tier: 1
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/elceef/dnstwist
categories: [dns-and-subdomains, typosquatting]
tags: [typosquat, homoglyph, phishing, brand]
status: unverified
status_checked: 2026-08-26
---

# dnstwist

## What question does it answer?
I have a brand or domain. What lookalike domains - typos, homoglyphs, swapped
TLDs - exist or are registered, and which of them are live and could be used for
phishing?

## When to reach for it
Immediately for phishing triage and brand protection. dnstwist generates the
permutation space around a name (character swaps, insertions, homoglyphs,
bitsquatting, alternate TLDs) and then checks which candidates are registered and
resolving. It is the fast answer to "is someone squatting on us." It never touches
the brand's own infrastructure; it queries DNS/WHOIS for the *lookalike* domains.

## Install
```bash
pipx install dnstwist        # Kali default; also: docker run elceef/dnstwist
```

## Usage
```bash
dnstwist example.com                     # generate + resolve permutations
dnstwist -r example.com                  # only domains that are actually registered
dnstwist -r -w -a example.com            # add WHOIS and all DNS records for hits
dnstwist --format json example.com > twists.json   # machine-readable
```

## Output
A table of permuted domains with the fuzzer that produced each, plus resolved A/AAAA,
MX, and (with `-w`) WHOIS. Registered, MX-having lookalikes are the ones to
investigate first - MX suggests they can receive mail for a phish.

## Gotchas
- Permutation counts explode for longer names; `-r` to keep only registered hits is
  usually what you want.
- Live-check and `-w` perform DNS/WHOIS lookups against the candidate domains
  (which may be attacker-controlled), so run them from infrastructure you are happy
  to expose.
- A registered lookalike is not proof of malice - parking and defensive
  registration are common. Confirm intent before acting.

## Alternatives
- [urlscan.io](../../04-web-exploration/fingerprinting/urlscan-io.md) - inspect what a suspicious lookalike actually serves
- [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md) - certs issued to a lookalike domain
- [Namedroppers](namedroppers.md) - registered names *containing* the brand, which permutations never generate
