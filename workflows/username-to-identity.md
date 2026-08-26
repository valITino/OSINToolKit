# Playbook: username to identity

**You have:** a username, handle, or alias.
**You want:** the accounts behind it, and whether they belong to one person.

This is the playbook with the most legal and ethical weight in the repo. You are
processing personal data about a real human being, and the central failure mode
is **confident misidentification**. Two people using the same handle is common;
concluding they are one person is a serious harm. Corroborate everything.

---

## 1. Spread the handle

- [Sherlock](../08-people-and-identity/username-enum/sherlock.md) - fast, clean
- [Maigret](../08-people-and-identity/username-enum/maigret.md) - more sites, extracts profile detail

```bash
sherlock someusername
maigret someusername --html
```

**Verify every hit by hand.** Both tools produce false positives: sites that
return 200 for any profile path, or serve a custom error page, register as hits.
An unverified list is not a finding.

This is **active** - hundreds of requests from your IP. Consider a VPN or proxy
first ([OPSEC](../00-methodology/opsec/README.md)); a burst will also trigger
rate limiting and CAPTCHAs.

## 2. Separate the real accounts from the coincidences

You now have candidate profiles. Before treating them as one person, look for
links that a coincidence cannot explain:

- **The same avatar.** Reverse image the profile picture -
  [Yandex](../08-people-and-identity/reverse-image/yandex-images.md) for similarity,
  [TinEye](../08-people-and-identity/reverse-image/tineye.md) for exact reuse. A
  shared, non-stock avatar across platforms is strong.
- **Cross-links the subject made themselves.** A bio linking to another profile is
  the subject asserting the connection - the best evidence you will get.
- **Writing style, timezone of activity, recurring topics.** Weak individually,
  meaningful together.
- **Account creation dates.** A handle registered years apart on two platforms
  weakens the single-person hypothesis.

Record which evidence supports which link. "Same username" alone is the weakest
possible connection.

## 3. Pivot to email

If a profile exposes an address, or you can infer the pattern:

- [holehe](../08-people-and-identity/email-osint/holehe.md) - which services it is registered with
- [Have I Been Pwned](../08-people-and-identity/email-osint/hibp.md) - which breaches it appears in

```bash
holehe target@example.com --only-used
```

HIBP is doubly useful: it confirms the address is real and in circulation, and
**each breach evidences an account on that platform**, often years back. That
builds a timeline the live profiles do not show.

Read holehe's rate-limited results as **unknown**, not negative.

## 4. Masked hints from recovery flows

- [Password reset clues](../08-people-and-identity/password-reset-clues/README.md)

Recovery flows show masked hints - `j•••••@g•••l.com`, a phone ending `47`. The
mask often reveals the provider, the **length**, and the first/last characters.
Combining masks across services narrows an identity that no single service would
give up.

Boundary: **do not actually attempt a reset**, and do not trigger notifications to
the account holder. Read the hint, stop there. See [../LEGAL.md](../LEGAL.md).

## 5. Code and paste sites

Developers leak identity through metadata more than through profiles.

- [GitHub code search](../09-code-paste-forums/code-search/github-code-search.md)
- [git history](../09-code-paste-forums/git-history/README.md)

```bash
git log --format='%an <%ae>  %cI' | sort -u
```

Commit metadata is the payoff: a personal email committed from an unconfigured
laptop, and a **timezone offset** in every timestamp that indicates where the
person works and when. `root@localhost.localdomain` suggests commits made as root
on a hastily configured box rather than a developer workstation.

Also check [paste sites](../09-code-paste-forums/paste-sites/README.md) and
[forums and wikis](../09-code-paste-forums/forums-wikis/README.md) - forum
registration dates and wiki edit histories (which expose the editing IP for
anonymous edits) both add hard timestamps.

## 6. Consolidate and test the opposite case

- [Maltego](../01-orchestrators/modular-frameworks/maltego.md) - build the link graph
- [SpiderFoot](../01-orchestrators/recursive-scanners/spiderfoot.md) - automated correlation

Before you write anything down as a conclusion, argue against it:

- Which links rest **only** on a shared username?
- Is any "corroborating" detail self-reported by the subject, and therefore a
  claim rather than a fact?
- Is there a plausible second person who fits the same evidence?
- What would falsify the identification - and did you look for it?

If the answer to the last question is no, you are not finished.

---

## Legal and ethical boundary

Read [../LEGAL.md](../LEGAL.md) before you start, not after.

- This is **personal data**. Collecting, storing, and combining it is regulated
  regardless of how public each individual source is. Have a lawful basis. GDPR
  applies to EU subjects wherever you are.
- **Automated face recognition against a real person is a further step** into
  special-category biometric data with a much higher bar. See
  [EagleEye](../08-people-and-identity/reverse-image/eagleeye.md) for why this repo
  does not recommend it.
- Never contact, test credentials against, or interact with a subject's accounts.
- Document your reasoning, not just your findings
  ([documentation](../00-methodology/documentation/README.md)). If this is ever
  challenged, the chain of inference is what gets examined.
