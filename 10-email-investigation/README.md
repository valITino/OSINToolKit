# 10 - Email Investigation

You have an .eml or a header block. Trace the path and origin, check the sending domain's SPF/DKIM/DMARC and whether a mailbox exists, and understand tracking and spoofing.

## Subcategories

- [header-analysis/](header-analysis/) - MXToolbox - parse headers, read them bottom-up
- [server-checks/](server-checks/) - SPF/DKIM/DMARC, callback verification, swaks
- [tracking/](tracking/) - Open-tracking and token methodology
- [spoofing-testing/](spoofing-testing/) - Authorised spoof testing

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [checkdmarc](server-checks/checkdmarc.md) | This message claims to come from example.com. **Could** it have? What does that domain's published policy actually say, and would... | 2 | active |
| [MXToolbox](header-analysis/mxtoolbox.md) | I have an email header block or a domain. What path did this message take, how long did each hop hold it, and is the sending... | 2 | passive |
| [PGP keyservers](server-checks/pgp-keyservers.md) | I have an email address. Does this person publish a PGP key - and does that key tie this address to a real name or to their... | 2 | passive |
| [swaks](server-checks/swaks.md) | How does this mail server actually behave - what does it advertise, does it accept mail for this address, and how does it... | 2 | active |
<!-- END:TOOLS -->
