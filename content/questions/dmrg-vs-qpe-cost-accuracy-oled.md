---
type: question
id: dmrg-vs-qpe-cost-accuracy-oled
title: Same-instance classical and quantum cost–accuracy curve for an OLED emitter
title_zh: 对同一 OLED 发光体测量经典与量子计算的成本和误差
summary: The published 14-emitter benchmark already reaches 0.0501 eV mean absolute error on classical processors. For one public, decision-relevant emitter Hamiltonian, can a fault-tolerant quantum algorithm beat the best classical workflow at the same accuracy and total cost? No such comparison is reported for the named emitters, and no buyer-defined acceptance threshold is documented.
summary_zh: 已发表的 14 个发光体基准在经典处理器上达到 0.0501 eV 平均绝对误差。对于一个公开、与实际决策有关的发光体哈密顿量，容错量子算法能否在相同精度和完整成本下超过最强经典流程？现有论文没有这样的同实例比较，也没有给出买方验收门槛。
status: seed
last_verified: 2026-09-27
question:
  what_would_settle_it: "Publish one emitter's geometry, basis, orbitals, integrals and observable definition. At several accuracy levels, compare measured wall time and hardware cost for the best classical methods (including iQCC+PT and whichever of CC, DMRG, SHCI and AFQMC is competitive) against a compiled fault-tolerant quantum algorithm on that same Hamiltonian. Include preparation overlap, repetitions, ancillas, logical gates, and state/geometry error. Obtain a buyer's written accuracy, throughput or price target. Report the full cost–error Pareto curves and all missing inputs."
  difficulty: phd
  resolved: false
related:
  applications: [oled-emitters]
  problems: [ground-state-energy, excited-states]
  methods: [phase-estimation]
  questions: [first-hand-payment-evidence]
references:
  - {arxiv: "2512.13657", title: "Towards Quantum Advantage in Chemistry", authors: "S. N. Genin, O. Kwon et al.", year: 2026, note: "v2, Table 2 and Supplementary Tables SI.1-2, SI.2-2, SI.3-1"}
  - {arxiv: "2208.02199", title: "Is there evidence for exponential quantum advantage in quantum chemistry?", authors: "S. Lee et al.", year: 2023}
  - {arxiv: "2111.04169", title: "Estimating Phosphorescent Emission Energies in Ir(III) Complexes using Large-Scale Quantum Computing Simulations", authors: "S. N. Genin et al.", year: 2022, note: "nine Ir emitters at CAS(36,36), or 72 active-space qubits; classical iQCC+PT and DFT comparison"}
---

## Why it matters

An OLED emitter is an industrially meaningful molecule, but the published Ir/Pt set does not establish a quantum advantage. OTI Lumionics and Samsung SAIT used classical processors to emulate iQCC+PT and obtained a 0.0501 eV mean absolute error on 14 measured T1-to-S0 emission gaps [1]. The paper's 0.05 eV is an **observed cohort error**, not a written buyer threshold. The authors regard these molecules as predominantly single-reference and classically tractable up to CAS(100,100) [1]. Thus a DMRG-only baseline would be incomplete; the group's own classical iQCC implementation must also be beaten.

Our [reanalysis script](https://github.com/yuchenguommm/practical-quantum-advantage/blob/main/numerics/oled_genin_benchmark.py) transcribes the public supplementary gaps and recomputes the five reported method errors. It does not run an electronic-structure solver. On Q1, the measured gap is 1.974 eV and iQCC+PT at the benchmark active space gives 1.988 eV, a 0.014 eV error. Q1's CAS(70,70) **singlet solver alone** took 107.10 hours; CAS(100,100) took 199.37 hours [1]. These timings are not the full gap cost. The paper gives no same-Hamiltonian quantum phase-estimation estimate, and the geometry and integral files needed for an independent solver comparison are not provided in the tables we used.

## What is known

| Evidence | Result | What it does not establish |
|---|---|---|
| 14-compound classical iQCC+PT [1] | Reported MAE 0.0501 eV | A buyer's acceptance threshold or quantum advantage |
| Q1 classical iQCC+PT [1] | 0.014 eV absolute gap error at benchmark active space | Error on an unseen emitter or total screening throughput |
| Q1 classical iQCC timing [1] | 107.10 h for one CAS(70,70) singlet solver run | Full S0/T1 workflow time or quantum crossover |
| Q1 CAS(100,100) [1] | 199.37 h for one singlet solver run | A hard correlated state; the authors' diagnostics favour a single-reference picture |

Supplementary Table SI.3-1 lists an active-space sweep for Q1's uncorrected iQCC gap, while Table SI.2-2 gives the **singlet-state solver** times on the same named molecule [1]. The [reanalysis data](https://github.com/yuchenguommm/practical-quantum-advantage/blob/main/numerics/results/oled_genin2026_reanalysis.json) combine those reported quantities without calling the result a full cost–error curve:

| Q1 active space | System qubits | SI.3-1 gap (eV) | Absolute gap error (eV) | Singlet solver (h) |
|---|---:|---:|---:|---:|
| CAS(50,50) | 100 | 1.999 | 0.025 | 87.02 |
| CAS(70,70) | 140 | 1.988 | 0.014 | 107.10 |
| CAS(100,100) | 200 | 1.932 | 0.042 | 199.37 |

The 100-system-qubit row is a concrete starting point for a near-term experiment. Those 100 qubits exclude ancillas and error correction; the 87.02 hours exclude the triplet solver, Hamiltonian generation and other workflow costs. The errors are non-monotone with active-space size. Table SI.1-2 also reports 1.982 eV for the benchmark's uncorrected Q1 iQCC result, rather than SI.3-1's 1.988 eV at CAS(70,70). That discrepancy needs clarification before joining the sweep to the 14-emitter benchmark. We have kept the two series separate in the figure.

A smaller alternative is the earlier nine-complex Ir benchmark at CAS(36,36), which maps to 72 active-space qubits [3]. Its iQCC+PT and fine-tuned DFT mean absolute deviations were 0.201 and 0.192 eV, respectively [3, Table 1]. A 72-qubit demonstration would still need to beat a measured classical baseline on the same molecular Hamiltonian; reproducing the already classically simulated circuit would only verify implementation. The older cohort has different molecules and methods, so its accuracy figures cannot be combined with Q1's active-space sweep.

## What would settle it

The front matter states the full benchmark. Start by obtaining public geometry, basis, selected orbitals and Hamiltonian for one emitter. Reproduce the reported classical result and measure the full S0/T1 workflow time, then test the strongest competing classical solvers on the same instance and accuracy. Only then compile phase estimation or another fault-tolerant method for that Hamiltonian, including state preparation, repeated runs and error correction. Display cost versus error for both approaches and add a written buyer requirement. The current evidence does not support an arbitrary 0.05 eV crossover line or a universal T-gate budget.
