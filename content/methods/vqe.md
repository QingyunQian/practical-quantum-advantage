---
type: method
id: vqe
title: Variational quantum eigensolver (VQE) and variational circuits
title_zh: 变分量子本征求解器（VQE）与变分电路
summary: Optimise the parameters of a shallow circuit classically to minimise the measured energy. The NISQ-era workhorse. It is a heuristic with no runtime guarantee, its landscapes flatten exponentially (barren plateaus) for expressive circuits, and circuits shallow enough to train are classically simulable; the single-layer LUCJ circuits of IBM's 77-qubit experiment ran on a laptop in under a minute (Belagali et al.). No instance is known where VQE beats DMRG or SHCI on the same Hamiltonian; the best VQE-family numbers (iQCC on OLED emitters) came from GPU simulation.
summary_zh: 经典优化浅层电路的参数以最小化测得的能量，是 NISQ 时代的主力方法。它是没有运行时保证的启发式方法，表达力强的电路的能量面指数变平（贫瘠高原），而浅到能训练的电路又能经典模拟：IBM 77 比特实验的单层 LUCJ 电路在笔记本上不到一分钟就被模拟（Belagali 等）。没有任何实例显示 VQE 在同一哈密顿量上胜过 DMRG 或 SHCI；最好的 VQE 系数字（OLED 发光体上的 iQCC）来自对电路的 GPU 模拟。
status: seed
last_verified: 2026-09-26
verdict: no-go
dimensions:
  classical_hardness: {level: none, note: "the trainable regime coincides with the classically simulable regime (Larocca et al.); LUCJ circuits used in flagship experiments simulate in polynomial time"}
  quantum_easiness: {level: heuristic, note: "no convergence guarantee; measurement cost 1/ε² per energy evaluation; barren plateaus for global cost functions and expressive ansätze"}
  willingness_to_pay: {level: unknown, note: "OTI Lumionics / Samsung SAIT use iQCC for OLED emitters, but run it on classical GPUs; inherits the application"}
resources: {logical_qubits: "not applicable (NISQ method)", gates: "1/ε² shots per energy; 10⁴–10⁷ energy evaluations per optimisation", note: "chemical accuracy on a 50-qubit Hamiltonian needs ~1e8–1e10 shots per evaluation in the worst case"}
related:
  problems: [ground-state-energy, classical-data-machine-learning]
  applications: [oled-emitters]
  methods: [sqd, phase-estimation, error-mitigation]
  claims: [ibm-sqd-2024]
references:
  - {arxiv: "2111.05176", title: "The Variational Quantum Eigensolver: a review of methods and best practices", authors: "J. Tilly et al.", year: 2022}
  - {arxiv: "1803.11173", title: "Barren plateaus in quantum neural network training landscapes", authors: "J. R. McClean, S. Boixo, V. N. Smelyanskiy, R. Babbush, H. Neven", year: 2018}
  - {arxiv: "2405.00781", title: "Barren Plateaus in Variational Quantum Computing", authors: "M. Larocca, S. Thanasilp, S. Wang, K. Sharma, J. Biamonte, P. J. Coles, L. Cincio, J. R. McClean, Z. Holmes, M. Cerezo", year: 2024}
  - {arxiv: "2607.21337", title: "Efficient classical simulation of large-scale unitary cluster Jastrow circuits", authors: "K. Belagali et al.", year: 2026}
  - {arxiv: "2208.02199", title: "Is there evidence for exponential quantum advantage in quantum chemistry?", authors: "S. Lee et al.", year: 2023}
  - {arxiv: "2512.13657", title: "Towards Quantum Advantage in Chemistry", authors: "S. N. Genin et al.", year: 2025, note: "OTI Lumionics / Samsung SAIT; iQCC+PT reaches 0.0501 eV error on OLED T1 versus 0.1209 for TD-B3LYP"}
  - {arxiv: "2603.08883", title: "Parallel iQCC Enables 200 Qubit Scale Quantum Chemistry on Accelerated Computing Platforms Surpassing Classical Benchmarks in Ruthenium Catalysts", authors: "S. M. Hosseini Jenab, T. Henderson, S. N. Genin", year: 2026, note: "actual runs at 100–124 qubits on GPUs; '200' is extrapolated"}
---

## How it works

Choose a parameterised circuit U(θ) (hardware-efficient layers, unitary coupled cluster, local unitary cluster Jastrow), prepare U(θ)|0⟩ on the device, measure ⟨H⟩ term by term, and feed the energy to a classical optimiser. The variational principle guarantees the result is an upper bound on the ground-state energy; nothing guarantees how close. Tilly et al. review the method and its many variants [1]. Adaptive versions (ADAPT-VQE, iQCC) grow the ansatz one operator at a time.

## Preconditions

1. The ansatz must contain a state within the target accuracy of the ground state, at a depth the device can run coherently.
2. The gradient (or cost-function variance) must not vanish exponentially in qubit number, or the optimiser cannot move.
3. The energy must be measured to precision ε at a shot cost that is affordable: 1/ε² per evaluation, multiplied by the number of Hamiltonian terms (after grouping) and the number of optimisation steps.
4. The circuit must not be classically simulable; otherwise the device is an expensive way to evaluate a classical wavefunction.

## Known limits

- **Barren plateaus.** McClean et al. showed that for random parameterised circuits the gradient variance vanishes exponentially in qubit number [2]. Larocca et al.'s 2024 synthesis makes the deeper point: every known mechanism that provably avoids a barren plateau (small dynamical Lie algebra, low entanglement, locality, small-angle initialisation) also yields a classical simulation of the relevant loss landscape, so trainability and classical simulability appear to be two sides of the same coin [3]. Preconditions 2 and 4 pull in opposite directions.
- **The flagship circuits are simulable.** The single-layer LUCJ circuits used in IBM's 77-qubit SQD experiment were simulated classically on a laptop in under a minute, with lower energies than the hardware [4]. The same class of circuit is the standard chemistry ansatz for near-term VQE.
- **The best VQE-family results are classical.** OTI Lumionics and Samsung SAIT report that iQCC with perturbative correction brings the OLED emitter T₁ error to 0.0501 eV against 0.1209 eV for TD-B3LYP [6], and a follow-up runs parallel iQCC at 100–124 qubits on GPUs and claims to surpass DMRG on ruthenium catalysts, projecting 200 qubits [7]. These are variational quantum circuits evaluated by classical simulation; the authors' own estimate is that the quantum threshold may lie beyond 200 qubits.
- **No advantage evidence, and no guarantee to look for one.** Lee et al. note that VQE has no runtime guarantee at all, so even the conditional argument available to phase estimation does not apply [5]. No published VQE hardware result reaches chemical accuracy on a Hamiltonian where DMRG or SHCI do not, and measurement counts of 10⁸–10¹⁰ shots per energy evaluation for 50-qubit molecular Hamiltonians at chemical accuracy make optimisation loops of 10⁴ steps impractical before noise is considered.

## Verdict

No-go as a route to advantage, with a caveat. The method is a heuristic whose trainable regime is classically simulable, whose flagship circuits have been simulated on laptops, and whose most useful outputs so far come from classical GPUs. The caveat is that variational circuits are a fine way to prepare initial states for phase estimation, and iQCC-style classical algorithms inspired by them are competitive chemistry methods in their own right. What would change the verdict: a variational circuit family shown to be trainable at scale (gradient variance decaying at most polynomially) and simultaneously proven or strongly evidenced to be hard to simulate, with an energy on a benchmark Hamiltonian below the best DMRG/SHCI value.
