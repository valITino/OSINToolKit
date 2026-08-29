# Playbook: dark web exposure monitoring

**You have:** an organisation - yours, a client's, or a supplier's.
**You want:** to know whether its data is being published or sold, early enough
to act, and with evidence somebody can act on.

This is a monitoring routine, not a one-off search. It is also the playbook
where the wrong instinct causes the most damage: the moment an organisation
appears on a leak site, somebody always wants to download the dump "to check
what is in it". That decision is not an analyst's to make, and it is a
processing decision with legal consequences either way.

---

## 1. Decide what you are watching for

Write the selectors down before you search. Vague monitoring produces vague
alerts.

- Domains and brand names, including the misspellings and the old trading names
- Executive and role-based email addresses, and the mail domain itself
- Key suppliers and outsourced providers - most organisations first learn of a
  breach because a supplier is named
- Product names and internal project names that leak in documents

## 2. Check the leak-site trackers

Weekly at minimum, and after any incident in your sector.

- [RansomLook](../12-darkweb/leak-monitoring/ransomlook.md) and
  [Ransomware.live](../12-darkweb/leak-monitoring/ransomware-live.md) - mirrored
  victim posts, searchable from the clearweb
- [ransomwatch](../12-darkweb/leak-monitoring/ransomwatch.md) - the self-hosted
  version, when you want your own copy and your own history

Use at least two. Each crawls a different subset of sites and each misses posts
during takedowns and rebrands. See
[leak monitoring](../12-darkweb/leak-monitoring/README.md).

## 3. Check the credential and paste side

Leak sites are only one channel. The same exposure usually shows up as:

- Breached credentials - [Have I Been Pwned](../08-people-and-identity/email-osint/hibp.md),
  and [holehe](../08-people-and-identity/email-osint/holehe.md) for where an
  address is registered
- Pastes and dumps on the clearweb -
  [paste sites](../09-code-paste-forums/paste-sites/)
- Secrets in code that never needed a breach at all -
  [code search](../09-code-paste-forums/code-search/) and
  [secret scanning](../09-code-paste-forums/secret-scanning/)
- Aggregated leak search -
  [Intelligence X](../12-darkweb/onion-discovery/intelligence-x.md)

## 4. Verify the claim before anybody panics

A leak-site post is a criminal's marketing copy. Before it becomes an incident
report, establish:

- **Is it us?** Name collisions are common, as are subsidiaries and franchises
  with similar names.
- **Is it us, or our supplier?** A third-party breach naming you is a different
  incident with a different owner.
- **Is it new?** Groups re-post old victims, rebrand, and inherit each other's
  victim lists. Check the dates and whether the same claim appeared under
  another group's name.
- **What is actually claimed?** File counts, data types, a sample screenshot,
  and a countdown are the facts you have. The dump is not evidence you can
  safely acquire.

## 5. Preserve what you can safely hold

- Screenshot and hash the post, with a timestamp and the URL you saw it at.
- Record the group, the claimed volume, the deadline, and any sample metadata.
- Store it where legal and incident response can reach it -
  [documentation](../00-methodology/documentation/README.md).

Do **not** download the corpus. It is stolen personal data, frequently criminal
property, and downloading it creates your own processing problem. See the dark
web section of [../LEGAL.md](../LEGAL.md).

## 6. Escalate as an incident, not as a finding

If your organisation is named, this stops being OSINT. Hand it to incident
response and legal with the evidence from step 5, and let them decide about
regulator and customer notification. The
[frameworks](../00-methodology/frameworks/README.md) note covers where this sits
in the response process.

## 7. Set the cadence, and keep the history

- Weekly checks of the trackers; daily during an active incident in your sector.
- Keep your own historical copy - trackers rewrite and lose posts, and "when did
  they first claim it" becomes the important question later.
- Re-scope the selectors after every acquisition, rebrand, or new supplier.

---

## Boundaries

- **No accounts, no negotiation, no purchases.** Registering on a forum or
  contacting a group is not monitoring; it is engagement, with legal and
  sanctions implications that are not an analyst's call.
- **No buying "your own" data back** to verify a claim. Beyond the legal
  exposure, it funds the operation and proves nothing.
- **Everything you collect about named individuals is personal data**, including
  the executives whose addresses appear in a dump summary. Have a lawful basis
  and keep it in the same place as the rest of the incident record.
