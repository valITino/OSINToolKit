# Contributing

This repo maps investigation tools to the questions they answer. A good
contribution makes it faster for an analyst holding one artifact — an IP, a
domain, a photo — to find the right next tool. Read this before opening a PR.

## The one rule

Every tool file must answer, in the investigator's voice, **"what question does
it answer?"** Not "what does it do." The difference:

- Bad: "WhatWeb is a web scanner that identifies technologies."
- Good: "I have a URL. What is this site built with, and does that match what
  the operator claims?"

If you cannot phrase the tool as the analyst's question, it probably does not
belong here yet.

## Frontmatter schema

Every tool file starts with YAML frontmatter. All fields are required. Copy
[`templates/tool-template.md`](templates/tool-template.md) to start.

```yaml
name: CMSmap              # display name, as the project spells it
slug: cmsmap              # kebab-case, must match the filename
tier: 2                   # 1 | 2 | 3  (see below)
contact: intrusive        # passive | active | intrusive  (see below)
type: cli                 # cli | web | gui | api | library
cost: free                # free | freemium | paid
platforms: [linux, macos] # any of: linux | macos | windows | web
url: https://github.com/Dionach/CMSmap
categories: [web-exploration, cms-scanners]   # [top-dir, sub-dir] without the numeric prefix
tags: [wordpress, joomla, drupal]
status: unverified        # active | stale | broken | archived | unverified
status_checked: 2026-08-26
```

`categories` must be `[top, sub]` matching the directory the file lives in,
with the numeric prefix stripped: a file in `04-web-exploration/cms-scanners/`
uses `categories: [web-exploration, cms-scanners]`. The build script relies on
this.

### Tier — how good and how broad

| Tier | Meaning |
|---|---|
| `1` | Daily driver. Broad coverage, actively maintained, worth mastering. There are only about twelve of these total. Do not add a tier 1 lightly. |
| `2` | Specialist. Best-in-class at one job. Reach for it deliberately. |
| `3` | Situational or legacy. Superseded, broken, or niche. Keep it, but the file must say **why** it is tier 3 and what replaced it. |

### Contact — how much it touches the target

| Level | Meaning |
|---|---|
| `passive` | Never touches the target. Archives, CT logs, registries, third-party APIs. |
| `active` | Touches the target normally: DNS query, single HTTP request, banner grab. |
| `intrusive` | Scanning, fuzzing, brute forcing. Requires written authorisation. See [LEGAL.md](LEGAL.md). |

When a tool spans levels, pick the level of its **primary in-scope use** here
and explain the boundary in Gotchas. Port scanners and content brute-forcers
are `intrusive` even in light configurations.

### Status

Default to `status: unverified`. Only use `active` if you have a concrete,
recent reason (you ran it, or checked its repo activity). Use `broken`,
`archived`, or `stale` when you know the tool is degraded, and say so in
Gotchas. Always set `status_checked` to the date you last looked.

## File format

- One markdown file per tool, kebab-case filename matching the `slug`, in the
  **deepest** matching subdirectory.
- Follow the section order in the template: What question / When to reach for it
  / Install / Usage / Output / Gotchas / Alternatives.
- Keep it under ~80 lines. If a tool needs more, write a cheatsheet in
  [`99-resources/cheatsheets/`](99-resources/cheatsheets/) and link to it.
- No emoji in headings. No badge walls. Plain, dense, scannable markdown.
- `Alternatives` links to sibling tool files by relative path.

## Scope limits

- **No exploit code, payloads, or credential-attack tooling.** This is a
  discovery and attribution reference. Describe brute-force and exploitation
  features as out of scope; do not document them.
- **No vendored third-party material.** Do not copy course slides, lecture
  PDFs, or wordlist files into the repo. Link to the source instead.
- Write every description fresh.

## Before you open a PR

1. Run `python3 scripts/build-index.py` and commit the regenerated `INDEX.md`
   and category README tables. CI fails if `INDEX.md` is out of date.
2. Run `python3 scripts/check-links.py --timeout 10` and fix or mark any dead
   `url`.
3. Confirm your frontmatter parses (the build script will complain if not).

CI runs both scripts on every PR. See
[`.github/workflows/validate.yml`](.github/workflows/validate.yml).
