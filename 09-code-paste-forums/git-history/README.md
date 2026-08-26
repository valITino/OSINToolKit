# Git history

A git repository is an identity leak that ships with the code. Every commit
carries the author's configured name, email, and a timestamp - and history is
append-only, so a name someone later "removed" is usually still in the log.

## Pull the identities

```bash
git log --format='%an <%ae>  %cI' | sort -u        # unique authors, emails, ISO timestamps
git log --all --format='%ae' | sort | uniq -c | sort -rn   # every email across all branches
git shortlog -sane --all                            # contributors with commit counts
```

Read the results for:

- **Real names and personal emails** committed from a laptop that was not
  configured for the org - people commit as `jane@personal-gmail` more often than
  you would think.
- **Timezones** in the commit timestamp (`%cI` keeps the offset), which hint at
  location and working hours.
- **`root@localhost.localdomain`** or similar: an unconfigured git running as root,
  often a sign of commits made on a hastily set-up server or container rather than a
  developer workstation.

## Exposed .git on web servers

If a live site serves its `.git/` directory, the whole history - including secrets
and removed files - can be reconstructed. Check for `/.git/HEAD` returning a valid
ref. This is passive discovery of a misconfiguration; extracting and dumping the
repo against a target you do not own is not - get authorisation.

## Then scan it

Author extraction tells you *who*; pair it with secret scanning for *what leaked*:

- [TruffleHog](../secret-scanning/trufflehog.md) - secrets with live verification, across full history
- [Gitleaks](../secret-scanning/gitleaks.md) - fast regex secret scan

## Related

- [code-search](../code-search/README.md) - find the repos in the first place
- [../../00-methodology/documentation/README.md](../../00-methodology/documentation/README.md)
