---
type: application
id: rare-earth-permanent-magnets
title: Rare-earth permanent magnets (Ce-for-Nd substitution)
title_zh: 稀土永磁（以 Ce 替代 Nd）
summary: Whether cheap cerium can replace neodymium in Nd2Fe14B-type magnets hinges on the 4f shell's crystal-field anisotropy and its Kondo screening, a genuine dynamical impurity problem. Japan's ESICMM programme treats the 4f shell in the Hubbard-I atomic limit to avoid solving it. A 7-orbital f impurity with 3–6 bath sites per spin-orbital fits in 56–98 qubits, but the industrial pull is weak, since demand has shifted toward rare-earth-free magnets and coercivity is set by microstructure.
summary_zh: 便宜的铈能否替代 Nd2Fe14B 类磁体中的钕，取决于 4f 壳层的晶体场各向异性及其近藤屏蔽，这是一个真正的动态杂质问题。日本的 ESICMM 计划用 Hubbard-I 原子极限处理 4f 壳层，绕开了这个求解。7 轨道 f 杂质加每个自旋轨道 3 到 6 个 bath 位点需要 56 到 98 个比特，但产业拉力偏弱：需求已经转向无稀土磁体，而矫顽力由微结构决定。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "CT-HYB sign problem grows exponentially with spin–orbit coupling, off-diagonal hybridisation and low temperature; a 7-orbital f shell with dynamics is beyond routine solvers, which is why Hubbard-I is used; tensor-train CT-QMC and neural-network solvers are closing part of the gap"}
  quantum_easiness: {level: heuristic, note: "impurity Green's function by Trotterised evolution or quantum Krylov/Arnoldi; bath discretisation and 10 meV resolution push T counts to 1e9–1e12; no end-to-end fault-tolerant estimate for an f-shell impurity exists"}
  willingness_to_pay: {level: second-hand, note: "ESICMM (with Toyota) and magnet makers fund 4f crystal-field calculations, but no written accuracy target; industry demand has moved toward rare-earth-free 3d magnets"}
resources: {logical_qubits: "56–98", gates: "1e9–1e12 T (illustrative scenario, not a resource estimate)", note: "7-orbital f impurity with 3–6 bath sites per spin-orbital; T count from 1e2–1e3 Trotter steps × 1e4–1e5 non-Clifford gates × 1e3–1e4 Hadamard-test samples for ~100 fs evolution at 10 meV resolution; Krylov methods may cut this by orders of magnitude"}
related:
  applications: [battery-cathode-spectroscopy, nuclear-fuel-actinide-spectra]
  problems: [linear-response-spectral-functions, ground-state-energy]
  methods: [dmft-impurity-solver, embedding-divide-and-conquer]
  questions: [dmft-impurity-cost-vs-ctqmc-sign-problem]
references:
  - {arxiv: "1705.08027", title: "Crystal field splittings in rare earth-based hard magnets: an ab initio approach", authors: "P. Delange, S. Biermann, T. Miyake, L. Pourovskii", year: 2017, note: "DFT+Hubbard-I crystal-field parameters for Nd2Fe14B-type magnets; the ESICMM approach"}
  - {arxiv: "1510.03859", title: "Hybrid quantum-classical approach to correlated materials", authors: "B. Bauer, D. Wecker, A. J. Millis, M. B. Hastings, M. Troyer", year: 2015, note: "origin of the ~100-logical-qubit DMFT impurity solver proposal"}
  - {arxiv: "2605.22920", title: "Estimating Green's functions with a robust quantum Arnoldi method", authors: "J. S. Nelson, A. B. Baczewski (Sandia)", year: 2026, note: "ROQAM: orders of magnitude cheaper than point-by-point QSVT for Green's functions"}
  - {arxiv: "2303.11199", title: "A Tensor Train Continuous Time Solver for Quantum Impurity Models", authors: "A. Erpenbeck et al., E. Gull", year: 2023, note: "sign-problem-free deterministic summation; the main classical competitor"}
  - {arxiv: "2603.15741", title: "Neural-Network Quantum Embedding Solvers for Correlated Materials", authors: "A. Valenti, H. Park, A. Georges, A. J. Millis, O. Parcollet", year: 2026, note: "learned impurity solvers at QMC accuracy, orders of magnitude faster"}
---

## Who needs it

Magnet makers (Hitachi Metals/Proterial, Shin-Etsu, TDK, JL MAG) and their customers in traction motors and wind turbines (Toyota, Nidec, Siemens Gamesa). Nd2Fe14B magnets consume neodymium and dysprosium whose prices are volatile and supply concentrated. The question with a price attached is whether the abundant, cheap cerium (a by-product of Nd mining) can replace part of the Nd without losing the uniaxial anisotropy that gives the magnet its coercivity. Japan's Elements Strategy Initiative Center for Magnetic Materials (ESICMM, with Toyota involvement) has run a decade-long programme on exactly this.

## Bottleneck

The intrinsic anisotropy comes from the 4f shell's crystal-field splitting in the Fe sublattice's exchange field. DFT+U and self-interaction-corrected functionals get Hund's rules and the anisotropy sign wrong for open 4f shells. The working method, developed by Delange, Biermann, Miyake and Pourovskii, is DFT plus the Hubbard-I approximation: the 4f shell is treated in the atomic limit, with the crystal field extracted from the DFT hybridisation [1]. It works because Nd's 4f³ shell is well localised. The method breaks down where it matters for the substitution question: Ce 4f¹ is mixed-valent and Kondo-screened by the Fe conduction band, so its anisotropy contribution is intrinsically weak and temperature-dependent, and it cannot be described in an atomic limit. Predicting how much Ce can be tolerated at a given operating temperature therefore requires the dynamical solution of a 7-orbital f impurity with spin–orbit coupling and low-temperature hybridisation, which is where CT-HYB's sign problem grows exponentially. ESICMM's choice of Hubbard-I is a deliberate way around a solver that does not exist.

Two caveats limit the value of solving it. First, coercivity in a real magnet is a fraction of the anisotropy field and is set by grain boundaries and microstructure, so an exact intrinsic anisotropy improves one input to a multiscale model. Second, the industrial demand has partly moved on: Bosch, Toyota and ARPA-E programmes now target rare-earth-free 3d magnets, for which the DFT errors are ordinary exchange-correlation errors rather than f-shell dynamics.

## Computational problems

- [Linear response and spectral functions](../problems/linear-response-spectral-functions.html): the 4f impurity Green's function inside a DFT+DMFT loop, at 10 meV resolution for crystal-field levels.
- [Ground-state energy](../problems/ground-state-energy.html) of the impurity multiplet as a sub-step.

## Best classical today

DFT+Hubbard-I for localised 4f (Nd, Sm, Dy); CT-HYB where spin–orbit and off-diagonal hybridisation are weak and temperature is not too low. The classical competitors closing in on the sign-problem region are tensor-train CT-QMC, which sums diagrams deterministically without a sign problem [4], and neural-network impurity solvers trained to QMC accuracy at orders-of-magnitude lower cost [5]. Neither has been shown on a full 7-orbital f shell with spin–orbit coupling at the temperatures of interest.

## Best quantum today

The DMFT impurity solver on about 100 logical qubits was proposed by Bauer et al. in 2015 [2]. A 7-orbital f impurity with 3–6 bath sites per spin-orbital needs 56–98 qubits, which is the one dynamical problem whose kernel fits a 100-logical-qubit machine. The cost is in gates: 10^2–10^3 Trotter steps, 10^4–10^5 non-Clifford gates each and 10^3–10^4 Hadamard-test samples give 10^9–10^12 T gates per Green's function at 10 meV resolution, before the DMFT self-consistency loop. Quantum Krylov and Arnoldi methods such as ROQAM reduce the cost by orders of magnitude relative to point-by-point QSVT [3]. No end-to-end fault-tolerant estimate for an f-shell impurity has been published; a quantum solver also removes only the solver error, not the embedding error (U, double counting, single-site approximation), which is usually larger.

## Verdict

Surviving. This is the dynamical scenario with the clearest decision attached (how much Ce, at what temperature) and the cleanest classical failure (a 7-orbital f impurity that the working programme avoids solving). The qubit count fits; the gate count does not fit a five-year horizon, and the industrial pull is second-hand and weakening as buyers shift to rare-earth-free compositions. What would move it to promising: a written statement from a magnet maker or ESICMM that the Ce anisotropy at operating temperature is the quantity blocking a composition decision, and an end-to-end T-count for the 7-orbital impurity compared against tensor-train and neural-network solvers on the same hybridisation function.

## Resource-count assumptions

The gate range quoted here is a sensitivity calculation: assume 10²–10³ time steps, 10⁴–10⁵ compiled T gates per step and 10³–10⁴ repetitions of one measured circuit. Multiplying endpoints gives **10⁹–10¹² T gates**. These inputs are not calibrated for a named impurity or a target error. The range excludes state preparation, additional time points and Green's-function components, bath convergence and DMFT iterations, so it is not an end-to-end estimate or a hardware readiness claim. See the [impurity-solver page](../methods/dmft-impurity-solver.html) for the conditions that remain to be checked.
