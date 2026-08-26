---
name: paaster
slug: paaster
tier: 2
contact: passive
type: web
cost: free
platforms: [web, linux]
url: https://paaster.io/
categories: [code-paste-forums, paste-sites]
tags: [paste, encryption, libsodium, indexeddb]
status: active
status_checked: 2026-08-26
---

# paaster

## What question does it answer?
I have a paaster link, or I have the device of someone who used paaster. What can I
still recover?

## When to reach for it
Know this one for what it leaves behind on the **creator's machine**. Like
[PrivateBin](privatebin.md), paaster encrypts in the browser and carries the key in the
URL fragment, so the server holds nothing readable. Unlike PrivateBin, it keeps a paste
history - and it does that by storing both the client secret and a server secret in the
browser's **IndexedDB**.

That is the investigative opening. On a seized or consented device, the browser profile
may still hold the keys and identifiers for pastes the subject created, including ones
whose URLs you never had. It is a device-forensics lead, not a network one.

## Install
```bash
# Nothing to install to read a paste. Self-hosting and the CLI:
docker pull wardpearce/paaster        # https://docs.paaster.io
```

## Usage
```text
https://paaster.io/<id>#KEYMATERIAL   # the fragment after # is the decryption key
https://paaster.io/                    # "paste history" lists what this browser created
```

## Output
The decrypted paste with syntax highlighting, plus any attached file. The history view
lists pastes created in that browser profile - which is the part worth capturing.

## Gotchas
- **"Delete after view" is supported**, so opening an unknown link may consume it. Decide
  who opens it and preserve the result immediately; there is no second attempt.
- **A URL cut at the `#` is worthless.** Fragments are never sent to the server, so they
  are absent from server logs, proxy logs, and referrer headers - which is also why the
  operator genuinely cannot decrypt anything.
- **No search and no public feed.** You cannot monitor paaster; links only ever come
  from somewhere else.
- IndexedDB is per browser profile. It does not sync, and clearing site data destroys
  it. Image the profile before browsing on the device.
- Encryption is libsodium XChaCha20-Poly1305 and is not optional, so there is no
  misconfigured-instance shortcut to plaintext.
- On an instance you do not host, zero-knowledge is a claim about the JavaScript you
  were served. The project says so itself.

## Alternatives
- [PrivateBin](privatebin.md) - the same model, far more widely deployed
- [Pastebin](pastebin.md) - searchable and monitorable; start there
- [../../07-documents-metadata/README.md](../../07-documents-metadata/README.md) - when the artifact is a file rather than a link
