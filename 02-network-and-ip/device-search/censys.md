---
name: Censys
slug: censys
tier: 2
contact: passive
type: web
cost: paid
platforms: [web]
url: https://search.censys.io/
categories: [network-and-ip, device-search]
tags: [device-search, certificates, host-correlation]
status: unverified
status_checked: 2026-08-26
---

# Censys

## What question does it answer?
Which hosts on the internet present this certificate, this SAN, or this service
configuration - and how do those hosts relate to my target?

## When to reach for it
When the pivot is a **certificate**. Censys indexes both hosts and certificates and
lets you join the two, which is what makes it the standard tool for questions like
"who else serves a cert for this domain" or "what host is behind this CDN,
identified by the origin certificate it still presents". For plain exposure
questions, [Shodan](shodan.md) is usually the faster answer.

## Install
```bash
# Web interface at search.censys.io; API access requires credentials.
```

## Usage
```text
# Host search:
services.tls.certificates.leaf_data.subject.common_name: "example.com"

# Certificate search:
names: example.com and parsed.validity.end: [2024-01-01 TO *]
```

## Output
Host records with services, TLS details, and ASN/location; certificate records with
subject, SANs, issuer, validity, and the CT logs that carry them. The two views
cross-link.

## Gotchas
- **The API is no longer meaningfully free.** Free-tier access has been reduced over
  time and now covers little more than interactive browsing - this is what breaks
  tools that depended on it, notably
  [CloudFlair](../../05-certificates-tls/origin-unmasking/cloudflair.md). Budget for a
  paid plan before building a workflow on it.
- The query language has changed across platform versions; syntax from older
  write-ups may not run. Check the current documentation.
- A certificate match links *hosts presenting a cert*, which is not the same as
  common ownership - see the Cloudflare shared-SAN trap in
  [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md).

## Alternatives
- [Shodan](shodan.md) - broader banner search, better value
- [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md) - free CT log search
- [MerkleMap](../../05-certificates-tls/ct-log-search/merklemap.md) - another free CT index
- [ZoomEye](zoomeye.md) - stronger APAC coverage, as a third opinion
