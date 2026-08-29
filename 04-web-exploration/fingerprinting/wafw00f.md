---
name: WAFW00F
slug: wafw00f
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/EnableSecurity/wafw00f
categories: [web-exploration, fingerprinting]
tags: [waf, cdn, bot-management, edge-detection]
status: active
status_checked: 2026-08-29
---

# WAFW00F

## What question does it answer?
I have a URL and a stack listing I do not trust. What WAF, CDN or
bot-management product is answering for this site - and so, am I fingerprinting
the application or the thing standing in front of it?

## When to reach for it
Before you believe any [WhatWeb](whatweb.md) or [httpx](httpx.md) result. Those
tools describe whatever answered; WAFW00F tells you whether that was the origin
at all. A named hit is the caveat that turns a stack listing into an honest
finding, and the cue to switch to
[origin-unmasking](../../05-certificates-tls/origin-unmasking/README.md).

Not a casual tool. It is intrusive here because on any host it cannot
fingerprint from headers alone, it escalates to attack traffic by itself, with
no flag to stop it (see Gotchas). For a quiet answer to a related question,
`httpx -cdn` matches resolved IPs against known CDN ranges and sends nothing
extra, and [urlscan.io](urlscan-io.md) shows the edge without you touching it.

## Install
```bash
sudo apt install wafw00f              # Kali/Debian, 2.4.2 - level with upstream
python3 -m pip install wafw00f        # or pipx install wafw00f; Python >= 3.10
pipx install git+https://github.com/EnableSecurity/wafw00f.git   # from source
```

## Usage
```bash
wafw00f https://example.com          # one target, stops at the first signature match
wafw00f -l                           # list every WAF it knows, before trusting a miss
wafw00f -i targets.txt -f json -o waf.json   # batch a list (-i), structured output
wafw00f -a -v -T 30 https://example.com      # find ALL matches - loud, every test
```

## Output
A banner, then `[*] Checking <url>` and one of three verdicts. A fingerprint
reads `[+] The site <url> is behind Edgecast (Verizon Digital Media) WAF.`, with
multiple hits joined by "and/or". A guess reads `[+] Generic Detection results:`
and `seems to be behind a WAF or some sort of security solution`, with a `[~]
Reason:` line. A miss reads `[-] No WAF detected by the generic detection`.

Every run ends with `[~] Number of requests: N`. Read that first: 2 means a
header answered cheaply, more means it escalated. JSON output gives one record
per target with the URL, the product, and what triggered the match.

## Gotchas
- **It sends real attack traffic, automatically.** Where no header or cookie
  signature matches, generic detection fires cross-site scripting, SQL
  injection, path traversal and command injection probe strings at the target;
  `-a` adds every vendor's test on top. These land in the target's WAF log as an
  attack and the escalation cannot be disabled, which is why this is intrusive
  rather than active - see [../../LEGAL.md](../../LEGAL.md) before pointing it
  at anything you do not own. Probing defences past identifying the product is
  out of scope here.
- **Generic detection is a guess, not an identification.** It means only that
  responses changed when payloads arrived - a rate limiter, a bot manager, a CDN
  error page or a plain 403 rule all do that. Only the `[+] ... is behind <name>
  WAF.` line is a fingerprint; never report the generic result as a product.
- **A miss is weak evidence.** Many WAFs are configured not to advertise
  themselves, and vendor tells change faster than signatures do.
- **Known gaps in 2.4.2:** DataDome has no entry at all, PerimeterX appears only
  under its pre-rebrand name, Akamai only as "Kona SiteDefender". Modern
  bot-management can read as clean, so check `wafw00f -l` before concluding.
- A Cloudflare hit says nothing about a second WAF at the origin, nor about the
  origin's address - you only ever fingerprint the edge you can reach.
- `-l` lists known WAFs, `-i` reads your target file. Passing a host list to
  `-l` is a silent no-op that just prints the catalogue.
- No account and no third party: every request goes from your IP straight to the
  target, so your address is in their logs. Route it or use a jump host - see
  [opsec](../../00-methodology/opsec/README.md).

## Alternatives
- [httpx](httpx.md) - `-cdn` matches IP ranges instead of behaviour; run both
- [urlscan.io](urlscan-io.md) - the edge's response without you sending anything
- [WhatWeb](whatweb.md) - what the thing that answered claims to be
- [BuiltWith](builtwith.md) - passive CDN and hosting history for the domain
