---
type: application
id: weather-forecasting
title: Numerical weather forecasting
title_zh: 数值天气预报
summary: The application most often named by industry and the least suited to a quantum computer. A forecast ingests a large volume of classical observations, integrates chaotic nonlinear equations, and must output the whole field. Each of the three steps meets a separate lower bound, so no algorithmic progress on PDE solvers changes the answer.
summary_zh: 产业界最常提到的应用，也是最不适合量子计算机的一个。预报要读入海量经典观测数据、积分混沌的非线性方程、再输出整个场，三步各自撞上一条下界，所以偏微分方程求解器的任何算法进展都改变不了结论。
status: seed
last_verified: 2026-09-26
verdict: no-go
dimensions:
  classical_hardness: {level: none, note: "operational forecasts already run on schedule on conventional supercomputers; the cost is scale, not an obstruction, and data-driven models have lowered it further"}
  quantum_easiness: {level: no, note: "chaotic dynamics: any algorithm that outputs the state costs exp(Ω(T)) (Lewis et al.); linear local parts are dequantized at short times (Sakamoto–Fujii); input and output are Ω(N)"}
  willingness_to_pay: {level: second-hand, note: "Tennie and Palmer discuss the case from inside the weather community; no met service has written a speed or accuracy target for a quantum solver"}
resources: {note: "no end-to-end resource estimate exists for an operational forecast; the obstruction is at the level of lower bounds, not gate counts"}
related:
  problems: [pde-solving, sparse-linear-systems, monte-carlo-expectation, sorting-fft-storage]
  methods: [hhl-qsvt, qram]
  applications: [turbulence-cfd]
references:
  - {arxiv: "2210.17460", title: "Quantum Computers for Weather and Climate Prediction: The Good, the Bad and the Noisy", authors: "F. Tennie, T. Palmer", year: 2022, note: "assessment from the weather-modelling side; names big-data input as the central obstacle"}
  - {arxiv: "2307.09593", title: "Limitations for Quantum Algorithms to Solve Turbulent and Chaotic Systems", authors: "D. Lewis, S. Eidenbenz, B. Nadiga, Y. Subaşı", year: 2024, note: "Quantum 8, 1509; exp(Ω(T)) for systems with a positive Lyapunov exponent"}
  - {arxiv: "2505.10445", title: "On the quantum computational complexity of classical linear dynamics with geometrically local interactions: Dequantization and universality", authors: "K. Sakamoto, K. Fujii", year: 2026, note: "Quantum 10, 2182; short-time geometrically local linear dynamics dequantized"}
  - {doi: "10.1038/nphys3272", title: "Read the fine print", authors: "S. Aaronson", year: 2015, note: "Nature Physics 11, 291; the input/output conditions on quantum linear-algebra speedups"}
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103; why the remaining polynomial speedups do not pay"}
---

## Who needs it

National and regional meteorological services (ECMWF, NOAA, the UK Met Office, the China Meteorological Administration), and downstream buyers of their products: reinsurers, energy traders, airlines, agriculture. The buyer is real and the budgets are large, which is why "weather" heads almost every industry list of quantum applications. This page exists because the argument for it collapses at every step once the computational task is written down.

## Bottleneck

An operational forecast has three stages. Data assimilation combines a previous forecast with a large volume of new observations (satellite radiances, radiosondes, surface stations) into an initial state. The model then integrates the discretised primitive equations of the atmosphere, a nonlinear system with chaotic dynamics, for hours to weeks of model time. Finally the entire field (pressure, wind, humidity, temperature at every grid point and level) is written out, because every downstream product reads it. The classical cost is dominated by the integration step and grows with resolution. Met services run it on schedule today; the wish is for higher resolution and larger ensembles at the same wall-clock time. Tennie and Palmer, writing from inside the weather community, single out the "big data" input as the first thing a quantum formulation has to survive [1].

## Computational problems

- [PDE solving](../problems/pde-solving.html): the integration step. Every proposed quantum route (linear-system solvers, Hamiltonian simulation, Carleman linearisation) is assessed there.
- [Sparse linear systems](../problems/sparse-linear-systems.html): the implicit solves and the variational data-assimilation step.
- [Monte Carlo expectation](../problems/monte-carlo-expectation.html): ensemble statistics.
- [Sorting, FFT and storage](../problems/sorting-fft-storage.html): the spectral transforms and the observation database, both of which are pure classical-data I/O.

## Why each stage fails

Input. The observations are classical data. Loading N numbers into amplitudes costs Ω(N) operations however it is done, and the QRAM that would hide this is an addressing structure whose control hardware could run a parallel classical algorithm equally fast [4]. There is no exponential shortcut into the initial state.

Dynamics. The atmosphere has positive Lyapunov exponents; that is what makes it a forecast problem. Lewis et al. prove that for a dynamical system with one or more positive Lyapunov exponents and sub-exponentially growing solutions, any quantum algorithm that outputs a state approximating the normalised solution has cost at least exponential in the integration time [2]. This is a statement about the task, not about a particular algorithm. The linear, geometrically local pieces (advection, diffusion) do not help either: Sakamoto and Fujii dequantize the simulation of short-time geometrically local classical linear dynamics, so no exponential advantage is available there [3].

Output. A forecast is the field, not a scalar. Reading N amplitudes out costs Ω(N) measurements, which cancels any polylog(N) advantage in the solver, the standard "fine print" condition on quantum linear algebra [4]. The only outputs a quantum solver returns cheaply are a few functionals, and no met service consumes a forecast that way.

What is left after the three bounds is a possible polynomial speedup on a linearised sub-problem with a scalar output, which Babbush et al. show does not pay under error-correction overheads unless it is at least quartic [5]. Meanwhile the classical baseline has moved: data-driven forecast models trained on reanalysis data have cut the cost of producing a forecast of comparable skill, so the wall-clock target a quantum solver would have to beat is falling, not rising.

## Verdict

No-go. Not because a quantum PDE solver is slow, but because the forecast task itself violates the input, dynamics and output conditions under which any quantum linear-algebra speedup is defined. Willingness to pay is genuine but second-hand: no met service has stated a target for a quantum solver, and none is likely to, since the same institutions are the ones publishing the obstacles [1]. The page would change only if a met service identified a scalar-output sub-task (a single verification statistic, say) that is classically expensive and does not require reading the field, and no such task is on record.
