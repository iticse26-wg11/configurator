# configurator

System to build, deploy and update GenAI literacy courses for computing students — built by ITiCSE 2026 Working Group 11.

An educator clones this repository, opens it with an AI coding assistant (Claude Code, or any agent that reads `AGENTS.md`), and is walked through configuring a course: which topics, how much time, how it splits between presentation and hands-on activities, whether to assess, and which institutional documents (e.g. a GenAI policy) the course must follow. The assistant then generates the course as plain Markdown files — syllabus, session plans with speaker notes, activities drawn from the working group's library, assessment items, and an instructor guide.

## Quick start for educators

1. **Install** [Claude Code](https://claude.com/claude-code) (or another AI assistant that supports project instructions).
2. **Get the repository**, including the content libraries:
   ```bash
   git clone --recurse-submodules git@github.com:iticse26-wg11/configurator.git
   cd configurator
   claude
   ```
3. **Say what you want**, e.g. *"I'd like to set up a one-day GenAI literacy workshop for first-year CS students."* The assistant will ask a handful of questions, one at a time. You never need to edit files yourself.
4. When the questions are done, say **"build the course"**. Your course appears in `course-material/<your-course>/`.
5. Ask for changes in plain language — *"make session 2 more hands-on"*, *"we now have 8 hours"*, *"add our department's AI policy"* — and the assistant updates only what's affected.

The four steps are also available as commands: `/configure-course`, `/gather-sources`, `/build-course`, `/revise-course`.

## What you get

- **Learning outcomes** taken verbatim from the working group's validated set of 32 ILOs (History · Mental Models · Ethics, Policy & Regulations · Computer Science) — never invented.
- **Activities** adapted from the working group's library of 15 classroom activities, cited by id, with any adaptation labelled.
- **A time budget that adds up**: every session's blocks sum to the hours you gave, split as you asked.
- **Traceability**: `coverage.md` shows where every outcome is taught, practised and assessed, and what was left out and why.
- **Your documents respected**: policies you attach are summarised in the syllabus and built into the activities where students use GenAI tools.

Requirements this implements (working group Table 15, CFG01–CFG08) and how they map onto the configuration: [`config/README.md`](config/README.md).

## Layout

| Path | What it is |
|------|------------|
| `intended-learning-outcomes/` | **Submodule** → [iticse26-wg11/intended-learning-outcomes](https://github.com/iticse26-wg11/intended-learning-outcomes). The ILOs (`ilos.yaml` + per-area markdown). |
| `learning-activities/` | **Submodule** → [iticse26-wg11/learning-activities](https://github.com/iticse26-wg11/learning-activities). One markdown file per activity, mapped to ILOs. |
| `config/` | Course configuration (`config.yaml`). |
| `course-material/` | Generated course material. |
| `course-resources/` | Supporting resources for courses. |
| `scripts/` | `validate-config.py` (checks a configuration), `update-content.sh` (maintainers: refresh content libraries). |
| `.claude/skills/` | The four workflows (`configure-course`, `gather-sources`, `build-course`, `revise-course`). |
| `AGENTS.md`, `CLAUDE.md` | Grounding instructions for the AI assistant. |

## For maintainers: the content submodules

The ILOs and activities live in their own repositories so they can be published and cited independently. This repo *pins* a specific commit of each, so a course build is reproducible even while the content repos keep changing.

### Cloning

```bash
git clone --recurse-submodules git@github.com:iticse26-wg11/configurator.git
```

If you already cloned without `--recurse-submodules` (the submodule directories will be empty):

```bash
git submodule update --init
```

To make `git pull` also update submodules automatically:

```bash
git config submodule.recurse true
```

### Pulling in the latest content

When the ILO or activity repos have new commits on `main`, bump the pinned versions with:

```bash
scripts/update-content.sh          # fetches latest, checks it out, commits the bump
git push
```

Use `scripts/update-content.sh --no-commit` to review the change first, or pass a submodule path to update only one (`scripts/update-content.sh learning-activities`).

What the script does, for reference:

```bash
git submodule update --remote --merge     # move each submodule to its origin/main
git add intended-learning-outcomes learning-activities
git commit -m "Bump content submodules"
```

### Editing content

Make content changes in the content repository itself (a sibling clone, or inside the submodule directory after `git checkout main` there), commit and push to that repo, then bump the pointer here with `scripts/update-content.sh`. Editing inside a submodule without checking out a branch first leaves you on a detached HEAD — the commit will exist but no branch points at it.
