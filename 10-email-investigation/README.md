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
| [MXToolbox](header-analysis/mxtoolbox.md) | I have an email header block or a domain. What path did this message take, how long did each hop hold it, and is the sending... | 2 | passive |
| [swaks](server-checks/swaks.md) | How does this mail server actually behave - what does it advertise, does it accept mail for this address, and how does it... | 2 | active |
<!-- END:TOOLS -->
