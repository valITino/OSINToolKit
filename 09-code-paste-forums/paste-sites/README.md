# Paste sites

Where leaked data often surfaces first, and how to search dumps of it.

**psbdmp is gone.** It was the one service that let you search historical Pastebin
content by email, domain, or keyword. `psbdmp.ws` no longer resolves and `psbdmp.cc`
has served only a farewell page since February 2026. Tooling that hardcodes it -
including several scrapers and framework modules - now fails silently, so an empty
result from one of those is a dead dependency, not a clean target. There is no
verified drop-in replacement; searching pastes now means monitoring
[Pastebin](pastebin.md) yourself or working from links found elsewhere.

The encrypted paste services below cannot be searched at all, by design. That is
exactly why they get used.

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [paaster](paaster.md) | I have a paaster link, or I have the device of someone who used paaster. What can I still recover? | 2 | passive |
| [Pastebin](pastebin.md) | Has data relating to my target - credentials, a customer list, internal configuration - been posted publicly, and when did it... | 2 | passive |
| [PrivateBin](privatebin.md) | I found a PrivateBin link in a chat log, an email, or another paste. Can I read it - and why can I not search for others like it? | 2 | passive |
<!-- END:TOOLS -->
