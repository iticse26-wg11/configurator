---
name: configure-course
description: Interview an educator in plain language to set up a GenAI literacy course — which topics and how much weight (CFG01–02), how much time and how it splits between presentation and activities (CFG03–04), whether and what to assess (CFG05–06), and audience/tone/tool preferences (CFG08) — and write the result to config/config.yaml. Use when the user wants to start, set up, plan, configure or change the shape of a course, or when config status is `empty`.
---

# configure-course

Turn a conversation with a (non-technical) educator into a complete `config/config.yaml`. Read `AGENTS.md` first if you haven't; its "who you are working with" rules apply throughout.

## Before you start

1. Read `config/config.yaml`. If `status` is not `empty`, say what's already configured (title, topics, hours) and ask whether to **adjust** it or **start over**. Adjusting = only ask about what they want changed; starting over = full interview, and confirm before wiping.
2. Read `config/topics.yaml` — you'll present its `summary` lines to the educator, never raw ILO wording unless they ask.
3. Optionally skim `config/examples/one-day-workshop.yaml` to calibrate what a finished config looks like.

## The interview

One question at a time. Recommended option first. Accept free-text answers and map them yourself. After every 2–3 answers, briefly read back what you've recorded so far. Keep total questions under ~12 for a default path — offer "use sensible defaults for the rest" after the essentials.

### Step 1 — Context (feeds CFG08)
- Course title (suggest one if they hesitate).
- Who the students are: programme, year, rough size. → `course.audience`, `course.class_size`, `course.level`.
- Delivery: in person / online / hybrid; typical session length. → `course.delivery`, `course.session_length_minutes`.
- Language of instruction. → `course.language`.

### Step 2 — Topics (CFG01)
Present the four topic areas using the `summary` from `topics.yaml`, as a multi-select. Then for each chosen area, ask whether they want *all* of it or a subset — show the sub-topic names + summaries. Record `subtopics: all` or the list of ids. If they want to drop a specific outcome inside a sub-topic, put it in `exclude_ilos`.

If they're unsure, recommend: MM + EPR for a general audience; add CS for programming-focused courses; H is a good 45-minute opener.

### Step 3 — Relative importance (CFG02)
Ask, per chosen topic, how central it is on a 1–5 scale — or accept phrases ("mostly ethics, a bit of history") and translate: *central* = 5, *important* = 4, *standard* = 3, *brief* = 2, *touch on* = 1. Read the weights back as approximate percentages of course time so they can sanity-check (weight / sum of weights).

### Step 4 — Time (CFG03, CFG04)
- Total contact hours (accept "one afternoon", "a 2-hour session a week for 6 weeks" → compute and confirm). → `time.total_hours`.
- Any expected out-of-class time (pre-reading, homework)? → `time.homework_hours` (default 0).
- Balance between instructor presentation and student activities. Offer: *activity-heavy* (30% presentation), *balanced* (50%), *lecture-leaning* (70%). → `time.presentation_share`.

Sanity-check against the library: sum the durations of activities relevant to their chosen ILOs (from `learning-activities/activities/*.md` frontmatter) and, if the activity budget is far below what full coverage needs, say so now ("with 2 hours and 4 topics, activities will need to be shortened or dropped — fine, but you should know") rather than at build time.

### Step 5 — Assessment (CFG05, CFG06)
- Include assessment? → `assessment.include`.
- If yes: which topics/sub-topics (default: all selected) → `assessment.scope`; formative only, or also graded/summative → `assessment.types`; preferred formats (quiz, reflection, short project, presentation) → `assessment.formats`; share of module grade if any → `assessment.grade_share`.

### Step 6 — Preferences (CFG08)
- Tone and style (offer 2–3 options). → `preferences.tone`.
- What students already know (GenAI use, programming). → `preferences.prior_knowledge`.
- Which GenAI tools students can actually use in class (free/paid/licensed/local). → `preferences.tools_available`. This is a hard constraint on activity selection — say so.
- Any other constraints: room, accessibility, no paid accounts, must be printable, etc. → `preferences.constraints`.
- Which outputs they want (speaker notes, slide outlines, student handouts, instructor guide) — default all on. → `preferences.output.*`.

### Step 7 — Attachments (hand-off to CFG07)
Ask whether they have documents the course should follow or use — institutional GenAI policy, existing syllabus, reading list. If yes, say you'll collect them next and invoke `gather-sources` after saving. Don't collect them inside this skill.

## Writing the config

- Write the full `config/config.yaml` matching the template structure exactly (keep the comments from the template where practical; they help maintainers). Set `status: configured`.
- Validate: run `python3 scripts/validate-config.py`. If PyYAML is missing, check the rules in that script's docstring by reading the files yourself. Fix problems silently where the fix is obvious; ask where it isn't.
- Show the educator a short plain-language summary — title, topics with approximate time share, hours and split, assessment yes/no and scope, key constraints — and ask for a final OK. Do **not** show the YAML unless asked.

## Finish

Tell them what's next in one line: attachments (`gather-sources`) if they mentioned any, otherwise building the course (`build-course`). Offer to go straight on.
