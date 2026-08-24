# Session 4: Responsibility, policy and you

**Topic area:** Ethics, Policy and Regulations · **Duration:** 90 min (25 presentation + 65 activities) · **ILOs:** EPR03, EPR04, EPR05, EPR06, EPR07, EPR10, EPR11, EPR12, EPR13, EPR14

## Learning outcomes for this session

| ID | Outcome (exact wording) |
|----|-------------------------|
| EPR03 | … evaluate data management in GenAI systems in order to identify risks of misuse, manipulation, and threats to data sovereignty. |
| EPR04 | … explain the shortcomings of GenAI outputs (e.g. accuracy, reliability) and recognise the need to follow the appropriate policies and regulations within the context where the outputs will be used. |
| EPR05 | … recognize limitations in GenAI model outputs, including hallucination, misinformation, privacy leakage, harmful content, in the context of societal impacts. |
| EPR06 | … differentiate between reliable, trustworthy, and responsible GenAI systems. |
| EPR07 | … identify tools and procedures for evaluating and verifying model outputs, and apply these to assess AI-generated content. |
| EPR10 | … evaluate (the use of) GenAI systems against relevant normative principles (e.g., fairness, transparency, accountability, safety, robustness, and human governance). |
| EPR11 | … design a plan for the responsible and context-appropriate use of GenAI, including documenting of GenAI-related outputs and decisions |
| EPR12 | … identify and interpret relevant GenAI policies, assessing their applicability to and impacts on GenAI use in different contexts. |
| EPR13 | … discuss societal perceptions of and expectations around GenAI use, taking into consideration power dynamics in the adoption of GenAI tools. |
| EPR14 | … discuss frameworks for the fair and responsible use of GenAI in the student's particular discipline. |

## Timeline

| Time | Block | Type | Notes |
|------|-------|------|-------|
| 0:00–0:05 | Opening: from "is it right?" to "is it right to use?" | Opening | |
| 0:05–0:25 | Presentation: Data, outputs and harm; reliable vs. trustworthy vs. responsible; how to verify; what society and your discipline expect | Presentation | EPR03–07, EPR13, EPR14 |
| 0:25–1:30 | Activity: AI evaluation frameworks + policies (LA11, shortened) — closes with the course wrap-up | Activity | Groups of 4–5; flipcharts; policy handouts |

## Presentation

### Slide outline (0:05–0:25, 9 slides)
- Data going *in*: what happens to your prompt — retention, training on user data, jurisdiction; data sovereignty in one sentence; the policy's "approved tools only for University data" rule as the practical consequence. (EPR03)
- Outputs coming *out*: accuracy and reliability are not guaranteed; the context decides how bad a wrong answer is — and which rules apply (a coursework rule, a medical-device regulation, a contract). (EPR04)
- Harms at scale: hallucination and misinformation; privacy leakage (training data or your pasted data reappearing); harmful content. Why "occasional mistakes" become societal problems when millions use the same model. (EPR05)
- Three words that aren't synonyms: **reliable** (does what it does consistently), **trustworthy** (you can justify relying on it — evidence, transparency, recourse), **responsible** (built and used with accountability for its effects). A system can be any one without the others. (EPR06)
- Verifying outputs — the toolkit: fact-check against a trusted source; cross-check with a differently-worded prompt or a second tool; run the code / test the claim; check provenance; an adversarial question ("what would make this wrong?"). Yesterday's habit, now a procedure. (EPR07)
- What people expect: public perception swings between magic and menace; who gets to decide how these tools are adopted — employers, universities, vendors — and who doesn't. (EPR13)
- Your discipline: the ACM Code of Ethics as a computing frame; how software teams are writing GenAI use rules (disclosure, review, no secrets in prompts). (EPR14)
- The activity ahead: you write the principles first, then see what real policies add — and miss.
- Homework reminder: the post-course mindmap.

### Speaker notes

**Data and outputs (EPR03, EPR04, EPR05).** Anchor everything in the policy they read: *why* does it say "approved tools only for University data"? Because of retention and training-on-inputs. *Why* an AI use statement? Because output reliability isn't guaranteed and responsibility stays with the submitter. Students who see the policy as reasoned rather than arbitrary are the ones who follow it.

**Reliable / trustworthy / responsible (EPR06).** Give one example of each failing alone: a very reliable model used for something it shouldn't be (not responsible); a responsible deployment of an unreliable model (not trustworthy). Ask the room to classify the tool they used in session 3.

**Verification (EPR07).** This is the only place the toolkit is stated as a list — students apply pieces of it in the activity's Part 1 when they justify ratings "with concrete evidence".

**Society and discipline (EPR13, EPR14).** Two slides, not a lecture; the activity's closing discussion (power and agency) does the depth. Name the ACM Code and the OECD Principles so the words are familiar when the handouts arrive.

## Activities

### Activity: AI evaluation frameworks + policies — *LA11, shortened* (65 min)
**Source:** learning-activities/activities/11-ai-evaluation-frameworks-and-policies.md · **ILOs:** EPR10, EPR12 (and, through the closing discussion, EPR13, EPR14) · **Adaptation:** shortened from 90 to 65 min (Part 1: 30 min instead of 45; Part 2: 25 min instead of 45; closing discussion 10 min). Three case cards instead of 4–6, and two policy handouts instead of three: the **University policy** (attached to this course, as its `how_to_use` requires) and the **OECD AI Principles** summary. The EU AI Act handout is dropped for time. The closing discussion doubles as the course wrap-up.

**Setup** — Groups of 4–5 (≈ 12 groups). Per group: one assigned principle (fairness · transparency · accountability · safety · robustness · human agency & oversight — two groups per principle), one case card (**W3**: three cases, four groups each), evaluation grid (**W3**), one policy handout (six groups: University policy; six groups: OECD Principles), sticky notes, markers. Shared flipchart at the front for the class framework. No GenAI tools needed.

**Part 1 — build your own framework (30 min)**
1. (8 min) Draft a working definition of your group's principle for GenAI systems — one or two sentences, on a sticky note.
2. (7 min) Whole class: one group per principle reads theirs; the pair with the same principle adds or objects; the instructor writes the agreed version on the flipchart. This is the class framework.
3. (15 min) Evaluate your case card against **all six** principles on the grid: rate each (meets / partly / fails / can't tell) and justify with concrete evidence or a scenario — use the verification toolkit from the presentation.

**Part 2 — apply a real policy (25 min)**
4. (12 min) Read your policy handout. Evaluate the *same* case through its lens: Which rules apply? How would this system or use be classified? What obligations or restrictions follow? Fill in the policy column of the grid.
5. (13 min) Pairs of groups with the same case but *different* policies compare: where did the University policy and the OECD Principles lead to different verdicts? Where did the class framework match or differ from the real policies? What did the real policy add — and what did it miss?

**Closing discussion (10 min)** — Whole class, on power and agency: Who wrote each policy, and whose interests does it protect? Who was not at the table? Do the people affected — students, patients, users — have any real choice or control? What would the policy look like if *you* had written it? Then, for the course: one thing from today you'll do differently.

**Debrief** — Draw out for EPR10: principles are only useful once you can point at evidence for a rating. For EPR12: the same system is judged differently by different policies; interpreting a policy means deciding which of its rules apply *here*. For EPR13/EPR14: the "who wasn't at the table" question, and that their own discipline (computing) is writing these rules now — they will be asked to.

## Assessment in this session
The completed evaluation grid (W3) is submitted per group — this is LA11's built-in formative assessment and covers EPR10 (and EPR12). Reflection R4 (EPR11 — your own responsible-use plan) is set as part of the homework below.

## Homework / preparation (15 min, after the course)
- **Post-course mindmap** (LA10, part 2, adapted to homework): revisit your session-1 mindmap. In a different colour, add, correct and cross out. Then answer in three sentences: What did I believe that turned out to be a myth? What did I over- or under-estimate? What surprised me most? (Reflection R1.)
- **My GenAI use plan** (Reflection R4, EPR11): half a page — how you will use GenAI in this degree, what you won't use it for, and how you will document its use (the policy's AI use statement is the minimum).

## Instructor notes
- Case cards (W3) are the key prep: three concrete GenAI uses with purpose, users, data and known failure modes. The ones supplied are a chatbot giving health advice, an image generator for a student society's posters, and an AI assistant that pre-grades programming assignments. Swap in a local example if you have one.
- Pre-process the policy handouts: the University policy is already two pages; the OECD Principles need a one-page summary (five values-based principles) — don't hand out the website.
- If running long, cut step 5 to pairs-of-groups reporting one difference each; keep the closing discussion — it's where EPR13 lives.
- No whiteboard in the room: the class framework goes on a flipchart; photograph it and share afterwards.
