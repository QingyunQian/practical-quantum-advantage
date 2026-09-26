---
type: method
id: phase-estimation
title: Quantum phase estimation for ground-state energies
title_zh: 基态能量的量子相位估计
summary: The fault-tolerant route to ground-state energies. Polynomial cost is proven only when an initial state with overlap ≥ 1/poly on the true ground state is supplied; no natural class of chemical Hamiltonians is known to satisfy this, and Lee et al. argue the same physics that makes a good initial state easy to find also makes classical heuristics work. Survives as the only method with a hardness theorem behind it (guided local Hamiltonian is BQP-complete at 1/poly precision).
summary_zh: 通向基态能量的容错路线。只有在初始态与真实基态的重叠不小于 1/poly 时才有多项式代价的证明；没有任何一类自然化学哈密顿量被证明满足这一条件，Lee 等人指出让好初态容易找到的物理同样让经典启发式方法有效。它是唯一背后有硬度定理的方法（带引导态的局域哈密顿量问题在 1/poly 精度下 BQP 完全），因此仍然幸存。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: reduction, note: "guided local Hamiltonian is BQP-complete at inverse-polynomial precision, even for 2-local Hamiltonians on 2D lattices; but constant precision is classically easy and the BQP-hard instances are not known to be chemical ones"}
  quantum_easiness: {level: conditional, note: "polynomial cost given overlap ≥ 1/poly and a block encoding; overlap is empirically found to decay with system size and no natural chemistry class has a proven lower bound"}
  willingness_to_pay: {level: unknown, note: "inherits the application (OLED emitters, catalysts); no buyer specific to the method"}
resources: {logical_qubits: "~1,200–2,200 (P450, FeMoco with ancillas)", gates: "5e8–1e10 Toffoli", note: "Goings et al. Table 4: 1,426–2,158 logical qubits and 4.3e9–8.3e9 Toffoli for P450 CAS(63e,58o); Google 2025 compilation: FeMoco 1,500 logical / 1e9 Toffoli; 2D Ising quench at 121 sites for comparison 140 logical / 4e4 Toffoli"}
related:
  problems: [ground-state-energy, excited-states]
  applications: [oled-emitters, homogeneous-catalysis, p450-drug-metabolism]
  methods: [sqd, vqe, embedding-divide-and-conquer]
  questions: [dmrg-vs-qpe-cost-accuracy-oled, kagome-guiding-state-overlap]
references:
  - {arxiv: "2208.02199", title: "Is there evidence for exponential quantum advantage in quantum chemistry?", authors: "S. Lee, J. Lee, H. Zhai, Y. Tong, et al.", year: 2023, note: "published as Nat. Commun. 14, 1952 (2023) under the title 'Evaluating the evidence for exponential quantum advantage in ground-state quantum chemistry'"}
  - {arxiv: "2111.09079", title: "Dequantizing the Quantum Singular Value Transformation: Hardness and Applications to Quantum Chemistry and the Quantum PCP Conjecture", authors: "S. Gharibian, F. Le Gall", year: 2022}
  - {arxiv: "2207.10250", title: "Improved Hardness Results for the Guided Local Hamiltonian Problem", authors: "C. Cade et al.", year: 2023}
  - {arxiv: "2411.16163", title: "A Dequantized Algorithm for the Guided Local Hamiltonian Problem", authors: "Y. Zhang, Y. Wu, X. Yuan", year: 2024}
  - {arxiv: "2102.11340", title: "Heisenberg-limited ground state energy estimation for early fault-tolerant quantum computers", authors: "L. Lin, Y. Tong", year: 2022}
  - {arxiv: "2503.12224", title: "Bounding Eigenstate Overlap from Hamiltonian Moments: Success Probability Guarantees for Quantum Phase Estimation", authors: "J. Lin, A. F. Izmaylov", year: 2025}
  - {arxiv: "2202.01244", title: "Reliably assessing the electronic structure of cytochrome P450 on today's classical computers and tomorrow's quantum computers", authors: "J. J. Goings et al.", year: 2022}
  - {arxiv: "2511.09124", title: "The Grand Challenge of Quantum Applications", authors: "R. Babbush et al.", year: 2025}
  - {arxiv: "2601.04621", title: "Classical computational simulation of the FeMo-cofactor model to chemical accuracy and its implications", authors: "H. Zhai, Z. Li, et al., G. K.-L. Chan", year: 2026}
---

## How it works

Encode the Hamiltonian as a block encoding (double factorisation or tensor hypercontraction), prepare an approximate ground state, and read out an eigenphase of the walk operator. If the prepared state has overlap p₀ = |⟨φ|ψ₀⟩|² with the true ground state, the correct energy is returned with probability p₀ per run, so the total cost scales as 1/p₀ (or 1/√p₀ with amplitude amplification) times the cost of resolving the energy to precision ε. Early fault-tolerant variants (Lin–Tong and follow-ups) trade ancilla qubits for repetitions and reach Heisenberg scaling in ε with a single ancilla [5].

## Preconditions

1. **Initial-state overlap ≥ 1/poly.** This is the entire content of the "quantum easiness" claim. Without it the runtime is exponential in the same way that classical methods are.
2. **A block encoding of the Hamiltonian** with polynomially bounded normalisation. For second-quantised chemistry this is available; the constant factors (10⁹–10¹⁰ Toffoli for 60–80 orbitals) come from here.
3. **Target precision ε = 1/poly.** The guided local Hamiltonian problem is BQP-complete at inverse-polynomial precision [2,3] but admits a classical polynomial-time algorithm at constant precision when the guiding state is classically samplable [4]. Chemical accuracy on a 100-orbital problem is inside the hard window, which is the only good news the complexity theory offers.

## Known limits

- **No natural class satisfies precondition 1 provably.** The BQP-hardness constructions [2,3] use engineered 2-local Hamiltonians; they do not show that any molecular family is hard. Conversely, Lee et al. [1] observe empirically that single-determinant overlaps decay exponentially with system size on Fe–S chains and argue that the locality and gap structure that keeps overlaps large is the same structure that makes classical heuristics converge polynomially. Their conclusion is that exponential advantage is not generic, and that the realistic expectation is polynomial.
- **The overlap is not a controllable knob.** The only tool that certifies an initial state's quality without solving the problem is the Hamiltonian-moment bound of Lin and Izmaylov [6], which needs classically computed moments ⟨H^k⟩. Where those moments are cheap, the classical side is usually already competitive.
- **The classical competitor keeps moving.** The FeMoco model (76 orbitals, 113 electrons) that motivated the early resource estimates was solved to ±0.31 kcal/mol in 2026 with DMRG at bond dimension 18,000 and about 2.8 million core-hours [9]. The same paper reports a symmetry-broken determinant with overlap 0.4468 on the DMRG state, so for this instance the initial state is easy but the classical answer already exists.
- **Cost.** P450 CAS(63e,58o) needs 1,426–2,158 logical qubits and 4.3–8.3 × 10⁹ Toffoli gates [7]; Google's 2025 compilation puts FeMoco at 1,500 logical qubits and 10⁹ Toffoli, about nine hours on a 5 × 10⁶ physical-qubit machine [8]. A 121-site 2D Ising quench costs 140 logical qubits and 4 × 10⁴ Toffoli in the same table, so chemistry ground states are two to five orders of magnitude more expensive than the dynamics problems the first machines will run.

## Verdict

Surviving. Phase estimation is the one ground-state method that carries a hardness theorem and a polynomial-time guarantee, but the guarantee is conditional on an overlap that nobody can certify in advance for the instances people want, and the hard instances known to complexity theory are not the instances chemistry wants. What would change the verdict: a molecular or lattice family where the guiding-state overlap is shown to decay at most polynomially while DMRG bond dimension, SHCI determinant count and AFQMC bias are shown to grow exponentially, with both sides measured on the same Hamiltonians. This repository's kagome numerics (`numerics/`, see the linked question) are one attempt at such a measurement.
