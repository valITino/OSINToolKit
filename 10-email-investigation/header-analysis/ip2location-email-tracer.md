---
name: IP2Location Email Tracer
slug: ip2location-email-tracer
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://www.ip2location.com/free/email-tracer
categories: [email-investigation, header-analysis]
tags: [headers, geolocation, received-chain, free]
status: active
status_checked: 2026-08-26
---

# IP2Location Email Tracer

## What question does it answer?
I have a header block full of IP addresses. Which networks and countries did this
message pass through - without me looking up each address by hand?

## When to reach for it
When the chain is long and you want the geolocation join done for you. It parses the
`Received` headers, extracts the IPs, and resolves each one against IP2Location's
database, so you get country, region and network per hop in a single pass instead of
pasting addresses into a lookup tool one at a time.

That convenience is also its trap, so use it deliberately: reach for it to **triage a
route quickly**, and reach for
[Google Messageheader](google-messageheader.md) when the question is timing, or
[MXToolbox](mxtoolbox.md) when it is reputation.

## Install
```bash
# Nothing to install - web only, no account.
```

## Usage
```text
https://www.ip2location.com/free/email-tracer
  Paste the full raw header block and submit.
```

## Output
The parsed hop chain with each `Received` IP resolved to a country, region, and network
or ISP, presented as a route. The underlying data is the same IP2Location dataset
described in
[IP2Location](../../02-network-and-ip/geolocation/ip2location.md) - the free tier, so
country and ASN are reasonable and city is not.

## Gotchas
- **A map of the hops is not a map of the sender.** This is the single easiest way to
  produce a confident, wrong conclusion in an email investigation. The IPs are relays,
  VPN exits, and cloud mail infrastructure; a "message from Lithuania" is usually a
  message that touched a server in Lithuania.
- **Everything below the first server you control can be forged**, so the earliest hop -
  the one that looks most like the sender - is precisely the least trustworthy line to
  geolocate.
- **Webmail removes the premise entirely.** Gmail and Outlook.com strip the sending
  client's IP from outbound headers, so for a message composed in a browser the
  "originating IP" is Google or Microsoft infrastructure. A hop geolocating to a
  provider's datacentre tells you which provider, and nothing about the person.
- Free-tier geolocation is country- and network-accurate at best. Do not report a city,
  and never a coordinate. See
  [../../02-network-and-ip/geolocation/README.md](../../02-network-and-ip/geolocation/README.md).
- Pasting headers uploads recipient addresses and internal hostnames to a third-party
  vendor. Parse locally on a sensitive case.
- The site sits behind a bot check, so scripted access does not work and a `BLOCKED`
  result from a link checker says nothing about its health.
- Large providers hand a message between internal hops that all geolocate to the same
  provider - visually busy, analytically empty.

## Alternatives
- [Google Messageheader](google-messageheader.md) - normalised hop timing; the better default
- [MXToolbox](mxtoolbox.md) - blacklist status and live DNS on the sending infrastructure
- [IP2Location](../../02-network-and-ip/geolocation/ip2location.md) - the same data, offline and in bulk
