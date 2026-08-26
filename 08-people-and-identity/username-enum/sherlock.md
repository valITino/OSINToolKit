---
name: Sherlock
slug: sherlock
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/sherlock-project/sherlock
categories: [people-and-identity, username-enum]
tags: [username, accounts, social-media, enumeration]
status: unverified
status_checked: 2026-08-26
---

# Sherlock

## What question does it answer?
I have a username. Which of hundreds of sites has an account registered under it?

## When to reach for it
The standard first move on a handle. Sherlock checks a large list of sites in
parallel and reports where the name exists, which turns one alias into a map of a
subject's online presence. It is fast, well-maintained, and produces clean output.
Use [Maigret](maigret.md) when you want more sites and profile content extracted
rather than a bare hit list.

## Install
```bash
pipx install sherlock-project
```

## Usage
```bash
sherlock someusername                          # check one username across all sites
sherlock user1 user2 --timeout 10               # several at once, with a per-site timeout
sherlock someusername --csv --folder-output ./out   # save structured results
```

## Output
A line per hit with the site name and the profile URL, written to a per-username text
file (plus CSV with `--csv`). Only claimed accounts are listed by default.

## Gotchas
- **False positives are routine.** Sites that return a 200 for any profile path, or
  that show a custom error page, produce phantom hits. **Open and confirm every URL
  manually** before treating it as a finding.
- **Active**: it requests a profile page from every site in the list, from your IP.
  Consider a VPN or proxy ([OPSEC](../../00-methodology/opsec/README.md)), and note
  that a burst of requests can trigger rate limiting or CAPTCHAs.
- The same username on two sites is not proof of the same person - common handles are
  reused by unrelated people. Corroborate with content, avatars, or writing style.
- Sites change their responses constantly; an out-of-date install produces more
  errors. Update before a real run.

## Alternatives
- [Maigret](maigret.md) - more sites, extracts profile detail
- [holehe](../email-osint/holehe.md) - the same question from an email address
- [WhatsMyName] - the community-maintained detection ruleset several tools build on
