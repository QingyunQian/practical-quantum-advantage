---
type: application
id: radar-cross-section
title: Radar cross-section of a target
title_zh: 目标的雷达散射截面
summary: The textbook match for the quantum linear-system algorithm, since the output is a single scalar computed from a sparse discretised Maxwell system. The only full gate-level estimate, by Scherer et al. for a 2D target with 3.3e8 unknowns, gives a circuit depth of order 1e25 without the geometry oracle and 1e29 with it. The algorithm exists; the numbers rule it out for decades.
summary_zh: 量子线性方程组算法的教科书式匹配：输出是一个标量，来自稀疏的离散 Maxwell 方程组。唯一的门级完整估计（Scherer 等，二维目标、3.3×10⁸ 个未知数）给出不计几何 oracle 时电路深度 10²⁵、计入后 10²⁹。算法存在，但这些数字在几十年内排除了它。
status: seed
last_verified: 2026-09-26
verdict: uneconomic
dimensions:
  classical_hardness: {level: none, note: "the crossover size N=3.3e8 in Scherer et al. is defined as the point where a crude big-O comparison first favours the quantum solver; below it classical iterative solvers win outright, and fast-multipole methods scale near-linearly"}
  quantum_easiness: {level: conditional, note: "QLSA applies given a sparse block encoding of the discretised Maxwell operator, a source state prepared from a formula, and a condition number that stays polylog; the condition number grows with mesh refinement and frequency"}
  willingness_to_pay: {level: second-hand, note: "stealth design and radar signature analysis are real engineering needs in aerospace and defence, but no buyer has stated a target for a quantum solver"}
resources: {logical_qubits: "~340 (oracle excluded) to ~1e8 (oracle included)", gates: "depth ~1e25 (oracle excluded), ~1e29 (oracle included)", note: "N = 332,020,680 unknowns, target accuracy 0.01, 2D scattering, Scherer et al. 2017"}
related:
  problems: [sparse-linear-systems, pde-solving]
  methods: [hhl-qsvt, qram]
  applications: [weather-forecasting]
references:
  - {arxiv: "1505.06552", title: "Concrete resource analysis of the quantum linear system algorithm used to compute the electromagnetic scattering cross section of a 2D target", authors: "A. Scherer, B. Valiron, S.-C. Mau, S. Alexander, E. van den Berg, T. E. Chapuran", year: 2017, note: "Quantum Inf. Process. 16, 60; width 340 / depth 1e25 without oracle, width 1e8 / depth 1e29 with oracle"}
  - {arxiv: "1301.2340", title: "Preconditioned quantum linear system algorithm", authors: "B. D. Clader, B. C. Jacobs, C. R. Sprouse", year: 2013, note: "Phys. Rev. Lett. 110, 250504; the RCS formulation that Scherer et al. cost out"}
  - {arxiv: "0811.3171", title: "Quantum algorithm for solving linear systems of equations", authors: "A. W. Harrow, A. Hassidim, S. Lloyd", year: 2009, note: "Phys. Rev. Lett. 103, 150502"}
  - {arxiv: "1512.05903", title: "Quantum algorithms and the finite element method", authors: "A. Montanaro, S. Pallister", year: 2016, note: "Phys. Rev. A 93, 032324; at fixed dimension with smooth solutions the FEM speedup is polynomial only"}
  - {doi: "10.1038/nphys3272", title: "Read the fine print", authors: "S. Aaronson", year: 2015, note: "Nature Physics 11, 291"}
---

## Who needs it

Aerospace and defence primes designing low-observable aircraft, ships and missiles, and the agencies that specify them; antenna and automotive-radar designers use the same solvers. The quantity of interest is the radar cross-section (RCS): the far-field scattered power at a given angle and frequency, a single number per configuration.

## Bottleneck

RCS is obtained by solving Maxwell's equations around the target, discretised by finite elements or the method of moments into a sparse (FEM) or dense (MoM) linear system with N unknowns. N grows with the target size in wavelengths, so high-frequency signatures of large targets are expensive, and design loops evaluate many geometries and angles. The output being a scalar functional of the solution is what makes this the canonical candidate for the quantum linear-system algorithm [3]: the fine-print objection that reading out the full solution vector costs Ω(N) does not apply [5]. Clader, Jacobs and Sprouse proposed exactly this formulation with a preconditioner to control the condition number [2].

## Computational problems

- [Sparse linear systems](../problems/sparse-linear-systems.html): the core task.
- [PDE solving](../problems/pde-solving.html): the frequency-domain Maxwell problem that generates the system.

## What the resource estimate says

Scherer et al. compiled the Clader–Jacobs–Sprouse algorithm to a fault-tolerant gate set with the Quipper compiler for a 2D scattering problem [1]. They chose N = 332,020,680 as the problem size beyond which a crude asymptotic comparison first favours the quantum solver, and a target accuracy of 0.01. Excluding the oracles that encode the geometry, material and source, the circuit has width about 340 and depth of order 1e25. Including them, width is of order 1e8 and depth of order 1e29. The authors' own summary is that the oracle cost, usually ignored, dominates, and that a reduction by many orders of magnitude is needed before the algorithm is practical.

To place 1e29 sequential logical operations: at one operation per microsecond, which is optimistic for a fault-tolerant T gate, the run takes 1e23 seconds. No plausible improvement in error correction (two to three orders of magnitude in gate cost over 2024–26) touches a gap of that size. Two structural problems remain even if constants fall. The condition number of the discretised Maxwell operator grows with mesh refinement and frequency, and it enters the quantum cost at least linearly. And the geometry is data: a CAD model is not a formula, so the block encoding that the algorithm assumes has to be built from classical input, which is where the 1e8 width comes from. Montanaro and Pallister's finite-element analysis adds that at fixed spatial dimension with smooth solutions the achievable speedup is polynomial in any case [4].

## Best classical today

Fast-multipole-accelerated MoM and domain-decomposed FEM solve scattering problems of this class on commodity clusters; the N = 3.3e8 crossover in [1] is by construction the size below which the classical solver is faster even under a big-O comparison that ignores all quantum constants.

## Verdict

Uneconomic. The application satisfies the output condition (scalar functional) that most linear-algebra candidates fail, and that is why it deserves a page: it is the cleanest test of whether the sparse-linear-system window has an engineering match, and the answer is a circuit depth of 1e29. There is no first-hand buyer statement, the classical side is not obstructed, and the quantum precondition (polylog condition number, formula-defined input) does not hold for real geometries. The verdict would move only if a new estimate on a 3D target brought the oracle-inclusive depth within perhaps 1e12 while keeping the condition number bounded.
