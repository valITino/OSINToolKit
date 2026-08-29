---
name: Favicon hash pivoting
slug: favicon-hash
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://pypi.org/project/mmh3/
categories: [certificates-tls, origin-unmasking]
tags: [favicon, murmurhash, shodan, origin]
status: active
status_checked: 2026-08-29
---

# Favicon hash pivoting

## What question does it answer?
This site sits behind a CDN. Which other hosts on the internet serve the **same
favicon** - and is one of them the unproxied origin?

## When to reach for it
When the certificate route has stopped working. [CloudFlair](cloudflair.md) needs paid
Censys access and [CloudFail](cloudfail.md) leans on a dead database, but this angle is
still live: internet-wide scanners index a hash of every favicon they see, so you can
ask "who else serves this exact icon?" and get back hosts that were never meant to be
public.

It works because a favicon is usually deployed with the application, not with the CDN.
The origin, the staging box and the forgotten dev instance all serve the identical file,
and none of them are hidden behind the proxy.

## Install
```bash
pip install mmh3        # Shodan's favicon hash is MurmurHash3 over the base64 of the file
```

## Usage
```bash
python3 - <<'PY'
import urllib.request, base64, mmh3
raw = urllib.request.urlopen("https://example.com/favicon.ico", timeout=20).read()
print("http.favicon.hash:%d" % mmh3.hash(base64.encodebytes(raw)))
PY
```
Then search that hash on a device-search engine - `http.favicon.hash:<value>` on
[Shodan](../../02-network-and-ip/device-search/shodan.md), or the equivalent favicon
filter on [ZoomEye](../../02-network-and-ip/device-search/zoomeye.md) and
[Censys](../../02-network-and-ip/device-search/censys.md).

## Output
A signed 32-bit integer - for example wikipedia.org's favicon hashes to `857403617`.
The search then returns every indexed host serving a byte-identical icon: the CDN edge,
and anything else that ever answered a scanner with the same file.

## Gotchas
- **The encoding must match exactly.** Shodan hashes the base64 of the raw bytes using
  `base64.encodebytes` - which inserts line breaks. Use `b64encode` instead and you get a
  different number and zero results. This is the usual reason the technique "does not
  work".
- **A shared favicon is not proof of a relationship.** Default framework and CMS icons
  are served by millions of hosts; hashing an untouched WordPress or Apache favicon
  returns noise. Check the icon is distinctive before trusting a match.
- Fetching the favicon is **one HTTP request to the target** - ordinary traffic, but not
  nothing. The search itself is passive and the target never sees it.
- Results depend on the scanner having indexed the origin, which needs it to have been
  exposed when the scanner passed. Absence proves nothing.
- A candidate origin still has to be **confirmed** - request the site directly with the
  correct `Host` header and compare the response before calling it the origin.
- Many origins are firewalled to the CDN's ranges and will simply not answer you. That
  is correct configuration, not a failed lookup. See [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [CloudFlair](cloudflair.md) - the certificate route, if you have paid Censys access
- [CloudFail](cloudfail.md) - unproxied subdomains, the other common leak
- [../../06-history-and-archives/ip-whois-history/README.md](../../06-history-and-archives/ip-whois-history/README.md) - the address used before the CDN
