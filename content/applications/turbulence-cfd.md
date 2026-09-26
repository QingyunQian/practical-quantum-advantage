---
type: application
id: turbulence-cfd
title: Turbulent flow simulation (CFD)
title_zh: 湍流模拟（计算流体力学）
summary: Engineering CFD needs resolved fields or specified observables at useful accuracy. Lewis et al. bound algorithms outputting a normalised solution state for specified chaotic systems; Jennings et al. analyse selected observables under a lattice-Boltzmann model. These limits weaken proposed quantum routes, but they do not prove a universal no-go for every industrial CFD observable.
summary_zh: 工程流体计算需要在有用精度下给出流场或指定观测量。Lewis 等对满足特定条件的混沌系统中输出归一化解量子态的算法给出下界；Jennings 等在格子玻尔兹曼模型下分析了部分观测量。这些结果限制了现有量子路线，但尚不能证明所有工业流体观测量都无望。
status: seed
last_verified: 2026-09-27
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "direct numerical simulation at Kolmogorov resolution scales as a power of Re and is out of reach at engineering Re; industry uses RANS/LES models instead, which are cheap and calibrated"}
  quantum_easiness: {level: unknown, note: "Lewis et al. bound normalised-state output for specified chaotic dynamics; Carleman convergence is restricted; Jennings et al. give model-dependent bounds for selected statistics. No end-to-end algorithm is established for a named engineering observable."}
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

For systems satisfying its positive-Lyapunov and growth assumptions, Lewis et al. prove an exponential-in-time lower bound on producing an approximate normalised solution state in natural coordinates [1]. This constrains algorithms with that output contract, including proposed linearisations when their assumptions apply. It does not cover every coarse CFD observable or every encoding. The paper also tightens worst-case bounds for the Carleman algorithm of Liu et al. [3], whose convergence requires a weakly nonlinear regime. Independently, distributing an N-value flow field requires Ω(N) output values; that output cost alone does not exclude a polynomial speedup over a more expensive classical computation.

## What survives: statistics

Lewis's bound constrains state output, leaving coarse observables as a separate task. Jennings et al. assess Carleman-based proposals and then construct and cost an incompressible lattice-Boltzmann route, including extraction [2]. Under their resolution and observable assumptions, they bound the available scaling improvement by O(Re^{3D/8}); this is **a bound within their model**, not a theorem for every CFD algorithm. Their numerics indicate a smaller benefit. Babbush et al. estimate that small polynomial speedups are difficult to turn into runtime wins on early surface-code machines under their gate-speed assumptions [7]. An industrial cost comparison would have to fix the observable, fidelity and classical solver.

Two other routes are on record. Meng et al. simulate rapidly distorted turbulence, a linear model, by linear combination of Hamiltonians with statistics as output [5]; being linear and local it is subject to the Sakamoto–Fujii dequantization at short times [6]. Zhuang et al. claim an end-to-end exponential speedup with 8.71 million physical qubits and 42.6 days for a 2^80-grid Navier–Stokes instance [4]; this has not been independently checked, and any such claim has to state what is output and how the Lewis bound is avoided.

## Verdict

Surviving as an application category, with no demonstrated quantum advantage. The cited state-output bound and the cost of reading a full field weaken proposals to deliver direct numerical simulation at engineering Reynolds number; the Jennings analysis limits one route to selected statistics under stated modelling assumptions. A stronger conclusion needs a named observable, geometry, Reynolds number and error tolerance, plus the best classical and compiled quantum time-to-solution on that same task. A buyer-defined threshold is still missing.
