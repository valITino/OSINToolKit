---
name: dorkscout
slug: dorkscout
tier: 3
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/R4yGM/dorkscout
categories: [web-exploration, dorking]
tags: [dorks, ghdb, automation, go, unmaintained]
status: broken
status_checked: 2026-08-29
superseded_by: pagodo
---

# dorkscout

## What question does it answer?
I have a domain. Can I pull the whole GHDB down as flat category files and fire
the lot at that domain from one command?

## Why this is tier 3
The `scan` half no longer works and does not say so. It parses Google results
by looking for `div.g` elements, which current result pages do not contain - a
live fetch on 2026-08-29 returned 92 KB with zero matches. It prints "Finished
scanning", exits 0, and reports nothing whether or not the target has anything
indexed. Upstream stopped in August 2021 (one release, tag 1.0).

What still works is `dorkscout install`, which fetches the GHDB into flat
per-category files - a usable dork dump to feed something else. To run dorks
against a domain use [pagodo](pagodo.md), which handles delays and proxies.

## Install
```bash
go install github.com/R4yGM/dorkscout@latest   # builds under go1.24.7, 2026-08-29
# The README's `go get` no longer installs binaries. The docker image
# r4yan/dorkscout:1.0 and the 1.0 release binaries are the same 2021 code.
```

## Usage
```bash
dorkscout install --output-dir ./dorks   # the only working subcommand: 15 GHDB files
touch ./out.txt                          # mandatory - -O aborts on a missing file
dorkscout scan -d "./dorks/Sensitive Directories.dorkscout" -t example.com -l 50 -O ./out.txt   # -l caps hits per dork
dorkscout scan -d "./dorks/Sensitive Directories.dorkscout" -H ./a.html -x socks5://127.0.0.1:9050  # HTML report via proxy
```

## Output
`install` prints one `[+] ./<Category>.dorkscout` line per file and drops a
hidden `.dorkscout` receipt of JSON reporting `"payloads":7944`. Each file is
one dork per line, ready to feed anything else.

`scan` prints a start line, result URLs, then "Finished scanning"; `-O` writes
plain text, `-H` an HTML table. A scan of a well-indexed target and a scan of
nothing at all are byte-for-byte identical.

## Gotchas
- **It fails to a false negative.** No results, no error, exit 0. An
  investigator reading that concludes "nothing exposed" when nothing was ever
  searched. Never cite a dorkscout scan as evidence.
- The URL circulating in tool lists, `obheda12/dorkscout`, is a 404 - that
  account wrote [GitDorker](gitdorker.md); dorkscout is R4yGM's.
- `-O` and `-H` abort with `remove <path>: no such file or directory` unless
  the output file already exists. Create it first.
- Automating google.com/search breaches Google's terms at any volume, and its
  own help advertises proxy rotation "to avoid getting blocked" - that raises
  the terms-of-service exposure rather than settling it. See
  [../../LEGAL.md](../../LEGAL.md).
- Its parser drops or merges entries: 7,944 payloads reported against 6,536
  lines written, some visibly concatenated. Read a line before running it.
- The corpus is GHDB, and inherits its problems - much of it is old,
  vulnerability-hunting material rather than discovery material.

## Alternatives
- [pagodo](pagodo.md) - the maintained way to run GHDB dorks at scale
- [GHDB](ghdb.md) - the corpus itself, browsable and current
- [DorkSearch](dorksearch.md) - the same corpus, with descriptions and export
