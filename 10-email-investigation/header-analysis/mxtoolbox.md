---
name: MXToolbox
slug: mxtoolbox
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://mxtoolbox.com/
categories: [email-investigation, header-analysis]
tags: [headers, dns, blacklist, spf, dmarc]
status: unverified
status_checked: 2026-08-26
---

# MXToolbox

## What question does it answer?
I have an email header block or a domain. What path did this message take, how long
did each hop hold it, and is the sending domain's mail configuration sound?

## When to reach for it
The fastest way to turn a wall of headers into a readable timeline. Paste the raw
headers into its analyser and it renders the `Received:` chain as ordered hops with
delays, then flags authentication results. Its DNS side answers the sending-domain
questions in the same place: MX records, SPF, DMARC, and blacklist status.

Always read the raw headers yourself as well - see
[../README.md](../README.md) for how.

## Install
```bash
# Nothing to install - web only. Free use is rate-limited; monitoring is paid.
```

## Usage
```text
https://mxtoolbox.com/EmailHeaders.aspx     # paste raw headers, get the parsed hop chain
https://mxtoolbox.com/SuperTool.aspx         # mx:, spf:, dmarc:, blacklist: lookups
```

## Output
The hop chain with per-hop delays and the originating IP, the SPF/DKIM/DMARC verdicts,
and blacklist status across many RBLs. Large per-hop delays are worth noting - they can
indicate queuing, greylisting, or an unusual relay.

## Gotchas
- **`Received:` headers read bottom-up.** The oldest hop - usually the originating
  system - is at the **bottom**. Reading top-down inverts the story.
- **Headers above the originating hop can be forged**, since a sender controls what it
  writes. Trust hops added by servers you trust; treat the rest as claims.
- **Forwarding a message replaces the original headers.** If a phishing email was
  forwarded to you, you are analysing the forward's path, not the attacker's. Always
  ask for the original as an attachment (`.eml`).
- Pasting headers into a third-party site discloses sender, recipient, and subject to
  that service. Consider whether that is acceptable
  ([OPSEC](../../00-methodology/opsec/README.md)).

## Alternatives
- [../README.md](../README.md) - reading headers by hand, which you should learn
- [host](../../03-dns-and-subdomains/query-tools/host.md) - the same DNS answers from your own machine
