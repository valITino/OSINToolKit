# Password reset clues

No tool - just methodology, and a sharp one. Many services, when you begin a
password or account recovery flow, show a **masked hint** to confirm you have the
right account: `j•••••@g•••l.com`, a phone ending `•• 47`, "we sent a code to your
number ending in 47." Those masks leak more than they intend.

## What the mask reveals

- **The provider.** `g•••l.com` is Gmail; `•••look.com` is Outlook. The domain
  shape often survives masking.
- **The length.** Many masks use one dot per hidden character. Counting the dots
  gives you the length of the local part or the phone number - a strong filter when
  you are testing candidate emails.
- **The endpoints.** First and last characters of an email, last two digits of a
  phone, are frequently shown in the clear.

## Triangulation across services

The power is in combining masks. If service A masks a recovery email as
`j•••@g•••.com` and service B masks a recovery phone as `••• ••• ••47`, and a
third confirms a first initial, you can often reconstruct or confirm an identity
that no single service would give up. Google, in particular, historically exposed
partial recovery phone digits in its own reset flow.

## Discipline

- Record each service, the exact mask shown, and the timestamp
  ([documentation](../../00-methodology/documentation/README.md)).
- A mask *confirms* a guess; it rarely hands you the whole value. Use it to narrow
  candidates you found elsewhere, not as a primary source.

## Legal and ethical boundary

Initiating recovery flows on accounts you do not own can breach a service's terms
and, depending on intent and jurisdiction, computer-misuse law. Do not trigger
notifications to the account holder, do not attempt to actually reset anything, and
have a lawful basis. See [../../LEGAL.md](../../LEGAL.md). This is a technique to
understand and to defend against as much as to use.

## Related

- [email-osint](../email-osint/README.md) - confirm which services an email holds an account on
- [username-enum](../username-enum/README.md) - find the accounts to probe in the first place
