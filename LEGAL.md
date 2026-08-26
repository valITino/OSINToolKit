# Legal and scope

This repository documents tools. It does not authorise their use against any
system. You are responsible for the legality of what you run. Read this before
using anything listed here against a target you do not own.

## The contact model

Every tool in this repo carries a `contact` level. It is the single most
important field for staying on the right side of the law.

| Level | What it means | Authorisation |
|---|---|---|
| `passive` | Never touches the target. Reads archives, certificate transparency logs, registries, and third-party APIs that already hold the data. | None required to look, but see OPSEC and privacy below. |
| `active` | Touches the target in the course of normal use: a DNS query, a single HTTP request, a TLS handshake, a banner grab. | Stay within normal, expected use. Do not assume this is always harmless. |
| `intrusive` | Port scanning, service enumeration, content brute forcing, fuzzing, vulnerability scanning. | **Written authorisation before you start.** No exceptions. |

The boundary between `active` and `intrusive` is not cosmetic. In many
jurisdictions, unauthorised port scanning and content brute forcing are the
line between research and an offence under computer-misuse law. When in doubt,
treat a tool as one level more dangerous than you think it is.

## Written authorisation

Before running anything marked `intrusive` against a system you do not own,
have written authorisation that names:

- the exact targets (hosts, IP ranges, domains) in scope,
- the time window in which testing is permitted,
- the techniques permitted and explicitly excluded,
- a named point of contact on the target side,
- who to notify if you find something serious.

A verbal "sure, go ahead" is not authorisation. Keep the document.

## Privacy law affects the data itself

- **GDPR and WHOIS.** Since the GDPR took effect, WHOIS records for many EU
  domains redact registrant name, email, and address. Empty or "REDACTED FOR
  PRIVACY" fields are the norm for EU registrants, not a sign the domain is
  suspicious. The same applies to EU public records generally: availability
  varies by member state and by the lawful basis you have for processing.
- **Personal data.** People-search, username-enumeration, and email-OSINT
  tools return personal data. Collecting and storing it may itself be regulated
  regardless of how public the source is. Have a lawful basis.

## OPSEC: some passive tools still tip off the subject

Passive does not always mean invisible to the subject.

- Running **Maltego** Transforms, and similar third-party API queries, can
  route through services that log or notify. Some Transforms perform active
  lookups against the target despite the graph looking passive.
- Submitting a URL to a **sandbox** (urlscan.io and similar) fetches the target
  from the sandbox's infrastructure. Searching existing results is passive;
  submitting a new scan is not.
- **Lure tools** (Canarytokens, IPLogger, Grabify) work by inducing a subject
  to contact infrastructure you control. That is an active interaction with a
  person, and in some jurisdictions logging an IP this way has legal weight.
  Use the defensive framing (Canarytokens) and understand the local rules.

If tipping off the subject would compromise an investigation, plan your OPSEC
before the first query, not after.

## Out of scope for this repository

This repo is a discovery and attribution reference. It documents how to find
and correlate information. It deliberately does **not** document:

- exploit code, payloads, or shellcode,
- credential-attack tooling or wordlists for password cracking,
- the brute-force and exploitation features of the tools it lists.

Where a listed tool has such features (WPScan's login brute force, CMSmap's
exploit integration, nmap's more aggressive NSE scripts), those features are
noted as out of scope, not explained.

## No warranty

Tool status notes here are best-effort and go stale. Verify a tool's current
behaviour, licence, and terms of service yourself before you rely on it.
Nothing here is legal advice.
