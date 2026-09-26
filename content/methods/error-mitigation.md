---
type: method
id: error-mitigation
title: Error mitigation on noisy circuits (ZNE, PEC, post-selection)
title_zh: 含噪电路上的误差缓解（零噪声外推、概率误差消除、后选择）
summary: Run a noisy circuit at several noise strengths or with inverted noise channels and extrapolate the observable to zero noise. The 2023 IBM "utility" experiment used it. Two results close the route. Mitigation overhead grows exponentially with depth, and under constant local depolarising noise any observable of a random circuit can be estimated classically in polynomial time (Schuster, Yin, Gao, Yao). Useful engineering for hardware demonstrations; no-go as a path to advantage.
summary_zh: 在几个噪声强度下运行含噪电路或反转噪声通道，再把可观测量外推到零噪声。IBM 2023 年的“实用性”实验用的就是它。两条结果关上了这条路：缓解开销随深度指数增长；在常数局域退极化噪声下，随机电路的任何可观测量都能经典多项式时间估计（Schuster、Yin、Gao、Yao）。它是硬件演示的有用工程手段，作为通向优势的路线则没戏。
status: seed
last_verified: 2026-09-26
verdict: no-go
dimensions:
  classical_hardness: {level: none, note: "polynomial-time classical algorithm for observables of noisy random circuits at constant local noise (effective depth O(log n)); the flagship mitigated experiment was reproduced on a laptop"}
  quantum_easiness: {level: no, note: "sampling overhead of mitigation grows exponentially with circuit depth and qubit number; the regime where it is affordable is the regime that is classically simulable"}
  willingness_to_pay: {level: none, note: "no buyer for a mitigated observable as such; buyers want the application-level answer"}
related:
  problems: [quench-dynamics]
  methods: [sqd, vqe]
  claims: [ibm-kicked-ising-utility-2023, qctrl-fermi-hubbard-2026]
references:
  - {arxiv: "2407.12768", title: "A polynomial-time classical algorithm for noisy quantum circuits", authors: "T. Schuster, C. Yin, X. Gao, N. Y. Yao", year: 2025, note: "Phys. Rev. X 15, 041018"}
  - {arxiv: "2210.11505", title: "Exponentially tighter bounds on limitations of quantum error mitigation", authors: "Y. Quek, D. Stilck França, S. Khatri, J. J. Meyer, J. Eisert", year: 2024}
  - {arxiv: "2409.01706", title: "Classically estimating observables of noiseless quantum circuits", authors: "A. Angrisani et al.", year: 2025, note: "Phys. Rev. Lett. 135, 170602"}
  - {arxiv: "2306.14887", title: "Efficient tensor network simulation of IBM's Eagle kicked Ising experiment", authors: "J. Tindall, M. Fishman, E. M. Stoudenmire, D. Sels", year: 2024, note: "PRX Quantum 5, 010308"}
  - {arxiv: "2308.05077", title: "Fast and converged classical simulations of evidence for the utility of quantum computing before fault tolerance", authors: "T. Begušić, J. Gray, G. K.-L. Chan", year: 2024, note: "Sci. Adv. 10, eadk4321"}
  - {arxiv: "2510.19928", title: "Mind the gaps: The fraught road to quantum advantage", authors: "J. Eisert, J. Preskill", year: 2025}
---

## How it works

Error mitigation does not correct errors; it estimates what a noiseless circuit would have output by combining many noisy runs. Zero-noise extrapolation (ZNE) runs the same circuit at amplified noise levels and fits a curve back to zero. Probabilistic error cancellation (PEC) samples circuits drawn from a quasi-probability decomposition of the inverse noise channel. Symmetry verification and post-selection discard runs that violate a conserved quantity. All of these multiply the number of shots needed to reach a fixed statistical error; none of them extend the coherent depth of the device.

The flagship use was IBM's 127-qubit kicked-Ising experiment (Kim et al., Nature 618, 500, 2023): ZNE on up to 20 Trotter steps of a heavy-hexagon transverse-field Ising model, presented as evidence of "utility before fault tolerance".

## Preconditions

1. The noise model must be learnable and stable over the run (PEC) or the observable's noise dependence must be smooth enough to extrapolate (ZNE).
2. The mitigation overhead, which is a multiplicative factor on shot count, must stay affordable: for PEC it is γ^(2L) for L noisy layers with γ > 1 per layer.
3. The mitigated circuit must sit in a regime where the noiseless observable is classically hard to estimate. This is the precondition that fails.

## Known limits

- **Exponential overhead is not an artefact of a particular scheme.** Quek et al. prove that for local depolarising noise at constant rate, any mitigation protocol needs a number of samples growing exponentially in circuit depth (and, for sufficiently deep circuits, in qubit number) to reach constant precision, with bounds exponentially tighter than earlier work [2].
- **The affordable regime is classically simulable.** Schuster, Yin, Gao and Yao show that under constant-rate local noise, without any anticoncentration assumption, any observable of a random circuit on any geometry can be estimated classically in polynomial time; the noise makes the effective light-cone depth O(log n) [1]. Angrisani et al. extend the observation to noiseless local-random circuits in the average case, numerically up to 127 qubits [3]. Together with the overhead bound, this closes the window: a circuit shallow enough to mitigate is shallow enough to simulate, on average.
- **The flagship was reproduced.** Tindall et al. matched or beat the mitigated IBM values with belief-propagation tensor networks at bond dimension ≈ 500 in minutes on a laptop [4]; Begušić, Gray and Chan did the same with sparse Pauli dynamics in seconds to minutes on a single core [5]. Eisert and Preskill's 2025 assessment concludes that no NISQ demonstration has produced an end-to-end runtime advantage [6].
- **Caveat on the theorems.** The classical algorithms are average-case over random circuits, at constant precision, with polynomial constants that can be large. Structured circuits, atypical inputs, or inverse-polynomial precision are not covered. Google's 2025 OTOC experiment (65 qubits, mitigated) has not been reproduced as of September 2026; it sits in this gap, without a hardness theorem.

## Verdict

No-go as a route to advantage. Mitigation is a legitimate tool for extracting cleaner numbers from a fixed device and will remain part of hardware benchmarking, but the combination of exponential shot overhead and the polynomial-time classical algorithm for noisy circuits means it cannot be the mechanism by which a quantum computer outperforms a classical one at scale. Evidence that would reopen the question: a mitigated experiment at inverse-polynomial precision on a structured (non-random) circuit family with a hardness argument, reproduced by an independent group and not matched by tensor-network or Pauli-propagation methods after a year.
