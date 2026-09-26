---
type: problem
id: excited-states
title: Excited-state energies of molecules (T1, S1, spin-orbit multiplets)
title_zh: 分子的激发态能量（T1、S1、自旋轨道多重态）
summary: Vertical and adiabatic excitation energies inform emitter colour, photocatalyst activity and spectroscopy. In a 14-emitter OLED benchmark, classical iQCC+PT reached 0.0501 eV mean absolute error on T1-to-S0 gaps; no buyer acceptance threshold or hard instance was established. Guided excited-state estimation has a conditional BQP-completeness result at inverse-polynomial precision, but its assumptions need checking on each molecule.
summary_zh: 垂直与绝热激发能用于判断发光体颜色、光催化活性和谱线归属。在 14 个 OLED 发光体的基准中，经典 iQCC+PT 对 T1 到 S0 能隙达到 0.0501 eV 平均误差；论文没有确立买方验收门槛或经典难例。带引导态的激发态估计在反多项式精度下有条件性的 BQP 完全性结果，前提仍需在具体分子上核对。
status: seed
last_verified: 2026-09-27
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "guided excited-state problem BQP-complete at 1/poly precision but constant precision has classical algorithms; the published 14 Ir/Pt phosphors are classically tractable at 0.0501 eV cohort MAE"}
  quantum_easiness: {level: conditional, note: "phase estimation on an excited state needs a guiding state with overlap ≥ 1/poly with that state; spin-orbit coupling and multi-state tracking are untested at 70–100 orbitals"}
  willingness_to_pay: {level: first-hand, note: "OTI Lumionics and Samsung SAIT co-authored an industrial benchmark; their achieved 0.0501 eV MAE is not a written buyer target"}
resources: {logical_qubits: "140–200 system qubits in the published CAS examples", note: "No same-instance fault-tolerant gate count, overlap or total logical-qubit count has been reported for these emitters"}
related:
  applications: [oled-emitters, battery-cathode-spectroscopy, nuclear-fuel-actinide-spectra]
  problems: [ground-state-energy, linear-response-spectral-functions]
  methods: [phase-estimation, vqe]
  questions: [dmrg-vs-qpe-cost-accuracy-oled]
references:
  - {arxiv: "2512.13657", title: "Towards Quantum Advantage in Chemistry", authors: "S. N. Genin, O. Kwon et al.", year: 2026, note: "v2; OTI Lumionics / Samsung SAIT; 14 Ir/Pt phosphor benchmark"}
  - {arxiv: "2207.10097", title: "Complexity of the Guided Local Hamiltonian Problem: Improved Parameters and Extension to Excited States", authors: "C. Cade, M. Folkertsma, J. Weggemans", year: 2022}
  - {arxiv: "2411.16163", title: "A Dequantized Algorithm for the Guided Local Hamiltonian Problem", authors: "Y. Zhang, Y. Wu, X. Yuan", year: 2024}
  - {arxiv: "2208.02199", title: "Evaluating the evidence for exponential quantum advantage in ground-state quantum chemistry", authors: "S. Lee, J. Lee, H. Zhai, Y. Tong, et al.", year: 2023}
  - {arxiv: "2603.19081", title: "Utility-scale quantum computational chemistry", authors: "S. Castaldo, M. Reiher", year: 2026}
---

## Best classical

- TD-DFT is commonly used for excitation energies. On the 14 Ir and Pt phosphors benchmarked by OTI Lumionics and Samsung SAIT, TD-B3LYP gives a mean absolute error of 0.121 eV on the T1-to-S0 gap and TD-CAM-B3LYP 0.256 eV; CCSD gives 0.220 eV and CR-CC(2,3) 0.291 eV [1]. These figures compare specific methods on one cohort; they do not establish a buyer's required accuracy.
- The iQCC+PT result that reaches 0.0501 eV MAE on the same set was computed on classical processors using an ansatz with an abstract quantum-circuit equivalent [1]. The paper's own diagnostics describe the studied molecules as predominantly single-reference. DMRG, SHCI and AFQMC are possible challenger baselines on a future hard molecule but were not costed on this exact cohort.
- Castaldo and Reiher's survey of utility-scale chemistry lists no excited-state instance where the best classical estimate and the target accuracy are separated by more than the classical error bar [5].

## Best quantum

Excited states can be estimated by preparing a guiding state, running phase estimation on a block-encoded Hamiltonian, and selecting the desired eigenvalue window. Complexity theory supports this narrowly. Cade, Folkertsma and Weggemans extended the guided local Hamiltonian problem to excited states and showed it is BQP-complete under specified inverse-polynomial overlap and precision conditions [2]. Zhang, Wu and Yuan gave a classical algorithm for a constant-precision regime [3]. Neither result classifies the cost of the published OLED benchmark without mapping its Hamiltonian normalization, observable and accuracy to the theorem's parameters.

The overlap precondition must be checked for each target state separately. For T1 or S1 one needs to define the appropriate state and symmetry sector; spin-orbit effects may alter the physical observable. The published active spaces have 140–200 system qubits, but no named-emitter phase-estimation gate count, overlap bound or total logical count has been established [1].

## What survives

Systems where the excited-state manifold is dense and multiconfigurational may remain interesting: other heavy-metal phosphors, transition-metal L-edge and actinide 5f multiplets, and photocatalyst intermediates with several open shells. The same features that challenge classical approximations can also make guiding-state preparation harder. The present Ir/Pt cohort supplies an industrial case and a classical benchmark, not a hard quantum instance [1].

## Verdict

Surviving as a broad computational problem. The published OLED cohort was solved to 0.0501 eV cohort MAE classically, and its buyer-defined tolerance is unknown [1]. The quantum overlap and cost preconditions are unverified for a hard, useful molecule. What would move this page is a same-Hamiltonian cost–error comparison with the strongest classical solver and an independently documented accuracy or throughput requirement.
