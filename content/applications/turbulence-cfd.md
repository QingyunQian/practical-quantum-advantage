---
type: application
id: turbulence-cfd
title: Turbulent flow simulation (CFD)
title_zh: 湍流模拟（计算流体力学）
summary: Engineers buy resolved flow fields at high Reynolds number. Lewis et al. prove that any quantum algorithm outputting the state of a chaotic system costs exp(Ω(T)), which rules out the field; the surviving target is a few statistics, for which the best end-to-end analysis (Jennings et al.) bounds the speedup by O(Re^{3D/8}), a polynomial that does not pay under error correction.
summary_zh: 工程师要买的是高雷诺数下的完整流场。Lewis 等证明任何输出混沌系统状态的量子算法代价为 exp(Ω(T))，这就排除了流场本身；剩下的目标是少数统计量，而最好的端到端分析（Jennings 等）把加速上界定为 O(Re^{3D/8})，这是一个在纠错开销下不划算的多项式。
status: seed
last_verified: 2026-09-26
verdict: no-go
dimensions:
  classical_hardness: {level: empirical, note: "direct numerical simulation at Kolmogorov resolution scales as a power of Re and is out of reach at engineering Re; industry uses RANS/LES models instead, which are cheap and calibrated"}
  quantum_easiness: {level: no, note: "full-field output: exp(Ω(T)) for chaotic dynamics (Lewis et al.); Carleman linearisation converges only for weak nonlinearity; selected statistics: bounded polynomial speedup at most (Jennings et al.)"}
  willingness_to_pay: {level: second-hand, note: "aerospace, automotive and energy would pay for resolved high-Re flows; no company has written a target for a quantum solver, and the published estimates come from algorithm groups"}
resources: {note: "Zhuang et al. claim 8.71e6 physical qubits and 42.6 days for a 2^80-grid Navier–Stokes instance at 5e-4 error rate; not independently checked, and its output model must be reconciled with the Lewis bound"}
related:
  problems: [pde-solving, sparse-linear-systems, monte-carlo-expectation]
  methods: [hhl-qsvt]
  applications: [weather-forecasting]
references:
  - {arxiv: "2307.09593", title: "Limitations for Quantum Algorithms to Solve Turbulent and Chaotic Systems", authors: "D. Lewis, S. Eidenbenz, B. Nadiga, Y. Subaşı", year: 2024, note: "Quantum 8, 1509; exp(Ω(T)) lower bound and tightened Carleman bounds"}
  - {arxiv: "2512.03758", title: "An end-to-end quantum algorithm for nonlinear fluid dynamics with bounded quantum advantage", authors: "D. Jennings, K. Korzekwa, M. Lostaglio, R. Ashworth, E. Marsili", year: 2025, note: "lattice-Boltzmann route; speedup bounded by O(Re^{3D/8}); numerics suggest less"}
  - {arxiv: "2011.03185", title: "Efficient quantum algorithm for dissipative nonlinear differential equations", authors: "J.-P. Liu, H. Ø. Kolden, H. K. Krovi, N. F. Loureiro, K. Trivisa, A. M. Childs", year: 2021, note: "PNAS 118, e2026805118; Carleman linearisation, requires weak nonlinearity"}
  - {arxiv: "2509.08807", title: "A Pathway to Practical Quantum Advantage in Solving Navier-Stokes Equations", authors: "X.-N. Zhuang, Z.-Y. Chen, M.-Y. Tan, J. Zhang, C.-C. Ye, et al.", year: 2025, note: "claims 2^80 grid with 8.71 million physical qubits in 42.6 days; unverified"}
  - {arxiv: "2511.18802", title: "Toward end-to-end quantum simulation of rapidly distorted turbulence", authors: "Z. Meng, L. Chen, J.-P. Liu, G. He", year: 2025, note: "linear rapid-distortion turbulence via LCHS with statistics as output"}
  - {arxiv: "2505.10445", title: "On the quantum computational complexity of classical linear dynamics with geometrically local interactions: Dequantization and universality", authors: "K. Sakamoto, K. Fujii", year: 2026, note: "Quantum 10, 2182; applies to the linearised routes"}
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103"}
---

## Who needs it

Aircraft and turbine makers (drag, lift, stall margins), automotive (aerodynamics, cabin acoustics), energy (combustion, wind-farm wakes), process industries (mixing). CFD is among the largest consumers of engineering HPC time. What a designer buys is a resolved flow field or a derived quantity (drag coefficient, heat-transfer rate, pressure spectrum) at the operating Reynolds number.

## Bottleneck

Direct numerical simulation must resolve the Kolmogorov scale, so the grid grows as a power of the Reynolds number (Re^{9/4} in three dimensions under the standard Kolmogorov estimate, which Jennings et al. adopt as their resolution assumption [2]), and engineering Reynolds numbers are far beyond what DNS reaches. Industry therefore runs modelled equations (RANS, LES) whose fidelity is limited by the turbulence model, not by compute. The unmet demand is DNS-grade fidelity at engineering Re.

## Computational problems

- [PDE solving](../problems/pde-solving.html): nonlinear, chaotic, in 3D.
- [Sparse linear systems](../problems/sparse-linear-systems.html): the linearised solves inside every time step and inside Carleman-type embeddings.
- [Monte Carlo expectation](../problems/monte-carlo-expectation.html): statistics over realisations, the only output form that survives.

## Why the field is out of reach

Turbulence is chaotic by definition. Lewis et al. prove that, in natural coordinates, for a dynamical system with one or more positive Lyapunov exponents and sub-exponentially growing solutions, any quantum algorithm that outputs a state approximating the normalised solution vector has complexity at least exponential in the integration time [1]. This is independent of the solver: it applies to Carleman linearisation, to Schrödingerisation, to lattice-Boltzmann embeddings and to anything else that ends in a state carrying the velocity field. The same paper tightens the worst-case bounds of the Carleman algorithm of Liu et al. [3], which in any case converges only for weakly nonlinear (dissipation-dominated) flows, the opposite of turbulence. On top of the dynamics bound, the field is N numbers and reading it out costs Ω(N).

## What survives: statistics

Lewis's bound constrains outputting the state, not a coarse observable. Jennings et al. take this route seriously: they first show that the Carleman-based proposals fail on convergence, time stepping, condition number and data extraction, then build an incompressible lattice-Boltzmann algorithm and cost it end to end, including gate counts. At Kolmogorov resolution in dimension D the quantum cost is lower-bounded by O(Re^{3(1+D/2)/4} × q_M) with an extraction overhead q_M = O(Re^{3/8}) for the drag force, so the improvement over classical scaling is at most O(Re^{3D/8}), and their numerics indicate less (Re^{1.936} × q_M in D = 2) [2]. In 3D the bound is Re^{9/8}, a polynomial gain of modest degree, obtained only for selected observables in the high-error-tolerance regime. Babbush et al.'s break-even analysis makes speedups of this degree uneconomic once error-correction overheads are included [7].

Two other routes are on record. Meng et al. simulate rapidly distorted turbulence, a linear model, by linear combination of Hamiltonians with statistics as output [5]; being linear and local it is subject to the Sakamoto–Fujii dequantization at short times [6]. Zhuang et al. claim an end-to-end exponential speedup with 8.71 million physical qubits and 42.6 days for a 2^80-grid Navier–Stokes instance [4]; this has not been independently checked, and any such claim has to state what is output and how the Lewis bound is avoided.

## Verdict

No-go for the application as the buyer defines it (a resolved field at engineering Re): the obstruction is a theorem about chaotic dynamics plus an Ω(N) readout, and no solver improvement changes it. The residual target, a handful of flow statistics, is at best a bounded polynomial speedup with no first-hand buyer, and belongs in the uneconomic category. The entry would be revisited if an end-to-end estimate for a named industrial observable (drag on a specified geometry at specified Re) showed a super-quadratic separation after all extraction and error-correction costs.
