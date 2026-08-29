---
name: PublicWWW
slug: publicwww
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://publicwww.com/
categories: [history-and-archives, analytics-linking]
tags: [source-code-search, tracking-ids, regex, fingerprints]
status: active
status_checked: 2026-08-26
---

# PublicWWW

## What question does it answer?
I have a string that should be unique to my target - a tracking ID, an affiliate code, a
pixel, an odd comment in their HTML. Which other sites contain it?

## When to reach for it
When the identifier is not one anybody thought to index. [SpyOnWeb](spyonweb.md) and
[DNSlytics](dnslytics.md) hold pre-extracted Analytics and AdSense IDs; PublicWWW
searches the **raw source** of half a billion pages for any alphanumeric string in the
HTML, JavaScript or CSS. That means it finds Facebook pixel IDs, affiliate tags, licence
keys, a bespoke JavaScript variable, a copy-pasted contact block - anything the operator
left behind that a dedicated ID index would never have a field for.

It supports regular expressions and ccTLD filters, so you can constrain a noisy string
to a plausible shape rather than drowning in matches.

## Install
```bash
# Nothing to install - web only, account required for full results.
```

## Usage
```text
https://publicwww.com/
  "UA-24230777-"                  # legacy Analytics: quote it, and KEEP the trailing hyphen
  "G-XXXXXXXXXX"                  # GA4 tag: plain quoted literal, no trailing hyphen
  "fbq('init', '1234567890')"     # sites sharing one Facebook pixel
  "Server: nginx/1.4.7"           # fingerprint by response header
```
`GTM-`, `AW-` and `DC-` tag IDs are worth querying the same way.

## Output
A list of matching URLs with the matched snippet in context, and a count of total
matches. The index stood at roughly 513 million pages when checked, dated the previous
day - it is actively maintained.

## Gotchas
- **The free tier is capped by site popularity, and that is the thing that will mislead
  you.** Anonymous searches return matches only from the top 1 million sites; a free
  account raises that to the top 3 million; the remaining ~510 million pages are paid.
  Obscure, throwaway and malicious sites are essentially never in the top 3M, so **a
  free-tier query about exactly the infrastructure you care about will return zero**.
  Never read that as "no shared identifier".
- **Keep the trailing hyphen on a UA ID.** `"UA-24230777-"` matches the whole property
  across all its view numbers and avoids colliding with longer numeric IDs;
  `"UA-24230777"` does neither reliably. GA4 `G-` IDs have no view suffix, so no hyphen.
- **It indexes source as delivered.** An ID injected at runtime by a tag manager, or one
  behind a login, is invisible - [NerdyData](nerdydata.md) renders pages and is the
  complement here. A negative result is weak either way.
- **Uniqueness is your responsibility.** A string from a common library or theme returns
  thousands of unrelated sites. Verify it is specific to your subject before calling a
  match a link.
- Index freshness varies per page: a site that removed a tag can still appear, and a
  recently added one may not. Corroborate before reporting.
- **Scripted requests get a JavaScript proof-of-work challenge that returns HTTP 200**
  with a ~6KB stub, so automation silently looks like it succeeded and found nothing.
  Check the terms before automating at all.

## Alternatives
- [SpyOnWeb](spyonweb.md) - free, and enough when the ID is a standard Analytics or AdSense one
- [DNSlytics](dnslytics.md) - historical depth and the ads.txt angle
- [NerdyData](nerdydata.md) - the same idea, priced for sales teams
