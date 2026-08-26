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
    python3 scripts/check-links.py --timeout 8      # per-request timeout (s)
    python3 scripts/check-links.py --delay 1.0      # seconds between requests
    python3 scripts/check-links.py --tier 3         # only check tier-3 tools
    python3 scripts/check-links.py --strict         # treat BLOCKED as failure too

Be polite: this touches third-party servers. The default delay is deliberate.
"""

from __future__ import annotations

import argparse
import http.client
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "templates", "scripts", ".github", "workflows",
             "__pycache__", "node_modules", "venv", ".venv", "SecLists"}
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
        # YAML needs only one space before '#'. A '#' with no leading
        # whitespace stays part of the value, keeping URL fragments intact.
        if value[:1] not in ("'", '"'):
            value = re.split(r"\s#", value, maxsplit=1)[0].strip()
        meta[key.strip()] = value.strip("'\"")
    return meta


def collect(tier_filter):
    entries = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            if not fn.endswith(".md") or fn in ("README.md", "INDEX.md"):
                continue
            path = os.path.join(dirpath, fn)
            # utf-8-sig: an editor-written BOM must not hide a tool's url
            with open(path, encoding="utf-8-sig") as fh:
                meta = parse_frontmatter(fh.read())
            if not meta or "url" not in meta or "slug" not in meta:
                continue
            if tier_filter and str(meta.get("tier")) != str(tier_filter):
                continue
            entries.append((os.path.relpath(path, REPO_ROOT), meta["url"]))
    entries.sort()
    return entries


def check(url, timeout):
    """Return (verdict, detail). Tries HEAD, falls back to a ranged GET.

    A HEAD response never decides the verdict on its own: plenty of servers
    answer 404 or 405 to HEAD and serve the same URL fine over GET. Since DEAD
    is the only verdict that fails the job, the second request is worth
    spending on any URL that is about to be condemned.
    """
    last = (BLOCKED, "no response")
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method)
            req.add_header("User-Agent", UA)
            if method == "GET":
                req.add_header("Range", "bytes=0-0")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return OK, resp.status
        except urllib.error.HTTPError as e:
            if e.code in DEAD_CODES:
                verdict = (DEAD, e.code)
            elif e.code in BLOCKED_CODES:
                verdict = (BLOCKED, f"{e.code} (bot challenge or auth wall)")
            else:
                verdict = (BLOCKED, e.code)
            if method == "HEAD":
                last = verdict
                continue
            return verdict
        except urllib.error.URLError as e:
            reason = getattr(e, "reason", e)
            # DNS failure usually means a genuinely dead host, but resolvers
            # blip; confirm on the second pass before condemning the URL.
            verdict = ((DEAD, f"DNS failure: {reason}")
                       if isinstance(reason, socket.gaierror)
                       else (BLOCKED, str(reason)))
            if method == "HEAD":
                last = verdict
                continue
            return verdict
        except ValueError as e:
            # http.client.InvalidURL is a ValueError; catch before OSError so a
            # malformed url is reported as such rather than as a socket error.
            return DEAD, f"malformed URL: {e}"
        except (OSError, http.client.HTTPException) as e:
            # RemoteDisconnected, IncompleteRead and raw socket errors are not
            # all URLError subclasses. Uncaught, one of them aborts the entire
            # run partway through and the remaining URLs go unchecked.
            verdict = (BLOCKED, f"{type(e).__name__}: {e}")
            if method == "HEAD":
                last = verdict
                continue
            return verdict
    return last


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--timeout", type=float, default=10.0, help="per-request timeout in seconds")
    ap.add_argument("--delay", type=float, default=0.5, help="seconds to wait between requests")
    ap.add_argument("--tier", type=int, choices=(1, 2, 3), help="only check this tier")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero on BLOCKED results too (noisy; off by default)")
    args = ap.parse_args()

    # Block buffering hides all progress when stdout is redirected, so a
    # run killed by a CI timeout would log nothing at all.
    sys.stdout.reconfigure(line_buffering=True)

    entries = collect(args.tier)
    if not entries:
        print("No tool files with a `url` were found. Check the layout and\n"
              "frontmatter keys before trusting this result.", file=sys.stderr)
        sys.exit(2)

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
        print(f"\n--strict: failing on {len(blocked)} BLOCKED result(s).")
        sys.exit(1)

    print("\nNo dead URLs found.")


if __name__ == "__main__":
    main()
