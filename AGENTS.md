# Course Configurator — agent grounding

This repository lets an **educator with no technical background** configure and generate a generative-AI-literacy course for computing students, by talking to an AI assistant. It was built by ITiCSE 2026 Working Group 11. Read this file before doing anything in the repo.

## Who you are working with

Assume the user is a university teacher, not a developer. They may never have used a terminal before this session. Consequences:

- Speak plainly. No git, YAML, shell or repo jargon unless they use it first. Say "your course settings", not "config.yaml"; "the activity library", not "the submodule".
- Ask **one question at a time**, offer sensible defaults, and accept vague answers ("about a day", "mostly ethics") — translate them into precise settings yourself and read the result back for confirmation.
- Never ask them to edit a file. You write files; they answer questions and review results.
- Before overwriting anything they may have edited (settings, generated course files, their attachments), say what will change and get a yes.
- When something fails (missing tool, empty folder), fix it or explain in one sentence what they should do — don't show stack traces.

## What the repo contains

| Path | Role |
|------|------|
| `intended-learning-outcomes/` | **Content library (git submodule).** `ilos.yaml` is the authoritative list of 32 intended learning outcomes (ILOs) in four areas: History (H), Mental Models (MM), Ethics/Policy/Regulations (EPR), Computer Science (CS). |
| `learning-activities/` | **Content library (git submodule).** 15 activities, `activities/LA<NN>/README.md` (plus `expanded.md` and `figures/` for some), each with YAML frontmatter (`id`, `related_ilos`, `duration`, `setting`, `grouping`, `mode`, `assessment`, …). `ilo-coverage.md` maps ILOs ↔ activities. |
| `config/topics.yaml` | Topic → sub-topic → ILO tree shown to educators when choosing content. |
| `config/config.yaml` | The educator's course settings (CFG01–CFG08). `config/README.md` documents every field. |
| `config/examples/` | Complete example configurations. |
| `course-resources/` | Educator-supplied attachments (policies, syllabi, readings) referenced from `config.yaml`. |
| `course-material/` | **Generated output.** One folder per built course. |
| `scripts/` | `validate-config.py` (config checks), `make-artwork.py` (optional header images, needs `OPENAI_API_KEY`), `publish-site.py` (Markdown → HTML for a static website), `update-content.sh` (maintainers: refresh content libraries). |
| `.claude/skills/` | The five workflows below, as skill files. Other agents: read and follow them as procedures. |

**If `intended-learning-outcomes/` or `learning-activities/` is empty**, the submodules were not fetched. Run `git submodule update --init` and tell the user "fetching the content library" — nothing more.

## Ground rules for content

1. **Never invent ILOs or activities.** Every learning outcome in a generated course must be one of the 32 in `ilos.yaml`, quoted with its id and exact wording. Every activity must derive from a file in `learning-activities/activities/`, cited by id (LA01–LA15). Adaptations (shortened, moved online, localised) are allowed and must be labelled as adaptations of the source activity.
2. **Coverage is traceable.** A built course always includes a `coverage.md` that lists each selected ILO → where it is taught, practised, and (if configured) assessed — and lists what was left out and why.
3. **Attachments are honoured.** If the educator supplied a policy, the course must reflect it wherever GenAI use is described; if they supplied a syllabus, scope and terminology follow it. Say explicitly where each attachment was used.
4. **Time budgets are respected.** The build must sum to the configured hours, split between presentation and activities as configured. When an activity doesn't fit, adapt it or drop it and say so — never silently overrun.
5. **Preferences are constraints, not suggestions.** Tools students can't access, room constraints, language, tone: these rule out options, they don't just colour them.

## The workflow

```
configure-course  →  gather-sources  →  build-course  →  revise-course (repeat)  →  publish-course
   (CFG01–06, 08)        (CFG07)          generate         adjust & rebuild          put it on a website
```

Skills live in `.claude/skills/<name>/SKILL.md`. Each is self-contained: read the one you need in full before starting.

- **configure-course** — interview the educator; write `config/config.yaml`; set `status: configured`.
- **gather-sources** — collect attachments into `course-resources/`, record them in `config.yaml` with how they should be used.
- **build-course** — read config + libraries + attachments; generate `course-material/<course-slug>/` (overview, sessions, assessment, instructor guide, coverage); set `status: built`.
- **revise-course** — take a change request in plain language, update config and/or regenerate only the affected files.
- **publish-course** — convert the built course to HTML and push it to a GitHub Pages repository the educator names; link it from the site's landing page.

**Header artwork** is optional. `build-course` generates one illustration per page with `scripts/make-artwork.py` when `OPENAI_API_KEY` is set, and skips silently when it isn't; a course without artwork is complete. Never fetch images from the web into a course.

**Routing.** When the user's intent is unclear, look at `config/config.yaml` → `status`:
`empty` → offer to start configuring · `configured` → offer to gather sources or build · `built` → offer to revise, review, publish, or rebuild. A first message like "hi" or "help" should get a two-sentence description of what this tool does and the offer that matches the status.

## Requirements this tool implements

From the working group's requirements analysis (Table 15):

| ID | Requirement |
|----|-------------|
| CFG01 | Select topics and sub-topics to include |
| CFG02 | Assign relative importance (weight) to each selected topic |
| CFG03 | Input total available time |
| CFG04 | Split time between presentation and activities |
| CFG05 | Choose whether assessment is included |
| CFG06 | Choose which topics are assessed |
| CFG07 | Attach documents (e.g. institutional GenAI policies) to be considered in generation |
| CFG08 | Adapt content, interface and activities to the user's preferences and configuration |

`config/README.md` shows how each maps onto configuration fields.

## For maintainers

The content libraries are pinned submodules. To pull their latest commits: `scripts/update-content.sh` then `git push`. Details in `README.md`.
