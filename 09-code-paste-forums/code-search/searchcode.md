---
name: SearchCode
slug: searchcode
tier: 3
contact: passive
type: web
cost: free
platforms: [web]
url: https://searchcode.com/
categories: [code-paste-forums, code-search]
tags: [code-search, multi-forge, legacy]
status: unverified
status_checked: 2026-08-26
superseded_by: github-code-search
---

# SearchCode

## What question does it answer?
Does this string appear in public source code across several forges - not just
GitHub, but Bitbucket, GitLab, SourceForge and others?

## Why this is tier 3
Its distinguishing feature is genuine: it indexes **multiple forges**, so it can
surface code that GitHub-only searches miss, including older projects on hosts that
have since faded. But its index freshness and coverage do not match
[GitHub code search](github-code-search.md), which is where the overwhelming majority
of current code and current leaks live. Treat SearchCode as a supplementary sweep for
older or non-GitHub material rather than a primary tool.

## Install
```bash
# Nothing to install - web search with an API.
```

## Usage
```text
https://searchcode.com/?q=internal.example.com     # search across indexed forges
```

## Output
Matching code snippets with the repository, file path, and source forge.

## Gotchas
- **Index freshness and completeness vary** - a negative result says little. Always
  run GitHub code search as well.
- Coverage of forges has changed over time; verify the current index scope before
  concluding a forge was searched.
- **Never test a credential you find.** Record and report it - see
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [GitHub code search](github-code-search.md) - the primary tool
- [TruffleHog](../secret-scanning/trufflehog.md) - full history and verification
- grep.app, Sourcegraph - other cross-repository search options
