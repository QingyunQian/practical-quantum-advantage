---
type: problem
id: ground-state-energy
title: Ground-state energy of molecules and materials
title_zh: 分子与材料的基态能量
summary: The canonical quantum-chemistry task. Quantum phase estimation gives it in polynomial time only if a good initial state is available; classical DMRG, SHCI and AFQMC now reach chemical accuracy on the FeMoco model, so the surviving window is systems with 100–200 highly entangled orbitals whose answer someone pays for.
summary_zh: 量子化学的核心任务。量子相位估计只有在初始态足够好时才是多项式时间；经典 DMRG、SHCI、AFQMC 已经把 FeMoco 模型算到化学精度，所以剩下的窗口是 100 到 200 个高纠缠轨道且答案有人买单的体系。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "QMA-hard in general, but the worst case is not the chemical case; FeMoco model solved classically to chemical accuracy in 2026; DMRG/SHCI routine to ~100 orbitals"}
  quantum_easiness: {level: conditional, note: "phase estimation needs overlap ≥ 1/poly with the true ground state; Lee et al. argue exponential advantage is not generically expected; no guarantee for strongly correlated cases"}
  willingness_to_pay: {level: first-hand, note: "only via specific applications: industrial co-authors studied OLED emitters but did not state a 0.05 eV buyer threshold; catalyst partners assigned the top studied case a $200k utility value"}
resources: {logical_qubits: "100–200 system + ancillas", gates: "1e9–1e12 Toffoli", note: "double-factorised or THC phase estimation; FeMoco-class instances need ~1e12 Toffoli"}
related:
  applications: [oled-emitters]
  methods: [phase-estimation, sqd]
  claims: [ibm-sqd-2024]
  questions: [ideal-sqd-vs-classical-selection]
references:
  - {arxiv: "2208.02199", title: "Is there evidence for exponential quantum advantage in quantum chemistry?", authors: "S. Lee, J. Lee, H. Zhai, Y. Tong, et al.", year: 2023, note: "published as Nat. Commun. 14, 1952 (2023), 'Evaluating the evidence for exponential quantum advantage in ground-state quantum chemistry'"}
  - {arxiv: "2601.04621", title: "Classical computational simulation of the FeMo-cofactor model to chemical accuracy and its implications", authors: "H. Zhai, Z. Li, et al., G. K.-L. Chan", year: 2026}
  - {arxiv: "2406.06335", title: "Feasibility of accelerating homogeneous catalyst discovery with fault-tolerant quantum computers", authors: "N. Bellonzi et al.", year: 2024}
  - {arxiv: "2603.28648", title: "Hunting for quantum advantage in electronic structure calculations is a highly non-trivial task", authors: "Ö. Legeza et al.", year: 2026}
---

## Best classical

- DMRG: routine chemical accuracy up to about 100 orbitals; GPU implementations have reached CAS(89,102) on Fe–S clusters [4]. The FeMoco active-space model that motivated early quantum resource estimates was solved to chemical accuracy in 2026 with DMRG at bond dimension 18,000 and about 2.8 million core-hours [2].
- SHCI / HCI: competitive to ~100 orbitals when the wavefunction is sparse in the determinant basis.
- AFQMC: scales polynomially but with a phase problem controlled by the trial state; error is non-monotonic in trial quality.
- Cost reference: Zapata's industrial case study prices a DMRG calculation on a Mo nitrogen-fixation catalyst at about 400,000 CPU-hours (roughly $16k at $0.04/core-hour) against a stated business value of $200k [3].

## Best quantum

Quantum phase estimation on a block-encoded Hamiltonian (double-factorised or tensor-hypercontracted). Cost scales polynomially in orbitals and 1/ε **given** an initial state with overlap ≥ 1/poly. Resource estimates for FeMoco-class instances are order 10³ logical qubits (after ancillas) and 10¹² Toffoli [3]. The published 70–100 orbital OLED active spaces require 140–200 system qubits, but a compiled, same-Hamiltonian phase-estimation cost for those emitters is not available.

Lee et al. argue that exponential advantage is not generically expected, because the same physics (locality, gaps) that makes the initial state good also makes classical heuristics work [1].

## What survives

Systems with correlation length short enough to be cut out by embedding but with very high local entanglement: several open-shell d/f centres within a few ångströms (FeMoco-like clusters, P450 heme, Fe–S clusters), and spin defects in semiconductors. These fragments have 50–120 orbitals, which is also where DMRG and SHCI are strongest, so the advantage window, if any, is narrow and must be established instance by instance.

## Verdict

Surviving. Hardness is empirical and shrinking every year; the quantum precondition (overlap) is unverified for exactly the strongly correlated cases that would matter; and willingness to pay exists only through specific applications. The evidence that would settle it is a cost–accuracy curve of DMRG, SHCI and early fault-tolerant phase estimation on the same 100–200 orbital instance, with DMRG bond-dimension growth and AFQMC phase-bias reported after orbital optimisation.
