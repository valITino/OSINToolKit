# 13 - Threat intel and malware

You are holding a file, a hash, or a URL you must not click, and the question is
the same one every time: has anybody seen this before, and what did they
conclude? This category is the community's memory - sample repositories,
sandboxes, and standing feeds of known-bad infrastructure.

It is deliberately narrow. This repo documents discovery and attribution, so
what belongs here is *looking up* and *correlating* what others already
analysed. Reverse engineering, unpacking, and detection engineering are real
disciplines and out of scope; the files here stop at the point where you would
need a debugger.

## Subcategories

- [file-and-hash/](file-and-hash/) - Jotti, MalwareBazaar, Hybrid Analysis, MalShare - what is known about this file
- [url-analysis/](url-analysis/) - urlQuery, Triage, ANY.RUN - what a URL serves, fetched by somebody else's browser
- [feeds-and-trackers/](feeds-and-trackers/) - URLhaus, ThreatFox, AlienVault OTX - infrastructure already published as bad

## Search before you submit

The single rule that matters in this category. Searching an existing corpus by
hash or by URL is passive and invisible. **Submitting is not**: the file or URL
usually becomes visible to other users, sometimes publicly and immediately, and
plenty of operators watch the public feeds of the big sandboxes for exactly
their own artifacts. A submission can tell your subject that they are being
investigated, and can leak the internal document you submitted along with it.

So: hash the file locally, search the hash, and only submit when you have
decided the operator learning about it is an acceptable cost.

```bash
sha256sum suspicious.doc      # search this, do not upload the file
```

## Reading a verdict honestly

- **Detection names are marketing, not taxonomy.** Two engines will call one
  file three different families. Use the names as search terms for pivoting,
  never as a conclusion.
- **A clean result means nothing** for a targeted or recent sample. Absence of
  detection is absence of evidence.
- **Feeds age badly.** An IP flagged as a C2 last year may be a blameless
  virtual host today; addresses get reassigned and shared hosting is shared.
  Always check the *date* on the entry before repeating it.
- **The pivot is worth more than the verdict.** The value of a sample entry is
  the infrastructure it names - domains, IPs, certificates, URL patterns - which
  you take back to [../02-network-and-ip/](../02-network-and-ip/) and
  [../05-certificates-tls/](../05-certificates-tls/).

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [ANY.RUN](url-analysis/any-run.md) | I have a URL that only misbehaves for a human. What does it do when somebody clicks through the CAPTCHA or the fake verification... | 2 | active |
| [Hybrid Analysis (Falcon Sandbox)](file-and-hash/hybrid-analysis.md) | I have a file or a hash. Has anyone already detonated it, and what did it do - which processes, which domains, which C2 - so that... | 2 | passive |
| [MalShare](file-and-hash/malshare.md) | I have a hash. Was this file collected in the wild - from which URL, under which filenames - and can I get a copy without asking... | 2 | passive |
| [MalwareBazaar](file-and-hash/malwarebazaar.md) | I have a hash. What family is it, who has already analysed it, and what other samples share its builder, its signing certificate... | 2 | passive |
| [Recorded Future Triage (tria.ge)](url-analysis/triage.md) | I have a URL or a file hash. Has anyone already detonated it, what family did it turn out to be, and what C2 configuration came... | 2 | active |
| [ThreatFox](feeds-and-trackers/threatfox.md) | I have an IP, domain or URL that looks like callback infrastructure. Is it a published C2 or payload-delivery indicator, for... | 2 | passive |
| [URLhaus](feeds-and-trackers/urlhaus.md) | I have a URL or a hostname out of a log. Has anyone already published it as a malware distribution site, which family did it... | 2 | passive |
| [urlquery](url-analysis/urlquery.md) | I have a URL I must not click. What does it serve when a real browser opens it, do any IDS rules or DNS blocklists already call... | 2 | active |
| [AlienVault OTX (LevelBlue Open Threat Exchange)](feeds-and-trackers/alienvault-otx.md) | I have an indicator another feed already flagged. Who wrote it up, in what report, and what else did they list in the same pulse? | 3 | passive |
| [Jotti's malware scan](file-and-hash/jotti.md) | I have a file, or only its hash. Have these thirteen engines ever seen this exact file - and if I must scan, can I do it... | 3 | active |
| [PhishTank](feeds-and-trackers/phishtank.md) | I have a URL that looks like a credential-harvesting page. Is it already in the community phishing corpus as verified and still... | 3 | passive |
<!-- END:TOOLS -->

## Related

- [../02-network-and-ip/reputation/](../02-network-and-ip/reputation/) - the IP and domain reputation view
- [../10-email-investigation/](../10-email-investigation/) - where most samples arrive from
- [../12-darkweb/leak-monitoring/](../12-darkweb/leak-monitoring/) - what the same crews publish
