---
type: method
id: dmft-impurity-solver
title: Quantum impurity solver inside dynamical mean-field theory (DMFT)
title_zh: 动力学平均场（DMFT）中的量子杂质求解器
summary: "DMFT couples an impurity solver to a classical self-consistency loop. Selected discretised d- and f-shell models fit a 50–100 qubit system register, but bath convergence and state preparation still need to be demonstrated. An illustrative multiplication of time steps, compiled T gates and repetitions gives 1e9–1e12 T gates; this is not an end-to-end resource estimate."
summary_zh: "DMFT 把杂质求解器嵌入经典自洽循环。部分离散化的 d、f 壳模型可装进 50 到 100 个系统比特，但浴离散化收敛和初态制备仍需验证。按文中假设相乘得到 1e9 到 1e12 个 T 门，这只是成本敏感性计算，不能当作端到端资源估计。"
status: seed
last_verified: 2026-09-27
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "CT-HYB sign problems occur for some multi-orbital models, but the cited cathode application was solved with classical CT-QMC; no matched application-level failure curve is supplied"}
  quantum_easiness: {level: conditional, note: "polynomial once the impurity ground (or thermal) state is prepared; needs bath discretisation that keeps the self-consistency converged; gate count 1e9–1e12 T from stated Trotter, non-Clifford and shot factors, not from a published estimate"}
  willingness_to_pay: {level: second-hand, note: "inherits the spectroscopy users of the linear-response problem; rare-earth magnet and actinide groups run DMFT but have not stated targets; industry mostly avoids DMFT"}
resources: {logical_qubits: "50–100", gates: "1e9–1e12 T (illustrative scenario, not a resource estimate)", note: "5-orbital d + SOC with 4–8 bath sites per spin-orbital = 50–90 qubits; 7-orbital f with 3–6 bath sites = 56–98; 2x2 cluster = 40–48; evolution to ~100 fs for 10 meV resolution; Krylov/Arnoldi methods may cut gates by orders of magnitude"}
related:
  problems: [linear-response-spectral-functions, quench-dynamics, ground-state-energy]
  methods: [embedding-divide-and-conquer, phase-estimation]
  applications: [rare-earth-permanent-magnets, battery-cathode-spectroscopy, nuclear-fuel-actinide-spectra]
  questions: [dmft-impurity-cost-vs-ctqmc-sign-problem, embedding-fragment-size-vs-correlation-length]
references:
  - {arxiv: "1510.03859", title: "Hybrid quantum-classical approach to correlated materials", authors: "B. Bauer, D. Wecker, A. J. Millis, M. B. Hastings, M. Troyer", year: 2016, note: "Phys. Rev. X 6, 031045"}
  - {arxiv: "2404.09527", title: "Dynamical Mean Field Theory for Real Materials on a Quantum Computer", authors: "J. Selisko, M. Amsler, C. Wever, Y. Kawashima, G. Samsonidze, et al., I. Tavernelli, T. Eckl", year: 2024, note: "Ca2CuO2Cl2 on IBM hardware, 14 qubits"}
  - {arxiv: "2605.22920", title: "Estimating Green's functions with a robust quantum Arnoldi method", authors: "S. Nelson, A. D. Baczewski", year: 2026}
  - {arxiv: "2207.06135", title: "Learning Feynman Diagrams with Tensor Trains", authors: "Y. Núñez Fernández, M. Jeannin, P. T. Dumitrescu, T. Kloss, J. Kaye, O. Parcollet, X. Waintal", year: 2022, note: "tensor cross interpolation, sign-problem-free"}
  - {arxiv: "2603.15741", title: "Neural-network quantum embedding solvers for correlated materials", authors: "A. Valenti, I. Park, A. Georges, A. J. Millis, O. Parcollet", year: 2026}
  - {arxiv: "1705.08027", title: "Crystal-field splittings in rare-earth-based hard magnets: an ab initio approach", authors: "P. Delange, S. Biermann, T. Miyake, L. Pourovskii", year: 2017, note: "Hubbard-I workaround for the 4f impurity"}
  - {arxiv: "1907.08570", title: "A Multiorbital Quantum Impurity Solver for General Interactions and Hybridizations", authors: "E. Eidelstein, E. Gull, G. Cohen", year: 2019, note: "classical Inchworm handles low-temperature examples where CT-HYB fails"}
  - {arxiv: "2601.04832", title: "Affordable Five-Orbital Dynamical Mean-Field Theory for Layered Iridates and Rhodates", authors: "L. Gaspard, C. Martins", year: 2026, note: "hybrid versus full five-orbital DMFT on two oxides"}
---

## How it works

DMFT replaces the lattice self-energy by a local one, obtained from an Anderson impurity model whose bath is fixed self-consistently from the lattice Green's function. The loop is: guess the hybridisation, solve the impurity for its Green's function G_imp(ω), extract the self-energy, recompute the lattice Green's function, update the hybridisation, repeat. The impurity solve is a potential classical bottleneck; the surrounding loop uses classical linear algebra. Its difficulty depends on the impurity, temperature and requested accuracy. Bauer, Wecker, Millis, Hastings and Troyer proposed doing the impurity solve on a quantum computer of about one hundred logical qubits, discretising the bath into a handful of sites per orbital and measuring the impurity Green's function by time evolution and Hadamard tests [1]. Selisko et al. closed the loop on IBM hardware for a real material, Ca₂CuO₂Cl₂, with 14 qubits [2]. Since then the Green's-function step has been reformulated in Krylov and Arnoldi forms; the robust quantum Arnoldi method estimates the spectral function over an interval at a cost orders of magnitude below pointwise QSVT [3].

## Preconditions

1. The embedding must be adequate. DMFT is exact only in infinite coordination; the quantum solver removes solver error, not the errors from the choice of U, double counting or the single-site approximation, which are typically larger.
2. The bath discretisation must fit the register and converge the requested observable. The small bath counts used in the examples are assumptions, not a uniform convergence guarantee. Real-frequency resolution may require larger baths; the required count must be measured for each model.
3. The impurity ground state (or thermal state) must be preparable with non-negligible overlap; for f shells with strong multiplet structure this is not automatic.
4. The target regime must be one where the best classical solvers actually fail at the requested accuracy. Multi-orbital spin–orbit models, dynamical f-shell treatments and low-temperature clusters are candidates for such a benchmark. The cited cathode example is not one: its DMFT step was solved with classical CT-QMC.

## Known limits

- **Gate count.** Under the illustrative assumptions below, 10²–10³ steps × 10⁴–10⁵ T gates per step × 10³–10⁴ repetitions gives 10⁹–10¹² T gates for one measured circuit. An end-to-end estimate must also account for state preparation, time sampling, the desired precision and the DMFT loop. The references listed here do not supply that estimate for the proposed SOC impurity.

- **Classical alternatives.** A low-temperature Kanamori impurity had a CT-HYB cost extrapolated to roughly 3 × 10⁹ core-hours at βt = 64, yet classical Inchworm produced its Green's function in roughly 1.5 × 10³ core-hours [7]. For Ba₂IrO₄ and Ba₂RhO₄, full five-orbital DMFT completed classically, while hybrid DMFT gave 43.8-fold and 41.2-fold total-time gains with reported low-energy agreement [8]. CT-HYB failure alone therefore does not establish a quantum opportunity.

## Verdict

Surviving. DMFT offers a useful way to isolate a quantum subproblem, and small hardware demonstrations show the self-consistency loop can close [1, 2]. The currently cited industrially relevant cathode impurity was solved classically; other hard regimes remain proposed benchmarks. No publication date or machine size for a practical advantage follows from the system-register count. Evidence that would change the verdict is a same-instance, same-accuracy comparison with CT-QMC, tensor-train and neural-network solvers, including bath convergence and the full loop cost.

## Resource-count assumptions

The gate range quoted here is a sensitivity calculation: assume 10²–10³ time steps, 10⁴–10⁵ compiled T gates per step and 10³–10⁴ repetitions of one measured circuit. Multiplying endpoints gives **10⁹–10¹² T gates**. These inputs are not calibrated for a named impurity or a target error. The range excludes state preparation, additional time points and Green's-function components, bath convergence and DMFT iterations, so it is not an end-to-end estimate or a hardware readiness claim. See the [impurity-solver page](../methods/dmft-impurity-solver.html) for the conditions that remain to be checked.
