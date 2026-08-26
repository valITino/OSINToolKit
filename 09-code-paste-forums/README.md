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
| [GitHub code search](code-search/github-code-search.md) | Does this organisation's name, domain, internal hostname, or API key appear anywhere in public source code? | 2 | passive |
| [Gitleaks](secret-scanning/gitleaks.md) | Does this repository or directory contain anything that matches a known secret pattern - quickly, and in a form I can wire into a... | 2 | passive |
| [paaster](paste-sites/paaster.md) | I have a paaster link, or I have the device of someone who used paaster. What can I still recover? | 2 | passive |
| [Pastebin](paste-sites/pastebin.md) | Has data relating to my target - credentials, a customer list, internal configuration - been posted publicly, and when did it... | 2 | passive |
| [PrivateBin](paste-sites/privatebin.md) | I found a PrivateBin link in a chat log, an email, or another paste. Can I read it - and why can I not search for others like it? | 2 | passive |
| [TruffleHog](secret-scanning/trufflehog.md) | Does this repository - across its **entire history**, not just its current files - contain credentials, and are any of them still... | 2 | passive |
| [Gitrob](secret-scanning/gitrob.md) | Which files in an organisation's public repositories look sensitive - keys, credentials, database dumps, configuration? | 3 | passive |
| [SearchCode](code-search/searchcode.md) | Does this string appear in public source code across several forges - not just GitHub, but Bitbucket, GitLab, SourceForge and... | 3 | passive |
<!-- END:TOOLS -->
