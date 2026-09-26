---
type: problem
id: quench-dynamics
title: Quench dynamics of local Hamiltonians
title_zh: 局域哈密顿量的淬火动力学
summary: Time-evolve a product state under a local Hamiltonian and measure local observables. This is BQP-complete, the cleanest hardness in the catalogue, and a 121-site 2D Ising quench costs about 140 logical qubits and 4e4 Toffoli gates. Every 100-qubit hardware demonstration so far has been reproduced classically, but 2D transverse-field Ising at 10×10 to 14×14 beyond t ≈ 2/J defeats MPS, TTN, belief-propagation tensor networks and neural quantum states. Nobody outside condensed-matter research pays for the answer.
summary_zh: 让乘积态在局域哈密顿量下演化并测量局域可观测量。这是 BQP 完全问题，是本目录中最干净的困难性证据；121 格点二维 Ising 淬火约需 140 个逻辑比特和 4e4 个 Toffoli 门。迄今每一个 100 比特硬件演示都被经典复现，但 10×10 到 14×14 的二维横场 Ising 在 t ≈ 2/J 之后让 MPS、TTN、信念传播张量网络和神经网络量子态全部失效。凝聚态研究之外没有人为这个答案付钱。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: reduction, note: "BQP-complete, including dynamical phase transitions and quadratic bosonic Hamiltonians; caveat: the hard instances encode circuits, and every noisy 100-qubit demonstration to date was reproduced by tensor networks or Pauli propagation"}
  quantum_easiness: {level: proven, note: "product-state input, Trotter or qubitised evolution, local observable; polynomial in system size and time with no overlap precondition"}
  willingness_to_pay: {level: none, note: "thermalisation, KPZ universality and many-body localisation are questions condensed-matter physicists want answered, but no company or agency has stated a target"}
resources: {logical_qubits: "~140", gates: "~4e4 Toffoli", note: "121-site 2D transverse-field Ising quench at logical error rate ~1e-5, from Google's 2025 compilation; ~160 logical qubits and 1e6 Toffoli for a 128 spin-orbital 2D Hubbard quench"}
related:
  problems: [linear-response-spectral-functions, ground-state-energy]
  methods: [error-mitigation, dmft-impurity-solver]
  claims: [ibm-kicked-ising-utility-2023, dwave-beyond-classical-2025, qctrl-fermi-hubbard-2026, quantinuum-floquet-prethermalization, google-quantum-echoes-otoc-2025]
  questions: [gauge-theory-bqp-completeness]
references:
  - {arxiv: "2511.09124", title: "The grand challenge of quantum applications", authors: "R. Babbush, R. King, S. Boixo, W. J. Huggins, T. Khattar, G. H. Low, J. R. McClean, T. O'Brien, N. C. Rubin", year: 2025}
  - {arxiv: "2511.19340", title: "Simulating dynamics of the two-dimensional transverse-field Ising model: a comparative study of large-scale classical numerics", authors: "J. Vovrosh, S. Julià-Farré, et al., J. Tindall, et al., A. Dauphin", year: 2026, note: "Phys. Rev. Research 8, 023311"}
  - {arxiv: "2606.30396", title: "Provable Quantum Advantage for Dynamical Phase Transition", authors: "J. Xu, X. Yuan, Q. Zhao", year: 2026}
  - {arxiv: "2603.26561", title: "Complexity of Quadratic Bosonic Hamiltonian Simulation: BQP-Completeness and PostBQP-Hardness", authors: "L. Zschetzsche, R. Mansuroglu, N. Schuch", year: 2026}
  - {arxiv: "2306.14887", title: "Efficient tensor network simulation of IBM's Eagle kicked Ising experiment", authors: "J. Tindall, M. Fishman, E. M. Stoudenmire, D. Sels", year: 2024}
  - {arxiv: "2308.05077", title: "Fast and converged classical simulations of evidence for the utility of quantum computing before fault tolerance", authors: "T. Begušić, J. Gray, G. K.-L. Chan", year: 2024}
  - {arxiv: "2503.05693", title: "Dynamics of disordered quantum systems with two- and three-dimensional tensor networks", authors: "J. Tindall, A. Mello, M. Fishman, E. M. Stoudenmire, D. Sels", year: 2026, note: "Science 392, 868; reproduces D-Wave's 2025 annealing observables"}
  - {arxiv: "2508.15759", title: "Evaluating classical simulations with a quantum processor", authors: "A. Nocera, J. Raymond, W. Bernoudy, M. H. Amin, A. D. King", year: 2025}
  - {arxiv: "2407.12768", title: "A polynomial-time classical algorithm for noisy quantum circuits", authors: "T. Schuster, C. Yin, X. Gao, N. Y. Yao", year: 2025}
  - {arxiv: "2409.01706", title: "Classically estimating observables of noiseless quantum circuits", authors: "A. Angrisani, A. Schmidhuber, M. S. Rudolph, M. Cerezo, Z. Holmes, H.-Y. Huang", year: 2025}
---

## Best classical

The record of hardware "utility" claims is a record of classical reproductions. IBM's 127-qubit kicked-Ising experiment was matched within weeks by belief-propagation tensor networks at bond dimension about 500 on a laptop in minutes [5] and by sparse Pauli dynamics on a single core [6]; the heavy-hexagon lattice is nearly a tree, which is why belief propagation is almost exact there. D-Wave's 2025 "beyond classical" annealing observables were reproduced with two- and three-dimensional belief-propagation tensor networks on a workstation [7]. Asymptotic theorems close the door on scalable advantage without error correction: constant local noise makes any geometry's random-circuit observables polynomial-time estimable [9], and even noiseless locally scrambling circuits have classically estimable observables on average [10].

The classical side has an honest boundary, though. Vovrosh et al. benchmarked MPS, tree tensor networks, belief-propagation tensor networks and neural quantum states on the 2D transverse-field Ising quench and found that for L ≥ 10 all methods deviate from each other once tJ exceeds about 2, with the largest 14×14 MPS run at bond dimension 600 [2]. Nocera et al. showed on D-Wave hardware that extrapolating tensor-network accuracy into the deeper regime is unreliable: errors grow faster than predicted [8]. The uncovered quadrant is clean 2D or 3D lattices, chaotic parameters, and times beyond 2/J, where entanglement follows a volume law and neither side can verify the other.

## Best quantum

Hardness here is a reduction, not folklore. Estimating local observables after local-Hamiltonian evolution is BQP-complete; recent results extend this to detecting dynamical quantum phase transitions [3] and to quadratic bosonic Hamiltonians [4]. The caveat that matters is that BQP-hard instances are Hamiltonians that encode circuits; BQP-completeness rules out a general classical method, not classical success on the model you care about. That gap is what the 2D TFIM benchmark [2] fills empirically.

Quantum easiness is the cleanest in the catalogue: the input is a product state, Trotter or qubitised evolution costs a number of gates proportional to system size times time, and there is no overlap precondition. Google's 2025 compilation prices a 121-site 2D Ising quench at about 140 logical qubits and 4×10⁴ Toffoli gates, a 70-site Heisenberg quench at 131 logical qubits, and a 128 spin-orbital 2D Hubbard quench at 160 logical qubits and 10⁶ Toffoli, all at logical error rates around 10⁻⁵ [1]. Those figures lie inside the 2027–2029 hardware roadmaps (order 100–200 logical qubits, 10⁶–10⁸ gates), which is the first time an application's requirement and a roadmap have lined up.

## Who wants it

Thermalisation and prethermalisation, KPZ universality in spin transport, many-body localisation boundaries, hydrodynamic transport coefficients. These are things condensed-matter and statistical physics genuinely want and cannot compute, but no company or agency has written down a target or a budget. The nearest paying relatives are spectral functions and DMFT impurity problems, which are quench dynamics cut into 50–100 qubit pieces.

## Verdict

Surviving, with willingness to pay set to none. Classical hardness is a reduction plus a measured 2D boundary; quantum easiness is proven; the quantum cost sits on the roadmaps. What is missing is a buyer, and an epistemic fix: at 100 qubits and t > 2/J neither the tensor network nor the device can be independently checked. Evidence that would change the page: an error-corrected run of a clean 2D quench at 10×10 or larger beyond t = 2/J with a verifiable observable (for example a Loschmidt echo or a symmetry-protected check), or a classical method that converges there.
