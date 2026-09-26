---
type: method
id: dqi
title: Decoded quantum interferometry (DQI)
title_zh: 解码量子干涉（DQI）
summary: Maps a max-LINSAT objective through a Fourier transform onto a decoding problem for the dual code, and reaches a "semicircle-law" fraction of satisfied constraints whenever that code has an efficient decoder. For optimal polynomial intersection (Reed–Solomon dual) no classical polynomial-time algorithm matches it, making DQI the first new candidate super-polynomial speedup family since Shor. It requires a decodable dual code; on unstructured or random-sparse instances spin-glass and overlap-gap arguments block it, and no industrial problem naturally carries the required structure.
summary_zh: 把 max-LINSAT 目标函数经傅里叶变换映射到对偶码的解码问题，只要对偶码有高效解码器就能达到“半圆律”比例的满足约束数。对最优多项式相交问题（对偶码为 Reed–Solomon）没有经典多项式算法能匹敌，使 DQI 成为 Shor 之后第一个新的超多项式加速候选家族。它要求对偶码可解码；对无结构或随机稀疏实例，自旋玻璃与 overlap gap 论证把它挡住，而且没有任何工业问题天然带有所需结构。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "OPI equals Reed–Solomon list recovery beyond the Guruswami–Sudan radius; no reduction to a standard assumption; best classical MCMC ~1.1^n; immune to relativizing dequantization (Marwaha et al.)"}
  quantum_easiness: {level: conditional, note: "polynomial time given an efficient decoder for the dual code B^T with decoding radius near m/2; nearly linear-time circuits exist for OPI"}
  willingness_to_pay: {level: none, note: "the only published industrial attempt (automotive option-package ILP, Sabater et al.) needs gadgets that inflate variables and collapse code distance, and does not claim to beat Gurobi"}
resources: {logical_qubits: "Õ(N) gates for OPI at size N", gates: "nearly linear in instance size (Rosmanis 2026)", note: "no fault-tolerant compilation of the Reed–Solomon decoder has been published"}
related:
  problems: [combinatorial-optimization]
  applications: [automotive-pricing-integer-programming, cryptanalysis]
  methods: [grover-amplitude-estimation]
references:
  - {arxiv: "2408.08292", title: "Optimization by Decoded Quantum Interferometry", authors: "S. P. Jordan, N. Shutty, M. Wootters, A. Zalcman, A. Schmidhuber, R. King, S. V. Isakov, R. Babbush", year: 2025, note: "Nature 646, 831"}
  - {arxiv: "2509.14509", title: "Spin Glass Transitions Obstruct Decoded Quantum Interferometry", authors: "E. R. Anschuetz, D. Gamarnik, B. Lu", year: 2025}
  - {arxiv: "2509.14443", title: "On the Complexity of Decoded Quantum Interferometry", authors: "K. Marwaha, B. Fefferman, A. Gheorghiu, V. Havlíček", year: 2025}
  - {arxiv: "2603.04540", title: "Tight inapproximability of max-LINSAT and implications for decoded quantum interferometry", authors: "M. J. Kramer, D. Schubert, J. Eisert", year: 2026}
  - {arxiv: "2604.09533", title: "On Worst-Case Optimal Polynomial Intersection", authors: "Y. Sun, M. Wootters", year: 2026}
  - {arxiv: "2601.15171", title: "A nearly linear-time Decoded Quantum Interferometry algorithm for the Optimal Polynomial Intersection problem", authors: "A. Rosmanis", year: 2026}
  - {arxiv: "2509.08328", title: "Towards solving industrial integer linear programs with Decoded Quantum Interferometry", authors: "F. Sabater et al.", year: 2026, note: "Quantum Sci. Technol. 11, 025054"}
---

## How it works

Max-LINSAT asks, for a matrix B ∈ F_p^{m×n} and subsets F_i ⊂ F_p, for an x maximising the number of rows i with (Bx)_i ∈ F_i. DQI prepares a superposition weighted by a polynomial in the objective, whose Fourier transform is a superposition over low-weight error patterns; decoding the dual code C^⊥ = ker B^T coherently uncomputes the error register and leaves a state concentrated on good x [1]. With a decoder of radius ℓ, the expected satisfied fraction follows the semicircle law ⟨s⟩/m = (√[(ℓ/m)(1 − r/p)] + √[(r/p)(1 − ℓ/m)])², where r = |F_i|. The flagship instance is optimal polynomial intersection (OPI): B is a Vandermonde matrix, the dual code is Reed–Solomon, Berlekamp–Massey decodes up to ℓ = ⌊(m − n)/2⌋, and at rate n/p ≈ 1/10 DQI reaches a fraction 0.7179 against 0.55 for the best classical algorithm the authors tried (Prange). Rosmanis gives a nearly linear-time circuit for OPI [6].

## Preconditions

1. **A decodable dual code.** B^T must generate a code with an efficient decoder; the advantage grows with the decoding radius, which must approach m/2 for a large gap.
2. **Instances that are not random-local.** The structure must come from algebra (Reed–Solomon, algebraic-geometry codes), not from a random sparse constraint graph.
3. **Classical hardness of the same instances.** For OPI this is the conjecture that Reed–Solomon list recovery with p/2 candidates per point is hard; there is no reduction to a standard assumption.

## Known limits

- **Unstructured instances are blocked.** Anschuetz, Gamarnik and Lu show that on random LDPC-type max-k-XOR-SAT the overlap-gap property obstructs DQI: the spin-glass transition prevents it from beating classical local algorithms asymptotically [2]. Kramer, Schubert and Eisert prove that beating the trivial r/q fraction on general max-LINSAT by a constant is NP-hard, so any advantage must come from structure [4].
- **Complexity status is intermediate.** Marwaha et al. show the DQI output distribution can be sampled in low levels of the polynomial hierarchy, so sampling-hardness arguments of the RCS type do not apply, while the task of finding high-value outputs resists relativizing dequantization [3].
- **The hard parameter region is shrinking from the top.** Sun and Wootters show that for prime-field OPI at rate n/m ≥ 0.6225 solutions beating the semicircle law exist, and at ≥ 0.7496 nearly perfect ones [5]; follow-up quantum algorithms exploit this, but classically it is an existence result. The region still believed hard is prime field, |F_i| ≈ p/2, rate 0.1–0.6, large p. Classical block-Gibbs MCMC approximates the DQI distribution at cost ~1.1ⁿ.
- **No industrial instance carries the structure.** The one published attempt, option-package pricing as an integer linear program (Sabater et al.), converts ILP to pseudo-Boolean to max-XORSAT through gadgets that inflate the variable count and can drop the code distance to 2, which kills decodability; BP decoding success falls quickly with error weight, the worked circuit is m = 3, n = 2, and no advantage over Gurobi is claimed [7]. Code-based cryptography (HQC, BIKE) is not threatened because those schemes use random codes without decoders. Noisy polynomial interpolation, the cryptographic cousin of OPI, underlies protocols that were abandoned years ago.

## Verdict

Surviving. DQI is the most important new algorithmic idea since 2024 and the one optimisation method in this catalogue with no known classical match on its natural instances. But quantum easiness holds only for algebraically structured objectives, hardness is a conjecture rather than a reduction, and the willingness-to-pay column is empty: every optimisation problem a company has asked about lacks a decodable dual code. What would change the verdict: either a sub-exponential classical algorithm for balanced-region OPI (which would kill it) or an industrial or cryptanalytic problem that reduces to OPI without gadgets (which would move it to promising).
