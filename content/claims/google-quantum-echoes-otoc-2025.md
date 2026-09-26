---
type: claim
id: google-quantum-echoes-otoc-2025
title: Google "Quantum Echoes" second-order OTOC on Willow (2025)
title_zh: Google Willow 上的 “Quantum Echoes” 二阶 OTOC 实验（2025）
summary: Google measured second-order out-of-time-order correlators with time-reversed random circuits on 65 qubits of the 103-qubit Willow chip and reported a 13,000-fold speedup over the best classical estimate, with the observable verifiable on small instances. As of 2026-09-26 there is no classical reproduction; Bermejo et al. argue belief-propagation tensor networks cannot feasibly simulate it. Exact verification stops near 40 qubits, and no hardness theorem covers the task.
summary_zh: Google 在 103 比特 Willow 芯片的 65 个比特上用时间反演随机电路测量二阶 OTOC，宣称比最好的经典估计快 13,000 倍，且可观测量在小实例上可验证。截至 2026-09-26 没有经典复现；Bermejo 等论证信念传播张量网络无法可行地模拟它。精确验证只到约 40 比特，且没有硬度定理覆盖该任务。
status: reviewed
last_verified: 2026-09-26
claim:
  claimant: Google Quantum AI
  date: 2025-10
  statement: "Constructive interference at the edge of quantum ergodic dynamics: second-order OTOCs measured with time-reversal on a 103-qubit processor, on circuits of 65 qubits, exceed the simulation capacity of known classical algorithms, a 13,000-fold speedup over the best classical method."
  hardware: Willow (superconducting)
  qubits: 65
  refuted: false
  refuted_by: "No classical reproduction as of 2026-09-26"
related:
  problems: [quench-dynamics, learning-from-quantum-experiments]
  methods: [error-mitigation]
  claims: [google-random-circuit-sampling, bluequbit-peaked-circuits-2025]
references:
  - {arxiv: "2506.10191", title: "Constructive interference at the edge of quantum ergodic dynamics", authors: "D. A. Abanin et al. (Google Quantum AI)", year: 2025, note: "Nature 646, 825 (2025), published as 'Observation of constructive interference at the edge of quantum ergodicity'"}
  - {arxiv: "2604.15427", title: "Tensor Networks with Belief Propagation Cannot Feasibly Simulate Google's Quantum Echoes Experiment", authors: "P. Bermejo, B. Villalonga, B. Ware, G. Vidal, A. Szasz", year: 2026}
  - {arxiv: "2510.19550", title: "Quantum computation of molecular geometry via many-body nuclear spin echoes", authors: "C. Zhang, R. G. Cortiñas, A. H. Karamlou et al.", year: 2025, note: "companion NMR application, 9 to 15 spins, classically simulable"}
  - {arxiv: "2407.12768", title: "A polynomial-time classical algorithm for noisy quantum circuits", authors: "T. Schuster, C. Yin, X. Gao, N. Y. Yao", year: 2025}
  - {arxiv: "2607.07530", title: "The NISQ Trap: Eight Years of Demonstrations the Hardware Was Built to Lose", authors: "A. Hagar", year: 2026}
---

## Claim

The experiment measures a second-order out-of-time-order correlator, OTOC(2): a random circuit U is applied, a local operator is inserted, U† is applied, and the interference between Pauli strings that form large loops is read out. Google reports that with time reversal the correlator stays sensitive to the underlying dynamics at long times, that the signal is dominated by constructive interference between loop-forming Pauli strings, and that on 65-qubit circuits of the 103-qubit Willow processor the measurement exceeds the capacity of known classical algorithms, quoted as 13,000× faster than the best classical method on Frontier [1]. The arXiv preprint appeared in June 2025; the Nature paper in October 2025 under the title "Observation of constructive interference at the edge of quantum ergodicity". The observable is a single expectation value, which the authors present as verifiable on small instances and, in a companion paper, as a route to NMR-based molecular geometry [3].

## Refutation

No classical reproduction as of 2026-09-26. Searched: arXiv quant-ph and cond-mat listings for "OTOC", "quantum echoes" and "Willow" through September 2026; the citing literature of [1]; the classical counter-results survey maintained with this repository. What exists:

- Bermejo, Villalonga, Ware, Vidal and Szasz (a Google-affiliated team) analysed belief-propagation tensor networks, the method that reproduced the IBM 2023 and D-Wave 2025 experiments, and concluded from theory and numerics that the states generated are too entangled and too incompressible for BP tensor networks to simulate the experiment feasibly [2]. This is an argument against one method family, made by the claimant's side.
- Objections on record: exact classical verification of the measured OTOC(2) only reaches about 40 qubits, so the 65-qubit value is checked against error-mitigated rescaling, not against an exact number; there is no hardness theorem for OTOC(2) estimation; and the constant-noise polynomial-time theorem of Schuster et al. [4] applies asymptotically to noisy random circuits, although the loop-interference structure may keep the relevant polynomial large. Hagar's survey classifies this as the single NISQ demonstration whose hardware-reachable regime has not yet been shown to overlap a classically compressible one [5].

This is, on the record as of 2026-09-26, the most robust standing NISQ advantage claim, and the catalogue treats "not yet reproduced" as distinct from "shown hard".

## Lesson for the catalogue

OTOC(2) is a high-order correlator of a random circuit, not an application quantity; the NMR companion work [3] runs at 9 to 15 spins and is classically simulable. What the claim would need to become an application entry is a Hamiltonian, not a random circuit, at the same depth and a buyer for the correlator; the `quench-dynamics` problem page tracks that gap.
