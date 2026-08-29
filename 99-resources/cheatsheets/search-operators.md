# Search operators, engine by engine

One question, six syntaxes. This is the mapping between them, so that a dork
you worked out on Google can be re-asked of the engine that actually indexed
the thing you want. The [dorking category](../../04-web-exploration/dorking/README.md)
covers the Google basics and the discipline; this file is the cross-engine
reference and the scripted-query syntax.

Checked 2026-08-29. Operator support changes without announcement - when a
query returns nothing, test the operator on a target you know before concluding
the data is not there.

## Web engines: the same question, four ways

| I want | Google | Bing | Yandex | DuckDuckGo |
|---|---|---|---|---|
| Pages on a domain | `site:example.com` | `site:example.com` | `site:example.com` | `site:example.com` |
| A domain and every subdomain | `site:example.com` | `site:example.com` | `rhost:com.example.*` | `site:example.com` |
| One file type | `filetype:pdf` | `filetype:pdf` / `ext:pdf` | `mime:pdf` | `filetype:pdf` |
| A phrase in the title | `intitle:"login"` | `intitle:"login"` | `title:"login"` | `intitle:"login"` |
| A string in the URL | `inurl:admin` | - (`url:` only tests one URL) | `url:*admin*` | `inurl:admin` |
| A phrase in the body | `intext:"internal use"` | `inbody:"internal use"` | - | `intext:"internal use"` |
| Pages hosted on an IP | - | `ip:203.0.113.10` | - | - |
| Pages linking to a file type | - | `contains:pdf` | - | - |
| One language | `lr=lang_de` (URL param) | `language:de` | `lang:de` | - |
| A date range | `after:2024-01-01 before:2025-01-01` | - (UI filter only) | `date:20240101..20250101` | - (UI filter only) |

Universal, on all four: `"exact phrase"`, `-excluded`, `term1 OR term2`,
`(grouping)`, and `*` as a within-phrase wildcard.

**Bing's `ip:` is the one worth remembering.** No other general engine will tell
you which indexed pages sit on a given address, which makes it a free
reverse-IP check that covers virtual hosts a DNS-based lookup misses. Compare
it against [viewdns.info](../../04-web-exploration/whois-domains/viewdns.md) and
[HackerTarget](../../03-dns-and-subdomains/reverse-dns/hackertarget-reversedns.md);
each sees a different slice, and the disagreements are informative.

**Yandex reverses hostnames.** `rhost:com.example.*` covers the domain and all
its subdomains in one query - the closest thing any engine has to a subdomain
operator. Yandex also indexes Cyrillic-script and CIS-hosted content the others
barely touch. Its operator documentation is thin; verify before relying on one.

Microsoft's own advanced-operator reference is archived rather than maintained,
so treat the Bing column as observed behaviour, not a contract.

## What is gone

- **`cache:` on Google and Bing.** Both retired the web cache in 2024. Use
  [Wayback](../../06-history-and-archives/web-archive/wayback-cdx-api.md).
- **The Bing Search APIs.** Retired on 11 August 2025 and decommissioned; the
  replacement, Grounding with Bing Search in Azure AI Agents, feeds an LLM
  rather than returning SERP JSON. Any tool whose multi-engine mode "just
  stopped working" - [inurlbr](../../04-web-exploration/dorking/inurlbr.md) and
  friends - is usually hitting this or a CAPTCHA wall, not a bug you can fix.
- **Google's SOAP and free JSON search APIs.** What remains is the Programmable
  Search Engine (CSE) JSON API: 100 free queries a day, and results scoped to
  the search engine you configure, not the whole web.

## Code hosts

GitHub code search, verified against the current syntax documentation:

```text
org:example-inc "AKIA"                    # a literal, inside one organisation
repo:owner/name path:*.tf "secret_key"    # one repo, one file glob
language:python symbol:decrypt_password   # definitions, not references
/api[_-]?key\s*=\s*["'][A-Za-z0-9]{20,}/  # regex goes between slashes
org:example NOT is:fork NOT is:archived   # boolean, and cut the noise
```

`AND` is implied between terms; `OR`, `NOT` and parentheses are explicit.
Quotes force an exact match, and `content:` restricts a term to file contents
rather than paths. The index is not the whole of GitHub - forks, vendored and
generated files are excluded unless you ask for them, and only indexed branches
are covered - so a negative result here is weak evidence.

For the same job across other hosts see
[Sourcegraph](../../09-code-paste-forums/code-search/sourcegraph.md),
[grep.app](../../09-code-paste-forums/code-search/grep-app.md) and
[SearchCode](../../09-code-paste-forums/code-search/searchcode.md), and run
[TruffleHog](../../09-code-paste-forums/secret-scanning/trufflehog.md) over
anything you clone rather than eyeballing search hits.

## Scan-data engines

These search someone else's scan of the internet, so the syntax is about
service attributes rather than page text. Full detail lives in the tool files;
this is the shape of each.

```text
# Shodan   - see ../../02-network-and-ip/device-search/shodan.md
org:"Example Inc" port:3389
ssl.cert.subject.CN:"example.com" http.title:"Dashboard"

# Censys   - see ../../02-network-and-ip/device-search/censys.md
services.tls.certificates.leaf_data.subject.common_name: "example.com"
host.services.port=8880 and host.autonomous_system.asn=15169
```

Censys now has two dialects: the legacy `services.*` fields on the search UI,
and CenQL (`host.services.*`, with `=` for exact, `:` for tokenised and `=~`
for regex) on the newer platform. A query that returns nothing may simply be
written in the other one.

The favicon trick is worth knowing across all of them: hash a site's favicon
and search for other hosts serving the same one - it links a CDN-fronted site
to its origin. See
[favicon hash pivoting](../../05-certificates-tls/origin-unmasking/favicon-hash.md).

## Bulk indexes you can query like an engine

```bash
# Certificate transparency: every logged name under a domain
curl -s 'https://crt.sh/?q=%25.example.com&output=json' | jq -r '.[].name_value'

# Every archived URL, de-duplicated
curl -s 'https://web.archive.org/cdx/search/cdx?url=example.com*&collapse=digest&fl=original'

# Common Crawl: list the crawls, then query one index for a host pattern
curl -s 'https://index.commoncrawl.org/collinfo.json' | jq -r '.[0].id'
curl -s 'https://index.commoncrawl.org/CC-MAIN-2025-05-index?url=*.example.com&output=json'
```

These three cover ground the engines do not: names that never resolved,
pages that were deleted, and pages nobody linked to. They are also the place to
grep for `.onion` strings when you are looking for a target's hidden services -
see [12-darkweb/onion-discovery](../../12-darkweb/onion-discovery/).

## Discipline

- **Automating an engine's web interface breaches its terms** and will earn a
  CAPTCHA wall within a few dozen queries. Rotate engines, slow down, or use the
  official API where one still exists.
- **Different engines, different indexes.** A negative on Google is not a
  negative. Re-ask Bing, Yandex, and an independent crawler such as Mojeek or
  Marginalia before you write "not found" in a report.
- **Personalisation and geography change results.** Two analysts running the
  same dork see different pages. Record the query, the engine, the date, and a
  screenshot - see [documentation](../../00-methodology/documentation/README.md).
- **Finding a file with a dork is passive; opening what you find may not be.**
  See [LEGAL.md](../../LEGAL.md).
