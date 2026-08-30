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
clicks through the CAPTCHA or the fake verification page, and can I drive that
session myself rather than hope an unattended run trips the payload?

## When to reach for it
When the lure requires interaction. Multi-stage phishing, pages that ask the
victim to paste a command, and archives whose password is in the mail body all
defeat an unattended scanner; here you type, scroll and drag files into a live
VM while it records. Check the public submissions feed first - somebody has
usually detonated it already, and reading their run costs the operator nothing.
Use [urlquery](urlquery.md) for a redirect chain, IDS hits and blocklist
corroboration, or for a sensitive URL - it is the only tool here that can keep a
submission private; [Recorded Future Triage (tria.ge)](triage.md) gives a family name and C2 config.

## Install
```bash
# Nothing to install - a browser-driven SaaS VM. Reading public reports needs no
# account; submitting needs free registration. There is no free CLI or SDK.
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
can drive while it runs, a verdict banner ("Malicious activity" / "Suspicious
activity" / "No threats detected"), threat name and tags, a process tree with
malicious PIDs and command lines, a MITRE ATT&CK matrix, TCP/UDP connections,
HTTP and DNS requests, Suricata alerts, dropped files, extracted config, and
downloadable text report, PCAP and TLS keys (5 requests per minute free). Read
somebody else's report as a recording, and check whether anyone drove it.

## Gotchas
- **The Community (free) tier publishes everything.** The plan table gives
  Community "Unlimited public analyses" and confines "Private analyses" to paid
  tiers. The path, query string, token or victim email in a targeted phishing
  link becomes a permanently browsable public report - the worst trap here.
- **60-second VM timeout** on Community, extendable by about four minutes.
  Staged loaders and sleep-heavy droppers never fire, so a free-tier "No
  threats detected" usually means the clock ran out. Maximum file size is 16 MB.
- OS coverage on the free tier is deliberately thin - Windows 10 64-bit,
  Windows 7 32-bit, Android 14 ARM, Ubuntu 22.04.2 - so malware that checks for
  a modern build looks inert on the environments you are allowed.
- No API on Community: `api.any.run/v1/analysis` 403s without an Enterprise key,
  so no scripted submission or bulk pull, unlike urlquery and Triage. Free TI
  Lookup gives 20 lookups with indicator detail, then analyses without them.
  Community is a **personal licence**: client or employer casework breaches it.
- Interactivity cuts both ways: an unattended run where nobody clicked through
  the fake CAPTCHA under-detects, and much of the public feed is exactly that.
- Reading the feed is passive; **submitting is active and unusually loud** - the
  VM acts like a real user, consuming a single-use link and telling the operator
  it was caught.

## Alternatives
- [urlquery](urlquery.md) - lighter, faster, keeps a submission private
- [Recorded Future Triage (tria.ge)](triage.md) - malware family and C2 config from the payload
- [urlscan.io](../../04-web-exploration/fingerprinting/urlscan-io.md) - page resources and screenshots, no interaction
