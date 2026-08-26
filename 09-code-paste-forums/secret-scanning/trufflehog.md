---
name: TruffleHog
slug: trufflehog
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/trufflesecurity/trufflehog
categories: [code-paste-forums, secret-scanning]
tags: [secrets, credentials, git-history, verification]
status: unverified
status_checked: 2026-08-26
---

# TruffleHog

## What question does it answer?
Does this repository - across its **entire history**, not just its current files -
contain credentials, and are any of them still live?

## When to reach for it
The tool that replaced [Gitrob](gitrob.md), which is archived. Two things make it the
default: it walks full git history, so it finds secrets that were committed and later
"removed" (they remain in the objects forever), and it **verifies** findings by
testing them against the relevant provider's API. Verification is what turns hundreds
of regex hits into the handful that actually matter.

## Install
```bash
# Release binaries on GitHub, or:
docker run --rm trufflesecurity/trufflehog:latest github --repo https://github.com/example/repo
```

## Usage
```bash
trufflehog git https://github.com/example/repo             # full history scan
trufflehog github --org=example-inc --only-verified         # whole org, confirmed live secrets only
trufflehog filesystem ./downloaded-repo --only-verified
```

## Output
Per-finding: the detector type (AWS, Slack, Stripe...), the raw secret, the commit
hash, the file, and the author - plus a verified/unverified flag. Start with
`--only-verified`; the commit author is your pivot into
[git-history](../git-history/README.md).

## Gotchas
- **Verification means TruffleHog authenticates to the third-party service** to test
  the key. That is contact with the provider (not with your target) and it may appear
  in the key owner's audit log. Understand the implication before scanning someone
  else's repository.
- **Never use a discovered credential for anything else.** Verification is the
  boundary; using it is unauthorised access. Report it.
- Unverified findings are mostly noise - test data, examples, expired keys.
- Scanning a large organisation takes a long time and is rate-limited by the forge.

## Alternatives
- [Gitleaks](gitleaks.md) - faster, no verification, better for CI
- [GitHub code search](../code-search/github-code-search.md) - current files, no clone needed
- [Gitrob](gitrob.md) - archived predecessor, tier 3
