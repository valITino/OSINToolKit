---
name: Maigret
slug: maigret
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/soxoj/maigret
categories: [people-and-identity, username-enum]
tags: [username, profiling, reporting, enumeration]
status: unverified
status_checked: 2026-08-26
---

# Maigret

## What question does it answer?
I have a username. Where does it exist, and what do those profiles actually say -
names, bios, locations, linked accounts?

## When to reach for it
When [Sherlock](sherlock.md)'s hit list is not enough. Maigret checks a larger site
list and goes a step further: it parses the profiles it finds and extracts details,
then recurses on the identifiers it discovers. It also generates readable HTML/PDF
reports, which makes it the better choice when the output has to go to someone else.

## Install
```bash
pipx install maigret
```

## Usage
```bash
maigret someusername                            # check and summarise
maigret someusername --html --pdf                # generate reports
maigret someusername --top-sites 500 -a          # broaden the site list, show all results
```

## Output
Found accounts with extracted profile data (display name, bio, location, avatar,
sometimes linked accounts), plus generated reports. The extracted detail is the part
that turns a list of URLs into an identity picture.

## Gotchas
- **Same false-positive caution as Sherlock** - verify every hit by hand. A larger
  site list means more false positives, not fewer.
- **Active and noisy**: hundreds of requests from your IP. Use a proxy and expect rate
  limiting; see [OPSEC](../../00-methodology/opsec/README.md).
- Extracted profile data is **self-reported by the subject** and frequently false.
  Treat a stated location or name as a claim, not a fact.
- Collecting and storing this data is processing personal data - have a lawful basis.
  See [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [Sherlock](sherlock.md) - faster, cleaner, fewer false positives
- [holehe](../email-osint/holehe.md) - pivot from an email instead
