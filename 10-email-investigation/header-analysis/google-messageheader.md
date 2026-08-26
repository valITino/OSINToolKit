---
name: Google Admin Toolbox Messageheader
slug: google-messageheader
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://toolbox.googleapps.com/apps/messageheader/
categories: [email-investigation, header-analysis]
tags: [headers, received-chain, hop-timing, spf-dkim-dmarc]
status: active
status_checked: 2026-08-26
---

# Google Admin Toolbox Messageheader

## What question does it answer?
I have a raw header block. What route did this message take, and **where did it sit** -
which hop introduced the delay?

## When to reach for it
For the hop-timing table, which is the thing it does better than anything else free.
Messageheader normalises the timestamps across every `Received` header - which are
written in whatever timezone each relay felt like - and shows the elapsed time between
hops as a table. A message that took four hours somewhere in the middle is telling you
something: a greylisting delay, a queue, or a forged header whose clock does not fit.

It also parses SPF, DKIM and DMARC results out of the authentication headers. Reach for
[MXToolbox](mxtoolbox.md) when you also want blacklist status for the sending IPs; reach
for this when you want the chain read clearly.

## Install
```bash
# Nothing to install - web only, no account.
```

## Usage
```text
https://toolbox.googleapps.com/apps/messageheader/
  1. In your mail client, view the original / raw source of the message.
  2. Copy the full header block - everything above the body.
  3. Paste it in and click "Analyze the header above".
```

## Output
A summary of sender, recipient, subject and message ID, then the hop table: one row per
`Received` header in the order the message actually travelled, with the normalised time
and the delay introduced at each step. Authentication results (SPF, DKIM, DMARC) are
shown alongside.

## Gotchas
- **Read `Received` headers bottom-up.** The oldest hop is at the bottom. The tool
  reverses them for you, which is helpful right up until you cross-reference against the
  raw source and lose your place.
- **Only the hops added by servers you trust are trustworthy.** Anything below the first
  server you control can be fabricated wholesale by the sender. The originating IP in a
  forged chain is whatever the forger typed.
- Pasting a header means pasting it into **Google**. Headers contain recipient addresses,
  internal hostnames, and message IDs. On a sensitive case, parse locally instead - see
  [../../00-methodology/opsec/README.md](../../00-methodology/opsec/README.md).
- A `dmarc=pass` only means the message passed *at the receiving server that wrote that
  line*. It is a claim in a header like any other.
- Truncated pastes are the usual failure: copy the whole block, including folded
  continuation lines, or the chain will be parsed wrong.
- It reads what is in the headers. It does not fetch, resolve, or check anything, so it
  will not tell you whether the sending IP is currently listed anywhere.

## Alternatives
- [MXToolbox](mxtoolbox.md) - adds blacklist checks and live DNS lookups on the senders
- [IP2Location Email Tracer](ip2location-email-tracer.md) - geolocates the hops, with the caveats that implies
- [checkdmarc](../server-checks/checkdmarc.md) - what the sending domain's policy actually permits
