# Active crawling

You have an address and the passive sources are exhausted. Everything here
connects: the hidden service receives your request, sees a Tor circuit, and can
log, fingerprint, rate-limit, or feed you different content because of it.
Treat every tool in this directory as `active` even when it feels like reading.

## Before you connect

- Work from the isolation set up in [../access-and-opsec/](../access-and-opsec/),
  never from your host.
- Decide what you are looking for first. "Have a look around" is how an analyst
  ends up rendering something they cannot unsee, and how a crawler ends up
  hammering a service until the operator notices.
- Fetch, do not interact. Crawling reads what is served to anyone; posting,
  registering, or messaging is a different activity with a different legal
  footing - see [../../LEGAL.md](../../LEGAL.md).
- Rate-limit hard. Tor is slow, hidden services are often a single box, and an
  aggressive crawl is both obvious and closer to a denial of service than to
  research.

## What you are actually collecting

The point of crawling a hidden service is rarely the text. It is the operational
residue that links the service to something outside Tor:

| Artifact | What it can link to |
|---|---|
| Analytics and advertising IDs | Clearweb sites with the same ID - [../../06-history-and-archives/analytics-linking/](../../06-history-and-archives/analytics-linking/) |
| Favicon, or a distinctive asset | Other hosts serving the same file - [../../05-certificates-tls/origin-unmasking/favicon-hash.md](../../05-certificates-tls/origin-unmasking/favicon-hash.md) |
| Server banners and default pages | A misconfigured clearweb twin of the same box |
| SSH host keys and certificates | The same key presented on a clearweb IP |
| Images and documents | EXIF, authorship, and software fingerprints - [../../07-documents-metadata/](../../07-documents-metadata/) |
| PGP keys, usernames, contact handles | People - [../../08-people-and-identity/](../../08-people-and-identity/) |
| Cryptocurrency addresses | Chain analysis, and reuse across sites |

Nothing in that table is proof on its own. A shared analytics ID or a reused
handle is a lead to corroborate, and the same shared-hosting caveats apply here
as anywhere else in this repo.

## Tool caveats specific to this work

- Most onion-specific tooling is old. The techniques still hold; the code often
  does not build without patching, and several projects target the v2 addresses
  that were removed from the network in 2021. Check what a tool assumes about
  address format before trusting an empty result.
- General-purpose crawlers work fine over Tor when pointed at a SOCKS proxy, and
  are usually better maintained than the onion-branded ones. See
  [../../04-web-exploration/crawling-spidering/](../../04-web-exploration/crawling-spidering/)
  and torsocks in [../access-and-opsec/](../access-and-opsec/).
- Scanning a hidden service for open ports is largely meaningless - the service
  is reached through the Tor daemon, not through its own IP - and any port
  scanning is `intrusive` and needs authorisation like anywhere else.

## Tools here

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [TorBot](torbot.md) | I have a .onion address. What does it link out to one or two hops deep, which of those pages are alive right now, and do any of... | 2 | active |
| [darkdump](darkdump.md) | I have a keyword, a brand or an email address. Which onions come back for it across six dark-web search engines, which of those... | 3 | active |
| [docker-onion-nmap](onion-nmap.md) | I have a .onion address and the web page is only part of it. What else answers on that service - SSH, SMTP, an admin panel on a... | 3 | intrusive |
| [OnionScan](onionscan.md) | I have a .onion address. Is the operator leaking themselves - a status page, an open directory, EXIF in an uploaded image, a PGP... | 3 | intrusive |
<!-- END:TOOLS -->

## Related

- [../onion-discovery/](../onion-discovery/) - where the address came from
- [../../04-web-exploration/scraping/](../../04-web-exploration/scraping/) - keeping a copy of what you found
- [../../00-methodology/documentation/README.md](../../00-methodology/documentation/README.md) - recording it so it survives the site
