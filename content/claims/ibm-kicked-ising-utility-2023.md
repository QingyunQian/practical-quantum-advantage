---
type: claim
id: ibm-kicked-ising-utility-2023
title: IBM 127-qubit kicked-Ising "utility" experiment
title_zh: IBM 127 比特 kicked-Ising “utility” 实验
summary: IBM ran kicked-Ising dynamics on the 127-qubit Eagle processor with zero-noise extrapolation and argued the results were beyond brute-force classical simulation. Within weeks, belief-propagation tensor networks and sparse Pauli dynamics reproduced every reported observable on a laptop.
summary_zh: IBM 在 127 比特 Eagle 上跑 kicked-Ising 动力学并用零噪声外推，宣称超出暴力经典模拟。几周内，信念传播张量网络和稀疏 Pauli 动力学在笔记本上复现了全部可观测量。
status: reviewed
last_verified: 2026-09-26
claim:
  claimant: IBM Quantum
  date: 2023-06
  statement: "Evidence for the utility of quantum computing before fault tolerance: error-mitigated expectation values on 127 qubits at depths where exact classical methods fail."
  hardware: Eagle r3 (superconducting)
  qubits: 127
  refuted: true
  refutation_date: 2023-08
  refuted_by: "Tindall et al. (belief-propagation tensor network, laptop, minutes); Begušić, Gray, Chan (sparse Pauli dynamics, single core)"
  time_to_refute: "weeks"
related:
  problems: [quench-dynamics]
  methods: [error-mitigation]
references:
  - {doi: "10.1038/s41586-023-06096-3", title: "Evidence for the utility of quantum computing before fault tolerance", authors: "Y. Kim et al.", year: 2023}
  - {arxiv: "2306.14887", title: "Efficient tensor network simulation of IBM's Eagle kicked Ising experiment", authors: "J. Tindall, M. Fishman, E. M. Stoudenmire, D. Sels", year: 2024}
  - {arxiv: "2308.05077", title: "Fast and converged classical simulations of evidence for the utility of quantum computing before fault tolerance", authors: "T. Begušić, J. Gray, G. K.-L. Chan", year: 2024}
  - {arxiv: "2407.12768", title: "A polynomial-time classical algorithm for noisy quantum circuits", authors: "T. Schuster, C. Yin, X. Gao, N. Y. Yao", year: 2025}
---

## Claim

Kim et al. ran Trotterized kicked-Ising dynamics on the heavy-hex lattice of the 127-qubit Eagle processor, up to 60 layers of two-qubit gates, and used zero-noise extrapolation to report local magnetisations and correlators. They compared against MPS and isoTNS simulations that failed to converge at the deepest circuits, and framed the result as evidence of "utility" before fault tolerance [1].

## Refutation

- Tindall, Fishman, Stoudenmire and Sels used a belief-propagation tensor network that exploits the heavy-hex graph's low connectivity, reproducing all reported observables on a laptop in minutes and extending to depths beyond the experiment [2].
- Begušić, Gray and Chan reproduced the results with sparse Pauli dynamics on a single core [3].
- The general lesson followed in 2024: Schuster et al. proved that for circuits with local depolarising noise, all observables can be computed classically in polynomial time [4]. Error-mitigated experiments on noisy hardware therefore cannot, as a class, establish advantage.

## Lesson for the catalogue

Comparing against one classical method (MPS with modest bond dimension) is not evidence of hardness. The claim page standard here is: classical hardness must survive the best method for the graph, not the most familiar one.
