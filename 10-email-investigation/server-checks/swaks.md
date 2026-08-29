---
name: swaks
slug: swaks
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://www.jetmore.org/john/code/swaks/
categories: [email-investigation, server-checks]
tags: [smtp, testing, spf, verification]
status: unverified
status_checked: 2026-08-26
---

# swaks

## What question does it answer?
How does this mail server actually behave - what does it advertise, does it accept
mail for this address, and how does it evaluate authentication?

## When to reach for it
The scriptable SMTP transaction tool, and far easier than driving a session by hand
over telnet. Use it to inspect a server's capabilities, to test whether your own
domain can be spoofed, and to check authentication handling against infrastructure you
control or are authorised to test.

## Install
```bash
sudo apt install swaks        # Kali/Debian; it is a single Perl script
```

## Usage
```bash
swaks --to user@example.com --server mail.example.com --quit-after RCPT   # probe without sending
swaks --to me@mydomain.com --from test@mydomain.com --server mail.mydomain.com  # authorised test
swaks --to user@example.com --server mail.example.com --quit-after EHLO    # capabilities only
```

`--quit-after RCPT` stops the transaction before `DATA`, so no message is delivered -
this is the form to use for verification.

## Output
The full SMTP conversation, both directions, with each response code. The banner
identifies the server software; `EHLO` output lists supported extensions; the `RCPT
TO` response is where mailbox-existence evidence lives.

## Gotchas
- **Callback verification is unreliable.** Many servers accept every recipient
  (catch-all), greylist first attempts, or deliberately return misleading codes to
  defeat address harvesting. A 250 is weak evidence the mailbox exists; a 550 is
  slightly stronger evidence it does not.
- **Repeated probing looks like address harvesting** and can get you blacklisted or,
  worse, treated as an attack. Rate-limit and stay in scope.
- **Sending mail that impersonates a domain, to someone who has not consented, is
  fraud in most jurisdictions.** Test only your own domains or with written
  authorisation, and deliver only to mailboxes you control. See
  [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [MXToolbox](../header-analysis/mxtoolbox.md) - the same checks from a browser
- [checkdmarc](checkdmarc.md) - SPF/DMARC/MTA-STS parsed and validated, in bulk
- [host](../../03-dns-and-subdomains/query-tools/host.md) - SPF/DMARC records without any SMTP contact
