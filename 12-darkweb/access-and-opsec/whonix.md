---
name: Whonix
slug: whonix
tier: 2
contact: active
type: gui
cost: free
platforms: [linux, macos, windows]
url: https://www.whonix.org/
categories: [darkweb, access-and-opsec]
tags: [tor, virtual-machine, gateway, isolation, opsec]
status: active
status_checked: 2026-08-29
---

# Whonix

## What question does it answer?
I have a whole toolkit to point at an onion service, not just a browser, and one
careless tool or one hostile page must not be able to learn my real IP. What do
I run the tools inside?

## When to reach for it
When the risk is a tool or a target, not a website: a crawler that resolves its
own DNS, a sample you want to detonate, a script whose proxy support you do not
trust. Two VMs enforce the boundary structurally, so a tool that silently
ignores `--proxy` still cannot reach the network in the clear. It grants no
authorisation - it changes where your traffic exits, nothing else.

## Install
```bash
# From https://www.whonix.org/wiki/Download - VirtualBox: import the single
# Whonix-LXQt-18.2.1.9.Intel_AMD64.ova (2.6 GiB), which holds both VMs. KVM:
gpg --import derivative.asc   # fingerprint 916B 8D99 C38E AF5E 8ADC 7A2A 8D66 066A 2EEA CCDA
tar -xSvf Whonix*.libvirt.xz  # NOT unxz - the wiki is explicit about this
virsh -c qemu:///session define Whonix-Gateway*.xml
virsh -c qemu:///session define Whonix-Workstation*.xml
# Needs AMD-V or Intel VT-x, 10 GB disk. Recommended split: 2 GB host / 2 GB
# Gateway / 4 GB Workstation. Qubes-Whonix is the third path, for advanced users.
```

## Usage
```bash
gpg --verify Whonix-LXQt-18.2.1.9.Intel_AMD64.ova.asc  # stop on any mismatch
mv Whonix-Gateway*.qcow2 ~/.local/share/images/Whonix-Gateway.qcow2
mv Whonix-Workstation*.qcow2 ~/.local/share/images/Whonix-Workstation.qcow2
```

## Output
Two VMs, and the Gateway must start first - the Workstation has no route until
it is up. Whonix-Gateway runs the Tor process and is the only way out;
Whonix-Workstation runs your tools on an isolated internal network and never
learns the host's IP. The Gateway boots to a CLI unless given 768 MB RAM or
more, when LXQt starts; the editions are CLI and LXQt, no Xfce build in 18.x.
The project's claim: IP, DNS, UDP and ICMP leaks are impossible from it.

## Gotchas
- **Illegal material can appear unbidden on a hidden service, and downloading it
  is an offence in most jurisdictions regardless of intent.** Because Whonix
  persists, it is still on the VM disk tomorrow - settle your evidence-handling
  and reporting duties first, see [../../LEGAL.md](../../LEGAL.md).
- **It is not amnesic** - the common confusion with Tails. History, downloads
  and anything you detonated survive reboots; snapshot first, roll back after.
- **Your host is the security floor.** Running Whonix on a daily driver with
  your own accounts logged in gives far less than the architecture suggests.
- Only the Workstation is designed for anonymous activity. Treating the Gateway
  console as a workspace is outside the threat model.
- The architecture stops leaks, not self-deanonymisation: an identity-linked
  login inside the Workstation burns the persona, and it covers neither social
  engineering nor physical access.
- Production images are x86-64 only (ARM64 experimental), so Apple Silicon means
  emulation; VT-x/AMD-V is often off in BIOS and collides with Hyper-V/WSL2.
- Extracting with `unxz` instead of `tar` gives an image that looks like it
  works. Check the current version against download.whonix.org, not the wiki:
  github.com/Whonix/Whonix is a 404, and tooling is Whonix/derivative-maker.

## Alternatives
- [Tails](tails.md) - when the session must leave nothing behind at all
- [Tor Browser](tor-browser.md) - one page, one look, no VM to maintain
- [torsocks](torsocks.md) - a wrapper, not a boundary, when a VM is overkill
