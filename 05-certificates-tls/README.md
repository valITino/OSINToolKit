# 05 - Certificates and TLS

Certificates leak structure. CT logs list every name an org certified; a TLS handshake reveals config; and sometimes a cert points at the real origin behind a CDN.

## Subcategories

- [ct-log-search/](ct-log-search/) - crt.sh, MerkleMap - subdomains from CT logs, passively
- [cert-analysis/](cert-analysis/) - testssl.sh, openssl - inspect a live TLS endpoint
- [origin-unmasking/](origin-unmasking/) - CloudFlair - find the origin behind Cloudflare (often broken)

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [crt.sh](ct-log-search/crt-sh.md) | I have a domain. What subdomains and hostnames has it ever requested certificates for - including ones that no longer resolve... | 1 | passive |
| [CertWatch](ct-log-search/certwatch.md) | I have an organisation's name rather than one domain. Which certificates has it requested **across every TLD** - the .net, the... | 2 | passive |
| [Favicon hash pivoting](origin-unmasking/favicon-hash.md) | This site sits behind a CDN. Which other hosts on the internet serve the **same favicon** - and is one of them the unproxied... | 2 | active |
| [MerkleMap](ct-log-search/merklemap.md) | What certificates and hostnames exist for this domain in the Certificate Transparency logs - especially the ones crt.sh did not... | 2 | passive |
| [openssl](cert-analysis/openssl.md) | What certificate is this host actually presenting right now - who issued it, to which names, and valid until when? | 2 | active |
| [SSLyze](cert-analysis/sslyze.md) | I need this host's TLS posture as **data**, not as a screenful of colour. What does it support, and does it meet a named standard... | 2 | active |
| [testssl.sh](cert-analysis/testssl.md) | What TLS configuration does this service actually run - which protocol versions and ciphers, what certificate, and does it still... | 2 | active |
| [CloudFail](origin-unmasking/cloudfail.md) | Does this Cloudflare-fronted domain have a subdomain that was never proxied, pointing straight at the origin? | 3 | active |
| [CloudFlair](origin-unmasking/cloudflair.md) | What is the real origin IP behind this Cloudflare-protected site? | 3 | active |
<!-- END:TOOLS -->
