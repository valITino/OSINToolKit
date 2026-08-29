# Feeds and trackers

Standing lists of infrastructure somebody has already published as malicious:
distribution URLs, command-and-control servers, phishing pages. These answer
"is this already known?" in one query, and they are the cheapest enrichment
step in any triage.

## Why these belong in an OSINT reference

They are not just blocklists. Each entry carries provenance - who reported it,
when, which malware family, which campaign - and that provenance is a pivot.
One IP from a phishing header becomes a family name, which becomes a set of
sibling domains, which becomes the scope of the incident.

## How to use them without embarrassing yourself

- **The date is the most important field.** Hosting is recycled constantly. An
  IP listed eighteen months ago tells you about a previous tenant, and repeating
  it as current is how a report gets discredited.
- **Shared infrastructure creates guilt by association.** A CDN edge, a large
  shared host, or a URL shortener will appear on every feed there is. Check what
  else lives at the same address before you attribute anything.
- **Confidence levels vary wildly.** Community-submitted entries range from
  carefully triaged to a single analyst's hunch. Read the submitter and the
  supporting evidence, not just the fact of the listing.
- **Bulk downloads beat repeated lookups.** Most of these publish full exports
  and APIs; pull once and check locally rather than hammering the service for
  every indicator.
- **Absence means nothing.** These feeds cover what somebody happened to report.
  Novel or targeted infrastructure is, by definition, not on them yet.

## Tools here

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [ThreatFox](threatfox.md) | I have an IP, domain or URL that looks like callback infrastructure. Is it a published C2 or payload-delivery indicator, for... | 2 | passive |
| [URLhaus](urlhaus.md) | I have a URL or a hostname out of a log. Has anyone already published it as a malware distribution site, which family did it... | 2 | passive |
| [AlienVault OTX (LevelBlue Open Threat Exchange)](alienvault-otx.md) | I have an indicator another feed already flagged. Who wrote it up, in what report, and what else did they list in the same pulse? | 3 | passive |
| [PhishTank](phishtank.md) | I have a URL that looks like a credential-harvesting page. Is it already in the community phishing corpus as verified and still... | 3 | passive |
<!-- END:TOOLS -->

## Related

- [../../02-network-and-ip/reputation/abuseipdb.md](../../02-network-and-ip/reputation/abuseipdb.md) - the same question for an IP, with abuse reports
- [../file-and-hash/](../file-and-hash/) - the sample the infrastructure delivered
- [../../03-dns-and-subdomains/passive-dns/](../../03-dns-and-subdomains/passive-dns/) - what else that host has served over time
