---
name: urlquery
slug: urlquery
tier: 2
contact: active
type: web
cost: free
platforms: [web, linux, macos, windows]
url: https://urlquery.net/
categories: [threat-intel, url-analysis]
tags: [sandbox, phishing, ids, dns-blocklist, pivoting]
status: active
status_checked: 2026-08-29
---

# urlquery

## What question does it answer?
I have a URL I must not click. What does it serve when a real browser opens it,
do any IDS rules or DNS blocklists already call it malicious, and who else has
scanned this domain, IP or ASN - without my browser ever touching it?

## When to reach for it
Search first: the corpus is anonymously searchable and pivots by domain, IP and
ASN, so a URL somebody already scanned costs you nothing and tells the operator
nothing. Submit when you want three independent opinions in one page - urlquery's
own heuristics, Suricata-style network rules, and third-party DNS filters.

Wrong tool when the page needs a human: a CAPTCHA, a fake verification step or a
password-protected archive all under-detect here, and [any-run.md](any-run.md)
exists for that. For a payload rather than a landing page, where you want a
family name and C2 configuration, use [triage.md](triage.md).

## Install
```bash
# Nothing to install: urlquery.net searches and reads reports anonymously.
go install github.com/urlquery/urlquery-cli@latest  # optional CLI, last commit 2025-07-05
urlquery-cli config set apikey <key>                # free key from /user/signup; CLI needs one
```

## Usage
```text
https://urlquery.net/search?q=url.domain:example.com   # passive: find a scan somebody already ran
https://urlquery.net/search?q=ip.addr:104.18.36.248    # pivot every scanned URL that hit this IP
https://urlquery.net/search?q=(tags:phishing OR tags:scam) AND date:[2026-05-01 TO 2026-05-09]
```
```bash
# The ONLY way to keep a submission out of public search. access is public|restricted|private.
curl -H "x-apikey: $UQ_KEY" -X POST https://api.urlquery.net/public/v1/submit/url \
  -d '{"url":"hxxp://evil.example/login","access":"private"}'
```

## Output
A report at `/report/<uuid>`: submitted URL, final URL after redirects, IP and
ASN, tags, and three counters spelled out as urlquery / Network Intrusion
Detection / Threat Detection Systems. Then a host summary, detected
technologies, a table of DNS filters with verdicts ("Cloudflare DNS | host |
malicious | Sinkholed"), HTTP transactions, a screenshot, raw JSON, and Related
reports pivoting by domain, IP, ASN and screenshot. Read the counters as three
independent opinions: high TDS with UQ 0 means the DNS filters already know the
name, not that the sandbox saw anything.

## Gotchas
- **Anonymous web submissions are public.** No account is needed to submit and
  the scan is searchable minutes later, so a URL carrying a victim's email, a
  session token or a password-reset secret gets published. `access: private`
  exists only on the API and CLI - and every API endpoint, search included,
  needs the `x-apikey` header. Only the web UI is anonymous.
- **Wrong field names return 0 hits, not an error** - a silent false negative.
  `domain:` and `url:` are not fields; `url.domain`, `url.fqdn`, `ip.addr`,
  `ip.asn`, `final.url.domain`, `artifacts.files.sha256` and `tags` are.
- An empty anonymous search means nobody scanned it *publicly*; broad searches
  truncate silently on timeout, and reports are kept "for a limited time" with
  no stated period, so this is no archive of record.
- The scanner fetches from urlquery infrastructure with a fixed, dated default
  user-agent (a 2022 Firefox string). Kits that geofence, require a referer or
  fingerprint datacentre ranges serve a decoy, so UQ 0 / IDS 0 / TDS 0 is not
  proof of a clean URL. The API overrides useragent and referer; the form cannot.
- Searching is passive; **submitting is active**. The target logs the visit -
  with urlquery's IP, not yours - and a single-use phishing token dies with it.

## Alternatives
- [triage.md](triage.md) - when you want the malware family and C2 config
- [any-run.md](any-run.md) - when the page only detonates for a human who clicks
- [urlscan.io](../../04-web-exploration/fingerprinting/urlscan-io.md) - larger corpus, richer pivots
