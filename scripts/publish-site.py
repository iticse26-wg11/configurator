#!/usr/bin/env python3
"""Convert a built course into HTML pages for a static website.

Usage:
  uv run --with markdown python3 scripts/publish-site.py course-material/<slug> <site-clone>/courses/<slug>
  (or: pip install markdown && python3 scripts/publish-site.py ...)

Writes one .html per .md (Mermaid diagrams render client-side, header artwork
becomes a full-width hero image), copies the .md sources and figures/ alongside,
and writes an index.html for the course. Title, blurb and date are read from the
course's own files (00-overview.md H1 and "About this course", coverage.md).
The site's landing page is not touched; the publish-course skill links the course
from it. Used by GitHub Pages "static upload" sites, where Markdown is not rendered.
"""
import html, json, pathlib, re, shutil, sys

import markdown

SRC = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
overview = (SRC / "00-overview.md").read_text(encoding="utf-8")
m = re.search(r"^# (.+)$", overview, re.M); TITLE = m.group(1).strip() if m else SRC.name
m = re.search(r"^## About this course\s+(.+?)\n\n", overview, re.S | re.M); BLURB = m.group(1).strip() if m else ""
cov = (SRC / "coverage.md"); m = re.search(r"Generated (\d{4}-\d{2}-\d{2})", cov.read_text(encoding="utf-8")) if cov.exists() else None
DATE = m.group(1) if m else ""

CSS = """
:root{--fg:#1f2328;--bg:#fff;--muted:#59636e;--line:#d1d9e0;--accent:#0969da;--code:#f6f8fa}
@media (prefers-color-scheme:dark){:root{--fg:#e6edf3;--bg:#0d1117;--muted:#9198a1;--line:#3d444d;--accent:#4493f8;--code:#161b22}}
*{box-sizing:border-box}body{margin:0;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--fg);background:var(--bg)}
nav.top{border-bottom:1px solid var(--line);padding:.6rem 1rem;font-size:.9rem;color:var(--muted)}nav.top a{color:var(--accent);text-decoration:none}nav.top a:hover{text-decoration:underline}
main{max-width:880px;margin:0 auto;padding:1.5rem 1rem 4rem}
h1{font-size:1.9rem;line-height:1.25;border-bottom:1px solid var(--line);padding-bottom:.3rem}h2{margin-top:2.2rem;border-bottom:1px solid var(--line);padding-bottom:.2rem}h3{margin-top:1.6rem}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto;font-size:.93rem}th,td{border:1px solid var(--line);padding:.4rem .6rem;vertical-align:top;text-align:left}th{background:var(--code)}
code{background:var(--code);padding:.1em .3em;border-radius:4px;font-size:.9em}pre{background:var(--code);padding:.8rem;overflow-x:auto;border-radius:6px}pre code{background:none;padding:0}
pre.mermaid{background:none;text-align:center}blockquote{border-left:4px solid var(--line);margin:0;padding:.2rem 1rem;color:var(--muted)}
a{color:var(--accent)}footer{max-width:880px;margin:0 auto;padding:1rem;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem}
ul.files li{margin:.3rem 0}.cap{color:var(--muted)}
img{max-width:100%}img.hero{display:block;width:100%;max-height:420px;object-fit:cover;border-radius:10px;margin:.5rem 0 1.5rem;box-shadow:0 8px 30px rgba(0,0,0,.25)}
"""

TEMPLATE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{css}</style></head><body>
<nav class="top">{crumbs}</nav>
<main>{body}</main>
<footer>{footer}</footer>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad:true,theme:window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'default'}});</script>
</body></html>"""

FOOTER = ('Built with the <a href="https://github.com/iticse26-wg11/configurator">GenAI Course Configurator</a> by ITiCSE 2026 Working Group 11, '
          "from the shared ILO and activity libraries. Every outcome and activity is cited by id.")

def convert(md_text):
    def fence(mm):  # mermaid fences -> raw <pre class="mermaid"> blocks, kept verbatim
        return "\n<pre class=\"mermaid\">\n" + mm.group(1).replace("<br>", "<br/>") + "\n</pre>\n"
    md_text = re.sub(r"```mermaid\n(.*?)\n```", fence, md_text, flags=re.S)
    md_text = re.sub(r"\]\(([^)]+?)\.md(#[^)]*)?\)", r"](\1.html\2)", md_text)  # .md links -> .html
    out = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])
    return re.sub(r'<p><img alt="([^"]*)" src="([^"]*figures/art-[^"]+)" /></p>', r'<img class="hero" alt="\1" src="\2">', out)

def first_h1(md_text):
    mm = re.search(r"^# (.+)$", md_text, re.M); return mm.group(1).strip() if mm else TITLE

if (SRC / "figures").is_dir():
    shutil.copytree(SRC / "figures", OUT / "figures", dirs_exist_ok=True)

files = sorted(p for p in SRC.rglob("*.md") if p.name != "README.md")
for p in files:
    rel = p.relative_to(SRC); dest = OUT / rel.with_suffix(".html"); dest.parent.mkdir(parents=True, exist_ok=True)
    text = p.read_text(encoding="utf-8"); up = "../" * (len(rel.parts) - 1)
    crumbs = (f'<a href="{up}../../index.html">Home</a> › <a href="{up}index.html">{html.escape(TITLE)}</a> › '
              f'{html.escape(first_h1(text))} · <a href="{rel.name}">Markdown source</a>')
    dest.write_text(TEMPLATE.format(title=html.escape(first_h1(text)) + " · " + html.escape(TITLE), css=CSS, crumbs=crumbs,
                                    body=convert(text), footer=FOOTER), encoding="utf-8")
    shutil.copy(p, dest.with_suffix(".md"))

def li(p, label=None):
    rel = p.relative_to(SRC).with_suffix(".html"); label = label or first_h1(p.read_text(encoding="utf-8"))
    return f'<li><a href="{rel}">{html.escape(label)}</a></li>'

def section(title, items):
    return f"<h2>{title}</h2><ul class=\"files\">{''.join(items)}</ul>" if items else ""

by_dir = lambda d: [p for p in files if p.parent.name == d]
spec_file = SRC / "figures" / "artwork.json"
alts = {k: v.get("alt", "") for k, v in json.loads(spec_file.read_text(encoding="utf-8")).get("pages", {}).items()} if spec_file.exists() else {}
hero = next((f'<img class="hero" alt="{html.escape(alts.get(k, ""))}" src="figures/art-{k}.jpg">'
             for k in ("index", "overview") if (OUT / "figures" / f"art-{k}.jpg").exists()), "")
start = [li(SRC / "00-overview.md", "Course overview: description, learning outcomes, schedule, policies, assessment")]
for name, label in [("instructor-guide.md", "Instructor guide: what to prepare, facilitation tips, what to cut if short on time"),
                    ("coverage.md", "Coverage report: every outcome traced to where it is taught, practised and assessed"),
                    ("CHANGELOG.md", "Change log: revisions made after the first build")]:
    if (SRC / name).exists(): start.append(li(SRC / name, label))
body = f"""<h1>{html.escape(TITLE)}</h1>
{hero}
<p class="cap">{html.escape(BLURB)}</p>
<p>Generated{' on ' + DATE if DATE else ''} with the <a href="https://github.com/iticse26-wg11/configurator">GenAI Course Configurator</a> by ITiCSE 2026 Working Group 11. Every learning outcome is quoted from the working group's intended learning outcomes and every activity is adapted from its activity library, cited by id. Each page links to its Markdown source for editing.</p>
{section("Start here", start)}
{section("Sessions", [li(p) for p in by_dir("sessions")])}
{section("Student handouts", [li(p) for p in by_dir("student-handouts")])}
{section("Assessment", [li(p) for p in by_dir("assessment")])}
"""
(OUT / "index.html").write_text(TEMPLATE.format(title=html.escape(TITLE), css=CSS, crumbs=f'<a href="../../index.html">Home</a> › {html.escape(TITLE)}',
                                                body=body, footer=FOOTER), encoding="utf-8")
print(f"wrote {len(files)} pages + index for '{TITLE}' → {OUT}")
