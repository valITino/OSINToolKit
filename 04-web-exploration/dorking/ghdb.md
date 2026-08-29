---
name: Google Hacking Database
slug: ghdb
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://www.exploit-db.com/google-hacking-database
categories: [web-exploration, dorking]
tags: [dorks, patterns, exposure, curated]
status: active
status_checked: 2026-08-29
---

# Google Hacking Database

## What question does it answer?
What should I actually search for? Someone has already worked out the query that
surfaces exposed backups, login panels, or config files - what is it?

## When to reach for it
When you know the operators but not the pattern. The
[operator list](README.md) tells you *how* to phrase a query; the GHDB is a curated
corpus of queries that are known to work, contributed and categorised over two decades -
directory listings, files containing credentials, error messages that leak paths, login
portals, and pages exposing network or device information.

Use it as a source of shapes to adapt, not as a script to run. Take a pattern, scope it
to your target with `site:`, and read what comes back.

## Install
```bash
# Nothing to install - browse or search the database on Exploit-DB.
```

## Usage
```text
https://www.exploit-db.com/google-hacking-database
  Filter by category, then adapt the dork to your scope:
  <ghdb pattern> site:example.com
```

## Output
Each entry gives the dork itself, a category, the date it was submitted, and the author.
The date matters: an entry from 2011 may reference software nobody runs, and the
phrasing may predate changes in how the engine handles operators.

## Gotchas
- **Always add `site:` to scope it.** An unscoped GHDB dork searches the whole web and
  returns other people's exposed systems. Looking at those is not covered by your
  authorisation, and some of it you would rather not have in your history.
- **Many entries are stale.** They were written against software versions and URL
  patterns that have moved on. Expect a lot to return nothing; that is not a finding.
- **A hit means a page is indexed, not that a system is vulnerable.** This reference
  covers discovery only - confirming exposure is one thing, acting on it is a different
  activity with different authorisation. See [../../LEGAL.md](../../LEGAL.md).
- The GHDB is Google-shaped. Operators differ on Bing and DuckDuckGo, and a dork copied
  verbatim often needs rewriting - which is itself a reason to try more than one engine.
- Running many dorks by hand in quick succession will get you a CAPTCHA. That friction is
  deliberate; see [pagodo](pagodo.md) for what automating it costs you.
- Some categories index pages exposing credentials. Finding one does not entitle you to
  use it; report it through the operator's disclosure channel.

## Alternatives
- [Dorking by hand](README.md) - the operators, and why manual beats automated
- [pagodo](pagodo.md) - runs GHDB dorks at scale, with the blocking problem that implies
- [PublicWWW](../../06-history-and-archives/analytics-linking/publicwww.md) - search page source rather than the index
