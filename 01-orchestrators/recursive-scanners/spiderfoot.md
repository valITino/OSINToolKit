---
name: SpiderFoot
slug: spiderfoot
tier: 1
contact: active
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/smicallef/spiderfoot
categories: [orchestrators, recursive-scanners]
tags: [correlation, domain, ip, email, automation]
status: unverified
status_checked: 2026-08-26
---

# SpiderFoot

## What question does it answer?
I have a domain, IP, email, or name. What is everything the public internet
already knows about it, and how do those facts connect to each other?

## When to reach for it
First pass on a new target when you want breadth and a correlation graph without
scripting it yourself. 200+ modules feed one dataset, so a subdomain found by CT
logs gets cross-referenced against reputation and breach data automatically.
Reach for [BBOT](bbot.md) instead when you want a fast, CLI-first, scriptable run
and can live without the web UI.

## Install
```bash
# Upstream recommends a packaged release over master:
wget https://github.com/smicallef/spiderfoot/archive/v4.0.tar.gz
tar zxvf v4.0.tar.gz && cd spiderfoot-4.0
pip3 install -r requirements.txt
```
There is no official PyPI package - **do not `pip install spiderfoot`**; the name
on PyPI is not the project. Kali also packages it as `spiderfoot`.

## Usage
```bash
spiderfoot -l 127.0.0.1:5001                       # start the web UI, then scan from the browser
spiderfoot -s example.com -t DOMAIN_NAME -o csv    # headless scan, CSV to stdout
spiderfoot -s example.com -u passive               # passive modules only (no target contact)
```

## Output
A scan is a graph of "entities" (hosts, IPs, emails, breaches, SSL certs) linked
by the module that produced each edge. The web UI shows the graph, a searchable
table, and a correlation view that surfaces notable clusters. Headless runs emit
CSV/JSON for piping into other tools.

## Gotchas
- Scans on large targets can run for **many hours**. Scope the modules and the
  target type before you start; do not point it at a broad asset and walk away.
- Full power needs API keys (Shodan, VirusTotal, HIBP, and dozens more). Without
  keys you get a fraction of the coverage. See
  [../../99-resources/api-keys/README.md](../../99-resources/api-keys/README.md).
- The default profile includes active modules that touch the target. Use
  `-u passive` when OPSEC matters.

## Alternatives
- [BBOT](bbot.md) - same concept, async, faster, CLI-first
- [recon-ng](../modular-frameworks/recon-ng.md) - when you want a persistent case database
- [theHarvester](../aggregators/theharvester.md) - narrower, quicker email/subdomain sweep
