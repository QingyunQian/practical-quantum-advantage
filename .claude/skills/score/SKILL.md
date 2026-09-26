---
name: score
description: Fill in or contest the three-dimension grades (classically hard, quantumly easy, someone pays) on an existing page with cited evidence.
---

Argument: `$ARGUMENTS` is a page id (e.g. `problems/ground-state-energy`).

1. Read `AGENTS.md` for the level definitions, then read the page.
2. For each dimension, ask what the strongest evidence at each level would look like, and search
   for it:
   - classically hard: a BQP/QMA-hardness reduction for the relevant instance family; a
     cryptographic assumption; a low-degree or overlap-gap bound; or benchmark data showing the
     best classical methods (state them) fail at the sizes that matter.
   - quantumly easy: the algorithm's precondition (initial-state overlap, adiabatic gap,
     decodable dual code, block-encoding cost) and any evidence about whether it holds for real
     instances, including negative results.
   - someone pays: a document in which a buyer states an accuracy or speed target, or co-authors
     a study. Company blogs count as second-hand unless they name a target.
3. Update the `dimensions` block with a level and a one-line `note` naming the evidence. Adjust
   the verdict according to the rule in AGENTS.md. Add references.
4. In the `## Verdict` section, write two or three sentences explaining the grade and what
   evidence would change it.
5. Run `python tools/validate.py` and `python tools/verify_refs.py`.
