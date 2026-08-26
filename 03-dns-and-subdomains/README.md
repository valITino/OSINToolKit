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
| [fierce](active-enum/fierce.md) | I have a domain and I am authorised to probe it. Which hostnames actually resolve, and what non-contiguous IP space does this... | 2 | intrusive |
| [HackerTarget reverse DNS API](reverse-dns/hackertarget-reversedns.md) | I have an IP. What hostnames point at it - including domains that have nothing to do with the one I started from? | 2 | passive |
| [host](query-tools/host.md) | I want one DNS answer, right now, without reading a full response packet. | 2 | active |
| [subfinder](passive-enum/subfinder.md) | I have a domain. What subdomains exist, gathered from every passive source at once, without sending a single packet to the target? | 2 | passive |
| [Sublist3r](passive-enum/sublist3r.md) | What subdomains exist for this domain, according to search engines and a handful of public sources? | 3 | passive |
<!-- END:TOOLS -->
