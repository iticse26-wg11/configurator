# Course material

Generated courses land here, one folder per course (`<course-slug>/`), produced by the `build-course` skill and updated by `revise-course`.

Each course folder contains:

```
00-overview.md          syllabus: description, ILOs, schedule, policies, assessment, reading
sessions/NN-<slug>.md   one file per session: timeline, slide outline, speaker notes,
                        activities (adapted from the activity library, cited by id), homework
assessment/             assessment items per ILO (only if assessment was configured)
student-handouts/       worksheets and briefs for activities (if enabled)
instructor-guide.md     prep checklist, facilitation tips, what to cut if short on time
coverage.md             traceability: every selected ILO → session / activity / assessment,
                        plus adaptations, exclusions and how attachments were used
figures/                header artwork (art-*.jpg) and the prompts that made it (artwork.json),
                        only if an image-generation key was available at build time
CHANGELOG.md            appears after the first revision
```

Everything is plain Markdown so it can be read on GitHub, pasted into a VLE, or converted to slides/PDF with tools such as Pandoc or Marp. Hand-edits are allowed; `revise-course` checks for them before overwriting.

`generative-ai-literacy-for-cs1/` is a finished example (two online days for first-year students), published at <https://iticse26-wg11.github.io/courses/generative-ai-literacy-for-cs1/>.
