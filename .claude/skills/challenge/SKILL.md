---
name: challenge
description: Adversarially search for classical reproductions or dequantizations of a quantum-advantage claim or method page, and record them.
---

Argument: `$ARGUMENTS` is a page id under `content/claims/` or `content/methods/` (or a topic).

Your job is to find reasons the page is too optimistic. Read `AGENTS.md`, then:

1. Read the page. Extract the concrete claim: system size, observable, accuracy, runtime,
   hardware, and the classical baseline the authors compared against.
2. Search for: tensor-network reproductions (belief propagation, PEPS, MPS with large bond
   dimension), Pauli-path or sparse-Pauli propagation, neural quantum states, Clifford
   perturbation, noise-induced classical simulability (Schuster et al. style), dequantization
   results (Tang, Chia, Gharibian and Le Gall), and simple heuristics (HCI, DMRG, AFQMC for
   chemistry claims). Search citing papers of the claim on Google Scholar or Semantic Scholar.
3. For each reproduction found: who, when, method, hardware, cost, and whether it matched or beat
   the quantum result. Compute time-to-refute from the claim's date.
4. Update the page: for a claim, fill `claim.refuted`, `refutation_date`, `refuted_by`,
   `time_to_refute` and the `## Refutation` section. For a method, add to `## Known limits` and
   lower `quantum_easiness` or the verdict if warranted.
5. If you find nothing after a genuine search, say so on the page ("no classical reproduction
   found as of <date>; searched: …") and leave the claim standing.
6. Run `python tools/validate.py` and `python tools/verify_refs.py`.
