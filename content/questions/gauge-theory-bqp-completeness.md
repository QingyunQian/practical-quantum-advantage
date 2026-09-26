---
type: question
id: gauge-theory-bqp-completeness
title: Is real-time dynamics of lattice gauge theories BQP-complete?
title_zh: 格点规范理论的实时动力学是否 BQP-完全？
summary: "Hamiltonian simulation of generic local Hamiltonians and scattering in scalar φ⁴ theory are BQP-complete, which is the strongest hardness evidence in the catalogue. No such result exists for any gauge theory: not Z2, U(1) or truncated SU(2), in any dimension, despite rapid progress on lattice-gauge-theory quantum algorithms and hardware demonstrations. Proving it would put lattice QCD-type dynamics on the same footing as φ⁴; a proof that gauge constraints make it easier would be equally important."
summary_zh: 通用局域哈密顿量的模拟和标量 φ⁴ 理论的散射是 BQP-完全的，这是本目录中最强的硬度证据。对任何规范理论（Z2、U(1)、截断 SU(2)，任意维度）都没有这样的结果，尽管格点规范理论的量子算法和硬件演示进展很快。证明它会让格点 QCD 类动力学与 φ⁴ 处于同等地位；若证明规范约束反而使问题变容易，同样重要。
status: seed
last_verified: 2026-09-26
question:
  what_would_settle_it: "Either a reduction showing that estimating a local observable after real-time evolution under a 2+1D Z2 (or U(1) or truncated SU(2)) lattice gauge theory with matter, to inverse-polynomial precision, is BQP-hard (universality of the gauge-fixed Hamiltonian via a Cubitt–Montanaro–Piddock-type argument, with Gauss's law implemented at polynomial overhead), together with the known BQP upper bound; or a polynomial-time classical algorithm for the gauge-invariant sector of some family, which would show that gauge constraints remove hardness. The 2+1D Z2 case with matter is the easiest target."
  difficulty: open-problem
  resolved: false
related:
  problems: [quench-dynamics]
  methods: [phase-estimation]
  claims: [google-quantum-echoes-otoc-2025]
references:
  - {arxiv: "1111.3633", title: "Quantum Algorithms for Quantum Field Theories", authors: "S. P. Jordan, K. S. M. Lee, J. Preskill", year: 2012, note: "Science 336, 1130 (2012)"}
  - {arxiv: "1703.00454", title: "BQP-completeness of Scattering in Scalar Quantum Field Theory", authors: "S. P. Jordan, H. Krovi, K. S. M. Lee, J. Preskill", year: 2018, note: "Quantum 2, 44 (2018)"}
  - {arxiv: "2606.30396", title: "Provable Quantum Advantage for Dynamical Phase Transition", authors: "(LOCAL-DQPT is BQP-complete for constant k)", year: 2026}
  - {arxiv: "2603.26561", title: "Complexity of Quadratic Bosonic Hamiltonian Simulation: BQP-Completeness and PostBQP-Hardness", authors: "(BQP-completeness even for quadratic bosonic Hamiltonians)", year: 2026}
  - {arxiv: "2507.01089", title: "Quantum Simulation of QED in Coulomb Gauge", authors: "X. Yao", year: 2025}
---

## Why it matters

Quantum-system simulation is one candidate application family in this catalogue. Within that family the hardness evidence is strongest where a BQP-completeness reduction exists, because then a polynomial classical algorithm would imply BPP = BQP. That has been proved for generic local Hamiltonian dynamics, for one-dimensional translation-invariant chains, for quadratic bosonic Hamiltonians [4], for dynamical quantum phase transitions [3] and, in field theory, for scattering in massive scalar φ⁴ theory coupled to classical sources [1, 2]. It has not been proved for any gauge theory. That is a gap in exactly the place physicists care about: real-time dynamics of QED and QCD at finite density, where lattice Monte Carlo has a sign problem, is the canonical motivation for quantum simulation, and the algorithms are being built (Coulomb-gauge QED with a 10^8-fold gate reduction over earlier encodings [5], SU(2) pure-gauge encodings, qudit hardware for 2D lattice gauge theories, gauge-covariant error correction). The cited scalar-field reductions do not establish the corresponding result for Z2, U(1) or SU(2) gauge theories. A resolution needs a precise choice of encoding, allowed inputs and observables.

The catalogue's honest caveat applies here in the strongest form: a BQP-hard instance family is an encoding of universal computation, and a proof would not show that any particular physical coupling is hard. What it would show is that no general-purpose classical method for gauge-theory dynamics can exist, which is the statement funding agencies actually rely on when they cite lattice QCD as a quantum-computing application.

## What is known

- Upper bound: gauge theories on a lattice with truncated link Hilbert spaces are local Hamiltonians, so their dynamics is in BQP; the constraint (Gauss's law) can be enforced by projection or by gauge-fixing at polynomial cost.
- Lower bound: the natural route is to gauge-fix, obtain a matter Hamiltonian with modified interactions, and show that the resulting family is universal in the sense of Cubitt–Montanaro–Piddock (able to encode arbitrary local Hamiltonians up to polynomial overhead). For 2+1D Z2 gauge theory coupled to matter this looks like a technical rather than conceptual step and is the target this repository ranks third among tractable open theory problems. For U(1) and truncated SU(2), the obstacle is that the gauge-invariant sector is a specific subspace and universality must be shown inside it.
- The obvious counter-scenario is that the gauge-invariant sector of some family is classically simulable (as pure Z2 gauge theory without matter is, via its dual Ising form); a clean statement of which families fall on which side would be a result in its own right.

## What would settle it

See the front matter. This is a theory problem: a reduction, or a classical algorithm. The Z2-with-matter case is estimated at difficulty 2 to 3 on a five-point scale in the survey behind this page, i.e. months of technical work by someone fluent in Hamiltonian complexity; the U(1)/SU(2) scattering version in the Jordan–Lee–Preskill sense is harder (upper bound 3, lower bound 4). No numerics settle this.

## Who could take it

A Hamiltonian-complexity theorist with a lattice-gauge-theory collaborator. The result would upgrade `quench-dynamics` for gauge theories from `empirical` to `reduction` on the classical-hardness axis, the only such upgrade available to a physically motivated application in this catalogue.
