# 04 - Web Exploration

You have a URL or web host. What is it built with, what CMS, what hidden content and paths, what does it look like, and who registered it. Fingerprint before you fuzz; content discovery is intrusive.

## Subcategories

- [fingerprinting/](fingerprinting/) - BuiltWith, urlscan.io, WhatWeb, wig - the tech stack
- [cms-scanners/](cms-scanners/) - CMSeeK, CMSmap, WPScan - identify and probe the CMS
- [content-discovery/](content-discovery/) - feroxbuster, ffuf, gobuster - find hidden paths (intrusive)
- [crawling-spidering/](crawling-spidering/) - katana, Photon - map what is linked
- [scraping/](scraping/) - HTTrack, Scrapy, trafilatura - take the content away and keep it
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
| [DomainTools](whois-domains/domaintools.md) | I have a registrant detail - an email, a name, a company, a phone number. What else did that person register, including the... | 2 | passive |
| [DorkSearch](dorking/dorksearch.md) | I have a target and a rough idea of what I want to find, but not the operator syntax. Can something build the dork for me, and... | 2 | passive |
| [feroxbuster](content-discovery/feroxbuster.md) | I am authorised to test this site. What directories and files exist that nothing links to - and what is inside the directories I... | 2 | intrusive |
| [ffuf](content-discovery/ffuf.md) | I am authorised to test this site. What happens if I substitute a wordlist into *this specific position* - a path, a parameter... | 2 | intrusive |
| [gobuster](content-discovery/gobuster.md) | I am authorised to test this target. What directories, DNS subdomains, or virtual hosts exist, brute-forced from a wordlist? | 2 | intrusive |
| [GooFuzz](dorking/goofuzz.md) | I have a domain. Which files, paths, extensions and subdomains has Google already indexed for it - found without sending a single... | 2 | passive |
| [Google Hacking Database](dorking/ghdb.md) | What should I actually search for? Someone has already worked out the query that surfaces exposed backups, login panels, or... | 2 | passive |
| [gowitness](monitoring-visual/gowitness.md) | I have hundreds of hosts or URLs. What does each one actually look like, so I can spot the interesting ones without opening... | 2 | active |
| [hakrawler](crawling-spidering/hakrawler.md) | I have a URL (or a thousand). What links, subdomains, and JavaScript files does it reference, right now, in one pipe? | 2 | active |
| [httpx](fingerprinting/httpx.md) | I have a list of hosts or subdomains. Which of them actually serve HTTP, on what status code and title, running what server and... | 2 | active |
| [HTTrack Website Copier](scraping/httrack.md) | I have a site that may change or vanish. Can I take a complete offline copy of it - and, on the current engine, a WARC/WACZ of... | 2 | intrusive |
| [katana](crawling-spidering/katana.md) | What URLs and endpoints does this site actually expose - including the ones that only appear when JavaScript runs? | 2 | active |
| [pagodo](dorking/pagodo.md) | I want to run hundreds of GHDB dorks against one domain instead of pasting them into a search box one at a time. Can that be... | 2 | passive |
| [Photon](crawling-spidering/photon.md) | While crawling this site, what OSINT falls out of it - emails, social handles, API keys, document links, subdomains? | 2 | active |
| [Playwright](scraping/playwright.md) | The page is empty in `curl` and full in my browser. How do I get the DOM after JavaScript runs, and capture what a visitor... | 2 | active |
| [Scrapy](scraping/scrapy.md) | I have a site holding thousands of records - listings, profiles, filings - behind paginated HTML. How do I pull them into JSON or... | 2 | active |
| [trafilatura](scraping/trafilatura.md) | I have a page of HTML and I need the article out of it: the body text without the navigation, cookie banner, share buttons and... | 2 | active |
| [urlscan.io](fingerprinting/urlscan-io.md) | What does this URL actually do when a browser loads it - what does it look like, what does it request, where does it redirect... | 2 | passive |
| [viewdns.info](whois-domains/viewdns.md) | I have a domain or IP and no tools installed. Who owns it, what else is on that address, what did it resolve to before, and does... | 2 | passive |
| [VisualPing](monitoring-visual/visualping.md) | This page matters to my investigation. Tell me when it changes - without me checking it every day, and without my IP appearing in... | 2 | passive |
| [VisualSiteMapper](monitoring-visual/visualsitemapper.md) | How is this site structured - which pages are central, which are barely linked, and where does the link graph cluster? | 2 | passive |
| [WAFW00F](fingerprinting/wafw00f.md) | I have a URL and a stack listing I do not trust. What WAF, CDN or bot-management product is answering for this site - and so, am... | 2 | intrusive |
| [WhatWeb](fingerprinting/whatweb.md) | I have a URL (or a list of them). What is running on it right now - server, CMS, framework, JavaScript libraries, and versions? | 2 | active |
| [Whoisology](whois-domains/whoisology.md) | I have one WHOIS record. Which other domains share its registrant email, name, organisation, or address - and who owned them at a... | 2 | passive |
| [WPScan](cms-scanners/wpscan.md) | This site is WordPress. Exactly which version, plugins, themes, and users does it expose, and which of those have known... | 2 | intrusive |
| [yt-dlp](scraping/yt-dlp.md) | I have a video URL that may be deleted, edited or made private. How do I preserve it and everything around it - channel ID... | 2 | active |
| [DirBuster](content-discovery/dirbuster.md) | What directories and files exist on this web server that nothing links to? | 3 | intrusive |
| [dorkscout](dorking/dorkscout.md) | I have a domain. Can I pull the whole GHDB down as flat category files and fire the lot at that domain from one command? | 3 | passive |
| [GitDorker](dorking/gitdorker.md) | I have an organisation name or a domain. Which of 500-odd secret-shaped GitHub search patterns return hits when combined with it... | 3 | passive |
| [GoSpider](crawling-spidering/gospider.md) | I have a domain. What does the site link to, and what did Wayback, Common Crawl and AlienVault OTX already know about it - with... | 3 | active |
| [inurlbr](dorking/inurlbr.md) | Can I run a dork across many search engines at once and automatically process the results? | 3 | passive |
| [snscrape](scraping/snscrape.md) | I have a handle or a channel name and no API key. Can I still pull that account's posts - and, more often now, is a dataset that... | 3 | active |
| [uDork](dorking/udork.md) | I have a domain. Can one bash script walk it through a whole set of prebuilt Google dorks - extensions, URL strings, titles... | 3 | passive |
| [Visual Site Mapper (sitemapper-nodejs)](crawling-spidering/sitemapper.md) | I have an old methodology write-up or link list naming "Visual Site Mapper" as the way to see a site's link graph. Is that... | 3 | active |
| [wfuzz](content-discovery/wfuzz.md) | What happens when I substitute a wordlist into any part of an HTTP request - path, parameter, header, or cookie? | 3 | intrusive |
| [wig](fingerprinting/wig.md) | What CMS and web platform is this site running, guessed from static file checksums and page markers? | 3 | active |
<!-- END:TOOLS -->
