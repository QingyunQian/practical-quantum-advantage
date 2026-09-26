---
type: question
id: embedding-fragment-size-vs-correlation-length
title: Which embedding problems fit within 100 logical qubits at useful accuracy?
title_zh: 哪些嵌入问题能在 100 个逻辑比特内达到有用精度？
summary: Map the fragment-plus-bath orbitals needed for a fixed observable error against measured correlation diagnostics and the cost of classical fragment solvers. EWF, DMET and related methods have different baths; circuit cutting is a separate technique. Existing protein calculations show 94 physical qubits at CCSD-like fragment accuracy, but do not establish a 100-logical-qubit advantage or a universal correlation-length cutoff.
summary_zh: 固定目标物理量与误差，测量所需的碎片加环境轨道数、关联特征和经典碎片求解成本。EWF、DMET 等方法构造环境的方式不同，电路切割也不是嵌入方法。现有蛋白质计算最多用了 94 个物理比特，碎片精度接近 CCSD，但没有建立 100 个逻辑比特上的优势，更没有通用的关联长度阈值。
status: seed
last_verified: 2026-09-26
question:
  what_would_settle_it: "Choose one industrially motivated observable, such as a metal-site ligand interaction energy, with a buyer-relevant error tolerance, and one correlated model as a stress test. For each, sweep fragment and bath sizes, basis and solver accuracy; report physical error against a converged reference, orbital count, qubit mapping, and classical CCSD/SCI/DMRG time and memory. Extract relevant correlation diagnostics on the same instances rather than assuming one universal length. Identify any point below 100 logical qubits where the complete quantum workflow has a credible scaling or complexity case over an optimized classical workflow."
  difficulty: phd
  resolved: false
related:
  applications: [protein-ligand-binding, homogeneous-catalysis, battery-cathode-spectroscopy]
  problems: [ground-state-energy]
  methods: [embedding-divide-and-conquer, sqd]
  claims: [ibm-sqd-2024]
references:
  - {arxiv: "2107.04916", title: "Systematic improvability in quantum embedding for real materials", authors: "M. Nusspickel, G. H. Booth", year: 2022, note: "PRX 12, 011046 (2022); the EWF scheme"}
  - {arxiv: "2605.01138", title: "Crossing the 12,000-atom barrier with heterogeneous quantum-classical supercomputing: quantum chemistry of protein-ligand complexes", authors: "K. M. Merz Jr., A. Shajan, D. Kaliakin et al.", year: 2026, note: "largest circuit 94 physical qubits; 21,006 circuits and >239 cumulative QPU hours across reported runs"}
  - {arxiv: "2305.16472", title: "Some mathematical insights on Density Matrix Embedding Theory", authors: "E. Cancès et al.", year: 2023}
  - {arxiv: "2404.03619", title: "Circuit Knitting Faces Exponential Sampling Overhead Scaling Bounded by Entanglement Cost", authors: "M. Jing, C. Zhu, X. Wang", year: 2024}
  - {arxiv: "1701.00054", title: "Stripe order in the underdoped region of the two-dimensional Hubbard model", authors: "B.-X. Zheng, C.-M. Chung, P. Corboz et al.", year: 2017, note: "Science 358, 1155 (2017)"}
  - {arxiv: "2303.08376", title: "Coexistence of superconductivity with partially filled stripes in the Hubbard model", authors: "H. Xu, C.-M. Chung, M. Qin, U. Schollwöck, S. R. White, S. Zhang", year: 2024, note: "Science 384, adh7691 (2024)"}
---

## Why it matters

Embedding offers a way to solve a large system through smaller, environmentally coupled problems. IBM's 12,000-atom protein–ligand study used EWF, circuits of up to 94 noisy *physical* qubits and classical subspace diagonalization [2]. Its quantum-assisted energies had classical EWF-CCSD counterparts; its authors explicitly make no quantum-advantage claim. The study did not demonstrate a 100-*logical*-qubit computation or a binding-free-energy prediction.

Locality helps both quantum embedding and classical local-correlation methods, but does not make their accuracy or relative cost identical. EWF has a full-bath limit and published convergence studies that include semi-metallic and correlated materials [1]. DMET has a weak-coupling mathematical result [3]. Neither gives a universal relation between a measured correlation length and the number of qubits needed for a chosen energy difference. Circuit cutting has a different sampling-overhead problem [4] and should be analysed separately. This question asks for an empirical and, where possible, theoretical *map* of accuracy, fragment size and competing solver cost.

## What is known

- Local multireference centres are plausible stress tests, but their size and classical cost depend on the chosen Hamiltonian, orbital basis and accuracy. An orbital-count threshold alone does not establish quantum advantage.
- Doped 2D Hubbard is a useful comparison problem for embedding and DMRG [5, 6], provided the same observable, geometry and error tolerance are used. Its behaviour should not be presented as a universal theorem about proteins or catalysts.
- The original EWF paper demonstrates bath convergence on diamond and discusses graphene and SrTiO₃ [1]. That is evidence of systematic improvability toward the selected full-system solver, while the qubit budget for a specific application remains to be measured.

## What would settle it

See the front matter. The deliverable is an instance-level table and plot of target error versus fragment-plus-bath orbitals, required qubits, and classical solver cost. Mark the 100-logical-qubit boundary and identify which assumptions control extrapolation. Report electronic interaction energies separately from experimental binding free energies.

## Who could take it

An embedding group with access to matched classical solvers and a domain collaborator who can define the application error target. A measured window would strengthen the embedding case; failure on one model would narrow that case without ruling out all embedding problems.
