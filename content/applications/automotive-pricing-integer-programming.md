---
type: application
id: automotive-pricing-integer-programming
title: Vehicle option-package pricing as an integer program
title_zh: 汽车选装包定价的整数规划
summary: BMW and BCG studied an automotive pricing ILP through decoded quantum interferometry. The smallest relevant encoded example has 827 max-XORSAT constraints and 345 variables, already above a 100-qubit register; reported performance uses smaller sampled matrices. The constructed code has distance 3 independent of size, and the better BP2 decoder was not compiled into a quantum circuit. Gurobi solves every tested instance optimally.
summary_zh: 宝马与 BCG 研究了用解码量子干涉求解汽车选装包定价整数规划。编码后最小的相关实例有 827 条 max-XORSAT 约束、345 个变量，已超过 100 比特的系统寄存器；性能图使用更小的抽样矩阵。构造出的码距固定为 3，效果更好的 BP2 解码器尚无量子电路。Gurobi 对全部测试实例求出了最优解。
status: seed
last_verified: 2026-09-27
verdict: surviving
dimensions:
  classical_hardness: {level: none, note: "Gurobi optimally solved every tested instance. The paper reports objective quality against Gurobi, not a matched runtime or industrial-scale hardness curve."}
  quantum_easiness: {level: unknown, note: "The constructed code has distance 3 regardless of encoded problem size. The BP1 hard-decision decoder has a circuit; the better BP2 soft-decision decoder in the performance comparison has no quantum implementation."}
  willingness_to_pay: {level: first-hand, note: "BMW researchers co-authored the simplified pricing study. No buyer-defined solve-time, objective-quality or procurement threshold is stated."}
resources: {logical_qubits: "more than 100 for the smallest relevant encoded example", note: "m=827 constraints and n=345 variables after ILP-to-max-XORSAT conversion. Performance figures use downscaled sampled matrices; full circuit simulations use fewer than 30 qubits on random toy instances."}
related:
  problems: [combinatorial-optimization]
  methods: [dqi]
  questions: [first-hand-payment-evidence, dqi-industrial-encoding-crossover]
references:
  - {arxiv: "2509.08328", title: "Towards solving industrial integer linear programs with Decoded Quantum Interferometry", authors: "F. Sabater et al. (BMW Group, BCG, TUM)", year: 2026, note: "Sections 5.3, 6.2, 6.5, 7.1 and 8"}
  - {arxiv: "2408.08292", title: "Optimization by Decoded Quantum Interferometry", authors: "S. P. Jordan et al.", year: 2025, note: "DQI decoder precondition"}
---

## Who needs it

Automakers choose option bundles and prices under demand and production constraints. BMW researchers co-authored a study that formulates a **simplified** version of this decision as a binary integer linear program (ILP) [1]. The authors explicitly say a production model would include competition, heterogeneous elasticities and demand-estimation uncertainty. The study documents industrial interest, without a buyer's required solve time or minimum improvement over existing pricing tools.

## Bottleneck

No classical bottleneck is established for the tested family. Gurobi returns optimal solutions for every considered instance [1, Section 6.1]. The paper reports the fraction of satisfied max-XORSAT constraints against that optimum, but does not provide a matched wall-time curve on original automotive ILPs that could locate a quantum crossover. Its reported DQI objective quality remains substantially below Gurobi's optimum on the smaller tested matrices.

## Computational problems

- [Combinatorial optimisation](../problems/combinatorial-optimization.html) on the original pricing ILP.
- Encoding the ILP as max-XORSAT while preserving objective meaning and producing a dual code that a quantum decoder can handle efficiently. This is the [open encoding benchmark](../questions/dqi-industrial-encoding-crossover.html).

## What the experiment actually tests

The smallest relevant automotive ILP becomes a max-XORSAT instance with **827 constraints and 345 variables** [1, Section 6.5]. The authors say its DQI circuit is too large for their classical circuit simulation. For the performance plot, they sample smaller matrices from that encoding, with matrix-size products from 276 to 10,296; each plotted point averages five sampled instances. The full DQI circuit is simulated separately on random max-XORSAT toy problems with **fewer than 30 qubits**, rather than on the automotive instance.

The ILP reduction uses auxiliary variables for arithmetic and comparisons. A naive alternative with repeated rows would yield code distance 2 [1, Section 5.1]. The **construction actually used has distance 3**, independent of size, because a three-row dependency is present in a CARRY gadget [1, Section 5.3]. It does not provide the growing code distance behind the favourable DQI examples in [2].

The paper implements a coherent circuit for a hard-decision belief-propagation decoder, BP1. Its stronger soft-decision decoder, BP2, improves the plotted DQI expectation, but the authors state that **no quantum implementation of BP2 exists in this work** [1, Sections 6.2 and 7.1]. Resource scaling is estimated for BP1 circuits on downscaled matrices. Thus the best objective-quality curve and the compiled circuit describe different decoder assumptions.

## Reproducible same-instance case

The authors' public example is a nine-variable synthetic option-selection ILP: maximize nine positive weights subject to selecting at most five options. Its exact optimum is **1547**, attained by choosing the five largest weights. Sorting gives a proof of optimality for this entire simplified input family. Our [case study, code and machine-readable result](https://github.com/yuchenguommm/practical-quantum-advantage/tree/main/numerics/cases/automotive_pricing) fix the input and a separate decision target of 1500, reproduce the authors' **827×345** XOR encoding with code statistic `3`, and build a **45-qubit clean arithmetic Grover oracle** for the original nine-variable input. An ideal five-query Grover calculation reaches the target with probability 0.98836. The compiled full circuit has 71,015 CX gates and depth 128,686 in an unoptimized gate basis; four one-oracle interference checks passed. The full Grover circuit and DQI on the 827×345 matrix were not run. These quantities describe different quantum routes and are not combined into a single claimed runtime.

This is a complete **negative assessment of that public illustrative input**: the best classical algorithm is an exact sort, and the DQI encoding already exceeds the 100-logical-qubit target. The numeric threshold 1500 is our reproducible target, not the shifted objective threshold in the authors' encoder or a buyer requirement. The case leaves richer pricing formulations open.

## Verdict

Surviving as an application category, with no advantage demonstrated for this pricing formulation. The industrial provenance is real, but tested instances are classically solved, the encoded realistic example exceeds the 100-logical-qubit target even before ancillas, and the tested reduction fixes the code distance at 3. A stronger claim would need public original ILPs, a conversion preserving the decision objective, a decodable code with distance scaling with size, a coherent circuit for the decoder used in the performance plot, and matched time-to-solution versus a tuned classical solver.
