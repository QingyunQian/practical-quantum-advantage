---
type: claim
id: google-random-circuit-sampling
title: Google random circuit sampling (Sycamore 2019, Willow 2024)
title_zh: Google 随机电路采样（Sycamore 2019，Willow 2024）
summary: Google's 2019 Sycamore claim (53 qubits, 20 cycles, "10,000 years on Summit") was overtaken by tensor-network samplers within three years, at 512 GPUs and 15 hours. The December 2024 Willow claim (105-qubit chip, "10^25 years on Frontier") has no end-to-end classical reproduction as of 2026-09-26, but its fidelity is measured only by extrapolated cross-entropy and asymptotic theorems say the constant-fidelity regime is simulable in principle.
summary_zh: Google 2019 年的 Sycamore 主张（53 比特、20 层、“Summit 需一万年”）三年内被张量网络采样器超越，代价为 512 块 GPU 15 小时。2024 年 12 月的 Willow 主张（105 比特芯片，“Frontier 需 10^25 年”）截至 2026-09-26 没有端到端的经典复现，但其保真度只能靠外推的交叉熵衡量，且渐近定理表明恒定保真度区间原则上可模拟。
status: reviewed
last_verified: 2026-09-26
claim:
  claimant: Google Quantum AI
  date: 2024-12
  statement: "Random circuit sampling on the Willow processor completes in under five minutes a task that would take Frontier 10 septillion (10^25) years; the 2019 Sycamore claim was 200 seconds versus 10,000 years on Summit."
  hardware: Sycamore (2019), Willow (2024), superconducting
  qubits: 105
  refuted: false
  refuted_by: "2019 Sycamore instance: Pan, Chen, Zhang (tensor-network sampler, 512 GPUs, 15 hours, one million samples at XEB 0.0037). Willow 2024 instance: no classical reproduction as of 2026-09-26."
related:
  problems: [quench-dynamics]
  claims: [google-quantum-echoes-otoc-2025, bluequbit-peaked-circuits-2025]
references:
  - {doi: "10.1038/s41586-019-1666-5", title: "Quantum supremacy using a programmable superconducting processor", authors: "F. Arute et al.", year: 2019, note: "Nature 574, 505 (2019); the arXiv entry 1910.11333 is the supplementary information"}
  - {arxiv: "2111.03011", title: "Solving the sampling problem of the Sycamore quantum circuits", authors: "F. Pan, K. Chen, P. Zhang", year: 2022, note: "PRL 129, 090502 (2022)"}
  - {arxiv: "2304.11119", title: "Phase transition in Random Circuit Sampling", authors: "A. Morvan et al.", year: 2024, note: "Nature 634, 328 (2024); 67 qubits at 32 cycles"}
  - {url: "https://blog.google/technology/research/google-willow-quantum-chip/", title: "Meet Willow, our state-of-the-art quantum chip", authors: "Google Quantum AI", year: 2024, note: "9 December 2024; source of the 10^25-year figure"}
  - {arxiv: "2407.12768", title: "A polynomial-time classical algorithm for noisy quantum circuits", authors: "T. Schuster, C. Yin, X. Gao, N. Y. Yao", year: 2025}
  - {arxiv: "2412.11924", title: "Establishing a New Benchmark in Quantum Computational Advantage with 105-qubit Zuchongzhi 3.0 Processor", authors: "D. Gao et al.", year: 2024}
  - {arxiv: "2607.07530", title: "The NISQ Trap: Eight Years of Demonstrations the Hardware Was Built to Lose", authors: "A. Hagar", year: 2026}
---

## Claim

Random circuit sampling (RCS) asks the processor to output bitstrings from a random circuit; success is scored by linear cross-entropy benchmarking (XEB) against ideal amplitudes on small instances and by extrapolation on large ones. Arute et al. sampled 53-qubit, 20-cycle circuits on Sycamore in 200 seconds and estimated 10,000 years on Summit [1]. Morvan et al. moved to 67 qubits at 32 cycles at XEB fidelity around 1.5×10^-3 and argued the cost is beyond existing supercomputers [3]. In December 2024 Google announced Willow, a 105-qubit chip, and stated that its RCS run would take Frontier 10^25 years [4]. The Zuchongzhi 3.0 group reported a comparable 83-qubit, 32-cycle benchmark [6].

## Refutation

Two different instances have to be kept apart.

- **Sycamore 2019: overtaken.** Pan, Chen and Zhang produced one million uncorrelated samples of the 53-qubit, 20-cycle circuit at XEB fidelity 0.0037 in about 15 hours on 512 GPUs with a tensor-network sampler [2]; later work produced verified samples faster than the hardware. The "10,000 years" estimate assumed Schrödinger–Feynman simulation with full-fidelity output, which is not what the experiment delivered. The 2019 claim is therefore treated as refuted in its stated form.
- **Willow 2024: no classical reproduction as of 2026-09-26.** Searched: arXiv listings under quant-ph for "random circuit sampling" and "Willow" through September 2026, the survey of classical counter-results maintained with this repository, and the citing literature of [3] and [4]. No group has produced samples at the claimed XEB fidelity for 67-qubit, 32- or 40-cycle Willow circuits. Three standing objections are recorded: (i) XEB fidelity above roughly 40 to 50 qubits is an extrapolation, not a measurement, so the target being missed is itself unverified; (ii) Schuster, Yin, Gao and Yao proved that circuits with constant local noise are classically simulable in polynomial time for observables [5], and the fixed-fidelity, log-depth regime of RCS is the regime that theorem addresses asymptotically, though the polynomial is impractical at these sizes; (iii) the base rate: classical cost estimates for RCS instances have shrunk by several orders of magnitude within two to three years each time (Hagar's "NISQ trap" [7]).

The `refuted: false` flag refers to the Willow instance only.

## Lesson for the catalogue

RCS has no application and is on this list only as the cleanest test of the claim-and-refutation cycle. A standing claim here means "not yet reproduced", not "shown hard": the 2019 instance fell to a better algorithm, not to a bigger computer. The same standard is applied to `google-quantum-echoes-otoc-2025`, the only other Google instance still standing.
