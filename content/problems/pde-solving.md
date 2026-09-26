---
type: problem
id: pde-solving
title: Solving partial differential equations
title_zh: 偏微分方程求解
summary: The computational task behind weather, CFD, electromagnetics and structural engineering. Chaotic and turbulent regimes are ruled out by an exp(Ω(T)) bound; short-time geometrically local linear dynamics is dequantized; the heat equation admits at most a quadratic speedup in d ≥ 2 and the linear-system route is never faster than the best classical method. What remains is a polynomial gain on wave-type problems with a scalar output, which does not pay under error correction.
summary_zh: 天气、流体、电磁、结构工程背后的计算任务。混沌与湍流区被 exp(Ω(T)) 下界排除；短时间的几何局域线性动力学已被去量子化；热方程在 d ≥ 2 维至多二次加速，且线性方程组路线从不快于最佳经典方法。剩下的是波动型问题在标量输出下的多项式增益，在纠错开销下不划算。
status: seed
last_verified: 2026-09-26
verdict: uneconomic
dimensions:
  classical_hardness: {level: none, note: "for the PDEs industry solves, multigrid and spectral methods are near-linear in the grid size; the classical cost is scale, and data-driven surrogates lower it further; the only hard regime (long-time local linear dynamics) is one nobody buys"}
  quantum_easiness: {level: conditional, note: "linear PDEs: QLSA or Hamiltonian simulation given block-encodable operator, formula-defined source, polylog condition number and scalar output; nonlinear PDEs: Carleman linearisation only for weak nonlinearity; chaotic: no"}
  willingness_to_pay: {level: second-hand, note: "every engineering discipline would pay for faster PDE solves, but no buyer has stated a target for a quantum solver; the derived applications (RCS, CFD, weather) are each catalogued separately"}
resources: {gates: "depth ~1e29 for the one fully compiled instance (2D RCS, N=3.3e8)", note: "Scherer et al. 2017; no other end-to-end estimate on an industrial PDE has been independently checked"}
related:
  applications: [weather-forecasting, turbulence-cfd, radar-cross-section, derivative-pricing]
  problems: [sparse-linear-systems, monte-carlo-expectation]
  methods: [hhl-qsvt]
references:
  - {arxiv: "2307.09593", title: "Limitations for Quantum Algorithms to Solve Turbulent and Chaotic Systems", authors: "D. Lewis, S. Eidenbenz, B. Nadiga, Y. Subaşı", year: 2024, note: "Quantum 8, 1509"}
  - {arxiv: "2505.10445", title: "On the quantum computational complexity of classical linear dynamics with geometrically local interactions: Dequantization and universality", authors: "K. Sakamoto, K. Fujii", year: 2026, note: "Quantum 10, 2182"}
  - {arxiv: "2004.06516", title: "Quantum vs. classical algorithms for solving the heat equation", authors: "N. Linden, A. Montanaro, C. Shao", year: 2022, note: "Commun. Math. Phys. 395, 601; ten algorithms compared"}
  - {arxiv: "1512.05903", title: "Quantum algorithms and the finite element method", authors: "A. Montanaro, S. Pallister", year: 2016, note: "Phys. Rev. A 93, 032324"}
  - {arxiv: "1010.2745", title: "High-order quantum algorithm for solving linear differential equations", authors: "D. W. Berry", year: 2014, note: "J. Phys. A 47, 105301; the linear-ODE-to-linear-system route"}
  - {arxiv: "2011.03185", title: "Efficient quantum algorithm for dissipative nonlinear differential equations", authors: "J.-P. Liu, H. Ø. Kolden, H. K. Krovi, N. F. Loureiro, K. Trivisa, A. M. Childs", year: 2021, note: "PNAS 118, e2026805118; Carleman linearisation"}
  - {arxiv: "1505.06552", title: "Concrete resource analysis of the quantum linear system algorithm used to compute the electromagnetic scattering cross section of a 2D target", authors: "A. Scherer et al.", year: 2017, note: "Quantum Inf. Process. 16, 60"}
  - {arxiv: "2512.03758", title: "An end-to-end quantum algorithm for nonlinear fluid dynamics with bounded quantum advantage", authors: "D. Jennings, K. Korzekwa, M. Lostaglio, R. Ashworth, E. Marsili", year: 2025}
  - {arxiv: "2607.12688", title: "Quantum PDE Solvers in Practice: Application-Driven Benchmarking of the Heat Equation", authors: "M. Elkarargy, A. Rahwan, A. Elsayed, F. Hatem, et al.", year: 2026}
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103"}
---

## Best classical

Finite-difference, finite-element and spectral discretisations, with multigrid or Krylov solvers whose cost is near-linear in the number of grid points N per time step. The cost of an industrial solve is set by N (resolution, dimension, time horizon), not by any per-step hardness: the solvers are mature, parallel and, for the most common equations, close to optimal. Since 2023, learned surrogates have cut the cost of repeated solves in weather and CFD by large factors at slightly reduced fidelity. Classical hardness in the complexity sense appears only in exotic regimes: Sakamoto and Fujii show that simulating geometrically local linear dynamics for exponentially long times is as hard as exponential-time polynomial-space quantum computation [2], a regime with no engineering counterpart.

## Best quantum

Three routes exist, each with its own no-go.

Linear PDEs via linear systems. Discretise, then apply a quantum linear-system solver (Berry's construction for linear ODEs [5], the finite-element analysis of Montanaro and Pallister [4]). The fine print is that of [sparse linear systems](sparse-linear-systems.html): the source must be prepared from a formula, the operator block-encoded, the condition number kept polylog, and only a scalar functional read out. Under those conditions Montanaro and Pallister find a polynomial speedup whose degree grows with the spatial dimension, and give evidence that no improvement of the quantum algorithm yields a super-polynomial speedup at fixed dimension when the solution is smooth [4]. For the heat equation Linden, Montanaro and Shao compare ten classical and quantum algorithms for computing the heat in a region and find that in d ≥ 2 the best quantum route (amplitude estimation on an accelerated random walk) is at most quadratically faster, and that the linear-system route is never faster than the best classical algorithm [3]. The single fully compiled industrial instance, the 2D radar cross-section, has circuit depth of order 1e29 once oracles are counted [7]. An application-driven benchmark of heat-equation solvers in 2026 finds no resource advantage across the kernels tested [9].

Linear dynamics via Hamiltonian simulation. Wave-type and Maxwell equations can be written as Schrödinger-like evolutions and simulated directly, with the source and the receiver functional defined by formulas. This is the route with the fewest violated preconditions, and it is where the survey's closest engineering match (a single-receiver acoustic or seismic response) sits. Sakamoto and Fujii dequantize the simulation of short-time (polynomial-time) geometrically local classical linear dynamics, so there is no exponential advantage in this regime; the gain is polynomial at best, and the medium (velocity model) is data that has to be loaded [2].

Nonlinear PDEs via Carleman linearisation. Liu et al. embed a dissipative nonlinear ODE into a larger linear one, with convergence only for weak nonlinearity relative to dissipation [6]. Lewis et al. tighten these bounds and prove a general limitation: for any system with a positive Lyapunov exponent and sub-exponentially growing solutions, any quantum algorithm outputting a state approximating the normalised solution costs exp(Ω(T)) in the integration time [1]. Chaotic and turbulent regimes are therefore excluded for any solver that outputs the field; the best remaining analysis of turbulence statistics, by Jennings et al., bounds the gain at O(Re^{3D/8}) for selected observables [8].

## What survives

Linear, well-conditioned, wave-type problems with formula-defined sources, a scalar receiver output and a required precision of 1/poly, in high enough spatial dimension that the Montanaro–Pallister polynomial is worth having. Every such gain is polynomial, and Babbush et al.'s break-even analysis makes speedups below quartic uneconomic under surface-code overheads [10]. No industrial instance in this window has a resource estimate that has been independently checked.

## Verdict

Uneconomic, with no-go sub-regimes. Chaotic and turbulent dynamics and any full-field output are ruled out by lower bounds; short-time local linear dynamics is dequantized; the heat equation and FEM admit at most polynomial gains; the one compiled instance has depth 1e29. The task class survives only as a polynomial speedup on wave-type scalar-output problems, and the catalogue's applications built on it (weather, CFD, RCS) each fail on their own page. It would move to surviving if an engineering problem were exhibited with formula-defined input, scalar output, bounded condition number and an end-to-end estimate showing a super-quadratic separation.
