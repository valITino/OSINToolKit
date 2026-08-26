# TLS fingerprinting

Even when TLS hides *what* is being sent, *how* the client negotiates the
handshake identifies the software sending it. The ClientHello - cipher suites,
extensions, elliptic curves, and their order - is remarkably specific to a given
client build. Hash it and you get a fingerprint you can match across sessions.

## JA3 and JA4

- **JA3 / JA3S** (Salesforce, 2017): an MD5 over selected ClientHello (JA3) or
  ServerHello (JA3S) fields. Widely deployed but easy to collide and to spoof, and
  now largely superseded.
- **JA4+** (FoxIO): a newer suite (JA4 for TLS clients, plus JA4H/JA4S/JA4L/... for
  HTTP, server, and latency). More robust, human-readable prefixes, and designed to
  resist the weaknesses JA3 had. Prefer JA4 for new work.

## What it answers

- "Are these two sessions the same client/tool?" - malware families and specific
  bots often share a fingerprint even across IPs.
- "Does this client claim to be a browser but fingerprint as a scripting library?"
  - a mismatch between User-Agent and TLS fingerprint is a strong tell.

## How to get the fingerprint

- From a capture: recent [Wireshark/tshark](../capture/wireshark-tshark.md) builds
  and Zeek expose JA3/JA4 fields; extract `tls.handshake.ja3` (or the JA4 plugin
  output) with `tshark -T fields`.
- The fingerprint is only as good as your corpus - you need known-good and
  known-bad samples to compare against.

## Decrypting the payload (your own traffic)

To read TLS contents in a capture you control, log the session keys and point
Wireshark at them:

```bash
export SSLKEYLOGFILE=~/tls-keys.log     # then launch the browser/app from this shell
# Wireshark: Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename
```

This only works for traffic whose keys you can log - it is not a way to decrypt a
third party's session.

## Related

- [../capture/wireshark-tshark.md](../capture/wireshark-tshark.md)
- [../analysis/networkminer.md](../analysis/networkminer.md)
