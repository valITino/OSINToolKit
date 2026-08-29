---
name: OSINT Cabal Live Center
slug: osintcabal
tier: 3
contact: passive
type: web
cost: free
platforms: [web]
url: https://osintcabal.org/livecenter/live.html
categories: [resources, awesome-lists]
tags: [hosted-tools, email-osint, username, breaches, community]
status: unverified
status_checked: 2026-08-29
---

# OSINT Cabal Live Center

## What question does it answer?
I have a selector - an email, a username, a domain - and no working install of
the usual tools. Is there a hosted instance I can run it through right now?

## Why this is tier 3
It is convenience infrastructure, not a tool of its own. The Live Center hosts
web front-ends for other people's tools (Holehe, Zehef, theHarvester, subdomain
and breach lookups, platform-specific suites for Telegram, TikTok, Reddit,
Instagram, Mastodon and Bluesky), grouped into kits. Everything it runs is
documented here in its own right, and running it locally is both faster and
safer. The reason to keep the bookmark is the machine that is not yours: a
loaner laptop, a locked-down corporate build, a phone.

## Install
```bash
# Nothing to install - a hosted set of web front-ends. An onion mirror exists.
```

## Usage
```text
https://osintcabal.org/livecenter/live.html    # the hub; pick a category, paste a selector
# Categories: email OSINT, domain and URL, breaches and leaks,
# platform-specific suites, public data, and bundled multi-tool kits.
```

## Output
Whatever the underlying tool produces, rendered in the browser. Because the
tools are third-party, the result formats vary and rarely match what the same
tool prints locally, so do not treat a screenshot of it as tool output in a
report - re-run the tool yourself for anything you will rely on.

## Gotchas
- **Every selector you type goes to somebody else's server.** The operator sees
  the email, username, or domain you are investigating, and so does anyone who
  compromises the host. For sensitive casework this is disqualifying; run
  [holehe](../../08-people-and-identity/email-osint/holehe.md) or
  [theHarvester](../../01-orchestrators/aggregators/theharvester.md) locally.
- Hosted instances lag upstream. A breakage in a tool here may be a stale
  deployment rather than a real result, and you cannot tell which.
- Which tools are present, and whether they work, changes without notice. It is
  one volunteer-run site, not a maintained service with an SLA.
- Some of the front-ends query paid APIs behind the scenes; blanks may mean an
  expired key rather than no data.

## Alternatives
- [awesome-lists README](README.md) - curated lists, when you want the exhaustive dump
- [holehe](../../08-people-and-identity/email-osint/holehe.md) - the email check, run locally
- [Maigret](../../08-people-and-identity/username-enum/maigret.md) - username sweep, run locally
- [SpiderFoot](../../01-orchestrators/recursive-scanners/spiderfoot.md) - one hosted UI you control
