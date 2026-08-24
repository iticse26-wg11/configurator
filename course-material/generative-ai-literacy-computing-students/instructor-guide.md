# Instructor guide: Generative AI Literacy for Computing Students

## What you need to create before the day

These activities need material you must *make*, not just print. Budget the time — this is the real cost of the course.

| Activity | What to create | Estimate |
|----------|----------------|----------|
| LA07 Unplugged LLM simulation (S2) | Five one-page training texts on the same topic in different genres (encyclopedia, news, forum, reviews, fiction); choose the conditioning words for the n-gram table (W1) and test-fill one table yourself | 1½–2 h |
| LA11 Evaluation frameworks + policies (S4) | Check/adapt the three case cards in W3; write a one-page summary of the OECD AI Principles (the University policy is ready as-is) | 1–1½ h |
| LA01 Timeline (S1) | Eight milestone cards and a timeline strip, 12 sets | 30 min |
| LA13 Use cases (S3) | Three fallback outputs for the regex task in case tool access fails; set up the W2 online form if not using paper | 30 min |
| **Total** | | **≈ 3½–4½ h** |

If that is more than you can do, ask `revise-course` to swap an activity — e.g. *"replace the unplugged simulation with something lower-prep"* (it will tell you the cost: MM01/CS02 become presentation-only).

## Before the course
- [ ] **Print** (for 60 students, 12 groups): 12 timeline strips + 12 envelopes of 8 milestone cards (S1); 12 training pages across 5 genres + 12 n-gram tables W1 (S2); 60 homework sheets H1 and H2 (end of S2); 60 reflection forms W2 or set up the online form (S3); 12 case cards + 12 evaluation grids W3, 6 copies each of the two policy handouts (S4). Handout masters are in `student-handouts/`.
- [ ] **Prepare** (biggest item): the five one-page training texts on the same topic in different genres for LA07, and pick the conditioning words for the n-gram table. Test-fill one table yourself.
- [ ] **Pre-generate** three fallback outputs for use case A in S3 (the student-ID regex) in case tool access fails.
- [ ] **Verify tool access**: ChatGPT free tier works on the room Wi-Fi; students have activated GitHub Copilot on the University licence (they need it for homework H2 and S3). No other tools are named anywhere in student material.
- [ ] **Read** the Example University GenAI policy — it is quoted in the overview, used as a policy check before every tool-using activity, and is one of the two policy lenses in S4.
- [ ] **Write** a one-page summary of the OECD AI Principles for the S4 handout (students should not be reading the website).
- [ ] **Room**: flipcharts and markers (no whiteboard); one flipchart stays up all day for the S1 "only one of us wrote it" list; dice or phones for S2.

## Session-by-session prep
| Session | Print / set up | Grouping | Timing pinch point |
|---------|----------------|----------|--------------------|
| 1 | A4 paper for mindmaps; timeline envelopes | Individual → pairs; groups of 5–6 | Myths board (cut to 3 myths if late) |
| 2 | Training pages, W1, dice; H1 + H2 to hand out | Groups of 5–6 | Step 3 of the simulation (cut to 2 outputs) |
| 3 | W2 forms or online form; fallback outputs; Wi-Fi check | Individual → groups of 4–5 | Whole-class discussion (cut to 5 min) |
| 4 | Case cards, grids, policy handouts, sticky notes | Groups of 4–5, paired by case | Part 2 step 5 (report one difference each) |

## Facilitation tips
- **S1 timeline**: the Mechanical Turk card is the moment — let the surprise land before explaining. Ask "which of these is *generative*?" to bridge to H02.
- **S2 simulation**: put three groups' generated sentences on the flipchart and ask *why different?* before you say anything about training or sampling. Everything in the presentation is an answer to that question.
- **S3 use cases**: the regex answer is usually almost right; get students to *run* it against `s1234567`, `S1234567`, `s12345678` before rating correctness. For the summary task, insist on line-by-line checking against the policy — a wrong summary of a policy you must follow is the cleanest example of MM06 in the day.
- **S3 cognitive debt**: keep the input to three minutes; the discussion is the content.
- **S4**: two groups per principle keeps definitions honest (they argue). In the closing discussion, ask "who was not at the table?" and wait — the silence is productive.

## If you have less time than planned
Cut in this order, per session, without losing an ILO entirely:
1. S1 myths board 20 → 10 min (MM03/MM05 still covered by Q1/Q2 and the mindmaps).
2. S3 whole-class discussion 20 → 10 min.
3. S4 Part 2 step 5 → one difference per pair.
4. S2 simulation step 3 → two outputs. Do **not** cut step 5 (the mapping to real concepts) — it is where MM01 and CS02 are consolidated.
Never cut: the timeline reveal (H01), the simulation (MM01/CS02), the LA11 closing discussion (EPR13).

## How your documents were used
- **Example University policy on student use of generative AI** (`course-resources/example-university-genai-policy.md`, kind: policy, applies to all):
  - summarised, with quoted rules, in `00-overview.md` → *Policies on GenAI use*;
  - a "policy check" step before both tool-using activities (S3 use cases; homework H2);
  - the AI use statement required at the end of the S3 activity and as the minimum in reflection R4;
  - one of the two policy handouts in S4's LA11 (as its `how_to_use` requested), replacing the source's generic "university's own AI policy";
  - the "approved tools only for University data" rule used as the concrete consequence of data retention in the S4 presentation (EPR03);
  - the summarisation use case in S3 is the policy itself, so students read it closely at least twice.

## Adapting further
Ask the assistant (`/revise-course`) for things like: *"we now have 8 hours — bring back the AI Model Pipeline activity"*; *"make session 1 the discovery version of the timeline"*; *"replace the regex task with a SQL one"*; *"add the EU AI Act handout to session 4"*; *"we do have Colab access after all — can the alignment lab fit?"*
