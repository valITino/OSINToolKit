---
name: Spokeo
slug: spokeo
tier: 2
contact: passive
type: web
cost: paid
platforms: [web]
url: https://www.spokeo.com/
categories: [people-and-identity, people-search]
tags: [people-search, us-records, data-broker, paid]
status: active
status_checked: 2026-08-26
---

# Spokeo

## What question does it answer?
I have a US name, phone, email, address, or username. What records does a large broker
hold against it - and how much can I learn before paying anything?

## When to reach for it
Spokeo is worth knowing mainly because **its free directory pages are more useful than
they look**. Without paying or logging in, a name page returns a candidate list with
ages, deceased flags, current and prior cities, named relatives, aliases, and *counts*
of the addresses, phones and emails held. The strings themselves are paywalled, but
that free skeleton is often enough to confirm you have the right person, or to build the
relative-and-location graph you then verify in
[public records](../public-records/README.md).

Pay only when you need the contact details themselves and have exhausted the free
sources. [ThatsThem](thatsthem.md) shows more for free.

## Install
```bash
# Nothing to install - web only.
```

## Usage
```text
https://www.spokeo.com/           # name, phone, email, address, or username
https://www.spokeo.com/First-Last  # free directory page: relatives, aliases, record counts
https://www.spokeo.com/optout      # removal request for your own listing
```

## Output
Free: candidate list, age, deceased status, location history, relatives, aliases, record
counts. Paid: the actual addresses, phone numbers, emails, and - via reverse email or
username - linked profiles across social, dating, and shopping sites. Criminal records
cost extra on top of the membership.

## Gotchas
- **Spokeo is not a consumer reporting agency.** Its own disclaimer forbids using it for
  credit, employment, tenant screening, or any FCRA-covered purpose. This is not
  theoretical: Spokeo paid an $800,000 FTC settlement in 2012 over allegations it
  operated as one.
- **Accuracy is disclaimed by Spokeo itself** - it "does not verify and cannot guarantee
  the accuracy of this Public Information". *Spokeo v. Robins* reached the US Supreme
  Court over a profile that got the plaintiff's education, wealth, and marital status
  wrong.
- **Relatives and aliases are same-name clustering, not verified relationships.** Common
  names produce fused identities. Never cite a Spokeo relative link as attribution.
- **Prices are not published** - the FAQ says only that membership is "very affordable".
  At checkout in August 2026 it offered roughly $15-$25 a month depending on term, with
  variants and promotions in rotation. Assume the figure you see is A/B tested.
- **Billing traps are in the policy**: trials auto-convert, plans auto-renew, all sales
  are final and non-refundable, and a subscription caps at 100 searches a month.
- Spokeo's privacy policy covers removal from "Spokeo.com and/or Thatsthem.com" - budget
  for opting out of both.
- **GDPR is a dead end here** and there is no EU erasure workflow. For a California
  resident, one submission to the state's DROP platform under the Delete Act now
  outperforms per-site opt-out forms. See [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [ThatsThem](thatsthem.md) - shows more for free; try it first
- [BeenVerified](beenverified.md) - comparable data, no free tier, roughly double the price
- [public-records](../public-records/README.md) - authoritative and verifiable
