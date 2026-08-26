---
name: wfuzz
slug: wfuzz
tier: 3
contact: intrusive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/xmendez/wfuzz
categories: [web-exploration, content-discovery]
tags: [fuzzing, legacy, python]
status: stale
status_checked: 2026-08-26
superseded_by: ffuf
---

# wfuzz

## What question does it answer?
What happens when I substitute a wordlist into any part of an HTTP request - path,
parameter, header, or cookie?

## Why this is tier 3
The concept is sound and wfuzz pioneered it, but the implementation is **aging
Python** that is slow next to modern alternatives and has had a patchy maintenance
history. [ffuf](ffuf.md) does the same job in Go: faster, actively developed, with
better filtering. There is no capability here that justifies choosing wfuzz for new
work - keep it only because it is Kali-installed and appears throughout older
write-ups.

## Install
```bash
sudo apt install wfuzz       # Kali; pip install wfuzz elsewhere
```

## Usage
```bash
wfuzz -w wordlist.txt --hc 404 https://example.com/FUZZ        # paths, hiding 404s
wfuzz -z range,1-100 --hc 404 https://example.com/user?id=FUZZ  # numeric range
```

`-z` selects the payload source, `FUZZ` is the injection marker, and `--hc`/`--hh`
hide responses by code or length - the same model ffuf uses.

## Output
A table of payload, HTTP status, and response size in lines/words/chars. As with any
fuzzer, filtering the baseline response out is what makes the output readable.

## Gotchas
- **Intrusive** - written authorisation before running it against anything you do not
  own. See [../../LEGAL.md](../../LEGAL.md).
- Slower than the Go and Rust alternatives; noticeable on large wordlists.
- Python dependency friction is common on current interpreters. Verify it runs before
  planning around it.

## Alternatives
- [ffuf](ffuf.md) - the direct replacement, use this instead
- [feroxbuster](feroxbuster.md) - recursive content discovery
- [gobuster](gobuster.md) - simpler directory and DNS brute forcing
