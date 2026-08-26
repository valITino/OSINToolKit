---
name: SSLyze
slug: sslyze
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/nabla-c0d3/sslyze
categories: [certificates-tls, cert-analysis]
tags: [tls, json, mozilla-config, starttls]
status: active
status_checked: 2026-08-26
---

# SSLyze

## What question does it answer?
I need this host's TLS posture as **data**, not as a screenful of colour. What does it
support, and does it meet a named standard - as a pass or fail I can put in a pipeline?

## When to reach for it
When the answer has to be machine-readable or repeatable. [testssl.sh](testssl.md)
prints a superb human report; SSLyze writes structured JSON and, by default, grades the
server against Mozilla's published TLS configurations and **exits non-zero if it fails**.
That makes it the one to use across a list of hosts, or as a check that runs
repeatedly and has to be diffed.

It also speaks STARTTLS for SMTP, IMAP, POP3, FTP, LDAP, RDP, XMPP and Postgres, so it
reaches mail and directory servers that HTTPS-only tooling cannot.

## Install
```bash
sudo apt install sslyze              # Kali ships 6.3.1
pip install --upgrade sslyze         # needs Python 3.10+; gives 'sslyze' and 'python -m sslyze'
```

## Usage
```bash
sslyze example.com                                   # default: check vs Mozilla "intermediate"
sslyze --mozilla_config=modern example.com           # stricter bar; exit code reflects it
sslyze --json_out=scan.json --targets_in hosts.txt   # many hosts, structured output
sslyze --starttls=auto mail.example.com:587          # mail server, protocol deduced from port
```

## Output
A per-host report on stdout ending in `OK - Compliant` or `FAILED - Not compliant` with
the specific reasons (certificate type, signature algorithm, cipher suites). `--json_out`
writes the full `ScanResult` structure - the same object tree as its Python API - and
`--json_out=-` sends it to stdout for piping. The exit code is the part worth wiring
into automation.

## Gotchas
- **`--regular` no longer exists.** It was removed in 5.0.0; passing it now is an
  argparse error. Current SSLyze runs the Mozilla check by default and needs no
  equivalent flag. Kali's own tools page still prints the stale `--regular` example -
  ignore it.
- **Naming any scan command disables the default set**, and with it the Mozilla
  compliance check and its exit code. Add `--mozilla_config` back explicitly if you
  want both.
- `--json_out -` cannot be combined with `--quiet`; the parser rejects the pair.
- Scanning is **active**: it opens many connections to test cipher suites and
  extensions, which is visible in the target's logs and may trip rate limiting. Get
  authorisation - see [../../LEGAL.md](../../LEGAL.md).
- Its `--heartbleed`, `--robot`, `--openssl_ccs` flags are **detection** checks that
  report whether a server is vulnerable. Exploitation is out of scope for this
  reference; do not treat a positive result as licence to go further.
- Results reflect what the server offers *your* client from *your* network. CDNs answer
  differently by geography and SNI - set `--sni` explicitly on a virtual host.
- A "not compliant" verdict is against Mozilla's opinionated baseline, not a law or a
  breach. Read the reasons before reporting it as a finding.
- Chain-validation verdicts come from bundled CA stores that go stale. Run
  `sslyze --update_trust_stores` before relying on one.

## Alternatives
- [testssl.sh](testssl.md) - the better read for a human, no Python needed
- [openssl](openssl.md) - one handshake, full certificate detail, already installed
- [crt.sh](../ct-log-search/crt-sh.md) - certificate history without touching the host
