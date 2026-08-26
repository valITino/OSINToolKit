# 04 - Web Exploration

You have a URL or web host. What is it built with, what CMS, what hidden content and paths, what does it look like, and who registered it. Fingerprint before you fuzz; content discovery is intrusive.

## Subcategories

- [fingerprinting/](fingerprinting/) - BuiltWith, urlscan.io, WhatWeb, wig - the tech stack
- [cms-scanners/](cms-scanners/) - CMSeeK, CMSmap, WPScan - identify and probe the CMS
- [content-discovery/](content-discovery/) - feroxbuster, ffuf, gobuster - find hidden paths (intrusive)
- [crawling-spidering/](crawling-spidering/) - katana, Photon - map what is linked
- [dorking/](dorking/) - Search operators, GHDB - targeted retrieval from search engines
- [monitoring-visual/](monitoring-visual/) - VisualPing, gowitness - screenshots and change tracking
- [whois-domains/](whois-domains/) - viewdns.info - domain ownership and history

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [BuiltWith](fingerprinting/builtwith.md) | I have a domain. What is this site built with, what analytics and advertising IDs does it carry, and what has its hosting looked... | 2 | passive |
| [CMSeeK](cms-scanners/cmseek.md) | I have a URL. Which CMS is behind it, which version, and what can I learn about its users and themes without hammering the site? | 2 | active |
| [CMSmap](cms-scanners/cmsmap.md) | I have a site running WordPress, Joomla, Drupal, or Moodle. What version, plugins, and themes is it running, and are any of them... | 2 | intrusive |
| [dirhunt](content-discovery/dirhunt.md) | What directory structure does this site have, worked out **without** brute forcing thousands of paths at it? | 2 | active |
| [feroxbuster](content-discovery/feroxbuster.md) | I am authorised to test this site. What directories and files exist that nothing links to - and what is inside the directories I... | 2 | intrusive |
| [ffuf](content-discovery/ffuf.md) | I am authorised to test this site. What happens if I substitute a wordlist into *this specific position* - a path, a parameter... | 2 | intrusive |
| [gobuster](content-discovery/gobuster.md) | I am authorised to test this target. What directories, DNS subdomains, or virtual hosts exist, brute-forced from a wordlist? | 2 | intrusive |
| [gowitness](monitoring-visual/gowitness.md) | I have hundreds of hosts or URLs. What does each one actually look like, so I can spot the interesting ones without opening... | 2 | active |
| [hakrawler](crawling-spidering/hakrawler.md) | I have a URL (or a thousand). What links, subdomains, and JavaScript files does it reference, right now, in one pipe? | 2 | active |
| [katana](crawling-spidering/katana.md) | What URLs and endpoints does this site actually expose - including the ones that only appear when JavaScript runs? | 2 | active |
| [Photon](crawling-spidering/photon.md) | While crawling this site, what OSINT falls out of it - emails, social handles, API keys, document links, subdomains? | 2 | active |
| [urlscan.io](fingerprinting/urlscan-io.md) | What does this URL actually do when a browser loads it - what does it look like, what does it request, where does it redirect... | 2 | passive |
| [viewdns.info](whois-domains/viewdns.md) | I have a domain or IP and no tools installed. Who owns it, what else is on that address, what did it resolve to before, and does... | 2 | passive |
| [VisualPing](monitoring-visual/visualping.md) | This page matters to my investigation. Tell me when it changes - without me checking it every day, and without my IP appearing in... | 2 | passive |
| [VisualSiteMapper](monitoring-visual/visualsitemapper.md) | How is this site structured - which pages are central, which are barely linked, and where does the link graph cluster? | 2 | passive |
| [WhatWeb](fingerprinting/whatweb.md) | I have a URL (or a list of them). What is running on it right now - server, CMS, framework, JavaScript libraries, and versions? | 2 | active |
| [WPScan](cms-scanners/wpscan.md) | This site is WordPress. Exactly which version, plugins, themes, and users does it expose, and which of those have known... | 2 | intrusive |
| [DirBuster](content-discovery/dirbuster.md) | What directories and files exist on this web server that nothing links to? | 3 | intrusive |
| [inurlbr](dorking/inurlbr.md) | Can I run a dork across many search engines at once and automatically process the results? | 3 | passive |
| [wfuzz](content-discovery/wfuzz.md) | What happens when I substitute a wordlist into any part of an HTTP request - path, parameter, header, or cookie? | 3 | intrusive |
| [wig](fingerprinting/wig.md) | What CMS and web platform is this site running, guessed from static file checksums and page markers? | 3 | active |
<!-- END:TOOLS -->
