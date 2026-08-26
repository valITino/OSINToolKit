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
  "UA-24230777-"                  # sites sharing a legacy Analytics property
  "G-XXXXXXXXXX"                  # sites sharing a modern Google Tag
  "fbq('init', '1234567890')"     # sites sharing one Facebook pixel
  "Server: nginx/1.4.7"           # fingerprint by response header
```

## Output
A list of matching URLs with the matched snippet in context, and a count of total
matches. The index stood at roughly 513 million pages when checked, dated the previous
day - it is actively maintained. Free searches preview results; full result sets and
exports need a paid plan.

## Gotchas
- **It indexes source, so it only sees what is in the delivered HTML/JS/CSS.**
  Identifiers injected at runtime by a tag manager, or present only behind a login, are
  invisible. A negative result is weak.
- **Coverage is a crawl, not a census.** Half a billion pages is a lot and is still a
  fraction of the web, weighted toward popular sites. Absence is not evidence.
- **Uniqueness is your responsibility.** Searching a string that appears in a common
  library or theme returns thousands of unrelated sites. Verify the string is actually
  specific to your subject before treating a match as a link.
- Snapshots age. A match reflects when PublicWWW last crawled that page, not today, so
  confirm the identifier is still live before reporting it.
- Free use is capped and full results are paywalled; the tool is priced for marketing
  research rather than investigation.
- The site needs JavaScript, so it is not scriptable from the browser interface.

## Alternatives
- [SpyOnWeb](spyonweb.md) - free, and enough when the ID is a standard Analytics or AdSense one
- [DNSlytics](dnslytics.md) - historical depth and the ads.txt angle
- [NerdyData](nerdydata.md) - the same idea, priced for sales teams
