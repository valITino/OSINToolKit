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
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories we never treat as containing tool files.
SKIP_DIRS = {".git", "templates", "scripts", ".github", "workflows"}

REQUIRED_KEYS = [
    "name", "slug", "tier", "contact", "type", "cost",
    "platforms", "url", "categories", "tags", "status", "status_checked",
]
VALID_TIERS = {1, 2, 3}
VALID_CONTACT = {"passive", "active", "intrusive"}
VALID_STATUS = {"active", "stale", "broken", "archived", "unverified"}

BEGIN_MARKER = "<!-- BEGIN:TOOLS -->"
END_MARKER = "<!-- END:TOOLS -->"

MD_LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


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
        value = value.strip()
        # strip inline comments that follow two spaces + '#'
        if "  #" in value:
            value = value.split("  #", 1)[0].strip()
        meta[key] = _coerce(value)
    body = "\n".join(lines[end + 1:])
    return meta, body


def _coerce(value):
    if value == "":
        return ""
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip("'\"") for item in inner.split(",")]
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
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            if fn in ("README.md", "INDEX.md"):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            meta, body = parse_frontmatter(text)
            if meta is None or "slug" not in meta:
                continue
            errors.extend(validate(path, meta, fn))
            tools.append(Tool(path, meta, body))
    tools.sort(key=lambda t: (t["tier"] or 9, str(t["categories"]), str(t["name"]).lower()))
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
    cats = meta.get("categories")
    if isinstance(cats, list) and len(cats) >= 2:
        parent = os.path.basename(os.path.dirname(path))
        grandparent = os.path.basename(os.path.dirname(os.path.dirname(path)))
        gp_clean = grandparent.split("-", 1)[1] if grandparent[:2].isdigit() else grandparent
        if cats[1] != parent:
            errs.append(f"{rel}: categories[1] '{cats[1]}' != directory '{parent}'")
        if cats[0] != gp_clean:
            errs.append(f"{rel}: categories[0] '{cats[0]}' != '{gp_clean}'")
    return errs


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def link(target_abs, from_dir):
    return os.path.relpath(target_abs, from_dir).replace(os.sep, "/")


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
            f"| [{t['name']}]({href}) | {t['tier']} | {t['contact']} "
            f"| {cat} | {t['status']} | {url} |"
        )
    out.append("")
    return "\n".join(out)


def render_tools_table(tools, from_dir):
    rows = [
        "| Tool | Answers | Tier | Contact |",
        "|---|---|---|---|",
    ]
    for t in sorted(tools, key=lambda x: (x["tier"] or 9, str(x["name"]).lower())):
        href = link(t.path, from_dir)
        answer = (t.answer or "").replace("|", "\\|")
        rows.append(f"| [{t['name']}]({href}) | {answer} | {t['tier']} | {t['contact']} |")
    return "\n".join(rows)


def update_readmes(tools, check):
    stale = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
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


def check_internal_links():
    """Report relative markdown links that do not resolve to a file on disk.

    Skips http(s), anchors, and mailto. templates/ is skipped because the
    template deliberately contains a placeholder link.
    """
    errs = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "templates")]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, REPO_ROOT)
            with open(path, encoding="utf-8") as fh:
                for lineno, line in enumerate(fh, 1):
                    for _text, target in MD_LINK.findall(line):
                        if target.startswith(("http://", "https://", "#", "mailto:")):
                            continue
                        target = target.split("#")[0].strip()
                        if not target:
                            continue
                        if not os.path.exists(os.path.normpath(os.path.join(dirpath, target))):
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
