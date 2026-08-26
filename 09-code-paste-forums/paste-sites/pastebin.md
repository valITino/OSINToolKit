---
name: Pastebin
slug: pastebin
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://pastebin.com/
categories: [code-paste-forums, paste-sites]
tags: [pastes, leaks, dumps, monitoring]
status: unverified
status_checked: 2026-08-26
---

# Pastebin

## What question does it answer?
Has data relating to my target - credentials, a customer list, internal
configuration - been posted publicly, and when did it first appear?

## When to reach for it
Paste sites are frequently where leaked data **first surfaces**, before it reaches
forums or breach aggregators. Checking them puts a date on an exposure and sometimes
gives you the raw dump itself. Pastebin is the largest, but the ecosystem matters:
privatebin instances, paaster, and others are used precisely because they are less
monitored.

## Install
```bash
# Nothing to install. Site search is limited - use the approaches below.
```

## Usage
```text
site:pastebin.com "example.com"          # search engines index public pastes
https://psbdmp.ws/                        # third-party archive of past pastes, searchable
```

Scriptable monitoring of new public pastes requires Pastebin's paid scraping API;
the free account cannot poll the firehose.

## Output
Raw text pastes with a creation date and, sometimes, an author handle. The timestamp
is often the most valuable field - it dates the exposure.

## Gotchas
- **Pastes are deleted, expire, or are set unlisted.** What is there today may be gone
  tomorrow - **archive immediately** on finding something relevant
  ([documentation](../../00-methodology/documentation/README.md)).
- Native site search is weak; you will get further through search engines and
  third-party paste archives.
- **Dumps are frequently fake, recycled from old breaches, or deliberately salted.**
  Verify claims against [HIBP](../../08-people-and-identity/email-osint/hibp.md) or the
  data itself before reporting an incident.
- Downloading and holding leaked personal data has legal implications - have a lawful
  basis and handle it accordingly. See [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Have I Been Pwned](../../08-people-and-identity/email-osint/hibp.md) - curated breach data
- [GitHub code search](../code-search/github-code-search.md) - the other place secrets get published
