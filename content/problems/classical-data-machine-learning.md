---
type: problem
id: classical-data-machine-learning
title: Machine learning on classical data (kernels, QNNs, low-rank linear algebra)
title_zh: 经典数据上的机器学习（核方法、量子神经网络、低秩线性代数）
summary: Low-rank linear algebra under specified sample-and-query access has classical sublinear algorithms. Random-feature dequantization also applies to kernel and QNN models under stated sufficient conditions. These results narrow particular exponential time claims; they do not cover all learning from classical data. A separate 2026 result proves an unconditional space separation for constructed classical-data streams, while its real-data test remains open.
summary_zh: 在特定采样与查询条件下，低秩线性代数已有次线性经典算法。满足充分条件的部分量子核和量子神经网络模型也能用随机特征方法近似。这些结果削弱了具体的指数时间加速主张，不能推广到所有经典数据学习任务。另一项 2026 年工作对构造的经典数据流任务证明了无条件空间分离，真实数据检验仍待完成。
status: seed
last_verified: 2026-09-27
verdict: no-go
dimensions:
  classical_hardness: {level: none, note: "specified low-rank sample-access tasks have dimension-independent classical algorithms; random-feature bounds apply to kernel and QNN models only when their sufficient conditions hold; the separate streaming-space model is excluded"}
  quantum_easiness: {level: conditional, note: "matched-access classical algorithms narrow the specified time claims, while other supervised-learning tasks and the separately catalogued streaming-space theorem require their own analysis"}
  willingness_to_pay: {level: none, note: "ML buyers are abundant but none has stated a task that classical ML fails and quantum ML meets"}
related:
  problems: [learning-from-quantum-experiments, sparse-linear-systems, sorting-fft-storage, streaming-classical-data-memory]
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

For the low-rank linear-algebra family (recommendation systems, principal component analysis, support-vector machines and regression), Chia and colleagues give classical singular-value-transformation methods whose cost is independent of input dimension under suitable sampling assumptions [1]. This defeats the dimension-based exponential separation claimed for the corresponding low-rank quantum routines under matched access. Sparse, high-rank systems with efficient operator access and limited output require separate analysis on the [linear-systems page](sparse-linear-systems.html).

For supervised kernel and QNN models, Sahebi et al. bound the risk gap between quantum models and classical random-Fourier-feature models, and give **sufficient conditions** under which that gap is small [2]. Their result does not say that every trainable variational circuit is efficiently classically simulable. Models outside the stated conditions need their own comparison. Eisert and Preskill's assessment [5] is a perspective on how much application evidence remains, not a theorem excluding every QML advantage.

## Best quantum

- Arbitrary amplitude loading has an Ω(N) input cost without a compact preparation procedure. Active QRAM changes the access model but carries a hardware opportunity cost under the architectures analysed by Jaques and Rattew [6]. The [QRAM page](../methods/qram.html) keeps these architecture assumptions explicit.
- A conditional time separation exists on constructed data. Liu, Arunachalam and Temme build a classification task from discrete logarithm on which a quantum kernel classifier succeeds under a classical hardness assumption [3]. The claim that this is the *only* provable separation for classical-data learning is too broad.
- A different, unconditional separation counts **space under a sample budget**. Zhao and colleagues prove classical memory lower bounds for constructed streaming linear-system and classification tasks while their quantum oracle-sketching algorithm uses polylogarithmic ideal logical memory [4]. Their real-dataset plots pair classical ridge/PCA accuracy with a formula-derived quantum memory count; the public code does not execute the quantum learner on those datasets. See the [separate streaming-space problem](../problems/streaming-classical-data-memory.html). The result does not reinstate an exponential *time* advantage for the low-rank and kernel routes on this page.

## What survives

The low-rank and random-feature routes covered here offer weaker time-advantage cases after matched classical access and error are counted [1, 2]. Other classical-data learning tasks remain outside those theorems. The separate [classical-data streaming problem](../problems/streaming-classical-data-memory.html) has an unconditional space theorem for constructed tasks [4]. Learning from quantum experiments has a different input model and its own [problem page](learning-from-quantum-experiments.html).

## Verdict

No-go **for the specified dimension-based exponential time claims** in the low-rank sample-access setting [1]. Random-feature bounds weaken kernel and QNN claims only where their sufficient conditions hold [2]. The page's verdict should not be read as a lower bound against every classical-data learning algorithm. A positive candidate needs a specified distribution, achievable quantum training and inference cost, a matched strong classical baseline and a buyer-defined target. The [streaming-space entry](../problems/streaming-classical-data-memory.html) records a different memory/sample separation [4].
