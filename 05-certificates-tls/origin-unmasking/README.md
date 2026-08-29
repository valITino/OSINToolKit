# Origin unmasking

Attempt to find the real origin IP behind a CDN. Often broken now.

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [Favicon hash pivoting](favicon-hash.md) | This site sits behind a CDN. Which other hosts on the internet serve the **same favicon** - and is one of them the unproxied... | 2 | active |
| [CloudFail](cloudfail.md) | Does this Cloudflare-fronted domain have a subdomain that was never proxied, pointing straight at the origin? | 3 | active |
| [CloudFlair](cloudflair.md) | What is the real origin IP behind this Cloudflare-protected site? | 3 | active |
<!-- END:TOOLS -->
