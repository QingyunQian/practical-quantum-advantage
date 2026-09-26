---
type: question
id: dqi-industrial-encoding-crossover
title: Can an industrial ILP retain DQI's decoding advantage after encoding?
title_zh: 工业整数规划编码后还能保留 DQI 的解码优势吗？
summary: The BMW pricing study converts a small automotive ILP to max-XORSAT, but the smallest relevant encoded example has 827 constraints and 345 variables, its code distance stays at 3, and its best-performing decoder has no quantum circuit. Can a practical ILP family preserve both a growing decoding radius and a competitive end-to-end result?
summary_zh: 宝马定价研究把整数规划编码为 max-XORSAT，但最小的相关编码实例已有 827 条约束和 345 个变量，码距固定为 3，表现最好的解码器尚无量子电路。是否存在工业问题族，在编码后仍能保留随规模增长的可解码半径，并在端到端比较中有竞争力？
status: seed
last_verified: 2026-09-27
question:
  what_would_settle_it: "Publish a size-indexed family of original industrial ILPs or structurally faithful public surrogates, the objective-preserving max-XORSAT conversion, the resulting code distance and coherent-decoder cost, and matched quality-versus-wall-time curves against tuned classical solvers on the same instances. Distinguish BP1 circuit results from BP2 expectation calculations."
  difficulty: phd
  resolved: false
related:
  applications: [automotive-pricing-integer-programming]
  problems: [combinatorial-optimization]
  methods: [dqi]
references:
  - {arxiv: "2509.08328", title: "Towards solving industrial integer linear programs with Decoded Quantum Interferometry", authors: "F. Sabater et al.", year: 2026, note: "Automotive encoding and benchmark, Sections 5–8"}
  - {arxiv: "2408.08292", title: "Optimization by Decoded Quantum Interferometry", authors: "S. P. Jordan et al.", year: 2025, note: "Decoder and code-distance dependence"}
---

## Why it matters

An industrial ILP is an application only if its objective survives conversion to the form the quantum algorithm solves. In the BMW and BCG case study, the smallest relevant encoded pricing example has 827 max-XORSAT constraints and 345 variables [1, Section 6.5]. The performance plots use smaller sampled matrices, while the full quantum-circuit simulations use unrelated random toy instances below 30 qubits. Gurobi solves every tested matrix optimally. These results do not establish an end-to-end comparison on the original pricing decision.

The gadget construction used in the paper produces a code of distance 3 regardless of instance size [1, Section 5.3]. A growing decodable radius is central to DQI's stronger examples [2]. The plotted soft-decision BP2 decoder also lacks a coherent circuit in this study; the resource estimates concern the implemented hard-decision BP1 decoder [1, Sections 6.2 and 7.1]. An encoding that loses the useful code structure, or a decoder that cannot be implemented within the claimed cost, blocks the proposed crossover even when the original ILP matters to a buyer.

## What would settle it

Publish the original ILPs if permitted, or a generator shown to preserve their constraint and objective structure. For at least three increasing sizes, report the original and encoded variable and constraint counts, map each decoded assignment back to the business objective, calculate or bound the code distance, and measure decoder success. Compile the same decoder used for objective-quality claims into a reversible circuit and count its actual qubits and gates.

Compare **the same instances and target objective quality** with tuned Gurobi or equivalent integer-programming and SAT methods. Report both expected DQI quality and the best feasible solution after a stated number of shots, with quantum compilation, repetitions and error-correction overhead included in projected time-to-target. Record a buyer-defined solve-time or price threshold if one exists. A growing quality or time advantage on a faithful family would support the application; failure to retain code distance or decoder performance would narrow it. Generic NP-hardness of ILP does not establish hardness for this family.
