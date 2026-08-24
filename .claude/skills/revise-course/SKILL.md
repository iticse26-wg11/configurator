---
name: revise-course
description: Take a plain-language change request about an already built course — "make session 2 shorter", "drop the history part", "add our new policy", "make it more hands-on", "we now have 8 hours not 6" — decide whether it changes the configuration, the generated material, or both, and apply the smallest change that satisfies it, regenerating only affected files. Use when config status is `built` and the user wants something different.
---

# revise-course

Implements the iterative side of CFG08: adapt the course to changed preferences without starting over. Read `AGENTS.md` first if you haven't; the build rules in `.claude/skills/build-course/SKILL.md` still apply to anything you regenerate.

## Classify the request

Read `config/config.yaml` and `course-material/<slug>/coverage.md` (the build's traceability record), then decide:

| Request type | Example | What changes |
|--------------|---------|--------------|
| **Configuration** | more/less time, add/drop topic, change weights, add assessment, new attachment, different tools | Update `config.yaml`, then rebuild affected sessions (often all, if time or weights changed). |
| **Material only** | reword, more examples, change the order of two activities, different scenario in an activity, tone tweak in one file | Edit the generated files directly. No config change. |
| **Both** | "make it more hands-on" (→ `presentation_share` down **and** regenerate) | Update config, regenerate affected files. |

If the request is ambiguous between a small local edit and a structural change, ask one question: "Do you want me to change just this session, or the balance across the whole course?"

## Apply the smallest sufficient change

1. Say in one or two sentences what you'll change and which files are affected. Get a yes if any previously generated file they might have edited will be overwritten. (Check `git status`/`git diff` on `course-material/` for hand edits; if present, preserve them or ask.)
2. Edit `config.yaml` if needed; run `python3 scripts/validate-config.py` when available.
3. Regenerate only what depends on the change, following `build-course` for those files. Keep unaffected files byte-identical. Always regenerate `coverage.md` and the schedule in `00-overview.md` if timing, topics, activities or assessment changed.
4. Keep the time budget honest: after any change, re-total the schedule and show the educator the new totals.
5. Set `status: built` and append a dated line to `course-material/<slug>/CHANGELOG.md` describing the revision (create the file on first revision).

## Finish

Summarise what changed in plain language, list the files touched, and state the new time totals. Offer a follow-up only if the change created a gap (e.g. an ILO now has no activity — say so and offer options).
