---
type: application
id: p450-drug-metabolism
title: Cytochrome P450 drug metabolism
title_zh: 细胞色素 P450 药物代谢
summary: P450 Compound I is a challenging electronic-structure model with published quantum resource estimates of 1,426–2,158 logical qubits and 4.3–8.3e9 Toffoli gates. A separate 2016 semiempirical-QM and ligand-based model placed an observed metabolism site among its top two predictions for 82–91% of compounds on seven isoform-specific test sets. This site-ranking result neither measures clearance nor shows that solving Compound I improves a drug-development decision.
summary_zh: P450 的 Compound I 是有难度的电子结构模型，已发表的量子资源估计为 1,426 到 2,158 个逻辑比特及 4.3 到 8.3e9 个 Toffoli 门。另一项 2016 年的半经验量子化学与配体模型，在七种同工酶各自的测试集中，对 82% 到 91% 的化合物将已观测到的代谢位点排在前两名。位点排序结果既不是清除率精度，也没有证明计算 Compound I 能改善药物研发决策。
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
  - {doi: "10.1021/acs.jcim.6b00233", url: "https://pubmed.ncbi.nlm.nih.gov/27753488/", title: "Predicting Regioselectivity and Lability of Cytochrome P450 Metabolism Using Quantum Mechanical Simulations", authors: "J. D. Tyzack, P. A. Hunt, M. D. Segall", year: 2016, note: "Independent test sets across seven CYP isoforms; semiempirical QM plus a trained ligand-based accessibility model; 82–91% top-2 site identification"}
---

## Who needs it

Pharmaceutical discovery and DMPK (drug metabolism and pharmacokinetics) groups. Cytochrome P450 enzymes, mainly CYP3A4, 2D6 and 2C9, metabolise most small-molecule drugs. The decisions are which atom of a candidate is oxidised first (site of metabolism, SoM), how fast it is cleared, whether it inhibits or induces a P450 and so causes drug–drug interactions, and whether a metabolite is reactive. Boehringer Ingelheim has co-authored both the field's perspective article [5] and a P450 resource estimate [3], which is why this scenario appears in most pharma quantum roadmaps.

## Bottleneck

The active-site chemistry is hard. Compound I, the iron(IV)-oxo porphyrin radical cation that does the oxidation, has near-degenerate doublet and quartet states, and CCSD(T) and DMRG disagree on the doublet. Goings et al. built CAS models up to (63e,58o) and found that DMRG converges them; their conclusion is that a quantum advantage problem arises only for models large enough to balance dynamic and multiconfigurational correlation, not for the active-space models studied [1].

Active-site electronic energies are only one part of predicting drug metabolism. Conformational sampling, accessibility, solvation and protonation also enter the workflow. The pharmaceutical perspective by Santagati et al. discusses the wider challenges of connecting quantum calculations to drug design [5]. The industry-co-authored resource study says that ensemble workflows would need individual energy evaluations on the scale of seconds or faster [3, Introduction]. It does not define a P450-specific accuracy, acceptance or procurement threshold.

A separate, industry-developed predictor uses semiempirical quantum calculations to estimate site reactivity, then a trained ligand-based model to account for isoform-specific access to the binding pocket. On independent test sets across seven CYP isoforms, an experimentally observed metabolism site appeared among its top two predictions for 82–91% of compounds [7]. This is a **top-two site-ranking metric**, not an 82–91% probability of predicting clearance, drug–drug interactions or every metabolite. The study does not isolate an error attributable to the Compound I electronic Hamiltonian, and it does not test whether replacing its reactivity model with phase estimation improves decisions.

## Computational problems

- [Ground-state energy](../problems/ground-state-energy.html) and [excited states](../problems/excited-states.html) of the heme–oxo cluster: spin-state ordering of Compound I and hydrogen-abstraction barriers.
- Sampling of substrate poses and protein conformations, with solvation and protonation, when a target prediction depends on the enzyme environment. Their contributions to error need to be measured for the specific endpoint.

## Best classical today

DMRG and DMRG-NEVPT2 on CAS(63e,58o) models, converged according to Goings et al. [1]; DLPNO-CCSD(T) on cluster models; QM/MM with DFT for barriers; and empirical or machine-learned site-of-metabolism (SoM) predictors for site ranking. The 2016 semiempirical-QM/ligand model supplies one measured SoM baseline [7], but its test-set score cannot be transferred to clearance or binding kinetics. Lee et al.'s general argument applies: the single-centre heme cluster is exactly where classical heuristics work best [6].

## Best quantum today

Phase estimation on the CAS(63e,58o) model is the most-optimised chemistry instance in the literature. Goings et al. estimate 1,426–2,158 logical qubits and 4.3–8.3×10^9 Toffoli gates [1]; Google's 2025 recompilation gives about 1,200 logical qubits and 5×10^8 Toffoli [2]; PsiQuantum with Boehringer report a 234× runtime reduction from improved tensor factorisation and active-volume compilation [3]; spectrum amplification yields further 4–195× reductions on benchmark instances [4]. The system register is 116 qubits; the total with ancillas and distillation is order 10^3 logical qubits, beyond a five-year 100-logical-qubit horizon.

## Verdict

Surviving, with direct industry interest but weak evidence of value for this computation. The electronic-structure problem is genuine and the resource estimates are among the most developed in chemistry, but the same paper that produced the original estimate found DMRG converged on the active space [1]. The company co-authors describe a general speed need for ensemble calculations [3]; they do not state what accuracy on which P450 quantity would change a drug-development decision. Two things would move this page: (a) a P450 model including protein polarisation on which DMRG, SHCI and AFQMC demonstrably fail to reach the decision-relevant accuracy after orbital optimisation; (b) a written DMPK statement that a specific energetic quantity, computed to a specific tolerance and throughput, would alter a decision. Absent (b), a demonstration on (a) would remain a science result with unproven application value.
