---
type: application
id: homogeneous-catalysis
title: Homogeneous transition-metal catalyst design
title_zh: 均相过渡金属催化剂设计
summary: A nitrogen-fixation study compares DMRG and phase estimation for named Mo catalyst Hamiltonians. Its $200,000 utility is the authors' estimate inferred from research funding, not a buyer quote; roughly 400,000 DMRG core-hours are extrapolated. The 8,478-logical-qubit, 1.4e12-Toffoli estimate is for one constituent Hamiltonian, not the entire reaction.
summary_zh: 一项固氮研究比较了具名 Mo 催化剂哈密顿量的 DMRG 与量子相位估计。20 万美元是作者根据科研经费推算的价值，并非买方报价；约 40 万核小时是 DMRG 外推成本。8,478 个逻辑比特与 1.4e12 个 Toffoli 门对应其中一个哈密顿量，而非整条反应路径。
status: seed
last_verified: 2026-09-27
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "Bellonzi et al. measured small-bond-dimension block2 DMRG runs and extrapolated cost to chemical accuracy for larger Mo pincer active spaces. The full reaction was not run at the projected cost; improved orbital ordering and other classical methods remain possible."}
  quantum_easiness: {level: conditional, note: "Phase estimation is compiled for the same active-space Hamiltonians. For Mo-pincer intermediate I, CAS(101e,75o), the initial CSF overlap proxy from DMRG is 0.86; success and total cost remain conditional on the model and hardware."}
  willingness_to_pay: {level: second-hand, note: "The $100k-$200k per-reaction utility is the paper authors' heuristic based on public research grants and publication counts; no end-user quote, acceptance requirement or procurement decision is documented."}
resources: {logical_qubits: "8,478 for Mo-pincer intermediate I", gates: "1.4e12 Toffoli per shot for intermediate I", note: "Bellonzi et al. Table 4(c), large active space CAS(101e,75o); five shots listed for this Hamiltonian. The two-step reaction requires several different Hamiltonians."}
related:
  applications: [oled-emitters, p450-drug-metabolism, protein-ligand-binding]
  problems: [ground-state-energy, excited-states]
  methods: [phase-estimation, embedding-divide-and-conquer, sqd]
  questions: [dmrg-vs-qpe-cost-accuracy-oled, first-hand-payment-evidence]
references:
  - {arxiv: "2406.06335", title: "Feasibility of accelerating homogeneous catalyst discovery with fault-tolerant quantum computers", authors: "N. Bellonzi et al.", year: 2024, note: "Abstract; Tables 3, 4 and 6; Sections 5.2-5.3"}
  - {arxiv: "1605.03590", title: "Elucidating Reaction Mechanisms on Quantum Computers", authors: "M. Reiher et al.", year: 2016}
  - {arxiv: "2208.02199", title: "Is there evidence for exponential quantum advantage in quantum chemistry?", authors: "S. Lee et al.", year: 2022}
  - {arxiv: "2603.28648", title: "Hunting for quantum advantage in electronic structure calculations is a highly non-trivial task", authors: "Ö. Legeza et al.", year: 2026, note: "classical DMRG baseline for correlated Fe-S clusters"}
  - {arxiv: "2601.04621", title: "Classical computational simulation of the FeMo-cofactor model to chemical accuracy and its implications", authors: "H. Zhai et al.", year: 2026}
---

## Who needs it

Researchers and companies developing molecular catalysts must compare reaction pathways, selectivity and catalyst stability. A calculation of electronic energies may inform that choice, but geometry, solvent, thermal corrections, side reactions and turnover must also be considered. The cited nitrogen-fixation paper examines Mo-containing catalyst models for two steps leading from dinitrogen to cyanate [1]. It supplies named Hamiltonians and cost models; it does **not** identify a customer who agreed to buy those calculations at a stated price.

## Bottleneck

For the Mo-pincer reaction, the study ran block2 DMRG at limited bond dimensions and extrapolated the dimension needed to reach approximately chemical accuracy [1]. Its abstract reports roughly **400,000 CPU-hours as an estimate** for an equivalent DMRG calculation on the highest-utility task. Table 3 shows much cheaper runs actually executed: the large-active-space intermediate I, for example, used bond dimension 400 and 217.05 CPU-hours, with residual extrapolation uncertainty. The paper itself notes that orbital ordering, sweep schedules, active-space selection and post-DMRG corrections could alter the classical estimate [1]. A large difference between CCSD(T) and DMRG does not prove that an optimised DMRG calculation is intractable.

## Computational problems

- [Ground-state energies](../problems/ground-state-energy.html) for each intermediate and transition-state model, combined into reaction-energy or barrier differences.
- [Excited and competing spin states](../problems/excited-states.html) where the chosen catalytic pathway requires them.
- Geometry optimisation, solvent and free-energy corrections, which remain outside the active-space energy estimate.

## Best classical today

The direct same-model baseline in [1] is block2 DMRG plus an extrapolation in discarded weight and bond dimension. The most expensive projected case was **not** a 400,000-core-hour run. Classical alternatives and improvements must be checked against the same orbitals and target observable. Larger correlated transition-metal clusters continue to be attacked with DMRG [4, 5], so a fixed-orbital-count argument is insufficient evidence for advantage.

## Best quantum estimate

The study compiles double-factorised phase estimation for the named active-space Hamiltonians [1]. Its Table 4(c) assigns **8,478 logical qubits and 1.4 × 10¹² Toffoli gates per shot** to large-active-space Mo-pincer intermediate I, CAS(101e,75o), and lists five shots. Other intermediates and the transition state have separate costs. The estimated dominant-configuration-state-function overlap with the DMRG state is 0.86 for I; this is a model-specific overlap proxy obtained using a classical calculation. The abstract's **139,000 QPU-hours** is a hardware-model estimate for the highest-utility two-step task, not a measured QPU runtime.

## Does the calculation have a buyer?

The paper's $100,000–$200,000 per-reaction utility comes from dividing a public $25 million research grant by an expected 250 papers, then making assumptions about the number of reactions per paper [1, Section 5.2]. Research funding supports the scientific area, but this arithmetic does not establish how much a catalyst developer would pay for the specified electronic energies. The paper's separate $0.04 per CPU-hour assumption converts the projected 400,000 hours to **$16,000**. That excludes uncertainty in the DMRG extrapolation and is not a measured market price for the full chemistry workflow.

## Verdict

Surviving as a research and potential industrial application. This study is unusually useful because it names Hamiltonians and presents classical and quantum cost models for the same task. Its utility number is an author estimate, the most costly classical result is extrapolated, and the quantum runtime depends on a hypothetical fault-tolerant device. The willingness-to-pay rating is therefore second-hand. A stronger case needs a process owner's written target, a converged best-classical cost–accuracy curve on the same reaction observable, and a quantum estimate including the complete workflow.
