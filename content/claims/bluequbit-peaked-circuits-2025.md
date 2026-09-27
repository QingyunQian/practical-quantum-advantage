---
type: claim
id: bluequbit-peaked-circuits-2025
title: BlueQubit 56-qubit peaked circuits on Quantinuum H2, "classical needs years"
title_zh: BlueQubit 在 Quantinuum H2 上的 56 比特 peaked circuits，“经典需数年”
summary: Gharibyan et al. ran 56-qubit peaked circuits on Quantinuum H2 and estimated that classical simulation would take years. Kremer and Dupuis recovered the peak in 4,059 seconds on one A100 GPU. A later same-instance tracker submission reports 734 seconds on an M5 Pro laptop CPU, with a documented cutoff-sensitive independent reproduction attempt.
summary_zh: Gharibyan 等在 Quantinuum H2 上运行 56 比特 peaked circuits，估计经典模拟需数年。Kremer 与 Dupuis 在单块 A100 GPU 上用 4,059 秒复现峰值。后续同实例提交报告了 M5 Pro 笔记本 CPU 上的 734 秒运行，但公开讨论记录了独立复现对截断参数的敏感性。
status: reviewed
last_verified: 2026-09-27
claim:
  claimant: BlueQubit (Gharibyan et al.), experiment on Quantinuum H2
  date: 2025-10
  statement: "Heuristic quantum advantage with peaked circuits: a 56-qubit H2 run produces the target peaked bitstring in under two hours, while classical simulation on Frontier or Summit would take years, suggesting a potentially exponential separation."
  hardware: Quantinuum System Model H2 (trapped ions)
  qubits: 56
  refuted: true
  refutation_date: 2026-04
  refuted_by: "Kremer and Dupuis (tensor-network contraction exploiting the mirrored circuit structure, single GPU, about one hour)"
  time_to_refute: "six months"
related:
  problems: [quench-dynamics]
  claims: [google-random-circuit-sampling, google-quantum-echoes-otoc-2025]
references:
  - {arxiv: "2510.25838", title: "Heuristic Quantum Advantage with Peaked Circuits", authors: "H. Gharibyan, M. Z. Mullath, N. E. Sherman, V. P. Su, H. Tepanyan, Y. Zhang", year: 2025}
  - {arxiv: "2604.21908", title: "Efficient Classical Simulation of Heuristic Peaked Quantum Circuits", authors: "D. Kremer, N. Dupuis", year: 2026}
  - {url: "https://github.com/quantum-advantage-tracker/quantum-advantage-tracker.github.io/issues/153", title: "Same-instance MPO plus unswapping CPU submission and public reproduction discussion", authors: "A. Galda and Quantum Advantage Tracker reviewers", year: 2026, note: "P9 56×1917 circuit; 734 s reported on M5 Pro; cutoff-sensitive independent attempt"}
---

## Claim

Peaked circuits are random-looking circuits engineered so that one output bitstring carries a large probability; unlike random circuit sampling, the answer is verifiable by checking for the peak. Gharibyan et al. built such circuits by variationally training a second half to partially undo a random first half, ran them on Quantinuum's 56-qubit H2 with up to 2,000 two-qubit gates at all-to-all connectivity, and observed the planted bitstring directly in under two hours of device time. They estimated that reproducing this classically on exascale machines would take years and described the result as heuristic quantum advantage with a potentially exponential separation [1].

## Refutation

- Kremer and Dupuis showed that the training procedure leaves the circuit approximately mirror-symmetric, so a tensor-network contraction that pairs the two halves collapses most of the entanglement. They recovered the peaked bitstring of the largest H2 instance in about one hour on a single GPU, roughly half the quantum wall-clock time, and argued the construction is efficiently simulable in general [2]. The preprint appeared on 2026-04-23, six months after the claim.
- The [Quantum Advantage Tracker](https://quantum-advantage-tracker.github.io/) records the same `peaked_circuit_P9_Hqap_56x1917` instance and the earlier 7,200-second H2 and 4,059-second A100 submissions. A later CPU submission reports the correct peak in 734 seconds on an Apple M5 Pro laptop [3]. In the public issue, an independent user reported that the submitted cutoff stalled on another M5 run; the author noted that the greedy truncation path is cutoff-sensitive and proposed a small sweep. We therefore treat 734 seconds as a **reported successful run on that hardware and configuration**, not a robust cross-machine runtime guarantee. This issue is a useful model of why one versioned instance and its subsequent submissions should remain together.
- The lesson is structural, not incremental: the same optimisation that makes the output verifiable also plants classical structure. A peaked circuit whose peak cannot be exploited classically would need a construction with a hardness argument, which this one did not have.

## Lesson for the catalogue

"Years on Frontier" was an estimate for generic contraction of a circuit that was not generic. Any verifiable-advantage claim should state what classical algorithm the estimate assumes and why the verification structure does not help that algorithm. Compare `google-quantum-echoes-otoc-2025`, where the classical infeasibility argument is at least made explicitly against the strongest known tensor-network method.
