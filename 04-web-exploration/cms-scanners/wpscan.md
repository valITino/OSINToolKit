---
name: WPScan
slug: wpscan
tier: 2
contact: intrusive
type: cli
cost: freemium
platforms: [linux, macos]
url: https://wpscan.com/
categories: [web-exploration, cms-scanners]
tags: [wordpress, plugins, themes, enumeration]
status: unverified
status_checked: 2026-08-26
---

# WPScan

## What question does it answer?
This site is WordPress. Exactly which version, plugins, themes, and users does it
expose, and which of those have known vulnerabilities?

## When to reach for it
The deepest option once you know the target is WordPress - which is most of the
web's CMS traffic. Its advantage over the generic scanners is the curated WordPress
vulnerability database behind it, so findings come with real advisory references
rather than version guesses.

WPScan can brute-force logins. That is **out of scope** here; use it for enumeration
and vulnerability lookup only.

## Install
```bash
sudo apt install wpscan          # Kali default
wpscan --update                   # refresh the local database
```

## Usage
```bash
wpscan --url https://example.com                                   # baseline enumeration
wpscan --url https://example.com --enumerate vp,vt --api-token "$WPSCAN_TOKEN"
wpscan --url https://example.com --stealthy                        # slower, rotates user agent
```

## Output
The WordPress version with confidence and how it was determined, enumerated plugins
and themes with versions and last-updated dates, exposed users where the site leaks
them, and - with an API token - the matching vulnerability records.

## Gotchas
- **Enumeration is intrusive.** `--enumerate` requests large numbers of paths.
  Written authorisation; see [../../LEGAL.md](../../LEGAL.md).
- Vulnerability data requires a free API token, which is capped at a small number of
  requests per day. Without it you get enumeration but no advisory matching. See
  [../../99-resources/api-keys/README.md](../../99-resources/api-keys/README.md).
- `--stealthy` reduces the request rate and rotates the user agent, but it is a
  courtesy, not concealment - a WAF will still see it.
- Passive detection can miss plugins that leave no public trace; absence is not proof.

## Alternatives
- [CMSmap](cmsmap.md) - multi-CMS, similar job
- [CMSeeK](cmseek.md) - identify the CMS first
