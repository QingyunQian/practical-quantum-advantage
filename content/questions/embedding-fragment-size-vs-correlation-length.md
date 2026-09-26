---
type: question
id: embedding-fragment-size-vs-correlation-length
title: At what correlation length does the embedding fragment exceed 100 qubits?
title_zh: 关联长度到多大时，嵌入碎片会超过 100 比特？
summary: Embedding methods (DMET, EWF, bootstrap embedding, circuit cutting) split a large system into fragments a 100-qubit solver could handle, but they rely on a short correlation length, and short correlation length is also what makes DLPNO-CCSD(T) and local DMRG work. Nobody has measured, on doped 2D Hubbard and on a metallic system, the fragment size (with bath) needed for a fixed energy error as a function of the correlation length, and hence where the fragment crosses 100 qubits.
summary_zh: 嵌入方法（DMET、EWF、bootstrap 嵌入、电路切割）把大体系拆成 100 比特求解器能处理的碎片，但它们依赖短关联长度，而短关联长度同样是 DLPNO-CCSD(T) 和局域 DMRG 奏效的前提。还没有人在掺杂二维 Hubbard 模型和金属体系上测量：固定能量误差下所需碎片（含 bath）随关联长度如何增长，从而碎片在何处超过 100 比特。
status: seed
last_verified: 2026-09-26
question:
  what_would_settle_it: "Two scans. (1) Doped 2D Hubbard at U/t = 8, doping 1/8 to 1/16, t'/t in {0, −0.2}: DMET or EWF energy error per site versus fragment size (2×2 up to 8×8 plus bath) against DMRG reference on width-6 to width-8 cylinders, with the spin/charge correlation length extracted from the same reference. (2) A simple metal or a metallic slab (e.g. Cu(111) or Na) with EWF: fragment plus bath orbitals needed for 1 kcal/mol convergence of an adsorption energy, versus a DLPNO-CCSD(T) reference. Report qubits = 2 × (fragment + bath) orbitals at each point. The answer is the correlation length at which that number crosses 100; if it crosses only where DLPNO or DMRG already converge, embedding gives a 100-qubit solver no territory."
  difficulty: phd
  resolved: false
related:
  applications: [protein-ligand-binding, homogeneous-catalysis, battery-cathode-spectroscopy]
  problems: [ground-state-energy]
  methods: [embedding-divide-and-conquer, sqd]
  claims: [ibm-sqd-2024]
references:
  - {arxiv: "2107.04916", title: "Systematic improvability in quantum embedding for real materials", authors: "M. Nusspickel, G. H. Booth", year: 2022, note: "PRX 12, 011046 (2022); the EWF scheme"}
  - {arxiv: "2605.01138", title: "Crossing the 12,000-atom barrier with heterogeneous quantum-classical supercomputing: quantum chemistry of protein-ligand complexes", authors: "L. Merz, B. Shajan, D. Kaliakin et al.", year: 2026, note: "fragments ≤ 47 orbitals (≤ 94 qubits), 21,006 circuits, > 239 hours on two Heron r2"}
  - {arxiv: "2305.16472", title: "Some mathematical insights on Density Matrix Embedding Theory", authors: "E. Cancès et al.", year: 2023}
  - {arxiv: "2404.03619", title: "Circuit Knitting Faces Exponential Sampling Overhead Scaling Bounded by Entanglement Cost", authors: "M. Jing, C. Zhu, X. Wang", year: 2024}
  - {arxiv: "1701.00054", title: "Stripe order in the underdoped region of the two-dimensional Hubbard model", authors: "B.-X. Zheng, C.-M. Chung, P. Corboz et al.", year: 2017, note: "Science 358, 1155 (2017)"}
  - {arxiv: "2303.08376", title: "Coexistence of superconductivity with partially filled stripes in the Hubbard model", authors: "H. Xu, C.-M. Chung, M. Qin, U. Schollwöck, S. R. White, S. Zhang", year: 2024, note: "Science 384, adh7691 (2024)"}
---

## Why it matters

The case for a 100-qubit solver having anything to do rests on divide and conquer: cut the protein, the catalyst or the crystal into fragments, solve each on the quantum computer, stitch. IBM's 12,000-atom protein–ligand demonstration did exactly this with EWF, one cluster per atom, fragments of at most 47 spatial orbitals (94 qubits), and reached CCSD-level fragment energies after 21,006 circuits and more than 239 hours on two Heron r2 processors [2]. IBM's own blog says the result does not yet outperform the best classical approaches; DLPNO-CCSD(T) handles thousand-atom proteins on a single node in days.

The reason is a theorem-shaped fact. Density matrices of gapped systems decay as exp(−r/ξ); every embedding scheme (DMET, EWF [1], bootstrap embedding, projection embedding) works because ξ is small, and so does every local classical method. The only mathematical analysis of DMET proves first-order accuracy in the weak-coupling limit [3]; circuit cutting and entanglement forging carry a sampling overhead exponential in the entanglement across the cut [4]. When ξ is large, as in doped Mott insulators where stripe and pairing orders compete on scales of 4 to 8 lattice spacings [5, 6], the fragment must be at least ξ wide, and an 8×8 Hubbard fragment with bath is already 256 or more qubits. When ξ is small, the fragment is classically solvable. The question is whether there is any window between the two, and the answer is a number: the ξ at which the fragment crosses 100 qubits, compared with the ξ at which DLPNO or DMRG stop converging.

## What is known

- The one plausible exception is short correlation length with high local entanglement: several open-shell d or f centres within a few ångström (FeMoco, P450, [4Fe-4S], Fe5S12 with CAS(89,102)) and semiconductor spin defects. These fragments are 50 to 120 orbitals, which is precisely the range where GPU-DMRG and SHCI are still competitive, so even the exception is a race, not a gap.
- On 2D Hubbard, DMRG on width-6 to width-8 cylinders with bond dimensions in the tens of thousands is the reference [5, 6]; there is no published DMET or EWF fragment-size scan against it at 1/8 doping that reports the bath size needed for a fixed energy error.
- On metals, EWF with MP2 baths [1] converges systematically for insulators; metallic convergence with fragment size is reported qualitatively but not as a qubit count.

## What would settle it

See the front matter. The Hubbard scan can be done with existing DMET/EWF codes (Vayesta, QCMaquis interfaces) against block2 DMRG references; the metal scan needs a periodic EWF implementation and a DLPNO reference, which is the harder half. Deliverable: two plots of qubits-needed versus correlation length with the 100-qubit line and the classical-convergence boundary on the same axes. A PhD-length project if both scans are done carefully; the Hubbard half alone is a few months.

## Who could take it

An embedding group (Booth, Chan, Scuseria, Reiher lineages) with access to DMRG references. The result changes the verdict of `embedding-divide-and-conquer` from `surviving` to either `promising` (a window exists) or `no-go` for the 100-qubit setting.
