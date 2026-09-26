---
type: problem
id: excited-states
title: Excited-state energies of molecules (T1, S1, spin-orbit multiplets)
title_zh: 分子的激发态能量（T1、S1、自旋轨道多重态）
summary: Vertical and adiabatic excitation energies decide emitter colour, photocatalyst activity and spectroscopic assignment. The one documented case where a company states an accuracy target that classical methods miss is OLED phosphor T1 energies at 0.05 eV. Phase estimation reaches excited states under the same overlap precondition as ground states, and the guided problem is BQP-complete only at inverse-polynomial precision.
summary_zh: 垂直与绝热激发能决定发光体颜色、光催化剂活性和谱线归属。唯一有企业写下精度目标且经典方法达不到的案例，是 OLED 磷光体 T1 能量的 0.05 eV。相位估计在与基态相同的重叠前提下可以求激发态，而带引导态的激发态问题只在反多项式精度下是 BQP 完全的。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "guided excited-state problem BQP-complete at 1/poly precision but constant precision is dequantized; on 14 Ir/Pt phosphors TD-DFT gives 0.12–0.26 eV MAE and coupled cluster 0.22–0.29 eV against a 0.05 eV target"}
  quantum_easiness: {level: conditional, note: "phase estimation on an excited state needs a guiding state with overlap ≥ 1/poly with that state; spin-orbit coupling and multi-state tracking are untested at 70–100 orbitals"}
  willingness_to_pay: {level: first-hand, note: "OTI Lumionics and Samsung SAIT state a 0.05 eV T1 target in a co-authored paper (Genin et al. 2025)"}
resources: {logical_qubits: "140–200 system + ancillas", gates: "1e9–1e10 T", note: "CAS(70–100) phosphor active spaces with spin-orbit coupling; same phase-estimation cost model as ground-state energy, one extra eigenstate per target"}
related:
  applications: [oled-emitters, battery-cathode-spectroscopy, nuclear-fuel-actinide-spectra]
  problems: [ground-state-energy, linear-response-spectral-functions]
  methods: [phase-estimation, vqe]
  questions: [dmrg-vs-qpe-cost-accuracy-oled]
references:
  - {arxiv: "2512.13657", title: "Towards quantum advantage in chemistry", authors: "I. Genin, S. Kwon, M. Hosseini Jenab, et al., I. G. Ryabinkin, M. Helander", year: 2025, note: "OTI Lumionics / Samsung SAIT; 14 Ir/Pt phosphor T1 benchmark"}
  - {arxiv: "2207.10097", title: "Complexity of the Guided Local Hamiltonian Problem: Improved Parameters and Extension to Excited States", authors: "C. Cade, M. Folkertsma, J. Weggemans", year: 2022}
  - {arxiv: "2411.16163", title: "A Dequantized Algorithm for the Guided Local Hamiltonian Problem", authors: "Y. Zhang, Y. Wu, X. Yuan", year: 2024}
  - {arxiv: "2208.02199", title: "Evaluating the evidence for exponential quantum advantage in ground-state quantum chemistry", authors: "S. Lee, J. Lee, H. Zhai, Y. Tong, et al.", year: 2023}
  - {arxiv: "2603.19081", title: "Utility-scale quantum computational chemistry", authors: "S. Castaldo, M. Reiher", year: 2026}
---

## Best classical

- TD-DFT is the industrial default for excitation energies. On the 14 Ir and Pt phosphors benchmarked by OTI Lumionics and Samsung SAIT, TD-B3LYP gives a mean absolute error of 0.121 eV on T1 and CAM-B3LYP 0.256 eV; CCSD gives 0.220 eV and CR-CC(2,3) 0.291 eV, so adding correlation the single-reference way does not help [1]. The stated business requirement is 0.05 eV.
- Multireference methods (CASPT2, NEVPT2, DMRG with spin-orbit coupling) are the honest classical route. DMRG excited states with spin-orbit coupling on 70–100 orbital heavy-metal complexes are not yet routine, which is why the OLED benchmark reports only single-reference and DFT baselines [1].
- The iQCC+PT result that reaches 0.050 eV MAE on the same set was computed on GPUs, using a quantum-inspired ansatz at about 200 logical-qubit scale [1]. Read carefully, the paper is evidence that the target is reachable classically at that scale, not evidence that hardware is required.
- Castaldo and Reiher's survey of utility-scale chemistry lists no excited-state instance where the best classical estimate and the target accuracy are separated by more than the classical error bar [5].

## Best quantum

Excited states are reached by the same machinery as ground states: prepare a guiding state, run phase estimation on a block-encoded Hamiltonian, and post-select the eigenvalue window. Complexity theory supports this narrowly. Cade, Folkertsma and Weggemans extended the guided local Hamiltonian problem to excited states and showed it is BQP-complete when the guiding state has inverse-polynomial overlap with the target eigenstate and the precision is inverse-polynomial [2]. Zhang, Wu and Yuan then showed that at constant precision the same problem has a classical polynomial-time algorithm [3], so the advantage window is exactly the high-precision end, which is where a 0.05 eV target on a 10 eV spectrum sits.

The precondition is harder to satisfy than for ground states. Lee et al.'s argument that overlap decays with system size applies to each target state separately [4], and for a T1/S1 pair one needs a guiding state in the right spin and spatial symmetry sector, with spin-orbit coupling included in the Hamiltonian. Cost scales like ground-state phase estimation: for CAS(70–100) phosphors, roughly 140–200 system qubits and 10⁹–10¹⁰ T gates per eigenvalue, before the ancilla overhead of block encoding (numbers inherited from the ground-state page; no phosphor-specific fault-tolerant resource estimate has been published).

## What survives

Systems where the excited-state manifold is dense and multiconfigurational: heavy-metal phosphors with strong spin-orbit coupling, transition-metal L-edge and actinide 5f multiplets, and photocatalyst intermediates with several open shells. In each case the same features that defeat TD-DFT (near-degeneracy, spin-orbit mixing) also make the guiding-state problem harder, so the window must be established instance by instance, and the 0.05 eV OLED result on GPUs shows the classical side is still moving.

## Verdict

Surviving. Hardness is empirical, and the only first-hand accuracy target (0.05 eV for T1 in OLED emitters) was met in 2025 by a classical GPU calculation at 200-qubit scale [1]. The quantum precondition (overlap with a specific excited eigenstate, with spin-orbit coupling) is unverified for the cases that matter. What would move this page: a DMRG-with-SOC versus phase-estimation cost curve on a 70–100 orbital phosphor, reporting the guiding-state overlap for T1 and S1 after orbital optimisation, and a second industrial domain (cathode spectroscopy or actinide multiplets) that writes down an accuracy target.
