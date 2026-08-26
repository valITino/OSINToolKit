# Social media

No single tool covers social platforms well for long - APIs close, scrapers break,
and terms of service shift. What lasts is method. Treat each platform as its own
source with its own quirks.

## Cross-platform first move

Start by spreading the handle, then confirm per platform:

- [Sherlock](../username-enum/sherlock.md) / [Maigret](../username-enum/maigret.md)
  to find where a username exists.
- Reverse-image the profile photo ([Yandex](../reverse-image/yandex-images.md),
  [TinEye](../reverse-image/tineye.md)) - reused avatars link accounts a name never
  would.

## Platform notes

- **Reddit**: a user's post/comment history is public and often revealing of
  timezone, location, and interests. Note that **Reveddit and Pushshift-based
  history tools no longer work** the way they used to - deleted-content recovery via
  those routes is largely gone. Work from what is live plus
  [Wayback](../../06-history-and-archives/web-archive/wayback-cdx-api.md).
- **Telegram**: public channels and groups are searchable and often the primary
  source in some investigations; membership and forwarded-message trails matter.
- **X/Twitter, Instagram, Facebook, TikTok, LinkedIn**: heavily rate-limited and
  login-walled. Expect to work manually, from a sock-puppet account
  ([OPSEC](../../00-methodology/opsec/README.md)), and to archive as you go because
  content disappears.

## Discipline

- Archive before you analyse - posts get deleted mid-investigation
  ([documentation](../../00-methodology/documentation/README.md)).
- Scraping and automated collection frequently breach platform terms and can carry
  legal weight for personal data. Have a lawful basis; see [../../LEGAL.md](../../LEGAL.md).

## Related

- [username-enum](../username-enum/README.md)
- [reverse-image](../reverse-image/README.md)
