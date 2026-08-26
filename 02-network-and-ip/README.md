# 02 - Network and IP

You have an IP or a netblock. Who owns it, where is it, is it known-bad, what is listening on it, and what is exposed. Prefer the passive reputation and device-search tools before you scan anything.

## Subcategories

- [registries-asn/](registries-asn/) - whois, RIRs, bgp.he.net, ipinfo.io - ownership and ASN
- [geolocation/](geolocation/) - Approximate physical location from an IP
- [reputation/](reputation/) - AbuseIPDB, VirusTotal, IPVoid, ExoneraTor - is it known-bad
- [port-scanning/](port-scanning/) - nmap - what is listening (intrusive)
- [device-search/](device-search/) - Shodan, Censys, WiGLE - exposure from existing scan data
- [vuln-scanners/](vuln-scanners/) - nuclei, Greenbone/OpenVAS - templated checks (intrusive)

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [nmap](port-scanning/nmap.md) | I have a host or an IP range. What ports are open, what services and versions are | 1 | intrusive |
| [AbuseIPDB](reputation/abuseipdb.md) | I have an IP. Has anyone else reported it for attacking them, and for what kind of | 2 | passive |
| [bgp.he.net](registries-asn/bgp-he-net.md) | I have an ASN, IP, or organisation. What prefixes does it actually announce to the | 2 | passive |
| [Censys](device-search/censys.md) | Which hosts on the internet present this certificate, this SAN, or this service | 2 | passive |
| [ExoneraTor](reputation/exonerator.md) | I have an IP and a date from a log. Was that IP a Tor relay at that moment - meaning | 2 | passive |
| [Greenbone / OpenVAS](vuln-scanners/greenbone-openvas.md) | I am authorised to assess this network. What known vulnerabilities does a full, | 2 | intrusive |
| [ipinfo.io](registries-asn/ipinfo-io.md) | I have an IP. In one call: who owns it, what ASN it belongs to, roughly where it | 2 | passive |
| [iplocation.net](geolocation/iplocation-net.md) | I have an IP. Roughly where is it, and do the major geolocation providers agree | 2 | passive |
| [IPVoid](reputation/ipvoid.md) | I have an IP. Is it listed on any of the well-known blacklists, and what do basic | 2 | passive |
| [nuclei](vuln-scanners/nuclei.md) | I have a list of hosts or URLs I am authorised to test. Which known | 2 | intrusive |
| [RIR databases (ARIN / RIPE / APNIC)](registries-asn/rir-databases.md) | I have an organisation name. Which IP ranges and ASNs are allocated to it - and, | 2 | passive |
| [Shodan](device-search/shodan.md) | What is exposed on this host, netblock, or organisation - without me scanning it - | 2 | passive |
| [VirusTotal](reputation/virustotal.md) | I have a file hash, URL, domain, or IP. Do security vendors consider it malicious, | 2 | passive |
| [whois](registries-asn/whois.md) | I have a domain, an IP, or an ASN. Who registered it, when, through whom, and what | 2 | passive |
| [WiGLE](device-search/wigle.md) | I have a wireless network name (SSID) or a MAC address (BSSID). Where in the world | 2 | passive |
<!-- END:TOOLS -->
