---
name: torsocks
slug: torsocks
tier: 2
contact: active
type: cli
cost: free
platforms: [linux, macos]
url: https://gitlab.torproject.org/tpo/core/torsocks
categories: [darkweb, access-and-opsec]
tags: [tor, socks, proxy, ld-preload, cli-wrapper]
status: active
status_checked: 2026-08-29
---

# torsocks

## What question does it answer?
I have a CLI tool with no `--proxy` flag and a .onion address to point it at.
How do I force its traffic and its DNS through Tor, and have it fail loudly
rather than leak if it cannot?

## When to reach for it
When a tool has no native proxy support and you need Tor specifically. Its value
over a general SOCKS chainer is the failure mode: traffic it cannot torify is
denied and the application forced to quit, not quietly sent in the clear. Prefer
a tool's own proxy support when it has one, and [Whonix](whonix.md) when the
tool is untrusted - a VM boundary catches what an `LD_PRELOAD` shim cannot.

## Install
```bash
sudo apt install torsocks tor    # Debian trixie ships 2.5.0; Kali has it already
brew install torsocks            # macOS; also builds on FreeBSD
git clone https://gitlab.torproject.org/tpo/core/torsocks  # the real upstream
cd torsocks && ./autogen.sh && ./configure && make && sudo make install
```

## Usage
```bash
torsocks curl https://check.torproject.org/api/ip   # ALWAYS first: want {"IsTor":true,...}
torsocks -i curl http://<address>.onion/            # -i isolates this run on its own circuit
torsocks -a 127.0.0.1 -P 9150 python3 collect.py    # Tor Browser's SOCKS port, not 9050
torsocks --shell                                    # subshell where every command is torified
```

## Output
None of its own - it wraps the target command, whose output comes through
unchanged. `-d` writes interception decisions to stderr, `-q` suppresses
everything including errors. Treat it as a boolean: either check.torproject.org
returned `IsTor:true` for this exact binary, or you do not trust the run.

## Gotchas
- **Illegal material can appear unbidden when you fetch from a hidden service,
  and downloading it is an offence in most jurisdictions regardless of intent.**
  A scripted fetch saves whatever it is given, unseen, to your disk. Settle your
  evidence-handling and reporting duties - [../../LEGAL.md](../../LEGAL.md).
- **It is `LD_PRELOAD`, so it is not universal.** Upstream says that if an
  application does not use libc, or uses raw syscalls, torsocks is useless and
  the traffic does not go through Tor. Statically linked binaries and Go
  programs sail past it while appearing to work - a confident wrong conclusion.
- setuid binaries ignore `LD_PRELOAD` by design, so anything you run under
  `sudo` is not torified by a `torsocks` prefix on the `sudo`.
- On macOS it uses `DYLD_INSERT_LIBRARIES`, which System Integrity Protection
  strips for system binaries: `torsocks curl` against `/usr/bin/curl` can do
  nothing at all, silently. Use a Homebrew-installed binary and re-verify.
- TCP only. UDP and ICMP are refused, so `ping`, `traceroute` and nmap UDP scans
  do not work through it - and should not, because they would leak.
- It needs a Tor SOCKS port already listening: 127.0.0.1:9050 for the tor
  daemon, 9150 for Tor Browser. `-i` is mutually exclusive with `-u`/`-p`, and
  `-6` only exists from 2.5.0, so scripts break on bookworm's 2.4.0.
- **Cite the GitLab project, not github.com/dgoulet/torsocks.** That mirror
  stopped at v2.3.0 in 2018; upstream shipped v2.5.0 in 2025 and Debian follows.
- Reaching an onion service through torsocks is active contact - the service
  logs the connection exactly as it would from a browser. Circuit isolation
  hides your connections from each other, not from the destination.

## Alternatives
- [proxychains](../../00-methodology/opsec/proxychains.md) - SOCKS chaining, but fail-open
- [Whonix](whonix.md) - enforce it at the network layer instead of in the loader
- [Tor Browser](tor-browser.md) - when the tool you need is a browser anyway
