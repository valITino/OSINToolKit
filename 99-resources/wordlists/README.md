# Wordlists

Directory-discovery, subdomain, and parameter fuzzing all need wordlists. This
repo does **not** vendor them - they are large, they change, and copying them here
would just make a stale fork of work other people maintain. Point your tools at
the real thing.

## Get SecLists

[SecLists](https://github.com/danielmiessler/SecLists) is the standard collection:
discovery paths, subdomains, usernames, common parameters, and more.

```bash
# Kali ships it:
ls /usr/share/seclists

# Elsewhere:
git clone --depth 1 https://github.com/danielmiessler/SecLists.git
```

## What each kind is for

| Wordlist family (in SecLists) | Used by | Answers |
|---|---|---|
| `Discovery/Web-Content/` (e.g. `directory-list-*.txt`, `raft-*`, `common.txt`) | [feroxbuster](../../04-web-exploration/content-discovery/feroxbuster.md), [ffuf](../../04-web-exploration/content-discovery/ffuf.md), [gobuster](../../04-web-exploration/content-discovery/gobuster.md) | What unlinked paths and files exist |
| `Discovery/DNS/` (e.g. `subdomains-top1million-*.txt`) | [gobuster](../../04-web-exploration/content-discovery/gobuster.md) (dns mode), [fierce](../../03-dns-and-subdomains/active-enum/fierce.md), Amass brute | What subdomains resolve |
| `Fuzzing/` | [ffuf](../../04-web-exploration/content-discovery/ffuf.md) | Parameter and value fuzzing |

## Which one to pick

- Start small (`common.txt`, `raft-small-*`) to get signal fast; escalate to
  `directory-list-2.3-medium.txt` only when you need depth. Bigger lists mean more
  requests, more noise, more chance of tripping rate limits or IDS.
- Match the list to the stack: a WordPress target wants a CMS-aware list, not a
  generic one.
- Prefer passive discovery first ([crt.sh](../../05-certificates-tls/ct-log-search/crt-sh.md),
  [subfinder](../../03-dns-and-subdomains/passive-enum/subfinder.md),
  [Wayback CDX](../../06-history-and-archives/web-archive/wayback-cdx-api.md)) before
  brute forcing. It finds real names the target actually used, at zero contact.

## Scope note

Content and subdomain brute forcing is **intrusive**. Wordlist-driven discovery
against a target you do not own needs written authorisation. See
[../../LEGAL.md](../../LEGAL.md). Password-cracking wordlists are deliberately out
of scope for this repo.
