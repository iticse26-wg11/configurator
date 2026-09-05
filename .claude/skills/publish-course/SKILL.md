---
name: publish-course
description: Put a built course on a public website — convert the course's Markdown into HTML pages (with rendered diagrams and header artwork), copy them into a GitHub Pages repository the educator names, link the course from the site's landing page, and push. Use when the user says publish, deploy, put online, "add it to the website", or names a GitHub Pages repo or URL. Requires a built course and access to the target repository.
---

# publish-course

Turns `course-material/<slug>/` into web pages on a site the educator controls. Read `AGENTS.md` first if you haven't. The working group's own site is `iticse26-wg11/iticse26-wg11.github.io` (a GitHub Pages "static upload" site); educators may name any repository they can push to.

## Before you start

1. `config/config.yaml` must say `status: built`. If not, offer `build-course` first.
2. Ask for (or confirm) the **target repository**: an `owner/name` or URL. Check access with `gh auth status` and `gh repo view <owner/name> --json viewerPermission`; you need write access. If `gh` is missing or not logged in, tell the educator in one sentence what to run (`gh auth login`) and stop.
3. Inspect the target before changing it: list its files and look at how it deploys (`.github/workflows/*.yml`, the Pages settings via `gh api repos/<owner/name>/pages`). Two common cases:
   - **Static upload** (a workflow that uploads the repository as-is): Markdown is *not* rendered, so convert to HTML with `scripts/publish-site.py`.
   - **Jekyll** (no workflow, or `_config.yml` present): Markdown renders on its own, but Mermaid diagrams and header images may not; converting is still the safer default.
4. Say what you'll do in two sentences (which folder you'll add, which existing file you'll edit) and get a yes before pushing. Never overwrite existing content of the site other than adding a link to the landing page.

## Steps

1. Clone the target into the scratchpad or a temp folder (never inside this repository).
2. Convert: `uv run --with markdown python3 scripts/publish-site.py course-material/<slug> <clone>/courses/<slug>` (fall back to `pip install markdown` if `uv` is missing). It writes one HTML page per Markdown file, copies the Markdown sources and `figures/` alongside, and writes a course `index.html`. Header artwork becomes a full-width hero image; Mermaid renders client-side.
3. Link the course from the landing page. If `index.html` is a placeholder or missing, write a simple landing page that names the organisation and lists the course; if it is a real page, add one list item with the course title and a one-line description, and touch nothing else. Reuse the site's existing style if it has one.
4. Check locally that every generated page has a `<title>`, that Mermaid blocks appear as `<pre class="mermaid">`, and that any `figures/art-*.jpg` referenced exists.
5. Commit in the *site* clone with a message naming the course, then push to its default branch. Wait for the deploy workflow (`gh run list --repo <owner/name> --limit 1`) and fetch the course index URL to confirm it returns 200.
6. Do **not** commit anything in this repository as part of publishing unless the educator asks.

## Republishing after a revision

Run the same conversion into the same folder; unchanged pages come out byte-identical, so the diff shows only what changed. Keep existing `figures/art-*.jpg` unless the educator asked for new artwork.

## Finish

Give the educator the live URL of the course index, list what was added to the site, and note anything the site still lacks (for example a landing page that is still a placeholder).
