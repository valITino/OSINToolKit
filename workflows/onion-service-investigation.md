# Playbook: onion service investigation

**You have:** a `.onion` address, or a claim that a target runs one.
**You want:** what the service is, whether it is what it claims, and what links
it to infrastructure or people outside Tor.

The whole game is operational mistakes. Tor hides the server's address; it does
not hide a reused analytics ID, a favicon copied from the clearweb site, an SSH
host key presented on both, or the EXIF in an uploaded photo. Work outward from
the artifacts, not inward from the address.

Read the dark web section of [../LEGAL.md](../LEGAL.md) first. Everything from
step 3 onwards is `active` contact with a service whose operator may be watching
for exactly that.

---

## 1. Ask the clearweb first

Nothing here touches the service, and it often answers the question outright.

- [Ahmia](../12-darkweb/onion-discovery/ahmia.md) and the other indexes - has a
  crawler already seen it, and what did it hold?
- [Intelligence X](../12-darkweb/onion-discovery/intelligence-x.md) - historical
  copies of onion pages, pastes, and leaked data mentioning the address
- [Certificate transparency](../05-certificates-tls/ct-log-search/) - onion names
  do appear in CT logs
- The bulk indexes: grep archived pages and crawl data for the address itself.
  See [onion discovery](../12-darkweb/onion-discovery/README.md) for the regex
  and the sources.

Record every mention with its date. A first-seen date from an index is often the
only timeline you will get.

## 2. Isolate before you connect

- [Tor Browser](../12-darkweb/access-and-opsec/tor-browser.md) for looking
- [Tails](../12-darkweb/access-and-opsec/tails.md) or
  [Whonix](../12-darkweb/access-and-opsec/whonix.md) for anything sensitive
- [torsocks](../12-darkweb/access-and-opsec/torsocks.md) to push CLI tools
  through the same circuit

Nothing on that machine may identify you or your organisation. No logins, no
personal browser profile, no corporate VPN. See
[OPSEC](../00-methodology/opsec/README.md).

## 3. Confirm it is live without rendering it

A headless probe tells you whether the service answers, what it serves, and its
title - without a browser fetching images and scripts you did not ask for.

```bash
torsocks curl -sI http://<address>.onion            # status and headers only
httpx -proxy socks5://127.0.0.1:9050 -title -status-code -tech-detect
```

If it does not answer, that means nothing on its own: hidden services go down
for an hour, get rebuilt at a new address, or get seized. Record the attempt and
the time; try again later.

## 4. Crawl, and keep a copy

- [TorBot](../12-darkweb/active-crawling/torbot.md) or
  [darkdump](../12-darkweb/active-crawling/darkdump.md) for onion-aware crawling
- A general crawler over the same SOCKS proxy is often better maintained -
  see [crawling and spidering](../04-web-exploration/crawling-spidering/)
- Keep the raw responses, not just extracted text -
  [scraping](../04-web-exploration/scraping/)

Throttle. Hidden services are usually one small box, and hammering one is both
obvious to the operator and closer to a denial of service than to research.

## 5. Harvest the correlatable artifacts

This is the step that produces attribution.

| Look for | Then pivot with |
|---|---|
| Analytics and ad IDs in the HTML | [analytics linking](../06-history-and-archives/analytics-linking/) |
| The favicon and distinctive static assets | [favicon hash pivoting](../05-certificates-tls/origin-unmasking/favicon-hash.md) |
| Server banners, error pages, directory listings | [device search](../02-network-and-ip/device-search/) |
| SSH host keys, TLS certificates | [device search](../02-network-and-ip/device-search/), [CT logs](../05-certificates-tls/ct-log-search/) |
| Images and documents | [metadata extraction](../07-documents-metadata/metadata-extraction/) |
| PGP keys, handles, contact addresses | [username enumeration](../08-people-and-identity/username-enum/) |
| Cryptocurrency addresses | reuse across sites, and chain analysis (out of scope here) |

[OnionScan](../12-darkweb/active-crawling/onionscan.md) automates several of
these checks and its findings list is still the best statement of what to look
for, even where the code has aged.

## 6. Take each artifact back to the clearweb

An analytics ID or favicon hash from step 5 becomes a search:

- The same ID on a clearweb site - [PublicWWW](../06-history-and-archives/analytics-linking/publicwww.md),
  [SpyOnWeb](../06-history-and-archives/analytics-linking/spyonweb.md)
- The same favicon or banner on a scanned host -
  [Shodan](../02-network-and-ip/device-search/shodan.md),
  [Censys](../02-network-and-ip/device-search/censys.md)
- The candidate host's history -
  [passive DNS](../03-dns-and-subdomains/passive-dns/),
  [IP and WHOIS history](../06-history-and-archives/ip-whois-history/)

A hit here is a hypothesis: "this clearweb host may be the same box". Test it
against timing, certificate reuse, and content, and say how strong it is.

## 7. Argue against your own conclusion

- Is the "same" ID or asset simply copied from a template that hundreds of sites
  use?
- Is the site a phishing clone of the service you think you are looking at?
  Mirrors are routinely impostors - check any signature the operator published.
- Does the timeline hold: did the clearweb host and the hidden service overlap?
- Would a second explanation fit the same evidence?

## 8. Record, then watch

Screenshot, hash, and timestamp everything as you go
([documentation](../00-methodology/documentation/README.md)); hidden services
disappear and the archives do not cover them. If the case is ongoing, set a
re-check cadence rather than a one-off look, and track the operator's other
addresses through [onion discovery](../12-darkweb/onion-discovery/).

---

## Where this playbook stops

- **No interaction.** No accounts, no messages, no uploads, no purchases. That
  is undercover activity, not observation, and in most jurisdictions it is
  reserved for law enforcement acting under authorisation.
- **No downloading of criminal material,** including leaked corpora. See the
  dark web section of [../LEGAL.md](../LEGAL.md), which also covers what to do
  if illegal imagery appears.
- **No port scanning** the service. It is reached through the Tor daemon rather
  than its own address, so the results mean little - and scanning is `intrusive`
  and needs authorisation regardless.
