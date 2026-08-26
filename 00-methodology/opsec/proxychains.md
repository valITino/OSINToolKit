---
name: proxychains
slug: proxychains
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/haad/proxychains
categories: [methodology, opsec]
tags: [proxy, tor, socks, anonymity]
status: unverified
status_checked: 2026-08-26
---

# proxychains

## What question does it answer?
How do I route a tool that has no proxy support of its own through Tor or a SOCKS
proxy, so the target does not see my real IP?

## When to reach for it
When the tool you need lacks a `--proxy` flag. proxychains hooks network calls at the
library level and forces them through your configured chain, which is how CLI tools
that were never written with anonymity in mind end up going through Tor. Prefer a
tool's **native** proxy support when it has one - it is more reliable and leaks less.

## Install
```bash
sudo apt install proxychains4      # Kali default; config at /etc/proxychains4.conf
```

## Usage
```bash
proxychains4 curl https://example.com          # single command through the chain
proxychains4 -q nmap -sT -Pn example.com        # quiet mode; note the caveats below
```

Config essentials in `/etc/proxychains4.conf`: choose `dynamic_chain` (skips dead
proxies) over `strict_chain`, keep `proxy_dns` enabled to stop DNS leaking, and set
the endpoint - Tor's default is `socks5 127.0.0.1 9050`.

## Output
No output of its own; it wraps the target command. Verify it is working before you
rely on it - `proxychains4 curl https://ifconfig.me` should show the exit node's IP,
not yours.

## Gotchas
- **It does not catch everything.** Statically linked binaries, raw sockets, and
  anything using its own network stack bypass the hook entirely and leak your real IP.
  **Always verify with a test request first**, and never assume coverage.
- **UDP does not work over SOCKS**, so `nmap` UDP scans and most raw-packet modes
  either fail or leak. TCP connect scans (`-sT`) are the only sane option.
- Enable `proxy_dns` or your DNS queries go direct and expose what you are looking up.
- Tor exit nodes are widely blocked and publicly listed, so this is not covert - the
  target may see traffic from a known exit node, which is itself a signal
  ([ExoneraTor](../../02-network-and-ip/reputation/exonerator.md) is the other side
  of this coin).
- Anonymity is not authorisation. Routing through a proxy does not make an intrusive
  scan legal; see [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- A VPN at the network layer - simpler and catches all traffic
- Native `--proxy` support in the tool itself, whenever it exists
