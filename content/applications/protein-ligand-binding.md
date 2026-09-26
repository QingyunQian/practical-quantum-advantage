---
type: application
id: protein-ligand-binding
title: Protein–ligand binding energies
title_zh: 蛋白质与配体结合能
summary: IBM, Cleveland Clinic and RIKEN used quantum sampling within embedded-fragment calculations for two protein–ligand complexes of 11,608 and 12,635 atoms. The largest circuit used 94 noisy qubits. Their fixed-geometry binding energies agreed approximately with a classical EWF-CCSD calculation, but the minimal-basis results had the wrong sign and the work did not compute binding free energies. The authors explicitly make no quantum-advantage claim.
summary_zh: IBM、克利夫兰诊所和 RIKEN 对两个分别含 11,608 和 12,635 个原子的蛋白质与配体复合物做了碎片嵌入计算，最大电路使用 94 个有噪声的物理比特。固定结构的结合能与经典 EWF-CCSD 结果大致相符，但最小基组结果的符号有误，也没有计算结合自由能。作者明确没有宣称量子优势。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "classical EWF-CCSD was run on the same complexes; DMRG provided lower fragment energies in the three reported benchmarks. No equal-accuracy comparison against an optimized classical full workflow establishes hardness"}
  quantum_easiness: {level: heuristic, note: "quantum samples select determinants for classical diagonalization; no general guarantee that sampling beats classical selection at a fixed error and total cost"}
  willingness_to_pay: {level: second-hand, note: "drug discovery values binding free energies, but the paper reports fixed-geometry electronic binding energies, without a buyer-defined accuracy or throughput target"}
resources: {logical_qubits: "up to 94 noisy physical qubits per fragment; no logical qubits demonstrated", gates: "21,006 circuits, 3.0e9 measurement outcomes, >239 h of cumulative QPU time", note: "two 156-qubit Heron r2 processors, with classical fragment diagonalization on Fugaku, Miyabi-G and ROQUO across the reported calculations"}
related:
  applications: [p450-drug-metabolism, homogeneous-catalysis]
  problems: [ground-state-energy]
  methods: [embedding-divide-and-conquer, sqd]
  claims: [ibm-sqd-2024]
  questions: [embedding-fragment-size-vs-correlation-length, ideal-sqd-vs-classical-selection]
references:
  - {arxiv: "2605.01138", title: "Crossing the 12,000-atom barrier with heterogeneous quantum-classical supercomputing: quantum chemistry of protein-ligand complexes", authors: "K. M. Merz Jr., A. Shajan, D. Kaliakin, et al., S. Yunoki, M. Motta (Cleveland Clinic, RIKEN, IBM)", year: 2026, note: "two complexes; largest circuit 94 physical qubits; 21,006 circuits; 3.0e9 outcomes; >239 h"}
  - {arxiv: "2512.17130", title: "Molecular Quantum Computations on a Protein", authors: "A. Shajan et al., K. M. Merz", year: 2025, note: "Trp-cage, 303 atoms, ≤66 qubits; folding energy 55.4 vs DLPNO-CCSD 52.1 kcal/mol in STO-3G"}
  - {arxiv: "2107.04916", title: "Systematic improvability in quantum embedding for real materials", authors: "M. Nusspickel, G. H. Booth", year: 2021, note: "the EWF embedding used in the IBM runs"}
  - {arxiv: "2305.16472", title: "Some mathematical insights on Density Matrix Embedding Theory", authors: "E. Cancès, F. Faulstich, A. Kirsch, E. Letournel, A. Levitt", year: 2023, note: "only mathematical analysis of DMET-type embedding: first-order exact in the weak-coupling limit"}
  - {arxiv: "2301.04114", title: "Drug design on quantum computers", authors: "R. Santagati et al.", year: 2023, note: "pharma perspective: binding-affinity bottleneck is sampling and force fields"}
  - {arxiv: "2603.28648", title: "Hunting for quantum advantage in electronic structure calculations is a highly non-trivial task", authors: "Ö. Legeza et al.", year: 2026}
---

## Who needs it

Every pharmaceutical discovery programme. Relative binding free energies between ligand analogues decide which compounds are synthesised, and free-energy perturbation (FEP) with classical force fields is used to compare related ligands; its accuracy depends on the target and chemical series. Quantum-chemical binding energies are used as a check on the force field and for cases with metal centres, covalent inhibitors or unusual electronics. Cleveland Clinic co-authored the IBM demonstrations as a prospective user.

## Bottleneck

For many protein–ligand systems, improving one electronic energy will not by itself settle the binding-affinity prediction. Conformational sampling, solvation and protonation states also contribute to the free energy [5]. A strongly correlated metal site could make the electronic calculation more consequential, but this particular benchmark did not test one.

The IBM, Cleveland Clinic and RIKEN paper studied trypsin–benzamidine and T4 lysozyme–n-butyl-benzene [1]. Its EWF procedure [3] constructed atom-centred fragments and an MP2-informed bath; the new implementation used a 7 Å localisation radius and a 3 Å buffer. The largest reported circuit used 94 physical qubits. Across the reported runs, two processors executed 21,006 circuits, collected 3.0×10⁹ measurement outcomes and spent more than 239 cumulative hours sampling. Fugaku, Miyabi-G and ROQUO handled classical fragment calculations. The authors found fragment energies comparable with EWF-CCSD, while DMRG supplied more accurate reference energies for the three fragments they benchmarked. These figures aggregate several calculations and should not be read as the cost of one binding-energy prediction. The earlier Trp-cage calculation concerned a protein folding energy, not ligand affinity [2].

The reported binding energy is E(bound complex) − E(unbound protein) − E(ligand) for selected structures. In the STO-3G basis, both EWF-TrimSQD and classical EWF-CCSD gave *positive* binding energies for both complexes. A mixed basis and tighter bath changed the T4 result to −21.07 kcal/mol (classical EWF-CCSD: −17.31); a separately introduced long-range electrostatic correction changed trypsin to −131.32 kcal/mol (classical: −130.59) [1]. These numbers are not experimental binding free energies, and the large trypsin value should not be interpreted as measured affinity. The authors explicitly say the work is not a quantum-advantage claim [1]. Their selected-CI/DMRG comparisons used particular CPU implementations versus TrimSQD running on 128 GPU nodes; the paper notes that porting its improved diagonalization kernel to classical SCI could change the comparison. Full CI is plainly impractical for their 33–45-orbital benchmark fragments, whose Hilbert spaces they report as 10¹⁸–10²¹ determinants.

## Computational problems

- [Ground-state energy](../problems/ground-state-energy.html) of each embedded fragment, and the assembled interaction energy.
- Sampling over conformations, solvent and protonation states to obtain a binding free energy; this was outside the reported quantum workflow.

## Best classical today

For ligand ranking, compare against validated classical free-energy calculations on the same chemical series. For this paper's fixed-geometry observable, classical EWF-CCSD is the direct full-workflow comparator; its own fragment study also reports SCI and DMRG results [1]. More demanding metal-site calculations should be compared against current DMRG/SCI at the same orbital space and accuracy [6].

## Verdict

Surviving as a research direction, with no demonstrated quantum advantage. The 12,635-atom calculation establishes that the hybrid workflow can be operated at scale. Its sign-sensitive results show why the bath, basis and electrostatic treatment must be controlled before a buyer could use the output. A stronger case would specify a drug-discovery decision and target error, compare the *same* fixed-geometry energy against an optimized classical EWF/SCI/DMRG workflow including all hardware costs, and then show how any improved electronic result changes a binding-free-energy or ligand-ranking decision. A metal-site complex is one candidate, but neither a >100-orbital threshold nor a <1 kcal/mol target follows from this demonstration.
