---
type: claim
id: bluequbit-peaked-circuits-2025
title: BlueQubit 56-qubit peaked circuits on Quantinuum H2, "classical needs years"
title_zh: BlueQubit 在 Quantinuum H2 上的 56 比特 peaked circuits，“经典需数年”
summary: Gharibyan et al. ran 56-qubit peaked circuits with up to 2,000 all-to-all two-qubit gates on Quantinuum's H2 and reported that the device found the planted bitstring in under two hours while exascale classical simulation would take years. Six months later Kremer and Dupuis exploited the circuits' mirrored structure to recover the peak in about one hour on a single GPU.
summary_zh: Gharibyan 等在 Quantinuum H2 上运行 56 比特、最多 2,000 个全连接两比特门的 peaked circuits，宣称设备在两小时内找到植入比特串，而百亿亿次级经典模拟需数年。半年后，Kremer 与 Dupuis 利用电路的镜像结构，在单块 GPU 上约一小时内复现了峰值。
status: reviewed
last_verified: 2026-09-26
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
---

## Claim

Peaked circuits are random-looking circuits engineered so that one output bitstring carries a large probability; unlike random circuit sampling, the answer is verifiable by checking for the peak. Gharibyan et al. built such circuits by variationally training a second half to partially undo a random first half, ran them on Quantinuum's 56-qubit H2 with up to 2,000 two-qubit gates at all-to-all connectivity, and observed the planted bitstring directly in under two hours of device time. They estimated that reproducing this classically on exascale machines would take years and described the result as heuristic quantum advantage with a potentially exponential separation [1].

## Refutation

- Kremer and Dupuis showed that the training procedure leaves the circuit approximately mirror-symmetric, so a tensor-network contraction that pairs the two halves collapses most of the entanglement. They recovered the peaked bitstring of the largest H2 instance in about one hour on a single GPU, roughly half the quantum wall-clock time, and argued the construction is efficiently simulable in general [2]. The preprint appeared on 2026-04-23, six months after the claim.
- The lesson is structural, not incremental: the same optimisation that makes the output verifiable also plants classical structure. A peaked circuit whose peak cannot be exploited classically would need a construction with a hardness argument, which this one did not have.

## Lesson for the catalogue

"Years on Frontier" was an estimate for generic contraction of a circuit that was not generic. Any verifiable-advantage claim should state what classical algorithm the estimate assumes and why the verification structure does not help that algorithm. Compare `google-quantum-echoes-otoc-2025`, where the classical infeasibility argument is at least made explicitly against the strongest known tensor-network method.
