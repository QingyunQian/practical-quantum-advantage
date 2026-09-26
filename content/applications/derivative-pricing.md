---
type: application
id: derivative-pricing
title: Derivative pricing by quantum amplitude estimation
title_zh: 衍生品定价（量子振幅估计）
summary: Banks price exotic derivatives by Monte Carlo and would pay for the same accuracy faster. Amplitude estimation offers a quadratic speedup, and Goldman Sachs and IBM published the resource threshold, about 8,000 logical qubits and T-depth 5.4e7 executed in about one second, i.e. a 10 MHz logical clock. Realistic fault-tolerant clocks are of order kilohertz, so the case is uneconomic by three orders of magnitude.
summary_zh: 银行用蒙特卡洛给奇异衍生品定价，愿意为同样精度下更快的结果付费。振幅估计给出二次加速，高盛与 IBM 发表了对应的资源门槛：约 8 千逻辑比特、T 深度 5.4×10⁷，要在约 1 秒内跑完，即 10 MHz 的逻辑时钟。现实的容错时钟在千赫兹量级，差三个数量级，不划算。
status: seed
last_verified: 2026-09-26
verdict: uneconomic
dimensions:
  classical_hardness: {level: none, note: "Monte Carlo with 1/ε² samples is embarrassingly parallel on GPUs; low-dimensional contracts are solved by PDE methods faster still"}
  quantum_easiness: {level: proven, note: "amplitude estimation gives 1/ε given a payoff oracle; the oracle (path generation plus payoff arithmetic) is the whole cost"}
  willingness_to_pay: {level: first-hand, note: "Goldman Sachs co-authored the threshold paper and states that advantage requires execution in about one second (Chakrabarti et al.)"}
resources: {logical_qubits: "~8,000 (4,700 with QSP payoff loading)", gates: "T-depth 5.4e7; ~1e9 T gates", note: "autocallable and TARF benchmarks; needs a ~10 MHz T-gate rate (45 MHz in the QSP variant) against ~6 kHz for a logical Toffoli at ~170 μs"}
related:
  problems: [monte-carlo-expectation, pde-solving]
  methods: [grover-amplitude-estimation]
  questions: [first-hand-payment-evidence]
references:
  - {arxiv: "2012.03819", title: "A Threshold for Quantum Advantage in Derivative Pricing", authors: "S. Chakrabarti, R. Krishnakumar, G. Mazzola, N. Stamatopoulos, S. Woerner, W. J. Zeng (Goldman Sachs, IBM)", year: 2021, note: "Quantum 5, 463; 8k logical qubits, T-depth 54 million, execution in ~1 s"}
  - {arxiv: "2307.14310", title: "Derivative Pricing using Quantum Signal Processing", authors: "N. Stamatopoulos, W. J. Zeng", year: 2024, note: "Quantum 8, 1322; 4.7k logical qubits, 1e9 T gates at 45 MHz"}
  - {arxiv: "1905.02666", title: "Option Pricing using Quantum Computers", authors: "N. Stamatopoulos, D. J. Egger, Y. Sun, C. Zoufal, R. Iten, N. Shen, S. Woerner", year: 2020, note: "Quantum 4, 291; the amplitude-estimation pricing construction"}
  - {arxiv: "1504.06987", title: "Quantum speedup of Monte Carlo methods", authors: "A. Montanaro", year: 2015, note: "Proc. R. Soc. A 471, 20150301; the general near-quadratic bound"}
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103; logical Toffoli ~170 μs at code distance ~30"}
---

## Who needs it

Investment banks and market makers (Goldman Sachs and JPMorgan have published on it; IBM and Quantinuum have partnered with banks). The products are path-dependent exotics: autocallables, target accrual redemption forwards (TARFs), barrier and Asian options. Pricing and risk desks re-value books overnight and intraday, and a desk that could reprice faster at the same accuracy would take the number.

## Bottleneck

The price is an expectation of a payoff over simulated paths of the underlying. Classical Monte Carlo reaches error ε with O(1/ε²) paths. This is slow in the sense that the number of paths is large, but the work is embarrassingly parallel and runs on GPU farms; for contracts on one to three underlyings the PDE route is faster still. The bottleneck is throughput at fixed accuracy, not tractability.

## Computational problems

- [Monte Carlo expectation](../problems/monte-carlo-expectation.html): the core task, quantum amplitude estimation giving O(1/ε) [4].
- [PDE solving](../problems/pde-solving.html): the alternative for low-dimensional contracts, where quantum methods offer at most polynomial gains.

## Best quantum

Stamatopoulos et al. gave the construction: encode the path distribution in amplitudes, compute the payoff in quantum arithmetic, and run amplitude estimation [3]. Chakrabarti et al. (Goldman Sachs and IBM) then did what almost no application study does: they estimated the full circuit for real benchmark contracts and stated the threshold at which it would matter. For autocallables and TARFs the program needs about 8,000 logical qubits and a T-depth of 54 million, and it has to finish in about one second to beat the classical desk [1]. That fixes the required logical clock at roughly 10 MHz on the T-gate critical path. Stamatopoulos and Zeng later moved the payoff into quantum signal processing, which cuts T gates by about 16× and qubits by about 4×, to 4,700 logical qubits and 1e9 T gates, but the required rate becomes 45 MHz because the target run time is unchanged [2].

## Why it does not pay

Babbush et al. put a logical Toffoli at about 170 μs on a surface code of distance about 30 with a 1 μs cycle, roughly 6 kHz [5]. Against a 10 MHz requirement that is a gap of three orders of magnitude, and the requirement is a rate on a serial critical path, so adding qubits does not close it. The 2024–26 improvements in magic-state cultivation, qLDPC codes and algorithmic fault tolerance together buy perhaps two to three orders of magnitude in gate cost, not in clock rate, and they benefit the depth count less than the volume count. Classical parallelism widens the gap further: the one-second target already assumes the bank's existing farm, and Monte Carlo scales linearly with added GPUs while amplitude estimation does not parallelise its O(1/ε) sequential oracle calls.

The same conclusion holds for the neighbouring finance tasks (credit risk, VaR, CVA), which inherit the quadratic bound and have no published estimate better than Chakrabarti's.

## Verdict

Uneconomic. This is the best-documented application in the catalogue on two of the three dimensions: the buyer has spoken first-hand and the quantum algorithm is proven. It fails on the third, classical hardness, because the speedup is only quadratic and the buyer's own threshold requires a logical clock about 1,000× faster than error-corrected hardware provides. The verdict would change if a fault-tolerant architecture demonstrated a sustained ~10 MHz T-gate rate on a serial path, or if a contract class were found for which the classical cost is not parallelisable.
