---
name: ransomwatch
slug: ransomwatch
tier: 3
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/joshhighet/ransomwatch
categories: [darkweb, leak-monitoring]
tags: [ransomware, leak-sites, archived, historical, dataset]
status: archived
status_checked: 2026-08-29
superseded_by: ransomlook
---

# ransomwatch

## What question does it answer?
I need a baseline. What did the leak-site ecosystem look like before mid-2025,
and where do I get a free, citable, timestamped record of claims going back to
2020 with no vendor in the chain of custody?

## Why this is tier 3
The repository was archived by its owner on 3 March 2026, and collection had
already stopped on 16 June 2025 - roughly nine months of apparent life after the
last real update. Worse, the JSON feed URLs that every blog post and cheat sheet
still cites (`ransomwhat.telemetry.ltd/posts` and `/groups`) now return HTTP 302
to an HTML notice page, so a script that does not check the content type will
ingest markup as data. Use [RansomLook](ransomlook.md) for anything current, and
[Ransomware.live](ransomware-live.md) beside it. The only reason this file still
exists is the frozen dataset: 16,072 claims across 157 groups, 2020-01-12 to
2025-06-16, Unlicense, verifiable offline. Take the file, not the project.

## Install
```bash
# Nothing to install for the data - it is one HTTP GET from the frozen repo.
# The project never was a package: you forked it and let GitHub Actions run it,
# with service containers supplying Tor and a geckodriver renderer. The clone
# still runs, but the parsers were last exercised in June 2025, so expect to
# rewrite them before you get a single new post.
```

## Usage
```bash
curl -s -o rw-posts.json \
  'https://raw.githubusercontent.com/joshhighet/ransomwatch/main/posts.json'
# the only thing still worth fetching: 16,072 frozen claims, 2.3 MB, HTTP 200
jq -r '.[]|select(.group_name=="akira")|[.discovered,.post_title]|@tsv' \
  rw-posts.json   # historical baseline for one crew, straight from the file
curl -s -o rw-groups.json \
  'https://raw.githubusercontent.com/joshhighet/ransomwatch/main/groups.json'
# the mid-2025 group-to-onion-mirror map: resolves an old address from a
# 2023-2024 incident without ever contacting the mirror
```

## Output
`posts.json` is a flat array of `{post_title, group_name, discovered}` - no
editorialising, which is exactly why it was called the transparent tracker.
`groups.json` maps each crew to the onion locations it was using. Read it as a
control set: to state that a crew first appeared on a given date, or that a
victim was claimed twice three months apart, this is free, offline and needs no
key. After 2025-06-16 it is silent, and silence here means the scraper stopped,
never that nothing happened.

## Gotchas
- **Archived, and deader than it looks.** Presenting this output as current
  means presenting a feed that stopped fourteen months before you ran it.
- The old API hosts 302 to HTML. Any runbook still citing them is broken, and a
  script without a content-type check will not notice.
- **Running your own fork is active contact** - the scraper fetches the crews'
  onion sites directly over Tor, which is the opposite of what this directory is
  for and is defensible only with a mandate and an opsec plan.
- Parser rot: mirrors rotate constantly, so a fork returns mostly empty results
  and a false sense of coverage. Coverage was never complete either - 157 groups
  in the frozen file against the 393 and 618 tracked live today - so never use
  it to argue that a crew or a victim did not exist.
- `discovered` is when the cron happened to look, and the cron had outages, so
  gaps in the timeline are scraper gaps rather than quiet periods. Victim
  strings are unnormalised attacker text; joining them to a register is manual.
- Mirror the raw JSON now: `raw.githubusercontent.com` is the last delivery
  path, and nobody is maintaining it.
- The corpus names real victims and lists criminal infrastructure; handling,
  disclosure and reporting duties apply - [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [RansomLook](ransomlook.md) - the live successor, free API, more crews
- [Ransomware.live](ransomware-live.md) - live, with notes, YARA and IoCs
- [DarkOwl](darkowl.md) - paid, keeps stored copies of removed content
