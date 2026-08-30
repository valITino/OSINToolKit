---
name: uDork
slug: udork
tier: 3
contact: passive
type: cli
cost: free
platforms: [linux, macos]
url: https://github.com/m3n0sd0n4ld/uDork
categories: [web-exploration, dorking]
tags: [dorks, automation, bash, dead, legacy]
status: broken
status_checked: 2026-08-29
superseded_by: goofuzz
---

# uDork

## What question does it answer?
I have a domain. Can one bash script run a whole set of prebuilt Google dorks -
extensions, URL strings, titles, admin panels - without me typing each one?

## Why this is tier 3
Dead, by the author's own notice of 11 June 2022: "last week Facebook withdrew
the service by which the tool made the requests, unfortunately the tool no
longer works." Every uDork query was a Google search laundered through
`developers.facebook.com/tools/debug/echo/` behind a live Facebook session
cookie; that endpoint now redirects to a business login page, confirmed
2026-08-29. No commit since 2022-06-20, no release ever.

Do not. It is here so you recognise it in the roundups that still list it, and
read a quiet run as a dead tool rather than a clean target. The author's own
replacement is [GooFuzz](goofuzz.md); for running dork sets against one
domain, use [pagodo](pagodo.md).

## Install
```bash
# Non-functional; listed for recognition only.
git clone https://github.com/m3n0sd0n4ld/uDork && cd uDork && chmod +x uDork.sh
# It then required pasting a live Facebook session into line 9 of uDork.sh:
#   cookies="c_user=XXXXXX; xs=XXXXXX;"   <- do not do this with a real account
```

## Usage
```bash
./uDork.sh host.com -e pdf -p 3          # README example: PDFs, 3 pages of results
./uDork.sh host.com -g admin             # -g runs a bundled set; -l lists them
./uDork.sh host.com -g all -o report.txt # every bundled set, exported to a file
```

## Output
When it worked: plain URLs one per line, filtered with `grep -i` on the domain
so only in-scope hits printed, then a count line and a saved report path. Today
the pipeline greps a Facebook login page for `url?q=`, matches nothing, and
prints "No results were found. Try harder!" for every dork.

## Gotchas
- **It fails to a false negative, not an error.** "No results were found" is
  what a genuinely clean domain looks like too. Never cite a uDork run as
  evidence that nothing is exposed.
- **It required a live Facebook session cookie in a shell script** - account
  credential material in plaintext on disk, with the author's own disclaimer
  that he is not responsible for what happens to the account. Do not resurrect
  the pattern with a current account.
- Its whole purpose was routing Google queries through a third party to dodge
  Google's rate limiting, which is terms-of-service exposure on both services
  at once. See [../../LEGAL.md](../../LEGAL.md).
- The bundled `./dorks` sets are GHDB-derived and frozen at 2022, carrying the
  same stale, vulnerability-centric entries [GHDB](ghdb.md) warns about.
- No tags and no releases: a clone of master is the only artefact, and the
  "v.3.1" in its banner exists only inside the script.

## Alternatives
- [GooFuzz](goofuzz.md) - the same author's working replacement
- [pagodo](pagodo.md) - maintained, runs dork sets against one domain properly
- [DorkSearch](dorksearch.md) - build and pick dorks, then run them yourself
- [Dorking by hand](README.md) - the operators, and why manual is more reliable
