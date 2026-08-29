---
name: Sourcegraph public code search
slug: sourcegraph
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://sourcegraph.com/search
categories: [code-paste-forums, code-search]
tags: [code-search, regex, graphql, cross-repo]
status: active
status_checked: 2026-08-26
---

# Sourcegraph public code search

## What question does it answer?
Does this string - an internal hostname, an API key format, a distinctive function -
appear anywhere in public source code, matched by a **regular expression** rather than a
literal?

## When to reach for it
When [GitHub code search](github-code-search.md) is not expressive enough. Sourcegraph
has a real query language: regular expressions across repositories, structural matching,
and filters like `lang:`, `repo:`, `file:`, and `count:` that compose. Searching for a
pattern - an internal naming convention, a credential shape, a config block - rather
than an exact string is what it is for.

**Its public search is still free and still works without an account**, which is worth
saying because it is widely assumed otherwise. The unauthenticated GraphQL endpoint
also answers, so this is the cross-repo code search you can actually script.

## Install
```bash
# Nothing to install. The web UI needs JavaScript; the API does not.
```

## Usage
```text
https://sourcegraph.com/search?q=context:global+YOUR_QUERY&patternType=standard
```
```bash
curl -s -X POST https://sourcegraph.com/.api/graphql -H 'Content-Type: application/json' \
  -d '{"query":"query{search(query:\"context:global count:20 lang:go internal.example.com\",version:V3){results{matchCount repositories{name}}}}"}'
```

## Output
Matching lines with surrounding context, grouped by repository and file. The GraphQL
response gives `matchCount`, a `limitHit` flag telling you the result set was truncated,
and the repositories involved - check `limitHit` before concluding you have seen
everything.

## Gotchas
- **Coverage is a curated index of public repositories, not all of GitHub.** A query can
  return nothing simply because the repository is not indexed. **Absence is not
  evidence** - cross-check against [GitHub code search](github-code-search.md).
- `count:` defaults low and `limitHit` will be true more often than you expect. Raise it
  deliberately rather than trusting the first page.
- **The web UI requires JavaScript**; scripted collection should go through the GraphQL
  endpoint instead of scraping the page.
- Public search is free; the Enterprise product is a separate, paid offering, and
  Sourcegraph has changed the shape of its public offering before. Re-verify before
  building a workflow that depends on it.
- **Finding a secret is not licence to use it.** This reference covers discovery only.
  Report exposed credentials through the vendor's disclosure process - see
  [../../LEGAL.md](../../LEGAL.md).
- Indexed code is a snapshot. A match may be from a commit long since reverted, and a
  removed secret stays in history - see [git-history](../git-history/README.md).

## Alternatives
- [GitHub code search](github-code-search.md) - broader coverage of GitHub itself
- [searchcode](searchcode.md) - older index, covers some forges GitHub search does not
- [trufflehog](../secret-scanning/trufflehog.md) - verified secret detection over a repo you have
