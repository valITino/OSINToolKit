# 12 - Dark web

You have an onion address, a leak-site claim, or a suspicion that something
about your organisation is circulating where you cannot search for it. This
category covers observing hidden services and what gets published on them -
finding addresses, crawling them, fingerprinting them, and watching the leak
sites from a safe distance.

Split the work the way the rest of this repo splits it. **Passive** means
somebody else already collected it: clearweb-hosted onion search engines, leak
aggregators, indexes, and leaked-paste search. **Active** means you connect and
the hidden service logs a request from a Tor exit into its own service - a real
interaction with an operator who may be monitoring for exactly that.

Read the dark web section of [../LEGAL.md](../LEGAL.md) before the first
connection. Two facts drive everything here: illegal material appears without
warning and a rendered page is a cached copy on your disk, and the line between
observing a criminal service and interacting with one is thinner than it looks.
This repo documents observation only.

## Subcategories

- [access-and-opsec/](access-and-opsec/) - Tor Browser, Tails, Whonix, torsocks - get there without carrying your identity
- [onion-discovery/](onion-discovery/) - Ahmia, OnionSearch, dark.fail, Intelligence X - find the address in the first place
- [active-crawling/](active-crawling/) - TorBot, OnionScan, darkdump - touch the service, map it, fingerprint it
- [leak-monitoring/](leak-monitoring/) - RansomLook, Ransomware.live, ransomwatch - what criminals publish, watched from the clearweb

## The order that keeps you out of trouble

1. **Ask the clearweb first.** Most of what an investigation needs about a
   hidden service is already on the clearweb: an indexer crawled it, a
   researcher screenshotted it, a leak aggregator recorded the victim list. None
   of that touches the service.
2. **Then connect, from a disposable machine.** An amnesic or compartmentalised
   OS, not your host. Nothing on it that identifies you or your organisation.
3. **Look, do not interact.** No accounts, no messages, no purchases, no
   uploads. Registration is where observation ends and undercover work begins,
   and that is not a decision for an analyst to take alone.
4. **Record as you go.** Hidden services vanish and the archives do not cover
   them. Your timestamped notes and hashes are usually the only evidence that
   will survive - see [../00-methodology/documentation/README.md](../00-methodology/documentation/README.md).

## Three things that are true here and nowhere else

- **Nothing is what it claims to be.** Mirrors are routinely phishing clones of
  the site they impersonate, and directories exist mainly to publish signed
  addresses so you can tell the difference. Verify a mirror against a signature
  the operator published, or treat what you see as unattributed.
- **Uptime is meaningless as a signal.** A service that does not answer may be
  seized, rebuilt at a new address, or simply offline for an hour. Absence
  proves nothing; record the attempt and re-check.
- **The interesting artifacts are the operational mistakes.** Reused analytics
  IDs, a favicon, an SSH host key, PGP keys, cryptocurrency addresses, and EXIF
  in uploaded images are what link a hidden service back to clearweb
  infrastructure. That is why
  [../06-history-and-archives/analytics-linking/](../06-history-and-archives/analytics-linking/)
  and [../05-certificates-tls/origin-unmasking/](../05-certificates-tls/origin-unmasking/)
  matter as much here as any onion-specific tool.

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [Ahmia](onion-discovery/ahmia.md) | I have a keyword - a victim name, a brand, a handle. Which indexed Tor hidden services mention it, when was each last seen alive... | 2 | passive |
| [dark.fail](onion-discovery/dark-fail.md) | I have the name of a well-known hidden service and an address someone handed me for it. Is that the real, PGP-signed .onion for... | 2 | passive |
| [Intelligence X](onion-discovery/intelligence-x.md) | I have a selector - an email address, a domain, a .onion host, an IP or a Bitcoin address. Where has it appeared in archived... | 2 | passive |
| [RansomLook](leak-monitoring/ransomlook.md) | I have an organisation name or domain. Which crew has claimed it, when, and what else do they publish - without me ever loading... | 2 | passive |
| [Ransomware.live](leak-monitoring/ransomware-live.md) | I have a company name, a country or an encrypted-file extension. Has this organisation been named on a leak site, and what do... | 2 | passive |
| [Tails](access-and-opsec/tails.md) | I have an onion address to open from a machine I do not fully trust, and this session must leave nothing behind on its disk when... | 2 | active |
| [Tor Browser](access-and-opsec/tor-browser.md) | I have a .onion address, or a clearweb page I do not want to hand my real IP. What do I open it in so the service sees a Tor exit... | 2 | active |
| [TorBot](active-crawling/torbot.md) | I have a .onion address. What does it link out to one or two hops deep, which of those pages are alive right now, and do any of... | 2 | active |
| [torsocks](access-and-opsec/torsocks.md) | I have a CLI tool with no `--proxy` flag and a .onion address to point it at. How do I force its traffic and its DNS through Tor... | 2 | active |
| [Whonix](access-and-opsec/whonix.md) | I have a whole toolkit to point at an onion service, not just a browser, and one careless tool or one hostile page must not be... | 2 | active |
| [darkdump](active-crawling/darkdump.md) | I have a keyword, a brand or an email address. Which onions come back for it across six dark-web search engines, which of those... | 3 | active |
| [DarkOwl](leak-monitoring/darkowl.md) | I have a client name, domain or credential. Where does it appear across leak sites, markets, forums and Telegram, and can I still... | 3 | passive |
| [docker-onion-nmap](active-crawling/onion-nmap.md) | I have a .onion address and the web page is only part of it. What else answers on that service - SSH, SMTP, an admin panel on a... | 3 | intrusive |
| [OnionScan](active-crawling/onionscan.md) | I have a .onion address. Is the operator leaking themselves - a status page, an open directory, EXIF in an uploaded image, a PGP... | 3 | intrusive |
| [OnionSearch](onion-discovery/onionsearch.md) | I have a keyword and a list of onion search engines. Which of them return a hit for it, collected into one CSV - and, read... | 3 | active |
| [ransomwatch](leak-monitoring/ransomwatch.md) | I need a baseline. What did the leak-site ecosystem look like before mid-2025, and where is a free, citable, timestamped record... | 3 | active |
| [Tor.taxi](onion-discovery/tor-taxi.md) | I have a site name, or only a category - onion search engines, forums, email hosts, information sites. Which addresses does this... | 3 | passive |
<!-- END:TOOLS -->

## Related

- [../00-methodology/opsec/README.md](../00-methodology/opsec/README.md) - isolate the work before you start
- [../09-code-paste-forums/paste-sites/README.md](../09-code-paste-forums/paste-sites/README.md) - where onion addresses and dumps surface on the clearweb
- [../13-threat-intel/](../13-threat-intel/) - the malware and infrastructure side of the same cases
