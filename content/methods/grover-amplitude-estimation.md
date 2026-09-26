---
type: method
id: grover-amplitude-estimation
title: Grover search and quantum amplitude estimation
title_zh: Grover 搜索与量子振幅估计
summary: The quadratic-speedup family (unstructured search, backtracking, amplitude-estimation Monte Carlo for finance and risk). The speedup is provably at most quadratic (BBBV) and does not pay under error-correction overhead. Babbush et al. compare a 170 μs logical Toffoli with a 0.3 ns classical operation and find break-even at ≥ 5 × 10⁵ iterations (about 2.4 hours) in the best case and 6 × 10⁷ (about 320 days) against simulated annealing, with classical parallelism pushing break-even past 100 days. Derivative pricing needs ~8,000 logical qubits and a 10 MHz logical clock.
summary_zh: 二次加速家族：无结构搜索、回溯、金融与风险的振幅估计蒙特卡洛。加速可证最多二次（BBBV），在纠错开销下不划算。Babbush 等人用 170 微秒的逻辑 Toffoli 对比 0.3 纳秒的经典操作，最好情况收支平衡也要 5×10⁵ 次迭代（约 2.4 小时），对比模拟退火则要 6×10⁷ 次（约 320 天），加上经典并行后平衡点超过 100 天。衍生品定价需要约 8 千逻辑比特和 10 MHz 逻辑时钟。
status: seed
last_verified: 2026-09-26
verdict: uneconomic
dimensions:
  classical_hardness: {level: none, note: "the classical competitor is whatever heuristic the application already uses; Grover gives √N over brute force, not over simulated annealing or branch-and-bound"}
  quantum_easiness: {level: proven, note: "Θ(√N) queries is tight (BBBV); amplitude estimation gives 1/ε instead of 1/ε² samples; but the query oracle must be compiled to a fault-tolerant circuit"}
  willingness_to_pay: {level: second-hand, note: "Goldman Sachs / IBM co-authored the derivative-pricing resource estimate but state a threshold, not a purchase"}
resources: {logical_qubits: "~8,000 (derivative pricing, published version)", gates: "T-depth 5.4e7 at a required 10 MHz logical clock", note: "Chakrabarti et al. 2021, published version; Stamatopoulos–Zeng 2024 reduce T count ~16× and qubits ~4×; Babbush et al. assume surface code d=30, 1 μs cycle, Toffoli ≈ 170 μs"}
related:
  problems: [monte-carlo-expectation, combinatorial-optimization]
  applications: [derivative-pricing]
  methods: [dqi, qram]
references:
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103"}
  - {arxiv: "2012.03819", title: "A Threshold for Quantum Advantage in Derivative Pricing", authors: "S. Chakrabarti et al.", year: 2021, note: "Quantum 5, 463; published version: ~8k logical qubits, T-depth 5.4e7, 10 MHz"}
  - {arxiv: "2307.14310", title: "Derivative Pricing using Quantum Signal Processing", authors: "N. Stamatopoulos, W. J. Zeng", year: 2024, note: "Quantum 8, 1322"}
  - {arxiv: "2406.19378", title: "Quartic quantum speedups for planted inference", authors: "A. Schmidhuber, R. O'Donnell, R. Kothari, R. Babbush", year: 2025, note: "Phys. Rev. X 15, 021077"}
  - {arxiv: "2508.09422", title: "A Classical Quadratic Speedup for Planted $k$XOR", authors: "M. Gupta, Y. He, R. O'Donnell, N. Singer", year: 2025}
  - {arxiv: "2510.19928", title: "Mind the gaps: The fraught road to quantum advantage", authors: "J. Eisert, J. Preskill", year: 2025}
---

## How it works

Grover's algorithm finds a marked item among N with Θ(√N) oracle queries; Bennett, Bernstein, Brassard and Vazirani proved this is optimal for black-box search. Amplitude estimation applies the same rotation to estimate a probability p to precision ε in O(1/ε) queries instead of the O(1/ε²) samples of classical Monte Carlo. Everything in this family (backtracking for constraint satisfaction, quantum walks on graphs, Monte Carlo for option pricing, value-at-risk, Bayesian inference, rare-event estimation) inherits the same square-root and the same fine print: the oracle is a reversible circuit that must be run coherently inside the error-corrected computer.

## Preconditions

1. The classical baseline must be brute-force enumeration or plain Monte Carlo; if the application already uses a structured heuristic (simulated annealing, branch-and-bound, importance sampling, quasi-Monte Carlo) the quantum speedup is measured against that instead.
2. The oracle (payoff function, constraint checker, model evaluation) must compile to a fault-tolerant circuit whose cost per call is comparable to one classical evaluation. In practice it costs 10⁵–10⁶ times more in wall-clock.
3. The run must be long enough for the √ to overcome the constant factors. This is the precondition that decides everything.

## Known limits

- **The break-even arithmetic.** Babbush et al. assume a surface code at distance 30 with a 1 μs cycle, giving a logical Toffoli every ≈ 170 μs, against a classical primitive at ≈ 0.3 ns [1]. A quadratic speedup then breaks even only after M > 5.2 × 10⁵ iterations (≈ 2.4 hours of quantum runtime) in the most favourable comparison and M > 6.3 × 10⁷ (≈ 320 days) against simulated annealing; against a classical machine with thousands of cores the break-even stretches to years or more, exceeding 100 days in every case considered. A quartic speedup would break even in 1.4 seconds to 2.9 minutes, which is why the authors recommend focusing on at least quartic speedups. Improvements since 2021 (magic-state cultivation, qLDPC codes, algorithmic fault tolerance) plausibly gain 10²–10³ in total and move "years" to "days to hours"; that does not flip the verdict. Eisert and Preskill reach the same conclusion in 2025: quadratic speedups are decades away from usefulness [6].
- **Derivative pricing is the best-studied case and does not close.** Chakrabarti et al. (Goldman Sachs / IBM) estimate that a useful autocallable or TARF pricing needs about 8,000 logical qubits with T-depth 5.4 × 10⁷ and, to finish within a second, a 10 MHz logical clock [2]. A realistic clock from the Toffoli time above is about 6 kHz. Stamatopoulos and Zeng cut T count by ~16× and qubits by ~4× with quantum signal processing [3], leaving a gap of one to two orders of magnitude in clock rate before the qubit count is considered.
- **The quartic escape hatch is closing.** The planted noisy kXOR speedup of Schmidhuber et al. [4] was the one natural super-quadratic case; Gupta, He, O'Donnell and Singer found a classical quadratic speedup that reduces it to quadratic for large k [5].
- **No lower bound helps.** Θ(√N) is a bound on the quantum side; it says nothing about the classical side of any structured instance.

## Verdict

Uneconomic. The speedup is real and proven, but constant factors of 10⁵–10⁶ in operation time (and a further factor from the classical competitor's parallelism) put break-even at days to years of continuous quantum runtime on machines of 10⁶–10⁷ physical qubits. Every finance, risk and search use case in the catalogue inherits this. What would change it: a logical clock within a factor of ten of classical hardware, or an application where the quantum oracle is intrinsically cheap and the classical baseline is provably brute force.
