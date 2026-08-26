# Spoofing testing

SMTP does not authenticate the `From:` header. Anyone can claim to be anyone; SPF,
DKIM, and DMARC exist to make that claim checkable, and plenty of domains still
publish weak policies. Testing whether a domain can be spoofed is legitimate work -
**on domains you own or are authorised to test**.

## What you are actually testing

1. Does the domain publish **SPF** (`TXT` record, `v=spf1 ...`), and does it end in
   `-all` (hard fail) or the far weaker `~all` / `?all`?
2. Does it publish **DMARC** (`_dmarc.<domain>` TXT), and is the policy `p=reject`,
   `p=quarantine`, or the toothless `p=none`?
3. Does the receiving side actually enforce those policies?

Check the records first - that is passive and answers most of the question:

```bash
host -t TXT example.com                # SPF lives here
host -t TXT _dmarc.example.com         # DMARC policy
```

See [../server-checks/README.md](../server-checks/README.md) for the full record
walkthrough.

## Sending a test message

[swaks](../server-checks/swaks.md) is the tool for constructing a test message with
a chosen envelope and header sender, against infrastructure you control or are
authorised to test. Send **to a mailbox you own**, then read the received message's
`Authentication-Results` header to see how SPF/DKIM/DMARC evaluated.

Public "send a spoofed mail" web forms (emkei.cz and similar) exist and are widely
demonstrated in coursework. They send real mail from infrastructure you do not
control, to a recipient of your choosing, with no audit trail. Treat them as a
teaching artifact, not an investigative tool.

## Boundary

Sending mail that impersonates a domain, to a recipient who has not consented, is
fraud in most jurisdictions regardless of intent to profit. Test only:

- domains you own, or have **written authorisation** to test, and
- with the message delivered to a mailbox you control.

See [../../LEGAL.md](../../LEGAL.md).

## Related

- [../server-checks/README.md](../server-checks/README.md) - SPF/DKIM/DMARC and mailbox verification
- [../header-analysis/README.md](../header-analysis/README.md) - reading the result
