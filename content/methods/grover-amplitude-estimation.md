---
type: method
id: grover-amplitude-estimation
title: Grover search and quantum amplitude estimation
title_zh: Grover 搜索与量子振幅估计
summary: Grover search has optimal quadratic query scaling for unstructured black-box search; amplitude estimation gives a near-quadratic query gain over plain Monte Carlo. End-to-end advantage depends on the reversible oracle, classical alternatives and fault-tolerant scheduling. The published derivative-pricing example needs 8,000 logical qubits and 54 million sequential T layers; its assumed one-second target would imply 54 MHz, despite the paper's separate 10 MHz statement.
summary_zh: Grover 搜索对无结构黑盒搜索有最优的二次查询加速；振幅估计相对普通蒙特卡洛有接近二次的查询次数改善。端到端优势还取决于可逆电路、经典替代方法和容错调度。已发表的衍生品定价实例需 8,000 个逻辑比特及 5,400 万层串行 T 门；假设一秒内完成，对应 5,400 万层每秒，尽管论文正文另写 1,000 万。
status: seed
last_verified: 2026-09-26
verdict: uneconomic
dimensions:
  classical_hardness: {level: none, note: "the classical competitor is whatever heuristic the application already uses; Grover gives √N over brute force, not over simulated annealing or branch-and-bound"}
  quantum_easiness: {level: proven, note: "Θ(√N) queries is tight (BBBV); amplitude estimation gives 1/ε instead of 1/ε² samples; but the query oracle must be compiled to a fault-tolerant circuit"}
  willingness_to_pay: {level: second-hand, note: "Goldman Sachs / IBM co-authored the derivative-pricing resource estimate but state a threshold, not a purchase"}
resources: {logical_qubits: "8,000 in 2021 autocallable example; 4,700 in later QSP study", gates: "T-depth 5.4e7 and 4.5e7 respectively, at different error settings", note: "at an assumed one-second target the layer rates are 54 and 45 MHz; 2021 text says 10 MHz contrary to its depth table. Babbush et al. give a separate Toffoli-time scenario, not a T-layer clock for these circuits"}
related:
  problems: [monte-carlo-expectation, combinatorial-optimization]
  applications: [derivative-pricing]
  methods: [dqi, qram]
  questions: [autocallable-same-instance-cost-crossover]
references:
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103"}
  - {arxiv: "2012.03819", title: "A Threshold for Quantum Advantage in Derivative Pricing", authors: "S. Chakrabarti et al.", year: 2021, note: "Quantum 5, 463; Table 1 depth 5.4e7 for autocallable, text quotes 10 MHz for one-second target"}
  - {arxiv: "2307.14310", title: "Derivative Pricing using Quantum Signal Processing", authors: "N. Stamatopoulos, W. J. Zeng", year: 2024, note: "Quantum 8, 1322"}
  - {arxiv: "2406.19378", title: "Quartic quantum speedups for planted inference", authors: "A. Schmidhuber, R. O'Donnell, R. Kothari, R. Babbush", year: 2025, note: "Phys. Rev. X 15, 021077"}
  - {arxiv: "2508.09422", title: "A Classical Quadratic Speedup for Planted $k$XOR", authors: "M. Gupta, Y. He, R. O'Donnell, N. Singer", year: 2025}
  - {arxiv: "2510.19928", title: "Mind the gaps: The fraught road to quantum advantage", authors: "J. Eisert, J. Preskill", year: 2025}
---

## How it works

Grover's algorithm finds a marked item among N with Θ(√N) oracle queries; Bennett, Bernstein, Brassard and Vazirani proved this is optimal for *unstructured black-box search*. Amplitude estimation can estimate a bounded expectation to precision ε with O(1/ε) coherent queries versus O(1/ε²) independent classical samples. Other structured search and quantum-walk algorithms have their own guarantees and are not covered by that black-box lower bound. In each case, the model and payoff or constraint checker must be implemented as a reversible circuit.

## Preconditions

1. The classical baseline must be brute-force enumeration or plain Monte Carlo; if the application already uses a structured heuristic (simulated annealing, branch-and-bound, importance sampling, quasi-Monte Carlo) the quantum speedup is measured against that instead.
2. The oracle (payoff function, constraint checker, model evaluation) must compile to a fault-tolerant circuit with an acceptable total cost. The quantum-to-classical cost ratio depends on the instance and architecture; one 2021 surface-code model [1] illustrates a large gap, not a universal factor.
3. The run must be long enough for the √ to overcome the constant factors. This is the precondition that decides everything.

## Known limits

- **The break-even arithmetic is conditional.** Babbush et al. model a distance-30 surface code at a 1 μs cycle and estimate about 170 μs per logical Toffoli [1]. Their favourable *100-Toffoli quantum primitive* therefore takes 17 ms, against a 33 ns classical primitive. This gives 5.2×10⁵ quantum steps and 2.4 hours to cross one classical core in their quadratic model. A separate compiled simulated-annealing example gives 6.3×10⁷ steps and 320 days. At a classical parallel speedup factor of 10³, their Table 1 gives 100 days and 880 years. The model illustrates why constants and parallelism matter; it is not a theorem that every quadratic quantum algorithm has these runtimes.
- **Derivative pricing remains open at equal task and cost.** The 2021 autocallable estimate has 8,000 logical qubits and T-depth 5.4×10⁷ [2]. Dividing by the assumed one-second comparator gives 54 MHz; the same paper's prose says 10 MHz. A 2024 QSP study [3] gives 4,700 qubits and T-depth 4.5×10⁷ under a different target error, implying 45 MHz at one second. Its headline 16-fold T-count and fourfold qubit improvements compare specific *oracle* implementations within that study, not the two end-to-end estimates at equal precision. A logical Toffoli duration from [1] cannot be equated directly with a T-layer clock without compiling and scheduling both on one architecture.
- **The quartic escape hatch is closing.** The planted noisy kXOR speedup of Schmidhuber et al. [4] was the one natural super-quadratic case; Gupta, He, O'Donnell and Singer found a classical quadratic speedup that reduces it to quadratic for large k [5].
- **No lower bound helps.** Θ(√N) is a bound on the quantum side; it says nothing about the classical side of any structured instance.

## Verdict

Uneconomic for the published derivative-pricing circuits under their assumed one-second comparator, and difficult for the two break-even examples in [1]. The asymptotic query improvements remain valid. A broader practical claim requires a specified task, equal accuracy, an optimized classical cost curve, a compiled reversible oracle and a fault-tolerant schedule. One finance estimate cannot determine the verdict for every search, risk or sampling application.
