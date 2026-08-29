# Passive DNS

Somebody else ran the query years ago and kept the answer. Passive DNS
providers collect resolver traffic and historical zone data, so they can tell
you what a name resolved to in 2019, and which other names have pointed at an
address since - questions live DNS cannot answer at all.

Nothing here touches the target. It is the first thing to reach for when a
domain has moved behind a CDN, when the interesting host was decommissioned, or
when you need to show that two pieces of infrastructure overlapped in time.

## What it answers that live DNS does not

| Question | Live DNS | Passive DNS |
|---|---|---|
| What does this name resolve to now? | Yes | Yes, but possibly stale |
| What did it resolve to in 2021? | No | Yes, with first/last-seen dates |
| Which other names resolved to this IP? | No | Yes |
| When did it move to Cloudflare? | No | Yes - the cutover shows as a date |
| Did these two domains ever share a host? | No | Yes, and that is the pivot |

The first/last-seen timestamps are the point. A shared IP means little on its
own; a shared IP *during the same three weeks*, on a small hosting provider, is
a real lead.

## The catch: nobody has it all

Every provider builds its dataset from its own sensors, so coverage differs by
region, by resolver population, and by time. A name that is absent from one
provider is routinely present in another. Treat these as partial witnesses:

- Query at least two before concluding a record never existed.
- Absence is never evidence. It means nobody's sensor saw the answer.
- Most of the deep historical sets are commercial. The free tiers are useful
  for a handful of pivots and will not sustain bulk work.
- Access usually needs an account even where the data is free - request it
  before you need it, not during an incident.

## Tools here

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [CIRCL Passive DNS](circl-pdns.md) | I have a domain or an IP that came out of an incident. What did it resolve to historically, and what else lived on that address... | 2 | passive |
| [DNSDB (Farsight / DomainTools)](dnsdb.md) | I have a name or an IP and I need the complete record, not a sample: everything it resolved to and everything that ever lived on... | 2 | passive |
| [mnemonic PassiveDNS](mnemonic-pdns.md) | I have a domain, or the IP it resolves to today. What did that name resolve to before, and what other names have answered from... | 2 | passive |
| [Validin](validin.md) | I have a domain or an IP. What did it resolve to over the last few years, what else has lived on that address or netblock, and... | 2 | passive |
<!-- END:TOOLS -->

## Related

- [../passive-enum/README.md](../passive-enum/README.md) - subdomains from the same sort of collected data
- [../reverse-dns/README.md](../reverse-dns/README.md) - the live view of IP-to-name
- [../../06-history-and-archives/ip-whois-history/README.md](../../06-history-and-archives/ip-whois-history/README.md) - ownership history to pair with resolution history
- [../../05-certificates-tls/ct-log-search/README.md](../../05-certificates-tls/ct-log-search/README.md) - names that were certified, whether or not they resolved
