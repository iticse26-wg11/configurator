# Session 3: Putting GenAI to work — and checking it

**Topic area:** Mental Models; Computer Science; Ethics, Policy and Regulations · **Duration:** 90 min (20 presentation + 70 activities) · **ILOs:** MM04, MM06, CS04a, CS04b, EPR08

## Learning outcomes for this session

| ID | Outcome (exact wording) |
|----|-------------------------|
| MM04 | … identify potential GenAI use cases, such as summarisation, augmented reasoning, generating content, evaluating content, ideation, and role playing, whilst recognising that these systems might make occasional mistakes. |
| MM06 | … evaluate whether GenAI is appropriate for use in specific scenarios, based on ethical, practical, and task-related considerations. |
| CS04a | … demonstrate the understanding of the need to verify and review GenAI outputs for correctness, completeness, bias, and potential harm before integrating them into a final solution. |
| CS04b | … explain limitations of GenAI verification arising from non-determinism, incomplete model transparency, and probabilistic output generation. |
| EPR08 | … explain how overreliance on GenAI can lead to cognitive debt. |

## Timeline

| Time | Block | Type | Notes |
|------|-------|------|-------|
| 0:00–0:05 | Quiz Q3 by show of hands; two homework H2 findings from the room | Opening | |
| 0:05–0:15 | Presentation: What GenAI is good for, and why you always check | Presentation | MM04, MM06, CS04a, CS04b |
| 0:15–1:05 | Activity: Use-case analysis (LA13, adapted) | Activity | Individual work, group comparison; laptops |
| 1:05–1:10 | Presentation: Cognitive debt in three minutes | Presentation | EPR08 |
| 1:10–1:30 | Activity: Personal AI use — group discussion (LA12, in-class part) | Activity | Groups of 4–5, homework H1 in hand |

## Presentation

### Slide outline

**What GenAI is good for, and why you always check (0:05–0:15, 5 slides)**
- Six things it does well: summarise, reason alongside you, generate content, evaluate content, ideate, role-play. One computing example each.
- Six ways it goes wrong: factual errors, omissions, unsupported assumptions, biased framing, security flaws, harmful consequences.
- The verification habit: before output goes into anything you submit or ship — correct? complete? biased? harmful? Can I explain it (policy: *every line*)?
- Why checking is hard: you can't reproduce an answer (non-determinism); you can't see why it said that (opacity); "probably right" is the best it offers.
- Appropriateness: for a given task, ask about ethics (whose data, whose work), practicality (can I verify it?) and the task itself (does the value come from *me* doing it?).

**Cognitive debt in three minutes (1:05–1:10, 2 slides)**
- Augmentation vs. substitution: AI helped me think, vs. AI thought for me.
- Cognitive debt: every substitution today is a skill you didn't practise; the interest is paid when you have to do it without the tool — in an exam, an interview, a production incident.

### Speaker notes

**Use cases and checking (MM04, MM06, CS04a, CS04b).** Open with two H2 findings from the room: someone will have found Copilot and ChatGPT disagreeing on a data model. *"Which one is right? How would you know?"* That question is the session. Keep the six-and-six slides fast; the activity does the work. On CS04b, be precise: verification isn't impossible, it's *limited* — you verify the artefact (does the code pass tests?), not the process (why did it produce this?).

**Cognitive debt (EPR08).** Short on purpose: students have just spent 50 minutes noticing what the tools did for them. Name the concept, give the calculator analogy both ways (mental arithmetic became optional — was that fine?), and send them into groups.

## Activities

### Activity: Use-case analysis — *LA13, adapted* (50 min)
**Source:** learning-activities/activities/13-ai-use-case-analysis-and-evaluation.md · **ILOs:** MM04, MM06, CS04a, CS04b · **Adaptation:** shortened from 70+ to 50 min — two use cases at 15 min each (source: 20 min each, 2–4 cases) and a 20-min discussion (source: 30). Half the room does the use cases in the opposite order, as the source suggests, so the discussion can compare.

**Setup** — Individual, laptop or phone, with ChatGPT (free) or Copilot. Reflection form **W2** (paper or online form). Groups of 4–5 for the discussion.

**Before you start: policy check** — you are using a free consumer tool: no personal data of others, nothing confidential. You'll be asked to write an AI use statement at the end, as the policy requires.

**Steps**
1. (15 min) **Use case A — write code.** Ask the tool for a Python function that validates a student ID in the format `s` + 7 digits and returns a clear error otherwise. Then complete the reflection form for A: correctness/quality; any factual errors, omissions, unsupported assumptions, biased framing, security flaws or harmful consequences; the added value of the tool; whether using it was appropriate. *Test the function* before you rate correctness.
2. (15 min) **Use case B — summarise a text.** Paste the University GenAI policy and ask for a five-line summary for first-year students. Complete the form for B, checking the summary line-by-line against the original.
   (Groups on the other side of the room do B then A.)
3. (20 min) **Group discussion**, then whole class. Prompts: For which task was the tool more useful? Where did it make mistakes you'd have missed without checking? For which task did ethical considerations matter most? Where did you see the best performance? Did order matter?

**Debrief** — Draw out for MM04: the tasks map onto *generate* and *summarise*, and both had occasional mistakes. For MM06: appropriateness differs — summarising a policy you must follow is a case where a wrong summary is costly. For CS04a/b: what "checking" consisted of (running tests; reading against the source), and what couldn't be checked (why it chose that regex). Every student writes a one-line AI use statement on their form.

### Activity: Personal AI use — group discussion — *LA12, in-class part* (20 min)
**Source:** learning-activities/activities/12-personal-ai-use-reflection.md · **ILOs:** EPR08 · **Adaptation:** none — pre-sessional work done as homework H1; in-class part run at the source's 15–20 min.

**Setup** — Groups of 4–5, homework sheet H1 in hand. No GenAI tools.

**Steps**
1. (10 min) Each person names one *augmentation* and one *substitution* from their week, and the one area where they think they're building cognitive debt.
2. (6 min) Group: Where does cognitive debt build up fastest? Which uses feel fine, and which feel harmful? Is some debt okay, like calculators and mental arithmetic?
3. (4 min) Whole class: collect common patterns on the flipchart, and ideas to counter them (first drafts without AI; explain the AI's output in your own words; deliberately practise the skill you're losing).

**Debrief** — Draw out for EPR08: cognitive debt is specific (which skill, which task) and manageable; the counter-measures are habits, not abstinence.

## Assessment in this session
Reflection R2 (MM06) is the *appropriateness* column of form W2. Reflection R3 (EPR08) is the last box on homework sheet H1, reviewed in step 1.

## Homework / preparation for next session
None. (Bring your H1 sheet and W2 form to session 4 if you want to refer to them.)

## Instructor notes
- Tool access is the risk: check the room's Wi-Fi and that ChatGPT free tier isn't rate-limiting at the start; have a fallback of pre-generated outputs for use case A (three variants) in case a table can't get a response.
- The regex task is chosen because the tool's answer is usually *almost* right (`^s\d{7}$` vs. forgetting the anchors) — a visible, testable mistake.
- If running long, cut discussion step 3 to five minutes rather than shortening the use cases.
