---
name: Robin
slug: robinonroids
tier: 2
contact: active
type: gui
cost: free
platforms: [linux, macos, windows]
url: https://github.com/valITino/robinonroids
categories: [darkweb, active-crawling]
tags: [tor, onion, search-engines, llm, scraping, reporting]
status: active
status_checked: 2026-09-22
---

# Robin

## What question does it answer?
I have a topic or selector. Which results from multiple onion search engines are
relevant, what do their pages say, and can an LLM turn the collected evidence
into a sourced investigation summary and follow-up pivots?

## When to reach for it
Use Robin when an analyst wants one local web interface for query refinement,
multi-engine discovery, relevance filtering, page collection, and reporting.
Unlike a search-only tool, it fetches selected result pages; unlike a crawler,
it does not follow a target's link graph. Prefer manual review when source
fidelity matters more than fast triage or when case data must not reach an LLM.

## Install
```bash
git clone https://github.com/valITino/robinonroids.git && cd robinonroids
cp .env.example .env   # add one supported provider key, or configure Ollama
docker build -t robinonroids .
docker run --rm -p 8501:8501 --add-host=host.docker.internal:host-gateway \
  -v "$(pwd)/.env:/app/.env" robinonroids
```

## Usage
```text
http://localhost:8501  # choose a model and report preset, enter the query, run
# Review Sources before Findings; download the summary or save the investigation.
```

## Output
The Streamlit UI shows the refined query, selected source titles and onion URLs,
an LLM-generated report, suggested pivot queries, and grounded follow-up chat.
Completed investigations are also stored locally as JSON; reports can be
downloaded as Markdown.

## Gotchas
- **This is active contact.** Robin queries 16 onion search engines through Tor,
  then fetches selected onion pages concurrently. Both engine and target
  operators can log the requests, and fetched content may be illegal to retain.
- Queries, result metadata, and scraped page text are sent to the configured LLM
  provider. Use a local model for sensitive work, or obtain approval before
  disclosing case material to a third party.
- LLM selection and summaries are leads, not evidence. Preserve the source URL,
  capture time, page, and hash separately; verify every material claim manually.
- The listed repository is a GitHub fork of `apurvsinghgautam/robin` and was
  identical to its upstream `main` branch when checked. Confirm both before
  choosing where to install updates from.
- Robin expects a Tor SOCKS proxy on `127.0.0.1:9050`; the container does not
  provide Tor. Search engines disappear and change, so zero results prove
  neither absence nor successful coverage.

## Alternatives
- [darkdump](darkdump.md) - CLI search and lightweight result-page triage without an LLM workflow
- [TorBot](torbot.md) - follow links from one known onion and build its adjacency tree
- [Ahmia](../onion-discovery/ahmia.md) - passive clearweb search before contacting onion services
