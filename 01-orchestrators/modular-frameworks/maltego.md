---
name: Maltego
slug: maltego
tier: 1
contact: passive
type: gui
cost: freemium
platforms: [linux, macos, windows]
url: https://www.maltego.com/
categories: [orchestrators, modular-frameworks]
tags: [link-analysis, graph, transforms, visualization]
status: unverified
status_checked: 2026-08-26
---

# Maltego

## What question does it answer?
I have a set of entities (people, domains, IPs, accounts) and a tangle of
relationships. How do they connect, and how do I show that connection to someone
who is not technical?

## When to reach for it
When the deliverable is a picture. Maltego is the industry standard for
*presenting* link analysis to stakeholders, courts, and clients. You run
"Transforms" that expand an entity into related ones (domain to subdomains,
email to breaches) and the graph grows visually. It is less about discovery
(orchestrators like [SpiderFoot](../recursive-scanners/spiderfoot.md) find more,
faster) and more about structuring and communicating what you already have.

## Install
```bash
# Download the desktop client from maltego.com and register a free account.
# Kali ships a launcher; it still fetches the current client on first run.
```

## Usage
```text
1. Drop an entity onto the graph (e.g. a Domain).
2. Right-click -> run a Transform (e.g. "To DNS Name [Attempt Zone Transfer]").
3. Iterate outward; pin and colour-code entities as the picture forms.
4. Export the graph as an image or report for the write-up.
```

## Output
An interactive link graph. Entities are nodes; Transforms are the labelled edges
that produced them. Exportable to image, PDF, and structured report formats.

## Gotchas
- The free "Community Edition" is now the **Basic** plan: free, **24 results per
  Transform, 200 credits/month**. Enough to learn on; not enough for a large case.
- OPSEC: running Transforms routes queries through third-party Transform servers,
  which can log the lookup, and some Transforms perform **active** lookups against
  the target despite the passive-looking graph. Assume a Transform can tip off the
  subject. See [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [SpiderFoot](../recursive-scanners/spiderfoot.md) - automated discovery, also graphs
- [recon-ng](recon-ng.md) - scriptable, database-backed, no GUI
