#!/usr/bin/env python3
"""Generate header artwork for a built course with an image-generation API.

Usage:
  python3 scripts/make-artwork.py course-material/<slug> [--insert] [--force] [--only name,name]

Reads <course>/figures/artwork.json, written by the build-course skill:

  {
    "style": "one paragraph of shared style directions, appended to every prompt",
    "pages": {
      "overview": {"file": "00-overview.md", "alt": "one-sentence description", "prompt": "the scene"},
      "session1": {"file": "sessions/01-....md", "alt": "...", "prompt": "..."}
    }
  }

For every page it writes <course>/figures/art-<name>.jpg (kept if it already
exists, unless --force). With --insert it also places
`![alt](figures/art-<name>.jpg)` directly under the page's H1 when no header
artwork is there yet, so the image shows on GitHub and on a published site.

Needs OPENAI_API_KEY in the environment (model gpt-image-1). Without a key the
script exits with code 3 and a one-line message; the course is complete without
artwork, so callers should treat that as "skip", not as an error. Standard
library only; four requests run at once; each image costs a few cents.
"""
import base64, json, os, pathlib, re, sys, time, urllib.request, concurrent.futures as cf

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if not args:
    sys.exit(__doc__)
course = pathlib.Path(args[0]); force = "--force" in sys.argv; insert = "--insert" in sys.argv
only = next((a.split("=", 1)[1].split(",") for a in sys.argv if a.startswith("--only=")), None)
FIG = course / "figures"; spec_path = FIG / "artwork.json"
if not spec_path.exists():
    sys.exit(f"make-artwork: {spec_path} not found; the build-course skill writes it (see docstring).")
spec = json.loads(spec_path.read_text(encoding="utf-8"))
STYLE = spec.get("style", "").strip()
PAGES = {k: v for k, v in spec["pages"].items() if not only or k in only}

KEY = os.environ.get("OPENAI_API_KEY")
if not KEY:
    print("make-artwork: OPENAI_API_KEY is not set; skipping artwork (the course is complete without it).")
    sys.exit(3)

def generate(name, page):
    dest = FIG / f"art-{name}.jpg"
    if dest.exists() and not force:
        return name, "kept"
    body = json.dumps({"model": "gpt-image-1", "prompt": page["prompt"].strip() + "\n\n" + STYLE, "size": "1536x1024",
                       "quality": "medium", "output_format": "jpeg", "output_compression": 82, "n": 1}).encode()
    for attempt in range(3):
        try:
            req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=body,
                                         headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=300) as r:
                data = json.load(r)
            dest.write_bytes(base64.b64decode(data["data"][0]["b64_json"]))
            return name, f"ok {dest.stat().st_size // 1024} KB"
        except Exception as e:  # noqa: BLE001
            err = getattr(e, "read", lambda: b"")()[:300]
            if attempt == 2:
                return name, f"FAILED {e} {err!r}"
            time.sleep(5 * (attempt + 1))

def insert_image(name, page):
    if not page.get("file"):
        return "no file"
    p = course / page["file"]
    if not p.exists():
        return f"missing {page['file']}"
    text = p.read_text(encoding="utf-8")
    if "figures/art-" in text:
        return "already has artwork"
    depth = len(pathlib.Path(page["file"]).parts) - 1
    rel = "../" * depth + f"figures/art-{name}.jpg"
    new = re.sub(r"^(# .+\n)", lambda m: m.group(1) + f"\n![{page.get('alt', '')}]({rel})\n", text, count=1, flags=re.M)
    p.write_text(new, encoding="utf-8")
    return "inserted"

failed = 0
with cf.ThreadPoolExecutor(4) as ex:
    for name, status in ex.map(lambda kv: generate(*kv), PAGES.items()):
        note = ""
        if insert and not status.startswith("FAILED"):
            note = " · " + insert_image(name, PAGES[name])
        failed += status.startswith("FAILED")
        print(f"{name:18s} {status}{note}", flush=True)
sys.exit(1 if failed else 0)
