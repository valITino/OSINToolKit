# Playbook: dorking to documents

**You have:** a domain or an organisation name.
**You want:** the files it published without meaning to, and what their metadata
gives away about the people and systems inside.

Dorking is passive, cheap, and routinely beats scanning: search engines have
already crawled the target, and the files they indexed carry internal usernames,
software versions, paths, and hostnames that no port scan would ever surface.
The chain is always the same - find the documents, keep them, read their
metadata, turn the metadata into leads.

---

## 1. Ask the obvious questions of one engine

```text
site:example.com filetype:pdf                 # published documents
site:example.com filetype:xlsx OR filetype:docx
site:example.com intitle:"index of"           # directory listings
site:example.com inurl:backup OR inurl:old
"@example.com" -site:example.com              # the domain's addresses elsewhere
```

Start from the patterns in the
[Google Hacking Database](../04-web-exploration/dorking/ghdb.md) rather than
inventing dorks from scratch. The operator reference is
[the search-operators cheatsheet](../99-resources/cheatsheets/search-operators.md).

## 2. Ask the other engines the same thing

Different indexes, different answers - and two of the useful operators do not
exist on Google at all:

- Bing's `ip:203.0.113.10` finds indexed pages on one address, including virtual
  hosts you would otherwise miss.
- Yandex's `rhost:com.example.*` covers a domain and its subdomains in a single
  query.

A negative result on one engine is not a negative result. See the cross-engine
table in [the search-operators cheatsheet](../99-resources/cheatsheets/search-operators.md).

## 3. Go around the engines entirely

The indexes only hold what is live today. These hold what was:

- [Wayback CDX API](../06-history-and-archives/web-archive/wayback-cdx-api.md),
  [gau](../06-history-and-archives/web-archive/gau.md) and
  [waybackurls](../06-history-and-archives/web-archive/waybackurls.md) - every
  archived URL, including the documents that were quietly removed
- [Common Crawl](../06-history-and-archives/web-archive/commoncrawl.md) - the
  raw crawl, queryable by URL pattern

```bash
gau example.com | grep -Ei '\.(pdf|docx?|xlsx?|pptx?)$' | sort -u
```

## 4. Automate, carefully

- [pagodo](../04-web-exploration/dorking/pagodo.md) - run GHDB dork sets
- [dorkscout](../04-web-exploration/dorking/dorkscout.md) - the same idea, in Go
- [uDork](../04-web-exploration/dorking/udork.md) - curated dork sets by theme

Automated dorking hits a CAPTCHA wall fast, breaches the engines' terms, and -
since the Bing Search APIs were retired in 2025 - has fewer scripted routes than
the tools' documentation assumes. Slow down, expect blocks, and never automate
through an account or an IP you care about.

## 5. Keep a copy before it moves

- [HTTrack](../04-web-exploration/scraping/httrack.md) for a browsable mirror,
  or the rest of [scraping](../04-web-exploration/scraping/) for targeted
  capture
- Hash and timestamp what you download
  ([documentation](../00-methodology/documentation/README.md))

Take it from the archive rather than the site where you can: no contact, and the
archived copy is the one you can cite later.

## 6. Read the metadata

- [ExifTool](../07-documents-metadata/metadata-extraction/exiftool.md) across
  the whole directory
- [oletools](../07-documents-metadata/office-forensics/oletools.md) and
  [DOCX as ZIP](../07-documents-metadata/office-forensics/docx-as-zip.md) for
  Office files
- [pdf-parser.py](../07-documents-metadata/pdf-forensics/pdf-parser.md) for PDFs

```bash
exiftool -r -Author -Creator -Producer -Software *.pdf *.docx
```

[metagoofil](../07-documents-metadata/harvest-from-web/metagoofil.md) and
[FOCA](../07-documents-metadata/harvest-from-web/foca.md) automate the
find-download-extract loop; check what they still do before relying on them.

## 7. Turn metadata into leads

| Metadata field | What it gives you |
|---|---|
| Author, Last Modified By | Internal usernames and the naming convention |
| Company, Manager | Org structure, and the tenant the file came from |
| Creator / Producer software | Versions, and therefore the build in use |
| File paths in templates | Internal share and hostname conventions |
| Printer names, template names | Site names and departments |

Take usernames to [username enumeration](../08-people-and-identity/username-enum/)
and [email OSINT](../08-people-and-identity/email-osint/); take internal
hostnames to [passive DNS](../03-dns-and-subdomains/passive-dns/) and
[subdomain enumeration](../03-dns-and-subdomains/passive-enum/).

## 8. Do the same to the code hosts

- [GitDorker](../04-web-exploration/dorking/gitdorker.md) - dork sets against
  GitHub search
- [GitHub code search](../09-code-paste-forums/code-search/github-code-search.md)
  and [grep.app](../09-code-paste-forums/code-search/grep-app.md)
- [TruffleHog](../09-code-paste-forums/secret-scanning/trufflehog.md) over
  anything you clone - search hits are not a substitute for scanning history

---

## Boundaries

- **Finding an exposed file is passive. Using it is not.** Credentials found in
  a document are not yours to test; that is where discovery ends and
  unauthorised access begins. See [../LEGAL.md](../LEGAL.md).
- **Documents contain personal data** - authors, addresses, sometimes far worse.
  Handle the corpus accordingly and keep only what the investigation needs.
- **Report exposure through the owner's channel**, not by publishing the dork.
