---
name: testssl.sh
slug: testssl
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://testssl.sh/
categories: [certificates-tls, cert-analysis]
tags: [tls, ciphers, certificate, configuration]
status: unverified
status_checked: 2026-08-26
---

# testssl.sh

## What question does it answer?
What TLS configuration does this service actually run - which protocol versions and
ciphers, what certificate, and does it still support anything it should not?

## When to reach for it
When you need a complete, readable picture of an endpoint's TLS posture and you would
rather not send it to a third-party web service. It is a single shell script, it runs
from your own machine (so nothing leaves your control), and it works against internal
hosts and non-standard ports that public scanners cannot reach.

## Install
```bash
git clone --depth 1 https://github.com/drwetter/testssl.sh.git
cd testssl.sh && ./testssl.sh --help      # Kali also packages it
```

## Usage
```bash
./testssl.sh example.com                       # full assessment
./testssl.sh --fast --parallel example.com      # quicker overview
./testssl.sh -p -S example.com                  # protocols and certificate details only
./testssl.sh --jsonfile out.json example.com    # structured output for reporting
```

## Output
A colour-coded report by section: supported protocols, cipher suites by strength, the
certificate chain with validity and signature algorithm, and named vulnerability
checks. JSON/CSV output for reports.

## Gotchas
- **Active**: a full run opens many connections to probe protocol and cipher support.
  It is normal TLS traffic, but it is visible and can look like scanning - get
  authorisation for anything sustained.
- A full run takes minutes per host; use `--fast` when triaging many endpoints.
- It tests the endpoint you point it at. Behind a CDN, you are assessing the CDN's
  TLS, not the origin's.

## Alternatives
- [openssl](openssl.md) - quick manual inspection of one connection
- [Censys](../../02-network-and-ip/device-search/censys.md) - existing scan data, no contact
