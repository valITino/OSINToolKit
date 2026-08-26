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
A public key's User IDs are self-asserted identity, and one key often carries several -
a name, a work address, a personal one, an old university address. That makes a
keyserver hit a genuine identity-linking pivot, and creation dates put a floor under how
long an address has been in use.

Know which server you are asking, because they behave very differently now. The old SKS
network accepted anything from anyone, so **keyserver.ubuntu.com** still answers address
searches with unverified User IDs - which is exactly what makes it useful here.
**keys.openpgp.org** deliberately does not: it publishes identity information only after
the address owner has confirmed it by email, and strips User IDs from everyone else's
keys entirely.

**Query both.** Their corpora differ in both directions - each serves keys the other
returns 404 for - so a miss on one is not a result.

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
- **pgp.mit.edu no longer works, despite loading.** The front page and its search form
  render fine, but queries by address or name return HTTP 500 or hang outright. Testing
  liveness by fetching `/` will tell you it is healthy. It is not - treat it as dead and
  fix any script or Dockerfile still passing `--keyserver pgp.mit.edu`.
- **keys.openpgp.org strips identity, not just search results.** Fetch a key by
  fingerprint and you get the key material with **zero User ID packets** unless its owner
  opted in - no name, no address. A 404 by email means "not opted in", never "no such
  key". Email search is exact-match only, by design, so you cannot enumerate a domain.
- **Its email lookups are rate-limited to roughly one a minute** (fingerprint and key-ID
  lookups are far more generous). Bulk address checking there is not viable.
- **SKS-era results are polluted.** The June 2019 certificate-flooding attack
  (CVE-2019-13050) left poisoned keys carrying tens of thousands of appended signatures,
  which can wedge older GnuPG - prefer fetching by full fingerprint over broad searches.
  Short or generic search terms on keyserver.ubuntu.com also return server errors.
- **Anyone can upload a key claiming any address**, with no proof of control, and the
  SKS model is append-only so nothing can ever be deleted. Impersonation keys exist and
  have been used to attribute statements to people who never held the key. Presence
  proves upload - not identity, not current ownership.
- Never import an unknown key into your working keyring - `gpg --show-keys` inspects one
  without touching your trust database.

## Alternatives
- [holehe](../../08-people-and-identity/email-osint/holehe.md) - which services an address registered with
- [Have I Been Pwned](../../08-people-and-identity/email-osint/hibp.md) - which breaches it appears in
- [swaks](swaks.md) - what the mail server itself says about the address
