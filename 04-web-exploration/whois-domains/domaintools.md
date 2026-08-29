---
name: DomainTools
slug: domaintools
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://www.domaintools.com/
categories: [web-exploration, whois-domains]
tags: [reverse-whois, whois-history, pre-gdpr, paid]
status: active
status_checked: 2026-08-26
---

# DomainTools

## What question does it answer?
I have a registrant detail - an email, a name, a company, a phone number. What else did
that person register, including the domains they have since hidden behind privacy?

## When to reach for it
When the case turns on **who**, and current WHOIS is redacted. DomainTools holds
historical WHOIS back to the 1990s, which is the archive where pre-2018 records still
carry real names and addresses. The workflow that makes it worth the money is two steps:
pull a domain's historical record to recover a registrant identity, then push that
identity through Reverse Whois to find everything else it ever registered.

Be clear-eyed about cost. This is the deepest source of its kind and also the most
expensive; [Whoisology](whoisology.md) answers the same pivot for a fraction of the
price with shallower data. Try that first unless the case justifies the spend.

## Install
```bash
# Nothing to install - web only. APIs exist but are enterprise-tier.
```

## Usage
```text
https://whois.domaintools.com/<domain>                        # free lookup, captcha-gated
https://reversewhois.domaintools.com/                          # email/name/phone -> domains
https://research.domaintools.com/research/whois-history/       # dated historical records
```

## Output
Historical WHOIS as dated records with side-by-side and inline diffs, so a registrant
change has a date attached to it. Reverse Whois shows a **count** of current and
historical matches for free and puts the actual domain list behind quota. Iris
Investigate adds pivot panels and a Domain Risk Score.

## Gotchas
- **The free lookup is reCAPTCHA-gated on every request** and there is no anonymous API,
  so none of it is scriptable. For a plain current record,
  [whois](../../02-network-and-ip/registries-asn/whois.md) is faster and free.
- **The legacy WHOIS tools are a decaying source.** DomainTools carries its own notice
  about possible deprecation of Whois services after 28 January 2025 as registrars move
  to RDAP, and RDAP support is being added only to the enterprise products.
- **Enterprise pricing is quote-only.** The numbers on the pricing page are query quotas,
  not dollars. Public procurement listings suggest five- to six-figure annual instances.
- The self-serve Individual membership is $99/month or $995/year, explicitly licensed
  **non-commercial, single user, no API**, with low quotas (single-digit reverse searches
  per month). Do not use it for client casework - shared credentials are grounds for
  termination.
- Post-GDPR records are mostly redacted; the value is almost entirely in the old archive.
- Reverse Whois on a privacy-service email returns millions of unrelated domains. Pivot
  only on a value unique to your subject.
- Iris screenshot and website panels **actively fetch the target site** - a different
  contact level from the rest of the database queries.

## Alternatives
- [Whoisology](whoisology.md) - the same registrant pivot, far cheaper, semi-annual snapshots
- [viewdns.info](viewdns.md) - free IP history and reverse IP, no account
- [whois](../../02-network-and-ip/registries-asn/whois.md) - the authoritative current record
