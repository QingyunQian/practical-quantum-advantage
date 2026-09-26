---
type: application
id: oled-emitters
title: OLED phosphorescent and TADF emitters
title_zh: OLED 磷光与 TADF 发光体
summary: Designing blue OLED emitters requires excitation energies (T1, S1–T1 gap) to about 0.05 eV; display makers have co-authored studies stating this target, and the decisive active spaces (70–100 orbitals) sit beyond routine classical accuracy. The strongest "someone pays" case found in chemistry.
summary_zh: 蓝光 OLED 发光体的设计需要把激发能算到约 0.05 eV，显示厂商在合作论文里明确写出了这个目标；决定性的活性空间（70 到 100 轨道）超出了经典方法的常规精度。这是化学领域里“有人付费”证据最强的案例。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "DFT/TD-DFT errors of 0.1–0.3 eV on Ir/Pt phosphors and multi-resonance TADF; CASPT2/DMRG feasible but not routine at 70–100 orbitals"}
  quantum_easiness: {level: conditional, note: "phase estimation needs initial-state overlap; closed-shell-like emitters likely fine, open-shell metal centres unverified"}
  willingness_to_pay: {level: first-hand, note: "OTI Lumionics and Samsung SAIT co-authored a target of ~0.05 eV on emission energies; Mitsubishi Chemical and JSR fund quantum-chemistry programmes"}
resources: {logical_qubits: "140–200", gates: "~1e9–1e10 T", note: "CAS(70–100) with double-factorised phase estimation; needs ~1000 logical qubits after ancillas and distillation"}
related:
  problems: [ground-state-energy, excited-states]
  methods: [phase-estimation]
references:
  - {arxiv: "2512.13657", title: "Towards quantum advantage in chemistry", authors: "I. Genin et al. (OTI Lumionics, Samsung SAIT)", year: 2025, note: "buyer-stated accuracy target"}
  - {arxiv: "2406.06335", title: "Feasibility of accelerating homogeneous catalyst discovery with fault-tolerant quantum computers", authors: "N. Bellonzi et al.", year: 2024, note: "comparable resource-vs-value methodology for catalysis"}
---

## Who needs it

Display makers (Samsung, LG, BOE) and emitter suppliers (Universal Display, Idemitsu, Kyulux, OTI Lumionics, Mitsubishi Chemical, JSR). The open engineering problem is a stable, efficient deep-blue emitter; red and green phosphors have been solved for a decade. Candidate molecules are Ir/Pt phosphors and multi-resonance TADF organics, screened by synthesis at a cost of weeks per compound.

## Bottleneck

Screening is limited by the accuracy of computed excitation energies. The quantities that decide whether a molecule is worth synthesising are the T1 energy (colour), the S1–T1 gap (reverse intersystem crossing rate for TADF) and spin–orbit coupling. Time-dependent DFT gets these to 0.1–0.3 eV, which is not enough to rank candidates whose emission differs by 0.05 eV. OTI Lumionics and Samsung SAIT state the target as roughly 0.05 eV on emission energies and identify active spaces of 70–100 orbitals as the relevant size [1].

Unlike battery electrolytes, where practitioners say DFT accuracy suffices and speed is the bottleneck, here accuracy is the bottleneck and each false positive costs a synthesis.

## Computational problems

- [Ground-state energy](../problems/ground-state-energy.html) of the T1 state (lowest triplet is a ground state in its spin sector).
- [Excited states](../problems/excited-states.html): S1 and higher triplets for the singlet–triplet gap.
- Spin–orbit coupling matrix elements between them (not separately catalogued).

## Best classical today

TD-DFT with tuned range-separated functionals for screening; CASPT2, DMRG or DLPNO-STEOM on a few hundred candidates per year. Multi-resonance TADF emitters are notoriously hard for TD-DFT (double-excitation character), which is exactly where a 70–100 orbital CAS treatment is proposed.

## Verdict

Surviving, not promising. The buyer and the accuracy target are real and written down, and the active spaces are at the edge of routine classical accuracy. What is missing is (a) evidence that DMRG or SHCI cannot reach 0.05 eV on these specific emitters at 70–100 orbitals, and (b) a demonstration that phase estimation's initial-state overlap is adequate for Ir/Pt centres. The resource estimate (order 1000 logical qubits with overheads) puts a demonstration beyond a five-year, 100-logical-qubit horizon. A cost–accuracy curve of DMRG vs early fault-tolerant phase estimation on one named emitter would move this to promising or to no-go.
