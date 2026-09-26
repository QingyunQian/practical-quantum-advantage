---
type: method
id: embedding-divide-and-conquer
title: Embedding and divide-and-conquer (DMET, EWF, bootstrap, projection, QDET)
title_zh: 嵌入与分而治之（DMET、EWF、bootstrap、投影嵌入、QDET）
summary: Embedding solves local fragments in an approximate environment, potentially placing a large system within a smaller quantum processor's reach. IBM's 12,635-atom protein–ligand example used up to 94 noisy physical qubits, but its fixed-geometry binding energies also had classical EWF-CCSD counterparts. Whether a fragment remains classically hard at a useful accuracy and within 100 logical qubits is open; no universal orbital or correlation-length threshold has been established.
summary_zh: 嵌入方法在近似环境中求解局部碎片，有机会让小型量子处理器参与大体系计算。IBM 的 12,635 原子蛋白质与配体案例最多用了 94 个有噪声的物理比特，但固定结构结合能也有经典 EWF-CCSD 对照。能否在 100 个逻辑比特内找到经典难解且精度足够的碎片，目前没有确定答案，也没有通用的轨道数或关联长度阈值。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "the IBM complexes also have classical EWF-CCSD results; DMRG provided lower energies for the three reported fragment benchmarks. No optimized equal-resource classical comparison or hard-fragment family is established"}
  quantum_easiness: {level: heuristic, note: "EWF is systematically improvable toward its full-system solver as the bath threshold goes to zero, but fixed-size cost and accuracy on difficult target instances remain unproven; the quantum SQD solver has no general sampling advantage guarantee"}
  willingness_to_pay: {level: second-hand, note: "Cleveland Clinic, RIKEN and IBM co-authored the protein–ligand study but no accuracy target beyond CCSD is stated; catalyst/enzyme buyers inherit from the applications"}
resources: {logical_qubits: "up to 94 noisy physical qubits per fragment in the IBM demonstration; 100-logical-qubit viability untested", gates: "fragment solver sets the cost", note: "across reported calculations: 21,006 circuits, >239 cumulative QPU hours, 3.0e9 outcomes; classical runs used Fugaku, Miyabi-G and ROQUO"}
related:
  problems: [ground-state-energy]
  applications: [protein-ligand-binding, homogeneous-catalysis, p450-drug-metabolism]
  methods: [sqd, phase-estimation, dmft-impurity-solver]
  claims: [ibm-sqd-2024]
  questions: [embedding-fragment-size-vs-correlation-length]
references:
  - {arxiv: "2605.01138", title: "Crossing the 12,000-atom barrier with heterogeneous quantum-classical supercomputing: quantum chemistry of protein-ligand complexes", authors: "K. M. Merz Jr., A. Shajan, D. Kaliakin, et al., S. Yunoki, et al., M. Motta", year: 2026}
  - {arxiv: "2512.17130", title: "Molecular Quantum Computations on a Protein", authors: "A. Shajan et al.", year: 2025, note: "Trp-cage, 303 atoms, EWF + SQD, ≤ 66 qubits, STO-3G"}
  - {arxiv: "2107.04916", title: "Systematic improvability in quantum embedding for real materials", authors: "M. Nusspickel, G. H. Booth", year: 2022, note: "Phys. Rev. X 12, 011046; the EWF scheme used by IBM"}
  - {arxiv: "2305.16472", title: "Some mathematical insights on Density Matrix Embedding Theory", authors: "E. Cancès, F. Faulstich, A. Kirsch, E. Letournel, A. Levitt", year: 2023}
  - {arxiv: "2404.03619", title: "Circuit Knitting Faces Exponential Sampling Overhead Scaling Bounded by Entanglement Cost", authors: "M. Jing, C. Zhu, X. Wang", year: 2024}
  - {arxiv: "2603.28648", title: "Hunting for quantum advantage in electronic structure calculations is a highly non-trivial task", authors: "Ö. Legeza et al.", year: 2026}
  - {arxiv: "2601.04621", title: "Classical computational simulation of the FeMo-cofactor model to chemical accuracy and its implications", authors: "H. Zhai et al., G. K.-L. Chan", year: 2026}
  - {arxiv: "2202.01244", title: "Reliably assessing the electronic structure of cytochrome P450 on today's classical computers and tomorrow's quantum computers", authors: "J. J. Goings et al.", year: 2022}
---

## How it works

All embedding schemes share one move: choose a fragment, build a small "bath" that represents the fragment's entanglement with the rest of the system, solve the fragment-plus-bath problem with a high-level method, and assemble fragment energies (democratically or self-consistently). The families differ in how the bath is built. DMET uses the Schmidt decomposition of a mean-field state (bath size = fragment size). EWF (Nusspickel–Booth) adds MP2-natural-orbital bath states controlled by a single threshold η, so the cluster grows toward the full system as η → 0 [3]. Bootstrap embedding matches overlapping fragments. Projection embedding (Manby–Miller) treats the environment with DFT. QDET (Galli) builds an effective Hamiltonian for a defect active space. Circuit cutting and entanglement forging are not embeddings: they reconstruct the full state exactly at a sampling cost exponential in the cut entanglement [5].

The largest protein demonstration studied T4 lysozyme (11,608 atoms) and trypsin (12,635 atoms) with EWF fragments and quantum-assisted determinant selection [1]. Across its reported calculations, the processors ran 21,006 circuits using up to 94 *physical* qubits, collecting 3.0 × 10⁹ outcomes over more than 239 cumulative QPU hours. Fugaku, Miyabi-G and ROQUO performed classical fragment calculations. Classical EWF-CCSD produced binding energies on the same complexes. The original authors explicitly decline to claim quantum advantage. The earlier Trp-cage study concerned folding energy [2]; it did not predict ligand affinity.

## Preconditions

1. **Converged environment.** The bath and fragment construction must reproduce the *target observable* at the required accuracy. In the protein example a 7 Å orbital-localisation radius was an empirical choice; the bath threshold and basis affected even the sign of the binding energy [1]. A single correlation length does not determine every embedding error.
2. **A classically difficult fragment.** Compare the fragment against suitable CCSD, selected CI and DMRG methods at equal error and total resources. Orbital count by itself is not a hardness certificate.
3. **Controlled assembly error.** EWF has a full-bath limit that recovers the chosen full-system solver [3], while the practical error at finite bath size must be measured. A mathematical analysis of DMET establishes a weak-coupling result [4]; it is not a universal error bound for all embedding methods.

## Known limits

- **Locality does not prove an advantage or a no-go.** Classical local-correlation methods exploit related structure, so their cost must be measured on the same target. EWF's original paper includes a 312-orbital embedded diamond calculation and discusses semi-metallic and correlated examples [3]; the bath size at fixed error varies with the system and observable. No published result here proves that a diverging correlation length forces every embedding fragment past 100 qubits.
- **Full CI was not easy for the demonstrated fragments.** The IBM paper reports 10¹⁸–10²¹ determinants for three 33–45-orbital fragments. It benchmarks SCI and DMRG, with lower DMRG energies, but its SQD implementation used substantial GPU parallelism. This demonstrates neither classical intractability nor an equal-resource speedup [1].
- **Strongly correlated local regions remain candidates.** Multi-metal clusters, P450 and related centres can retain difficult local physics [8]. They also face improving classical DMRG and SCI baselines [6, 7]. Which side wins depends on the particular Hamiltonian, accuracy and hardware budget, not a universal >100-orbital cutoff.
- **Circuit cutting cannot substitute.** Jing, Zhu and Wang prove the sampling overhead of circuit knitting is lower-bounded exponentially by the entanglement cost across the cut [5].

## Verdict

Surviving as a route to a meaningful experiment. The existing protein calculation validates a large hybrid workflow, while leaving advantage and decision value open. The next benchmark should fix a useful observable and accuracy, sweep bath threshold and fragment size, and compare quantum-assisted and optimized classical solvers at the same error including the cost of the full workflow. Correlation length, fragment orbitals and required qubits should be *measured* together; neither a 100-qubit opportunity nor its impossibility follows from the current examples.
