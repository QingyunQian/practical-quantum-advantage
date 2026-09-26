---
type: question
id: dmft-impurity-cost-vs-ctqmc-sign-problem
title: Where does the CT-QMC sign problem bite for f-shell impurities, and does a 50–100 qubit solver beat it?
title_zh: CT-QMC 符号问题在 f 壳杂质上从哪里开始失效，50 到 100 比特的求解器能否胜过它？
summary: DMFT is the one dynamics workflow whose kernel, an Anderson impurity with a handful of bath orbitals, fits in 50 to 100 qubits, and CT-HYB has a documented failure region (spin–orbit coupling, off-diagonal hybridisation, seven-orbital f shells, low temperature). Nobody has mapped that region quantitatively, as average sign versus orbital count, SOC strength and temperature, next to the T-gate count (10^9 to 10^12 by rough estimate) a quantum Green's-function solver would need on the same impurity.
summary_zh: DMFT 是唯一内核（带少量 bath 轨道的 Anderson 杂质）能装进 50 到 100 比特的动力学工作流，而 CT-HYB 有明确记载的失效区（自旋轨道耦合、非对角杂化、七轨道 f 壳、低温）。还没有人定量地画出这个区域（平均符号随轨道数、SOC 强度和温度的变化），并把它与量子格林函数求解器在同一杂质上所需的 T 门数（粗估 10^9 到 10^12）并列比较。
status: seed
last_verified: 2026-09-26
question:
  what_would_settle_it: "A phase map for a single-site Anderson impurity with (a) 5 d orbitals plus SOC λ in {0, 0.1, 0.3} eV and (b) 7 f orbitals with Kanamori/Slater interactions, 3 to 8 bath orbitals per spin-orbital, at T in {300, 100, 30} K: the CT-HYB average sign and the CPU-hours to reach 1% accuracy in the Matsubara self-energy, next to the tensor-train (TCI) and MPS solver bond dimensions, next to the number of Trotter steps × samples × non-Clifford gates for a quantum Krylov or robust Arnoldi Green's-function solver at the same accuracy. The question is settled positively if there is a contiguous region (f shell with SOC below 100 K is the candidate) where the sign is below 0.01, TCI/MPS do not converge, and the quantum T count is below 10^9; negatively if TCI or NN solvers cover the whole map."
  difficulty: phd
  resolved: false
related:
  applications: [rare-earth-permanent-magnets, battery-cathode-spectroscopy, nuclear-fuel-actinide-spectra]
  problems: [linear-response-spectral-functions]
  methods: [dmft-impurity-solver, phase-estimation]
references:
  - {arxiv: "1510.03859", title: "Hybrid quantum-classical approach to correlated materials", authors: "B. Bauer, D. Wecker, A. J. Millis, M. B. Hastings, M. Troyer", year: 2016, note: "PRX 6, 031045 (2016); the 'about a hundred logical qubits' proposal"}
  - {arxiv: "2605.22920", title: "Estimating Green's functions with a robust quantum Arnoldi method", authors: "T. Nelson, A. D. Baczewski", year: 2026}
  - {arxiv: "2603.15741", title: "Neural-Network Quantum Embedding Solvers for Correlated Materials", authors: "A. Valenti, J. Park, A. Georges, A. J. Millis, O. Parcollet", year: 2026}
  - {arxiv: "2207.06135", title: "Learning Feynman Diagrams with Tensor Trains", authors: "Y. Núñez Fernández et al.", year: 2022, note: "PRX 12, 041018 (2022); tensor cross interpolation for diagrammatic sums"}
  - {arxiv: "1705.08027", title: "Crystal field splittings in rare earth-based hard magnets: an ab initio approach", authors: "P. Delange, S. Biermann, T. Miyake, L. Pourovskii", year: 2017, note: "PRB 96, 155132 (2017); Hubbard-I used to avoid a dynamical 4f solver"}
  - {arxiv: "2510.02875", title: "Redox Chemistry of LiCoO$_2$, LiNiO$_2$, and LiNi$_{1/3}$Mn$_{1/3}$Co$_{1/3}$O$_2$ Cathodes: Deduced via XPS, DFT+DMFT, and Charge Transfer Multiplet Simulations", authors: "Y. Xie, F. Mellin, W. Jaegermann, S. Hofmann, F. M. F. de Groot, H. Zhang", year: 2025}
  - {arxiv: "2404.09527", title: "Dynamical Mean Field Theory for Real Materials on a Quantum Computer", authors: "J. Selisko, M. Amsler, C. Wrigley et al.", year: 2024, note: "Ca2CuO2Cl2 on 14 IBM qubits"}
---

## Why it matters

Quench dynamics on clean 2D lattices motivates quantum simulation, but a difficult classical benchmark does not by itself establish industrial value. DMFT is the dynamics workflow that does have users: rare-earth magnet groups deciding whether Ce can replace Nd (they currently use Hubbard-I precisely to avoid a dynamical 4f solver [5]); battery groups reading operando XAS/XPS of NMC and LiNiO2 cathodes through DFT+DMFT multiplet simulations [6]; actinide-fuel groups at LANL and LLNL assigning UO2/PuO2 5f spectra. Its kernel is an impurity of (orbitals × spins) × (1 + baths) qubits: 5 d orbitals with SOC and 4 baths per spin-orbital is 50 qubits, 8 baths is 90; a 7-orbital f shell with 3 to 6 baths is 56 to 98 [1]. These system-register counts make selected discretised impurities candidates for a small quantum processor; coverage of the full classically difficult region remains unproved.

The difficulty region is real but undocumented as numbers. CT-HYB's average sign collapses with off-diagonal hybridisation, spin–orbit coupling and low temperature, and worst for f shells; NRG stops at about 3 orbitals; MPS solvers reach about 3 orbitals. The quantum side has a route (Krylov and Arnoldi Green's-function estimators [2], Trotterised Kanamori evolution) with a rough cost of 10^2 to 10^3 Trotter steps × 10^4 to 10^5 non-Clifford gates × 10^3 to 10^4 samples, i.e. 10^9 to 10^12 T gates, before state preparation, extra observables and the self-consistency loop. No end-to-end resource estimate exists for a 5-orbital impurity with SOC; that number decides whether this direction is alive.

## What is known

- The classical side is moving: tensor-train and tensor-cross-interpolation diagrammatics sum CT-QMC expansions deterministically without a sign problem [4], and neural-network impurity solvers are orders of magnitude faster than CT-HYB on multi-orbital problems [3]. If these cover the f-shell-with-SOC region, the quantum solver has no territory.
- Hardware demonstrations are at 2-site and 14-qubit scale [7]; they show the loop closes, not that it wins.
- Embedding error (U, double counting, single-site approximation) is usually larger than solver error; the quantum computer removes only the latter. This bounds the value of a perfect solver from above.

## What would settle it

See the front matter. The classical half is a systematic CT-HYB and TCI/MPS benchmark on synthetic impurities with controlled SOC and hybridisation, reporting sign and cost; the quantum half is a gate-level count for one Green's-function estimator at matched accuracy, using existing compilers for Trotterised Kanamori Hamiltonians. Deliverable: a map in the (orbitals, SOC, T) space with three regions coloured by which solver is cheapest. A PhD-length project if done for both d and f shells with real-material parameters; the synthetic d-shell map alone is a few months.

## Who could take it

A DMFT group with CT-HYB (TRIQS or w2dynamics) and an interest in quantum solvers, or a quantum-algorithms group willing to run the classical benchmarks honestly. The result sets the verdict of `dmft-impurity-solver` and of the three application pages that depend on it.

## Resource-count assumptions

The gate range quoted here is a sensitivity calculation: assume 10²–10³ time steps, 10⁴–10⁵ compiled T gates per step and 10³–10⁴ repetitions of one measured circuit. Multiplying endpoints gives **10⁹–10¹² T gates**. These inputs are not calibrated for a named impurity or a target error. The range excludes state preparation, additional time points and Green's-function components, bath convergence and DMFT iterations, so it is not an end-to-end estimate or a hardware readiness claim. See the [impurity-solver page](../methods/dmft-impurity-solver.html) for the conditions that remain to be checked.
