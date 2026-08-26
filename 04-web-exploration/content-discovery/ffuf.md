---
name: ffuf
slug: ffuf
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/ffuf/ffuf
categories: [web-exploration, content-discovery]
tags: [fuzzing, content-discovery, vhost, parameters]
status: unverified
status_checked: 2026-08-26
---

# ffuf

## What question does it answer?
I am authorised to test this site. What happens if I substitute a wordlist into
*this specific position* - a path, a parameter name, a header, a virtual host?

## When to reach for it
The most versatile fuzzer of the group, and the one to learn if you learn one. The
`FUZZ` keyword can go anywhere in the request, which means the same tool covers
directory discovery, parameter discovery, and vhost enumeration. It is the modern
replacement for [wfuzz](wfuzz.md), which is the same idea in aging Python.

## Install
```bash
go install github.com/ffuf/ffuf/v2@latest     # also packaged on Kali
```

## Usage
```bash
ffuf -u https://example.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt
ffuf -u https://example.com/?FUZZ=test -w params.txt -fs 4242          # parameter names, filter by size
ffuf -u https://example.com -H 'Host: FUZZ.example.com' -w subs.txt -fc 404   # vhosts
ffuf -u https://example.com/FUZZ -w list.txt -rate 50 -o out.json      # rate-limited, JSON out
```

## Output
Matching responses with status, size, words, lines, and duration. The filtering flags
(`-fc` status, `-fs` size, `-fw` words) are the tool - a raw run is mostly noise
until you filter the baseline response out.

## Gotchas
- **Intrusive** and fast enough to hurt a small site. Use `-rate` and `-p` (delay)
  against anything you do not own, with written authorisation.
- Establish the baseline first: request a path you know does not exist, note its
  size, then filter it. Otherwise soft-404s swamp the results.
- Auto-calibration (`-ac`) helps but is not reliable on dynamic pages.

## Alternatives
- [feroxbuster](feroxbuster.md) - recursive by default, less configuration
- [gobuster](gobuster.md) - simpler for plain directory/DNS work
- [wfuzz](wfuzz.md) - the tier 3 predecessor
