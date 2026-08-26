---
name: DirBuster
slug: dirbuster
tier: 3
contact: intrusive
type: gui
cost: free
platforms: [linux, windows]
url: https://wiki.owasp.org/index.php/Category:OWASP_DirBuster_Project
categories: [web-exploration, content-discovery]
tags: [legacy, deprecated, java, content-discovery]
status: archived
status_checked: 2026-08-26
superseded_by: gobuster
---

# DirBuster

## What question does it answer?
What directories and files exist on this web server that nothing links to?

## Why this is tier 3
**Deprecated - do not use it for new work.** DirBuster is an old OWASP Java GUI
application that is no longer actively developed, is slow, and is heavy to run
compared with anything current. Its lasting contribution is its **wordlists**, which
were folded into SecLists and are still widely used. Use
[gobuster](gobuster.md), [ffuf](ffuf.md), or [feroxbuster](feroxbuster.md) instead -
all three are faster, maintained, and scriptable.

It is documented here only because it appears constantly in older course material and
tutorials, and you should know why not to reach for it.

## Install
```bash
# Historically bundled with Kali; no longer the recommended path.
# Take the wordlists from SecLists instead - see 99-resources/wordlists/.
```

## Usage
```text
Java GUI: enter the target URL, choose a wordlist and extensions, start the scan.
```

## Output
A tree and list view of discovered paths with response codes - the same information
modern CLI tools stream to stdout.

## Gotchas
- **Intrusive**, like every content brute forcer. Written authorisation required.
- Java GUI overhead makes it slow and awkward to script or run remotely.
- No active maintenance; expect no fixes.

## Alternatives
- [gobuster](gobuster.md) - the standard replacement
- [feroxbuster](feroxbuster.md) - recursive
- [ffuf](ffuf.md) - most flexible
- [../../99-resources/wordlists/README.md](../../99-resources/wordlists/README.md) - the wordlists, which are still good
