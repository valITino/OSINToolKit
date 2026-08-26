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

- [Netcraft Site Report](netcraft.md) - free, no account; the fastest way to get a
  site's first-seen date and its current netblock owner.
- [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md) - free IP history
  and historical lookups; the no-account starting point.
- [SecurityTrails](securitytrails.md) - historical DNS and WHOIS back to 2008 over a
  JSON API; small free tier, then paid. See
  [api-keys](../../99-resources/api-keys/README.md).
- [Whoisology](../../04-web-exploration/whois-domains/whoisology.md) and
  [DomainTools](../../04-web-exploration/whois-domains/domaintools.md) - deep historical
  and reverse WHOIS; paid, aimed at professional casework.

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [Netcraft Site Report](netcraft.md) | How long has this site actually existed, and whose network is it really on? | 2 | passive |
| [SecurityTrails](securitytrails.md) | What did this domain resolve to **before**, who registered it before the record was redacted, and what else has lived in the... | 2 | passive |
<!-- END:TOOLS -->

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
