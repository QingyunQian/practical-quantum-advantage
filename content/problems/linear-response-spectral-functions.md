---
type: problem
id: linear-response-spectral-functions
title: Linear response and spectral functions (Green's functions, XAS, ARPES, INS)
title_zh: 线性响应与谱函数（格林函数、XAS、ARPES、INS）
summary: Spectral functions are what industry actually measures and decides on, and the correlated cases (3d oxide core-level spectra, 4f and 5f shells) are exactly where CT-QMC impurity solvers hit the sign problem. Dynamical mean-field theory turns this into a 50–100 qubit impurity problem, at an estimated 1e9–1e12 T gates for 10 meV resolution; industry today uses DFT+U and multiplet codes, not DMFT.
summary_zh: 谱函数是工业界真正测量并据以决策的量，而关联强的情形（3d 氧化物核能级谱、4f 与 5f 壳层）正是 CT-QMC 杂质求解器遇到符号问题的地方。动力学平均场把它变成 50 到 100 比特的杂质问题，10 meV 分辨率估计需要 1e9 到 1e12 个 T 门；工业界目前用的是 DFT+U 和多重态程序，而不是 DMFT。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "CT-HYB sign problem grows exponentially with spin-orbit coupling, off-diagonal hybridisation and low temperature; tensor-train QMC and neural-network solvers are eroding the region"}
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
  - {arxiv: "1705.08027", title: "Crystal-field splittings in rare-earth-based hard magnets: an ab initio approach", authors: "P. Delange, S. Biermann, T. Miyake, L. Pourovskii", year: 2017, note: "Phys. Rev. B 96, 155132; Hubbard-I treatment of the 4f shell"}
  - {arxiv: "2008.13295", title: "Fast inversion, preconditioned quantum linear system solvers, and fast evaluation of matrix functions", authors: "Y. Tong, D. An, N. Wiebe, L. Lin", year: 2020, note: "QSVT route to Green's functions"}
  - {arxiv: "2605.22920", title: "Estimating Green's functions with a robust quantum Arnoldi method", authors: "S. Nelson, A. D. Baczewski", year: 2026}
  - {arxiv: "2603.15741", title: "Neural-network quantum embedding solvers for correlated materials", authors: "A. Valenti, I. Park, A. Georges, A. J. Millis, O. Parcollet", year: 2026}
  - {arxiv: "2207.06135", title: "Learning Feynman Diagrams with Tensor Trains", authors: "Y. Núñez Fernández, M. Jeannin, P. T. Dumitrescu, T. Kloss, J. Kaye, O. Parcollet, X. Waintal", year: 2022, note: "tensor cross interpolation; sign-problem-free diagrammatic summation"}
---

## Best classical

The quantities are retarded Green's functions and susceptibilities: single-particle spectral functions (ARPES, XPS), core-level absorption (XAS, RIXS), magnetic response (INS), optical conductivity. Industrial practice is DFT-based almost everywhere: DFT+U projected density of states and charge-transfer multiplet fits for cathode L-edges, DFPT for phonons, GW-BSE for optics, spin-wave models for neutron scattering. DMFT is used where DFT+U fails qualitatively; Xie, de Groot, Zhang and co-workers needed DFT+DMFT plus multiplet simulations to show that delithiation of LiNiO₂ and NMC is not rigid-band, and that the paramagnetic insulating state of LiNiO₂ appears only in DMFT [2].

The bottleneck inside DMFT is the impurity solver. Continuous-time hybridisation-expansion QMC (CT-HYB) is the workhorse but its sign problem grows exponentially with spin-orbit coupling, off-diagonal hybridisation, cluster size and inverse temperature; the regimes that remain out of reach are a 5-orbital d shell with full SOC below about 100 K, dynamical (non-atomic-limit) treatment of 7-orbital f shells, and 2×2 or larger clusters at low temperature. Rare-earth magnet work sidesteps the f-shell solver entirely with the Hubbard-I atomic limit [3]. Exact diagonalisation and NRG are limited to a few orbitals by bath count; MPS solvers reach three orbitals with about 100 bath sites. Two classical developments are eroding the hard region: tensor-train (tensor cross interpolation) summation of diagrammatic expansions, which has no sign problem [7], and neural-network impurity solvers trained to QMC accuracy at orders-of-magnitude lower cost [6].

## Best quantum

Bauer, Wecker, Millis, Hastings and Troyer proposed in 2016 that the impurity problem be handed to a quantum computer of "about one hundred logical qubits", with the lattice self-consistency kept classical [1]. Qubit arithmetic is simple: (orbitals × 2 spins) × (1 + bath sites per spin-orbital). A 5-orbital d shell with 4 bath sites per spin-orbital is 50 qubits, with 8 it is 90; a 7-orbital f shell with 3–6 bath sites is 56–98; a 2×2 cluster with baths is 40–48. These are system-register examples, excluding ancillas. They do not show that the bath discretisation converges in every regime where CT-HYB struggles.

The Green's function itself comes from time evolution with a Hadamard test, from QSVT evaluation of (ω − H)⁻¹ pointwise [4], from Lehmann-representation phase estimation, or from Krylov and Arnoldi constructions; the robust quantum Arnoldi method of Nelson and Baczewski estimates the whole spectral interval at a cost orders of magnitude below pointwise QSVT [5]. Gate counts are the problem. Resolving 10 meV requires evolution to about 100 fs (ħ/10 meV ≈ 66 fs). Taking 10²–10³ Trotter steps, 10⁴–10⁵ non-Clifford gates per step for a 50–100 qubit Kanamori Hamiltonian, and 10³–10⁴ shots gives 10⁹–10¹² T gates; this is an order-of-magnitude estimate assembled from those stated factors, and no end-to-end fault-tolerant resource estimate for a 5-orbital impurity with SOC has been published. Bath counts must be converged for the model and observable; neither real-frequency spectra nor Matsubara self-consistency has a universal small-bath guarantee.

## What survives

Three scenarios have identifiable decision-makers: cathode operando XAS/XPS/RIXS interpretation (is capacity fade Ni oxidation or O 2p oxidation) [2]; whether cheap Ce can replace Nd in Nd–Fe–B magnets, a 4f Kondo-screening question that current workflows avoid with Hubbard-I [3]; and UO₂/PuO₂ 5f spectra at national laboratories that already run DMFT. All are "explain the spectrum" rather than "design the material", and in each the embedding error (choice of U, double counting, single-site approximation) is typically larger than the solver error that a quantum solver would remove.

## Verdict

Surviving. The problem has a natural divide-and-conquer that fits 50–100 qubits, a classical hard region defined by a sign problem rather than folklore, and real spectroscopy users, but willingness to pay is second-hand and the gate count sits at 10⁹–10¹² T. What would settle it: an end-to-end resource estimate for a 5-orbital impurity Green's function with SOC, and a head-to-head against tensor-train QMC and neural-network solvers on the same Sr₂RuO₄ or Ce-4f instance below 100 K.

## Resource-count assumptions

The gate range quoted here is a sensitivity calculation: assume 10²–10³ time steps, 10⁴–10⁵ compiled T gates per step and 10³–10⁴ repetitions of one measured circuit. Multiplying endpoints gives **10⁹–10¹² T gates**. These inputs are not calibrated for a named impurity or a target error. The range excludes state preparation, additional time points and Green's-function components, bath convergence and DMFT iterations, so it is not an end-to-end estimate or a hardware readiness claim. See the [impurity-solver page](../methods/dmft-impurity-solver.html) for the conditions that remain to be checked.
