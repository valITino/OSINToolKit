---
name: Recorded Future Triage (tria.ge)
slug: triage
tier: 2
contact: active
type: web
cost: freemium
platforms: [web, linux, macos, windows]
url: https://tria.ge/
categories: [threat-intel, url-analysis]
tags: [sandbox, malware-config, c2, detonation, corpus-search]
status: active
status_checked: 2026-08-29
---

# Recorded Future Triage (tria.ge)

## What question does it answer?
I have a URL or a file hash. Has anyone already detonated it, what family did it
turn out to be, and what C2 configuration came out of it - searchable by hash,
family, C2 domain, IP or wallet across a public corpus I can read with no account?

## When to reach for it
When the artifact ends in a payload and you want a name for it. The
family-specific config extractors are the draw: they pull C2 addresses, keys and
botnet IDs out of the sample, which is the pivot you take to
[VirusTotal](../../02-network-and-ip/reputation/virustotal.md). Search the public
corpus first; it often answers the question outright.

Not the tool for a phishing page that needs a human to click through - that is
[any-run.md](any-run.md) - nor for a sensitive URL: there is no private option
here at any free tier.

## Install
```bash
# Nothing to install to search or read: /reports/public and /s/<query> need no login.
go install github.com/hatching/triage/go/cmd/triage@latest  # or: pip install hatching-triage
triage authenticate <api-key>   # key appears only on a Researcher account, at /account
```

## Usage
```text
https://tria.ge/reports/public   # live feed of what the world is detonating right now
https://tria.ge/s/family:lumma   # anonymous corpus search: md5:/sha256:/family:/tag:/botnet:/url:/domain:/ip:/wallet:/from:/to:, with AND OR NOT
```
```bash
curl -H 'Authorization: Bearer <KEY>' -X POST -F 'file=@sample.bin' \
  -F '_json={"kind":"file","interactive":true}' https://tria.ge/api/v0/samples  # pauses so you pick a profile
curl -H 'Authorization: Bearer <KEY>' https://tria.ge/api/v0/samples/<ID>/reports/static  # retry on REPORT_NOT_AVAILABLE
```

## Output
A sample page at `/<YYMMDD-random>`: filename, size, the full hash set
(SHA256/MD5/SHA1/SHA512/SSDEEP/TLSH) and a score out of 10. Then Malware Config
with extracted C2 addresses, keys and botnet IDs, and per-task tabs each with
signatures, TTPs, registry and file events, network requests and memory dumps;
PCAPNG downloads contain TLS-MITM-decrypted HTTPS. Score scale: 10 known bad
with a family named, 8-9 likely malicious, 5-7 suspicious with benign uses, 2-4
likely benign, 1 nothing seen, N/A incomplete - and heed the vendor's own
warning to read the signatures that fired, since they produced the number.

## Gotchas
- **Every submission is public and permanent.** Verbatim from the FAQ: "All
  submissions are publicly visible and cannot be deleted." There is no way to
  withdraw a URL you pasted with a victim's token still in the query string.
- The free API key is gated behind an application, not a checkbox. Individual
  gets no API; Researcher adds API, YARA and profiles, but the form demands a
  full organisation postal address, phone, website and a motivation. Web search
  is anonymous, API search is not - `/api/v0/search` unauthenticated gives 401.
- `kind:"url"` executes the URL in a browser; `kind:"fetch"` downloads it as a
  file. Pick wrong and a phishing page fetched as a file looks like inert HTML.
- Samples with no behavioural task are documented as *not* returned by
  `from:`/`to:` searches, so time-boxed sweeps miss them. Statically extracted
  config may be absent from the behavioural report if the C2 was offline: an
  empty network tab is not evidence of no C2. Runtime caps at 3600 s via API.
- Acceptable use is enforced with permanent account loss - no filter
  circumvention, streaming, games, mining or offensive hacking; using the
  sandbox as a free proxy to reach a blocked site gets you banned. Separately,
  the official client has had no commit since 2023-10-09 and PyPI stops at
  0.2.0 while the API changes: the service is active, the client is not.
- Reading is passive; **submitting is active**. For a targeted phishing link the
  detonation itself tells the operator the link was caught.

## Alternatives
- [urlquery.md](urlquery.md) - lighter, and the only one here with a private submission option
- [any-run.md](any-run.md) - when somebody has to click through the lure by hand
- [urlscan.io](../../04-web-exploration/fingerprinting/urlscan-io.md) - page resources rather than payload behaviour
