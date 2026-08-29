---
name: Namedroppers
slug: namedroppers
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://www.namedroppers.com/
categories: [dns-and-subdomains, typosquatting]
tags: [brand-abuse, keyword-search, zone-data, legacy]
status: active
status_checked: 2026-08-26
---

# Namedroppers

## What question does it answer?
Which **registered** domains contain my brand name anywhere in them - not the typos, but
the compositions: brand-support, my-brand, brand-login?

## When to reach for it
As the complement to [dnstwist](dnstwist.md). dnstwist generates permutations of a name
and checks them, which catches typos, homoglyphs, and swapped TLDs. It will not produce
`acme-account-recovery.com`, because that is not a misspelling of anything - it is a
composition. Namedroppers searches actual zone data for names *containing* your keyword,
so it finds exactly that class of brand-abuse registration.

Run it when you are scoping brand exposure and want the names a permutation engine
cannot imagine. Do not run it expecting ownership information.

## Install
```bash
# Nothing to install - web only, and it actively blocks scripted clients.
```

## Usage
```text
https://www.namedroppers.com/     # enter one or more keywords; all must appear in the name
  More Options: exclude=, starts-with, ends-with, exclude digits/letters/dashes,
                minimum and maximum label length
```

## Output
A list of registered domain names containing every keyword you gave, with the match
highlighted and a WHOIS hand-off link per result. The header reports total matches
against the size of its active-record set - around 188 million records at the time of
checking, described as refreshed nightly.

## Gotchas
- **It answers "which names contain this string", not "who owns them".** There is no
  reverse WHOIS and no registrant index here. For ownership pivots use
  [Whoisology](../../04-web-exploration/whois-domains/whoisology.md) or
  [DomainTools](../../04-web-exploration/whois-domains/domaintools.md).
- **Zone coverage is narrow and dated: com, net, org, edu, biz, us, info, name only.**
  No new gTLDs and no ccTLDs at all - so `.xyz`, `.top`, `.shop`, `.io` and `.co` are
  invisible, and that is where a great deal of modern abuse infrastructure lives. Treat
  a clean result as covering a fraction of the namespace.
- **Free results are hard-capped at 50** even when the query matches thousands. The full
  list is a paid report from about $30; keyword change monitoring is a separate
  subscription.
- Scripted requests are refused with a 403 - it wants a real browser with a referrer and
  a session cookie. Do not build automation against it.
- The search form has a roughly even chance of opening an advertising popup on submit.
- The site looks abandoned - a 2021 copyright and 1990s markup - but the database behind
  it is current. Do not judge it by the frontend, in either direction.
- It is also a registrar front, so results are shaped toward selling you a registration.

## Alternatives
- [dnstwist](dnstwist.md) - permutations, homoglyphs, and live checks; start here
- [crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md) - brand names that requested certificates
- [CertWatch](../../05-certificates-tls/ct-log-search/certwatch.md) - the same brand across every TLD, from CT logs
