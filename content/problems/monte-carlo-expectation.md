---
type: problem
id: monte-carlo-expectation
title: Monte Carlo expectation values and sampling
title_zh: 蒙特卡洛期望值与采样
summary: Estimating an expectation to error ε costs O(1/ε²) classical samples; quantum amplitude estimation does it in O(1/ε) oracle calls, a proven quadratic speedup behind every finance, risk and Bayesian proposal. Under error-correction overheads a quadratic speedup breaks even only after about 5e5 sequential iterations (2.4 hours) in the most quantum-favourable case, 320 days against simulated annealing, and never once classical parallelism is allowed; quantum-enhanced MCMC has no worst-case gain.
summary_zh: 把期望值估到误差 ε 需要 O(1/ε²) 个经典样本，量子振幅估计只需 O(1/ε) 次 oracle 调用，这是金融、风险与贝叶斯提案背后已证明的二次加速。但在纠错开销下，二次加速在对量子最有利的情形也要约 5×10⁵ 次串行迭代（2.4 小时）才能持平，对模拟退火要 320 天，而一旦允许经典并行则永远追不上；量子增强 MCMC 在最坏情形下没有加速。
status: seed
last_verified: 2026-09-26
verdict: uneconomic
dimensions:
  classical_hardness: {level: none, note: "Monte Carlo is embarrassingly parallel; quasi-Monte Carlo and variance reduction often beat the 1/ε² baseline in practice; tensor-network and parallel-tempering samplers are the real classical competitors for MCMC"}
  quantum_easiness: {level: proven, note: "amplitude estimation gives O(1/ε) with a bounded-variance oracle (Montanaro); the oracle, i.e. the model evaluation in quantum arithmetic, is the entire cost"}
  willingness_to_pay: {level: first-hand, note: "Goldman Sachs co-authored the derivative-pricing threshold paper and states that advantage requires execution in about one second"}
resources: {logical_qubits: "~8,000 (derivative pricing benchmark)", gates: "T-depth 5.4e7", note: "Chakrabarti et al. 2021; needs a ~10 MHz logical clock against ~6 kHz for a 170 μs logical Toffoli"}
related:
  applications: [derivative-pricing, weather-forecasting, turbulence-cfd]
  problems: [combinatorial-optimization, pde-solving, sorting-fft-storage]
  methods: [grover-amplitude-estimation, qram]
references:
  - {arxiv: "1504.06987", title: "Quantum speedup of Monte Carlo methods", authors: "A. Montanaro", year: 2015, note: "Proc. R. Soc. A 471, 20150301; near-quadratic speedup for bounded-variance expectations and partition functions"}
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103; break-even iteration counts and runtimes"}
  - {arxiv: "2012.03819", title: "A Threshold for Quantum Advantage in Derivative Pricing", authors: "S. Chakrabarti, R. Krishnakumar, G. Mazzola, N. Stamatopoulos, S. Woerner, W. J. Zeng", year: 2021, note: "Quantum 5, 463"}
  - {arxiv: "2307.14310", title: "Derivative Pricing using Quantum Signal Processing", authors: "N. Stamatopoulos, W. J. Zeng", year: 2024, note: "Quantum 8, 1322; 4.7k logical qubits, 1e9 T gates at 45 MHz"}
  - {arxiv: "2203.12497", title: "Quantum-enhanced Markov chain Monte Carlo", authors: "D. Layden, G. Mazzola, R. V. Mishmash, M. Motta, P. Wocjan, S. Sheldon", year: 2023, note: "Nature 619, 282; empirical polynomial gain in mixing on small spin glasses"}
  - {arxiv: "2403.03087", title: "Bounding speedup of quantum-enhanced Markov chain Monte Carlo", authors: "A. Orfi, D. Sels", year: 2024, note: "Phys. Rev. A 110, 052414; Markov-gap upper bound, no worst-case speedup for any unital proposal"}
  - {arxiv: "2510.19928", title: "Mind the gaps: The fraught road to quantum advantage", authors: "J. Eisert, J. Preskill", year: 2025, note: "assessment of the time horizon for quadratic speedups"}
---

## Best classical

Plain Monte Carlo reaches error ε in O(σ²/ε²) samples, and the samples are independent, so the work parallelises perfectly across cores and GPUs. Quasi-Monte Carlo, control variates, importance sampling and multilevel schemes routinely beat the 1/ε² baseline for smooth integrands. For sampling from Boltzmann distributions the practical competitors are not naive Metropolis but parallel tempering, cluster updates and, since 2025, tensor-network and belief-propagation samplers that have reproduced hardware "beyond-classical" sampling claims. The classical side is not obstructed; it is merely large.

## Best quantum

Montanaro's algorithm estimates the expected output of any randomised or quantum subroutine with bounded variance to error ε using O(1/ε) calls, a near-quadratic speedup over the classical sample complexity, and extends to partition functions via quantum walks [1]. The construction is proven and general. Its cost is the oracle: the model (a stochastic path, a risk factor simulation, a likelihood) must be evaluated in quantum arithmetic inside a coherent circuit, and the O(1/ε) calls are sequential.

The break-even arithmetic is Babbush et al.'s [2]. With a surface code at distance about 30 and a 1 μs cycle, a logical Toffoli takes about 170 μs, against about 0.3 ns for a classical step. For a quadratic speedup to overtake a single classical core, the quantum computation must run at least about 5e5 Grover-type iterations, 2.4 hours of runtime, in the case most favourable to the quantum side; against a simulated-annealing competitor the figure is about 6e7 iterations, roughly 320 days. If the classical side may parallelise, the classical runtime at break-even exceeds 100 days. The 2024–26 improvements in magic-state cultivation, qLDPC codes and algorithmic fault tolerance together buy perhaps three orders of magnitude, which shifts "years" to "days" but does not reverse the conclusion; Eisert and Preskill's 2025 assessment puts practical quadratic advantage decades away [7].

The finance instance is where the arithmetic has been done concretely. Chakrabarti et al. (Goldman Sachs, IBM) find that pricing benchmark autocallables and TARFs by amplitude estimation needs about 8,000 logical qubits and a T-depth of 54 million, executed in about one second to matter, a logical clock of order 10 MHz [3]; Stamatopoulos and Zeng reduce this to 4,700 logical qubits and 1e9 T gates but at 45 MHz [4]. Credit risk, VaR and CVA inherit the same bound with no better estimate; structural reliability and catastrophe-insurance proposals add a table-lookup oracle that is QRAM in another name.

For sampling rather than expectation, Layden et al.'s quantum-enhanced MCMC uses a quantum device to propose moves and reports an empirical polynomial gain in mixing on small spin-glass instances [5]. Orfi and Sels give an upper bound on the Markov gap for any unital quantum proposal and show there is no speedup over classical sampling on a worst-case unstructured problem [6]. Quantum walks give at most a quadratic gain in spectral gap (Szegedy). There is no provable super-quadratic quantum speedup for sampling from a classical distribution.

## Verdict

Uneconomic. The speedup is proven, the buyer has spoken first-hand, and the classical task is not hard, only voluminous and perfectly parallel. A quadratic gain on a serial critical path against a parallel classical baseline does not pay under any error-correction technology on the horizon. The page would change only if a Monte Carlo task were found whose classical evaluation is inherently sequential and whose quantum oracle is cheap, or if fault-tolerant hardware reached the multi-megahertz logical clock the finance estimates require.
