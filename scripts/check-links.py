#!/usr/bin/env python3
"""HTTP-check every `url` in tool frontmatter and report the ones that fail.

Sends an HTTP HEAD (falling back to a ranged GET for servers that reject HEAD)
to every tool file's `url`, then classifies the result into three buckets:

  OK        2xx/3xx - the page is there.
  BLOCKED   The server answered but refused an automated client: 401/403/429,
            a Cloudflare or WAF bot challenge, or a connection reset. This says
            nothing about whether the tool is alive, so it is NOT a failure.
  DEAD      404/410, DNS failure, or an explicit "no such host". These are the
            ones worth acting on.

That distinction matters. Many tool sites in this repo (Shodan, AbuseIPDB,
ThatsThem and others) sit behind bot protection and will answer 403 to any
scripted request forever. An earlier version of this script counted those as
failures, which would have marked a large fraction of perfectly healthy tools
as broken. Only DEAD results should ever change a tool's `status`.

**GitHub URLs:** many networks and CI environments block or rate-limit scripted
requests to github.com while git itself still works. If a github.com URL reports
BLOCKED, confirm it before believing it:

    git ls-remote https://github.com/owner/repo HEAD

A hash means the repository is alive. "could not read Username" means it is gone,
renamed, or private - that is a real DEAD result.

Standard library only. Run from the repository root:

    python3 scripts/check-links.py                 # check everything
    python3 scripts/check-links.py --timeout 15     # per-request timeout (s)
    python3 scripts/check-links.py --delay 1.0      # seconds between requests
    python3 scripts/check-links.py --tier 3         # only check tier-3 tools
    python3 scripts/check-links.py --strict         # treat BLOCKED as failure too

Be polite: this touches third-party servers. The default delay is deliberate.
"""

from __future__ import annotations

import argparse
import os
import socket
import sys
import time
import urllib.error
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "templates", "scripts", ".github", "workflows"}
UA = "osint-toolkit-linkcheck/1.0 (+https://github.com/valITino/OSINToolKit)"

OK, BLOCKED, DEAD = "OK", "BLOCKED", "DEAD"

# Answered, but refused an automated client. Says nothing about tool health.
BLOCKED_CODES = {401, 402, 403, 407, 429, 503, 520, 521, 522, 526}
# The resource is genuinely not there.
DEAD_CODES = {404, 410}


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None
    meta = {}
    for raw in lines[1:end]:
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if "  #" in value:
            value = value.split("  #", 1)[0].strip()
        meta[key.strip()] = value.strip("'\"")
    return meta


def collect(tier_filter):
    entries = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md") or fn in ("README.md", "INDEX.md"):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding="utf-8") as fh:
                meta = parse_frontmatter(fh.read())
            if not meta or "url" not in meta or "slug" not in meta:
                continue
            if tier_filter and str(meta.get("tier")) != str(tier_filter):
                continue
            entries.append((os.path.relpath(path, REPO_ROOT), meta["url"]))
    entries.sort()
    return entries


def check(url, timeout):
    """Return (verdict, detail). Tries HEAD, falls back to a ranged GET."""
    last = None
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method)
        req.add_header("User-Agent", UA)
        if method == "GET":
            req.add_header("Range", "bytes=0-0")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return OK, resp.status
        except urllib.error.HTTPError as e:
            last = e.code
            # Many servers reject HEAD specifically; retry those with GET.
            if method == "HEAD" and e.code in (403, 405, 406, 501):
                continue
            if e.code in DEAD_CODES:
                return DEAD, e.code
            if e.code in BLOCKED_CODES:
                return BLOCKED, f"{e.code} (bot challenge or auth wall)"
            return BLOCKED, e.code
        except urllib.error.URLError as e:
            reason = getattr(e, "reason", e)
            last = reason
            # DNS resolution failure is a genuinely dead host.
            if isinstance(reason, socket.gaierror):
                return DEAD, f"DNS failure: {reason}"
            if method == "HEAD":
                continue
            # Reset/timeout mid-handshake: inconclusive, often bot protection.
            return BLOCKED, f"{reason}"
        except (TimeoutError, socket.timeout):
            last = "timeout"
            if method == "HEAD":
                continue
            return BLOCKED, "timeout"
        except ValueError as e:
            return DEAD, f"malformed URL: {e}"
    return BLOCKED, str(last)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--timeout", type=float, default=10.0, help="per-request timeout in seconds")
    ap.add_argument("--delay", type=float, default=0.5, help="seconds to wait between requests")
    ap.add_argument("--tier", type=int, choices=(1, 2, 3), help="only check this tier")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero on BLOCKED results too (noisy; off by default)")
    args = ap.parse_args()

    entries = collect(args.tier)
    print(f"Checking {len(entries)} URL(s) with timeout={args.timeout}s, delay={args.delay}s\n")

    dead, blocked = [], []
    for i, (rel, url) in enumerate(entries):
        verdict, info = check(url, args.timeout)
        print(f"[{verdict:<7}] {info!s:>34}  {url}  ({rel})")
        if verdict == DEAD:
            dead.append((rel, url, info))
        elif verdict == BLOCKED:
            blocked.append((rel, url, info))
        if i < len(entries) - 1:
            time.sleep(args.delay)

    ok = len(entries) - len(dead) - len(blocked)
    print(f"\n{ok} OK, {len(blocked)} blocked, {len(dead)} dead.")

    if blocked:
        print(f"\n{len(blocked)} BLOCKED - the server answered but refused an automated")
        print("client. This is NOT evidence the tool is dead; do not change `status`")
        print("on the strength of it. For github.com URLs confirm with:")
        print("    git ls-remote <url> HEAD")
        for rel, url, info in blocked:
            print(f"  - {rel}: {url} -> {info}")

    if dead:
        print(f"\n{len(dead)} DEAD - these are worth acting on:")
        for rel, url, info in dead:
            print(f"  - {rel}: {url} -> {info}")
        print("\nVerify each by hand, then set 'status: broken' (or fix the url).")
        sys.exit(1)

    if blocked and args.strict:
        sys.exit(1)

    print("\nNo dead URLs found.")


if __name__ == "__main__":
    main()
