# IP and WHOIS history

The current WHOIS and DNS tell you what an asset is now. History tells you what it
was - and the past is often where the attribution lives. A domain that hides behind
privacy today may have leaked a real registrant in 2016; an IP that serves a CDN now
may have hosted the origin last year.

## What history answers

- **Who registered a domain before WHOIS privacy**, or before GDPR redaction - the
  old record may still exist in historical databases.
- **What IP a domain used to resolve to**, which can reveal a shared host, a real
  origin, or a hosting move.
- **What else lived on an IP** at a given time (passive DNS reverse lookups over
  time), linking domains that share infrastructure.

## Where to get it

- [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md) - free IP history
  and historical lookups; the no-account starting point.
- **SecurityTrails** - historical DNS, WHOIS history, and passive DNS; generous-ish
  free tier, then paid. See [api-keys](../../99-resources/api-keys/README.md).
- **Whoisology / DomainTools** - deep historical and reverse WHOIS; paid, aimed at
  professional casework.

## Caveats

- Historical WHOIS accuracy varies; registrant fields were often unverified even
  when public. Treat a name as a lead, not proof.
- Passive DNS coverage is uneven - absence of a record is not proof an asset never
  existed.
- Shared hosting inflates "related" results: many unrelated domains share one IP.
  Corroborate before drawing a line between them.

## Related

- [../web-archive/README.md](../web-archive/README.md) - historical *content* to go with historical *infrastructure*
- [analytics-linking](../analytics-linking/README.md) - a different way to link sites over time
