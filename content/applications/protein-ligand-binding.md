---
type: application
id: protein-ligand-binding
title: Protein–ligand binding energies
title_zh: 蛋白质与配体结合能
summary: The showcase for "quantum-centric supercomputing". IBM, Cleveland Clinic and RIKEN ran wavefunction embedding on an 11,608-atom T4 lysozyme and a 12,635-atom trypsin complex, with fragments of at most 47 spatial orbitals (94 qubits) solved by sample-based diagonalisation to CCSD accuracy. It is an engineering milestone rather than an advantage, because every fragment is within reach of classical CCSD, and the authors state it does not yet outperform the best classical methods.
summary_zh: 这是“量子中心超算”的展示案例：IBM、克利夫兰诊所和 RIKEN 对 11,608 原子的 T4 溶菌酶和 12,635 原子的胰蛋白酶复合物做了波函数嵌入，碎片最多 47 个空间轨道（94 个比特），用采样对角化算到 CCSD 精度。这是工程里程碑，不是优势：每个碎片都在经典 CCSD 能力范围内，作者自己也说尚未超过最好的经典方法。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "none for the demonstrated systems: fragments of 6–47 orbitals are solvable by CCSD, SHCI or FCI, and DLPNO-CCSD(T) handles thousand-atom proteins routinely; a residual hard case exists only for metal-containing active sites, where the local fragment is strongly correlated"}
  quantum_easiness: {level: heuristic, note: "sample-based diagonalisation on each fragment has no convergence guarantee; the embedding itself (EWF, non-self-consistent) is numerically but not provably improvable; if fragments must exceed 100 orbitals to retain hardness, the qubit budget exceeds 200"}
  willingness_to_pay: {level: second-hand, note: "pharma pays for binding free energies (FEP is standard practice), but the accuracy limit there (about 1 kcal/mol MUE) is set by force fields and sampling; Cleveland Clinic co-authored the demonstration without stating an accuracy target"}
resources: {logical_qubits: "≤94 per fragment (demonstrated on noisy hardware)", gates: "21,006 circuits, 1.3e9 shots, >239 h on two Heron r2 processors", note: "EWF-TrimSQD on trypsin–ligand (12,635 atoms) with Fugaku and Miyabi-G for the classical part; fragments ≤47 spatial orbitals"}
related:
  applications: [p450-drug-metabolism, homogeneous-catalysis]
  problems: [ground-state-energy]
  methods: [embedding-divide-and-conquer, sqd]
  claims: [ibm-sqd-2024]
  questions: [embedding-fragment-size-vs-correlation-length, ideal-sqd-vs-classical-selection]
references:
  - {arxiv: "2605.01138", title: "Crossing the 12,000-atom barrier with heterogeneous quantum-classical supercomputing: quantum chemistry of protein-ligand complexes", authors: "K. M. Merz Jr., A. Shajan, D. Kaliakin, et al., S. Yunoki, M. Motta (Cleveland Clinic, RIKEN, IBM)", year: 2026, note: "11,608 and 12,635 atoms; fragments ≤94 qubits; 21,006 circuits; >239 h"}
  - {arxiv: "2512.17130", title: "Molecular Quantum Computations on a Protein", authors: "A. Shajan et al., K. M. Merz", year: 2025, note: "Trp-cage, 303 atoms, ≤66 qubits; folding energy 55.4 vs DLPNO-CCSD 52.1 kcal/mol in STO-3G"}
  - {arxiv: "2107.04916", title: "Systematic improvability in quantum embedding for real materials", authors: "M. Nusspickel, G. H. Booth", year: 2021, note: "the EWF embedding used in the IBM runs"}
  - {arxiv: "2305.16472", title: "Some mathematical insights on Density Matrix Embedding Theory", authors: "E. Cancès, F. Faulstich, A. Kirsch, E. Letournel, A. Levitt", year: 2023, note: "only mathematical analysis of DMET-type embedding: first-order exact in the weak-coupling limit"}
  - {arxiv: "2301.04114", title: "Drug design on quantum computers", authors: "R. Santagati et al.", year: 2023, note: "pharma perspective: binding-affinity bottleneck is sampling and force fields"}
  - {arxiv: "2603.28648", title: "Hunting for quantum advantage in electronic structure calculations is a highly non-trivial task", authors: "Ö. Legeza et al.", year: 2026}
---

## Who needs it

Every pharmaceutical discovery programme. Relative binding free energies between ligand analogues decide which compounds are synthesised, and free-energy perturbation (FEP) with classical force fields is used to compare related ligands; its accuracy depends on the target and chemical series. Quantum-chemical binding energies are used as a check on the force field and for cases with metal centres, covalent inhibitors or unusual electronics. Cleveland Clinic co-authored the IBM demonstrations as a prospective user.

## Bottleneck

For most protein–ligand systems, the electronic-structure part is not the bottleneck. DLPNO-CCSD(T) on thousand-atom systems is routine on a single node in days, and the residual error in a binding free energy comes from conformational sampling, solvation and protonation states, and force-field transferability, as the pharma-authored perspective states [5]. The exception is a ligand bound at a metal site, where the local fragment is multiconfigurational.

The IBM, Cleveland Clinic and RIKEN work is the largest quantum-involved chemistry calculation to date [1]. They used the EWF embedding of Nusspickel and Booth [3]: one cluster per atom, IAO fragments with an MP2 bath localised to 7–10 Å, a single accuracy parameter η, non-self-consistent. On T4 lysozyme (11,608 atoms) and a trypsin–ligand complex (12,635 atoms, with explicit water) the fragments have at most 47 spatial orbitals (94 qubits); the quantum part was 21,006 circuits, 1.3×10^9 shots and more than 239 hours on two Heron r2 processors, with Fugaku and Miyabi-G doing the classical work. Fragment energies reached CCSD accuracy. The earlier Trp-cage run (303 atoms, up to 66 qubits) gave a folding energy of 55.4 kcal/mol against 52.1 for DLPNO-CCSD in the STO-3G basis [2].

Two facts follow. First, every fragment is in the range where CCSD, SHCI or FCI is easy; the quantum solver (sample-based diagonalisation) is a determinant-selection heuristic whose classical post-processing does the work (see the [SQD](../methods/sqd.html) page). Second, the embedding works precisely because correlation is local: the density matrix of a gapped system decays as exp(−r/ξ), which is the same assumption that makes DLPNO-CCSD(T) work. Fragmentation therefore removes the hardness it was meant to isolate. The only mathematical analysis of DMET-type embedding proves first-order exactness in the weak-coupling limit and nothing beyond [4]. The authors themselves state that the approach does not yet outperform the best classical methods.

## Computational problems

- [Ground-state energy](../problems/ground-state-energy.html) of each embedded fragment, and the assembled interaction energy.
- Free-energy sampling of the complex, which is where the practical error lives and which no quantum algorithm addresses.

## Best classical today

FEP with modern force fields for the decision; DLPNO-CCSD(T) or local MP2 with counterpoise corrections for benchmark interaction energies on thousands of atoms; DMRG or SHCI for metal-site fragments up to about 100 orbitals, with Legeza et al. setting the benchmark expectation for any advantage claim [6].

## Verdict

Surviving in a narrow sense; the demonstrated route offers no advantage. The 12,635-atom run shows that a QPU–HPC loop and a linear-scaling bath work at scale, which is useful infrastructure. It does not show a quantum gain, because the fragments are classically easy and the embedding assumption is the classical assumption. The residual window is a ligand at a strongly correlated metal site where the fragment must exceed about 100 orbitals to keep the multireference physics, at which point the qubit budget is beyond 200 and DMRG is the competitor. Evidence that would move the verdict: a metalloprotein–ligand interaction energy where the quantum-solved fragment is above 100 orbitals, the result is validated against DMRG or SHCI extrapolation, the total error is below 1 kcal/mol, and the error is shown to come from the metal fragment rather than from sampling. Larger atom counts do not count.
