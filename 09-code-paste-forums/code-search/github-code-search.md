---
name: GitHub code search
slug: github-code-search
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://github.com/search
categories: [code-paste-forums, code-search]
tags: [code-search, secrets, dorking, repositories]
status: unverified
status_checked: 2026-08-26
---

# GitHub code search

## What question does it answer?
Does this organisation's name, domain, internal hostname, or API key appear anywhere
in public source code?

## When to reach for it
One of the highest-yield passive searches available, because developers commit things
they should not and GitHub indexes them immediately. Searching for a target's domain
or internal hostnames routinely surfaces configuration files, deployment scripts, and
credentials from employees' personal repositories - material that exists in no other
source. Fully passive: you query GitHub, never the target.

## Install
```bash
# Web search needs only an account. The gh CLI and API allow scripted queries.
```

## Usage
```text
"example.com" language:yaml            # config files mentioning the domain
org:example-inc filename:.env           # environment files in the org's repos
"internal.example.com" NOT is:fork      # internal hostnames, excluding forks
"api.example.com" path:*.json
```

## Output
Matching code with the surrounding lines, the repository, and the file path. Follow
the repository through to its commit history - see
[../git-history/README.md](../git-history/README.md), since the author's email is
often as valuable as the code.

## Gotchas
- **Code search requires being signed in**, and rate limits apply - use a token for
  scripted queries. See [../../99-resources/api-keys/README.md](../../99-resources/api-keys/README.md).
- The index reflects current file contents. **Secrets removed from HEAD still live in
  history and will not appear here** - clone the repo and run
  [TruffleHog](../secret-scanning/trufflehog.md) to find those.
- **Never test a discovered credential.** Using it is unauthorised access regardless
  of how it was published. Record it and report it.
- Forks and mirrors inflate results; exclude them to see the real source.

## Alternatives
- [TruffleHog](../secret-scanning/trufflehog.md) - full history, with verification
- [SearchCode](searchcode.md) - other forges, tier 3
- grep.app, Sourcegraph - alternative cross-repository code search
