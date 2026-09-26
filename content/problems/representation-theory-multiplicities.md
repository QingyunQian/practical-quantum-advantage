---
type: problem
id: representation-theory-multiplicities
title: Representation-theoretic multiplicities (Kronecker, plethysm, Littlewood–Richardson)
title_zh: 表示论重数（Kronecker 系数、plethysm、Littlewood–Richardson）
summary: Kronecker coefficients and their relatives count multiplicities in tensor products and restrictions of group representations and are central to algebraic combinatorics and geometric complexity theory. Bravyi, Chowdhury, Gosset, Havlíček and Zhu showed the normalised coefficients are quantum-estimable and conjectured a speedup; Panova gave a classical polynomial-time algorithm for the same quantity in 2025, closing the conjecture. The remaining question is which multiplicities, if any, stay quantum-only.
summary_zh: Kronecker 系数及其推广计数群表示张量积与限制中的重数，是代数组合学和几何复杂度理论的核心对象。Bravyi、Chowdhury、Gosset、Havlíček 与 Zhu 证明归一化系数可用量子机估计并猜想有加速；Panova 在 2025 年给出同一量的经典多项式算法，猜想被关闭。剩下的问题是还有哪些重数（如果有的话）只有量子能算。
status: seed
last_verified: 2026-09-26
verdict: no-go
dimensions:
  classical_hardness: {level: none, note: "the normalised Kronecker coefficient that the quantum algorithm estimates has a classical polynomial-time algorithm (Panova 2025); exact coefficients are #P-hard for both sides"}
  quantum_easiness: {level: proven, note: "normalised multiplicities estimable to additive error in BQP; positivity in QMA; plethysm in #BQP; but the estimated quantity is now classically accessible"}
  willingness_to_pay: {level: none, note: "buyers are mathematicians; additive approximations of normalised coefficients are not what they need"}
related:
  problems: [topological-invariants, integer-factoring-hidden-subgroup]
  methods: [phase-estimation]
references:
  - {arxiv: "2302.11454", title: "Quantum complexity of the Kronecker coefficients", authors: "S. Bravyi, A. Chowdhury, D. Gosset, V. Havlíček, G. Zhu", year: 2023, note: "PRX Quantum 5, 010329 (2024)"}
  - {arxiv: "2407.17649", title: "Quantum Algorithms for Representation-Theoretic Multiplicities", authors: "M. Larocca, V. Havlíček", year: 2024}
  - {arxiv: "2502.20253", title: "Polynomial time classical versus quantum algorithms for representation theoretic multiplicities", authors: "G. Panova", year: 2025}
  - {arxiv: "2602.08441", title: "Plethysm is in #BQP", authors: "M. Christandl, A. W. Harrow, G. Panova, P. M. Posta, M. Walter", year: 2026, note: "CCC 2026"}
---

## Best classical

The Kronecker coefficient g(λ, μ, ν) is the multiplicity of the irreducible representation of the symmetric group S_n labelled by ν in the tensor product of those labelled by λ and μ. Computing it exactly is #P-hard, and even deciding positivity is not known to be in NP; the absence of a combinatorial formula has been open since Murnaghan in 1938 and became a bottleneck for geometric complexity theory's approach to VP versus VNP. Littlewood–Richardson coefficients, by contrast, have a combinatorial rule and positivity is in P; plethysm coefficients sit in between.

Panova's 2025 result is the decisive classical fact: for the normalised quantity that the quantum algorithm estimates, the Kronecker coefficient divided by the appropriate dimension factor with additive error 1/poly, there is a classical polynomial-time algorithm, using character theory and the structure of the symmetric group rather than any quantum ingredient [3]. The paper explicitly refutes the speedup conjecture of Larocca and Havlíček for this setting.

## Best quantum

Bravyi, Chowdhury, Gosset, Havlíček and Zhu showed that Kronecker coefficients can be written as dimensions of eigenspaces of a Hamiltonian built from the quantum Fourier transform over S_n, so that the normalised coefficient is estimable to additive error in BQP, exact computation lies in #BQP, and positivity lies in QMA; they conjectured this was a task with no efficient classical algorithm [1]. Larocca and Havlíček generalised the construction to multiplicities of arbitrary group representations, including plethysm and higher tensor products [2]. Christandl, Harrow, Panova, Posta and Walter subsequently placed plethysm coefficients in #BQP [4]. All of these are correct as complexity-class memberships; none now implies a speedup, because the estimated quantity has a classical algorithm [3].

## What survives

Two questions remain open and are listed in this repository's open-theory survey: whether some family of multiplicities (plethysm, or GL_n tensor products in the normalised sense) escapes Panova's argument, which relies on symmetric-group structure; and whether positivity of Kronecker coefficients lies in NP, which would be a result about QMA versus NP and not about speedup. There is also a mismatch of demand: additive approximation of a normalised coefficient, which is exponentially small in the interesting cases, is not what an algebraic combinatorialist wants; they want exact values, positivity, or a formula.

## Verdict

No-go. The one quantity the quantum algorithm computes is now classically polynomial [3]; exact values are #P-hard for everyone; and the intended users do not need additive approximations. The page would reopen if a multiplicity family were shown to be BQP-hard or DQC1-hard to approximate in the normalised sense, with Panova's technique provably failing on it.
