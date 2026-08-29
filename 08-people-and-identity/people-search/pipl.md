---
name: Pipl
slug: pipl
tier: 2
contact: passive
type: api
cost: paid
platforms: [web]
url: https://pipl.com/
categories: [people-and-identity, people-search]
tags: [identity-resolution, enterprise, no-free-tier, api]
status: active
status_checked: 2026-08-26
---

# Pipl

## What question does it answer?
I need identity resolution across a global graph, with provenance I can defend in a
report. Can I even get access?

## When to reach for it
Usually you cannot, and that is the most useful thing to know about it. **The free Pipl
search that a decade of OSINT guides still recommends was shut down back in 2019.**
There is no free tier, no trial, no self-serve signup, and no published price -
`pipl.com/pricing` is a 404 and every route into the product is a login page or a sales
form. Users are vetted for a stated legitimate purpose, and the terms are written for
entities rather than individuals.

If your organisation does hold a contract, Pipl Search is genuinely different from a
consumer broker: it resolves identities across emails, phones, usernames, addresses, and
profiles with confidence and provenance signals attached, and it is available as a JSON
API rather than a web form. That provenance is the reason enterprise teams buy it.

## Install
```bash
# Nothing to install - and nothing to sign up for. Contract only.
```

## Usage
```text
https://pipl.com/contact-us                      # the only entry point for new customers
https://search.pipl.com/accounts/login/           # existing customers: the investigation UI
https://docs.pipl.com/                            # Search API docs; key issued under contract
https://pipl.com/personal-information-removal-request   # remove yourself from the graph
```

## Output
Resolved identity records linking names, emails, phone numbers, usernames, addresses,
and associated profiles, with confidence and provenance signals. Delivered as JSON via
the Search API or through the browser investigation UI. Risk scoring is a separate
product; Search deliberately does not assign fraud scores.

## Gotchas
- **Any guide telling you to "just search pipl.com" is years out of date.** The consumer
  search ended in 2019; the company cited bot and abuse prevention at the time.
- **It is not an alternative to [Spokeo](spokeo.md) or [BeenVerified](beenverified.md).**
  Those sell single reports to individuals; Pipl sells contracts to fraud, compliance,
  trust-and-safety, and law-enforcement teams. Do not present them as substitutes.
- **Pricing is unpublished.** Figures circulating on affiliate and SEO sites are
  uncorroborated - treat annual contract costs as "contact sales" rather than quoting a
  number.
- Effectively unavailable to a solo investigator, journalist, or student.
- **Naming confusion:** "Elephant" is Pipl's risk model and the hostname for its Trust
  product. The company did not rebrand; articles claiming otherwise are wrong.
- Its centre of gravity has shifted toward payment and transaction risk. Search still
  exists, but building a long-lived workflow on it carries product-direction risk.
- Same-name and shared-device merges are a structural hazard in any identity graph, and
  Pipl publishes no accuracy rate. Corroborate.

## Alternatives
- [ThatsThem](thatsthem.md) - free, and actually reachable
- [Spokeo](spokeo.md) - the consumer-tier answer to a similar question
- [Maltego](../../01-orchestrators/modular-frameworks/maltego.md) - build the identity graph yourself from sources you control
