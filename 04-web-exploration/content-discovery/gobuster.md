---
name: gobuster
slug: gobuster
tier: 2
contact: intrusive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/OJ/gobuster
categories: [web-exploration, content-discovery]
tags: [content-discovery, dns, vhost, brute-force]
status: unverified
status_checked: 2026-08-26
---

# gobuster

## What question does it answer?
I am authorised to test this target. What directories, DNS subdomains, or virtual
hosts exist, brute-forced from a wordlist?

## When to reach for it
The straightforward workhorse, and the tool that replaced
[DirBuster](dirbuster.md) - use this instead, always. Its modes are separate and
explicit (`dir`, `dns`, `vhost`, `fuzz`), which makes it easy to reason about and
hard to misfire. Pick [feroxbuster](feroxbuster.md) when you want recursion, or
[ffuf](ffuf.md) when you need to fuzz somewhere other than the path.

## Install
```bash
sudo apt install gobuster       # Kali default
```

## Usage
```bash
gobuster dir -u https://example.com -w /usr/share/seclists/Discovery/Web-Content/common.txt
gobuster dns -d example.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
gobuster vhost -u https://example.com -w subs.txt --append-domain
gobuster dir -u https://example.com -w list.txt -x php,bak -t 10   # extensions, fewer threads
```

## Output
One line per hit with the path or name, the HTTP status, and the response size.
`dns` mode prints resolving names; `vhost` prints hosts whose response differs from
the baseline.

## Gotchas
- **Intrusive** in every mode - `dns` brute forcing hits the target's nameservers
  just as `dir` hits the web server. Written authorisation; see [../../LEGAL.md](../../LEGAL.md).
- Default thread count is aggressive for small sites; drop `-t` and consider `--delay`.
- No recursion. A found directory needs a second run against it - that is the
  trade-off for the simpler model.
- Wildcard DNS makes `dns` mode return everything; check before you trust a big list.

## Alternatives
- [feroxbuster](feroxbuster.md) - recursive
- [ffuf](ffuf.md) - fuzz any position
- [subfinder](../../03-dns-and-subdomains/passive-enum/subfinder.md) - passive subdomains, no brute forcing
