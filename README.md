# OSINT / Cyber-Investigation Toolkit

A reference that maps OSINT and cyber-investigation tools to the questions they
answer. It is built for the moment you are holding one artifact - an IP, a
domain, a photo, an .eml file - and have lost track of which tool does what.
Every tool carries a **tier** (how good and how broad) and a **contact level**
(how much it touches the target). Those two fields are the point of the repo:
they tell you what to master and what is safe to run.

## I have... start here

The primary entry point. You arrive with one artifact; follow the chain. Every
destination is a category README that explains what the tools there are for.

### An artifact

| I have... | Start at |
|---|---|
| A domain | [`01-orchestrators`](01-orchestrators/) -> [`03-dns-and-subdomains`](03-dns-and-subdomains/) -> [`05-certificates-tls`](05-certificates-tls/) -> [`06-history-and-archives`](06-history-and-archives/) |
| An IP address | [`02-network-and-ip`](02-network-and-ip/) -> [`03-dns-and-subdomains/reverse-dns`](03-dns-and-subdomains/reverse-dns/) |
| A netblock or an ASN | [`02-network-and-ip/registries-asn`](02-network-and-ip/registries-asn/) -> [`03-dns-and-subdomains/reverse-dns`](03-dns-and-subdomains/reverse-dns/) |
| An email address | [`01-orchestrators`](01-orchestrators/) -> [`08-people-and-identity/email-osint`](08-people-and-identity/email-osint/) -> [`10-email-investigation`](10-email-investigation/) |
| A username or alias | [`08-people-and-identity/username-enum`](08-people-and-identity/username-enum/) -> [`09-code-paste-forums`](09-code-paste-forums/) |
| A person's name or phone number | [`08-people-and-identity/people-search`](08-people-and-identity/people-search/) -> [`08-people-and-identity/public-records`](08-people-and-identity/public-records/) |
| A photo | [`08-people-and-identity/reverse-image`](08-people-and-identity/reverse-image/) -> [`07-documents-metadata/metadata-extraction`](07-documents-metadata/metadata-extraction/) -> [`07-documents-metadata/geo-media`](07-documents-metadata/geo-media/) |
| A document (PDF/DOCX) | [`07-documents-metadata`](07-documents-metadata/) |
| An Office file that may carry macros | [`07-documents-metadata/office-forensics`](07-documents-metadata/office-forensics/) |
| An .eml file | [`10-email-investigation/header-analysis`](10-email-investigation/header-analysis/) |
| A .pcap file | [`11-traffic-capture`](11-traffic-capture/) |
| A URL I must not click | [`13-threat-intel/url-analysis`](13-threat-intel/url-analysis/) -> [`04-web-exploration/fingerprinting`](04-web-exploration/fingerprinting/) -> [`06-history-and-archives/web-archive`](06-history-and-archives/web-archive/) |
| A .onion address | [`12-darkweb/onion-discovery`](12-darkweb/onion-discovery/) -> [`12-darkweb/active-crawling`](12-darkweb/active-crawling/) |
| A file, or just its hash | [`13-threat-intel/file-and-hash`](13-threat-intel/file-and-hash/) -> [`07-documents-metadata`](07-documents-metadata/) |
| A paste or pastebin link | [`09-code-paste-forums/paste-sites`](09-code-paste-forums/paste-sites/) |
| A tracking, Analytics or AdSense ID | [`06-history-and-archives/analytics-linking`](06-history-and-archives/analytics-linking/) |
| A registrant name, email or phone | [`04-web-exploration/whois-domains`](04-web-exploration/whois-domains/) -> [`06-history-and-archives/ip-whois-history`](06-history-and-archives/ip-whois-history/) |
| Only a company name | [`02-network-and-ip/registries-asn`](02-network-and-ip/registries-asn/) -> [`01-orchestrators`](01-orchestrators/) |

### A situation

Sometimes the starting point is a question rather than a thing.

| I need to work out... | Start at |
|---|---|
| What this organisation exposes to the internet | [`02-network-and-ip/device-search`](02-network-and-ip/device-search/) -> [`02-network-and-ip/port-scanning`](02-network-and-ip/port-scanning/) |
| What is really behind this CDN | [`05-certificates-tls/origin-unmasking`](05-certificates-tls/origin-unmasking/) -> [`06-history-and-archives/ip-whois-history`](06-history-and-archives/ip-whois-history/) |
| What this page used to say | [`06-history-and-archives/web-archive`](06-history-and-archives/web-archive/) |
| Which lookalike domains target this brand | [`03-dns-and-subdomains/typosquatting`](03-dns-and-subdomains/typosquatting/) -> [`05-certificates-tls/ct-log-search`](05-certificates-tls/ct-log-search/) |
| Whether mail from this domain can be forged | [`10-email-investigation/server-checks`](10-email-investigation/server-checks/) |
| Whether this organisation has leaked secrets | [`09-code-paste-forums/code-search`](09-code-paste-forums/code-search/) -> [`09-code-paste-forums/secret-scanning`](09-code-paste-forums/secret-scanning/) -> [`09-code-paste-forums/paste-sites`](09-code-paste-forums/paste-sites/) |
| Which sites share an owner with this one | [`06-history-and-archives/analytics-linking`](06-history-and-archives/analytics-linking/) -> [`03-dns-and-subdomains/reverse-dns`](03-dns-and-subdomains/reverse-dns/) |
| What search engines already indexed | [`04-web-exploration/dorking`](04-web-exploration/dorking/) -> [`99-resources/cheatsheets/search-operators.md`](99-resources/cheatsheets/search-operators.md) |
| What this name resolved to years ago | [`03-dns-and-subdomains/passive-dns`](03-dns-and-subdomains/passive-dns/) |
| Whether this organisation is named on a ransomware leak site | [`12-darkweb/leak-monitoring`](12-darkweb/leak-monitoring/) |
| Which hidden services mention this brand, and where their addresses leak | [`12-darkweb/onion-discovery`](12-darkweb/onion-discovery/) |
| Whether this infrastructure is already known-bad to someone else | [`13-threat-intel/feeds-and-trackers`](13-threat-intel/feeds-and-trackers/) |
| How to keep a copy of this site before it changes | [`04-web-exploration/scraping`](04-web-exploration/scraping/) |

For the three most common cases there are full playbooks in
[`workflows/`](workflows/) that chain the tools in order and explain why the
order is what it is: [domain investigation](workflows/domain-investigation.md),
[phishing email triage](workflows/phishing-email-triage.md), and
[username to identity](workflows/username-to-identity.md).

## Tier 1 - the twelve daily drivers

Broad, well-maintained, worth mastering. If you learn twelve tools, learn these.

| Tool | Contact | Why it earns the slot |
|---|---|---|
| [SpiderFoot](01-orchestrators/recursive-scanners/spiderfoot.md) | active | 200+ modules correlate domain/IP/email/person into one graph; the broad first pass |
| [BBOT](01-orchestrators/recursive-scanners/bbot.md) | active | SpiderFoot's concept, async and CLI-first; typically finds more subdomains, scriptable |
| [Maltego](01-orchestrators/modular-frameworks/maltego.md) | passive | Industry standard for *presenting* link analysis to non-technical stakeholders |
| [theHarvester](01-orchestrators/aggregators/theharvester.md) | passive | One command, very broad email/subdomain/host sweep; the fast first look |
| [recon-ng](01-orchestrators/modular-frameworks/recon-ng.md) | passive | Workspace database persists across sessions - built for real casework |
| [OWASP Amass](01-orchestrators/aggregators/amass.md) | active | Deepest DNS/ASN/netblock asset model; maps an org's true footprint |
| [nmap](02-network-and-ip/port-scanning/nmap.md) | intrusive | The quasi-standard for ports/services/OS; nothing has replaced it |
| [ExifTool](07-documents-metadata/metadata-extraction/exiftool.md) | passive | Metadata from hundreds of file formats; the first move on any file |
| [crt.sh](05-certificates-tls/ct-log-search/crt-sh.md) | passive | Subdomains and cert history from CT logs without touching the target |
| [Wayback CDX API](06-history-and-archives/web-archive/wayback-cdx-api.md) | passive | Every historical URL as a greppable list; deleted pages and forgotten files |
| [Wireshark / tshark](11-traffic-capture/capture/wireshark-tshark.md) | passive | Capture plus bulk field extraction; tshark + awk beats the GUI at scale |
| [dnstwist](03-dns-and-subdomains/typosquatting/dnstwist.md) | passive | Typosquat/homoglyph generation with live checking; instant phishing/brand work |

Everything else is tier 2 (best-in-class specialist) or tier 3 (situational or
legacy - kept, but the file says why). See [INDEX.md](INDEX.md) for the full,
sortable list once the build script has run.

## Directory tree

```text
00-methodology/         # how to work: frameworks, documentation, OPSEC
  documentation/        # note-taking, screenshots, chain of custody
  frameworks/           # Kill Chain, MITRE ATT&CK, NIST SP 800-61 / 800-86
  opsec/                # proxychains
01-orchestrators/       # START HERE: multi-purpose, broad coverage
  aggregators/          # OWASP Amass, theHarvester, Sn1per
  modular-frameworks/   # Maltego, recon-ng
  recursive-scanners/   # BBOT, SpiderFoot
02-network-and-ip/
  device-search/        # Censys, Shodan, WiGLE, ZoomEye
  geolocation/          # IP2Location, MaxMind GeoLite2, iplocation.net
  port-scanning/        # nmap, masscan, naabu
  registries-asn/       # RIR databases (ARIN / RIPE / APNIC), bgp.he.net, ipinfo.io, whois
  reputation/           # AbuseIPDB, ExoneraTor, IPVoid, VirusTotal
  vuln-scanners/        # Greenbone / OpenVAS, Rapid7 Nexpose, Tenable Nessus, nuclei
03-dns-and-subdomains/
  active-enum/          # dnsmap, fierce, massdns, puredns
  passive-enum/         # DNSDumpster, subfinder, Sublist3r
  query-tools/          # dig, dnsx, host, nslookup
  reverse-dns/          # HackerTarget reverse DNS API, Robtex, hakrevdns
  typosquatting/        # dnstwist, Namedroppers
04-web-exploration/
  cms-scanners/         # CMSeeK, CMSmap, WPScan
  content-discovery/    # dirhunt, feroxbuster, ffuf, gobuster, DirBuster, wfuzz
  crawling-spidering/   # Photon, hakrawler, katana
  dorking/              # Google Hacking Database, pagodo, inurlbr
  fingerprinting/       # BuiltWith, WhatWeb, urlscan.io, wig
  monitoring-visual/    # VisualPing, VisualSiteMapper, gowitness
  whois-domains/        # DomainTools, Whoisology, viewdns.info
05-certificates-tls/
  cert-analysis/        # SSLyze, openssl, testssl.sh
  ct-log-search/        # crt.sh, CertWatch, MerkleMap
  origin-unmasking/     # Favicon hash pivoting, CloudFail, CloudFlair
06-history-and-archives/
  analytics-linking/    # DNSlytics, NerdyData, PublicWWW, SpyOnWeb
  ip-whois-history/     # Netcraft Site Report, SecurityTrails
  web-archive/          # Wayback CDX API, archive.today, gau, waybackurls
07-documents-metadata/
  geo-media/            # geolocating photos and video
  harvest-from-web/     # FOCA, metagoofil
  metadata-extraction/  # ExifTool, exiv2, mat2
  office-forensics/     # DOCX as ZIP, oledump.py, oletools
  pdf-forensics/        # binwalk, pdf-parser.py, pdfimages, qpdf
08-people-and-identity/
  email-osint/          # Have I Been Pwned, holehe, hunter.io
  ip-luring/            # Canarytokens, IPLogger / Grabify
  password-reset-clues/ # methodology, no tool
  people-search/        # BeenVerified, Pipl, Spokeo, ThatsThem
  public-records/       # registries and court records
  reverse-image/        # Google Lens, TinEye, Yandex Images, EagleEye
  social-media/         # platform notes
  username-enum/        # Maigret, Sherlock, WhatsMyName, userrecon
09-code-paste-forums/
  code-search/          # GitHub code search, Sourcegraph, grep.app, SearchCode
  forums-wikis/         # forum and wiki history
  git-history/          # author/email extraction methodology
  paste-sites/          # Pastebin, PrivateBin, paaster
  secret-scanning/      # Gitleaks, TruffleHog, Gitrob
10-email-investigation/
  header-analysis/      # MXToolbox, Google Messageheader, IP2Location Email Tracer
  server-checks/        # PGP keyservers, checkdmarc, swaks
  spoofing-testing/     # authorised spoof testing
  tracking/             # open-tracking and token methodology
11-traffic-capture/
  analysis/             # NetworkMiner, Zeek
  capture/              # Wireshark / tshark, tcpdump
  tls-fingerprinting/   # JA3/JA4 methodology
99-resources/
  api-keys/             # which keys are worth paying for
  awesome-lists/        # curated external lists
  cheatsheets/          # long-form notes that outgrew a tool file
  wordlists/            # pointers to SecLists (not vendored)
workflows/              # end-to-end playbooks chaining the tools in order
scripts/                # build-index.py, check-links.py (stdlib only)
templates/              # the empty tool schema
```

## Legal and scope

This repository documents tools; it does not authorise their use. Read
[LEGAL.md](LEGAL.md) before running anything against a target you do not own.

- `passive` never touches the target. `active` touches it normally (a DNS query,
  one HTTP request). `intrusive` means scanning, fuzzing, or brute forcing and
  **requires written authorisation**.
- Privacy law shapes the data itself: GDPR redacts WHOIS for EU registrants and
  limits EU public records. Some passive tools (Maltego Transforms, sandbox
  submissions, lure tokens) can still tip off a subject - plan OPSEC first.
- Dark web work adds exposure the rest of the repo does not have: illegal
  material appears unbidden and a rendered page is a cached copy, a leak-site
  dump is still personal data, and registering or buying is not observation.
  [`12-darkweb`](12-darkweb/) documents observation only - read the dark web
  section of [LEGAL.md](LEGAL.md) before the first connection.
- This is a **discovery and attribution** reference. Exploit code, payloads, and
  credential-attack tooling are deliberately out of scope; where a listed tool
  has such features, they are named as out of scope, not documented.

## Contributing

New tools follow one rule: the file must answer *"what question does it answer?"*
in the investigator's voice. See [CONTRIBUTING.md](CONTRIBUTING.md) for the
frontmatter schema and the tier/contact definitions, and
[templates/tool-template.md](templates/tool-template.md) to start a file. Run
`python3 scripts/build-index.py` before committing so [INDEX.md](INDEX.md) and the
category tables stay current.
