# Assessment: all selected outcomes (Mental Models; Ethics, Policy and Regulations)

![Paper lanterns rising over a lake at dusk](../figures/art-assessment.jpg)

**Type:** formative · **Formats:** quiz, reflection · **Grade share:** none (ungraded) · **ILOs assessed:** MM01–MM08, EPR01–EPR14

Every selected outcome has exactly one item here, or a built-in check in an activity (listed at the end). Quizzes are run as live polls or a shared form in the closing block of each day; answers are revealed immediately. Reflections are written in the class chat or in the student's own document.

## Items

### Day 1 quiz (end of session 2) — Q1–Q10

### MM01 — quiz (Q1)
**Prompt / question** — A chat AI produces its answer by: (a) searching a database of facts and copying the best match; (b) repeatedly predicting a likely next word given the prompt and what it has written so far; (c) running the rules a programmer wrote for each question; (d) asking a human operator when unsure.
**What a good answer shows** — (b). Distractor (a) probes the "it looks things up" myth; (c) probes the "hand-coded rules" model of software; (d) probes the belief that there is a human in the loop at answer time.
**Where it sits** — session 2 closing, day 1 quiz.

### MM05 — quiz (Q2)
**Prompt / question** — True or false: when you correct a chat AI during a conversation, the underlying model is updated so it will not make that mistake for other users.
**What a good answer shows** — False. The model does not change while you chat; only the current conversation acts as memory. Probes the "it learns from me live" misconception.
**Where it sits** — session 2 closing, day 1 quiz.

### MM03 — quiz (Q3)
**Prompt / question** — In the session 1 simulation, your group's model only looked at the last word before choosing the next. Which limitation of real systems does this illustrate, even though they look back much further? (a) hallucination; (b) the context window; (c) computational cost; (d) bias.
**What a good answer shows** — (b). Distractors probe whether students can tell the limitations apart rather than treating "limitations" as one blob.
**Where it sits** — session 2 closing, day 1 quiz.

### EPR02 — quiz (Q4)
**Prompt / question** — Two groups ran the simulation with the same prompt but different training texts and got very different outputs. Which statement about real models follows? (a) Output quality depends only on the prompt; (b) What is common in the training data becomes common in the output, so who is represented in the data shapes the model's behaviour; (c) Training data has no effect once the model is trained; (d) Models always balance out differences in their data.
**What a good answer shows** — (b). Distractor (a) probes over-crediting the prompt; (c) and (d) probe the belief that training is neutral.
**Where it sits** — session 2 closing, day 1 quiz.

### MM02 — quiz (Q5)
**Prompt / question** — Put these stages in order: alignment (fine-tuning and RLHF) · your prompt · data collection · pre-training. Then: at which stage does the "cutoff date" arise?
**What a good answer shows** — Data collection → pre-training → alignment → your prompt. The cutoff date arises at data collection (the text stops at some point). Probes whether students have the pipeline in sequence and can attach a limitation to its stage.
**Where it sits** — session 2 closing, day 1 quiz.

### MM02 companion / RLHF — quiz (Q6, also MM02)
**Prompt / question** — Where does a chat AI's politeness and its refusal to answer some requests mainly come from? (a) the raw internet text it was pre-trained on; (b) alignment, where human raters' preferences shaped its behaviour; (c) a filter that checks a list of banned words; (d) the user's settings.
**What a good answer shows** — (b). Distractor (a) probes conflating pre-training and alignment; (c) probes the "simple filter" model; (d) probes over-crediting the user.
**Where it sits** — session 2 closing, day 1 quiz.

### EPR03 — quiz (Q7)
**Prompt / question** — You paste a paragraph containing a friend's full name and medical condition into a free chat tool to "make it sound better". Name two distinct risks from the pipeline worksheet that this creates, and say who could have prevented each.
**What a good answer shows** — Any two of: disclosure of sensitive information; unclear data retention (it may be stored); loss of control over where the data is stored or which law applies (data sovereignty); possible use for future training without consent. Prevention: the user (do not paste it), the provider (retention and training policies), the regulator (rules on personal data). Probes whether students see data control as a shared responsibility that includes themselves.
**Where it sits** — session 2 closing, day 1 quiz (short free text).

### MM07 — quiz (Q8)
**Prompt / question** — A spam filter shows you the yes/no rules it used to classify your email. A chat AI, asked why it gave an answer, writes a paragraph of reasons. Which system is explainable in the XAI sense, and why does that matter for trust?
**What a good answer shows** — The spam filter: its actual decision process is visible and checkable, so you can contest a wrong decision and calibrate trust. The chat AI's paragraph is generated text about its answer, not a view of its process. Probes the confusion between an explanation and a plausible-sounding justification.
**Where it sits** — session 2 closing, day 1 quiz.

### MM08 — quiz (Q9)
**Prompt / question** — You cannot see inside a chat model. Which of these is NOT a useful strategy for judging one of its answers anyway? (a) check the claim against a trusted source; (b) ask the same question phrased differently and compare; (c) ask the model to rate its own confidence and accept its number; (d) ask it for its source and confirm the source exists.
**What a good answer shows** — (c). The model's self-reported confidence is another generated output. Distractors (a), (b), (d) are the strategies from the ILO; the item probes whether students treat the model's statements about itself as evidence.
**Where it sits** — session 2 closing, day 1 quiz.

### MM03 companion — quiz (Q10, also MM03 and MM05)
**Prompt / question** — A chat AI gives you a detailed, confident, well-formatted answer with three references. What can you conclude? (a) It is very likely correct; (b) Nothing yet: fluency and confidence are not evidence, and the references may not exist; (c) It is correct if the references have real-looking titles; (d) It is more reliable than a shorter answer.
**What a good answer shows** — (b). Probes the "confident means correct" misconception and the hallucinated-reference failure mode.
**Where it sits** — session 2 closing, day 1 quiz.

### Day 2 quiz (end of session 4) — Q11–Q18

### EPR05 — quiz (Q11)
**Prompt / question** — Match each to its name: (1) the tool invents a Python library that does not exist; (2) the tool reproduces someone's phone number that appeared in its training text; (3) a false health claim is repeated to millions of users in a fluent voice. Names: hallucination · misinformation at scale · privacy leakage.
**What a good answer shows** — 1 hallucination, 2 privacy leakage, 3 misinformation at scale. Probes whether students can distinguish the limitation types and connect them to societal impact.
**Where it sits** — session 4 closing, day 2 quiz.

### EPR04 — quiz (Q12)
**Prompt / question** — The same wrong answer from a chat tool is "cheap" in one context and "expensive" in another. Give one example of each from your studies or future work, and state what you must know about a context before using AI output in it.
**What a good answer shows** — Cheap: brainstorming project ideas, a first draft you will rewrite. Expensive: submitted coursework, a medical or legal summary, code deployed to users. You must know the rules (policy, regulation, assessment rules) that govern where the output will be used. Probes the link between output shortcomings and context-specific rules.
**Where it sits** — session 4 closing, day 2 quiz (short free text).

### MM04 — quiz (Q13)
**Prompt / question** — Which of these is a use where a chat AI typically adds real value for a CS1 student, provided the output is checked? (a) Explaining a concept a second way after the textbook did not land; (b) Producing the final answer to a graded exercise; (c) Looking up today's lecture room change; (d) Deciding your grade.
**What a good answer shows** — (a). Distractor (b) probes appropriateness (substitution in assessed work); (c) probes the "it knows current facts" myth (cutoff, no access to your timetable); (d) probes accountability.
**Where it sits** — session 4 closing, day 2 quiz.

### EPR07 — quiz (Q14)
**Prompt / question** — Yesterday the tool wrote `is_leap_year`. Name the verification step that would catch a function that gets 1900 wrong, and one further step you could take if you had no way to run the code.
**What a good answer shows** — Test it on edge cases (1900 should be False; 2000 True). Without running: trace it by hand; check the rule against a trusted source; ask the tool a differently worded question about failing inputs; ask a second tool and compare. Probes whether students can name and apply concrete verification procedures.
**Where it sits** — session 4 closing, day 2 quiz.

### EPR06 — quiz (Q15)
**Prompt / question** — A tool produces plausible-looking but fake references every single time. Is it reliable, trustworthy, responsible, or none of these? Explain using the definitions.
**What a good answer shows** — Reliable (it behaves consistently) but not trustworthy (you have no good reason to rely on it for this task) and not responsible (no accountability for the harm). Probes whether students can pull the three terms apart rather than using them as synonyms.
**Where it sits** — session 4 closing, day 2 quiz.

### EPR01 — quiz (Q16)
**Prompt / question** — Name four different kinds of resource needed to build and run a large AI system, and for one of them say where it comes from and who bears the cost.
**What a good answer shows** — Any four of: minerals for chips; electricity for training and answering; water for cooling; human labour for labelling, rating and moderation; data written by the public; land and buildings for data centres. The follow-up should name a real origin (a mining region, a data-labelling workforce, a river or aquifer) and a cost-bearer. Probes whether students can see past the chat window.
**Where it sits** — session 4 closing, day 2 quiz (short free text).

### EPR09 — quiz (Q17)
**Prompt / question** — If a tool can write routine code, which of these is the best-supported conclusion about the job market you are entering? (a) Programmers will not be needed; (b) The tasks expected of a junior developer shift toward specifying, verifying, integrating and taking responsibility for code, while some routine tasks and some jobs behind the tools (labelling, moderation) are created or displaced elsewhere; (c) Nothing changes; (d) Only senior roles are affected.
**What a good answer shows** — (b). Distractors probe both the doom and the denial positions; the item checks whether students can analyse effects on tasks, expectations and the wider labour market rather than predict a single outcome.
**Where it sits** — session 4 closing, day 2 quiz.

### EPR12 — quiz (Q18)
**Prompt / question** — You are handed a two-page university GenAI policy. Write the four questions you would ask of it to work out whether and how it applies to your programming assignment.
**What a good answer shows** — Who does it apply to? What does it allow, forbid and require (for example disclosure)? What counts as GenAI use under it? What are the consequences of breaking it? Optionally: does it differ by course or assessment type? Probes the skill of interpreting a policy for a context rather than recalling a specific rule.
**Where it sits** — session 4 closing, day 2 quiz (short free text).

### Reflections — R1–R6

### MM06 — reflection (R1)
**Prompt / question** — (In the LA13 observation form.) Was using the chat tool for the leap-year task appropriate for a CS1 student? Give one task-related reason, one practical reason and one ethical reason, and say whether your answer would change if this were your graded assignment.
**What a good answer shows** — Weighs the task (small, checkable, but exactly the skill CS1 teaches), the practical side (could verify by tracing; free tool available) and the ethical side (disclosure, fairness to peers, institutional rules). A good answer distinguishes the course exercise from an assessed one.
**Where it sits** — session 3, in-class, inside LA13.

### EPR08 — reflection (R2)
**Prompt / question** — (LA12 individual step.) Which parts of the leap-year task did the AI produce? Which parts do you fully understand? Could you write the function again tomorrow without AI? Was your use augmentation or substitution, and what is one habit that would keep it on the augmentation side?
**What a good answer shows** — Honest sorting of the work; explicit link between "cannot do it again alone" and cognitive debt; a concrete countermeasure (attempt first, explain the output in own words, practise the skipped skill).
**Where it sits** — session 3, in-class, inside LA12.

### EPR10 — reflection (R3)
**Prompt / question** — (Chat, principles block.) Rate the chat tool you used yesterday on transparency and on accountability, 1–5 each, and justify each rating in one sentence.
**What a good answer shows** — Uses the principle's meaning (transparency: can you see how it decided and what it was trained on; accountability: who answers if it is wrong) and cites evidence from the course (no view inside; explanation is generated; terms of service).
**Where it sits** — session 4, in-class, principles block.

### EPR11 — reflection (R4)
**Prompt / question** — (Responsible-use plan, written individually.) Answer the five prompts: tasks I will and will not use GenAI for; how I will verify; how I will record use (tool, date, prompt, what I kept); what I will never paste in; which institutional rule applies and where it lives.
**What a good answer shows** — Specific to their studies, includes a documentation habit, names a verification step per use, and cites where the applicable rule is found.
**Rubric** — *Specificity:* generic / some concrete tasks / named tasks with reasons. *Verification:* absent / one generic step / a step matched to each use. *Documentation:* absent / "I will note it" / a format (tool, date, prompt, kept). *Rules:* none / "follow the rules" / names the policy and where to find it.
**Where it sits** — session 4, in-class, 1:15–1:25 block; kept by the student.

### EPR13 — reflection (R5)
**Prompt / question** — (Chat, closing.) One rule you would add to your university's GenAI policy if you had written it, and one group whose interests the current rules probably do not represent.
**What a good answer shows** — Recognises that policies are written by particular parties, names a group left out (students, data workers, people whose text was scraped) and proposes a rule that reflects that group's interest.
**Where it sits** — session 4 closing.

### EPR14 — reflection (R6)
**Prompt / question** — (Chat, principles block.) In one sentence: what does "you are responsible for the code you ship, whoever wrote it" mean for how you use GenAI in a programming course?
**What a good answer shows** — Connects the discipline's norm to concrete practice: verify, understand, disclose, do not submit what you cannot explain.
**Where it sits** — session 4, in-class, principles block.

## Reused from activities

- **LA15 AI Model Pipeline** (session 2): formative, the room's completed worksheet (stage matching, risk placement, process explanation, responsibility answers). Covers MM02 and EPR03.
- **LA08 Anatomy of (Another) AI System** (session 4): formative, the room's four-box slide judged on depth and specificity of research and connection to earlier discussion. Covers EPR01 and EPR09.
