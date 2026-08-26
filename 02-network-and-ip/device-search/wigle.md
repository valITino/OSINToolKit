---
name: WiGLE
slug: wigle
tier: 2
contact: passive
type: web
cost: freemium
platforms: [web]
url: https://wigle.net/
categories: [network-and-ip, device-search]
tags: [wifi, bssid, ssid, wardriving, location]
status: unverified
status_checked: 2026-08-26
---

# WiGLE

## What question does it answer?
I have a wireless network name (SSID) or a MAC address (BSSID). Where in the world
has that network been observed?

## When to reach for it
When a photo, screenshot, or device artifact gives you a wireless network and you
need to place it geographically. WiGLE is a crowd-sourced database of wardriving
observations - volunteers log the networks their devices see, with GPS coordinates -
so a distinctive SSID or a specific BSSID can pin down a street address. It also
covers Bluetooth and cell observations.

## Install
```bash
# Web search at wigle.net (account required). API access needs credentials.
```

## Usage
```text
https://wigle.net/search        # search by SSID, BSSID, or map area
# A BSSID (the AP's MAC) is far more precise than an SSID, which may be shared.
```

## Output
Observation records: SSID, BSSID, encryption type, the coordinates where it was
seen, and the first/last observation dates. The map view plots them.

## Gotchas
- **Coverage is uneven** - it depends entirely on whether a volunteer drove past.
  No result means nobody logged it, not that the network does not exist.
- **A common SSID is worthless** for location: thousands of networks are named
  after the same default or the same coffee chain. Use the BSSID when you have it.
- Access points move (routers get relocated, mobile hotspots travel), and
  observations can be years old. Check the dates.
- Searching requires a free account, and heavier use requires API credentials.

## Alternatives
- [../geolocation/README.md](../geolocation/README.md) - IP-based location, with its own limits
- [../../07-documents-metadata/geo-media/README.md](../../07-documents-metadata/geo-media/README.md) - placing an image from its content
