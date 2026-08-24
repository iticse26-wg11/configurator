# Coverage report

Generated 2026-08-24 from `config/config.yaml` (example: one-day workshop).

## Selected ILOs

| ILO | Taught (session) | Practised (activity) | Assessed (item) |
|-----|------------------|----------------------|-----------------|
| H01 | S1 | LA01 (condensed) | — (out of scope) |
| H02 | S1 | LA01 (condensed) | — |
| MM01 | S1, S2 | LA07 | Q1 |
| MM02 | S2 | — presentation only (LA15 did not fit the activity budget) | Q3 |
| MM03 | S1 | — presentation only (LA09 excluded by constraints) | Q2 |
| MM04 | S3 | LA13 (adapted) | Q4 |
| MM05 | S1 | LA10 part 1 (in class) + part 2 (homework) | R1 |
| MM06 | S3 | LA13 (adapted) | R2 |
| EPR02 | S2 | LA07 | — |
| EPR03 | S4 | — presentation only (LA15 did not fit) | — |
| EPR04 | S4 | — presentation only (LA03 did not fit); the policy-check steps in S3/H2 practise the "follow the policy" half | — |
| EPR05 | S4 | — presentation only (LA09 excluded by constraints) | — |
| EPR06 | S4 | — presentation only (LA06 did not fit) | — |
| EPR07 | S4 | — presentation only (LA02 did not fit); the toolkit is applied in LA11 Part 1 evidence | — |
| EPR08 | S3 | LA12 (homework H1 + in-class discussion) | R3 |
| EPR10 | S4 | LA11 (shortened) | LA11 grid |
| EPR11 | — (no dedicated presentation; framed in S4 closing) | — | R4 (use plan) |
| EPR12 | S4 | LA11 (shortened) | — (out of scope; LA11 grid policy column evidences it) |
| EPR13 | S4 | LA11 closing discussion | — |
| EPR14 | S4 | LA11 closing discussion | — |
| CS01 | S2 | homework H2 (adapted from LA14 pre-sessional) | — |
| CS02 | S2 | LA07 | — |
| CS03 | S2 | homework H2 (adapted from LA14 pre-sessional) | — |
| CS04a | S3 | LA13 (adapted) | — |
| CS04b | S3 | LA13 (adapted) | — |

**Summary:** 25 selected ILOs; 15 have an in-class or homework activity; 10 are presentation-only. All 9 ILOs in the assessment scope have an item.

## Not included
- Excluded by configuration: **EPR09** (`exclude_ilos`).
- Sub-topics not selected: **MM.explainability** (MM07, MM08), **EPR.resources-labor** (EPR01), **CS.collaboration** (CS05, CS06, CS07).

## Adaptations and generated material
| Activity | Change | Why |
|----------|--------|-----|
| LA01 AI History Timeline | Condensed 45 → 15 min: 8 cards, no cross-group round, run after the history presentation | H has weight 1 → 15 min activity budget. **Exceeds the skill's ≤30 % shortening guideline**; done anyway because a 15-min "generated" alternative would be a worse version of the same thing. Flagged for the educator. |
| LA10 AI Pre/Post Mindmap | Part 1 25 → 20 min in S1; part 2 moved to 15 min homework after S4 | MM activity budget; no in-class time in S4 |
| LA11 AI Evaluation Frameworks + Policies | 90 → 65 min; 3 case cards; 2 policy handouts (University policy + OECD), EU AI Act dropped; closing discussion doubles as course wrap-up | EPR activity budget; the attached policy is used as the university handout per its `how_to_use` |
| LA13 AI Use Case Analysis | 70 → 50 min: 2 cases × 15 min + 20 min discussion; concrete tasks fixed (regex validator; policy summary) | CS activity budget; tasks chosen to be testable and to reuse the attached policy |
| LA14 Application of AI to Specific Problem | Only the pre-sessional part used, 60 → 25 min, as homework H2 covering CS01/CS03 | CS05/CS06 not selected; in-class part (90–120 min) far over budget |
| LA07, LA12 | none | — |

No generated mini-activities were needed.

## Activities considered but not used
| Activity | Reason |
|----------|--------|
| LA09 AI Alignment Lab | Constraint: requires Colab and a 7B-parameter model download; configuration says no local model downloads / no paid accounts. MM03, EPR05 → presentation-only. |
| LA15 AI Model Pipeline (45 min, MM02/EPR03) | Budget: MM and EPR activity budgets exhausted by LA07/LA10 and LA12/LA11. **First thing to add if the course grows by 45 min.** |
| LA03 Basic LLM Output Evaluation (60, EPR04) | Budget. Would also use the attached policy well. |
| LA06 LLM Output-Checking (60, EPR06) | Budget; MM08 not selected. |
| LA02 Content Detection Limitations (60–90, EPR07) | Budget. |
| LA04 AI Application Project (120, EPR11/13/14) | Budget; far over any single session. EPR11 is instead assessed by reflection R4. |
| LA05, LA08 | No selected ILOs (MM07; EPR01/EPR09). |

## Attachments
- **Example University policy on student use of generative AI** → `00-overview.md` *Policies* (quoted); policy-check steps in S3 activity and homework H2; AI use statement in W2 and R4; policy handout in S4 LA11; EPR03/EPR04 presentation in S4; summarisation task in S3.

## Time reconciliation
| | Contact | Presentation | Activities | Homework |
|---|---|---|---|---|
| Configured | 360 min | 144 min (40 %) | 216 min | 60 min |
| Built | 360 min | 145 min (40.3 %) | 215 min | 60 min |
| Difference | 0 | +1 (5-minute rounding) | −1 | 0 |

Per topic (activities): H 15 · MM 65 (LA07 45 + LA10 20) · CS 50 (LA13) · EPR 85 (LA12 20 + LA11 65) — matches the weight-derived budget of 16.6 / 66.5 / 49.8 / 83.1 within rounding. Presentation blocks mix topics within sessions; approximate split H 10 · MM 55 · CS 30 · EPR 50.
