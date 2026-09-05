@AGENTS.md

## Claude Code specifics

- The five workflows are installed as skills: `/configure-course`, `/gather-sources`, `/build-course`, `/revise-course`, `/publish-course`. Invoke them with the Skill tool when the educator's request matches; educators may also type them directly.
- Use `AskUserQuestion` for the interview steps in `configure-course` — one question per call, with the recommended option first. Fall back to plain questions in prose if the tool is unavailable.
- Read attachments with the `Read` tool (it handles PDF, images and text). Don't ask the educator to convert files.
- Generated files go under `course-material/<course-slug>/` via `Write`. Never write generated material into the content-library submodules.
- Header artwork (`build-course` step 7b) needs `OPENAI_API_KEY`; if it isn't set, skip without fuss and mention it once in the build report. Never print the key.
- `publish-course` pushes to a *website* repository the educator names, after a yes. That is the only push you make without a further request.
- Don't commit or push in this repository on the educator's behalf unless they ask. If they ask, commit in this repo only — never inside the submodule directories.
