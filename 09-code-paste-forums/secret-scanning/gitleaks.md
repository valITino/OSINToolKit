---
name: Gitleaks
slug: gitleaks
tier: 2
contact: passive
type: cli
cost: free
platforms: [linux, macos, windows]
url: https://github.com/gitleaks/gitleaks
categories: [code-paste-forums, secret-scanning]
tags: [secrets, regex, ci, git-history]
status: unverified
status_checked: 2026-08-26
---

# Gitleaks

## What question does it answer?
Does this repository or directory contain anything that matches a known secret
pattern - quickly, and in a form I can wire into a pipeline?

## When to reach for it
When speed and automation matter more than verification. Gitleaks is a fast regex and
entropy scanner with a configurable ruleset, designed to run as a pre-commit hook or
CI gate. Reach for [TruffleHog](trufflehog.md) when you need to know which findings
are *live*; reach for Gitleaks when you need to scan a lot of code quickly or to stop
secrets being committed in the first place.

## Install
```bash
# Release binaries on GitHub; also packaged in Homebrew and on Kali.
gitleaks version
```

## Usage
```bash
gitleaks detect --source . --report-path leaks.json    # scan a repo including history
gitleaks detect --no-git --source ./files               # scan a plain directory
gitleaks protect --staged                                # pre-commit: block secrets before they land
```

## Output
JSON (or SARIF/CSV) findings with the rule that matched, the file and line, the commit
and author, and the matched string. The commit author is the pivot into
[git-history](../git-history/README.md).

## Gotchas
- **No verification** - every finding is a pattern match, so expect false positives
  from test fixtures, example keys, and high-entropy strings that are not secrets.
  Triage manually.
- Entropy rules are noisy on minified assets and lockfiles; use `.gitleaksignore` or a
  custom config to keep signal up.
- Custom or unusual credential formats need custom rules - the default set covers
  common providers, not everything internal.
- As with any secret finding: **never test the credential**. Report it.

## Alternatives
- [TruffleHog](trufflehog.md) - verifies which secrets are live
- [GitHub code search](../code-search/github-code-search.md) - no clone required
