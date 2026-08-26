---
name: grep.app
slug: grep-app
tier: 2
contact: passive
type: web
cost: free
platforms: [web, linux, macos, windows]
url: https://grep.app/
categories: [code-paste-forums, code-search]
tags: [code-search, regex, github, mcp]
status: active
status_checked: 2026-08-26
---

# grep.app

## What question does it answer?
Does this exact string - an internal hostname, a key prefix, an employee address -
appear in any public GitHub repository, or anywhere in **this organisation's** repos?

## When to reach for it
For speed and for the org sweep. grep.app searches over a million pre-indexed public
GitHub repositories as literal text, and returns results faster than GitHub's own
search. Its `repo` filter matches partially, so `targetorg/` sweeps every repository an
organisation owns in one query - which is the pivot that turns "they have a GitHub
presence" into a list of leaked internal hostnames.

It also searches **any** public repo on demand at `grep.app/<owner>/<repo>`, including
ones outside the pre-built index, which is the way to get current content for a
specific target.

## Install
```bash
# Nothing to install - free, no account. Scriptable via its MCP endpoint.
```

## Usage
```text
https://grep.app/search?q=internal.example.com     # toggles: match case, whole words, regex
https://grep.app/targetorg/somerepo                 # on-demand search of one repo
```
```bash
curl -sS -X POST https://mcp.grep.app -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"searchGitHub",
       "arguments":{"query":"internal.example.com","repo":"targetorg/"}}}'
```

## Output
Matching lines with file path, repository, licence, and line-numbered context. The MCP
`searchGitHub` tool takes `query` plus optional `matchCase`, `matchWholeWords`,
`useRegexp`, `repo`, `path`, and `language`.

## Gotchas
- **The web UI and its old `/api/search` endpoint sit behind a bot challenge** and return
  429 to scripted clients from datacenter addresses. The MCP endpoint above is not
  challenged and is the reliable programmatic route - a `BLOCKED` result from a link
  checker here means nothing.
- **It matches literal code, not keywords.** `useState(` works; "how to use react" does
  not. Search for the string as it would appear in a file.
- **Regex is Go/RE2**: no backreferences, no lookarounds. Prefix `(?s)` to make `.`
  match newlines. A PCRE pattern may fail silently rather than error.
- **Public GitHub only** - no GitLab, Bitbucket, Codeberg, or **gists**. Gists are a
  common accidental-disclosure route, so this is a real blind spot for leak hunting.
- **It is a live index, not an archive.** Content that was force-pushed or deleted is
  gone. A secret committed and then scrubbed will not appear here - see
  [git-history](../git-history/README.md).
- Index freshness is not published, and the million-repo figure is the pre-indexed set.
  Use the per-repo route when currency matters.
- **Finding a secret is not licence to use it.** Report exposures through the vendor's
  disclosure process - see [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [GitHub code search](github-code-search.md) - authoritative for GitHub, richer filters
- [Sourcegraph](sourcegraph.md) - structural search and a scriptable GraphQL API
- [trufflehog](../secret-scanning/trufflehog.md) - verified secret detection over a repo you hold
