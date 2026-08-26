---
name: feroxbuster
slug: feroxbuster
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/epi052/feroxbuster
categories: [web-exploration, content-discovery]
tags: [content-discovery, recursive, rust, fuzzing]
status: unverified
status_checked: 2026-08-26
---

# feroxbuster

## What question does it answer?
I am authorised to test this site. What directories and files exist that nothing
links to - and what is inside the directories I find?

## When to reach for it
When you want recursion without managing it yourself. feroxbuster is Rust, fast, and
**recursive by default**: it queues newly discovered directories and keeps going, so
one command maps a tree that would take several passes with a flat scanner. That is
the practical difference from [gobuster](gobuster.md), and the reason to prefer it
for exploratory discovery.

## Install
```bash
sudo apt install feroxbuster     # packaged on Kali; release binaries on GitHub
```

## Usage
```bash
feroxbuster -u https://example.com -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt
feroxbuster -u https://example.com -x php,txt,bak -d 2      # extensions, depth cap
feroxbuster -u https://example.com --rate-limit 20 -o found.txt   # be polite, save output
```

## Output
A live table of responses: HTTP status, size in lines/words/bytes, and the URL.
Sizes matter as much as status - a wall of identical-size 200s is a catch-all page,
not real content. `-o` saves; `--json` gives structured output.

## Gotchas
- **Intrusive.** Thousands of requests against someone else's server. Written
  authorisation before you start; see [../../LEGAL.md](../../LEGAL.md).
- Recursion multiplies request volume quickly. Use `-d` to cap depth and
  `--rate-limit` on anything you do not own outright.
- Sites that return 200 for everything need `--filter-size` or `--filter-words` to be
  usable; otherwise every guess looks like a hit.
- Try passive discovery first -
  [Wayback CDX](../../06-history-and-archives/web-archive/wayback-cdx-api.md) often
  yields real paths at zero contact.

## Alternatives
- [ffuf](ffuf.md) - more flexible fuzzing, any injection point
- [gobuster](gobuster.md) - simpler, also does DNS and vhosts
- [dirhunt](dirhunt.md) - analysis instead of brute force
