# 08 - People and Identity

You have a name, username, email, or photo. Search for the person, spread a username across platforms, tie an email to accounts and breaches, and run a reverse image search. Personal data - mind the law.

## Subcategories

- [people-search/](people-search/) - ThatsThem - free people/IP lookup
- [public-records/](public-records/) - Registries and court records
- [username-enum/](username-enum/) - Sherlock, Maigret - one handle across many sites
- [email-osint/](email-osint/) - holehe, HIBP - which services an email is on
- [reverse-image/](reverse-image/) - Yandex, TinEye - find where an image appears
- [social-media/](social-media/) - Platform-specific notes
- [password-reset-clues/](password-reset-clues/) - Masked hints from reset flows (methodology)
- [ip-luring/](ip-luring/) - Canarytokens, IPLogger - induce a subject to reveal an IP

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [Canarytokens](ip-luring/canarytokens.md) | Did someone open this document, visit this URL, or access this resource - and from what IP and client? | 2 | active |
| [Have I Been Pwned](email-osint/hibp.md) | I have an email address. Which public data breaches has it appeared in, and what categories of data were exposed each time? | 2 | passive |
| [holehe](email-osint/holehe.md) | I have an email address. Which online services is it registered with? | 2 | active |
| [Maigret](username-enum/maigret.md) | I have a username. Where does it exist, and what do those profiles actually say - names, bios, locations, linked accounts? | 2 | active |
| [Sherlock](username-enum/sherlock.md) | I have a username. Which of hundreds of sites has an account registered under it? | 2 | active |
| [ThatsThem](people-search/thatsthem.md) | I have a name, phone number, email, or IP. What publicly aggregated records connect to it - address, relatives, associated phone... | 2 | passive |
| [TinEye](reverse-image/tineye.md) | Where did this exact image first appear, and how has it been used and modified since? | 2 | passive |
| [Yandex Images](reverse-image/yandex-images.md) | I have a photo. Where else does this image - or a visually similar one, or this person's face - appear online? | 2 | passive |
| [EagleEye](reverse-image/eagleeye.md) | Given a name and some photos, can automated face comparison find that person's social media profiles? | 3 | active |
| [IPLogger / Grabify](ip-luring/iplogger-grabify.md) | If I get someone to click a link I control, what is their IP address, approximate location, device, and browser? | 3 | active |
| [userrecon](username-enum/userrecon.md) | Which social platforms have an account under this username? | 3 | active |
<!-- END:TOOLS -->
