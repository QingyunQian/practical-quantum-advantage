---
type: problem
id: linear-response-spectral-functions
title: Linear response and spectral functions (Green's functions, XAS, ARPES, INS)
title_zh: 线性响应与谱函数（格林函数、XAS、ARPES、INS）
summary: Spectra help interpret correlated materials, but an application-level quantum advantage requires a named impurity and a measured classical bottleneck. A cited cathode XPS study used classical CT-QMC for the DMFT step and a separate multiplet code for the core-level spectrum. A 50–100-system-qubit register count and an illustrative gate multiplication do not establish its quantum cost or industrial value.
summary_zh: 谱学有助于解读关联材料，但量子优势需要具体杂质和可测量的经典瓶颈。所引正极 XPS 研究用经典 CT-QMC 完成 DMFT 步骤，再以独立的多重态程序计算核能级谱。50 到 100 个系统比特的计数和示意性的门数相乘，尚不能确定量子成本或产业价值。
status: seed
last_verified: 2026-09-27
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "CT-HYB has a sign problem on some multi-orbital models, but the cited cathode impurity was solved classically; a matched hard application instance has not been supplied"}
  quantum_easiness: {level: conditional, note: "Green's function from Hamiltonian simulation of the impurity model is polynomial once the impurity ground state is prepared; bath discretisation and sampling set the constant; no end-to-end resource estimate exists"}
  willingness_to_pay: {level: second-hand, note: "spectroscopy users (cathode XAS/XPS, rare-earth magnets, actinide fuels) exist and DMFT is changing interpretations, but no company has written an accuracy target and industry mostly uses DFT+U or multiplet fits"}
resources: {logical_qubits: "50–100 (impurity + bath)", gates: "1e9–1e12 T (illustrative scenario, not a resource estimate)", note: "5-orbital d shell with SOC and 4–8 bath sites per spin-orbital, or 7-orbital f shell with 3–6 bath sites; Trotter time evolution to ~100 fs for 10 meV resolution; Krylov methods may cut this by orders of magnitude"}
related:
  applications: [battery-cathode-spectroscopy, rare-earth-permanent-magnets, nuclear-fuel-actinide-spectra]
  problems: [quench-dynamics, ground-state-energy, excited-states]
  methods: [dmft-impurity-solver, embedding-divide-and-conquer, phase-estimation]
  questions: [dmft-impurity-cost-vs-ctqmc-sign-problem]
references:
  - {arxiv: "1510.03859", title: "Hybrid quantum-classical approach to correlated materials", authors: "B. Bauer, D. Wecker, A. J. Millis, M. B. Hastings, M. Troyer", year: 2016, note: "Phys. Rev. X 6, 031045; proposes the ~100 logical qubit impurity solver"}
  - {arxiv: "2510.02875", title: "Redox chemistry of LiCoO2, LiNiO2, and LiNi1/3Mn1/3Co1/3O2 cathodes: deduced via XPS, DFT+DMFT, and charge transfer multiplet simulations", authors: "Y. Xie, et al., F. M. F. de Groot, H. Zhang", year: 2025}
  - {arxiv: "2206.15093", title: "Ce and Dy substitutions in Nd$_{2}$Fe$_{14}$B: site-specific magnetic anisotropy from first-principles", authors: "J. Boust et al.", year: 2022, note: "Direct magnet alloy study: Nd 4f in Hubbard-I, mixed-valent Ce approximated"}
  - {arxiv: "2008.13295", title: "Fast inversion, preconditioned quantum linear system solvers, and fast evaluation of matrix functions", authors: "Y. Tong, D. An, N. Wiebe, L. Lin", year: 2020, note: "QSVT route to Green's functions"}
  - {arxiv: "2605.22920", title: "Estimating Green's functions with a robust quantum Arnoldi method", authors: "S. Nelson, A. D. Baczewski", year: 2026}
  - {arxiv: "2603.15741", title: "Neural-network quantum embedding solvers for correlated materials", authors: "A. Valenti, I. Park, A. Georges, A. J. Millis, O. Parcollet", year: 2026}
  - {arxiv: "2207.06135", title: "Learning Feynman Diagrams with Tensor Trains", authors: "Y. Núñez Fernández, M. Jeannin, P. T. Dumitrescu, T. Kloss, J. Kaye, O. Parcollet, X. Waintal", year: 2022, note: "tensor cross interpolation; sign-problem-free diagrammatic summation"}
  - {arxiv: "1504.07979", title: "Electronic structure and core-level spectra of light actinide dioxides in the dynamical mean-field theory", authors: "J. Kolorenč, A. B. Shick, A. I. Lichtenstein", year: 2015, note: "finite-bath exact diagonalisation of UO2/NpO2/PuO2, including XPS"}
---

## Best classical

The observables include single-particle and core-level spectra, magnetic response and optical conductivity. Different experiments require different models. In the cited cathode study, DFT+DMFT provided transition-metal configuration probabilities through a classical CT-QMC solver; Quanty then used those probabilities in a separate charge-transfer multiplet model to calculate XPS [2]. The study found that delithiation does not follow a rigid-band picture. It did not report CT-QMC failure or a quantum computation of the core-hole response. For UO₂, NpO₂ and PuO₂, a separate LDA+DMFT study used classical finite-bath Lanczos to reproduce valence and 4f-core XPS features [8]. Its impurity had 14 f and 14 bath spin orbitals. This is a benchmark of classical success on named actinide oxides, not a measured quantum opportunity.

The bottleneck inside some DMFT calculations is the impurity solver. Continuous-time hybridisation-expansion QMC (CT-HYB) can suffer a severe sign problem with off-diagonal hybridisation, spin–orbit coupling and low temperature; severity depends on the model and basis. Candidate hard regimes include multi-orbital d and f shells and low-temperature clusters. The direct Ce-substituted magnet study [3] treated localised Nd 4f states in the Hubbard-I limit and approximated mixed-valent Ce without a dynamical Ce impurity solve. It does not measure a CT-HYB failure on that alloy. Classical alternatives include tensor-train diagram summation [7] and neural-network embedding solvers [6]; their performance must be checked on the same hybridisation function and observable before declaring any industrial instance classically hard.

## Best quantum

Bauer, Wecker, Millis, Hastings and Troyer proposed in 2016 that the impurity problem be handed to a quantum computer of "about one hundred logical qubits", with the lattice self-consistency kept classical [1]. Qubit arithmetic is simple: (orbitals × 2 spins) × (1 + bath sites per spin-orbital). A 5-orbital d shell with 4 bath sites per spin-orbital is 50 qubits, with 8 it is 90; a 7-orbital f shell with 3–6 bath sites is 56–98; a 2×2 cluster with baths is 40–48. These are system-register examples, excluding ancillas. They do not show that the bath discretisation converges in every regime where CT-HYB struggles.

The Green's function itself comes from time evolution with a Hadamard test, from QSVT evaluation of (ω − H)⁻¹ pointwise [4], from Lehmann-representation phase estimation, or from Krylov and Arnoldi constructions; the robust quantum Arnoldi method of Nelson and Baczewski estimates the whole spectral interval at a cost orders of magnitude below pointwise QSVT [5]. Gate counts are the problem. Resolving 10 meV requires evolution to about 100 fs (ħ/10 meV ≈ 66 fs). Taking 10²–10³ Trotter steps, 10⁴–10⁵ non-Clifford gates per step for a 50–100 qubit Kanamori Hamiltonian, and 10³–10⁴ shots gives 10⁹–10¹² T gates; this is an order-of-magnitude estimate assembled from those stated factors, and no end-to-end fault-tolerant resource estimate for a 5-orbital impurity with SOC has been published. Bath counts must be converged for the model and observable; neither real-frequency spectra nor Matsubara self-consistency has a universal small-bath guarantee.

## What survives

Three possible settings are cathode XPS interpretation [2], rare-earth magnet electronic structure [3] and actinide spectra. The first cited cathode calculation succeeded with classical CT-QMC, so it is evidence of relevance, not of a hard impurity instance. The connection from any improved impurity spectrum to a purchase or changed material decision remains undocumented here. Embedding choices such as U and double counting also contribute uncertainty that a more accurate impurity solver alone cannot remove.

## Verdict

Surviving as a computational problem. Some discretised impurity models fit a 50–100-qubit system register, and some classical solvers have a sign problem. The current applications do not yet identify an instance with both a measured classical failure and a documented decision benefit. The quoted T-gate range is an unconstrained sensitivity calculation, not a compiled resource estimate. A matched impurity benchmark with converged bath, output accuracy and full workflow cost would decide whether this candidate progresses.

## Resource-count assumptions

The gate range quoted here is a sensitivity calculation: assume 10²–10³ time steps, 10⁴–10⁵ compiled T gates per step and 10³–10⁴ repetitions of one measured circuit. Multiplying endpoints gives **10⁹–10¹² T gates**. These inputs are not calibrated for a named impurity or a target error. The range excludes state preparation, additional time points and Green's-function components, bath convergence and DMFT iterations, so it is not an end-to-end estimate or a hardware readiness claim. See the [impurity-solver page](../methods/dmft-impurity-solver.html) for the conditions that remain to be checked.
