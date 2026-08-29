---
name: dnsmap
slug: dnsmap
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/pagvac/dnsmap
categories: [dns-and-subdomains, active-enum]
tags: [dns, brute-force, subdomains, scraping]
status: active
status_checked: 2026-08-26
---

# dnsmap

## What question does it answer?
I have a domain and I am authorised to probe it. Which subdomains exist, from one
command, without me choosing a wordlist or tuning anything?

## When to reach for it
When you want a result rather than a configuration exercise. dnsmap deliberately ships
with **no command-line flags** beyond `-d` for debug - it scrapes public sources and
then brute forces from a built-in list, and that is the whole interface. That makes it
the one to hand someone new to this, or to run while you set up something heavier.

Reach for [puredns](puredns.md) instead when you have your own wordlist and need
wildcard filtering; reach for [subfinder](../passive-enum/subfinder.md) first if you
have no authorisation, since dnsmap's brute-force half touches the target.

## Install
```bash
git clone https://github.com/pagvac/dnsmap && cd dnsmap
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt      # on Windows install dnspython alone - see Gotchas
```

## Usage
```bash
python3 dnsmap.py example.com              # scrape plus brute force, results to stdout
python3 dnsmap.py example.com > subs.txt   # clean list; progress stays on stderr
```

## Output
Confirmed subdomains on stdout, one per line, and nothing else - the progress bar and
the closing `[stats]` line (duration, attempted, found, scrape_found) go to stderr. So
a plain redirect gives you a list that pipes straight into a resolver or a fuzzer with
no filtering step.

## Gotchas
- **`apt install dnsmap` gives you the wrong tool.** Debian and Kali package the
  original C version; its author has since rewritten dnsmap in Python and states the
  old version should no longer be used. Install from the repo above.
- Brute forcing DNS is **intrusive** and noisy against the target's nameservers.
  Written authorisation - see [../../LEGAL.md](../../LEGAL.md).
- No flags means no wordlist control, no rate limiting, and no wildcard handling. On a
  wildcard domain, expect noise you have to filter yourself.
- **It queries third-party OSINT APIs before brute forcing**, so running it tells several
  outside services which domain you are investigating. Some of those sources are defunct
  or rate-limited, which is why `scrape_found` is legitimately 0 sometimes. See
  [../../00-methodology/opsec/README.md](../../00-methodology/opsec/README.md).
- `requirements.txt` pins `uvloop`, which has no Windows wheels and will fail there. The
  code imports it inside a `try`, so installing `dnspython` alone works fine on Windows.
- There is no PyPI package - `pip install dnsmap` does not get you this tool.
- A full run is not quick - the sample run in its own README took ~200 seconds for
  ~100k attempts.

## Alternatives
- [puredns](puredns.md) - your wordlist, with wildcard filtering and validation
- [fierce](fierce.md) - adds the surrounding netblock, not just the names
- [subfinder](../passive-enum/subfinder.md) - passive, no authorisation needed
