---
type: application
id: p450-drug-metabolism
title: Cytochrome P450 drug metabolism
title_zh: 细胞色素 P450 药物代谢
summary: P450 Compound I is a textbook strongly correlated active site and the subject of the best-known pharmaceutical resource estimate (1,426–2,158 logical qubits, 4.3–8.3e9 Toffoli). But the decision pharma makes, which site of a drug is metabolised, is already predicted to 82–91% top-2 accuracy with DFT descriptors, and the errors that matter for clearance and drug–drug interactions come from sampling and induced fit, not from the active-site electronic structure.
summary_zh: P450 的 Compound I 是教科书级的强关联活性位点，也是最著名的制药资源估计对象（1,426 到 2,158 个逻辑比特，4.3 到 8.3e9 个 Toffoli）。但药企要做的决策，即药物的哪个位点被代谢，用 DFT 描述符已经能达到 82% 到 91% 的 top-2 准确率；影响清除率和药物相互作用的误差来自采样和诱导契合，而不是活性位点的电子结构。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "doublet and quartet states of Compound I are near-degenerate and CCSD(T) and DMRG disagree on the doublet; Goings et al. find DMRG converges the CAS(63e,58o) model and argue advantage requires models large enough to balance dynamic and multiconfigurational correlation"}
  quantum_easiness: {level: conditional, note: "phase estimation on the CAS(63e,58o) model: 1,426–2,158 logical qubits and 4.3–8.3e9 Toffoli (Goings et al.), recompiled to ~1,200 logical and 5e8 Toffoli (Babbush et al. 2025); initial-state overlap for the heme–oxo cluster not reported"}
  willingness_to_pay: {level: first-hand, note: "Boehringer Ingelheim researchers co-authored the drug-design perspective and the P450 resource study, documenting direct industry interest. Their discussion of seconds-scale energy evaluations concerns ensemble workflows, not a P450-specific acceptance or procurement threshold."}
resources: {logical_qubits: "1,426–2,158 (Goings 2022); ~1,200 (Google 2025 recompilation)", gates: "4.3–8.3e9 Toffoli; ~5e8 after recompilation", note: "CAS(63e,58o) Compound I model, 116 system qubits; PsiQuantum–Boehringer report a 234× runtime reduction with improved tensor factorisation and active-volume compilation"}
related:
  applications: [homogeneous-catalysis, protein-ligand-binding]
  problems: [ground-state-energy, excited-states]
  methods: [phase-estimation, embedding-divide-and-conquer]
  questions: [embedding-fragment-size-vs-correlation-length]
references:
  - {arxiv: "2202.01244", title: "Reliably assessing the electronic structure of cytochrome P450 on today's classical computers and tomorrow's quantum computers", authors: "J. J. Goings, A. White, J. Lee, et al., N. C. Rubin", year: 2022, note: "Table 4: 1,426–2,158 logical qubits, 4.3–8.3e9 Toffoli"}
  - {arxiv: "2511.09124", title: "The Grand Challenge of Quantum Applications", authors: "R. Babbush et al. (Google Quantum AI)", year: 2025, note: "recompiled P450 estimate ~1,200 logical qubits, 5e8 Toffoli"}
  - {arxiv: "2501.06165", title: "Faster quantum chemistry simulations on a quantum computer with improved tensor factorization and active volume compilation", authors: "A. Caesura et al. (PsiQuantum, Boehringer Ingelheim)", year: 2025, note: "234× runtime reduction on P450"}
  - {arxiv: "2502.15882", title: "Fast quantum simulation of electronic structure by spectrum amplification", authors: "G. H. Low et al. (Google Quantum AI)", year: 2025, note: "4–195× Toffoli reductions on chemistry benchmarks"}
  - {arxiv: "2301.04114", title: "Drug design on quantum computers", authors: "R. Santagati et al. (Boehringer Ingelheim and others)", year: 2023, note: "pharma-authored perspective; bottleneck is sampling of large systems at finite temperature"}
  - {arxiv: "2208.02199", title: "Is there evidence for exponential quantum advantage in quantum chemistry?", authors: "S. Lee et al.", year: 2022}
---

## Who needs it

Pharmaceutical discovery and DMPK (drug metabolism and pharmacokinetics) groups. Cytochrome P450 enzymes, mainly CYP3A4, 2D6 and 2C9, metabolise most small-molecule drugs. The decisions are which atom of a candidate is oxidised first (site of metabolism, SoM), how fast it is cleared, whether it inhibits or induces a P450 and so causes drug–drug interactions, and whether a metabolite is reactive. Boehringer Ingelheim has co-authored both the field's perspective article [5] and a P450 resource estimate [3], which is why this scenario appears in most pharma quantum roadmaps.

## Bottleneck

The active-site chemistry is hard. Compound I, the iron(IV)-oxo porphyrin radical cation that does the oxidation, has near-degenerate doublet and quartet states, and CCSD(T) and DMRG disagree on the doublet. Goings et al. built CAS models up to (63e,58o) and found that DMRG converges them; their conclusion is that a quantum advantage problem arises only for models large enough to balance dynamic and multiconfigurational correlation, not for the active-space models studied [1].

Active-site electronic energies are only one part of predicting drug metabolism. Conformational sampling, accessibility, solvation and protonation also enter the workflow. The pharmaceutical perspective by Santagati et al. discusses the wider challenges of connecting quantum calculations to drug design [5]. The industry-co-authored resource study says that ensemble workflows would need individual energy evaluations on the scale of seconds or faster [3, Introduction]. It does not define a P450-specific accuracy, acceptance or procurement threshold.

## Computational problems

- [Ground-state energy](../problems/ground-state-energy.html) and [excited states](../problems/excited-states.html) of the heme–oxo cluster: spin-state ordering of Compound I and hydrogen-abstraction barriers.
- Sampling of substrate poses in the pocket and of the protein at 300 K, a classical MD and free-energy problem that dominates the practical error.

## Best classical today

DMRG and DMRG-NEVPT2 on CAS(63e,58o) models, converged according to Goings et al. [1]; DLPNO-CCSD(T) on cluster models; QM/MM with DFT for barriers; empirical and ML SoM predictors for the actual decision. Lee et al.'s general argument applies: the single-centre heme cluster is exactly where classical heuristics work best [6].

## Best quantum today

Phase estimation on the CAS(63e,58o) model is the most-optimised chemistry instance in the literature. Goings et al. estimate 1,426–2,158 logical qubits and 4.3–8.3×10^9 Toffoli gates [1]; Google's 2025 recompilation gives about 1,200 logical qubits and 5×10^8 Toffoli [2]; PsiQuantum with Boehringer report a 234× runtime reduction from improved tensor factorisation and active-volume compilation [3]; spectrum amplification yields further 4–195× reductions on benchmark instances [4]. The system register is 116 qubits; the total with ancillas and distillation is order 10^3 logical qubits, beyond a five-year 100-logical-qubit horizon.

## Verdict

Surviving, with direct industry interest but weak evidence of value for this computation. The electronic-structure problem is genuine and the resource estimates are among the most developed in chemistry, but the same paper that produced the original estimate found DMRG converged on the active space [1]. The company co-authors describe a general speed need for ensemble calculations [3]; they do not state what accuracy on which P450 quantity would change a drug-development decision. Two things would move this page: (a) a P450 model including protein polarisation on which DMRG, SHCI and AFQMC demonstrably fail to reach the decision-relevant accuracy after orbital optimisation; (b) a written DMPK statement that a specific energetic quantity, computed to a specific tolerance and throughput, would alter a decision. Absent (b), a demonstration on (a) would remain a science result with unproven application value.
