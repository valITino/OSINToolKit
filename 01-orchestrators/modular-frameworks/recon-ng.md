---
name: recon-ng
slug: recon-ng
tier: 1
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/lanmaster53/recon-ng
categories: [orchestrators, modular-frameworks]
tags: [framework, workspaces, database, modules]
status: unverified
status_checked: 2026-08-26
---

# recon-ng

## What question does it answer?
I am running a real case over days or weeks. Where do I keep every host, contact,
and credential I find so that each new module builds on the last instead of
starting from a blank page?

## When to reach for it
When the case needs a memory. recon-ng is a Metasploit-style framework with a
per-workspace SQLite database: hosts, contacts, domains, and credentials
accumulate in tables, and modules read from and write back to them. Reach for it
over [theHarvester](../aggregators/theharvester.md) when you want persistence and
a structured DB rather than a one-shot sweep, and over
[Maltego](maltego.md) when you want scripting instead of a GUI.

## Install
```bash
pipx install recon-ng      # Kali ships it; pipx tracks upstream
```

## Usage
```text
workspaces create acme            # a database scoped to this case
marketplace install all           # or install only the modules you need
modules load recon/domains-hosts/hackertarget
options set SOURCE acme.com
run                               # results land in the hosts table
show hosts                        # review; feed into the next module
```

## Output
Populated database tables (hosts, contacts, domains, ports, credentials) you can
query, and a reporting module set that renders them to HTML/CSV. State persists
across sessions in the workspace.

## Gotchas
- Many marketplace modules need API keys (`keys add <name> <value>`). Without
  them the module simply returns nothing rather than erroring loudly.
- Modules come and go from the marketplace; pin the ones a workflow depends on.
- Most modules are passive, but a few resolve or request the target - check the
  module's source before running it if OPSEC matters.

## Alternatives
- [theHarvester](../aggregators/theharvester.md) - quick, stateless, one command
- [SpiderFoot](../recursive-scanners/spiderfoot.md) - broader automation, correlation graph
- [Maltego](maltego.md) - when the output needs to be a visual for stakeholders
