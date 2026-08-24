# Visual elements — reference snippets

Use Mermaid (fenced ```mermaid blocks): it renders on GitHub, in VS Code and in most markdown-aware VLEs, needs no tooling, and stays editable. Keep diagrams small (≤ 12 nodes), use default styling (it adapts to light/dark themes), and always follow a diagram with a one-line caption in italics saying what to look at. Every student-facing file should have at least one figure where a concept is structural (a process, a split, a timeline, a decision). Don't decorate: if a table says it better, use the table.

Reuse library figures where they exist (copy into `<course>/figures/`): `learning-activities/activities/figures/xai-decision-tree-example.png` (LA05).

## Course at a glance (overview)
```mermaid
timeline
    title Course at a glance
    Session 1 : Where GenAI came from : How it generates text
    Session 2 : Unplugged LLM simulation : How models are made
    Session 3 : Use cases and checking : Cognitive debt
    Session 4 : Principles and policies
```

## Next-token generation loop (MM01, CS02 — LA07 handout)
```mermaid
flowchart LR
    P[Prompt / text so far] --> L[Look up likely next tokens]
    L --> S[Sample one<br>randomness / temperature]
    S --> A[Append token]
    A --> P
    A -.stop?.-> O[Output]
```

## How a model is made (MM02, EPR02, EPR03 — LA15 or session 2 handout)
```mermaid
flowchart LR
    D[Data collection<br>web, books, code, forums] --> T[Pre-training<br>next-token prediction]
    T --> F[Alignment<br>fine-tuning, RLHF]
    F --> U[Your prompt] --> G[Output]
    G --> R[(Stored? Used for training?)]
    D -. bias, consent, cutoff date .-> T
    F -. raters' preferences .-> G
```

## Augmentation vs. substitution (EPR08 — LA12 handout)
```mermaid
quadrantChart
    title Where does your GenAI use sit?
    x-axis "I could not do it without AI" --> "I could do it myself"
    y-axis "AI did the thinking" --> "AI helped me think"
    quadrant-1 Augmentation
    quadrant-2 Learning with help
    quadrant-3 Cognitive debt risk
    quadrant-4 Convenience
```

## Verify before you use it (CS04a, EPR07 — use-case handout)
```mermaid
flowchart TD
    O[GenAI output] --> C{Correct?<br>test it / check the source}
    C -- no --> X[Fix or discard]
    C -- yes --> M{Complete? Biased? Harmful?}
    M -- no --> X
    M -- yes --> E{Can I explain every line?}
    E -- no --> X
    E -- yes --> U[Use it — and disclose it]
```

## Reliable / trustworthy / responsible (EPR06)
```mermaid
flowchart LR
    R[Reliable<br>behaves consistently] --> T[Trustworthy<br>you can justify relying on it]
    T --> S[Responsible<br>accountable for its effects]
    R -. not enough on its own .-> S
```

## AI history (H01 — LA01 reveal, post-activity handout)
```mermaid
timeline
    title Older than you think
    1770 : Mechanical Turk "chess robot"
    1956 : Term "artificial intelligence"
    1966 : ELIZA, first chatbot
    1980s : Expert systems ; then AI winter
    1997 : Computer beats chess champion
    2011 : Voice assistants
    2017 : Transformers
    2022 : Chat-style GenAI for everyone
```

## Mindmap starter (MM05 — LA10)
```mermaid
mindmap
  root((GenAI))
    What it is
    What it can do
    What it can't do
    Risks
    Tools I've used
```

## Policy in one picture (EPR04, EPR12 — from a `policy` attachment)
Render the attachment's allowed / not-allowed / always rules as a three-column flowchart or a simple table; quote the policy's own wording in the nodes.
