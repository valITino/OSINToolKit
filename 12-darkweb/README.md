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
_No tool files here yet._
<!-- END:TOOLS -->

## Related

- [../00-methodology/opsec/README.md](../00-methodology/opsec/README.md) - isolate the work before you start
- [../09-code-paste-forums/paste-sites/README.md](../09-code-paste-forums/paste-sites/README.md) - where onion addresses and dumps surface on the clearweb
- [../13-threat-intel/](../13-threat-intel/) - the malware and infrastructure side of the same cases
