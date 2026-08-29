---
name: PhishTank
slug: phishtank
tier: 3
contact: passive
type: web
cost: free
platforms: [linux, macos, windows, web]
url: https://phishtank.org/
categories: [threat-intel, feeds-and-trackers]
tags: [phishing, brand-impersonation, community-verified, bulk-export, talos]
status: active
status_checked: 2026-08-29
---

# PhishTank

## What question does it answer?
I have a URL that looks like a credential-harvesting page. Is it already in the
community phishing corpus as verified and still online, and which brand was it
impersonating?

## Why this is tier 3
The data is alive - Cisco Talos operates it, and on 2026-08-29 the dump held a
phish submitted at 21:09Z and verified at 21:11Z - but the platform is frozen.
`register.php` says "New user registration temporarily disabled", so there is no
account, no application key, no submitting and no voting, whatever older guides
say, and the published statistics stop at May 2017. For a live phishing feed use
OpenPhish (https://openphish.com/feed.txt); report sites to Netcraft
(https://report.netcraft.com/report) or APWG (reportphishing@apwg.org).

## When to reach for it
As a cheap second opinion on one URL, or to get the impersonated brand named for
you - `target` tells you which campaign you are in. Never to prove a URL clean.

## Install
```bash
# Nothing to install: two HTTP endpoints, both keyless on 2026-08-29.
```

## Usage
```bash
UA="phishtank/yourname"     # a descriptive User-Agent is required in practice
# Single-URL lookup. url must be urlencoded; format is xml|php|json.
curl -s -A "$UA" -X POST https://checkurl.phishtank.com/checkurl/ \
  -d "url=https%3A%2F%2Fexample.com%2Flogin&format=json"
# The whole verified-and-online corpus: 14 MB, 73,873 rows, rebuilt hourly.
curl -sL -A "$UA" -o verified_online.csv \
  http://data.phishtank.com/data/online-valid.csv
```

## Output
Rows of phish_id, url, phish_detail_url, submission_time, verified,
verification_time, online, target, ip_address, cidr_block, announcing_network
and rir; the lookup API answers narrower. `target` is the pivot - the
impersonated brand names the campaign - and `announcing_network` gives the
hosting provider. Read `verified` as "a quorum of volunteers voted", no more.

## Gotchas
- **Keyless access is throttled**: the lookup API reported a limit of 250 per
  300 seconds, and unkeyed bulk downloads a few per day. Over the limit returns
  HTTP 509, and abuse gets you firewalled.
- **The feed is verified AND online only, and has no history.** On 2026-08-29
  there were 115,280 online submissions but 73,870 verified - some 41,000 live
  phishing URLs sat in the vote queue, invisible to the export. 4.29 million
  phish have been verified over the project's life; the file holds only the ~74k
  online now. A miss is "not verified yet, or taken down", never "not phishing".
- **URLs are matched as exact strings.** A campaign that rotates one path or
  query parameter gets a new phish_id, so also check the bare domain.
- **Submissions are fully public**, each with a screenshot and vote history on
  its own detail page - relevant only if you hold a legacy account.
- **Follow redirects, hardcode nothing**: phishtank.org serves the site, detail
  links point at www.phishtank.com, and the dumps redirect to a signed
  CloudFront URL. `phish_detail.php` returns 403 to scripted clients.

## Alternatives
- [URLhaus](urlhaus.md) - malware distribution URLs, the other half of this
- [urlQuery](../url-analysis/urlquery.md) - what the page serves, and to whom
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - multi-vendor
  verdicts when one community vote is not enough
