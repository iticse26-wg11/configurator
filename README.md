# configurator

System to build, deploy and update GenAI literacy courses.

## Layout

| Path | What it is |
|------|------------|
| `intended-learning-outcomes/` | **Submodule** → [iticse26-wg11/intended-learning-outcomes](https://github.com/iticse26-wg11/intended-learning-outcomes). The ILOs (`ilos.yaml` + per-area markdown). |
| `learning-activities/` | **Submodule** → [iticse26-wg11/learning-activities](https://github.com/iticse26-wg11/learning-activities). One markdown file per activity, mapped to ILOs. |
| `config/` | Course configuration (`config.yaml`). |
| `course-material/` | Generated course material. |
| `course-resources/` | Supporting resources for courses. |
| `scripts/` | Helper scripts. |

## Working with the content submodules

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
