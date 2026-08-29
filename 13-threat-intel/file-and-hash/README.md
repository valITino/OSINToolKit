# File and hash

I have a file, or only its hash. Has anyone seen it, what did they call it, and
what infrastructure does it reach out to?

## Hash first, always

Compute the hash locally and search that. It is free, instant, passive, and it
cannot leak the document:

```bash
sha256sum sample.bin          # the search key everything here accepts
md5sum sample.bin             # older corpora and feeds still index by MD5
```

Fuzzy hashes (ssdeep, imphash, TLSH) answer a different question - "what else
is nearly this file" - and the repositories that support them are where you find
a family rather than a sample.

## When to upload, and what it costs

Uploading gets you an analysis of an unknown sample. It also:

- makes the file available to the service's customers, and on free tiers often
  to the public,
- tells anybody watching that the sample is in someone's hands,
- can expose whatever the file contains - a real invoice, a real address book,
  the internal document the attacker attached.

For a suspected targeted attack, treat submission as a disclosure decision, not
a lookup. Where you need an analysis without publishing, that is what a paid
private submission or a local sandbox is for.

## Reading the result

- Multi-engine verdicts count detections, and the count is not a confidence
  score. One good engine beats thirty weak ones, and a 3/70 on a recent sample
  is normal.
- Sample repositories are the better source for *pivoting*: tags, the campaign
  a submitter attributed it to, related samples, and the URLs it was served
  from.
- Check the first-seen date. A file first seen this morning behaves differently
  in these datasets than one from a five-year-old commodity family.

## Tools here

<!-- BEGIN:TOOLS -->
_No tool files here yet._
<!-- END:TOOLS -->

## Related

- [../../07-documents-metadata/office-forensics/](../../07-documents-metadata/office-forensics/) - what the document itself says, offline
- [../../07-documents-metadata/pdf-forensics/](../../07-documents-metadata/pdf-forensics/) - the same for PDFs
- [../../02-network-and-ip/reputation/virustotal.md](../../02-network-and-ip/reputation/virustotal.md) - the multi-engine corpus most people reach for first
