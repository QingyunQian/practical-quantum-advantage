---
type: application
id: battery-cathode-spectroscopy
title: Operando spectroscopy of battery cathodes (XAS, XPS, RIXS)
title_zh: 电池正极的 operando 谱学解读（XAS、XPS、RIXS）
summary: Whether capacity fade in high-nickel NMC and LiNiO2 is driven by Ni or by O 2p oxidation is read off operando X-ray spectra, and the interpretation now depends on DFT+DMFT plus charge-transfer multiplet calculations rather than rigid-band DFT+U. The 3d-oxide core-level problem maps to a 5-orbital impurity with full Coulomb vertex and spin–orbit coupling (60–100 qubits), but the value is in interpreting spectra, not in designing materials, and classical impurity solvers are improving fast.
summary_zh: 高镍 NMC 和 LiNiO2 的容量衰减到底是镍氧化还是氧 2p 氧化，是从 operando X 射线谱里读出来的，而这个解读现在依赖 DFT+DMFT 加电荷转移多重态计算，而不是刚性能带的 DFT+U。3d 氧化物的核能级问题对应一个带完整库仑顶点和自旋轨道耦合的 5 轨道杂质（60 到 100 个比特），但价值在于解释谱，而不是设计材料，而且经典杂质求解器进步很快。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "rigid-band DFT+U fails for delithiated LiNiO2/NMC (Xie et al. 2025); charge-transfer multiplet fits are semi-empirical; CT-HYB with full Coulomb vertex, spin–orbit coupling and a core hole at finite temperature has a sign problem; tensor-train and neural-network solvers are the moving classical frontier"}
  quantum_easiness: {level: heuristic, note: "impurity Green's function and core-level response by Trotter or Krylov methods; a 14-qubit DMFT loop on a cuprate has been run on IBM hardware (Selisko et al.); resolution and bath count push T counts to 1e9–1e12; no fault-tolerant estimate with a core hole"}
  willingness_to_pay: {level: second-hand, note: "battery makers and synchrotron beamlines run these measurements and fund interpretation, but the routine tools are DFT+U and multiplet fits; no company has stated a required accuracy for a computed spectrum"}
resources: {logical_qubits: "60–100", gates: "1e9–1e12 T (illustrative scenario, not a resource estimate)", note: "5-orbital d impurity + spin–orbit coupling with 4–8 bath sites per spin-orbital (50–90 qubits) plus core-hole multiplet; T count for ~100 fs evolution at 10 meV resolution; Ivanov et al. give 1e10–1e12 T for static ground states of 200–900 spin-orbital NiO/PdO cells"}
related:
  applications: [battery-electrolyte-design, rare-earth-permanent-magnets, nuclear-fuel-actinide-spectra]
  problems: [linear-response-spectral-functions, excited-states]
  methods: [dmft-impurity-solver, phase-estimation]
  questions: [dmft-impurity-cost-vs-ctqmc-sign-problem]
references:
  - {arxiv: "2510.02875", title: "Redox Chemistry of LiCoO$_2$, LiNiO$_2$, and LiNi$_{1/3}$Mn$_{1/3}$Co$_{1/3}$O$_2$ Cathodes: Deduced via XPS, DFT+DMFT, and Charge Transfer Multiplet Simulations", authors: "R. Xie, M. Mellin, T. Jaegermann, J. P. Hofmann, F. M. F. de Groot, H. Zhang", year: 2025, note: "shows delithiation is not rigid-band; paramagnetic insulating LiNiO2 needs DMFT"}
  - {arxiv: "1510.03859", title: "Hybrid quantum-classical approach to correlated materials", authors: "B. Bauer, D. Wecker, A. J. Millis, M. B. Hastings, M. Troyer", year: 2015}
  - {arxiv: "2404.09527", title: "Dynamical Mean Field Theory for Real Materials on a Quantum Computer", authors: "J. Selisko et al., I. Tavernelli, T. Eckl", year: 2024, note: "Ca2CuO2Cl2 DMFT loop with a 14-qubit impurity on IBM hardware"}
  - {arxiv: "2210.02403", title: "Quantum Computation for Periodic Solids in Second Quantization", authors: "A. V. Ivanov et al.", year: 2022, note: "1e10–1e12 T gates, up to 3e8 physical qubits, for 200–900 spin-orbital NiO/PdO"}
  - {arxiv: "2603.15741", title: "Neural-Network Quantum Embedding Solvers for Correlated Materials", authors: "A. Valenti, H. Park, A. Georges, A. J. Millis, O. Parcollet", year: 2026}
  - {arxiv: "2303.11199", title: "A Tensor Train Continuous Time Solver for Quantum Impurity Models", authors: "A. Erpenbeck et al., E. Gull", year: 2023}
---

## Who needs it

Cathode developers (LG Energy Solution, Samsung SDI, Umicore, BASF, CATL) and the synchrotron beamlines (SSRL, ALS, Diamond, SPring-8) that run operando X-ray absorption, photoemission and resonant inelastic scattering on cells during cycling. The decision is mechanistic: in high-nickel NMC and LiNiO2, is the capacity fade and oxygen release driven by Ni³⁺/Ni⁴⁺ redox or by oxidation of O 2p (ligand-hole) states? The answer determines whether to dope, coat or change the cut-off voltage, and it is read from spectra whose interpretation depends on a many-body calculation.

## Bottleneck

The routine interpretation tools are DFT+U projected densities of states for K edges and semi-empirical charge-transfer multiplet (CTM) fits for L edges. Both fail on the relevant question. Xie, de Groot, Zhang and co-workers combined XPS with DFT+DMFT and CTM simulations for LiCoO2, LiNiO2 and NMC111 and showed that delithiation is not a rigid-band process and that the paramagnetic insulating state of LiNiO2, which is what the cell contains at room temperature, is obtained only with DMFT [1]. The d⁸L ligand-hole configurations and multiplet satellites that distinguish Ni oxidation from O oxidation are precisely the features a single-particle picture cannot produce.

The many-body kernel is a 5-orbital 3d impurity with the full Coulomb vertex, spin–orbit coupling, a core hole for the spectroscopy, and finite temperature. Continuous-time hybridisation-expansion QMC handles parts of this, but the sign problem grows exponentially with spin–orbit coupling, off-diagonal hybridisation and decreasing temperature; NRG stops at about 3 orbitals; matrix-product-state solvers reach 3 orbitals at zero temperature. This is the region Bauer et al. identified in 2015 for a roughly 100-logical-qubit impurity solver [2].

The limit on value is that the output is an interpretation, not a design. A better spectrum assignment changes a hypothesis about degradation; the material decision still goes through synthesis and cycling.

## Computational problems

- [Linear response and spectral functions](../problems/linear-response-spectral-functions.html): the impurity Green's function inside DFT+DMFT, and the core-hole response for XAS/RIXS.
- [Excited states](../problems/excited-states.html): multiplet structure of d⁸L and d⁷ configurations with the core hole.

## Best classical today

DFT+U and CTM (Quanty, CTM4XAS) in industry; DFT+DMFT with CT-HYB in a few groups, temperature-limited when spin–orbit coupling matters. Two classical developments are eating into the sign-problem region: tensor-train CT-QMC evaluates the diagram sums deterministically without a sign problem [6], and neural-network impurity solvers trained on QMC data reach QMC accuracy orders of magnitude faster [5]. Neither yet covers a full 5-orbital plus core-hole problem at 300 K.

## Best quantum today

A DMFT loop on a real material (Ca2CuO2Cl2) with a 14-qubit impurity has been closed on IBM hardware [3]. The target impurity here needs 50–90 qubits (5 orbitals, spin–orbit, 4–8 bath sites per spin-orbital) plus the core-hole degrees of freedom, so 60–100 logical qubits. Evolving it for about 100 fs at 10 meV resolution costs 10^9–10^12 T gates per Green's function under the illustrative assumptions below. Both the bath discretisation and spectral resolution must be converged for the target model. For comparison, static ground states of 200–900 spin-orbital NiO/PdO cells were estimated at 10^10–10^12 T gates [4]. No fault-tolerant estimate that includes the core hole exists.

## Verdict

Surviving. The question is real and is asked by companies; the classical failure is specific (paramagnetic, spin–orbit-coupled, finite-temperature multiplet spectra); the kernel fits 100 logical qubits. Against it: the value is interpretive, the routine industrial tools are not even DMFT yet, classical solvers are advancing, and the gate count is 10^9–10^12 T, which is outside a five-year horizon. What would move it: a spectrum of delithiated LiNiO2 or NMC where DFT+DMFT with the best classical solver demonstrably cannot resolve the Ni-versus-O assignment, together with an end-to-end T-count for the 5-orbital impurity with core hole compared against tensor-train and neural-network solvers on the same hybridisation function.

## Resource-count assumptions

The gate range quoted here is a sensitivity calculation: assume 10²–10³ time steps, 10⁴–10⁵ compiled T gates per step and 10³–10⁴ repetitions of one measured circuit. Multiplying endpoints gives **10⁹–10¹² T gates**. These inputs are not calibrated for a named impurity or a target error. The range excludes state preparation, additional time points and Green's-function components, bath convergence and DMFT iterations, so it is not an end-to-end estimate or a hardware readiness claim. See the [impurity-solver page](../methods/dmft-impurity-solver.html) for the conditions that remain to be checked.
