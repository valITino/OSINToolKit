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
I have a file or a hash. Has anyone already detonated it, and what did it
actually do - which processes, which domains, which C2 - so that I do not have
to run it myself?

## When to reach for it
When a family label is not enough and you need behaviour: the process tree, the
command lines, and above all the `domains` and `hosts` arrays, a ready-made list
of the operator's infrastructure you can pivot on without sending it a packet.
The feed and the web hash search need no account, so checking costs nothing.

Reach elsewhere for the other questions - [MalwareBazaar](malwarebazaar.md) for
family and campaign correlation, [Triage](../url-analysis/triage.md) for an
extracted configuration rather than a behaviour log, VirusTotal for engine
consensus - and not at all when the sample must stay private.

## Install
Nothing to install for the two things you need most - the public feed and the
web hash search are open. For the API: register, complete the vetting process,
create a key on your profile, and send `api-key: <key>`, which the v2 docs give
as the only supported authentication (guides that also set a `Falcon Sandbox`
user agent describe v1). The official client `PayloadSecurity/VxAPI` still
installs but was last committed on 2024-01-31; treat it as reference code.

## Usage
```bash
# No key, no account: the recent window of public detonations.
curl -s "https://hybrid-analysis.com/feed?json" \
  | jq '.data[] | {sha256, submitname, vxfamily, threatlevel_human, reporturl}'

# Hash lookup. GET replaced the deprecated POST in v2.35.0; level restricted.
curl -s -H "api-key: $HA_KEY" \
  "https://hybrid-analysis.com/api/v2/search/hash?hash=<md5|sha1|sha256>"

# Aggregated cross-report overview for one sha256; level restricted.
curl -s -H "api-key: $HA_KEY" \
  "https://hybrid-analysis.com/api/v2/overview/<sha256>"
```

## Output
Feed rows and search hits carry md5/sha1/sha256, `submitname`, size, type,
`environmentId` and its description ("Windows 11 64 bit", "Android Static
Analysis"), `analysis_start_time`, `threatscore` 0-100, `threatlevel_human`
("no specific threat", "suspicious", "malicious"), `avdetect`, `vxfamily`,
`tags`, `domains`, `hosts`, `ssdeep`, `reporturl`, `sharedanalysis`,
`isreliable`, and a `process_list` of uid, parentuid, name, path and command
line. Read `vxfamily` and `threatlevel_human` for the verdict, `domains` and
`hosts` as your C2 candidate list, the parent/child chains for what executed,
then `isreliable` and `sharedanalysis` to judge whether the row is worth
anything at all.

## Gotchas
- **The false-negative trap: a sandbox verdict is behavioural, not consensus.**
  One live feed row scored 46 as "no specific threat" for a binary whose whole
  process list was itself spawning `WerFault.exe` - it crashed. Anti-analysis
  checks, missing dependencies, a dead C2 or the wrong environment all produce
  clean-looking reports. Confirm the sample ran before reading a low score.
- **Everything submitted is public by default** - uploads are made available to
  community YARA and string search, and flagging a report "sample not shared"
  still leaves the metadata indexed. The sandbox also makes outbound requests as
  the sample, so detonation reaches the operator's infrastructure.
- **Two contradictory statements about API keys.** The v2 documentation says
  free non-vetted accounts get restricted search keys; the site's own modal says
  vetting is required before any key or sample download. Plan for the stricter
  one, and note that sample and PCAP downloads need `default` level either way.
- **Endpoint churn silently breaks copied code.** `POST /search/hash` and
  `/feed/latest` are deprecated, and every `/file-collection/*` endpoint has
  returned `410 Gone` since 2026-08-21. Check the changelog, not a tutorial.
- **The web UI is JavaScript-rendered**: curl on `/sample/<sha256>` returns a
  page shell and a reCAPTCHA config. Use the API; do not build a scraper.
- **The free feed is a rolling window** of recent public detonations - 239
  records in one pull - not the corpus and not history. Absence proves nothing,
  and `avdetect`/`vtdetect` are often empty or `-1` there - not a zero.
- **Quotas are per key and unpublished**: read the `Api-Limits` response header
  or `GET /api/v2/key/current` before any loop.

## Alternatives
- [MalwareBazaar](malwarebazaar.md) - family, YARA and builder-level pivots
- [Triage](../url-analysis/triage.md) - sandbox reports with extracted configs
- [ANY.RUN](../url-analysis/any-run.md) - interactive detonation you steer
- [MalShare](malshare.md) - where the file was collected, not what it does
