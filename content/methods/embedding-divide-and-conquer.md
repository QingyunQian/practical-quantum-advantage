---
type: method
id: embedding-divide-and-conquer
title: Embedding and divide-and-conquer (DMET, EWF, bootstrap, projection, QDET)
title_zh: 嵌入与分而治之（DMET、EWF、bootstrap、投影嵌入、QDET）
summary: Cut a large molecule or material into fragments small enough for a ≤100-qubit solver. IBM's 12,635-atom protein–ligand run (May 2026) proves the engineering works, but every fragment was ≤ 47 orbitals at CCSD accuracy and the authors state it does not beat the best classical methods. Fragmentation assumes correlation decays as exp(−r/ξ), the same assumption that makes DLPNO-CCSD(T) work; where ξ diverges, fragments exceed 256 qubits. The only cut-and-still-hard region is a few open-shell d/f centres within a few Å, where GPU-DMRG already reaches CAS(89,102).
summary_zh: 把大分子或材料切成不超过 100 比特求解器能处理的碎片。IBM 2026 年 5 月 12,635 原子的蛋白-配体计算证明工程上可行，但所有碎片不超过 47 个轨道、精度为 CCSD 级，作者明说没有超过最好的经典方法。碎片化假设关联按 exp(−r/ξ) 衰减，而这正是 DLPNO-CCSD(T) 有效的前提；ξ 发散的掺杂 Mott 材料碎片超过 256 比特。既能切又切完仍难的区域只剩几埃内的多个开壳 d/f 中心，而 GPU-DMRG 已经做到 CAS(89,102)。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "fragments demonstrated so far (≤ 47 orbitals) are FCI/SHCI/DMRG-solvable; the hard fragments (multi-centre Fe–S, P450 (63e,58o), Fe5S12 CAS(89,102)) are exactly where GPU-DMRG now competes"}
  quantum_easiness: {level: heuristic, note: "DMET has a first-order accuracy proof only in the weak-coupling limit; EWF/bootstrap/projection convergence is numerical; circuit cutting overhead is exponential in cut entanglement"}
  willingness_to_pay: {level: second-hand, note: "Cleveland Clinic, RIKEN and IBM co-authored the protein–ligand study but no accuracy target beyond CCSD is stated; catalyst/enzyme buyers inherit from the applications"}
resources: {logical_qubits: "≤ 94 per fragment (47 spatial orbitals) in the largest demonstration; ≥ 256 for 8×8 Hubbard clusters plus bath", gates: "not applicable (fragment solver sets the cost)", note: "12,635-atom run: 21,006 circuits, > 239 hours on two Heron r2 processors, 1.3e9 samples, post-processed on Fugaku and Miyabi-G"}
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

The largest demonstration is IBM/RIKEN/Cleveland Clinic's May 2026 run on T4 lysozyme (11,608 atoms) and a trypsin complex (12,635 atoms): EWF fragments of at most 47 spatial orbitals (94 qubits), solved by SQD across 21,006 circuits on two Heron r2 processors over more than 239 hours, with 1.3 × 10⁹ samples post-processed on Fugaku and Miyabi-G [1]. The fragment energies were reported at CCSD accuracy, and the paper states that the workflow does not yet outperform the best classical approaches. The earlier Trp-cage study (303 atoms, ≤ 66 qubits, STO-3G) gave a folding energy of 55.4 kcal/mol against 52.1 for DLPNO-CCSD [2].

## Preconditions

1. **Correlation locality.** The one-body density matrix must decay as exp(−r/ξ) with ξ of a few Å, so that a 7–10 Å bath captures the fragment's environment. Every scheme above relies on it.
2. **A fragment that is hard after cutting.** The high-level solver only matters if the fragment-plus-bath problem is beyond FCI/SHCI/DMRG at the required accuracy.
3. **Controlled assembly error.** DMET's only proof is exactness in the non-interacting limit and first-order accuracy at weak coupling [4]; self-consistency can fail to converge, and density convergence does not imply energy convergence. EWF and bootstrap show numerical exponential convergence without a bound.

## Known limits

- **Precondition 1 is the classical method's precondition too.** Local correlation methods (DLPNO-CCSD(T)) recover about 99.9% of the correlation energy on thousand-atom proteins by the same locality. In gapped systems the fragments are small but the classical answer already exists; in metals, critical points and doped Mott insulators ξ diverges, and the fragment must exceed the correlation length. For 2D Hubbard stripe-versus-pairing physics this means clusters of at least 8 × 8 sites plus bath, i.e. ≥ 256 qubits, outside the "≤ 100 qubits" regime that motivates embedding.
- **The demonstrated fragments are not hard.** 33–47 orbitals is comfortably within SHCI, DMRG and often FCI. The 12,635-atom result demonstrates systems integration, not a physical gain from the quantum solver; the SQD step is a determinant-selection heuristic that the linked page shows is matched by classical selection.
- **The one region that is cut-and-still-hard is contested.** Multiple open-shell d/f centres within a few Å (FeMoco with ~35 open-shell electrons, P450 CAS(63e,58o) [8], Fe₅S₁₂ at CAS(89,102)) stay multireference after cutting. But GPU-DMRG already benchmarks Fe₅S₁₂H₄⁵⁻ at CAS(89,102) and Legeza et al. argue any advantage claim must be measured against it [6]; the FeMoco model was solved to ±0.31 kcal/mol classically in 2026 [7]. Critics place the quantum threshold at single fragments of > 100–200 orbitals.
- **Circuit cutting cannot substitute.** Jing, Zhu and Wang prove the sampling overhead of circuit knitting is lower-bounded exponentially by the entanglement cost across the cut [5].

## Verdict

Surviving, narrowly. Embedding is necessary infrastructure for any quantum chemistry workflow on real systems, but as of September 2026 no embedding-plus-quantum-solver result beats the best classical method on the same active space. The surviving case is (i) local, strongly correlated multi-metal clusters or defects with 50–120 fragment orbitals, where DMRG/SHCI are still in the race; (ii) long-range correlated materials are not reachable with ≤ 100 qubits. What would change the verdict: a > 100-orbital fragment energy or spin-state ordering, verified against DMRG/SHCI extrapolation, that the classical methods cannot converge, rather than a larger atom count.
