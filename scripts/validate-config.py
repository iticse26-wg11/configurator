#!/usr/bin/env python3
"""Validate a course configuration against the topic tree and ILO library.

Usage: python3 scripts/validate-config.py [config/config.yaml]

Rules checked (agents without PyYAML: verify these by reading the files):
  1. config parses; `version` is 1; `status` in {empty, configured, built}.
  2. If status != empty: course.title, time.total_hours (> 0),
     time.presentation_share (0..1), assessment.include (bool) are set,
     and at least one topic is selected.
  3. Every topics[].id exists in config/topics.yaml; weight is an int 1..5;
     subtopics is `all` or a list of sub-topic ids belonging to that topic;
     exclude_ilos only names ILOs inside the selected sub-topics.
  4. assessment.scope is `all` or a list of topic / sub-topic / ILO ids that
     are all within the selected set.
  5. Every attachments[].path exists; kind is one of the allowed kinds;
     how_to_use is non-empty; applies_to is `all` or a list of known ids.
  6. Consistency of the libraries themselves: every ILO in topics.yaml exists
     in ilos.yaml and every ILO in ilos.yaml appears exactly once in
     topics.yaml; every activity's related_ilos resolve.
Exit code 0 = valid (warnings allowed), 1 = errors.
"""
import glob
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "validate-config: PyYAML is not installed (pip install pyyaml).\n"
        "Fall back to checking the rules listed in this script's docstring by hand.\n")
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KINDS = {"policy", "syllabus", "reading", "example", "dataset", "other"}
STATUSES = {"empty", "configured", "built"}
errors, warnings = [], []
err = errors.append
warn = warnings.append


def load(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return yaml.safe_load(f)


def frontmatter(path):
    with open(path, encoding="utf-8") as f:
        m = re.match(r"\A---\n(.*?)\n---", f.read(), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


# --- libraries ---------------------------------------------------------------
ilo_path = "intended-learning-outcomes/ilos.yaml"
act_glob = "learning-activities/activities/*.md"
if not os.path.exists(os.path.join(ROOT, ilo_path)):
    err(f"{ilo_path} missing — run `git submodule update --init`")
    print("\n".join("ERROR: " + e for e in errors)); sys.exit(1)

ilos = {i["id"] for i in load(ilo_path)["ilos"]}
topics = load("config/topics.yaml")["topics"]
topic_ids = {t["id"] for t in topics}
sub_of = {}          # subtopic id -> topic id
sub_ilos = {}        # subtopic id -> set of ILO ids
seen = {}
for t in topics:
    for s in t.get("subtopics", []):
        sub_of[s["id"]] = t["id"]
        sub_ilos[s["id"]] = set(s["ilos"])
        for i in s["ilos"]:
            if i not in ilos:
                err(f"topics.yaml: {s['id']} lists unknown ILO {i}")
            seen[i] = seen.get(i, 0) + 1
for i in sorted(ilos):
    if seen.get(i, 0) != 1:
        err(f"topics.yaml: ILO {i} appears {seen.get(i, 0)} times (expected 1)")

activity_ids = set()
for p in glob.glob(os.path.join(ROOT, act_glob)):
    fm = frontmatter(p)
    activity_ids.add(fm.get("id"))
    for i in fm.get("related_ilos", []):
        if i not in ilos:
            err(f"{os.path.relpath(p, ROOT)}: related ILO {i} not in ilos.yaml")
if not activity_ids:
    err(f"no activities found at {act_glob} — run `git submodule update --init`")

known_ids = topic_ids | set(sub_of) | ilos | activity_ids

# --- config ------------------------------------------------------------------
cfg_path = sys.argv[1] if len(sys.argv) > 1 else "config/config.yaml"
try:
    cfg = load(cfg_path) or {}
except Exception as e:  # noqa: BLE001
    err(f"{cfg_path}: cannot parse ({e})")
    print("\n".join("ERROR: " + e for e in errors)); sys.exit(1)

if cfg.get("version") != 1:
    err("version must be 1")
status = cfg.get("status")
if status not in STATUSES:
    err(f"status must be one of {sorted(STATUSES)}, got {status!r}")

selected_ilos = set()
if status != "empty":
    course = cfg.get("course") or {}
    if not course.get("title"):
        err("course.title is required")
    time = cfg.get("time") or {}
    th = time.get("total_hours")
    if not isinstance(th, (int, float)) or th <= 0:
        err("time.total_hours must be a positive number")
    ps = time.get("presentation_share")
    if not isinstance(ps, (int, float)) or not 0 <= ps <= 1:
        err("time.presentation_share must be between 0 and 1")
    if (time.get("homework_hours") or 0) < 0:
        err("time.homework_hours cannot be negative")
    if not isinstance((cfg.get("assessment") or {}).get("include"), bool):
        err("assessment.include must be true or false")

    tlist = cfg.get("topics") or []
    if not tlist:
        err("at least one topic must be selected")
    for t in tlist:
        tid = t.get("id")
        if tid not in topic_ids:
            err(f"topics: unknown topic id {tid!r}"); continue
        w = t.get("weight")
        if not isinstance(w, int) or not 1 <= w <= 5:
            err(f"topics[{tid}].weight must be an integer 1..5")
        subs = t.get("subtopics", "all")
        if subs == "all":
            chosen = {s for s, top in sub_of.items() if top == tid}
        elif isinstance(subs, list):
            chosen = set()
            for s in subs:
                if sub_of.get(s) != tid:
                    err(f"topics[{tid}].subtopics: {s!r} is not a sub-topic of {tid}")
                else:
                    chosen.add(s)
        else:
            err(f"topics[{tid}].subtopics must be 'all' or a list"); chosen = set()
        t_ilos = set().union(*(sub_ilos[s] for s in chosen)) if chosen else set()
        for i in t.get("exclude_ilos") or []:
            if i not in t_ilos:
                warn(f"topics[{tid}].exclude_ilos: {i} is not among the selected sub-topics (no effect)")
        selected_ilos |= t_ilos - set(t.get("exclude_ilos") or [])
    if tlist and not selected_ilos:
        err("selection resolves to zero ILOs")

    scope = (cfg.get("assessment") or {}).get("scope", "all")
    if scope != "all":
        if not isinstance(scope, list):
            err("assessment.scope must be 'all' or a list")
        else:
            sel_topics = {t.get("id") for t in tlist}
            for s in scope:
                if s in topic_ids:
                    ok = s in sel_topics
                elif s in sub_of:
                    ok = bool(sub_ilos[s] & selected_ilos)
                elif s in ilos:
                    ok = s in selected_ilos
                else:
                    err(f"assessment.scope: unknown id {s!r}"); continue
                if not ok:
                    warn(f"assessment.scope: {s} is not part of the selected content")

for n, a in enumerate(cfg.get("attachments") or []):
    p = a.get("path", "")
    if not p or not os.path.exists(os.path.join(ROOT, p)):
        err(f"attachments[{n}].path {p!r} does not exist")
    if a.get("kind") not in KINDS:
        err(f"attachments[{n}].kind must be one of {sorted(KINDS)}")
    if not (a.get("how_to_use") or "").strip():
        err(f"attachments[{n}].how_to_use is required")
    ap = a.get("applies_to", "all")
    if ap != "all":
        for x in (ap if isinstance(ap, list) else [ap]):
            if x not in known_ids:
                err(f"attachments[{n}].applies_to: unknown id {x!r}")

# --- report ------------------------------------------------------------------
for w in warnings:
    print("WARNING:", w)
for e in errors:
    print("ERROR:", e)
if errors:
    sys.exit(1)
n = len(selected_ilos)
print(f"OK: {cfg_path} (status={status}, {n} ILO{'s' if n != 1 else ''} selected)")
