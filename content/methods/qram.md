---
type: method
id: qram
title: Quantum random-access memory (QRAM) and classical data loading
title_zh: 量子随机存取存储器（QRAM）与经典数据加载
summary: A QRAM answers a superposition of addresses with stored values in O(log N) depth and is the assumed input model for most quantum linear-algebra, machine-learning and search speedups on classical data. It is an addressing structure, not a storage advantage. The Holevo bound limits n qubits to n classical bits, all O(N) cells must be active on every query, and the same control hardware could run a parallel classical algorithm equally fast. Jaques and Rattew conclude that cheap passive QRAM is unlikely; resource-state QRAM factories improve constants, not the argument.
summary_zh: QRAM 用 O(log N) 深度对地址叠加态返回存储值的叠加态，是大多数经典数据上量子线性代数、机器学习与搜索加速所假设的输入模型。它是寻址结构而非存储优势：Holevo 界限制 n 个量子比特只能承载 n 个经典比特，O(N) 个存储单元在每次查询时都必须活动，同样的控制硬件拿来跑并行经典算法一样快。Jaques 与 Rattew 的综述认为廉价的被动 QRAM 不太可能；资源态 QRAM 工厂改善常数但不改变论证。
status: seed
last_verified: 2026-09-26
verdict: no-go
dimensions:
  classical_hardness: {level: none, note: "any algorithm whose speedup depends on QRAM over classical data must be compared with a classical machine that has the same O(N) active hardware; loading N numbers costs Ω(N) either way"}
  quantum_easiness: {level: no, note: "log-depth bucket-brigade circuits exist, but fault-tolerant versions cost O(N) active error-corrected cells per query; no passive, cheap QRAM is known"}
  willingness_to_pay: {level: none, note: "storage users want density and bandwidth; Holevo forbids a density gain and QRAM offers no bandwidth gain"}
related:
  problems: [sorting-fft-storage, classical-data-machine-learning, sparse-linear-systems]
  methods: [hhl-qsvt, grover-amplitude-estimation]
references:
  - {arxiv: "2305.10310", title: "QRAM: A Survey and Critique", authors: "S. Jaques, A. G. Rattew", year: 2025, note: "Quantum 9, 1922"}
  - {arxiv: "2503.19172", title: "Resource-state Quantum RAM for Fast and Error-Correctable Queries", authors: "F. Cesa, H. Bernien, H. Pichler", year: 2026, note: "Nat. Commun."}
  - {arxiv: "1910.06151", title: "Sampling-based sublinear low-rank matrix arithmetic framework for dequantizing quantum machine learning", authors: "N.-H. Chia et al.", year: 2020}
  - {arxiv: "2604.07639", title: "Exponential quantum advantage in processing massive classical data", authors: "H. Zhao, A. Zlokapa, H. Neven, R. Babbush, J. Preskill, J. R. McClean, H.-Y. Huang", year: 2026, note: "space/communication advantage with ~60 logical qubits, two worked examples; not a time advantage"}
  - {arxiv: "2510.19928", title: "Mind the gaps: The fraught road to quantum advantage", authors: "J. Eisert, J. Preskill", year: 2025}
---

## How it works

A QRAM implements the map Σ_i α_i |i⟩|0⟩ → Σ_i α_i |i⟩|x_i⟩ for N stored classical values x_i. The bucket-brigade architecture routes the address qubits down a binary tree of N − 1 switches and back in O(log N) depth, and is the input model assumed by HHL-type linear algebra, quantum recommendation systems, quantum k-means, Grover search over databases, and amplitude-encoding of classical vectors. Whether a QRAM query should be counted as one operation or as N is the whole question.

## Preconditions

For a QRAM-based speedup on classical data to be real:

1. The N memory cells and the routing tree must exist as coherent, error-corrected hardware, and the query must cost O(polylog N) in the same units used for the rest of the algorithm.
2. The data must already be in the memory; writing N values costs Ω(N) regardless.
3. The classical baseline must be charged for a machine of comparable size. A QRAM with N active cells is an O(N)-parallel machine.

## Known limits

- **Information-theoretic ceiling.** The Holevo bound limits the classical information reliably retrievable from n qubits to n bits, so there is no quantum storage-density advantage; QRAM is an addressing scheme layered on ordinary classical memory.
- **Every query touches every cell.** Jaques and Rattew's survey [1] examines the physical proposals (bucket brigade, optical, spin-based) and the fault-tolerant versions and argues on opportunity-cost grounds that a QRAM which is cheap to query is unlikely: error correction of a log-depth query over N cells requires the cells to be active and error-corrected, giving O(N) hardware per query; and hardware capable of coherently addressing N cells in O(log N) time could equally run a classical algorithm on N parallel processors, which removes the speedup for Grover-over-a-database and for QML on classical inputs. Resource-state QRAM (Cesa, Bernien, Pichler) prepares the routing tree as a factory-produced entangled state so that queries become fast and error-correctable [2]; it lowers the per-query latency and improves error handling, but the active hardware scales the same way and the opportunity-cost argument stands.
- **The algorithms that assumed QRAM were dequantized anyway.** The low-rank linear-algebra and recommendation algorithms that motivated QRAM admit classical polylogarithmic algorithms under the sample-and-query access model that QRAM would provide [3]; the input model is the source of both the quantum and the classical speedup.
- **What survives is not a time advantage.** Zhao et al. show exponential quantum advantage in processing massive classical data using ~60 logical qubits [4]; the advantage is in space and communication (a streaming sketch of the data), applies to two constructed problem families, and requires reviewing before any application is claimed. Eisert and Preskill describe QML advantage on classical data as resting on cherry-picked examples [5].

## Verdict

No-go for storage and for data loading as a source of advantage. QRAM does not increase storage density (Holevo), does not reduce the cost of loading data (Ω(N)), and, once the hardware for a fast coherent query is built and paid for, that hardware could run a parallel classical algorithm at least as fast. Algorithms whose speedup survives only under a free-QRAM accounting (Grover over databases, HHL on data matrices, most QML on classical inputs) inherit this verdict. What would change it: a passive QRAM design whose per-query cost is provably polylog(N) in error-corrected resources, with no O(N) active component, or an application where the data is generated by a quantum process rather than stored classically (which is not QRAM's job).
