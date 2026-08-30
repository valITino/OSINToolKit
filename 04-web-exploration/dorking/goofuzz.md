---
name: GooFuzz
slug: goofuzz
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/m3n0sd0n4ld/GooFuzz
categories: [web-exploration, dorking]
tags: [dorks, content-discovery, google-api, subdomains, passive]
status: active
status_checked: 2026-08-29
---

# GooFuzz

## What question does it answer?
I have a domain. Which files, paths, extensions and subdomains has Google
already indexed for it - found without sending a single request to the target?

## When to reach for it
When you want content discovery but cannot touch the target: no authorisation
yet, an OPSEC constraint, or a first pass before deciding whether to scan at
all. It asks Google whether a path or extension exists rather than asking the
server, so nothing appears in the target's logs - and it sees only what Google
indexed. With authorisation, [ffuf](../content-discovery/ffuf.md) or
[feroxbuster](../content-discovery/feroxbuster.md) gives you the truth; for
whole GHDB dork sets rather than a wordlist, use [pagodo](pagodo.md).

## Install
```bash
git clone https://github.com/m3n0sd0n4ld/GooFuzz && cd GooFuzz
sudo apt install jq          # plus bash/zsh, curl and sed
chmod +x GooFuzz && ./GooFuzz -h
# A Dockerfile is included: docker build -t goofuzz . && docker run --rm -it goofuzz -h
```
It needs a Google API key and a Programmable Search Engine CX ID, both free,
passed together in a keys file with `-k`.

## Usage
```bash
./GooFuzz -t example.com -k keys.txt -e pdf,doc,bak      # indexed files by extension
./GooFuzz -t example.com -k keys.txt -s -p 10 -d 5       # subdomains, 10 pages, 5s delay
./GooFuzz -t example.com -k keys.txt -w config.php,admin,/images/   # specific paths
./GooFuzz -t example.com -k keys.txt -c password -o out.txt         # pages containing a string
```
`-x` excludes hosts, `-r` sets a proxy, `-p` is pages of results (default 1).

## Output
Lists of matching URLs grouped by what produced them - extension, path, content
string, or subdomain - and written to the `-o` file when you ask for one. Each
line is an indexed URL, so it is directly usable as input to
[gowitness](../monitoring-visual/gowitness.md) or a metadata harvest.

## Gotchas
- **Configure the search engine for the whole web.** A Programmable Search
  Engine defaults to searching only the sites you list. Point it at the entire
  web or every query returns nothing, which reads exactly like a clean target.
- **The free CSE allowance is about 100 queries a day.** A dictionary run burns
  it quickly; `-p 10` is ten queries per term, not one. Use `-d` to pace, and
  expect Google to throttle or block a key it considers abused.
- **Indexed does not mean present.** Google's copy proves the file was reachable
  when it was crawled, not that it is there now - and fetching it to check is
  the `active` step this tool exists to avoid.
- **Absence is not evidence.** Anything behind robots.txt, a login or a no-index
  header is invisible here, and Google's coverage of a small site is patchy. Ask
  [another engine](../../99-resources/cheatsheets/search-operators.md) too.
- No tags or releases: a clone of `main` is the artefact, so pin a commit if you
  need the run to be reproducible.
- Using the API this way is within Google's terms; scraping the same queries
  from the web interface is not. See [../../LEGAL.md](../../LEGAL.md).

## Alternatives
- [pagodo](pagodo.md) - GHDB dork sets against one domain
- [uDork](udork.md) - the same author's earlier tool, dead since 2022
- [ffuf](../content-discovery/ffuf.md) - the authorised, intrusive answer
- [Google Hacking Database](ghdb.md) - the query patterns to feed it
