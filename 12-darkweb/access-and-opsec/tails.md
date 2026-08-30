---
name: Tails
slug: tails
tier: 2
contact: active
type: gui
cost: free
platforms: [linux, macos, windows]
url: https://tails.net/
categories: [darkweb, access-and-opsec]
tags: [tor, amnesic, live-usb, opsec, anonymity]
status: active
status_checked: 2026-08-29
---

# Tails

## What question does it answer?
I have an onion address to open from a machine I do not fully trust, and this
session must leave nothing behind on its disk when I am finished. What do I boot
instead of the installed operating system?

## When to reach for it
When the host is borrowed, shared or suspect and "no residue" matters more than
convenience: a live USB that routes everything through Tor and wipes RAM on
shutdown. It is the wrong tool when you need the same tooling and state across
many sessions - [Whonix](whonix.md) gives a persistent workstation behind the
same Tor enforcement. For one look from a machine you control, [Tor
Browser](tor-browser.md) alone is enough.

## Install
```bash
# Guided installer at https://tails.net/install/ (Windows, macOS, Linux), or:
wget --continue https://download.tails.net/tails/stable/tails-amd64-7.11/tails-amd64-7.11.img
wget https://tails.net/tails-signing.key && gpg --import < tails-signing.key
sudo dd if=tails-amd64-7.11.img of=/dev/sdX bs=16M oflag=direct status=progress
# Floor: 8 GB USB stick, 3 GB RAM, 64-bit x86-64. Version 7.11 is 2026-08-19.
```

## Usage
```bash
KEY=A490D0F4D311A4153E2BB7CADBB802B258ACD84F
gpg --keyid-format 0xlong --check-sigs $KEY  # who certified it? the trust step
gpg --lsign-key $KEY                         # then sign it locally
TZ=UTC gpg --no-options --verify tails-amd64-7.11.img.sig tails-amd64-7.11.img
```

## Output
Boots to a Welcome Screen (language, keyboard, optional admin password, MAC
spoofing, unsafe browser), then a GNOME desktop. The Tor Connection assistant
runs first and nothing reaches the network until a circuit is up. It ships Tor
Browser, KeePassXC, Metadata Cleaner, OnionShare and the Persistent Storage
tool. On shutdown RAM is wiped and the host disk untouched.

## Gotchas
- **Illegal material can appear unbidden on a hidden service, and downloading it
  is an offence in most jurisdictions regardless of intent.** Amnesia is not a
  defence and does not discharge your evidence-handling or reporting duties -
  agree the procedure first, see [../../LEGAL.md](../../LEGAL.md).
- **It hides residue, not that you use it.** Tails warns it is obvious you are
  using Tor and probably Tails; on a small network that alone identifies you.
- **Amnesia cuts both ways.** Everything collected dies at shutdown. Plan the
  export and hashing first; clean exports with Metadata Cleaner before sharing.
- Persistent Storage defeats the amnesia deliberately and is not deniable:
  anyone holding the stick can see it exists, and you can be forced or tricked
  into giving up the passphrase. Tails advises five to seven random words.
- Hardware limits bite in the field: x86-64 only since 3.0, Apple Silicon Macs,
  phones, tablets and Raspberry Pi unsupported, Nvidia and Radeon flaky.
- No OS protects against firmware attacks or hardware alterations such as a
  keylogger, and installing from a compromised computer can corrupt the stick.
- One session, one identity: mixing a persona and your own accounts in a single
  boot correlates them through the shared circuit and browser state. End-to-end
  timing correlation is out of scope for Tor entirely.
- Version 7.8 removed Thunderbird, so an email-header step that assumed a mail
  client present in the bundle no longer has one.

## Alternatives
- [Whonix](whonix.md) - the same Tor enforcement, but persistent and scriptable
- [Tor Browser](tor-browser.md) - when the host is already yours and trusted
- [OPSEC methodology](../../00-methodology/opsec/README.md) - wider discipline
