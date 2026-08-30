---
name: RansomLook
slug: ransomlook
tier: 2
contact: passive
type: web
cost: free
platforms: [web, linux]
url: https://www.ransomlook.io/
categories: [darkweb, leak-monitoring]
tags: [ransomware, extortion, leak-sites, api, attribution]
status: active
status_checked: 2026-08-29
---

# RansomLook

## What question does it answer?
I have an organisation name or domain. Which crew has claimed it, when, and what
else do they publish - without me ever loading their onion blog?

## When to reach for it
First stop when a client, supplier or acquisition target might be named on a
leak site: it mirrors 618 groups and markets to the clearweb behind an open JSON
API, so a check costs one curl and no account, and it is the only free source
publishing torrent-swarm overlap between crews. No ransom notes, YARA rules or
negotiation transcripts - for those use [Ransomware.live](ransomware-live.md).

## Install
```bash
# Hosted service: nothing to install, no key, anonymous curl. No pip/apt/Docker
# package. Self-hosting is Ubuntu 24.04 only: clone valkey-io/valkey and make it
# in a directory SIBLING to the RansomLook clone, then Poetry 2.1.0+, poetry
# install, RANSOMLOOK_HOME in .env, poetry run start. That also makes it ACTIVE:
# your own instance is the thing fetching the leak sites.
```

## Usage
```bash
curl -s 'https://www.ransomlook.io/api/search?q=airbus'
# one search across groups, markets, posts, breaches and notes. Parameter is q
curl -s 'https://www.ransomlook.io/api/posts?days=1'
# lean cron firehose: group, title, discovered only, 2.6 KB a day. Also takes
# ?from=&to= and ?groups=qilin,akira
curl -s 'https://www.ransomlook.io/api/hot/7'
# which crews actually worked this week; use it to test a "group is dead" claim
```

## Output
JSON everywhere, the web UI a thin skin over it. `post_title` is the victim
string as the crew typed it, `discovered` is RansomLook's first observation and
not the attack date, and `screen` is an archived screenshot you can cite without
loading the blog. A group record's `locations[]` marks dead mirrors with
`available: false` beside a 2023 `lastscrape`. Search the entity, then the group
record for mirrors, then `/api/hot/` and `/api/health/` to spot a rebrand shell.

## Gotchas
- **`/api/group/{name}` is enormous** - it inlines base64 screenshots, and qilin
  measured 30,148,261 bytes. Use `/api/posts?days=` in any loop.
- The search parameter is `q`. `?query=airbus` returns HTTP 400 "Query must be
  at least 2 characters" for a six-character string - a misleading error.
- **Every record is an attacker claim.** Crews post fake victims, re-post old
  ones after a rebrand, and name parent companies for subsidiary incidents.
- 618 is the all-time group count; only 336 of 3,248 known group locations were
  online when checked. Do not report it as "active groups".
- Group and health records hand you live onion slugs, and one health record
  returned `ftp://` URLs with embedded credentials pointing at live exfil
  infrastructure. Reading them is passive; curling one is **active contact**,
  and for that host unlawful access. Record it, do not connect.
- Parser contributions go through public GitHub issues, so the victim name or
  onion address that prompted yours becomes a permanent record under your name.
- Illegal material can arrive unbidden in screenshots and samples; downloading
  it is an offence in most jurisdictions whatever your intent, and evidence and
  reporting duties apply - [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Ransomware.live](ransomware-live.md) - ransom notes, YARA, negotiation chats
- [ransomwatch](ransomwatch.md) - frozen 2020-2025 baseline for older claims
- [DarkOwl](darkowl.md) - paid, and reaches markets, forums and Telegram
- [Intelligence X](../onion-discovery/intelligence-x.md) - dumps, by selector
