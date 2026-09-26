# Instructions for contributors (humans and agents)

This repository is a catalogue of quantum-computing application candidates. Every page is a
Markdown file with YAML front matter under `content/`. The site at
https://yuchenguommm.github.io/practical-quantum-advantage/ is built from these files; there is
no other database. To change a verdict, change the file and open a pull request.

## What a page is

Five page types live in five folders:

| folder | type | what it describes | example |
|---|---|---|---|
| `content/applications/` | application | a scenario that a company or lab would pay for | electrolyte design, OLED emitters, derivative pricing |
| `content/problems/` | problem | the computational task behind one or more applications | ground-state energy, PDE solving, Monte Carlo expectation |
| `content/methods/` | method | a quantum (or hybrid) algorithmic approach | phase estimation, SQD, DQI, embedding |
| `content/claims/` | claim | one published "quantum advantage" claim and whether it was refuted | IBM 127-qubit utility experiment |
| `content/questions/` | question | a concrete unanswered question someone could take on | does ideal SQD sampling beat classical selection? |

The distinction between application and problem is the point of the site. Industry says
"weather forecasting is an application"; algorithm papers say "PDE solving is an application".
Both layers are kept, and linked through `related.problems` / `related.applications`.

## Three dimensions and the verdict

Every application, problem and method carries a verdict and three graded dimensions.

Verdicts: `no-go` (information-theoretically impossible or dequantized), `uneconomic` (only a
quadratic speedup, which does not pay under error-correction overhead), `surviving` (no known
obstruction, but no proof and no scaling evidence yet), `promising` (hardness evidence and a real
buyer), `unassessed`.

`dimensions.classical_hardness.level`: `reduction` (BQP- or QMA-hardness), `crypto`
(cryptographic assumption), `lower-bound` (low-degree, overlap-gap, or similar), `empirical`
(best known classical methods are slow), `none`, `unknown`.

`dimensions.quantum_easiness.level`: `proven` (polynomial-time algorithm with verified
preconditions), `conditional` (polynomial time if a stated precondition holds, e.g. overlap
≥ 1/poly, adiabatic gap ≥ 1/poly, decodable dual code), `heuristic`, `unknown`, `no`.

`dimensions.willingness_to_pay.level`: `first-hand` (a company or agency has stated an accuracy
or speed target in writing, or co-authored a study), `second-hand` (a plausible argument in the
literature), `none`, `unknown`.

A verdict of `promising` requires classical_hardness ≥ `lower-bound`, quantum_easiness ≥
`conditional`, and willingness_to_pay = `first-hand`. Anything weaker is at most `surviving`.

## File format

```markdown
---
type: problem
id: ground-state-energy            # must equal the filename without .md
title: Ground-state energy of molecules and materials
title_zh: 分子与材料的基态能量
summary: One or two sentences in English, 20 to 600 characters. Shown in lists and search.
summary_zh: 可选的中文摘要。
status: seed                       # seed | reviewed | disputed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "DMRG and SHCI reach chemical accuracy up to ~100 orbitals"}
  quantum_easiness:   {level: conditional, note: "needs initial-state overlap ≥ 1/poly; not guaranteed for strongly correlated systems"}
  willingness_to_pay: {level: first-hand, note: "industrial co-authors studied OLED emitters; the reported 0.0501 eV is achieved cohort error, not a buyer target"}
resources: {logical_qubits: "140–200", gates: "1e9–1e10 T", note: "for CAS(70–100)"}
related:
  applications: [oled-emitters, homogeneous-catalysis]
  methods: [phase-estimation, sqd]
  claims: [ibm-sqd-2024]
  questions: [ideal-sqd-vs-classical-selection]
references:
  - {arxiv: "2208.02199", title: "Evaluating the evidence for exponential quantum advantage in ground-state quantum chemistry", authors: "S. Lee et al.", year: 2023}
---

## Best classical
...

## Best quantum
...

## Verdict
...
```

Required body sections (checked by CI):

- application: `## Who needs it`, `## Bottleneck`, `## Computational problems`, `## Verdict`
- problem: `## Best classical`, `## Best quantum`, `## Verdict`
- method: `## Preconditions`, `## Known limits`, `## Verdict`
- claim: `## Claim`, `## Refutation`
- question: `## Why it matters`, `## What would settle it`

You may add further sections. Keep pages under about 1,200 words. Write in English; a Chinese
`title_zh` and `summary_zh` are welcome.

## Rules for evidence

1. Every application, problem, method and claim page cites at least one reference. Prefer arXiv
   IDs; CI resolves each ID against the arXiv API and compares titles, so a fabricated ID or a
   wrong title fails the build.
2. Numbers (qubit counts, gate counts, runtimes, prices) must be traceable to a reference or to a
   script under `numerics/`. State the assumptions the number depends on. Do not cite private or
   unpublished notes; if a number is your own estimate, say so and show the arithmetic.
3. Figures from `numerics/` go in `numerics/figs/` and are embedded as `![caption](../figs/name.png)`;
   the build copies that folder to the site. Commit the script and the JSON results next to the figure.
4. `willingness_to_pay: first-hand` needs a citation to a document in which the buyer speaks
   (a co-authored paper, a public RFP, a written accuracy target). A survey's opinion is
   `second-hand`.
5. When you change a verdict, say in the PR description which dimension changed and what
   evidence changed it. Do not silently soften wording.
6. Refutations are as valuable as claims. If a classical simulation reproduces a claimed
   advantage, add it to the claim page and set `refuted: true`.

## Workflow

```
python tools/validate.py       # schema, required sections, cross-links
python tools/verify_refs.py    # arXiv IDs resolve and titles match (needs network)
python tools/build.py          # writes ./site
```

Dependencies: `pip install -r requirements.txt` (PyYAML, jsonschema, markdown, jinja2, requests).

Branch from `main`, one topic per pull request. Agent-authored PRs are welcome; label them
`agent` and list the sources consulted. A maintainer merges after checking the evidence, not the
prose.

## Skills for Claude Code users

`.claude/skills/` contains four skills you can invoke from a Claude Code session opened in this
repo:

- `/survey <topic>` — research a candidate and write or update its page.
- `/challenge <claim-id>` — search for classical reproductions of an advantage claim.
- `/score <page-id>` — fill in or contest the three dimensions with cited evidence.
- `/verify-refs` — run the reference checker and fix mismatches.

## Things not to do

- Do not add a page without a verdict and at least one reference.
- Do not add marketing language ("revolutionary", "game-changing"). State what was measured.
- Do not copy abstracts verbatim; paraphrase and cite.
- Do not delete a refuted claim. Refuted claims are the most useful part of the record.
