---
name: checkdmarc
slug: checkdmarc
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/domainaware/checkdmarc
categories: [email-investigation, server-checks]
tags: [spf, dkim, dmarc, mta-sts, phishing]
status: active
status_checked: 2026-08-26
---

# checkdmarc

## What question does it answer?
This message claims to come from example.com. **Could** it have? What does that
domain's published policy actually say, and would a forgery have been rejected or
delivered?

## When to reach for it
Phishing triage, and the fastest honest answer to "is this spoofable". checkdmarc pulls
and *parses* a domain's SPF, DMARC, MX, MTA-STS, TLS-RPT, BIMI and DNSSEC records in one
command and tells you whether each is valid, rather than leaving you to read a TXT
record by eye. The parsing matters: SPF has a ten-lookup limit that silently invalidates
a record, and a DMARC policy of `p=none` looks like protection while permitting
everything.

Use it alongside [MXToolbox](../header-analysis/mxtoolbox.md) - that answers the same
questions in a browser; this one answers them for a hundred domains into a CSV. See the
[phishing triage playbook](../../workflows/phishing-email-triage.md) for where it sits
in a real workflow.

## Install
```bash
pipx install checkdmarc          # needs Python 3.10+
```

## Usage
```bash
checkdmarc example.com --skip-tls                        # DNS records only
checkdmarc example.com -n 1.1.1.1 8.8.8.8                # pin resolvers; domain FIRST
checkdmarc domains.txt -f csv -o report.csv -w 1.0       # bulk, rate-limited
checkdmarc example.com -d                                # add tag descriptions to the JSON
```

## Output
JSON by default with one section each for `spf`, `dmarc`, `mx`, `ns`, `dnssec`, `soa`,
`mta_sts`, `smtp_tls_reporting` and `bimi`. Each carries `valid`, the raw `record`,
parsed `tags`, and any `warnings` or `error`. `-f csv` flattens it into one row per
domain, which is the form to hand a non-technical reader.

## Gotchas
- **Put the domain before `-n`, `--mx`, or `--ns`.** Those flags take multiple values and
  will greedily swallow a trailing domain argument, leaving you with "the following
  arguments are required: domain".
- **Without `--skip-tls` it connects to the domain's mail servers** to test STARTTLS.
  That is real contact with a third party's infrastructure - use `--skip-tls` when you
  want a purely passive DNS answer.
- `valid: false` on SPF often means the record blew the **ten-lookup limit**, not that
  it is absent. Read the `error` field before reporting "no SPF".
- **`p=none` is not protection.** A valid DMARC record with `p=none` monitors and
  publishes nothing enforceable; treat it as spoofable.
- These records describe what a *receiver should have done*. They do not tell you what
  the receiver actually did - for that you need the message's own
  [headers](../header-analysis/README.md).
- DKIM cannot be enumerated from DNS: selectors are arbitrary, so you can only check one
  you already know from a header.
- Bulk runs are a lot of DNS queries. Use `-w` to space them out.

## Alternatives
- [MXToolbox](../header-analysis/mxtoolbox.md) - the same checks in a browser, no install
- [swaks](swaks.md) - what the server does in practice, rather than what it publishes
- [dig](../../03-dns-and-subdomains/query-tools/dig.md) - read the raw TXT records yourself
