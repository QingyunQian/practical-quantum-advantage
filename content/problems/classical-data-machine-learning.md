---
type: problem
id: classical-data-machine-learning
title: Machine learning on classical data (kernels, QNNs, low-rank linear algebra)
title_zh: 经典数据上的机器学习（核方法、量子神经网络、低秩线性代数）
summary: The quantum-machine-learning proposals of 2014–2019 assumed low-rank data with sample access and were dequantized by Tang and by Chia et al.; kernel and variational models are matched by random Fourier features and tensor-train surrogates. The only provable separations use datasets built from the discrete logarithm. A 2026 result gives exponential space and communication advantage on massive data with under 60 logical qubits, but it is a memory advantage, not a time advantage, and awaits scrutiny.
summary_zh: 2014 到 2019 年的量子机器学习提案假设低秩数据和采样访问，被 Tang 与 Chia 等人去量子化；核方法和变分模型被随机 Fourier 特征和张量列代理追平。唯一可证明的分离用的是由离散对数构造的数据集。2026 年一项结果用不到 60 个逻辑比特在海量数据上给出指数级的空间和通信优势，但那是内存优势而不是时间优势，尚待检验。
status: seed
last_verified: 2026-09-26
verdict: no-go
dimensions:
  classical_hardness: {level: none, note: "low-rank linear algebra with sample access is classically polynomial; kernel/QSVM/QNN predictions dequantized by random Fourier features; the only crypto-hard separation uses an artificial discrete-log dataset"}
  quantum_easiness: {level: no, note: "loading N classical numbers costs Ω(N) without QRAM, and QRAM's fault-tolerant cost is comparable to classical memory; trainable variational models are the classically simulable ones"}
  willingness_to_pay: {level: none, note: "ML buyers are abundant but none has stated a task that classical ML fails and quantum ML meets"}
related:
  problems: [learning-from-quantum-experiments, sparse-linear-systems, sorting-fft-storage]
  methods: [hhl-qsvt, qram, vqe]
references:
  - {arxiv: "1910.06151", title: "Sampling-based sublinear low-rank matrix arithmetic framework for dequantizing quantum machine learning", authors: "N.-H. Chia, A. Gilyén, T. Li, H.-H. Lin, E. Tang, C. Wang", year: 2020, note: "STOC 2020"}
  - {arxiv: "2505.15902", title: "On dequantization of supervised quantum machine learning via random Fourier features", authors: "M. Sahebi, A. Barthe, Y. Suzuki, Z. Holmes, M. Grossi", year: 2025}
  - {arxiv: "2010.02174", title: "A rigorous and robust quantum speed-up in supervised machine learning", authors: "Y. Liu, S. Arunachalam, K. Temme", year: 2021, note: "Nature Physics 17, 1013; discrete-log-based dataset"}
  - {arxiv: "2604.07639", title: "Exponential quantum advantage in processing massive classical data", authors: "H. Zhao, A. Zlokapa, H. Neven, R. Babbush, J. Preskill, J. R. McClean, H.-Y. Huang", year: 2026}
  - {arxiv: "2510.19928", title: "Mind the gaps: the fraught road to quantum advantage", authors: "J. Eisert, J. Preskill", year: 2025}
  - {arxiv: "2305.10310", title: "QRAM: A Survey and Critique", authors: "S. Jaques, A. G. Rattew", year: 2025, note: "Quantum 9, 1922"}
---

## Best classical

For the linear-algebra family (recommendation systems, principal component analysis, support-vector machines, low-rank regression), Tang's 2018 recommendation-system algorithm and the general framework of Chia, Gilyén, Li, Lin, Tang and Wang show that whenever the quantum algorithm assumes low rank and sample-and-query access to the data, a classical algorithm with the same access runs in time polynomial in rank and precision and independent of dimension [1]. That removed the exponential claims of HHL-based QML. What remains of HHL survives only for sparse, well-conditioned matrices with compactly preparable inputs and scalar outputs, which are not typical data-science conditions.

For kernel and variational models, Sahebi et al. show that predictions of quantum kernel machines, QSVMs and many quantum neural networks are reproduced by classical random-Fourier-feature models with polynomial resources [2]; a growing body of work makes the pairing precise: the parameter regimes in which variational circuits are trainable (no barren plateau) are the regimes in which they are classically simulable. Eisert and Preskill's 2025 assessment describes the surviving QML advantages as "cherry-picked examples" [5].

## Best quantum

- The input bottleneck is fundamental. Loading N classical numbers into amplitudes costs Ω(N) without a QRAM, and Jaques and Rattew's survey argues that a fault-tolerant, actively error-corrected QRAM has an opportunity cost comparable to just doing the classical computation, while a cheap passive QRAM is "unlikely" [6].
- Provable separation exists only on artificial data. Liu, Arunachalam and Temme construct a classification task from the discrete logarithm problem on which a quantum kernel classifier succeeds and every efficient classical learner fails, assuming discrete log is hard [3]. Nothing resembling a natural dataset has this structure.
- The one recent positive result changes the resource being counted. Zhao, Zlokapa, Neven, Babbush, Preskill, McClean and Huang show that for certain tasks on massive classical data, a quantum processor of fewer than 60 logical qubits achieves exponential savings in memory and communication over any classical algorithm, with unconditional information-theoretic proofs, for a small number of specific problems [4]. This is a space advantage, not a time advantage; whether any of the stated tasks matches a real workload has not been examined independently.

## What survives

Almost nothing on the "learn from classical data faster" axis. What survives is adjacent: learning from quantum data with quantum memory (see the learning-from-quantum-experiments page), and streaming or communication-limited settings where the count that matters is qubits stored rather than gates executed [4].

## Verdict

No-go. The dequantization results are theorems, the input barrier is structural, and the only rigorous separation lives on a cryptographic construction. The page would be reopened by an independent check that one of the massive-data tasks in Zhao et al. [4] corresponds to a workload someone runs, and that its memory saving translates into cost that a buyer would pay for.
