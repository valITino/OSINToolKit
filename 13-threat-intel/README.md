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
_No tool files here yet._
<!-- END:TOOLS -->

## Related

- [../02-network-and-ip/reputation/](../02-network-and-ip/reputation/) - the IP and domain reputation view
- [../10-email-investigation/](../10-email-investigation/) - where most samples arrive from
- [../12-darkweb/leak-monitoring/](../12-darkweb/leak-monitoring/) - what the same crews publish
