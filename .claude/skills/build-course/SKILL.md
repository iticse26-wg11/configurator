---
name: build-course
description: Generate a complete GenAI literacy course as markdown files under course-material/ from config/config.yaml, the ILO library, the activity library and the educator's attachments — course overview with schedule, one file per session (presentation outline, speaker notes, activities adapted to the setting), assessment items where configured, an instructor guide, and an ILO coverage report. Use when the user says build, generate, create, produce, or "make the course", or when config status is `configured`.
---

# build-course

Turns a configuration into teachable material. Read `AGENTS.md` first if you haven't — its five content ground rules are non-negotiable here. Templates for each output file are in `templates/` next to this skill; use their structure.

## 1. Load everything

- `config/config.yaml` — refuse politely if `status: empty` (offer `configure-course`). If `status: built`, ask: rebuild from scratch, or should they use `revise-course`? Confirm before overwriting a folder they may have edited.
- `config/topics.yaml` — resolve the selected topics/sub-topics/exclusions into a **selected ILO set**.
- `intended-learning-outcomes/ilos.yaml` — exact wording for each selected ILO.
- `learning-activities/activities/*.md` — read frontmatter for all 15; read the full body of every activity whose `related_ilos` intersects the selected set.
- Every file in `attachments[]` — read in full. Note the concrete rules/terms you must reflect.
- Run `python3 scripts/validate-config.py` if PyYAML is present. Stop and fix on errors.

If a submodule folder is empty, run `git submodule update --init` first.

## 2. Compute the time budget

```
contact   = time.total_hours × 60                (minutes)
present   = contact × time.presentation_share
activity  = contact − present
homework  = time.homework_hours × 60
```

Per topic: `share = weight / Σ weights`; `present_t = present × share`; `activity_t = activity × share`. Within a topic, split across selected sub-topics in proportion to their ILO count. Round to 5-minute blocks and keep a running remainder so totals still add up exactly.

## 3. Select and fit activities

For each topic, walk its selected ILOs and pick activities from the library:

1. **Candidates**: activities whose `related_ilos` intersect the topic's selected ILOs.
2. **Filter by hard constraints** from `course.*` and `preferences.*`: delivery mode (an `Unplugged` activity in an online course needs adaptation or replacement), `tools_available` (drop/adapt activities needing tools they don't have, e.g. LA09 needs Colab + a 7B model), class size vs. `scale`, `constraints` (e.g. "no paid accounts").
3. **Rank** by selected-ILOs-covered per minute; take greedily until `activity_t` is spent.
4. **Fitting**: if the best candidate exceeds the remaining budget by ≤ 30 %, include a **shortened adaptation** and label it (`Adapted from LA07 — shortened to 30 min: fewer sampling rounds`). If it exceeds by more, either move its pre-work into `homework` (if the source allows a pre-sessional part, e.g. LA12, LA14) or replace it with a *mini-activity* you design that explicitly targets the ILO, labelled as `Generated (no library activity fits): …`. Generated mini-activities are last resort and must be listed in `coverage.md`.
5. **Sequencing constraints** from the library: LA10 (mindmap) splits into first and last session; LA09 assumes LA07 before it; LA13 assumes MM01/MM02/EPR05/CS02 taught first; LA14 assumes CS01–CS03. Respect these when ordering sessions.
6. **Assessment-bearing activities** (LA08, LA11, LA14, LA15) are preferred when `assessment.include` is true and the ILO is in scope.

Any selected ILO with no activity after this step is recorded as *presentation-only* in `coverage.md` with the reason (budget, constraints, no library match).

## 4. Plan sessions

Chunk the budget into sessions of `course.session_length_minutes` (last one may be shorter). Keep each session on one topic where possible; order topics H → MM → CS → EPR unless weights or prerequisites argue otherwise (EPR discussion activities land better after students have a mental model). Each session gets: opening (≤ 5 min), presentation blocks, activities, wrap-up (≤ 5 min). Sum every session's blocks; the grand total **must** equal `contact`. Show the per-session table in `00-overview.md`.

Homework minutes go to pre-sessional parts of activities (LA12, LA14), the pre/post mindmap, reflections, and reading from `reading` attachments.

## 5. Assessment (if `assessment.include`)

Resolve `assessment.scope` to an ILO set. For each ILO in scope: first reuse the built-in assessment of a selected activity, then generate items in the requested `formats` — a quiz item (with answer and which misconception it probes), a reflection prompt (with what a good answer shows), or a short project/presentation brief (with a 3–4 criterion rubric). Every item names the ILO id it assesses. Put them in `assessment/` and reference them from the relevant session file. State `grade_share` in the overview if set.

## 6. Apply attachments and preferences

- `policy` attachments: summarise the rules in `00-overview.md` → *Policies*; add a "check the policy" step to every activity where students use GenAI tools; use as the "provided policy" in LA03/LA11-derived activities. Quote the policy's actual wording where students need it.
- `syllabus`: align titles, terminology and scope; mention anything in the config that the syllabus contradicts.
- `reading`: place as recommended reading per session; do not add outside readings unless `how_to_use` allows.
- `example`: match structure/tone; reuse content where licensed/appropriate and say where.
- `how_to_use` text overrides these defaults. Record where each attachment was applied in `coverage.md` → *Attachments*.
- Write everything in `course.language`, in `preferences.tone`, pitched at `preferences.prior_knowledge`. Name only tools from `preferences.tools_available` in student-facing instructions.

## 7. Write the files

Course slug: kebab-case of `course.title` (max ~6 words). Output to `course-material/<slug>/`:

```
00-overview.md            syllabus: description, audience, ILOs (exact wording), schedule table,
                          policies, assessment summary, reading — template: templates/overview.md
sessions/NN-<slug>.md     one per session — template: templates/session.md
assessment/               only if assessment.include — template: templates/assessment.md
instructor-guide.md       prep checklist, materials to print/prepare, timing tips, common pitfalls,
                          how each attachment was used — template: templates/instructor-guide.md
student-handouts/         only if preferences.output.student_handouts — one per activity needing
                          a worksheet or brief (from the activity's Resources list)
coverage.md               ILO → session / activity / assessment; presentation-only ILOs and why;
                          excluded ILOs; adaptations; attachments — template: templates/coverage.md
```

Toggle speaker notes / slide outlines per `preferences.output`. Use the templates' headings verbatim so `revise-course` can find sections later.

Finally set `status: built` in `config/config.yaml`.

## 8. Report

Tell the educator, in plain language: where the course is, the session list with minutes, which library activities were used (ids + names), anything adapted or generated, any ILO that ended up presentation-only, and how each attachment was applied. Then offer `revise-course` for changes. Don't paste file contents unless asked.
