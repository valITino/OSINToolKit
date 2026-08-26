# Playbook: phishing email triage

**You have:** a suspicious email, ideally as a `.eml` file.
**You want:** where it really came from, what it was trying to do, and whether
anyone fell for it.

Speed matters here, but so does not becoming a victim yourself. **Do not click
anything in the message.** Work from the source, in a VM.

---

## 0. Get the original, not a forward

Before anything else, check what you actually have.

**Forwarding a message replaces the original headers.** If someone forwarded you
the phish, you are looking at *their* mail path, not the attacker's. Ask for the
original as an **attachment** (`.eml`/`.msg`), which preserves the headers intact.

This one step is the difference between a real investigation and a wasted hour.

## 1. Read the headers bottom-up

- [Reading headers by hand](../10-email-investigation/header-analysis/README.md)
- [MXToolbox](../10-email-investigation/header-analysis/mxtoolbox.md) - parses the chain for you

**`Received:` headers read bottom-up.** The bottom entry is the earliest hop -
usually the originating system. Working top-down inverts the story completely.

What to pull out:

- The **originating IP** at the bottom of the chain.
- `Authentication-Results:` - how SPF, DKIM, and DMARC evaluated.
- Mismatches between the `From:` display name, the `From:` address, `Return-Path:`,
  and `Reply-To:`. A `Reply-To:` pointing somewhere unrelated is a classic tell.

**Headers above the first trusted hop can be forged.** A sender controls what it
writes; only hops added by servers you trust are reliable.

## 2. Investigate the originating IP

- [AbuseIPDB](../02-network-and-ip/reputation/abuseipdb.md) - has anyone reported it
- [VirusTotal](../02-network-and-ip/reputation/virustotal.md) - reputation plus passive DNS
- [ipinfo.io](../02-network-and-ip/registries-asn/ipinfo-io.md) - who owns it
- [ExoneraTor](../02-network-and-ip/reputation/exonerator.md) - was it a Tor relay at that time

```bash
curl -s https://ipinfo.io/<IP>/json
```

Check ExoneraTor with the **exact date and timezone** from the header. If it was a
Tor exit, attribution to a person from that IP is effectively dead.

Note whether the IP belongs to a hosting provider, a compromised residential
machine, or a legitimate mail service being abused - each implies a different
kind of actor.

## 3. Check the sending domain's mail policy

- [host](../03-dns-and-subdomains/query-tools/host.md)
- [server checks](../10-email-investigation/server-checks/README.md)

```bash
host -t TXT sender-domain.com            # SPF
host -t TXT _dmarc.sender-domain.com     # DMARC policy
```

Two different findings here:

- **The sender's domain was spoofed** - it publishes `-all` and `p=reject`, and the
  mail failed authentication. The domain owner is a victim too.
- **The domain is the attacker's own** - freshly registered, weak or absent policy.
  Feed it into the [domain investigation playbook](domain-investigation.md).

## 4. Analyse the links without visiting them

- [urlscan.io](../04-web-exploration/fingerprinting/urlscan-io.md)

Search **existing** scans first - it is passive, and someone has usually scanned
that phishing domain already:

```text
https://urlscan.io/search/?q=page.domain:suspicious-domain.com
```

If you must submit a new scan, set it **Unlisted or Private** - a public scan is
visible to the attacker, who may be watching for exactly that.

Expand shortened links in a sandbox, never in your browser. Note that phishing
kits often **cloak**: they serve a benign page to datacentre IPs and the real one
to targets, so a clean scan is not proof of a clean site.

## 5. Is the domain impersonating a brand?

- [dnstwist](../03-dns-and-subdomains/typosquatting/dnstwist.md)

```bash
dnstwist -r -w yourbrand.com     # registered lookalikes of the impersonated brand
```

This finds the rest of the campaign. Attackers register lookalikes in batches, so
one phishing domain usually has siblings - and the ones with MX records can
receive replies.

## 6. Attachments: analyse statically, in a VM

- [ExifTool](../07-documents-metadata/metadata-extraction/exiftool.md) - metadata first
- [oletools](../07-documents-metadata/office-forensics/oletools.md) - Office macros
- [pdf-parser.py](../07-documents-metadata/pdf-forensics/pdf-parser.md) - PDF objects

```bash
exiftool -a -u -g1 attachment.docx
oleid attachment.doc && olevba attachment.doc
```

**Never open the attachment in its native application** - that is the entire point
of these tools. Metadata (author, company, creation software) sometimes links the
document to other campaigns.

Deep malware analysis is out of scope for this repo; record what is present and
hand it to a malware team.

## 7. Certificate and infrastructure pivots

- [crt.sh](../05-certificates-tls/ct-log-search/crt-sh.md)

A phishing domain's certificate history dates the campaign - the certificate is
usually issued days before the mail goes out. Certificates and hosting often link
the domain to the attacker's other infrastructure.

## 8. Scope the incident

Turn the investigation into an answer for whoever asked:

- Search your mail logs for the sender domain, originating IP, and subject line -
  who else received it?
- Search web/proxy logs for the phishing URL - who clicked?
- Check exposure of any address that responded:
  [Have I Been Pwned](../08-people-and-identity/email-osint/hibp.md).

---

## Record everything

Phishing infrastructure disappears within days. **Archive as you go** - screenshots
with the URL and timestamp visible, saved raw headers, saved scan results. If it
matters later, the live site will be gone.

See [../00-methodology/documentation/README.md](../00-methodology/documentation/README.md)
and [../LEGAL.md](../LEGAL.md).
