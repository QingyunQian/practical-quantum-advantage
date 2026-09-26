---
type: claim
id: dwave-beyond-classical-2025
title: D-Wave "beyond-classical" spin-glass annealing (2025)
title_zh: D-Wave 自旋玻璃退火 “beyond-classical” 主张（2025）
summary: King et al. ran fast quenches of transverse-field Ising spin glasses on D-Wave annealers and argued that tensor-network and neural-network methods could not match the quantum samples at comparable cost. Belief-propagation tensor networks reproduced the main geometries within months on a workstation, and time-dependent variational Monte Carlo followed; D-Wave's own follow-up shows tensor-network accuracy extrapolation is unreliable in the deepest regime.
summary_zh: King 等在 D-Wave 退火机上快速淬火横场 Ising 自旋玻璃，宣称张量网络与神经网络方法无法以可比代价达到同等精度。数月内，信念传播张量网络在工作站上复现了主要几何，随后 tVMC 也跟进；D-Wave 自己的后续工作则表明张量网络在最深区间的精度外推不可靠。
status: reviewed
last_verified: 2026-09-26
claim:
  claimant: D-Wave Quantum (King et al.)
  date: 2025-03
  statement: "Beyond-classical computation in quantum simulation: annealing processors generate samples in close agreement with Schrödinger dynamics for 2D, 3D and diamond-lattice spin glasses at sizes and times where tensor-network and neural-network methods fail to reach the same accuracy."
  hardware: Advantage / Advantage2 prototype (superconducting flux-qubit annealers)
  qubits: 5000
  refuted: true
  refutation_date: 2025-03
  refuted_by: "Tindall, Mello, Fishman, Stoudenmire, Sels (belief-propagation tensor networks in 2D and 3D, workstation); Wiersema (time-dependent variational Monte Carlo)"
  time_to_refute: "months (preprint March 2024; BP tensor-network reproduction appeared the week of the Science publication, March 2025)"
related:
  problems: [quench-dynamics]
  methods: [error-mitigation]
  claims: [ibm-kicked-ising-utility-2023, quantinuum-floquet-prethermalization]
references:
  - {arxiv: "2403.00910", title: "Beyond-classical computation in quantum simulation", authors: "A. D. King, A. Nocera, M. M. Rams et al.", year: 2025, note: "Science 388, 199 (2025)"}
  - {arxiv: "2503.05693", title: "Dynamics of disordered quantum systems with two- and three-dimensional tensor networks", authors: "J. Tindall, A. Mello, M. Fishman, E. M. Stoudenmire, D. Sels", year: 2026, note: "Science 392, 868 (2026)"}
  - {arxiv: "2609.01719", title: "Numerical simulation of D-Wave's quantum advantage experiment with time-dependent variational Monte Carlo", authors: "R. Wiersema", year: 2026}
  - {arxiv: "2508.15759", title: "Evaluating classical simulations with a quantum processor", authors: "A. Nocera, J. Raymond, W. Bernoudy, M. H. Amin, A. D. King", year: 2025}
---

## Claim

King et al. quenched transverse-field Ising spin glasses on D-Wave annealing processors, on square, cubic, diamond and biclique-like geometries with up to thousands of qubits, and compared the sampled correlations with Schrödinger-equation solutions on small instances and with classical approximations on large ones. They reported area-law entanglement along the quench and stated that several leading approximate methods based on tensor networks and neural networks cannot reach the same accuracy in comparable time, from which they inferred that the annealer performs a computation beyond classical reach [1]. The preprint appeared in March 2024; the Science paper in March 2025.

## Refutation

- Tindall, Mello, Fishman, Stoudenmire and Sels applied belief-propagation tensor networks directly in two and three dimensions (no snake mapping to an MPS) and reproduced the reported annealing observables for the main geometries with modest resources, extending to hundreds of qubits and recovering Kibble–Zurek scaling; the preprint appeared in March 2025 and was published in Science 392, 868 (2026) [2]. This is the same family of methods that reproduced the IBM kicked-Ising experiment [see ibm-kicked-ising-utility-2023].
- Wiersema showed that time-dependent variational Monte Carlo, with an ansatz enlarged systematically, approximates the final two-spin correlation errors of the processor on large graph instances at polynomial cost, while documenting Markov-chain mixing and solver-stability limits [3].
- D-Wave's reply, Nocera, Raymond, Bernoudy, Amin and King, used the processor as a reference to test the classical simulations and found that tensor-network accuracy scales differently from what was predicted, i.e. the BP tensor-network error grows faster than the extrapolation in the most strongly entangled, fastest-quench regime [4]. This is a fair point about extrapolation and it is recorded here as the honest boundary: the reproductions cover the main reported geometries, not every parameter corner.

The refuted flag is set because the central statement, that tensor-network methods cannot reach the same accuracy at comparable cost, did not survive the first dedicated attempt for the headline instances.

## Lesson for the catalogue

Comparing against a tensor network in the wrong geometry (an MPS snake through a 3D lattice) is the same mistake as IBM's 2023 comparison. The residual open region, fast quenches on 3D lattices where BP is not converged, is exactly the region where neither side can verify its answer; that gap is tracked under `quench-dynamics`, not as a standing advantage claim.
