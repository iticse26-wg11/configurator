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
4. **Fitting** — prefer the library, always. If the best candidate is longer than the remaining budget, ask one question: *does the activity's core mechanic survive at the shorter length?* (The timeline reveal, the dice-driven sampling, the hidden-vs-revealed decision tree, the policy comparison.) If yes, include a **shortened adaptation**, however deep the cut, and label it precisely (`Adapted from LA01 — condensed 45 → 15 min: 8 cards, single whole-class reveal`). If the mechanic doesn't survive, move its pre-sessional part into `homework` where the source has one (LA12, LA14), or take a *part* of it (LA10 part 1 in class, part 2 as homework). Only when nothing in the library targets the ILO at all do you design a *mini-activity*, labelled `Generated (no library activity fits): …`. Every adaptation and every generated item is listed in `coverage.md` with the reason. Don't apply a fixed percentage threshold — the example build showed a 3× condensed library activity beats an invented one.
5. **Sequencing constraints** from the library: LA10 (mindmap) splits into first and last session; LA09 assumes LA07 before it; LA13 assumes MM01/MM02/EPR05/CS02 taught first; LA14 assumes CS01–CS03. Respect these when ordering sessions.
6. **Assessment-bearing activities** (LA08, LA11, LA14, LA15) are preferred when `assessment.include` is true and the ILO is in scope.

Any selected ILO with no activity after this step is recorded as *presentation-only* in `coverage.md` with the reason (budget, constraints, no library match).

## 4. Plan sessions

**Activities are lumpy; presentation is fluid.** Place activities first, then let presentation fill the remaining minutes of each session. The per-topic budgets from step 2 are *targets* for activity selection, not per-session quotas — what must add up exactly is the **per-session timeline** and the **grand total**.

1. Chunk the budget into sessions of `course.session_length_minutes` (last one may be shorter). Keep each session on one or two topics; order H → MM → CS → EPR unless weights or prerequisites argue otherwise (EPR discussion activities land better after students have a mental model).
2. Place the selected activities into sessions, respecting the sequencing constraints from step 3 and contiguity (a 45-min activity needs 45 contiguous minutes — never split one across a break).
3. Fill each session's remaining minutes with presentation blocks for that session's ILOs, plus an opening (≤ 5 min) and a closing (≤ 5 min; may be folded into an activity's closing discussion). Every ILO that has no activity must get a named presentation block.
4. Sum every session's blocks; the grand total **must** equal `contact`, and the presentation/activity split must be within one 5-minute block of the configured split. Show the per-session table in `00-overview.md` and reconcile the numbers in `coverage.md`. Before writing files, verify the timeline arithmetic (a quick script over the timeline tables is fine).

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

## 7. Visual elements (student-facing files)

Handouts, the overview and student-facing activity steps get diagrams where the concept is structural — a process, a split, a timeline, a decision. Use Mermaid fenced blocks (they render on GitHub, VS Code and most VLEs; no image tooling; editable by the educator). Ready snippets for the recurring concepts — generation loop, model pipeline, augmentation/substitution quadrant, verification flow, reliable/trustworthy/responsible, history timeline, mindmap starter, course-at-a-glance — are in `templates/visuals.md`; adapt them to the course's wording rather than inventing new ones. Rules: ≤ 12 nodes; default styling (theme-safe); a one-line italic caption after each; reuse library figures by copying them into `<course>/figures/`; never link external images. Slide outlines are instructor-facing — mark figure cues there as `[figure: …]` rather than embedding diagrams. Target: the overview has the course-at-a-glance timeline; every handout has one figure that does work.

### 7b. Header artwork (optional, needs an image-generation key)

Each page can open with one illustration that sets its tone. This is optional: the course is complete without it, and many educators will have no API key. Do it when `OPENAI_API_KEY` is set in the environment (check with `[ -n "$OPENAI_API_KEY" ]`); otherwise skip silently and mention in the report that artwork can be added later.

1. Write `course-material/<slug>/figures/artwork.json`: a shared `style` paragraph (medium, palette, mood; always end with "No text, no letters, no logos, no watermarks, no realistic faces") and one entry per page under `pages` — key, `file` (path relative to the course folder; `null` for the site index image), a one-sentence `alt`, and a `prompt` describing a *scene that embodies the page's idea*, not a diagram of it (a river of word tiles and a die for next-word prediction; roots under a speech bubble for resources and labour; a fractured mirror for unreliable outputs). Keep prompts to one or two sentences and vary the motifs across pages so the set feels like one illustrated book. The demo course's `figures/artwork.json` is a worked example.
2. Run `python3 scripts/make-artwork.py course-material/<slug> --insert`. It generates `figures/art-<key>.jpg` (about 300 KB each, a few cents each) and places `![alt](figures/art-<key>.jpg)` directly under each page's H1. Exit code 3 means no key: skip. A `FAILED` line means one image did not come through: re-run with `--only=<key>` or leave that page without artwork and say so.
3. Look at two or three of the images (the `Read` tool shows them) before reporting; regenerate any that contain text or drift from the style with `--force --only=<key>`.

Artwork lives in `figures/` with the course so it renders on GitHub and travels with the Markdown; never link images from external sites.

## 8. Write the files

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
figures/                  header artwork (art-*.jpg + artwork.json) if generated in step 7b; library figures copied here
```

Toggle speaker notes / slide outlines per `preferences.output`. Use the templates' headings verbatim so `revise-course` can find sections later.

Finally set `status: built` in `config/config.yaml`.

## 9. Report

Tell the educator, in plain language: where the course is, the session list with minutes, which library activities were used (ids + names), anything adapted or generated, any ILO that ended up presentation-only, and how each attachment was applied.

Then state the **preparation burden** explicitly — this is the thing a non-technical educator most needs to hear before the day: which activities require material the instructor must *create* (not just print), with a rough time estimate. From the library: LA07 needs ~5 one-page training texts in different genres and a tested n-gram table (~1–2 h); LA06 needs 10 pre-generated outputs with planted errors (~1 h); LA11 needs case cards and 1–2-page policy summaries (~1–2 h); LA02 needs a scenario plus a custom GPT/knowledge base (~1 h); LA15 needs a pipeline diagram and worksheet (~1 h); LA01 needs milestone cards (~30 min). Put the same list at the top of `instructor-guide.md` under *Before the course* with the estimates, so it isn't buried.

Mention whether header artwork was generated (and if not, that it can be added later with an image-generation key), and that `publish-course` can put the course on a website.

Finally offer `revise-course` for changes — including swapping out a high-prep activity if the estimate is a problem. Don't paste file contents unless asked.
