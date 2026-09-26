---
type: problem
id: monte-carlo-expectation
title: Monte Carlo expectation values and sampling
title_zh: 蒙特卡洛期望值与采样
summary: For bounded-variance expectation estimation, amplitude estimation offers a near-quadratic query improvement over plain Monte Carlo, provided a coherent sampler and payoff oracle can be built. Runtime depends on that oracle and the classical competitor. Published derivative-pricing circuits need thousands of logical qubits and tens of millions of T layers; their quoted one-second comparison is an assumption, and the 2021 paper's 10 MHz statement conflicts with its own depth table.
summary_zh: 对有界方差的期望值估计，若能构造相干采样及收益函数电路，振幅估计相对普通蒙特卡洛有接近二次的查询次数改善。实际时间取决于电路和经典对照。已发表的衍生品定价电路需要数千逻辑比特、数千万层 T 门；其一秒对照属于论文假设，而且 2021 年论文的 1,000 万层每秒说法与本身的深度表格不符。
status: seed
last_verified: 2026-09-26
verdict: uneconomic
dimensions:
  classical_hardness: {level: none, note: "Monte Carlo is embarrassingly parallel; quasi-Monte Carlo and variance reduction often beat the 1/ε² baseline in practice; tensor-network and parallel-tempering samplers are the real classical competitors for MCMC"}
  quantum_easiness: {level: proven, note: "amplitude estimation gives O(1/ε) with a bounded-variance oracle (Montanaro); the oracle, i.e. the model evaluation in quantum arithmetic, is the entire cost"}
  willingness_to_pay: {level: second-hand, note: "Goldman Sachs co-authored the pricing estimates; a one-second classical comparator is assumed, while a desk-defined purchase threshold is not documented"}
resources: {logical_qubits: "8,000 in one derivative-pricing benchmark; 4,700 in later QSP study", gates: "autocallable T-depth 5.4e7 (2021) or 4.5e7 (later QSP, different error settings)", note: "at an assumed one-second runtime, the respective T-layer rates are 54 and 45 MHz; 2021 text also says 10 MHz, contrary to its table"}
related:
  applications: [derivative-pricing, weather-forecasting, turbulence-cfd]
  problems: [combinatorial-optimization, pde-solving, sorting-fft-storage]
  methods: [grover-amplitude-estimation, qram]
  questions: [autocallable-same-instance-cost-crossover]
references:
  - {arxiv: "1504.06987", title: "Quantum speedup of Monte Carlo methods", authors: "A. Montanaro", year: 2015, note: "Proc. R. Soc. A 471, 20150301; near-quadratic speedup for bounded-variance expectations and partition functions"}
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103; break-even iteration counts and runtimes"}
  - {arxiv: "2012.03819", title: "A Threshold for Quantum Advantage in Derivative Pricing", authors: "S. Chakrabarti, R. Krishnakumar, G. Mazzola, N. Stamatopoulos, S. Woerner, W. J. Zeng", year: 2021, note: "Quantum 5, 463"}
  - {arxiv: "2307.14310", title: "Derivative Pricing using Quantum Signal Processing", authors: "N. Stamatopoulos, W. J. Zeng", year: 2024, note: "Quantum 8, 1322; 4.7k logical qubits, 2.4e9 total T gates, 4.5e7 T-depth"}
  - {arxiv: "2203.12497", title: "Quantum-enhanced Markov chain Monte Carlo", authors: "D. Layden, G. Mazzola, R. V. Mishmash, M. Motta, P. Wocjan, S. Sheldon", year: 2023, note: "Nature 619, 282; empirical polynomial gain in mixing on small spin glasses"}
  - {arxiv: "2403.03087", title: "Bounding speedup of quantum-enhanced Markov chain Monte Carlo", authors: "A. Orfi, D. Sels", year: 2024, note: "Phys. Rev. A 110, 052414; Markov-gap upper bound, no worst-case speedup for any unital proposal"}
  - {arxiv: "2510.19928", title: "Mind the gaps: The fraught road to quantum advantage", authors: "J. Eisert, J. Preskill", year: 2025, note: "assessment of the time horizon for quadratic speedups"}
---

## Best classical

Plain Monte Carlo reaches error ε in O(σ²/ε²) samples, and the samples are independent, so the work parallelises perfectly across cores and GPUs. Quasi-Monte Carlo, control variates, importance sampling and multilevel schemes routinely beat the 1/ε² baseline for smooth integrands. For sampling from Boltzmann distributions the practical competitors are not naive Metropolis but parallel tempering, cluster updates and, since 2025, tensor-network and belief-propagation samplers that have reproduced hardware "beyond-classical" sampling claims. The classical side is not obstructed; it is merely large.

## Best quantum

Montanaro's algorithm estimates the expected output of any randomised or quantum subroutine with bounded variance to error ε using O(1/ε) calls, a near-quadratic speedup over the classical sample complexity, and extends to partition functions via quantum walks [1]. The construction is proven and general. Its cost is the oracle: the model (a stochastic path, a risk factor simulation, a likelihood) must be evaluated in quantum arithmetic inside a coherent circuit, and the O(1/ε) calls are sequential.

The break-even arithmetic of Babbush and colleagues [2] uses a distance-30 surface code with 1 μs cycles, yielding about 170 μs per logical Toffoli in their model. Their *illustrative quantum primitive* contains 100 Toffolis, so one quantum step takes 17 ms; they assign its classical counterpart 33 ns. With those assumptions a quadratic speedup crosses one classical core after 5.2×10⁵ quantum steps and 2.4 hours. A separately compiled simulated-annealing example needs 6.3×10⁷ steps and 320 days. Their Table 1 gives 100 days and 880 years respectively when the classical speedup factor is 10³. These are scenario calculations, not universal lower bounds for expectation estimation. More parallel classical capacity worsens this comparison, while faster quantum gates or a cheaper oracle can improve it.

For a basket autocallable, Chakrabarti and colleagues estimate 8,000 logical qubits and T-depth 54 million at a target error of 2×10⁻³ [3]. Dividing that depth by their assumed one-second runtime gives 54 MHz, although the same paper's discussion states 10 MHz. The later QSP calculation [4] gives 4,700 logical qubits, T-depth 45 million and T-count 2.4 billion for an autocallable with a different error specification. At a one-second comparator its required T-layer rate is 45 MHz. Neither paper supplies a bank's written procurement target or a measured best-classical runtime for exactly the compiled payoff at identical accuracy. Other finance or reliability tasks need their own oracle and baseline rather than inheriting these numbers.

For sampling rather than expectation, Layden et al.'s quantum-enhanced MCMC uses a quantum device to propose moves and reports an empirical polynomial gain in mixing on small spin-glass instances [5]. Orfi and Sels give an upper bound on the Markov gap for any unital quantum proposal and show there is no speedup over classical sampling on a worst-case unstructured problem [6]. Quantum walks give at most a quadratic gain in spectral gap (Szegedy). There is no provable super-quadratic quantum speedup for sampling from a classical distribution.

## Verdict

Uneconomic for the compiled finance examples under their one-second benchmark assumption. The query speedup itself is real, but a broad verdict for all Monte Carlo problems would require matched instance-level costs. A favourable candidate would need an efficiently reversible oracle, a documented classical bottleneck after variance reduction and parallelism, and a buyer-valued output at a tolerable quantum runtime.
