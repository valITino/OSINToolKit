#!/usr/bin/env python3
"""HTTP-check every `url` in tool frontmatter and report the ones that fail.

Sends an HTTP HEAD (falling back to a ranged GET for servers that reject HEAD)
to every tool file's `url` and prints a status line per tool. Tools whose URL
does not return a 2xx/3xx are collected at the end so dead entries can be found
and marked `status: broken`.

Standard library only. Run from the repository root:

    python3 scripts/check-links.py                 # check everything
    python3 scripts/check-links.py --timeout 15     # per-request timeout (s)
    python3 scripts/check-links.py --delay 1.0      # seconds between requests
    python3 scripts/check-links.py --tier 3         # only check tier-3 tools

Be polite: this touches third-party servers. The default delay is deliberate.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
import urllib.error
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "templates", "scripts", ".github", "workflows"}
UA = "osint-toolkit-linkcheck/1.0 (+https://github.com/valITino/OSINToolKit)"


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
    """Return (ok, code_or_reason). Tries HEAD, falls back to ranged GET."""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method)
        req.add_header("User-Agent", UA)
        if method == "GET":
            req.add_header("Range", "bytes=0-0")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return True, resp.status
        except urllib.error.HTTPError as e:
            # Some servers reject HEAD with 405/403; retry with GET.
            if method == "HEAD" and e.code in (403, 405, 406, 501):
                continue
            return False, e.code
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            reason = getattr(e, "reason", e)
            if method == "HEAD":
                continue
            return False, str(reason)
    return False, "unreachable"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--timeout", type=float, default=10.0, help="per-request timeout in seconds")
    ap.add_argument("--delay", type=float, default=0.5, help="seconds to wait between requests")
    ap.add_argument("--tier", type=int, choices=(1, 2, 3), help="only check this tier")
    args = ap.parse_args()

    entries = collect(args.tier)
    print(f"Checking {len(entries)} URL(s) with timeout={args.timeout}s, delay={args.delay}s\n")

    failures = []
    for i, (rel, url) in enumerate(entries):
        ok, info = check(url, args.timeout)
        mark = "ok  " if ok else "FAIL"
        print(f"[{mark}] {info!s:>12}  {url}  ({rel})")
        if not ok:
            failures.append((rel, url, info))
        if i < len(entries) - 1:
            time.sleep(args.delay)

    print()
    if failures:
        print(f"{len(failures)} URL(s) failed:")
        for rel, url, info in failures:
            print(f"  - {rel}: {url} -> {info}")
        print("\nReview these; set 'status: broken' where the tool is truly gone.")
        sys.exit(1)
    print("All URLs reachable.")


if __name__ == "__main__":
    main()
