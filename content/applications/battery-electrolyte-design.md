---
type: application
id: battery-electrolyte-design
title: Battery electrolyte and SEI design
title_zh: 电池电解液与 SEI 设计
summary: "Fault-tolerant resource estimates exist for battery electrolyte molecules, but a resource estimate does not establish an industrial advantage. This page asks whether a specific formulation decision needs electronic-structure accuracy beyond the best classical workflow, and whether its value would cover the quantum cost."
summary_zh: "电解液分子已有容错量子计算的资源估计，但资源估计本身不能证明产业优势。需要明确哪一项配方决策受限于经典方法的电子结构精度，以及改善这项决策的价值能否覆盖量子计算成本。"
status: seed
last_verified: 2026-09-26
verdict: uneconomic
dimensions:
  classical_hardness: {level: none, note: "closed-shell organic solvents and salts; DFT/DLPNO-CCSD(T) reach the accuracy the screening workflow uses; residual failures (SEI single-electron reduction potentials, anion redox) are self-interaction errors fixed by hybrid functionals or CCSD(T), not multireference character"}
  quantum_easiness: {level: conditional, note: "phase estimation applies and initial-state overlap is unproblematic for closed-shell molecules; the task is simply not hard enough to need it"}
  willingness_to_pay: {level: none, note: "the public references listed here do not give a buyer-defined accuracy target and payment threshold for a quantum electrolyte calculation"}
resources: {logical_qubits: "not the constraint", gates: "1e10–1e12 T per periodic-solid instance", note: "Ivanov et al. estimate 1e10–1e12 T gates for 200–900 spin-orbital NiO/PdO cells; per-molecule fault-tolerant estimates for electrolyte molecules exist (Kim et al.) but the same molecules are routine for DFT"}
related:
  applications: [battery-cathode-spectroscopy, oled-emitters]
  problems: [ground-state-energy]
  methods: [phase-estimation]
  questions: [first-hand-payment-evidence]
references:
  - {arxiv: "2104.10653", title: "Fault-tolerant resource estimate for quantum chemical simulations: Case study on Li-ion battery electrolyte molecules", authors: "I. H. Kim et al. (PsiQuantum)", year: 2021, note: "resource estimate for electrolyte molecules on a photonic fault-tolerant architecture"}
  - {arxiv: "2210.02403", title: "Quantum Computation for Periodic Solids in Second Quantization", authors: "A. V. Ivanov et al.", year: 2022, note: "1e10–1e12 T gates for 200–900 spin-orbital transition-metal-oxide cells"}
  - {arxiv: "2204.11890", title: "Simulating key properties of lithium-ion batteries with a fault-tolerant quantum computer", authors: "A. Delgado et al. (Xanadu)", year: 2022, note: "cathode-material resource estimate; illustrates the battery narrative"}
  - {arxiv: "2603.19081", title: "Utility-scale quantum computational chemistry", authors: "D. Castaldo, M. Reiher", year: 2026, note: "argues that value in chemistry comes from throughput, which classical wavefunction methods are narrowing"}
  - {arxiv: "2511.09124", title: "The Grand Challenge of Quantum Applications", authors: "R. Babbush et al. (Google Quantum AI)", year: 2025, note: "concedes that connecting chemistry resource estimates to a decision someone pays for is the missing step"}
---

## Who needs it

Cell makers and their materials suppliers (CATL, LG Energy Solution, Samsung SDI, Panasonic, BYD, and the solvent and salt vendors behind them). The engineering questions are which solvent and additive combination gives a stable solid-electrolyte interphase (SEI), a wide electrochemical window, adequate ionic conductivity at low temperature, and no gas evolution at high voltage. Candidate formulations are combinatorial: a handful of carbonate or ether solvents, one or two lithium salts, and a long list of additives at percent-level loadings.

## Bottleneck

Screening electrolytes involves both electronic-structure calculations and finite-temperature sampling. The resource studies [1–3] show how selected calculations might be performed on a fault-tolerant machine. They do not by themselves show that improved electronic energies would change a formulation decision or be worth the resulting runtime. That connection needs a public, application-specific benchmark.

For each proposed target, the relevant comparison is against a converged classical workflow at the accuracy required for that property. Errors from functional choice, sampling and solvation must be separated from the many-electron correlation error a quantum solver aims to reduce. A useful benchmark should state these error contributions explicitly.

Castaldo and Reiher make the general version of this argument: as classical wavefunction methods close the accuracy gap, any value quantum computers could add to chemistry has to come from high throughput, and a fault-tolerant machine running phase estimation at 10^10 T gates per energy is the opposite of high throughput [4]. Google's own applications review concedes that connecting a chemistry resource estimate to a decision a buyer will pay for is the step nobody has completed [5].

## Computational problems

- [Ground-state energy](../problems/ground-state-energy.html) of closed-shell organic molecules and ion–solvent clusters, needed to about 1 kcal/mol for potentials and barriers, which DFT with a good functional and DLPNO-CCSD(T) already provide.
- Finite-temperature sampling of the liquid and of SEI growth, which is a classical molecular-dynamics problem and not a quantum-computing target.

## Best classical today

DFT (usually a range-separated hybrid with implicit solvation) for screening; DLPNO-CCSD(T) for benchmarks on molecules of 50–100 atoms; machine-learned potentials trained on DFT for the liquid-state properties. Fault-tolerant resource estimates exist for exactly the molecules in this workflow: PsiQuantum estimated the cost of simulating Li-ion electrolyte molecules on a photonic fault-tolerant architecture [1], Xanadu did the same for a cathode material [3], and Ivanov et al. estimate 10^10–10^12 T gates for periodic transition-metal-oxide cells of 200–900 spin-orbitals [2]. These estimates describe a machine that would reproduce, at large cost, numbers the screening pipeline already trusts.

## Verdict

Uneconomic under the cost assumptions used in this seed assessment. The cited resource studies do not establish a cost advantage over the classical screening workflow or document a buyer-defined value for extra accuracy. Evidence that would reopen this verdict is a public target for a named electrolyte property, a failure of the best classical approach at that target, and a quantum cost estimate on the same instance.