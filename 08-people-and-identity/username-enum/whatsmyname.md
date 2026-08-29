---
name: WhatsMyName
slug: whatsmyname
tier: 2
contact: active
type: web
cost: free
platforms: [web, linux, macos, windows]
url: https://whatsmyname.app/
categories: [people-and-identity, username-enum]
tags: [username, dataset, json, community]
status: active
status_checked: 2026-08-26
---

# WhatsMyName

## What question does it answer?
I have a username. Where does it exist - and can I see the actual detection rule for
each site, so I can judge whether a hit is real?

## When to reach for it
When you care about the evidence behind a hit. WhatsMyName is not a checker; it is a
**dataset** that checkers read. A single `wmn-data.json` describes each site by URL
pattern, the HTTP status and response string that mean "found", and the ones that mean
"not found". That separation is the reason to prefer it: you can read exactly why a
tool called an account a match, instead of trusting its verdict.

Note which tools actually use it. [Maigret](maigret.md) and [Sherlock](sherlock.md)
maintain their own separate site lists and do **not** read this file; Blackbird and
Naminter do. So a WhatsMyName hit and a Sherlock hit are independent signals, not the
same one twice.

Use [whatsmyname.app](https://whatsmyname.app/) for a no-install run with category
filters and CSV export. Use the JSON when you are writing your own tooling or auditing
another tool's false positives.

## Install
```bash
# Nothing to install for the web app. For the raw data:
curl -O https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json
```

## Usage
```text
https://whatsmyname.app/          # enter the username; filter by category; export CSV
```
```bash
jq -r '.sites[] | select(.cat=="coding") | .name' wmn-data.json   # which coding sites are covered
jq -c '.sites[] | select(.name|test("github";"i"))' wmn-data.json  # the exact rules behind one site
```

## Output
Each site entry carries `uri_check` (the URL the checker requests, `{account}`
substituted), `e_code` and `e_string` (the status and body text that mean the account
exists), `m_code` and `m_string` (the "missing" equivalents), `cat`, and a `protection`
field flagging sites behind bot defences. Note `uri_check` is often an API endpoint -
where an entry also has `uri_pretty`, that is the human-facing profile URL and the one
to put in a report. `known` lists real accounts you can use to sanity-check a rule. At
the time of checking the file covered 716 sites across 21 categories.

## Gotchas
- **The project stopped shipping its checker in May 2023** and focuses on the data.
  Anything marketed as "the WhatsMyName tool" is a third-party consumer of the JSON.
- A match means a profile page exists at that URL, **not** that your subject owns it.
  Common handles collide constantly. Corroborate before linking accounts to a person.
- Sites marked `protection` sit behind Cloudflare or similar; results there are the
  least reliable and vary by checker.
- **Match on `name` loosely.** Entries are often qualified rather than bare - GitHub
  appears as `GitHub (User)` and `GitHub (Gists)`, not `GitHub` - so an exact `==`
  filter quietly returns nothing. Use `test("...";"i")`.
- Running a full sweep sends a request to hundreds of sites from your IP, which is
  visible to every one of them. See [../../00-methodology/opsec/README.md](../../00-methodology/opsec/README.md).
- Licensed CC BY-SA 4.0 - attribute it if you redistribute the data.

## Alternatives
- [Maigret](maigret.md) - fetches and parses the profiles, not just their existence
- [Sherlock](sherlock.md) - the widely known checker, its own site list
- [holehe](../email-osint/holehe.md) - the same idea starting from an email address
