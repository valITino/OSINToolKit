---
name: dark.fail
slug: dark-fail
tier: 2
contact: passive
type: web
cost: free
platforms: [web]
url: https://dark.fail/
categories: [darkweb, onion-discovery]
tags: [tor, onion, directory, pgp, phishing, uptime]
status: active
status_checked: 2026-08-29
---

# dark.fail

## What question does it answer?
I have the name of a well-known hidden service and an address someone handed me
for it. Is that the real, PGP-signed .onion for the site, and is the service up
right now?

## When to reach for it
When you know what the service is called and need the canonical address rather
than a candidate - phishing clones of prominent onions are the norm and this is
an authority file built to defeat them. It is not a discovery tool: 32 addresses
in total, so a missing target proves nothing. Start from [Ahmia](ahmia.md) for
keyword discovery, and [Tor.taxi](tor-taxi.md) for the categories omitted here.

## Install
```bash
# None: static clearweb page, no account, no JavaScript. You need GnuPG to
# verify the signed listings, and Tor Browser to open anything you find:
sudo apt install gnupg          # see ../access-and-opsec/tor-browser.md
```

## Usage
```text
https://dark.fail/
  # the whole product: one page, ~32 canonical onions, per-entry Online/Offline
  # status and a UTC "Updated" timestamp in the header
https://dark.fail/pgp.txt
  # the admin key - fetch it, then verify the signed listing before you trust
  # any address you copied off the page. Skipping this discards the entire point
https://dark.fail/pgp-sigs.txt   # key rotation history - check it before
  # trusting a key you cached on an earlier visit
```

## Output
One flat HTML page: site names, each followed by its full v3 .onion as plain
unclickable text, "Offline" beside anything failing the uptime check, a
last-refresh timestamp in the header and an alert bar carrying seizure news.
Read it as an authority file, not a search engine: you arrive knowing the name
and leave with the address that is cryptographically vouched for. Offline is a
snapshot at that timestamp, not a seizure - mainstream newsrooms were flagged
Offline here on 2026-08-29.

## Gotchas
- **Unverified, it is just a listicle.** The value is the signature. Fetch
  `/pgp.txt`, check it against `/pgp-sigs.txt`, verify the signed listing; a
  copy-pasted address carries the same phishing risk as any other directory.
- **Heavy typosquatting.** Clone domains rank in search results, and the site's
  own footer warns that its name always has a dot between the two words. Only
  dark.fail and its published onion mirror are canonical.
- Links are deliberately unclickable to prevent accidental clearnet lookups; do
  not defeat that by pasting one into a normal browser, or you leak the lookup
  to your resolver and the site's CDN. Use the onion mirror if that matters.
- Curated by email to the admin with no published criteria, so you cannot audit
  why something is listed - and the site says it vouches for nothing it lists.
- Uptime is checked by dark.fail, not you: re-read the header timestamp before
  quoting an Online/Offline state in a report.
- **The page indexes criminal services alongside newsrooms.** Reading it is
  passive; opening a listing is active, logged by the operator, and can expose
  you to illegal material that arrives unbidden - downloading it is an offence
  in most jurisdictions whatever your intent, and finding it brings reporting
  duties. Read [../../LEGAL.md](../../LEGAL.md) first.

## Alternatives
- [Tor.taxi](tor-taxi.md) - wider, categorised, also PGP-signed, but undated
- [Ahmia](ahmia.md) - keyword search and a bulk seed list when you have no name
- [Intelligence X](intelligence-x.md) - archived copies of onion content
