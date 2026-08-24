@AGENTS.md

## Claude Code specifics

- The four workflows are installed as skills: `/configure-course`, `/gather-sources`, `/build-course`, `/revise-course`. Invoke them with the Skill tool when the educator's request matches; educators may also type them directly.
- Use `AskUserQuestion` for the interview steps in `configure-course` — one question per call, with the recommended option first. Fall back to plain questions in prose if the tool is unavailable.
- Read attachments with the `Read` tool (it handles PDF, images and text). Don't ask the educator to convert files.
- Generated files go under `course-material/<course-slug>/` via `Write`. Never write generated material into the content-library submodules.
- Don't commit or push on the educator's behalf unless they ask. If they ask, commit in this repo only — never inside the submodule directories.
