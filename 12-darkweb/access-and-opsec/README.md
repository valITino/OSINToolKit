# Access and OPSEC

Reaching a hidden service is easy. Reaching one without carrying your identity,
your employer's network, or last week's browser fingerprint along with you takes
deliberate setup. Do this part first; there is no retrofit.

## What each layer actually protects

| Layer | Protects against | Does not protect against |
|---|---|---|
| Tor Browser | The service learning your IP; your ISP learning the destination | Anything you type into the site; a compromised host OS |
| torsocks | A CLI tool leaking your IP through its own sockets | DNS or UDP the tool does outside the wrapper |
| Amnesic OS (Tails) | Anything persisting on disk after the session | Correlation of what you do inside one session |
| Isolated gateway (Whonix) | An application-level compromise learning your real IP | Your own logins, timing, and writing style |

The layers are cumulative and none of them fixes an operational mistake. Logging
into anything of yours over Tor undoes every layer at once.

## Rules that matter more than the tooling

- **Separate machine, separate everything.** A snapshot-and-revert VM is the
  baseline; an amnesic OS on separate hardware is better for sensitive work.
- **Never authenticate.** Not to the target, not to your own accounts in the
  same browser session, not "just to read the forum".
- **Do not maximise the browser window, do not install add-ons.** Both make you
  more distinguishable, which is the opposite of the point.
- **Assume the exit is hostile for clearweb traffic.** Onion-to-onion traffic
  never leaves the network, but browsing the clearweb over Tor passes through
  an exit that can see and modify anything not TLS-protected.
- **Check the rules that apply to you.** Some employers and some jurisdictions
  treat installing Tor on a managed device as a policy or legal problem in its
  own right.

## Tools here

<!-- BEGIN:TOOLS -->
_No tool files here yet._
<!-- END:TOOLS -->

## Related

- [../../00-methodology/opsec/README.md](../../00-methodology/opsec/README.md) - the general OPSEC discipline
- [../../00-methodology/opsec/proxychains.md](../../00-methodology/opsec/proxychains.md) - the other way to push a tool through a proxy
- [../../02-network-and-ip/reputation/exonerator.md](../../02-network-and-ip/reputation/exonerator.md) - was a given IP a Tor exit at a given time
