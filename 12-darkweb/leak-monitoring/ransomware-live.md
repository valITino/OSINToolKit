---
name: Ransomware.live
slug: ransomware-live
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://www.ransomware.live/
categories: [darkweb, leak-monitoring]
tags: [ransomware, extortion, leak-sites, api, negotiations, yara]
status: active
status_checked: 2026-08-29
---

# Ransomware.live

## What question does it answer?
I have a company name, a country or an encrypted-file extension. Has this
organisation been named on a leak site, in which sector, and what do that crew's
ransom note, YARA rule and negotiation transcripts look like?

## When to reach for it
The one to reach for when the question runs past "were they named": beyond the
victim table it publishes ransom notes, negotiation chats, YARA rules, IoCs, a
TTP matrix and SEC Form 8-K filings, which is what a DFIR team can act on when
the victim has only an encrypted file extension to go on. For breadth of crews
and for wallet or torrent pivots [RansomLook](ransomlook.md) covers more; run
both, since each misses posts the other catches.

## Install
```bash
# Nothing to install; the v2 API is anonymous. PRO is also free but gated on
# registration: enter an email at https://www.ransomware.live/my, follow the
# magic link (no password, no payment), then send X-API-KEY to api-pro.
curl -s 'https://api.ransomware.live/v2/info'   # {"groups":393,"victims":31303}
```

## Usage
```bash
curl -s 'https://api.ransomware.live/v2/searchvictims/airbus'
# the call most investigations need: free-text victim search, returning
# activity, attackdate, claim_url, country, data_size, description, group_name
curl -s 'https://api.ransomware.live/v2/countryvictims/CH'
# every claim against an ISO-3166 alpha-2 country, to see whether one claim is
# part of a campaign. Siblings: /v2/sectorvictims/, /v2/groupvictims/, /v2/yara/
curl -s -H "X-API-KEY: $KEY" 'https://api-pro.ransomware.live/iocs/akira'
# PRO-only material v2 lacks; /negotiations/, /ransomnotes/, /8k and /validate
# sit beside it, and a call with no header returns HTTP 401
```

## Output
JSON victim objects: `{activity, attackdate, claim_url, country, data_size,
description, discovered, group_name, post_title, website}`. The docs spell out
the date trap themselves - `attackdate` is an *estimated* attack or publication
date, `discovered` is when the project first saw the listing, so only the second
is an observation you can defend. `description` is the crew's own extortion
blurb. Search the entity, widen to country and sector to place the claim, then
pull the crew's IoCs and note text for the responders.

## Gotchas
- **It did not move to paid.** Both tiers are advertised free and the project
  states it has no paywall; what changed is registration, not money. Do not tell
  a client this now costs money.
- A PRO key means handing an email address to a magic-link login, and the
  operator can correlate it with everything you query. Use a dedicated address.
- v2 documents "1 req/min per endpoint" but did not enforce it in testing; build
  for the documented limit. PRO allows 500,000 calls/month and then returns HTTP
  429, not a partial result, so a per-victim loop over a portfolio burns it.
- **Entries get removed.** One group record states outright that its claims
  could not be verified and its entries were deleted, so absence is not evidence
  of no breach, and month-over-month counts are not a stable trend line.
- Every record carries `claim_url`, a live onion post: reading it here is
  passive, fetching it is **active contact** and lands you in the crew's access
  log. Defang these before a report is forwarded.
- Country and sector are inferred from the domain, so multinationals are filed
  under the wrong country routinely.
- v2 and PRO have overlapping but non-identical paths (`/recentvictims` versus
  `/victims/recent`), and it is a single-maintainer project run outside working
  hours - mirror anything you intend to cite.
- Notes, chats and samples can carry illegal material; downloading it is an
  offence in most jurisdictions whatever your intent, and evidence handling and
  reporting duties apply - [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [RansomLook](ransomlook.md) - more crews tracked, wallet and torrent pivots
- [ransomwatch](ransomwatch.md) - frozen 2020-2025 claims for historical work
- [DarkOwl](darkowl.md) - paid, and reaches beyond RaaS blogs
- [HIBP](../../08-people-and-identity/email-osint/hibp.md) - the credential side
