# 09 - Code, Paste Sites, Forums

Where secrets and identities leak in plain text: source repositories, commit history, paste sites, and forum/wiki edit trails.

## Subcategories

- [code-search/](code-search/) - GitHub code search - cross-repo, current
- [secret-scanning/](secret-scanning/) - TruffleHog, Gitleaks - secrets in repos
- [git-history/](git-history/) - Author names, emails, timestamps from commits
- [paste-sites/](paste-sites/) - pastebin and paste-dump search
- [forums-wikis/](forums-wikis/) - Forum and wiki history

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [GitHub code search](code-search/github-code-search.md) | Does this organisation's name, domain, internal hostname, or API key appear anywhere | 2 | passive |
| [Gitleaks](secret-scanning/gitleaks.md) | Does this repository or directory contain anything that matches a known secret | 2 | passive |
| [Pastebin](paste-sites/pastebin.md) | Has data relating to my target - credentials, a customer list, internal | 2 | passive |
| [TruffleHog](secret-scanning/trufflehog.md) | Does this repository - across its **entire history**, not just its current files - | 2 | passive |
| [Gitrob](secret-scanning/gitrob.md) | Which files in an organisation's public repositories look sensitive - keys, | 3 | passive |
| [SearchCode](code-search/searchcode.md) | Does this string appear in public source code across several forges - not just | 3 | passive |
<!-- END:TOOLS -->
