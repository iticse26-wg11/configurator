# Session 1: Where GenAI came from, and how it works

**Topic area:** History; Mental Models · **Duration:** 90 min (55 presentation + 35 activities) · **ILOs:** H01, H02, MM01, MM03, MM05, EPR05

## Learning outcomes for this session

| ID | Outcome (exact wording) |
|----|-------------------------|
| H01 | … identify key milestones (e.g. symbolic AI, rule-based systems, machine learning, transformers, …) in AI history and explain why the field experienced periods of rapid advancement and decline (AI winters) |
| H02 | … distinguish between earlier applications of AI (e.g., search algorithms and engines, recommendation systems, navigation systems) and GenAI |
| MM01 | … explain how GenAI models generate output using a simplified "next-word prediction" process, recognising that real systems predict tokens and use contextual information from prompts and prior text to determine their responses. |
| MM03 | … evaluate technical, ethical and practical limitations of GenAI systems (e.g. hallucinations, computational cost, context window, lack of true understanding, biases, …) |
| MM05 | … analyze existing misconceptions about GenAI, distinguishing between its actual capabilities and common myths / misinterpretations. |
| EPR05 | … recognize limitations in GenAI model outputs, including hallucination, misinformation, privacy leakage, harmful content, in the context of societal impacts. |

## Timeline

| Time | Block | Type | Notes |
|------|-------|------|-------|
| 0:00–0:05 | Welcome, what today is for, the University policy in one minute | Opening | |
| 0:05–0:25 | Activity: Pre-course mindmap (LA10, part 1) | Activity | Individual, then pairs; keep the mindmaps! |
| 0:25–0:35 | Presentation: A very short history of AI | Presentation | H01, H02 |
| 0:35–0:50 | Activity: Quick timeline challenge (LA01, condensed) | Activity | Groups of 5–6 |
| 0:50–1:05 | Presentation: How GenAI generates text | Presentation | MM01 |
| 1:05–1:25 | Presentation: What it can't do, what people think it does, and why it matters at scale | Presentation | MM03, MM05, EPR05 |
| 1:25–1:30 | Wrap-up: three things to remember; pointer to session 2 | Closing | |

## Presentation

### Slide outline

**Welcome (0:00–0:05, 2 slides)**
- Today in one sentence: understand the tool you already use, and decide how *you* want to use it.
- The University's GenAI policy: allowed (brainstorm, explain, code you can explain), not allowed (undisclosed submission, closed-book, other people's data), always disclose. One slide, we come back to it.

**A very short history of AI (0:25–0:35, 5 slides)**
- 1950s–60s: the term "artificial intelligence"; symbolic AI, rule-based systems; big promises.
- The first AI winter (1970s) and the second (late 1980s): why funding and enthusiasm collapsed.
- 1990s–2010s: machine learning, data and compute; the AI you used without noticing — search ranking, recommendations, satnav routing.
- 2017→: transformers; 2022→: chat interfaces make it *generative* and *conversational*.
- What's different about GenAI: it produces new content rather than ranking, classifying or routing existing things.

**How GenAI generates text (0:50–1:05, 6 slides)**
- "Next-word prediction" as the working model: given everything so far, what's a likely next piece?
- Tokens, not words (show a sentence split into tokens).
- Where the "likely" comes from: patterns in a very large amount of text.
- Context: the prompt and everything already generated steer the prediction.
- Randomness: the same prompt can give different answers — and that's by design.
- The mental model to keep: a very good autocomplete that has read a lot, not a database, not a mind.

**What it can't do, what people think it does, and why it matters at scale (1:05–1:25, 8 slides)**
- Hallucination: fluent, confident, wrong. Example: an invented citation or a non-existent library function.
- The context window: the model only "sees" so much; long conversations drift.
- No true understanding: it has no model of the world to check against.
- Cost: compute, energy and water behind every query.
- Bias: what's in the data comes out in the answers.
- At scale: one student's hallucinated citation is a bad mark; the same failure across millions of users is misinformation. Add privacy leakage (your pasted data, or someone's training data, reappearing) and harmful content — these are the *societal* versions of the limitations above.
- Myths board: "it searches the internet", "it knows when it's wrong", "it learns from my chat", "it's neutral", "it's basically a person". For each: what's actually true.
- What this means for you: verify, and know *what kind* of task you gave it.

### Speaker notes

**History (H01, H02).** Make the pattern the point, not the dates: big promise → limits hit → funding gone → quiet progress → new breakthrough. Ask the room *"what AI did you use this morning before ChatGPT?"* — phone unlock, maps, spam filter, playlist — and use that to draw the line between *earlier* AI (classify, rank, route) and *generative* AI (produce). Misconception to address: "AI was invented in 2022".

**Generation (MM01).** Do one live prediction on a slide: "The capital of France is …" — students shout the next word; then "The capital of Freedonia is …" — they realise the model will still produce *something*. That's the seed for hallucination later. Keep the vocabulary to *token*, *context*, *likely*: session 2 adds training, and the unplugged simulation makes this concrete.

**Limitations, myths and harms (MM03, MM05, EPR05).** Return to the mindmaps from the opening: *"who wrote that it searches the internet?"* — several will have. Take the myths one by one and ask for a show of hands before revealing. The "at scale" slide is deliberately here rather than in session 4: session 3's use-case activity assumes students can already name hallucination, misinformation, privacy leakage and harmful content as *kinds* of failure — session 4 then adds the data-management and policy side. Close with the question they'll carry through the day: *"if it can be confidently wrong, what do I have to do before I use its output?"*

## Activities

### Activity: Pre-course mindmap — *LA10, part 1* (20 min)
**Source:** learning-activities/activities/10-ai-pre-post-mindmap.md · **ILOs:** MM05 · **Adaptation:** shortened from ~25 to 20 min; part 2 (post-course mindmap) becomes 15 min of homework after session 4 instead of an in-class session.

**Setup** — Individual, on paper (A4 provided) or a phone/laptop drawing app. No GenAI tools in this activity.

**Steps**
1. (1 min) Write "GenAI" in the middle of the page.
2. (12 min) Branch out everything you currently believe about it: what it is, how it works, what it can and can't do, where it's used, what worries you. There are no wrong answers — this is a snapshot, not a test. Starter branches if you're stuck: *What it is · What it can do · What it can't do · Risks · Tools I've used*.
3. (5 min) Swap with a neighbour: find one thing you both wrote and one thing only one of you wrote.
4. (2 min) Photograph or keep your mindmap. You will need it after session 4.

**Debrief** — Collect 4–5 "only one of us wrote it" items on a flipchart; leave it up all day. Draw out for MM05: the items people disagree on are exactly the misconceptions the day will test.

### Activity: Quick timeline challenge — *LA01, condensed* (15 min)
**Source:** learning-activities/activities/01-ai-history-timeline.md · **ILOs:** H01, H02 · **Adaptation:** condensed from 45 to 15 min — 8 milestone cards instead of a full set, no cross-group comparison round, reveal done as one whole-class round. Placed *after* the history presentation rather than before it (the source recommends before) because there is no time for the discovery version; the surprise cards still do their work.

**Setup** — Groups of 5–6. Each group: one printed blank timeline strip (1700 → "the future"), 8 milestone cards, glue or tape. Cards (from the source, with the deliberate surprises): *first chess-playing "robot"* (Mechanical Turk, 1770), *the term "artificial intelligence" coined* (1956), *first chatbot* (ELIZA, 1966), *expert systems in industry* (1980s), *computer beats world chess champion* (1997), *voice assistants on phones* (2011), *transformer architecture* (2017), *chat-style GenAI for the public* (2022).

**Steps**
1. (7 min) Place the cards on the timeline where your group thinks they belong.
2. (5 min) Whole-class reveal, one card at a time: groups hold up where they put it; instructor gives the real date.
3. (3 min) Show of hands: which card surprised you most?

**Debrief** — Draw out for H01: the long tail (a "chess robot" in the 1770s), and the boom–bust rhythm. For H02: which cards are *generative* and which are earlier AI that classifies, ranks or plays a fixed game.

## Assessment in this session
Quiz items Q1 (MM01) and Q2 (MM03) in `assessment/formative-items.md` can be run as a 3-minute show-of-hands at the start of session 2. The mindmap is the pre-half of reflection R1 (MM05).

## Homework / preparation for next session
None before session 2. (Homework for session 3 is set at the end of session 2.)

## Instructor notes
- 60 students → 10–12 groups for the timeline. Have the cards pre-cut in envelopes; handing out loose cards costs 5 minutes you don't have.
- If running long, cut the myths board to three myths; don't cut the timeline reveal — the Mechanical Turk card is the moment the day's theme (things are older and messier than they look) lands.
- Room has no whiteboard: use the flipchart for the "only one of us wrote it" list and keep it visible all day.
