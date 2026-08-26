# 01 - Orchestrators

Start here. Multi-purpose tools that cover a lot of ground from a single seed (a domain, IP, email, or name) and correlate what they find. Run one of these first, then drill into the specialist categories for the leads it surfaces.

## Subcategories

- [recursive-scanners/](recursive-scanners/) - SpiderFoot, BBOT - one seed, recursive correlation
- [modular-frameworks/](modular-frameworks/) - recon-ng, Maltego - structured, database- or graph-backed
- [aggregators/](aggregators/) - theHarvester, Amass - broad sweeps of public sources

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [BBOT](recursive-scanners/bbot.md) | I have a domain (or IP, email, or org). What is the full attack surface, found recursively, in one command I can drop into a... | 1 | active |
| [Maltego](modular-frameworks/maltego.md) | I have a set of entities (people, domains, IPs, accounts) and a tangle of relationships. How do they connect, and how do I show... | 1 | passive |
| [OWASP Amass](aggregators/amass.md) | I have a domain or an organisation. What is its full DNS and network footprint - subdomains, resolved IPs, ASNs, and netblocks... | 1 | active |
| [recon-ng](modular-frameworks/recon-ng.md) | I am running a real case over days or weeks. Where do I keep every host, contact, and credential I find so that each new module... | 1 | passive |
| [SpiderFoot](recursive-scanners/spiderfoot.md) | I have a domain, IP, email, or name. What is everything the public internet already knows about it, and how do those facts... | 1 | active |
| [theHarvester](aggregators/theharvester.md) | I have a company or domain. What emails, subdomains, hostnames, and employee names are already exposed across search engines and... | 1 | passive |
| [Sn1per](aggregators/sn1per.md) | What does a fully automated recon-and-attack-surface sweep of this target produce, by chaining dozens of other tools together? | 3 | intrusive |
<!-- END:TOOLS -->
