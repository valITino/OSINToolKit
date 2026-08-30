---
name: Tor Browser
slug: tor-browser
tier: 2
contact: active
type: gui
cost: free
platforms: [linux, macos, windows]
url: https://www.torproject.org/
categories: [darkweb, access-and-opsec]
tags: [tor, onion, browser, fingerprinting, anonymity]
status: active
status_checked: 2026-08-29
---

# Tor Browser

## What question does it answer?
I have a .onion address, or a clearweb page I do not want to hand my real IP.
What do I open it in so the service sees a Tor exit and a fingerprint shared
with every other Tor user, rather than one that is uniquely mine?

## When to reach for it
Any first look at a hidden service, and any clearweb page where simply being
seen is the risk; it is the only thing in a normal toolkit that resolves .onion
addresses out of the box. Skip it when a clearweb source already holds the
answer - an indexer or a leak aggregator gets the same content without the
operator seeing you. It protects the browser's traffic, not the machine
underneath: for that, boot [Tails](tails.md) or [Whonix](whonix.md).

## Install
```bash
# No official apt/dnf/brew package. torbrowser-launcher in Debian and Kali is a
# third-party wrapper around this tarball, not a Tor Project build.
gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org
gpg --output ./tor.keyring --export EF6E286DDA85EA2A4BA7DE684E2C6E8793298290
tar -xf tor-browser-linux-x86_64-15.0.20.tar.xz    # stable, built 2026-08-17
# Windows: the verified .exe. macOS: the verified .dmg. Android: F-Droid or
# Google Play. There is no iOS build - Onion Browser is a different project.
```

## Usage
```bash
TB=tor-browser-linux-x86_64-15.0.20.tar.xz   # substitute your actual version
gpgv --keyring ./tor.keyring "$TB.asc" "$TB" # want: Good signature from Tor Browser Devs
cd tor-browser && ./start-tor-browser.desktop  # first run: direct or a bridge
```

## Output
A Firefox-ESR-derived window that bootstraps a circuit before anything loads.
The shield icon sets the security level: Standard (everything enabled), Safer
(JavaScript off on non-HTTPS sites), Safest (JavaScript off everywhere). The
menu carries New Identity, killing the session and all circuits, and New Tor
Circuit for this Site, re-routing one tab. The URL bar's circuit display names
the guard, middle and exit relays - the exit is what the target logged.

## Gotchas
- **Illegal material appears unbidden, and a rendered page is already a cached
  copy on your disk.** Possession is an offence in most jurisdictions regardless
  of intent, and reporting duties can attach the moment you see it. Agree the
  stop-and-report procedure first - [../../LEGAL.md](../../LEGAL.md).
- **Loading an onion page is active contact.** The service logs your request and
  its timing. Record why you made each visit.
- **Do not customise it.** Only the bundled NoScript is tested; the Tor
  Project's position is that other add-ons harm privacy, and your usual OSINT
  extensions make your fingerprint unique. Letterboxing pads the viewport to
  rounded values to hide your screen size - do not drag the window to fit.
- Safest breaks most onion forums, which lean on JavaScript; dropping to
  Standard and forgetting restores the JS attack surface on a hostile site.
- Exit nodes are publicly enumerated, so on clearweb targets you are not covert:
  the site may block you or serve different content. That difference is a
  finding, not the real page. The verification docs drift too - their examples
  still say 13.0.1, and old tb-manual.torproject.org links have dead anchors.
- It anonymises the transport, not your behaviour. One login tied to you, or a
  persona reused across a New Identity boundary, links the sessions anyway.

## Alternatives
- [Tails](tails.md) - the same browser on an amnesic OS, no disk trace
- [Whonix](whonix.md) - when the leak you fear is a tool, not the browser
- [torsocks](torsocks.md) - push a CLI tool through Tor instead of clicking
