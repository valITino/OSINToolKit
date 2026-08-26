# OSINT / Cyber-Investigation Toolkit

A reference that maps OSINT and cyber-investigation tools to the questions they
answer. It is built for the moment you are holding one artifact - an IP, a
domain, a photo, an .eml file - and have lost track of which tool does what.
Every tool carries a **tier** (how good and how broad) and a **contact level**
(how much it touches the target). Those two fields are the point of the repo:
they tell you what to master and what is safe to run.

## I have... start here

The primary entry point. You arrive with one artifact; follow the chain.

| I have... | Start at |
|---|---|
| A domain | [`01-orchestrators`](01-orchestrators/) -> [`03-dns-and-subdomains`](03-dns-and-subdomains/) -> [`05-certificates-tls`](05-certificates-tls/) -> [`06-history-and-archives`](06-history-and-archives/) |
| An IP address | [`02-network-and-ip`](02-network-and-ip/) -> [`03-dns-and-subdomains/reverse-dns`](03-dns-and-subdomains/reverse-dns/) |
| An email address | [`01-orchestrators`](01-orchestrators/) -> [`08-people-and-identity/email-osint`](08-people-and-identity/email-osint/) -> [`10-email-investigation`](10-email-investigation/) |
| A username or alias | [`08-people-and-identity/username-enum`](08-people-and-identity/username-enum/) -> [`09-code-paste-forums`](09-code-paste-forums/) |
| A photo | [`08-people-and-identity/reverse-image`](08-people-and-identity/reverse-image/) -> [`07-documents-metadata/metadata-extraction`](07-documents-metadata/metadata-extraction/) |
| A document (PDF/DOCX) | [`07-documents-metadata`](07-documents-metadata/) |
| An .eml file | [`10-email-investigation/header-analysis`](10-email-investigation/header-analysis/) |
| A .pcap file | [`11-traffic-capture`](11-traffic-capture/) |
| Only a company name | [`02-network-and-ip/registries-asn`](02-network-and-ip/registries-asn/) -> [`01-orchestrators`](01-orchestrators/) |

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
  frameworks/           # Kill Chain, MITRE ATT&CK, NIST SP 800-61 / 800-86
  documentation/        # note-taking, screenshots, chain of custody
  opsec/                # VM setup, sock puppets, proxychains, VPN/Tor
01-orchestrators/       # START HERE: multi-purpose, broad coverage
  recursive-scanners/   # SpiderFoot, BBOT
  modular-frameworks/   # recon-ng, Maltego
  aggregators/          # theHarvester, Amass, Sn1per
02-network-and-ip/
  registries-asn/       # whois, RIRs, bgp.he.net, ipinfo.io
  geolocation/          # iplocation.net and multi-source geo
  reputation/           # AbuseIPDB, VirusTotal, IPVoid, ExoneraTor
  port-scanning/        # nmap
  device-search/        # Shodan, Censys, WiGLE
  vuln-scanners/        # nuclei, Greenbone/OpenVAS
03-dns-and-subdomains/
  query-tools/          # dig, host
  passive-enum/         # subfinder, DNSDumpster, Sublist3r
  active-enum/          # fierce
  reverse-dns/          # HackerTarget reverse-DNS API
  typosquatting/        # dnstwist
04-web-exploration/
  fingerprinting/       # BuiltWith, urlscan.io, WhatWeb, wig
  cms-scanners/         # CMSeeK, CMSmap, WPScan
  content-discovery/    # feroxbuster, ffuf, gobuster, dirhunt, wfuzz, DirBuster
  crawling-spidering/   # katana, Photon
  dorking/              # search operators, GHDB, inurlbr
  monitoring-visual/    # VisualPing, VisualSiteMapper, gowitness
  whois-domains/        # viewdns.info
05-certificates-tls/
  ct-log-search/        # crt.sh, MerkleMap
  cert-analysis/        # testssl.sh, openssl
  origin-unmasking/     # CloudFlair
06-history-and-archives/
  web-archive/          # Wayback CDX, waybackurls, gau
  ip-whois-history/     # historical WHOIS / passive DNS
  analytics-linking/    # SpyOnWeb and shared-ID linking
07-documents-metadata/
  metadata-extraction/  # ExifTool, mat2
  harvest-from-web/     # metagoofil, FOCA
  pdf-forensics/        # pdf-parser.py, qpdf, pdfimages, binwalk
  office-forensics/     # oletools
  geo-media/            # geolocating photos and video
08-people-and-identity/
  people-search/        # ThatsThem
  public-records/       # registries and court records
  username-enum/        # Sherlock, Maigret, userrecon
  email-osint/          # holehe, HIBP
  reverse-image/        # Yandex, TinEye, EagleEye
  social-media/         # platform notes
  password-reset-clues/ # methodology, no tool
  ip-luring/            # Canarytokens, IPLogger/Grabify
09-code-paste-forums/
  code-search/          # GitHub code search, SearchCode
  secret-scanning/      # TruffleHog, Gitleaks, Gitrob
  git-history/          # author/email extraction methodology
  paste-sites/          # pastebin and paste search
  forums-wikis/         # forum and wiki history
10-email-investigation/
  header-analysis/      # MXToolbox, Received-header reading
  server-checks/        # SPF/DKIM/DMARC, callback verification, swaks
  tracking/             # open-tracking and token methodology
  spoofing-testing/     # authorised spoof testing
11-traffic-capture/
  capture/              # Wireshark, tshark
  analysis/             # NetworkMiner
  tls-fingerprinting/   # JA3/JA4 methodology
99-resources/
  wordlists/            # pointers to SecLists (not vendored)
  awesome-lists/        # curated external lists
  api-keys/             # which keys are worth paying for
  cheatsheets/          # long-form notes that outgrew a tool file
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
