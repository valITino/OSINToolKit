---
name: PrivateBin
slug: privatebin
tier: 2
contact: passive
type: web
cost: free
platforms: [web, linux]
url: https://privatebin.info/
categories: [code-paste-forums, paste-sites]
tags: [paste, encryption, zero-knowledge, self-hosted]
status: active
status_checked: 2026-08-26
---

# PrivateBin

## What question does it answer?
I found a PrivateBin link in a chat log, an email, or another paste. Can I read it -
and why can I not search for others like it?

## When to reach for it
Understand it, mostly. PrivateBin turns up constantly in leak and threat-actor
tradecraft precisely because it defeats the monitoring that works on
[Pastebin](pastebin.md). It is zero-knowledge: content is encrypted in the browser with
256-bit AES and **the key lives in the URL fragment, after the `#`**. Browsers never
transmit a fragment, so the operator cannot decrypt the paste and neither can anyone
reading server logs.

The practical consequences for an investigation are the whole point. There is no
search, no index, and no crawlable listing - only whoever holds the complete URL can
read it. And instances are independent: it is self-hosted software, so a link on one
instance says nothing about any other.

## Install
```bash
# Nothing to install to read a paste. To run your own instance, PrivateBin is PHP:
# https://github.com/PrivateBin/PrivateBin/blob/master/doc/Installation.md
```

## Usage
```text
https://privatebin.info/directory/     # directory of public instances
https://<instance>/?abc123#KEYMATERIAL  # the fragment after # IS the decryption key
```

## Output
The decrypted paste, in your browser. Optionally a discussion thread, and an attached
file if the poster added one.

## Gotchas
- **Opening a "burn after reading" paste destroys it.** That is a supported expiry
  option, and one visit consumes it for everyone. Before clicking an unknown PrivateBin
  link, assume it may be single-use: capture the full URL, decide who opens it, and
  record the result immediately - there is no second attempt.
- **A URL truncated at the `#` is useless.** Many logs, referrer headers, and chat
  clients strip fragments. Without the key material you have proof a paste existed and
  nothing more.
- **You cannot monitor PrivateBin the way you monitor Pastebin.** No API to scrape, no
  public feed, no search. Discovery only ever comes from finding the link somewhere else.
- Pastes may additionally be password-protected on top of the fragment key.
- Expiry is real: pastes vanish on schedule. Preserve content the moment you read it -
  see [../../00-methodology/documentation/README.md](../../00-methodology/documentation/README.md).
- You are trusting the instance operator not to have modified the JavaScript. On a
  hostile instance, zero-knowledge is a claim, not a guarantee.

## Alternatives
- [Pastebin](pastebin.md) - searchable and monitorable; where things actually surface
- [paaster](paaster.md) - the same encrypted-paste model, different implementation
- [GitHub code search](../code-search/github-code-search.md) - for content that was committed rather than pasted
