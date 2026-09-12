# Course configuration

`config.yaml` describes the course an educator wants. It is written by the `configure-course` and `gather-sources` skills through conversation — educators do not need to edit it by hand — and read by `build-course` to generate `course-material/`.

`topics.yaml` is the menu of topics and sub-topics (mapped to ILO ids) that the configuration draws from. `examples/` holds complete worked configurations.

## How the fields map to the working-group requirements

| Requirement | Field(s) |
|-------------|----------|
| **CFG01** Topic selection | `topics[].id`, `topics[].subtopics`, `topics[].exclude_ilos` |
| **CFG02** Relative importance | `topics[].weight` (1–5) |
| **CFG03** Available time | `time.total_hours`, `time.homework_hours` |
| **CFG04** Time allocation (presentation vs. activities) | `time.presentation_share` (activities get the remainder) |
| **CFG05** Assessment inclusion | `assessment.include` |
| **CFG06** Assessment scope | `assessment.scope` (`all` or topic / sub-topic / ILO ids), `assessment.types`, `assessment.formats` |
| **CFG07** Attachments considered in generation | `attachments[]` — files under `course-resources/` with `kind`, `how_to_use`, `applies_to` |
| **CFG08** Adapt to preferences and configuration | `course.*` (audience, level, delivery, session length) and `preferences.*` (tone, prior knowledge, tools, constraints, output options) |

## Field reference

### `status`
`empty` → nothing configured yet · `configured` → ready to build · `built` → `course-material/` reflects this config. Skills use it to decide what to offer next.

### `course`
Basic facts. `session_length_minutes` drives how the build chunks content into sessions; `delivery` and `class_size` affect which activities fit (e.g. unplugged group work vs. online).

### `topics[]`
One entry per included topic area (`H`, `MM`, `EPR`, `CS`). `weight` is relative: a topic with weight 4 gets twice the time of one with weight 2. `subtopics: all` or a list of ids from `topics.yaml`. `exclude_ilos` removes individual ILOs from an otherwise included sub-topic.

### `time`
`total_hours` is contact time. `presentation_share` is the fraction of contact time for instructor-led presentation; the rest goes to activities. `homework_hours` lets the build place pre-sessional or reflective work outside class.

### `assessment`
When `include` is true the build generates assessment items for ILOs in `scope`. Activities that carry their own formative assessment (LA04, LA12, LA13, LA05) are used first; additional items are generated in the requested `formats`.

### `attachments[]`
Each file the educator wants considered. `kind` tells the build how to treat it: a `policy` is binding content to summarise and reference; a `syllabus` constrains scope and terminology; `reading` and `example` are material to cite or reuse. `how_to_use` is free text and takes precedence over defaults. `applies_to` limits where the attachment is used.

### `preferences`
`tone`, `prior_knowledge`, `tools_available` and `constraints` shape the wording and the selection/adaptation of activities. `output.*` toggles which generated files are produced.

## Validation

```bash
python3 scripts/validate-config.py            # checks config/config.yaml
python3 scripts/validate-config.py config/examples/one-day-workshop.yaml
```

Requires PyYAML (`pip install pyyaml`). If it is not installed, the skills fall back to checking the same rules by reading the files.
