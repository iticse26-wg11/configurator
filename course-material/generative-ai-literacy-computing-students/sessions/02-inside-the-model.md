# Session 2: Inside the model

**Topic area:** Mental Models; Computer Science · **Duration:** 90 min (45 presentation + 45 activities) · **ILOs:** MM01, MM02, EPR02, CS01, CS02, CS03

## Learning outcomes for this session

| ID | Outcome (exact wording) |
|----|-------------------------|
| MM01 | … explain how GenAI models generate output using a simplified "next-word prediction" process, recognising that real systems predict tokens and use contextual information from prompts and prior text to determine their responses. |
| MM02 | … explain, in high-level terms, the GenAI model development process, including data collection, pre-training, and alignment methods such as fine-tuning and RLHF, as well as limitations associated with these processes (e.g., biases related with data collection, dataset cutoff dates). |
| EPR02 | … identify data sources used to train GenAI models and describe how training data quality, consent, and representation shape GenAI model behaviors. |
| CS01 | … distinguish between different types of GenAI systems (e.g., web-based chatbots, coding assistants, local vs cloud-hosted models) and apply this knowledge to select an appropriate system for specific contexts. |
| CS02 | … explain operational GenAI concepts (e.g., tokens, context windows, probability distributions, and non-determinism) and use these concepts to interpret system behavior, output variability, and prompt sensitivity. |
| CS03 | … compare open-source and proprietary GenAI models and identify their main advantages and disadvantages for a given context, for example in terms of data privacy. |

## Timeline

| Time | Block | Type | Notes |
|------|-------|------|-------|
| 0:00–0:05 | Recap quiz (Q1, Q2 by show of hands); today: build one yourself | Opening | |
| 0:05–0:50 | Activity: Unplugged LLM simulation (LA07) | Activity | Groups of 5–6, dice, printed datasets |
| 0:50–1:10 | Presentation: How models are made — data, pre-training, alignment; tokens, context, randomness | Presentation | MM02, EPR02, CS02 |
| 1:10–1:25 | Presentation: Kinds of GenAI systems; open vs. proprietary | Presentation | CS01, CS03 |
| 1:25–1:30 | Wrap-up and homework briefing | Closing | Hand out homework sheets H1 and H2 |

## Presentation

### Slide outline

**How models are made (0:50–1:10, 8 slides)**
- What you just did, mapped onto a real model: your page of text = training data; your n-gram table = the learned patterns; the die = sampling.
- Step 1 — data collection: web crawls, books, code repositories, forums. Whose text? With whose consent? Who is over- and under-represented?
- Step 2 — pre-training: predicting the next token across all of it; the "knowledge cutoff" date is simply the last day of the data.
- Step 3 — alignment: fine-tuning on curated examples; RLHF — humans rate outputs, the model is nudged towards what raters prefer (and towards raters' biases).
- What each step leaves behind: gaps and bias from the data; cutoff dates; agreeableness and confident tone from alignment.
- Tokens revisited: why "strawberry has two r's" happens.
- Context window: the model's working memory; what falls out when a chat gets long.
- Probability and non-determinism: temperature; why the same prompt gives different code twice — and why that matters for testing.

**Kinds of GenAI systems (1:10–1:25, 5 slides)**
- Chatbot in a browser (ChatGPT) vs. assistant inside your editor (Copilot) vs. agent that runs tools: what each can see and do.
- Cloud-hosted vs. local: where your prompt goes, who stores it, what it costs.
- Open-source (weights you can download and inspect) vs. proprietary (an API you call): trade-offs — privacy, control, cost, capability, support.
- A decision question for any task: *what am I sending, where is it going, and who is allowed to see it?* Link to the policy: free consumer tools only for non-sensitive material.
- Homework preview: you'll compare two of these on the same prompt.

### Speaker notes

**Bridging from the simulation (MM01, MM02, CS02).** Start the presentation by asking each group for their generated sentence; write three on the flipchart. They will be different and mostly odd. *"Same prompt, same rules — why different?"* → different training pages (data) and different dice (sampling). Every concept in the next 20 minutes is a scaled-up version of something they just touched. Misconception to address: "training" as the model *reading and remembering facts* — it's pattern statistics, which is why it can produce fluent falsehoods.

**Data and consent (EPR02).** Ask *"was your training page written by someone who agreed to be in a language model?"* — the text genres in the activity (news, forum, encyclopedia, fiction) map onto real training sources. Point at representation: languages, dialects and communities that are thin in the data produce worse or stereotyped output.

**Systems (CS01, CS03).** Keep this practical for first-years: they have ChatGPT free and Copilot via the University licence. Use those two as the running example of *browser chatbot* vs. *editor assistant*, and *consumer tool* vs. *licensed tool*. Local/open-source models get one slide as the third option they'll meet later — no downloads in this course.

## Activities

### Activity: Unplugged LLM simulation — *LA07* (45 min)
**Source:** learning-activities/activities/07-unplugged-llm-simulation.md · **ILOs:** MM01, EPR02, CS02 · **Adaptation:** none (run as specified; expanded-version link not yet available in the library).

**Setup** — Groups of 5–6 (≈ 10–12 groups). Per group: one printed "training dataset" (≈ 1 page of text; different genre per group — encyclopedia entry, news story, forum thread, product reviews, short fiction, all on the same topic), one blank n-gram table (handout **W1**), pencils, one six-sided die (or a phone random-number app). No GenAI tools in this activity.

**Steps**
1. (3 min) Read your training page. Note its genre.
2. (15 min) Fill in the rows of the n-gram table for the words listed at the top: for each, which words follow it in your page, and how often. Convert the counts to die ranges (e.g. 1–3 → "the", 4–5 → "a", 6 → "an").
3. (12 min) Everyone gets the same prompt: **"The system"**. Starting from the last word, roll the die, look up the table, write the next word; repeat until you have 12 words or hit a word with no row. Do this three times to get three outputs.
4. (5 min) Pick your favourite output and write it on the flipchart with your genre.
5. (10 min) In your group, match parts of what you did to the real thing: your page → *training data*; the words you conditioned on → *context window*; the table → *learned probabilities*; the die → *sampling / temperature*. Which of the real model's limitations did you feel?

**Debrief** — Read the flipchart outputs aloud. Draw out for MM01: generation is sampling a likely continuation, one token at a time. For CS02: context (how many previous words the table looks at) and randomness explain variability and prompt sensitivity. For EPR02: the outputs sound like their sources — the model is its data.

## Assessment in this session
Quiz items Q1–Q3 (MM01, MM03, MM02) — Q3 is best run at the start of session 3.

## Homework / preparation for next session (45 min)
- **H1 — My GenAI week** (handout, 20 min): pre-sessional part of *LA12 Personal AI Use Reflection*. Log your GenAI use over the past week or two; answer the reflection questions; sort each use into *augmentation* or *substitution*. Bring it to session 3.
- **H2 — Two tools, one prompt** (handout, 25 min): adapted from the pre-sessional part of *LA14 Application of AI to Specific Problem* (shortened from 60 min; ILOs CS01, CS03). Give ChatGPT (free) and GitHub Copilot the same prompt — *"Outline the data model for a small university course-management app"* — and record: differences in quality and usefulness; what each tool could see; where your prompt went and who stores it; which you'd choose for University work under the policy, and why. **Policy check first:** don't include any real personal data in the prompt.
- Read the University GenAI policy (2 pages) before session 3.

## Instructor notes
- Prepare the five training pages and the n-gram table *before the day*; this is the biggest prep item in the course (see instructor guide). Test-fill one table yourself to choose the conditioning words — the activity dies if the prompt's last word has no row.
- If a group finishes early, have them run the prompt with a "temperature" change: only accept rolls of 1–2 (greedy) and see how repetitive it gets.
- If running long, shorten step 3 to two outputs; keep step 5 — it's where MM01/CS02 are consolidated.
