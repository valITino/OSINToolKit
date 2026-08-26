---
name: EagleEye
slug: eagleeye
tier: 3
contact: active
type: cli
cost: free
platforms: [linux]
url: https://github.com/ThoughtfulDev/EagleEye
categories: [people-and-identity, reverse-image]
tags: [face-recognition, social-media, legacy, privacy-sensitive]
status: unverified
status_checked: 2026-08-26
---

# EagleEye

## What question does it answer?
Given a name and some photos, can automated face comparison find that person's social
media profiles?

## Why this is tier 3
The premise - scrape candidate profiles, then use face recognition to pick matches -
is fragile in practice and heavy in consequence:

- **It depends on scraping social platforms**, which actively block automation. The
  scraping stage breaks routinely, and when it breaks the whole tool returns nothing.
- **Automated face recognition against real people is legally sensitive.** Under GDPR,
  biometric data used to identify a person is a special category with a high bar for
  lawful processing. Several jurisdictions restrict it further.
- Maintenance has been intermittent; dependency setup is heavy.

Manual reverse image search ([Yandex](yandex-images.md), [TinEye](tineye.md)) combined
with [username enumeration](../username-enum/README.md) achieves the same investigative
goal with better reliability and far less legal exposure. Do that instead.

## Install
```bash
# Heavy dependency stack including face_recognition and a browser driver.
# Verify current status before investing time.
```

## Usage
```bash
# Intended: supply a name plus known images, then run the comparison pipeline.
```

## Output
Candidate profiles with a similarity indication for the face comparison.

## Gotchas
- **Face recognition produces false matches**, and a false identification of a real
  person is a serious harm, not a minor error. Never treat a match as identification.
- **Biometric processing needs a lawful basis** - see [../../LEGAL.md](../../LEGAL.md).
- Scraping breaches platform terms and breaks constantly.

## Alternatives
- [Yandex Images](yandex-images.md) - manual, better at faces, no biometric processing by you
- [TinEye](tineye.md) - exact-match provenance
- [Sherlock](../username-enum/sherlock.md) / [Maigret](../username-enum/maigret.md) - find profiles by handle
