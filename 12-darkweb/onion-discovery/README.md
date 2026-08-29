# Onion discovery

The hard part of dark web work is rarely the crawling. It is learning that an
address exists at all. There is no DNS to enumerate and no crawler that has seen
everything, so discovery means asking several partial indexes and mining the
clearweb for the addresses people leak there.

Everything in this directory is passive: the indexes and aggregators did the
connecting, and you are reading their copy.

## Where onion addresses actually come from

Work these in order. The first four cost nothing and touch nothing.

1. **The clearweb mentions them.** Operators, victims, researchers, and
   customers all publish onion addresses on the clearweb. Grep for the address
   pattern rather than searching for the site's name:

   ```bash
   # v3 addresses are 56 base32 characters plus .onion
   grep -Eoh '[a-z2-7]{56}\.onion' *.html | sort -u
   ```

   Feed that regex over pages you already hold, then go looking for more:
   pastes ([../../09-code-paste-forums/paste-sites/](../../09-code-paste-forums/paste-sites/)),
   code and config files ([../../09-code-paste-forums/code-search/](../../09-code-paste-forums/code-search/)),
   archived pages ([../../06-history-and-archives/web-archive/](../../06-history-and-archives/web-archive/)),
   and the bulk indexes in
   [search-operators.md](../../99-resources/cheatsheets/search-operators.md).
2. **Certificate transparency.** Onion services can hold certificates, and the
   names land in the CT logs like any other. Search the logs for `.onion` under
   a target's organisation via [../../05-certificates-tls/ct-log-search/](../../05-certificates-tls/ct-log-search/).
3. **Onion-Location headers and links.** Clearweb sites advertise their own
   hidden service in an `Onion-Location` HTTP header or an alternate-service
   link. One request to the clearweb site - which you were making anyway -
   answers it:

   ```bash
   curl -sI https://example.com | grep -i '^onion-location'
   ```
4. **Search engines and directories built for it.** Ahmia and its peers crawl
   hidden services and expose the results on the clearweb; the link directories
   publish signed lists of addresses precisely because clones are endemic.
5. **Leak and paste aggregators.** Intelligence X and the leak-site trackers in
   [../leak-monitoring/](../leak-monitoring/) index onion content and often hold
   a copy of a page that is already gone.

## Reading what you find

- **An address is not an identity.** Anyone can stand up a mirror, and phishing
  clones of well-known services are the norm rather than the exception. Prefer
  addresses signed by the operator, and record where you got each one.
- **Indexes are partial and opinionated.** Ahmia filters abuse material by
  policy; others index only what their crawler happened to reach. Three empty
  results are not evidence of absence.
- **Old lists rot fast.** Most addresses in any published list are dead. Check
  liveness yourself before drawing conclusions from a directory entry, and see
  [../active-crawling/](../active-crawling/) for how to do that without more
  contact than you intended.

## Tools here

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [Ahmia](ahmia.md) | I have a keyword - a victim name, a brand, a handle. Which indexed Tor hidden services mention it, when was each last seen alive... | 2 | passive |
| [dark.fail](dark-fail.md) | I have the name of a well-known hidden service and an address someone handed me for it. Is that the real, PGP-signed .onion for... | 2 | passive |
| [Intelligence X](intelligence-x.md) | I have a selector - an email address, a domain, a .onion host, an IP or a Bitcoin address. Where has it appeared in archived... | 2 | passive |
| [OnionSearch](onionsearch.md) | I have a keyword and a list of onion search engines. Which of them return a hit for it, collected into one CSV - and, read... | 3 | active |
| [Tor.taxi](tor-taxi.md) | I have a site name, or only a category - onion search engines, forums, email hosts, information sites. Which addresses does this... | 3 | passive |
<!-- END:TOOLS -->

## Related

- [../access-and-opsec/](../access-and-opsec/) - set this up before you open anything you find
- [../../04-web-exploration/dorking/README.md](../../04-web-exploration/dorking/README.md) - the clearweb half of the search
- [../../99-resources/cheatsheets/search-operators.md](../../99-resources/cheatsheets/search-operators.md) - engine syntax for the harvesting queries
