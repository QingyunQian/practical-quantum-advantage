---
type: method
id: sqd
title: Sample-based quantum diagonalization (SQD / QSCI)
title_zh: 采样式量子对角化（SQD / QSCI）
summary: Sample bitstrings from a quantum circuit, then diagonalise the Hamiltonian classically in the sampled subspace. IBM's flagship "quantum-centric supercomputing" method. Its premise, a sparse ground state, fails for strong correlation; in the ideal limit it does not beat classical selected-CI, and its 77-qubit result was reproduced on a laptop.
summary_zh: 用量子电路采样比特串，再在采到的子空间里经典对角化。IBM 量超融合的核心方法。它依赖基态稀疏这一前提，而强关联恰恰破坏这一前提；在理想极限下不比经典 SCI 好，77 比特的结果已被笔记本复现。
status: seed
last_verified: 2026-09-26
verdict: no-go
dimensions:
  classical_hardness: {level: none, note: "the classical post-processing (configuration recovery + diagonalisation) does the work; single-layer LUCJ sampling circuits are classically simulable"}
  quantum_easiness: {level: no, note: "requires the ground state to be sparse in the computational basis; exact-state sampling test shows no gain over classical selection at equal subspace size"}
  willingness_to_pay: {level: unknown, note: "inherits the application; no buyer specific to the method"}
related:
  problems: [ground-state-energy]
  claims: [ibm-sqd-2024]
  questions: [ideal-sqd-vs-classical-selection]
references:
  - {arxiv: "2405.05068", title: "Chemistry beyond the scale of exact diagonalization on a quantum-centric supercomputer", authors: "J. Robledo-Moreno et al.", year: 2025}
  - {arxiv: "2501.07231", title: "Critical limitations in quantum-selected configuration interaction methods", authors: "P. Reinholdt et al.", year: 2025}
  - {arxiv: "2605.02494", title: "A Critical Assessment of the Sample-Based Quantum Diagonalization for Heisenberg and Hubbard Models", authors: "C. Gaberle, M. S. Jattana", year: 2026, note: "exact-ground-state sampling on Heisenberg/Hubbard lattices; required configurations grow exponentially even with optimal ordering"}
  - {arxiv: "2607.21337", title: "Efficient classical simulation of large-scale unitary cluster Jastrow circuits", authors: "K. Belagali et al.", year: 2026}
---

## How it works

Prepare an approximate ground state on the device (typically a local unitary cluster Jastrow, LUCJ, circuit), sample computational-basis bitstrings, correct them for particle-number and spin symmetry ("configuration recovery"), and diagonalise the Hamiltonian in the span of the sampled determinants on a classical computer. Iterate: the classical eigenvector's occupation numbers steer the next round of recovery. Demonstrated on N₂ and [2Fe-2S]/[4Fe-4S] clusters with 77 qubits [1], and in 2026 extended, via embedding, to a 12,635-atom protein–ligand complex.

## Preconditions

1. The ground state must be sparse in the computational basis: a subspace of size K ≪ dim must capture the energy to the target accuracy.
2. The sampling circuit must produce that subspace more efficiently than a classical selection rule (HCI/CIPSI perturbative selection, or simply sorting exact amplitudes).
3. The circuit itself must not be classically simulable; otherwise the bitstrings can be generated without the device.

## Known limits

- **Sparsity fails under strong correlation.** Gaberle and Jattana sample from exact ground states of Heisenberg and Hubbard lattices and find the number of configurations needed for fixed accuracy grows exponentially with size, even with optimal ordering [3].
- **Ideal sampling does not beat classical selection.** In this repository's test (`numerics/sqd_ideal_test.py`), sampling from the exact ground state of the 4×3 half-filled Hubbard model at U/t = 4 gives the same energy-vs-K curve as taking the K largest exact amplitudes and as HCI at equal K. At 16% of the full space the error is still 0.04 t per site, about 40× a chemical-accuracy analogue. Starting from uniformly random bitstrings, two rounds of classical configuration recovery reach the same accuracy: the classical loop does the work.
- **Systmatic errors.** Reinholdt et al. document biases in QSCI energies and non-variational behaviour under realistic sampling budgets [2].
- **The circuits are simulable.** The single-layer LUCJ circuits used in the 77-qubit experiment were simulated classically on a laptop in under a minute, with lower energies than the hardware run [4].

![Ideal-limit SQD test](../figs/fig5_sqd_ideal.png)

## Verdict

No-go as a route to advantage. In the weakly correlated regime the ground state is sparse but classical selected-CI already works; in the strongly correlated regime the premise fails. The method may remain useful as an error-tolerant post-processing scheme for hardware demonstrations, but there is no instance family known where the quantum sampler contributes something the classical loop cannot. Evidence that would change this: an instance where exact-state sampling beats HCI at equal K by a factor that grows with size.
