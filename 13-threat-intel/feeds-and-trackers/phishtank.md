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
phish submitted at 21:09Z and community-verified at 21:11Z - but the platform is
frozen. `register.php` says "New user registration temporarily disabled", so you
cannot get an account, an application key, or the ability to submit or vote, and
the published statistics stop at May 2017. The feed carries only
verified-and-still-online phish, with no history. That makes it a situational
cross-check: for a live phishing feed use OpenPhish's free community feed
(https://openphish.com/feed.txt), for malware distribution URLs
[URLhaus](urlhaus.md), and to report a site Netcraft
(https://report.netcraft.com/report) or APWG (reportphishing@apwg.org).

## When to reach for it
As a cheap second opinion on one URL, or when you want the impersonated brand
named for you - `target` is the field worth coming for, because it tells you
which campaign you are in. Never to prove a URL is clean, or for history.

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

# Browser view of active submissions still awaiting votes - the invisible queue:
# https://phishtank.org/phish_search.php?verified=u&active=y
```

## Output
Rows of phish_id, url, phish_detail_url, submission_time, verified,
verification_time, online and target, plus ip_address, cidr_block,
announcing_network and rir; the lookup API answers narrower, with in_database,
phish_id, verified, verified_at and valid. Read `target` as the pivot - it is
the impersonated brand, so it names the campaign - and `announcing_network` to
jump to the hosting provider. Read `verified` as "a quorum of volunteers voted",
not as a laboratory finding.

## Gotchas
- **You cannot register**, so no application key, no submitting and no voting.
  Anything telling you to sign up for a key is out of date.
- **Keyless access is throttled**: the lookup API reported a limit of 250 per
  300 seconds, and unkeyed bulk downloads are limited to a few per day. Over the
  limit returns HTTP 509, and abuse gets you firewalled.
- **The feed is verified AND online only.** On 2026-08-29 there were 115,280
  online submissions but 73,870 verified - some 41,000 live phishing URLs in the
  vote queue, invisible to the export. A miss means "not verified yet, or
  already taken down", never "not phishing".
- **There is no history.** 4.29 million phish have been verified over the
  project's life, but the file only holds the ~74k currently online - it cannot
  answer "was this URL phishing last March".
- **URLs are matched as exact strings.** A campaign that rotates one path or
  query parameter gets a new phish_id, so also check the bare domain.
- **Submissions are fully public**, each with a screenshot and vote history on
  its own detail page - relevant only if you hold a legacy account.
- **Three hostnames are in play**: phishtank.org serves the site, detail links
  point at www.phishtank.com, and the dumps redirect to a signed CloudFront URL
  on data.phishtank.com, so follow redirects and never hardcode that URL.
  `phish_detail.php` returns 403 to scripted clients - read it in a browser.

## Alternatives
- [URLhaus](urlhaus.md) - malware distribution URLs, the other half of this
- [urlQuery](../url-analysis/urlquery.md) - what the page serves, and to whom
- [ANY.RUN](../url-analysis/any-run.md) - a human clicking through the flow
- [VirusTotal](../../02-network-and-ip/reputation/virustotal.md) - multi-vendor
  URL verdicts on the same artifact
