---
name: openssl
slug: openssl
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://www.openssl.org/
categories: [certificates-tls, cert-analysis]
tags: [tls, certificate, san, handshake]
status: unverified
status_checked: 2026-08-26
---

# openssl

## What question does it answer?
What certificate is this host actually presenting right now - who issued it, to which
names, and valid until when?

## When to reach for it
The universally available way to look at one certificate. Every Unix box has it, so
it works when nothing else is installed. The investigative payoff is the **SAN list**:
one handshake often reveals a set of related hostnames you had not enumerated. Use it
for a targeted look; use [testssl.sh](testssl.md) for a full configuration audit.

## Install
```bash
sudo apt install openssl        # present on essentially every Unix system
```

## Usage
```bash
# The certificate, decoded:
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -text

# Just the SANs - the hostname pivot:
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -ext subjectAltName

# Validity dates and issuer only:
openssl s_client -connect example.com:443 </dev/null 2>/dev/null | openssl x509 -noout -dates -issuer
```

## Output
The decoded certificate: subject and issuer, validity window, public key details,
signature algorithm, and extensions - including `subjectAltName`, which holds the
hostname list.

## Gotchas
- **Always pass `-servername`** for SNI. Without it a shared host returns its default
  certificate, not the target's, and you will analyse the wrong thing.
- **The Cloudflare shared-SAN trap**: Universal SSL certificates list unrelated
  customers' domains together, so a shared SAN is **not** evidence of shared
  ownership. See [crt.sh](../ct-log-search/crt-sh.md).
- A handshake is contact with the target - normal, but logged.
- Behind a CDN you see the edge certificate, not the origin's.

## Alternatives
- [testssl.sh](testssl.md) - the full configuration report
- [crt.sh](../ct-log-search/crt-sh.md) - historical certificates without touching the host
