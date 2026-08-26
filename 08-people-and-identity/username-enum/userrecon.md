---
name: userrecon
slug: userrecon
tier: 3
contact: active
type: cli
cost: free
platforms: [linux]
url: https://github.com/issamelferkh/userrecon
categories: [people-and-identity, username-enum]
tags: [username, legacy, outdated]
status: stale
status_checked: 2026-08-26
superseded_by: sherlock
---

# userrecon

## What question does it answer?
Which social platforms have an account under this username?

## Why this is tier 3
**Outdated.** userrecon checks a small, hard-coded list of sites with a simple shell
approach, and site detection logic goes stale quickly as platforms change their
responses to missing profiles. The result is a high false-positive and false-negative
rate compared with current tools.

[Sherlock](sherlock.md) covers many times more sites and is actively maintained;
[Maigret](maigret.md) goes further and extracts profile content. There is no reason to
choose userrecon for new work - it is listed so you recognise it as superseded when
you meet it in older material.

## Install
```bash
git clone https://github.com/issamelferkh/userrecon.git
cd userrecon && bash userrecon.sh
```

## Usage
```bash
bash userrecon.sh          # prompts for the username, then checks its site list
```

## Output
A per-site found/not-found list written to a text file.

## Gotchas
- **Detection logic is stale** - both false positives and missed accounts are common.
  Verify every hit by hand, which erodes the point of automating it.
- Its site list is small and fixed; platforms that matter today may be absent
  entirely.
- Active: it requests profile pages from your IP, like any enumerator
  ([OPSEC](../../00-methodology/opsec/README.md)).

## Alternatives
- [Sherlock](sherlock.md) - the direct replacement
- [Maigret](maigret.md) - more sites plus profile extraction
