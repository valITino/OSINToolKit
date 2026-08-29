# URL analysis

I have a URL I must not click. What does it serve, where does it redirect, and
what does it look like - answered by making somebody else's browser fetch it.

## The order

1. **Search first.** Every service here is searchable by URL, domain, or hash.
   If the URL was already scanned, you get the answer for free and the operator
   learns nothing.
2. **Then submit, deliberately.** A scan fetches the target from the service's
   infrastructure, which is good for your OPSEC and bad for your secrecy: on
   free tiers the result is usually public, and the operator may be watching the
   public feed for their own domains. Phishing kits also fingerprint sandbox
   ranges and serve them a benign page, so a clean scan of a live kit is a
   common false negative.
3. **Never open it yourself**, and never in a browser that has your sessions.

## What a scan tells you that a screenshot does not

- The full redirect chain, including the traffic-distribution hops that decide
  whether you get the payload or a decoy.
- Every request the page makes: analytics IDs, kit assets, and third-party
  infrastructure you can pivot on.
- The hosting and certificate the page landed on, which usually links it to
  the rest of the campaign.
- Whether the same kit has been seen elsewhere - most phishing pages are
  redeployments, and the reuse is the attribution.

## Traps

- **Targeted links are single-use.** Many phishing URLs carry a token that
  identifies the recipient and dies after one fetch; a sandbox that follows it
  burns the evidence and also tells the operator the mail was received.
- **Geofencing and user-agent gating.** A kit that only serves the payload to a
  residential IP in one country will look harmless from a datacentre scanner.
- **Redirects age out.** Re-scan before you conclude a URL is dead; the same URL
  may be benign at 09:00 and malicious at 17:00.

## Tools here

<!-- BEGIN:TOOLS -->
_No tool files here yet._
<!-- END:TOOLS -->

## Related

- [../../04-web-exploration/fingerprinting/urlscan-io.md](../../04-web-exploration/fingerprinting/urlscan-io.md) - the same idea, with a searchable public corpus
- [../../10-email-investigation/header-analysis/](../../10-email-investigation/header-analysis/) - where the URL arrived from
- [../feeds-and-trackers/](../feeds-and-trackers/) - check the URL against what is already published
