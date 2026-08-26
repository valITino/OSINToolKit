#!/usr/bin/env python3
"""Regenerate INDEX.md and refresh the tool tables in every category README.

Walks the repository, parses the YAML frontmatter of every tool file, and:

  1. Writes INDEX.md - a sortable table of every tool
     (name, tier, contact, category, status, url).
  2. Replaces the block between <!-- BEGIN:TOOLS --> and <!-- END:TOOLS -->
     in every README.md with a table of the tools that live in that README's
     directory subtree (tool, question it answers, tier, contact).

It also validates as it goes: required frontmatter keys, allowed values for
tier/contact/status, filename-matches-slug, categories-match-directory, and
that every relative markdown link in the repo resolves to a real file.

Standard library only. Run from the repository root:

    python3 scripts/build-index.py            # rewrite files in place
    python3 scripts/build-index.py --check     # exit 1 if anything is stale

The --check mode makes no changes; it is what CI runs.
"""

from __future__ import annotations

import argparse
import os
import csv
import re
import sys
import urllib.parse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Top-level directories that never contain tool files, matched against the
# repo-relative path so a nested directory of the same name is not dropped.
# ".github" already covers CI config; the repo's own top-level "workflows/"
# holds playbooks and stays in scope.
SKIP_TOP_LEVEL = {".git", "templates", "scripts", ".github"}

# Directory names skipped at any depth: vendored or generated trees a
# contributor may create locally. SecLists is named explicitly because
# 99-resources/wordlists tells contributors to clone it, and .gitignore
# anticipates it landing in the repo root.
SKIP_ANYWHERE = {"__pycache__", "node_modules", "venv", ".venv", "SecLists"}

# A tool file is expected under a numbered category directory. Markdown found
# there that does not parse is an error, not something to skip quietly.
CATEGORY_DIR = re.compile(r"^\d\d-")

REQUIRED_KEYS = [
    "name", "slug", "tier", "contact", "type", "cost",
    "platforms", "url", "categories", "tags", "status", "status_checked",
]
VALID_TIERS = {1, 2, 3}
VALID_CONTACT = {"passive", "active", "intrusive"}
VALID_STATUS = {"active", "stale", "broken", "archived", "unverified"}

BEGIN_MARKER = "<!-- BEGIN:TOOLS -->"
END_MARKER = "<!-- END:TOOLS -->"

# Link targets may contain balanced parentheses, e.g. ./foo(1).md
MD_LINK = re.compile(r"\[([^\]]*)\]\(((?:[^()]|\([^()]*\))+)\)")


def prune(dirpath, dirnames):
    """Filter os.walk's dirnames in place, and sort for deterministic order.

    Ordering matters: os.walk yields os.listdir order, which is sorted on some
    filesystems and hash-ordered on ext4. Without sorting, two entries that tie
    on a sort key could swap between runs and make --check fail intermittently.
    """
    rel = os.path.relpath(dirpath, REPO_ROOT)
    kept = []
    for d in dirnames:
        if d in SKIP_ANYWHERE:
            continue
        top = d if rel == "." else os.path.normpath(os.path.join(rel, d))
        if top in SKIP_TOP_LEVEL:
            continue
        kept.append(d)
    kept.sort()
    dirnames[:] = kept


def in_category_dir(path):
    """True if path sits under a numbered top-level category directory."""
    rel = os.path.relpath(path, REPO_ROOT)
    return bool(CATEGORY_DIR.match(rel.split(os.sep)[0]))


# --------------------------------------------------------------------------- #
# Minimal frontmatter parsing (no third-party YAML dependency)
# --------------------------------------------------------------------------- #
def parse_frontmatter(text):
    """Return (metadata_dict, body_str) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text
    meta = {}
    for raw in lines[1:end]:
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        meta[key] = _coerce(_strip_comment(value.strip()))
    body = "\n".join(lines[end + 1:])
    return meta, body


def _strip_comment(value):
    """Remove a YAML inline comment: whitespace then '#', outside quotes.

    YAML needs only one space before '#', so the old two-space rule let
    "tier: 2 # top tier" through as the string "2 # top tier". A '#' with no
    leading whitespace is part of the value, which keeps URL fragments intact.
    """
    if value[:1] in ("'", '"'):
        quote = value[0]
        closing = value.find(quote, 1)
        if closing != -1:
            return value[: closing + 1]
        return value
    return re.split(r"\s#", value, maxsplit=1)[0].strip()


def _coerce(value):
    if value == "":
        return ""
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        # csv handles quoted items containing commas: ["dns, mx", spf]
        try:
            items = next(csv.reader([inner], skipinitialspace=True))
        except (csv.Error, StopIteration):
            items = inner.split(",")
        return [item.strip().strip("'\"") for item in items if item.strip()]
    stripped = value.strip("'\"")
    if stripped.isdigit():
        return int(stripped)
    return stripped


ANSWER_MAX = 130


def first_answer_line(body):
    """Return the 'What question does it answer?' paragraph, trimmed for a table.

    Reads the whole paragraph rather than its first physical line, because the
    source is hard-wrapped and a line-based read cuts sentences in half. Long
    answers are truncated on a word boundary so the table stays scannable.
    """
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("## what question"):
            para = []
            for follow in lines[i + 1:]:
                if follow.strip().startswith("## "):
                    break
                if not follow.strip():
                    if para:
                        break
                    continue
                para.append(follow.strip())
            text = " ".join(para)
            if len(text) <= ANSWER_MAX:
                return text
            cut = text[:ANSWER_MAX].rsplit(" ", 1)[0].rstrip(" ,;:-")
            return f"{cut}..."
    return ""


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #
class Tool:
    def __init__(self, path, meta, body):
        self.path = path                      # absolute
        self.rel = os.path.relpath(path, REPO_ROOT)
        self.meta = meta
        self.answer = first_answer_line(body)

    def __getitem__(self, key):
        return self.meta.get(key)


def discover_tools():
    tools, errors = [], []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        prune(dirpath, dirnames)
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            if fn in ("README.md", "INDEX.md"):
                continue
            path = os.path.join(dirpath, fn)
            # utf-8-sig so an editor-written BOM does not defeat the leading
            # '---' test and silently drop the file from the index.
            with open(path, encoding="utf-8-sig") as fh:
                text = fh.read()
            meta, body = parse_frontmatter(text)
            rel = os.path.relpath(path, REPO_ROOT)
            if meta is None or "slug" not in meta:
                # Outside the numbered category tree this is expected - it is
                # how LEGAL.md and the playbooks are skipped. Inside it, the
                # file was meant to be a tool and vanishing quietly would leave
                # CI green while the tool disappeared from every table.
                if in_category_dir(path):
                    reason = ("no YAML frontmatter (file must start with '---')"
                              if meta is None else "frontmatter has no 'slug' key")
                    errors.append(f"{rel}: {reason}")
                continue
            errors.extend(validate(path, meta, fn))
            tools.append(Tool(path, meta, body))
    # Sort keys are total (rel path last) and type-safe: a malformed tier must
    # surface as a validation message, not a TypeError traceback.
    tools.sort(key=lambda t: (t["tier"] if isinstance(t["tier"], int) else 9,
                              str(t["categories"]), str(t["name"]).lower(), t.rel))
    return tools, errors


def validate(path, meta, filename):
    rel = os.path.relpath(path, REPO_ROOT)
    errs = []
    for key in REQUIRED_KEYS:
        if key not in meta or meta[key] in ("", None, []):
            errs.append(f"{rel}: missing or empty required key '{key}'")
    if meta.get("tier") not in VALID_TIERS:
        errs.append(f"{rel}: tier must be 1, 2 or 3 (got {meta.get('tier')!r})")
    if meta.get("contact") not in VALID_CONTACT:
        errs.append(f"{rel}: contact must be one of {sorted(VALID_CONTACT)}")
    if meta.get("status") not in VALID_STATUS:
        errs.append(f"{rel}: status must be one of {sorted(VALID_STATUS)}")
    slug = meta.get("slug")
    if slug and filename != f"{slug}.md":
        errs.append(f"{rel}: filename must match slug '{slug}.md'")
    # Compare against the path relative to the repository root. Deriving the
    # category from basename(dirname(...)) made the result depend on what the
    # checkout directory happened to be called, so the same file passed in one
    # clone and failed in another.
    cats = meta.get("categories")
    parts = os.path.relpath(os.path.dirname(path), REPO_ROOT).split(os.sep)
    if len(parts) != 2:
        errs.append(f"{rel}: tool files must live at <NN-category>/<subcategory>/")
    elif not isinstance(cats, list) or len(cats) < 2:
        errs.append(f"{rel}: categories must list [top-category, sub-category]")
    else:
        strip_prefix = lambda p: re.sub(r"^\d+-", "", p)  # noqa: E731
        expected = [strip_prefix(parts[0]), strip_prefix(parts[1])]
        if cats[0] != expected[0]:
            errs.append(f"{rel}: categories[0] '{cats[0]}' != '{expected[0]}'")
        if cats[1] != expected[1]:
            errs.append(f"{rel}: categories[1] '{cats[1]}' != '{expected[1]}'")
    return errs


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def link(target_abs, from_dir):
    return os.path.relpath(target_abs, from_dir).replace(os.sep, "/")


def cell(value):
    """Escape a value for a markdown table cell.

    A single unescaped '|' in a name or URL splits the row into extra columns
    and corrupts the generated table with no validation error to explain it.
    """
    return str("" if value is None else value).replace("|", "\\|")


def render_index(tools):
    out = [
        "# Tool index",
        "",
        "Every tool in the repository, generated by `scripts/build-index.py`.",
        "Do not edit by hand. Sort in your editor or grep by column.",
        "",
        f"{len(tools)} tools indexed.",
        "",
        "| Tool | Tier | Contact | Category | Status | URL |",
        "|---|---|---|---|---|---|",
    ]
    for t in tools:
        cats = t["categories"] or []
        cat = " / ".join(cats) if isinstance(cats, list) else str(cats)
        href = link(t.path, REPO_ROOT)
        url = t["url"] or ""
        out.append(
            f"| [{cell(t['name'])}]({href}) | {cell(t['tier'])} | {cell(t['contact'])} "
            f"| {cell(cat)} | {cell(t['status'])} | {cell(url)} |"
        )
    out.append("")
    return "\n".join(out)


def render_tools_table(tools, from_dir):
    rows = [
        "| Tool | Answers | Tier | Contact |",
        "|---|---|---|---|",
    ]
    ordered = sorted(tools, key=lambda x: (x["tier"] if isinstance(x["tier"], int) else 9,
                                           str(x["name"]).lower(), x.rel))
    for t in ordered:
        href = link(t.path, from_dir)
        rows.append(f"| [{cell(t['name'])}]({href}) | {cell(t.answer)} "
                    f"| {cell(t['tier'])} | {cell(t['contact'])} |")
    return "\n".join(rows)


def update_readmes(tools, check):
    stale = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        prune(dirpath, dirnames)
        if "README.md" not in filenames:
            continue
        readme = os.path.join(dirpath, "README.md")
        with open(readme, encoding="utf-8") as fh:
            content = fh.read()
        if BEGIN_MARKER not in content or END_MARKER not in content:
            continue
        subtree = [
            t for t in tools
            if os.path.abspath(t.path).startswith(os.path.abspath(dirpath) + os.sep)
        ]
        if subtree:
            table = render_tools_table(subtree, dirpath)
        else:
            table = "_No tool files here yet._"
        block = f"{BEGIN_MARKER}\n{table}\n{END_MARKER}"
        pre = content.split(BEGIN_MARKER)[0]
        post = content.split(END_MARKER, 1)[1]
        new_content = f"{pre}{block}{post}"
        if new_content != content:
            stale.append(os.path.relpath(readme, REPO_ROOT))
            if not check:
                with open(readme, "w", encoding="utf-8") as fh:
                    fh.write(new_content)
    return stale


_LISTING_CACHE = {}


def _listing(directory):
    try:
        names = set(os.listdir(directory))
    except OSError:
        names = set()
    _LISTING_CACHE[directory] = names
    return names


def resolves_exactly(full_path):
    """True if every path component exists with exactly this spelling.

    os.path.exists() is case-insensitive on macOS, so a link written as
    ./Geolocation/README.md resolves on the author's laptop and 404s on the
    ext4 CI runner. Checking each component against the real directory listing
    gives the same answer on every filesystem.
    """
    full_path = os.path.normpath(full_path)
    try:
        rel = os.path.relpath(full_path, REPO_ROOT)
    except ValueError:
        return os.path.exists(full_path)
    if rel.startswith(".."):            # outside the repo; fall back
        return os.path.exists(full_path)
    current = REPO_ROOT
    for part in rel.split(os.sep):
        if part == ".":
            continue
        names = _LISTING_CACHE.get(current)
        if names is None:
            names = _listing(current)
        if part not in names:
            return False
        current = os.path.join(current, part)
    return True


def check_internal_links():
    """Report relative markdown links that do not resolve to a file on disk.

    Skips http(s), anchors, and mailto. templates/ is skipped because the
    template deliberately contains a placeholder link.
    """
    errs = []
    _LISTING_CACHE.clear()
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = sorted(d for d in dirnames
                             if d not in ({".git", "templates"} | SKIP_ANYWHERE))
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, REPO_ROOT)
            with open(path, encoding="utf-8-sig") as fh:
                for lineno, line in enumerate(fh, 1):
                    for _text, target in MD_LINK.findall(line):
                        if target.startswith(("http://", "https://", "#", "mailto:")):
                            continue
                        # Percent-decode: editors and GitHub's "copy link"
                        # encode spaces and parentheses in filenames.
                        cleaned = urllib.parse.unquote(target.split("#")[0].strip())
                        cleaned = cleaned.strip("<>")
                        if not cleaned:
                            continue
                        if not resolves_exactly(os.path.join(dirpath, cleaned)):
                            errs.append(f"{rel}:{lineno}: broken link -> {target}")
    return errs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="make no changes; exit 1 if anything is stale or invalid")
    args = ap.parse_args()

    tools, errors = discover_tools()
    if errors:
        print("Frontmatter errors:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)

    index_path = os.path.join(REPO_ROOT, "INDEX.md")
    new_index = render_index(tools)
    old_index = ""
    if os.path.exists(index_path):
        with open(index_path, encoding="utf-8") as fh:
            old_index = fh.read()
    index_stale = new_index != old_index
    if index_stale and not args.check:
        with open(index_path, "w", encoding="utf-8") as fh:
            fh.write(new_index)

    readme_stale = update_readmes(tools, args.check)

    # Run after the READMEs are refreshed so generated tables are checked too.
    link_errors = check_internal_links()
    if link_errors:
        print("Broken internal links:", file=sys.stderr)
        for e in link_errors:
            print(f"  - {e}", file=sys.stderr)

    print(f"{len(tools)} tools indexed.")
    if args.check:
        problems = bool(errors) or bool(link_errors) or index_stale or bool(readme_stale)
        if index_stale:
            print("INDEX.md is out of date. Run scripts/build-index.py.", file=sys.stderr)
        for r in readme_stale:
            print(f"Out of date: {r}", file=sys.stderr)
        if problems:
            sys.exit(1)
        print("Everything up to date.")
    else:
        print(f"INDEX.md {'updated' if index_stale else 'unchanged'}; "
              f"{len(readme_stale)} README(s) refreshed.")
        if errors or link_errors:
            print(f"{len(errors)} frontmatter error(s), "
                  f"{len(link_errors)} broken link(s); see above.", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
