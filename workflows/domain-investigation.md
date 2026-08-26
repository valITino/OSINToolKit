# Playbook: domain investigation

**You have:** a domain name.
**You want:** its infrastructure, its history, its owner, and everything it
connects to.

Work top to bottom. Each step says *why* it comes where it does. Stay passive
until the passive sources are exhausted - once you go active you are in the
target's logs, and you cannot undo that.

---

## 1. Registration: who claims it, and since when

Start here because it is instant, free, and frames everything else.

```bash
whois example.com
```

- [whois](../02-network-and-ip/registries-asn/whois.md)

Read the **creation date** first. A domain registered three weeks ago that
presents as an established company is the finding. Registrar and nameservers
tell you which ecosystem it lives in.

Expect redaction: **GDPR removes registrant details for many EU domains**, so
blank contact fields are normal, not suspicious. If the current record is
private, the old one may not have been - go to
[historical WHOIS](../06-history-and-archives/ip-whois-history/README.md).

## 2. Certificate transparency: subdomains for free

Before touching the target's DNS, take the names it has already published to
the CT logs.

- [crt.sh](../05-certificates-tls/ct-log-search/crt-sh.md)
- [MerkleMap](../05-certificates-tls/ct-log-search/merklemap.md) - run both, they return different sets

```bash
curl -s 'https://crt.sh/?q=%25.example.com&output=json' | jq -r '.[].name_value' | tr ',' '\n' | sed 's/\*\.//' | sort -u
```

This is often the single richest subdomain source and it never touches the
target. Watch for `dev-`, `staging-`, `vpn-`, `mail-` prefixes: names the
operator did not intend to advertise.

**Trap:** Cloudflare Universal SSL puts unrelated customers on shared SANs. A
shared SAN is **not** evidence of shared ownership.

## 3. Aggregate the passive sources

CT logs are one source. Sweep the rest in one command.

- [subfinder](../03-dns-and-subdomains/passive-enum/subfinder.md)
- [theHarvester](../01-orchestrators/aggregators/theharvester.md) - adds emails and employee names

```bash
subfinder -d example.com -all -o subs.txt
theHarvester -d example.com -b all
```

Still passive. You now have a candidate name list and, usually, a set of email
addresses that feed a separate people/identity track.

## 4. Resolve, and map the network

Now you find out which of those names are real. Resolution is **active** - it
queries the target's nameservers.

- [dig](../03-dns-and-subdomains/query-tools/dig.md)
- [Amass](../01-orchestrators/aggregators/amass.md) - relationships, ASNs, netblocks
- [bgp.he.net](../02-network-and-ip/registries-asn/bgp-he-net.md) - what the org actually announces

```bash
dig example.com NS +short && dig MX example.com +short
amass enum -passive -d example.com
```

Resolve the names to IPs, then ask what else lives on those IPs
([HackerTarget reverse DNS](../03-dns-and-subdomains/reverse-dns/hackertarget-reversedns.md)).
**Shared hosting means co-located domains are usually unrelated** - check whether
the IP belongs to a hosting provider before drawing any line.

## 5. What is exposed, without scanning

- [Shodan](../02-network-and-ip/device-search/shodan.md)
- [Censys](../02-network-and-ip/device-search/censys.md)

```bash
shodan search 'ssl.cert.subject.CN:"example.com"'
```

This answers "what ports and services are open" from existing scan data, at zero
contact. Do this **before** considering [nmap](../02-network-and-ip/port-scanning/nmap.md),
which is intrusive and needs written authorisation.

## 6. History: what the site used to be

- [Wayback CDX API](../06-history-and-archives/web-archive/wayback-cdx-api.md)
- [gau](../06-history-and-archives/web-archive/gau.md) - broader source coverage

```bash
gau --subs example.com | sort -u > urls.txt
grep -Ei '\.(pdf|docx|xlsx)$' urls.txt      # documents to run through ExifTool
```

Deleted pages, old endpoints, and forgotten files live here. Remember **Google
and Bing cache were discontinued in 2024** - Wayback is the fallback.

Documents found here go to
[07-documents-metadata](../07-documents-metadata/README.md): their metadata often
carries internal usernames and software versions.

## 7. The ownership pivot: tracking IDs

The strongest link between sites that share no infrastructure.

- [BuiltWith](../04-web-exploration/fingerprinting/builtwith.md) - find the IDs
- [SpyOnWeb](../06-history-and-archives/analytics-linking/spyonweb.md) - find who else uses them

```bash
curl -s https://example.com | grep -Eo 'UA-[0-9]+-[0-9]+|G-[A-Z0-9]+|(ca-)?pub-[0-9]+'
```

A shared Analytics or AdSense ID suggests a common operator. **Corroborate** -
agencies and templates reuse IDs across unrelated clients.

## 8. Look at it

- [urlscan.io](../04-web-exploration/fingerprinting/urlscan-io.md) - search existing scans first (passive)
- [gowitness](../04-web-exploration/monitoring-visual/gowitness.md) - screenshot the whole subdomain list

```bash
gowitness scan file -f subs.txt
```

A wall of screenshots surfaces forgotten admin panels and default installs
instantly. Note that gowitness loads pages **from your IP**; urlscan does not.

## 9. Lookalikes, if this is phishing or brand work

- [dnstwist](../03-dns-and-subdomains/typosquatting/dnstwist.md)

```bash
dnstwist -r -w example.com      # registered lookalikes, with WHOIS
```

Registered lookalikes with MX records are the priority - MX means it can receive
mail for a phish.

---

## Stop here unless you are authorised

Everything above is passive or normal-use active. The next steps -
[content discovery](../04-web-exploration/content-discovery/README.md),
[port scanning](../02-network-and-ip/port-scanning/nmap.md),
[vulnerability scanning](../02-network-and-ip/vuln-scanners/README.md) - are
**intrusive** and require written authorisation naming the targets and the window.
See [../LEGAL.md](../LEGAL.md).

## Record as you go

Every step above produces something you will need to cite later. Timestamp it,
save raw output, and archive pages that may change. See
[../00-methodology/documentation/README.md](../00-methodology/documentation/README.md).
