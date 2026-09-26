---
type: application
id: nuclear-fuel-actinide-spectra
title: Actinide 5f spectra of nuclear fuels and waste forms (UO2, PuO2)
title_zh: 核燃料与核废料的锕系 5f 谱（UO2、PuO2）
summary: Valence and multiplet assignment in UO2, PuO2 and mixed-oxide fuels is done from M4,5-edge XAS and photoemission, interpreted with LDA+DMFT that national laboratories already run and that is temperature-limited by the impurity solver. A 7-orbital 5f impurity with 3–6 bath sites per spin-orbital fits in 56–98 qubits. The users are credible but few, the value is scientific and regulatory rather than commercial, and the gate count is 1e9–1e12 T.
summary_zh: UO2、PuO2 和混合氧化物燃料的价态与多重态归属来自 M4,5 边 XAS 和光电子谱，其解读依赖国家实验室已经在用的 LDA+DMFT，而它受限于杂质求解器的温度范围。7 轨道 5f 杂质加每个自旋轨道 3 到 6 个 bath 位点需要 56 到 98 个比特。用户可信但数量少，价值是科学与监管意义而非商业价值，门数在 1e9 到 1e12 个 T 门。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "7-orbital 5f shell with strong spin–orbit coupling, mixed valence in Pu, and finite temperature; CT-HYB sign problem is exponential in this regime, and Hubbard-I misses the itinerant part; dense multiplet spectra also make classical multireference chemistry on U2-type benchmarks hard"}
  quantum_easiness: {level: heuristic, note: "impurity Green's function by Trotter or quantum Krylov/Arnoldi; no fault-tolerant estimate for an f-shell impurity; dense spectra make phase-estimation-type approaches sensitive to initial-state overlap"}
  willingness_to_pay: {level: second-hand, note: "LANL and LLNL run DFT+DMFT on Pu and U compounds and fund the spectroscopy; no written accuracy target; the value is in fuel and waste-form qualification, not a market"}
resources: {logical_qubits: "56–98", gates: "1e9–1e12 T (illustrative scenario, not a resource estimate)", note: "7-orbital f impurity with 3–6 bath sites per spin-orbital; T count for ~100 fs evolution at 10 meV resolution; no published end-to-end estimate"}
related:
  applications: [rare-earth-permanent-magnets, battery-cathode-spectroscopy]
  problems: [linear-response-spectral-functions, ground-state-energy]
  methods: [dmft-impurity-solver]
  questions: [dmft-impurity-cost-vs-ctqmc-sign-problem]
references:
  - {arxiv: "1510.03859", title: "Hybrid quantum-classical approach to correlated materials", authors: "B. Bauer, D. Wecker, A. J. Millis, M. B. Hastings, M. Troyer", year: 2015, note: "~100-logical-qubit impurity solver proposal"}
  - {arxiv: "2605.22920", title: "Estimating Green's functions with a robust quantum Arnoldi method", authors: "J. S. Nelson, A. B. Baczewski (Sandia)", year: 2026}
  - {arxiv: "2303.11199", title: "A Tensor Train Continuous Time Solver for Quantum Impurity Models", authors: "A. Erpenbeck et al., E. Gull", year: 2023, note: "sign-problem-free classical competitor"}
  - {arxiv: "2603.15741", title: "Neural-Network Quantum Embedding Solvers for Correlated Materials", authors: "A. Valenti, H. Park, A. Georges, A. J. Millis, O. Parcollet", year: 2026}
  - {arxiv: "2601.10813", title: "Chemically decisive benchmarks on the path to quantum utility", authors: "S. Poyyapakkam Sundar, V. Abraham, B. Peng, A. Asthana", year: 2026, note: "graded benchmark set whose hardest tier is U2 actinide–actinide bonding"}
  - {arxiv: "1705.08027", title: "Crystal field splittings in rare earth-based hard magnets: an ab initio approach", authors: "P. Delange, S. Biermann, T. Miyake, L. Pourovskii", year: 2017, note: "Hubbard-I treatment of localised f shells, the approximation that fails for itinerant 5f"}
---

## Who needs it

National laboratories responsible for fuel qualification, plutonium ageing and waste-form stability (Los Alamos, Lawrence Livermore, Idaho, CEA, JAEA), and the fuel vendors and regulators that rely on their assessments. The questions are the oxidation state and multiplet structure of U and Pu in UO2, PuO2, mixed-oxide fuel and corrosion products, the degree of 5f localisation in δ-Pu and its alloys, and how these change with temperature, radiation damage and non-stoichiometry. The measurements are M4,5-edge X-ray absorption, HERFD-XAS, photoemission and RIXS; the interpretation requires a many-body calculation because 5f multiplets are dense and spin–orbit coupling is strong.

## Bottleneck

Actinide 5f electrons sit between the localised 4f limit and the itinerant 3d limit. DFT and DFT+U give the wrong metallic ground state for UO2 without symmetry breaking and misplace the 5f states in Pu. The working method is LDA+DMFT, and the laboratories have used it for two decades on δ-Pu and uranium compounds; it is also how the 14-orbital (7 spatial × 2 spin) 5f shell of Pu is currently modelled. The limitation is the impurity solver: CT-HYB with full spin–orbit coupling and off-diagonal hybridisation has a sign problem that grows exponentially with decreasing temperature, so the calculations are restricted to temperatures above where many of the spectroscopic questions are asked. The alternative, Hubbard-I, treats the f shell in the atomic limit [6] and cannot describe the mixed-valent, partially itinerant character of Pu 5f or of U in reduced oxides.

The same physics makes actinide molecules the hardest tier of chemistry benchmarks: the graded benchmark set of Poyyapakkam Sundar et al. places U2 actinide–actinide bonding above Fe–S clusters in difficulty, because of dense near-degenerate spectra, relativistic effects and dynamic correlation together [5]. Unlike the catalysis and OLED cases, however, no one has produced a classical-failure certificate for a specific actinide instance; the difficulty is documented mostly as method disagreement.

Value is real but not commercial: a better assignment of U valence in a corroded fuel pellet feeds a licensing or storage decision, and the users have decades of investment in exactly these calculations. There is no market, and no laboratory has written down a required accuracy.

## Computational problems

- [Linear response and spectral functions](../problems/linear-response-spectral-functions.html): the 5f impurity Green's function inside LDA+DMFT, and core-hole spectra at M4,5 edges.
- [Ground-state energy](../problems/ground-state-energy.html) of actinide molecules and clusters as benchmark instances (U2, uranyl, Pu oxides).

## Best classical today

LDA+DMFT with CT-HYB above roughly 100 K; Hubbard-I where the f shell is localised; relativistic multireference (CASPT2, DMRG with spin–orbit) for molecular actinide chemistry. Tensor-train CT-QMC removes the sign problem in principle by deterministic summation [3], and neural-network impurity solvers deliver QMC-quality self-energies orders of magnitude faster [4]; neither has been demonstrated on a full 5f shell with spin–orbit coupling at low temperature.

## Best quantum today

The 100-logical-qubit DMFT impurity solver of Bauer et al. [1] applied to a 7-orbital f shell: with 3–6 bath sites per spin-orbital the register is 56–98 qubits, which is the same kernel as the rare-earth magnet case and fits a 2029–2030 machine in qubit count. The T-gate cost of one Green's function at 10 meV resolution is 10^9–10^12 by the maintainers' estimate; quantum Arnoldi methods reduce this by orders of magnitude relative to point-by-point QSVT [2]. The dense multiplet spectrum is a mixed blessing: it is why classical solvers struggle, and also why any overlap-dependent quantum method (phase estimation on the impurity) needs care with initial states. No end-to-end fault-tolerant estimate for a 5f impurity exists.

## Verdict

Surviving. Of the DMFT scenarios, this one has the most credible users (laboratories that already run DMFT and already own the spectrometers) and the least commercial pull. Hardness is empirical and specific to the low-temperature, spin–orbit-coupled f shell; the quantum kernel fits 56–98 qubits; the gate count does not fit a five-year horizon; willingness to pay is second-hand and non-market. A demonstration around 2030 on a 200-logical-qubit machine, reproducing a UO2 or PuO2 M-edge spectrum where CT-HYB cannot reach the temperature and Hubbard-I gives the wrong valence, would be a science result with a real reader. To move the verdict, a laboratory would need to state which spectroscopic assignment, at which temperature and resolution, is currently blocked by the solver, and an end-to-end resource estimate for that instance would need to beat tensor-train and neural-network solvers on the same hybridisation function.

## Resource-count assumptions

The gate range quoted here is a sensitivity calculation: assume 10²–10³ time steps, 10⁴–10⁵ compiled T gates per step and 10³–10⁴ repetitions of one measured circuit. Multiplying endpoints gives **10⁹–10¹² T gates**. These inputs are not calibrated for a named impurity or a target error. The range excludes state preparation, additional time points and Green's-function components, bath convergence and DMFT iterations, so it is not an end-to-end estimate or a hardware readiness claim. See the [impurity-solver page](../methods/dmft-impurity-solver.html) for the conditions that remain to be checked.
