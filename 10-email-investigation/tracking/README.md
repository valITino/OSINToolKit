# Tracking

Email tracking works by making the recipient's mail client fetch something from a
server you control. Understanding the mechanism matters two ways: recognising when
*you* are being tracked, and (defensively, with authorisation) confirming that an
address is live and monitored.

## How it works

- **Tracking pixel**: a 1x1 image whose URL is unique per recipient. When the client
  loads remote images, the server logs the fetch - open time, IP, and User-Agent
  (client and rough platform).
- **Unique links**: any link with a per-recipient token records the click the same
  way.
- What it reveals: that the message was opened, roughly when, and the opener's IP
  and mail client. It does **not** reveal message content or reply intent.

## Spotting it in a message you received

- View the raw source and look for remote image URLs with long, unique-looking query
  strings or per-message subdomains.
- Most modern clients block remote image loading by default - that block is the
  defence. Keep it on for anything untrusted.

## Defensive / authorised use

- [Canarytokens](../../08-people-and-identity/ip-luring/canarytokens.md) is the
  defensively-framed version: generate a token (a URL, a document, a DNS name), place
  it, and get alerted with an IP when someone interacts. Legitimate for tripwires on
  your own assets and for authorised engagements.
- Hosted "read receipt" services (GetNotify and similar) do the same with less
  control and more third-party exposure.

## Boundary

Tracking a person without a lawful basis - especially to obtain their IP or
location - can breach privacy law and platform terms. Use the defensive framing,
and see [../../LEGAL.md](../../LEGAL.md) and
[ip-luring](../../08-people-and-identity/ip-luring/README.md) for the legal weight.

## Related

- [../header-analysis/README.md](../header-analysis/README.md)
- [../../08-people-and-identity/ip-luring/canarytokens.md](../../08-people-and-identity/ip-luring/canarytokens.md)
