# Dorking

Search engines have already crawled the target. Dorking is asking them precisely,
with operators, instead of hopefully. It is entirely passive - you query the engine,
never the target - and it routinely finds exposed documents, directory listings, and
admin pages that no scanner would reach.

## Operators worth knowing

| Operator | Finds |
|---|---|
| `site:example.com` | Only pages on that domain (and subdomains) |
| `inurl:admin` | Pages whose URL contains a string |
| `intitle:"index of"` | Pages whose title contains a string - the classic directory-listing dork |
| `filetype:pdf` | A specific file extension |
| `intext:"internal use only"` | A phrase in the page body |
| `cache:` | Formerly the engine's cached copy - **discontinued, see below** |
| `related:example.com` | Sites the engine considers similar |
| `"exact phrase"` | Exact match |
| `term1 OR term2` | Either term |
| `-term` | Exclude a term |
| `*` | Wildcard within a phrase |
| `2019..2023` | A numeric or year range |

Combine them - that is where the power is:

```text
site:example.com filetype:pdf                      # public documents to feed ExifTool
site:example.com inurl:admin -inurl:blog           # admin paths, minus the noise
site:example.com intitle:"index of"                # directory listings
"@example.com" -site:example.com                   # the domain's emails mentioned elsewhere
```

## Search-engine cache is gone

**Google and Bing both discontinued their web cache in 2024.** `cache:` no longer
works. When you need the previous version of a page, use
[Wayback](../../06-history-and-archives/web-archive/wayback-cdx-api.md) instead - it
is the fallback now.

## GHDB

The [Google Hacking Database](https://www.exploit-db.com/google-hacking-database) is
a curated, categorised collection of dorks that surface exposed files, error
messages, and login pages. Use it as a source of query patterns to adapt - and note
that many GHDB entries target vulnerable software, which is outside this repo's
discovery-and-attribution scope.

## Discipline

- Vary engines. Bing, DuckDuckGo, and Yandex index differently; a dork that returns
  nothing on Google can hit elsewhere.
- Heavy automated dorking triggers CAPTCHAs and rate limits, and automating Google
  queries breaches its terms.
- Finding an exposed file with a dork is passive. *Acting* on what you find may not
  be - see [../../LEGAL.md](../../LEGAL.md).

## Tools here

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [DorkSearch](dorksearch.md) | I have a target and a rough idea of what I want to find, but not the operator syntax. Can something build the dork for me, and... | 2 | passive |
| [GooFuzz](goofuzz.md) | I have a domain. Which files, paths, extensions and subdomains has Google already indexed for it - found without sending a single... | 2 | passive |
| [Google Hacking Database](ghdb.md) | What should I actually search for? Someone has already worked out the query that surfaces exposed backups, login panels, or... | 2 | passive |
| [pagodo](pagodo.md) | I want to run hundreds of GHDB dorks against one domain instead of pasting them into a search box one at a time. Can that be... | 2 | passive |
| [dorkscout](dorkscout.md) | I have a domain. Can I pull the whole GHDB down as flat category files and fire the lot at that domain from one command? | 3 | passive |
| [GitDorker](gitdorker.md) | I have an organisation name or a domain. Which of 500-odd secret-shaped GitHub search patterns return hits when combined with it... | 3 | passive |
| [inurlbr](inurlbr.md) | Can I run a dork across many search engines at once and automatically process the results? | 3 | passive |
| [uDork](udork.md) | I have a domain. Can one bash script walk it through a whole set of prebuilt Google dorks - extensions, URL strings, titles... | 3 | passive |
<!-- END:TOOLS -->

## Related

- [../../07-documents-metadata/harvest-from-web/README.md](../../07-documents-metadata/harvest-from-web/README.md) - dorks are how you find the documents
- [../../06-history-and-archives/web-archive/README.md](../../06-history-and-archives/web-archive/README.md)
