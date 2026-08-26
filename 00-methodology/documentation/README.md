# Documentation

An investigation that is not documented did not happen, legally speaking. If a
finding might ever be challenged - in court, in a report, by a colleague - the
record of *how* you got it matters as much as the finding. Build the habit before
you need it.

## Contemporaneous notes

Write down what you did as you do it, not afterward. For each step record:

- **When** (timestamp, with timezone).
- **What** you ran (exact command or URL, tool version).
- **Why** (what question the step was answering).
- **What came back** (the result, and where you saved the raw output).

Keep raw output verbatim. A screenshot of a parsed table is not the same as the
JSON the API returned; save both.

## Screenshots and captures

- Capture the whole context: URL bar, timestamp, and the content in one frame.
  A cropped screenshot loses provenance.
- For web pages that may change or vanish, also archive them
  ([Wayback](../../06-history-and-archives/web-archive/wayback-cdx-api.md),
  archive.today) and save the URL of the archived copy.
- Prefer tools that record reproducibly:
  [gowitness](../../04-web-exploration/monitoring-visual/gowitness.md) for bulk web
  screenshots, [urlscan.io](../../04-web-exploration/fingerprinting/urlscan-io.md)
  for a dated, shareable page capture.

## Chain of custody

If evidence may be used in a proceeding, track it from acquisition onward:

- **What** the item is (file, hash, source).
- **Who** collected it and who has held it since.
- **When** each transfer happened.
- **How** it was stored and protected from alteration.

Hash every acquired file (`sha256sum`) at collection and record the hash. A
matching hash later proves the file is unchanged. Work on copies; never analyse the
only original.

## Tooling

- Note-taking that timestamps and structures: any tool you will actually keep up -
  a case wiki, Obsidian, CherryTree, or a disciplined markdown file per case.
- [recon-ng](../../01-orchestrators/modular-frameworks/recon-ng.md)'s workspace
  database doubles as a structured record of what was collected.

## Related

- [../frameworks/README.md](../frameworks/README.md) - NIST 800-86 forensic discipline
- [../opsec/README.md](../opsec/README.md)
