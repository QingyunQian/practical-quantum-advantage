---
type: question
id: dmft-impurity-cost-vs-ctqmc-sign-problem
title: Which DMFT impurity defeats the best classical solver, and can a quantum solver help?
title_zh: 哪个 DMFT 杂质超出最强经典求解器的能力，量子求解器能否帮助？
summary: "Sign-problem papers supply concrete CT-HYB bottlenecks and classical responses: Inchworm solves a low-temperature model whose CT-HYB cost was extrapolated to 3 billion core-hours, while hybrid DMFT runs roughly 40 times faster than full five-orbital DMFT on two real oxides. A quantum advantage needs the strongest classical baseline on the same impurity and observable."
summary_zh: 符号问题论文给出了 CT-HYB 的具体瓶颈，也给出了经典替代方案：Inchworm 求解了一个 CT-HYB 外推需要约 30 亿核小时的低温模型；混合 DMFT 在两种真实氧化物上比完整五轨道 DMFT 快约 40 倍。量子优势必须在同一杂质和输出量上与最强经典方法比较。
status: seed
last_verified: 2026-09-27
question:
  what_would_settle_it: "Publish a named impurity Hamiltonian or hybridisation function, temperature and output observable tied to an application. Show a matched error-versus-cost comparison among optimised CT-HYB, Inchworm, hybrid DMFT where its approximation is valid, tensor-train, MPS and neural-network solvers. Document bath-discretisation and embedding errors. Compile a fault-tolerant quantum Green's-function algorithm on that identical model, including state preparation, ancillas, repetitions and the full DMFT loop. Report whether a documented accuracy or throughput requirement is reached at lower total cost. A small CT-HYB average sign by itself does not settle the question."
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
  - {arxiv: "2206.15093", title: "Ce and Dy substitutions in Nd$_{2}$Fe$_{14}$B: site-specific magnetic anisotropy from first-principles", authors: "J. Boust et al.", year: 2022, note: "Direct alloy study; mixed-valent Ce modelled approximately"}
  - {arxiv: "2510.02875", title: "Redox Chemistry of LiCoO$_2$, LiNiO$_2$, and LiNi$_{1/3}$Mn$_{1/3}$Co$_{1/3}$O$_2$ Cathodes: Deduced via XPS, DFT+DMFT, and Charge Transfer Multiplet Simulations", authors: "Y. Xie, F. Mellin, W. Jaegermann, S. Hofmann, F. M. F. de Groot, H. Zhang", year: 2025}
  - {arxiv: "2404.09527", title: "Dynamical Mean Field Theory for Real Materials on a Quantum Computer", authors: "J. Selisko, M. Amsler, C. Wrigley et al.", year: 2024, note: "Ca2CuO2Cl2 on 14 IBM qubits"}
  - {arxiv: "1907.08570", title: "A Multiorbital Quantum Impurity Solver for General Interactions and Hybridizations", authors: "E. Eidelstein, E. Gull, G. Cohen", year: 2019, note: "Figs. 1-3; Inchworm versus CT-HYB on matched models"}
  - {arxiv: "2601.04832", title: "Affordable Five-Orbital Dynamical Mean-Field Theory for Layered Iridates and Rhodates", authors: "L. Gaspard, C. Martins", year: 2026, note: "Table 4; full DMFT and hybrid DMFT on two real materials"}
  - {arxiv: "1907.11298", title: "Alleviating the Sign Problem in Quantum Monte Carlo Simulations of Spin-Orbit-Coupled Multi-Orbital Hubbard Models", authors: "A. J. Kim, P. Werner, R. Valentí", year: 2020, note: "basis optimisation changes the measured CT-HYB sign"}
  - {arxiv: "1504.07979", title: "Electronic structure and core-level spectra of light actinide dioxides in the dynamical mean-field theory", authors: "J. Kolorenč, A. B. Shick, A. I. Lichtenstein", year: 2015, note: "classically solved UO2/NpO2/PuO2 benchmark; valence and 4f-core XPS"}
---

## Why it matters

DMFT has material users. A direct Ce-substituted Nd₂Fe₁₄B study used Hubbard-I for localised Nd 4f states and approximated mixed-valent Ce through LSDA and an experimentally informed sublattice model [5]. The need for a more dynamical Ce treatment is a research question; the paper did not show that CT-QMC fails for its alloy. A cathode spectroscopy study combined DFT+DMFT with a separate charge-transfer multiplet calculation [6]. **That cathode study solved its DMFT impurity with classical CT-QMC**, then used Quanty for the core-level XPS. A discretised impurity with five d orbitals and four bath orbitals per spin orbital would have 50 system qubits; eight bath orbitals would give 90. These counts do not establish bath convergence or quantum advantage for the cited materials.

Hard impurity regimes exist, but difficulty depends on the Hamiltonian, basis, temperature and observable. Off-diagonal hybridisation and spin–orbit coupling can worsen CT-HYB's sign; [8–10] show why one solver's failure does not determine the classical frontier. The quantum side has Krylov and Arnoldi Green's-function approaches [2]. Multiplying illustrative step, gate and shot ranges gives 10^9–10^12 T gates for one measured circuit, before state preparation, additional observables or self-consistency. No end-to-end estimate exists for a named five-orbital SOC or actinide fuel impurity at a specified error. The classically solved oxide spectra [11] should not be used as evidence of such a failure.

## What is known

| Instance and observable | Measured or reported classical result | Limit of the evidence |
|---|---|---|
| Two-orbital Kanamori impurity with continuous Bethe bath; imaginary-time Green's function at βt = 64 [8] | CT-HYB cost of comparable quality extrapolated to ~3 × 10⁹ core-hours; classical Inchworm ran for ~1.5 × 10³ core-hours and gave controlled results | The huge CT-HYB cost is an extrapolation; this is a model impurity, not an industrial material or a quantum benchmark |
| Ba₂IrO₄ five-orbital DMFT [9] | Full classical DMFT converged with CT-QMC average sign 0.37; hybrid DMFT obtained sign 0.53 and a 43.8-fold total-time speedup | Hybrid DMFT treats part of the orbital manifold at mean-field level; the result concerns an oxide research problem |
| Ba₂RhO₄ five-orbital DMFT [9] | Full-DMFT sign 0.58; hybrid-DMFT sign 0.60 and 41.2-fold total-time speedup | Neither method establishes an industrial buyer or a quantum crossover |
| UO₂, NpO₂ and PuO₂ valence and 4f-core XPS [11] | LDA+DMFT with classical Lanczos on 14 impurity plus 14 bath spin orbitals reproduced the reported spectra | This is a finite-bath success case; M-edge XAS is a different observable, and a harder fuel instance is not identified |

The first row is unusually clear evidence that **one classical algorithm** has a bottleneck, followed by evidence that another classical algorithm overcame it for the same Green's function. In the oxide examples, the full five-orbital calculation itself completed, and the cheaper approximation reproduced the reported low-energy self-energies within Monte Carlo noise [9]. The classical frontier also includes basis optimisation for CT-HYB [10], tensor-train diagram summation [4] and neural-network embedding solvers [3]. These methods must be considered before calling a sign-problem instance classically intractable.

- Hardware demonstrations are at 2-site and 14-qubit scale [7]; they show the loop closes, not that it wins.
- The cathode example [6] already has a successful classical CT-QMC calculation. Its core-hole physics is handled in a distinct multiplet step, so a quantum solver for the first-stage impurity cannot claim the full XPS computation as its benchmark.
- Embedding error (U, double counting, single-site approximation) is usually larger than solver error; the quantum computer removes only the latter. This bounds the value of a perfect solver from above.

## What would settle it

See the front matter. First reproduce one published hybridisation function and output, including the classical Inchworm or hybrid-DMFT result where applicable [8, 9]. Then test CT-HYB with an optimised basis [10], tensor-train and MPS alternatives, recording errors as well as the average sign. Only after the best classical cost curve is established should a quantum Green's-function circuit be compiled at matching accuracy, with the bath and state-preparation requirements stated. The current papers do not provide that quantum curve.

## Who could take it

A DMFT group with CT-HYB (TRIQS or w2dynamics) and an interest in quantum solvers, or a quantum-algorithms group willing to run the classical benchmarks honestly. The result sets the verdict of `dmft-impurity-solver` and of the three application pages that depend on it.

## Resource-count assumptions

The gate range quoted here is a sensitivity calculation: assume 10²–10³ time steps, 10⁴–10⁵ compiled T gates per step and 10³–10⁴ repetitions of one measured circuit. Multiplying endpoints gives **10⁹–10¹² T gates**. These inputs are not calibrated for a named impurity or a target error. The range excludes state preparation, additional time points and Green's-function components, bath convergence and DMFT iterations, so it is not an end-to-end estimate or a hardware readiness claim. See the [impurity-solver page](../methods/dmft-impurity-solver.html) for the conditions that remain to be checked.
