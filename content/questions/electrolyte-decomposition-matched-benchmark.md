---
type: question
id: electrolyte-decomposition-matched-benchmark
title: Can an electrolyte reaction barrier yield a matched quantum and classical decision benchmark?
title_zh: 电解液反应势垒能否形成同实例的经典与量子决策基准？
summary: "A public EC decomposition study gives reaction energies and molecular coordinates, while a separate quantum paper estimates QPE resources for related electrolyte molecules. Can one barrier, its classical alternatives, quantum costs and formulation decision be compared on the same inputs?"
summary_zh: "公开的碳酸乙烯酯分解研究提供反应能与分子坐标，另一项量子研究估计了相关电解液分子的 QPE 资源。能否在同一组输入上比较势垒、经典替代方案、量子成本和实际配方决策？"
status: seed
last_verified: 2026-09-27
question:
  what_would_settle_it: "Choose one published EC ring-opening reactant and transition-state pair. Release versioned coordinates, charge/spin, basis, frozen-core and solvation conventions, orbital/integral files, and a script reproducing the reference barrier. Measure classical cost versus barrier error for calibrated DFT and converged DLPNO-CCSD(T), with canonical CCSD(T) where feasible. Estimate quantum state overlap, per-energy precision, repetitions, logical qubits, gates and wall time on those same Hamiltonians. Supply a documented formulation or mechanistic decision whose outcome changes within the residual classical uncertainty."
  difficulty: phd
  resolved: false
related:
  applications: [battery-electrolyte-design]
  problems: [ground-state-energy]
  methods: [phase-estimation]
  questions: [first-hand-payment-evidence]
references:
  - {doi: "10.1021/acs.jpca.3c04369", url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC10795021/", title: "Accurate Quantum Chemical Reaction Energies for Lithium-Mediated Electrolyte Decomposition and Evaluation of Density Functional Approximations", authors: "S. Debnath et al.", year: 2023, note: "EC barrier benchmark; supporting information supplies individual reaction energies and molecular coordinates"}
  - {arxiv: "2104.10653", title: "Fault-tolerant resource estimate for quantum chemical simulations: Case study on Li-ion battery electrolyte molecules", authors: "I. H. Kim et al.", year: 2022, note: "resource estimate for related molecules, not the same EC reaction-path Hamiltonians"}
---

## Why it matters

For one lithium-mediated ethylene-carbonate (EC) ring-opening step, tested DFT barriers span 3.01–17.15 kcal/mol; canonical CCSD(T) gives 12.84 kcal/mol [1]. This is a concrete electronic-structure accuracy problem. The same study also computes the path with classical correlated methods, so the DFT spread alone is no evidence of quantum advantage.

The electrolyte quantum resource paper estimates phase estimation for isolated EC, FEC, PF6- and Li-containing variants, with DFT-optimized geometries and 1 mHartree precision per total energy [2]. It does not compute the reactant and transition-state pair of [1]. The two studies therefore cannot yet be placed on one cost–accuracy curve. Neither reports a buyer's target or an electrolyte formulation ranking changed by a more accurate barrier.

## What would settle it

The front matter specifies the full comparison. A first milestone is a versioned input bundle for the EC reactant and transition state in [1], using the published supporting coordinates and enough method settings to regenerate their barrier. If the exact integrals or orbitals are unavailable, newly generated ones should be identified as a new benchmark rather than a reproduction.

On that bundle, report reaction-barrier error and *total* elapsed time for selected DFT functionals and converged classical correlated methods. A quantum estimate should use the same Hamiltonians and include both energy calculations, state preparation, precision allocation, repetition and error correction. A later application claim needs a documented decision that changes within the classical residual uncertainty. Without it, the result remains a useful computational benchmark rather than a demonstrated electrolyte-design application.
