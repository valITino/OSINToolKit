---
name: Hybrid Analysis (Falcon Sandbox)
slug: hybrid-analysis
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web, linux, macos, windows]
url: https://hybrid-analysis.com/
categories: [threat-intel, file-and-hash]
tags: [sandbox, detonation, behaviour, c2, hash-lookup]
status: active
status_checked: 2026-08-29
---

# Hybrid Analysis (Falcon Sandbox)

## What question does it answer?
I have a file or a hash. Has anyone already detonated it, and what did it do -
which processes, which domains, which C2 - so that I need not run it myself?

## When to reach for it
When a family label is not enough and you need behaviour: the process tree, the
command lines, and above all the `domains` and `hosts` arrays - the operator's
infrastructure, pivotable without sending a packet. The feed and the web hash
search need no account. Not for engine consensus, and not at all when the sample
must stay private.

## Install
Nothing for the feed and the web hash search, which are open. For the API,
register, complete the vetting process, create a key on your profile and send
`api-key: <key>` - the only authentication v2 supports (guides that also set a
`Falcon Sandbox` user agent describe v1). The official client
`PayloadSecurity/VxAPI` was last committed on 2024-01-31; reference code only.

## Usage
```bash
# No key, no account: the recent window of public detonations.
curl -s "https://hybrid-analysis.com/feed?json" \
  | jq '.data[] | {sha256, submitname, vxfamily, threatlevel_human, reporturl}'
# Hash lookup. GET replaced the deprecated POST in v2.35.0; level restricted.
curl -s -H "api-key: $HA_KEY" \
  "https://hybrid-analysis.com/api/v2/search/hash?hash=<md5|sha1|sha256>"
```

## Output
Feed rows and search hits carry the hashes, `submitname`, `environmentId` (the
OS image), `threatscore` 0-100, `threatlevel_human` ("no specific threat",
"suspicious", "malicious"), `avdetect`, `vxfamily`, `tags`, `domains`, `hosts`,
`reporturl`, `sharedanalysis`, `isreliable`, and a `process_list` of uid,
parentuid, name, path and command line. Read `vxfamily` and `threatlevel_human`
for the verdict, `domains` and `hosts` for C2, the process chains for what ran,
then `isreliable` and `sharedanalysis` to judge the row.

## Gotchas
- **The false-negative trap: a sandbox verdict is behavioural, not consensus.**
  One feed row scored 46 ("no specific threat") for a binary that had crashed
  into `WerFault.exe`. Anti-analysis checks, a dead C2 or the wrong environment
  all produce clean-looking reports; confirm the sample ran before trusting a
  score.
- **Everything submitted is public by default**: uploads reach community YARA
  and string search, and "sample not shared" still leaves the metadata indexed.
  Detonation also makes outbound requests as the sample, reaching the operator's
  infrastructure.
- **Two contradictory statements about API keys.** The v2 documentation says
  free non-vetted accounts get restricted search keys; the site's modal says
  vetting is required before any key or sample download. Plan for the stricter
  one; sample and PCAP downloads need `default` level. Quotas are per key and
  unpublished - read the `Api-Limits` header or `GET /api/v2/key/current` first.
- **Endpoint churn silently breaks copied code.** `POST /search/hash` and
  `/feed/latest` are deprecated, and every `/file-collection/*` endpoint has
  returned `410 Gone` since 2026-08-21. The web UI is JavaScript-rendered - curl
  gets a page shell and a reCAPTCHA config - so use the API.
- **The free feed is a rolling window** of recent public detonations - 239
  records in one pull - not the corpus and not history. Absence proves nothing,
  and `avdetect`/`vtdetect` are often empty or `-1` there, not a zero.

## Alternatives
- [MalwareBazaar](malwarebazaar.md) - family, YARA and builder-level pivots
- [Triage](../url-analysis/triage.md) - sandbox reports with extracted configs
- [ANY.RUN](../url-analysis/any-run.md) - interactive detonation you steer
- [MalShare](malshare.md) - where the file was collected, not what it does
