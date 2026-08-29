---
name: GitDorker
slug: gitdorker
tier: 3
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/obheda12/GitDorker
categories: [web-exploration, dorking]
tags: [dorks, github, code-search, triage, unmaintained]
status: stale
status_checked: 2026-08-29
---

# GitDorker

## What question does it answer?
I have an organisation name or a domain. Which of 500-odd secret-shaped GitHub
search patterns return hits when combined with it, so I know where to start
reading?

## Why this is tier 3
It still runs - Python 3.11, three dependencies, a live GitHub endpoint - but
has had no commit since 2021-05-07, no release ever, and is mis-tuned to
today's API: it announces "29 requests per minute allowed" against an endpoint
GitHub documents at 10 per minute, so a full-list run buries hits under
failures. Its README also names a dork file that is not in the repository.

## When to reach for it
When you want a quick sense of which patterns hit at all for an organisation,
driven deliberately: one thread, a short dork list. If you know the pattern
already, query GitHub's code search directly - maintained, and it returns the
matching lines. Judging whether a hit is a live credential needs a scanner.

## Install
```bash
git clone https://github.com/obheda12/GitDorker && cd GitDorker
pip3 install -r requirements.txt   # termcolor, tqdm, requests - runs on Python 3.11
# Needs a *classic* PAT - it sends the old `Authorization: token <PAT>` header,
# which fine-grained tokens do not reliably satisfy.
```

## Usage
```bash
python3 GitDorker.py -t <CLASSIC_PAT> -q example.com -d Dorks/alldorksv3 -o example
# alldorksv3 (513 dorks) - the README's Dorks/alldorks.txt is not in the repo
python3 GitDorker.py -tf tokens.txt -q example.com -d Dorks/medium_dorks.txt -p -e 1 -o example
# -tf rotates tokens, -p hides zero-hit rows, -e 1 keeps one thread, nearer the real 10/min
python3 GitDorker.py -tf tokens.txt -org exampleorg -d Dorks/alldorksv3 -ri -o exampleorg
# scope to an org rather than free text; -ri sorts result URLs most-recently-indexed
```

## Output
One line per dork - `[+] (N) DORK = <dork> | https://github.com/search?...` for
hits, `[#] (0)` for none, `[-] <url>` for a failed request. Read it as a triage
index, not evidence: `(N)` is the API's `total_count`, and GitDorker never
downloads a matched file, path or line. Sort by N, discard the thousands (a
generic term, not a leak), open the few low-count URLs, then verify each.

## Gotchas
- **The rate limit is wrong by roughly 3x.** GitHub documents `/search/code`
  at 10 requests per minute; GitDorker computes `(tokens x 30) - 1`. A failed
  dork means the same as a zero-hit one: you learned nothing about it.
- **`-lb/--limitbypass` exists to exceed per-token limits with tokens from
  separate accounts.** GitHub's acceptable use policies forbid excessive
  automated bulk activity and reserve suspension, so it risks those accounts.
  See [../../LEGAL.md](../../LEGAL.md).
- The count and the link come from two different indexes: `total_count` is the
  legacy REST index (default branch, files under 384 KB) while the printed URL
  opens current code search, which also drops vendored and generated files.
  Expect the browser to show a different number.
- Every result URL needs you signed in to GitHub: code search is unavailable
  logged out even for public repositories, so you get a login wall, not zero.
- A high count is nearly always a false lead: `access_token` against a common
  domain matches documentation, fixtures and vendored samples. It finds
  strings, not secrets.

## Alternatives
- [github-code-search](../../09-code-paste-forums/code-search/github-code-search.md) - the same index, maintained
- [grep.app](../../09-code-paste-forums/code-search/grep-app.md) - cross-host code search, no token
- [trufflehog](../../09-code-paste-forums/secret-scanning/trufflehog.md) - confirms a live credential
- [pagodo](pagodo.md) - the same idea against web search engines
