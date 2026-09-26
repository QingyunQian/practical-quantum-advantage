---
type: problem
id: learning-from-quantum-experiments
title: Learning from quantum experiments with quantum memory
title_zh: 借助量子存储从量子实验中学习
summary: "A learner that can store copies of a quantum state or channel and measure them jointly needs exponentially fewer samples than any single-copy learner with classical processing, for tasks such as Pauli-channel estimation, purity testing and predicting observables. The separation is unconditional and information-theoretic, and has been demonstrated on Quantinuum H1-1 with 12 qubits against 62–382 classical bits. The buyer is quantum technology itself: device characterisation, sensor networks, simulator readout."
summary_zh: 能存储量子态或信道的多个副本并联合测量的学习者，在 Pauli 信道估计、纯度检验、可观测量预测等任务上比任何单副本加经典处理的学习者少指数多的样本。这一分离是无条件的信息论结果，并已在 Quantinuum H1-1 上用 12 个比特对 62 到 382 个经典比特演示。买家是量子技术自身：器件表征、传感网络、模拟器读出。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: lower-bound, note: "unconditional information-theoretic sample-complexity lower bounds for single-copy (classical-memory) learners; stronger than any complexity assumption"}
  quantum_easiness: {level: proven, note: "two-copy Bell-basis measurements suffice for Pauli-channel estimation and purity; logarithmic quantum memory suffices for Pauli channels; demonstrated on hardware"}
  willingness_to_pay: {level: second-hand, note: "device characterisation and sensor networks are argued in the literature; the buyer is the quantum industry itself and no external party has stated a target"}
resources: {logical_qubits: "2n–3n for n-qubit systems", gates: "shallow", note: "two or three copies held simultaneously and measured in an entangled basis; the interface that moves a sensor's or device's state into the memory losslessly is the unsolved part"}
related:
  problems: [classical-data-machine-learning, quench-dynamics]
  methods: [error-mitigation]
  claims: [google-random-circuit-sampling]
  questions: [first-hand-payment-evidence]
references:
  - {arxiv: "2111.05881", title: "Exponential separations between learning with and without quantum memory", authors: "S. Chen, J. Cotler, H.-Y. Huang, J. Li", year: 2021, note: "FOCS 2021"}
  - {arxiv: "2112.00778", title: "Quantum advantage in learning from experiments", authors: "H.-Y. Huang, M. Broughton, J. Cotler, S. Chen, J. Li, et al.", year: 2022, note: "Science 376, 1182"}
  - {arxiv: "2309.14326", title: "Efficient Pauli channel estimation with logarithmic quantum memory", authors: "S. Chen, W. Gong", year: 2023, note: "PRX Quantum 6, 020323 (2025)"}
  - {arxiv: "2509.07255", title: "Demonstrating an unconditional separation between quantum and classical information resources", authors: "W. Kretschmer, S. Grewal, M. DeCross, et al., S. Aaronson", year: 2025, note: "Quantinuum H1-1, 12 qubits"}
  - {arxiv: "2410.17718", title: "Exponential Separations between Quantum Learning with and without Purification", authors: "Z. Liu, W. Gong, Z. Du, Z. Cai", year: 2024}
  - {arxiv: "2507.11089", title: "On the Fundamental Resource for Exponential Advantage in Quantum Channel Learning", authors: "M. Kim, C. Oh", year: 2025}
---

## Best classical

The classical competitor is a learner that measures each copy of the unknown state or channel separately, possibly adaptively, and processes the outcomes on a classical computer. Classical shadows and related randomized-measurement protocols are the practical instances and they are efficient for many tasks: predicting few-body observables, fidelities, and low-rank noise channels. The lower bounds below are worst-case over a family of states or channels; when the actual object is structured (low-rank, local, or sparse in the Pauli basis), single-copy protocols are often enough, which is the main reason the separation has produced no external market.

## Best quantum

Chen, Cotler, Huang and Li proved that for several natural tasks a learner with quantum memory, able to hold copies and perform entangled measurements, needs polynomially many samples while any learner without quantum memory needs exponentially many [1]. The proofs are information-theoretic; they do not assume BPP ≠ BQP or any cryptographic hardness. Huang et al. gave the physical framing and a Sycamore demonstration: predicting observables, testing symmetry of dynamics, and estimating Pauli channels with two-copy Bell measurements [2]. The list of tasks has grown: purity and mixedness testing, quantum principal component analysis, separations for learning with and without purification of the state [5], and an analysis of which resource (memory versus coherence) is fundamental for channel learning [6]. On the resource side, Chen and Gong showed that Pauli-channel estimation needs only O(log n) qubits of quantum memory rather than a full second copy [3].

The cleanest hardware evidence is Kretschmer et al. on Quantinuum H1-1: a 12-qubit quantum system accomplishes a communication-style task that provably requires 62 to 382 classical bits, an unconditional separation in information resources rather than in time [4]. Together with the Sycamore experiment of Huang et al. [2], this is the only family of exponential quantum advantage that is both proven without assumptions and demonstrated on hardware.

## Who wants it

The buyer is quantum technology. Characterising a 50-qubit device's noise channel, reading out a quantum simulator, and fusing the outputs of a quantum sensor network are all tasks in which the data arrive as quantum states, so the input bottleneck that kills classical-data QML does not apply. The obstacle is the interface: the separation assumes the state can be moved losslessly into the learner's quantum memory, and in practice a sensor's state must be transduced and stored for the duration of the joint measurement. No external party (a chip vendor, a metrology institute) has written down a characterisation task with a target that single-copy methods fail.

## Verdict

Surviving, and internal to the field. Hardness is a lower bound, easiness is proven, and there is hardware evidence at 12 qubits [4]; what is missing is a first-hand buyer outside the quantum industry and an interface that makes the "quantum data" premise real. Evidence that would promote the page: a device-characterisation or sensing task where an entangled-measurement protocol reduces experiment time by a documented factor on a deployed system, with the customer's target stated in writing.
