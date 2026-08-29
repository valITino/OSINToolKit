---
name: ANY.RUN
slug: any-run
tier: 2
contact: active
type: web
cost: freemium
platforms: [web]
url: https://any.run/
categories: [threat-intel, url-analysis]
tags: [sandbox, interactive, phishing, detonation, process-tree]
status: active
status_checked: 2026-08-29
---

# ANY.RUN

## What question does it answer?
I have a URL that only misbehaves for a human. What does it do when somebody
clicks through it - past the CAPTCHA, the password-protected archive, the fake
verification page - and can I drive that session myself rather than hope an
unattended run trips the payload?

## When to reach for it
When the lure requires interaction. Multi-stage phishing, pages that ask the
victim to paste a command, and archives whose password is in the mail body all
defeat an unattended scanner; here you type, scroll and drag files into a live
VM while it records. Check the public submissions feed first - somebody has
usually detonated it already, and reading their run costs the operator nothing.

Use [urlquery.md](urlquery.md) instead when you only need the redirect chain,
IDS hits and blocklist corroboration, or when the URL is sensitive: it is the
only tool here that can keep a submission private. Use [triage.md](triage.md)
for a family name and extracted C2 config.

## Install
```bash
# Nothing to install - a browser-driven SaaS VM. Reading public reports needs no
# account; submitting needs free registration. No free CLI or SDK exists:
# api.any.run/v1/analysis returns 403 without a key, sold only with Enterprise.
```

## Usage
```text
https://app.any.run/submissions   # public feed: filter by hash, URL vs file, verdict, tag, domain, IP, ATT&CK, Suricata SID
https://any.run/report/<sha256>/<task-uuid>   # a public report, readable with no account
https://app.any.run/tasks/<task-uuid>/        # the interactive view - where you drive the VM
https://intelligence.any.run/                 # TI Lookup: IOC pivot; free tier is 20 lookups, then degraded
```

## Output
A live session rather than a static report: a video stream of the desktop you
can interact with while it runs, a verdict banner ("Malicious activity" /
"Suspicious activity" / "No threats detected"), threat name and tags, a process
tree with malicious PIDs and command lines highlighted, a MITRE ATT&CK matrix,
TCP/UDP connections with destination country and port, HTTP and DNS requests,
Suricata alerts, dropped files, extracted configuration, and downloadable text
report, PCAP and TLS keys (5 requests per minute on the free tier). Read
somebody else's report as a recording - and check whether anyone drove it.

## Gotchas
- **The Community (free) tier publishes everything.** The plan table lists
  "Unlimited public analyses" for Community and confines "Private analyses" to
  the paid tiers, and ANY.RUN's own blog says your task will be shared publicly.
  The path, query string, token or victim email in a targeted phishing link
  becomes a permanently browsable public report - the worst trap in this
  directory.
- **60-second VM timeout** on Community, extendable by about four minutes.
  Staged loaders, sleep-heavy droppers and anything waiting on a scheduled task
  never fire, so a free-tier "No threats detected" usually means the clock ran
  out. 16 MB is the maximum file size; larger cannot be submitted at all.
- OS coverage on the free tier is deliberately thin - Windows 10 64-bit,
  Windows 7 32-bit, Android 14 ARM, Ubuntu 22.04.2 - so malware that checks for
  a modern build looks inert on the environments you are allowed.
- No API on Community, so no scripted submission or bulk pull, unlike urlquery
  and Triage. The free Threat Intelligence tier is a teaser: 20 lookups with
  full indicator detail, then analyses without the indicators. Community is also
  a **personal licence** - using it for client or employer casework breaches it.
- Interactivity cuts both ways: an unattended run where nobody clicked through
  the fake CAPTCHA under-detects, and much of the public feed is exactly that.
- Reading the feed is passive; **submitting is active and unusually loud**. The
  VM behaves like a real user, so a single-use link is consumed and the operator
  learns it was caught.

## Alternatives
- [urlquery.md](urlquery.md) - lighter, faster, and can keep a submission private
- [triage.md](triage.md) - malware family and C2 config from the payload
- [urlscan.io](../../04-web-exploration/fingerprinting/urlscan-io.md) - page resources and screenshots, no interaction
