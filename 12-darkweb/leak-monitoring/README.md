# Leak monitoring

Ransomware crews, extortion groups, and data brokers publish. That publishing is
the most reliably useful dark web source there is: it is timestamped, it names
victims, and several projects mirror it to the clearweb so you never have to
load the leak site yourself.

Everything here is passive. Somebody else's crawler took the risk.

## What these sources answer

- Is my organisation, or my supplier, named on a leak site - and when?
- What is the group claiming: volume, data types, a countdown, a price?
- Which group is active this quarter, and what does their posting cadence look
  like across the sector I care about?
- Is a claim recycled? Groups re-post old victims, and two "breaches" of the
  same company are often one incident under two brands.

## What they cannot answer

- **Whether the claim is true.** A leak-site post is a criminal's marketing.
  Victim lists include companies that were never breached, companies breached
  through a third party, and entries posted to pressure a negotiation.
- **What is actually in the dump.** Do not download it to find out. The metadata
  the aggregators publish - file counts, sample screenshots, dates - is the
  evidence you can safely work with; the corpus itself is stolen personal data
  and often criminal property. See the dark web section of
  [../../LEGAL.md](../../LEGAL.md).
- **The full picture.** Every tracker crawls a different subset of sites and
  each misses posts during takedowns and rebrands. Compare at least two.

## Using them well

- **Watch, do not sample.** These are monitoring sources: a weekly check, or an
  API poll into your own store, beats a panicked search after the fact.
- **Record the post, not just the fact.** Screenshot and hash the entry, with a
  timestamp. Posts are edited and deleted, and the aggregator's copy may change.
- **Route disclosure through the right people.** If your organisation appears,
  this is an incident, not an OSINT finding. Legal and incident response own
  the next step - see [../../00-methodology/frameworks/README.md](../../00-methodology/frameworks/README.md).
- **Watch the supply chain, not just yourself.** Most organisations first learn
  about a third-party breach because their supplier is named.

## Tools here

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [RansomLook](ransomlook.md) | I have an organisation name or domain. Which crew has claimed it, when, and what else do they publish - without me ever loading... | 2 | passive |
| [Ransomware.live](ransomware-live.md) | I have a company name, a country or an encrypted-file extension. Has this organisation been named on a leak site, and what do... | 2 | passive |
| [DarkOwl](darkowl.md) | I have a client name, domain or credential. Where does it appear across leak sites, markets, forums and Telegram, and can I still... | 3 | passive |
| [ransomwatch](ransomwatch.md) | I need a baseline. What did the leak-site ecosystem look like before mid-2025, and where is a free, citable, timestamped record... | 3 | active |
<!-- END:TOOLS -->

## Related

- [../onion-discovery/](../onion-discovery/) - where leak-site addresses come from
- [../../08-people-and-identity/email-osint/hibp.md](../../08-people-and-identity/email-osint/hibp.md) - the credential side of the same exposure
- [../../13-threat-intel/feeds-and-trackers/](../../13-threat-intel/feeds-and-trackers/) - the infrastructure the same groups use
