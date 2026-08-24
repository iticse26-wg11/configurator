---
name: gather-sources
description: Collect documents an educator wants the generated course to follow or use — institutional GenAI policies, syllabi, reading lists, example materials (CFG07) — put them in course-resources/, and record in config/config.yaml how each should be used. Use when the user mentions a policy, a document, a file, a syllabus, readings, "our university rules", or wants to attach/upload/add something for the course.
---

# gather-sources

Implements CFG07: attachments the build must take into account. Read `AGENTS.md` first if you haven't.

## Getting the files in

Educators may not know how to "put a file in a folder". Offer these routes, simplest first:

1. **They drag the file into the terminal / paste a path.** Copy it into `course-resources/` with a clean, descriptive filename (lowercase, hyphens, keep the extension). Keep the original untouched.
2. **They paste the text.** Save it as `course-resources/<descriptive-name>.md` with a one-line header noting where it came from and the date.
3. **They give a URL.** Fetch it if you can; save the extracted text as markdown with the URL and retrieval date at the top. If you can't fetch, ask them to paste the text.
4. **The file is already in `course-resources/`.** List what's there and ask which to use.

Accepted formats: PDF, Markdown, plain text, Word (`.docx` — if you cannot read it, ask for PDF or pasted text), images of documents (read with the Read tool). Always open each file and confirm you can read it before recording it.

## For each attachment, establish

Ask in plain language, one thing at a time, with a guessed default from the content:

- **What it is** → `kind`: `policy` (rules students/staff must follow), `syllabus` (existing course description that scopes this one), `reading` (material to cite/assign), `example` (existing slides, activities, assessments to reuse or match), `dataset`, `other`.
- **Title** → `title` (take it from the document if present).
- **How the course should use it** → `how_to_use`. Get this right; it's what the build reads, and specific instructions produce a course where the document actually *does* something. Draft a concrete proposal from what you read, then confirm it. For a policy, the example build used the attached document in six ways — quoted in the syllabus, a "policy check" step before each tool-using activity, the required AI-use statement in handouts, the text students summarise in a use-case exercise, one of the policy lenses in the evaluation activity, and the rationale for the data-retention slide — so propose at that level: *"Binding. Quote the key rules in the overview; add a policy-check step to every activity where students use GenAI tools; require its AI-use statement on handouts; use it as the university policy handout in LA11 and as the 'provided policy' in LA03; if a summarisation task is needed, make this the text."* Other examples: *"Use this reading list as recommended reading, one item per session; don't add others."* — *"Match the structure and tone of these existing slides; reuse their diagrams where relevant."* Vague instructions ("take it into account") should be pushed back on gently: ask what they'd expect to see changed in the course because of it.
- **Where it applies** → `applies_to`: `all`, or topic / sub-topic / ILO / activity ids. Default `all` for policies; ask for the rest.

After reading a document, briefly tell the educator what you found in it that matters (e.g. "your policy allows GenAI for brainstorming but requires disclosure — I'll make sure the activities include a disclosure step"). This confirms you read the right thing and often surfaces corrections.

## Record it

Append to `attachments:` in `config/config.yaml`:

```yaml
  - path: course-resources/<file>
    kind: policy
    title: …
    how_to_use: …
    applies_to: all
```

Path is relative to the repo root. Keep `status` as it is (`configured` or `built`; if `built`, mention that a rebuild or `revise-course` is needed for the new attachment to take effect). Run `python3 scripts/validate-config.py` if available.

## Finish

Summarise the attachments recorded (title, kind, one-line use). Offer the next step: build the course if `status: configured` and no build exists; otherwise `revise-course` to fold the new sources in.
