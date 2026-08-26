---
name: PGP keyservers
slug: pgp-keyservers
tier: 2
contact: passive
type: api
cost: free
platforms: [web, linux, macos, windows]
url: https://keys.openpgp.org/
categories: [email-investigation, server-checks]
tags: [pgp, keyserver, hkp, identity]
status: active
status_checked: 2026-08-26
---

# PGP keyservers

## What question does it answer?
I have an email address. Does this person publish a PGP key - and does that key tie
this address to a real name or to their **other** addresses?

## When to reach for it
A public key's User IDs are self-asserted identity, and one key often carries several
of them: a name, a work address, a personal address, an old university one. That makes
a keyserver hit a genuine identity-linking pivot, and the creation dates put a floor
under how long an address has been in use.

Know which server you are asking, because they behave very differently now. The old
SKS network accepted anything from anyone, so **keyserver.ubuntu.com** still answers
address searches with unverified User IDs - which is exactly what makes it useful here.
**keys.openpgp.org** deliberately does not: it publishes identity information only
after the address owner has confirmed it by email. That is a privacy feature, and it
means an absence there proves nothing.

## Install
```bash
# Nothing required - plain HTTP. gpg is the usual client:
sudo apt install gnupg
```

## Usage
```bash
curl -s 'https://keyserver.ubuntu.com/pks/lookup?op=index&search=alice%40example.com'
curl -s 'https://keys.openpgp.org/pks/lookup?op=index&search=0xFINGERPRINT'
gpg --keyserver hkps://keyserver.ubuntu.com --search-keys alice@example.com
gpg --show-keys downloaded.asc          # inspect a key WITHOUT importing it
```

## Output
An index listing: `pub` lines with algorithm, key size, key ID and creation time; `uid`
lines carrying the name and email; `sig` lines for certifications. The uid lines are the
prize - one key showing three addresses links three addresses. Creation and expiry dates
give you a timeline.

## Gotchas
- **pgp.mit.edu is broken for search.** Its front page loads and key-ID lookups answer,
  but `op=index` searches by address or name return HTTP 500 "Error handling request".
  Do not rely on it, and do not read a failure there as "no key exists".
- **keys.openpgp.org returns 404 for an address search unless the owner verified it.**
  Fingerprint lookups work fine. It also strips third-party signatures, so there is no
  web-of-trust graph to walk there any more.
- **SKS-era results are polluted.** The 2019 certificate-flooding attacks left duplicate
  and spam keys behind: a single address can return several near-identical keys created
  minutes apart. Name searches on keyserver.ubuntu.com currently return a server error.
- **Anyone can upload a key claiming any address.** A uid is an assertion, not proof.
  Corroborate before treating a name as identification.
- Uploads are effectively permanent and were never deletable on the old network, so a
  key may reflect an identity from a decade ago.
- Never import an unknown key into your working keyring. `gpg --show-keys` inspects it
  without touching your trust database.

## Alternatives
- [holehe](../../08-people-and-identity/email-osint/holehe.md) - which services an address registered with
- [Have I Been Pwned](../../08-people-and-identity/email-osint/hibp.md) - which breaches it appears in
- [swaks](swaks.md) - what the mail server itself says about the address
