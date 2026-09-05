# Instructor guide: Generative AI Literacy for CS1

![An empty stage under crossed spotlights, a lectern and an open notebook waiting](figures/art-instructor-guide.jpg)

## What you need to create before the day

These are the materials you must *make*, not just copy. Everything else in the course is ready to paste into a shared document.

| Activity | What to create | Estimate |
|---|---|---|
| **LA07 Run a language model by hand** (session 1) | Five one-page texts on the topic "cats", one per genre: news report, children's story, forum post, encyclopedia entry, recipe blog. Each about 250–350 words. Then one next-word table per text: choose ten starting words that appear several times (for example *the, cat, a, is, and, to, of, in, was, it*), fill six rows yourself and leave four blank. Test one full generation run per text so you know the table works and the prompt "The cat" has an entry. Put text + table + prompt into ten shared documents (two per genre). | 1½–2 h |
| **LA15 Take the pipeline apart** (session 2) | Nothing to author: the handout contains the diagram, the shuffled descriptions, the ten risks and the reflection prompts. Copy it into ten shared documents, one per room. | 30 min |
| **LA13 Put a chat tool to work** (session 3) | One shared class form or document with the five observation questions from the handout. Try the leap-year prompt yourself in two tools the day before, so you know what your students are likely to see. | 30 min |
| **LA12 What did the tool do** (session 3) | Nothing to author. Handout only. | 0 |
| **LA08 What is your AI system made of** (session 4) | Ten shared slides or documents with the four-box template and top line. A short list of two or three reputable starting sources per system, to paste into the chat for rooms that stall. | 45 min |
| **Quizzes** (sessions 2 and 4) | Load the 18 poll questions from `assessment/formative-checks.md` into your platform's poll tool or a shared form. | 45 min |
| **Slides** | Build slides from the four session outlines. Figures marked `[figure: …]` are cues; the Mermaid diagrams in the handouts render on GitHub and in most Markdown editors and can be screenshotted. | 3–4 h |

**Total: roughly 7–9 hours**, of which about 4 hours is slide-making. If the LA07 preparation is too much, ask `revise-course` to swap it; the alternatives it will offer are all presentation-based for MM01, so the trade is real.

## Before the course

- [ ] Ten breakout rooms of 5 pre-assigned for sessions 1, 2, 3 (LA12) and 4; a pairs layout (25 rooms, or 12–13 rooms of 4) for session 3's LA13. Post the room-to-document mapping in the chat before opening rooms.
- [ ] Shared documents created and link-shared: 10 for LA07, 10 for LA15, 1 class form for LA13, 10 slides for LA08, plus one "class document" for LA07 outputs.
- [ ] Tool access to verify: only free tiers of ChatGPT, Gemini, Claude or Copilot are used, and only in session 3. Send the "create one free account before day 2" reminder at the end of session 2 and again the next morning. No paid accounts, no Python installation required (tracing by hand is explicitly allowed).
- [ ] Attachments: none were provided. If your institution has a GenAI policy, ask `revise-course` to attach it before the course; session 4's policy block and the LA13 "before you start" step will then quote it.
- [ ] Pre-generated content: the five LA07 training texts and tables (see above). Nothing else.
- [ ] Polls loaded: Q1–Q10 for session 2, Q11–Q18 for session 4.

## Session-by-session prep

**Session 1.** Ten LA07 documents open in tabs so you can visit rooms. Have a chat tool logged in for the two demonstrations (made-up restaurant phone number; same prompt twice). The transition at 0:30 is the tight moment: rooms, links and the "roll a die" site should be in the chat before you say "go". Timing pressure is in the table-filling step; call time at 15 minutes.

**Session 2.** Ten LA15 documents. The pipeline slide with all five stage names must be on screen during the activity; rooms will refer to it. Quiz polls loaded. Do not cut the account reminder.

**Session 3.** Opening poll on accounts, then pairing. The LA13 form link in the chat before rooms open. Keep the verification toolkit slide available for students. Rooms of 5 for LA12 are a second breakout layout in the same session; set both up in advance if your platform allows it, or reuse the LA13 rooms and accept groups of 4.

**Session 4.** Ten LA08 slides, one per room, systems pre-assigned two rooms each. Your two or three reputable starting sources per system ready to paste. The plan-writing block needs no setup, but tell students to open a personal document at the start of the session so they are not scrambling at 1:15. Quiz polls loaded.

## Facilitation tips

Drawn from the source activities and the example build.

- **LA07:** the reveal (same prompt, five genres, ten different outputs) is the whole payoff; protect it even if the tables are incomplete. The most common confusion in rooms is which word to look up: always the last one written. When a word is missing from the table, that *is* the lesson ("your model is lost"); tell them to pick the most common word and carry on.
- **LA15:** "misleading outputs" is deliberately hard to place (produced at stage 4, caused at 1–3); use it in the debrief. The responsibility step is where EPR03 lands: push rooms past "the company should fix it" to "which country's law applies to a server you cannot see?" and "what did *you* decide to paste in?".
- **LA13:** many tools get `is_leap_year` right, and that is fine: the lesson is that students had to *check* to know. If a pair gets a wrong one (often the 1900 case), have them show it. When pushed, tools sometimes invent a weakness that does not exist; that is a hallucination about itself and worth naming.
- **LA12:** resist adding your own patterns until the rooms have posted theirs. The calculator comparison comes up every time; the useful complication is "you learned arithmetic first".
- **LA08:** insist on "number plus source". A chat tool's figure with no traceable origin does not count, and saying so out loud reinforces session 3. In the debrief, move explicitly from resources to jobs: the same demand that strains resources reshapes what a junior developer is hired to do.
- **Presentation blocks:** the live demonstrations (a made-up restaurant's phone number in session 1; a made-up Python module in session 3) do more than any slide. Rehearse them, and have a screenshot as a fallback in case the tool behaves unusually well.

## If you have less time than planned

Cut in this order, per session, without losing an outcome entirely:

- **Session 1:** drop LA07's second generation run (saves ~5 min); then compress the limitations block to hallucination and context window only (MM03 keeps its quiz item).
- **Session 2:** drop the second example in LA15 step 3; fold the LA15 debrief into the first explainability slide; if desperate, run the quiz as a chat instead of polls.
- **Session 3:** cut LA13's "push it" step to one follow-up question and the discussion to 10 minutes; keep LA12 at full length, it is short and carries EPR08 alone.
- **Session 4:** one room per system in LA08 sharing, no chat additions; plan-writing reduced to prompts 1–3; the closing chat reflection can move to a post-course message.

## How your documents were used

No documents were attached. The course therefore uses a default disclosure statement in the overview and treats "your institution's rules" as a placeholder in session 4. Attaching a policy via `revise-course` will replace the placeholder with quoted rules in the overview, in LA13's "before you start" step, and in the session 4 policy block.

## Adapting further

Ask `revise-course` in plain language. Requests that work well for this course:

- "Swap the unplugged simulation for something with less preparation."
- "Add our university's GenAI policy" (attach the file).
- "We now have three days, not two."
- "Make session 4 more hands-on."
- "The students all have Python installed, let them run the code in session 3."
- "Add the history opener."
