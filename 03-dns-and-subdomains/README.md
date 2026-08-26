# 03 - DNS and Subdomains

You have a domain. Resolve its records, enumerate its subdomains (passively first), turn IPs back into names, and generate the lookalikes an attacker would.

## Subcategories

- [query-tools/](query-tools/) - dig, host - resolve any record
- [passive-enum/](passive-enum/) - subfinder, DNSDumpster - subdomains without touching the target
- [active-enum/](active-enum/) - fierce - resolution and brute forcing (authorised)
- [reverse-dns/](reverse-dns/) - HackerTarget API - IP back to hostnames
- [typosquatting/](typosquatting/) - dnstwist - lookalike and homoglyph domains

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [dnstwist](typosquatting/dnstwist.md) | I have a brand or domain. What lookalike domains - typos, homoglyphs, swapped TLDs - exist or are registered, and which of them... | 1 | passive |
| [dig](query-tools/dig.md) | I have a domain. What does DNS actually say about it - any record type, from any resolver I choose? | 2 | active |
| [DNSDumpster](passive-enum/dnsdumpster.md) | I have a domain and want a quick, visual picture of its DNS footprint - subdomains, mail servers, and the hosts they map to... | 2 | passive |
| [dnsmap](active-enum/dnsmap.md) | I have a domain and I am authorised to probe it. Which subdomains exist, from one command, without me choosing a wordlist or... | 2 | intrusive |
| [dnsx](query-tools/dnsx.md) | I have a list of hostnames or a netblock, not a single name. What does DNS say about all of them, in a form I can pipe into the... | 2 | active |
| [fierce](active-enum/fierce.md) | I have a domain and I am authorised to probe it. Which hostnames actually resolve, and what non-contiguous IP space does this... | 2 | intrusive |
| [HackerTarget reverse DNS API](reverse-dns/hackertarget-reversedns.md) | I have an IP. What hostnames point at it - including domains that have nothing to do with the one I started from? | 2 | passive |
| [hakrevdns](reverse-dns/hakrevdns.md) | I have a netblock rather than a single address. What hostname does every IP in it resolve back to, and which of those names... | 2 | active |
| [host](query-tools/host.md) | I want one DNS answer, right now, without reading a full response packet. | 2 | active |
| [massdns](active-enum/massdns.md) | I have a list of millions of candidate names, or a whole netblock. Which of them actually resolve, and can I find out in minutes... | 2 | intrusive |
| [Namedroppers](typosquatting/namedroppers.md) | Which **registered** domains contain my brand name anywhere in them - not the typos, but the compositions: brand-support... | 2 | passive |
| [puredns](active-enum/puredns.md) | I brute forced a domain and got thousands of hits. Which of them are real, and which are just a wildcard record answering... | 2 | intrusive |
| [Robtex](reverse-dns/robtex.md) | I have an IP, a nameserver, or a mail server. What hostnames point at it now, what pointed at it before, and when did that change? | 2 | passive |
| [subfinder](passive-enum/subfinder.md) | I have a domain. What subdomains exist, gathered from every passive source at once, without sending a single packet to the target? | 2 | passive |
| [nslookup](query-tools/nslookup.md) | I am on a machine that has nothing installed - very often a Windows one. What does DNS say about this name, right now? | 3 | active |
| [Sublist3r](passive-enum/sublist3r.md) | What subdomains exist for this domain, according to search engines and a handful of public sources? | 3 | passive |
<!-- END:TOOLS -->
