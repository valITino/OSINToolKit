# OPSEC

The subject can investigate back. Every query you make can leak your identity,
your interest, or your intent - through your IP in a server log, a Transform
routed via a third party, a sock-puppet account tied to your real one, or malware
in a sample you opened on your daily-driver machine. Plan this before the first
lookup, not after.

## Isolate the work

- **A dedicated VM**, snapshotted, is the baseline. Investigate from it; revert it
  when done. Never open a suspicious sample or click a subject's link from your
  host OS. Wireshark and analysis tools live here too.
- Keep investigation browsers, accounts, and infrastructure separate from
  personal ones. Containers or separate profiles at minimum; separate machines for
  sensitive work.

## Attribute nothing to yourself

- **Sock puppets**: research personas that are not linked to you. Building a
  credible one takes time and consistency; a throwaway account created five minutes
  ago is itself a signal. Respect platform terms - many prohibit this.
- **Network**: route through a VPN or Tor so the target's logs do not show your
  real IP. [proxychains](proxychains.md) chains tools that do not natively support a
  proxy through one. Understand what each hop does and does not hide.

## Remember which "passive" tools still tip off the subject

Passive to you is not always invisible to them:

- [Maltego](../../01-orchestrators/modular-frameworks/maltego.md) Transforms and
  similar API queries route through logging third parties, and some do active
  lookups against the target.
- Submitting a URL to [urlscan.io](../../04-web-exploration/fingerprinting/urlscan-io.md)
  (or any sandbox) fetches the target from the sandbox and may make the scan public.
- [Lure tokens](../../08-people-and-identity/ip-luring/canarytokens.md) work by
  making the subject contact you - inherently an interaction.

See [../../LEGAL.md](../../LEGAL.md) for the legal weight of these.

## Tools here

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [proxychains](proxychains.md) | How do I route a tool that has no proxy support of its own through Tor or a SOCKS | 2 | passive |
<!-- END:TOOLS -->

## Related

- [../frameworks/README.md](../frameworks/README.md)
- [../documentation/README.md](../documentation/README.md)
