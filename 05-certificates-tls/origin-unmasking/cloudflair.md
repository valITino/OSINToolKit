---
name: CloudFlair
slug: cloudflair
tier: 3
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/christophetd/CloudFlair
categories: [certificates-tls, origin-unmasking]
tags: [cloudflare, origin-ip, censys, broken]
status: broken
status_checked: 2026-08-26
---

# CloudFlair

## What question does it answer?
What is the real origin IP behind this Cloudflare-protected site?

## Why this is tier 3
The technique is clever: search [Censys](../../02-network-and-ip/device-search/censys.md)
for hosts presenting a certificate for the target's domain, then test each candidate
by requesting the site directly and comparing the response. If the origin server is
reachable and still serves the certificate, the protection is bypassed.

It is tier 3 because **it is effectively broken: the Censys API is no longer free.**
The tool depends on Censys certificate search, and that access now requires a paid
plan, so a fresh install with free credentials returns nothing. The underlying
technique still works if you have paid Censys access - the tool's automation is what
has become unavailable to most people.

## Install
```bash
git clone https://github.com/christophetd/CloudFlair.git
cd CloudFlair && pip install -r requirements.txt
# Requires CENSYS_API_ID and CENSYS_API_SECRET - see the status note above.
```

## Usage
```bash
python3 cloudflair.py example.com          # find and verify candidate origin IPs
```

## Output
Candidate origin IPs, and for each one whether requesting the site directly returned
content matching the real site.

## Gotchas
- **Requires paid Censys API access.** Without it, no candidates. See
  [../../99-resources/api-keys/README.md](../../99-resources/api-keys/README.md).
- **Connecting directly to a candidate origin is active contact** with a host that is
  deliberately not exposed. Get authorisation; see [../../LEGAL.md](../../LEGAL.md).
- Modern deployments increasingly restrict origin access to Cloudflare's ranges or use
  Authenticated Origin Pulls, which defeats the technique entirely.
- **Cloudflare Universal SSL groups unrelated domains under shared SANs**, so
  certificate-based candidates include hosts with no connection to your target. Verify
  before drawing conclusions - see [../ct-log-search/crt-sh.md](../ct-log-search/crt-sh.md).

## Alternatives
- [crt.sh](../ct-log-search/crt-sh.md) / [MerkleMap](../ct-log-search/merklemap.md) - certificate history, free
- [../../06-history-and-archives/ip-whois-history/README.md](../../06-history-and-archives/ip-whois-history/README.md) - the IP the domain used *before* it moved behind a CDN
