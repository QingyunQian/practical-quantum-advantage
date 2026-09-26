---
type: claim
id: ibm-sqd-2024
title: IBM 77-qubit sample-based quantum diagonalization for chemistry
title_zh: IBM 77 比特样本量子对角化（SQD）化学计算
summary: Robledo-Moreno et al. combined 77-qubit LUCJ circuits on IBM Heron with subspace diagonalization on Fugaku to compute N2 and iron–sulfur cluster energies "beyond the scale of exact diagonalization". Two years later Belagali et al. evaluated the single-layer LUCJ energy classically in polynomial time, reproducing the largest experiment on a laptop in under a minute and obtaining a lower energy; independent studies had already shown the sampled subspaces are no better than classical selection.
summary_zh: Robledo-Moreno 等把 IBM Heron 上 77 比特 LUCJ 电路的采样与富岳上的子空间对角化结合，计算 N2 与铁硫团簇能量，称“超出精确对角化的规模”。两年后 Belagali 等给出单层 LUCJ 能量的多项式时间经典算法，在笔记本上不到一分钟复现最大实验并得到更低能量；此前的独立研究已表明采样子空间并不优于经典选择。
status: reviewed
last_verified: 2026-09-26
claim:
  claimant: IBM Quantum with RIKEN (Robledo-Moreno et al.)
  date: 2024-05
  statement: "Chemistry beyond the scale of exact diagonalization on a quantum-centric supercomputer: circuits up to 77 qubits and 10,570 gates sampled on Heron, post-processed on Fugaku, yield ground-state energy upper bounds for N2 and [2Fe-2S]/[4Fe-4S] clusters in active spaces beyond exact diagonalization."
  hardware: IBM Heron r1 (superconducting) plus Fugaku
  qubits: 77
  refuted: true
  refutation_date: 2026-07
  refuted_by: "Belagali, Van Camp, Pradeep, Das, Anand, LaRose (polynomial-time classical evaluation of single-layer LUCJ energies; laptop, under one minute, lower energy). Earlier: Reinholdt et al. (HCI/CIPSI beat sampled subspaces at equal size); Vaquero-Sabater et al. (random bitstrings plus configuration recovery reach the same accuracy)."
  time_to_refute: "two years for the quantum step; eight months for the first critique of the selection premise"
related:
  problems: [ground-state-energy]
  methods: [sqd]
  questions: [ideal-sqd-vs-classical-selection]
  claims: [ibm-kicked-ising-utility-2023]
references:
  - {arxiv: "2405.05068", title: "Chemistry Beyond the Scale of Exact Diagonalization on a Quantum-Centric Supercomputer", authors: "J. Robledo-Moreno, M. Motta, H. Haas et al.", year: 2025, note: "Sci. Adv. 11, eadu9991 (2025)"}
  - {arxiv: "2607.21337", title: "Efficient classical simulation of large-scale unitary cluster Jastrow circuits", authors: "H. Belagali, T. Van Camp, R. Pradeep, S. Das, N. Anand, R. LaRose", year: 2026}
  - {arxiv: "2501.07231", title: "Critical Limitations in Quantum-Selected Configuration Interaction Methods", authors: "P. Reinholdt et al.", year: 2025, note: "JCTC 21, 6811 (2025)"}
  - {arxiv: "2605.23697", title: "Noise and Configuration Recovery Impact on Quantum Selected Configuration Interaction", authors: "N. Vaquero-Sabater, A. Carreras, L. Broers, T. Shirakawa, S. Yunoki, D. Casanova", year: 2026}
  - {arxiv: "2605.02494", title: "A Critical Assessment of the Sample-Based Quantum Diagonalization for Heisenberg and Hubbard Models", authors: "M. Gaberle, M. S. Jattana", year: 2026}
---

## Claim

Robledo-Moreno et al. prepared local unitary cluster Jastrow (LUCJ) states on up to 77 qubits with up to 10,570 gates on an IBM Heron processor, sampled bitstrings, applied symmetry-based configuration recovery, and diagonalised the Hamiltonian in the sampled determinant subspace on up to 6,400 nodes of Fugaku. They reported variational energy upper bounds for N2 dissociation and for [2Fe-2S] and [4Fe-4S] clusters in active spaces larger than exact diagonalization can handle [1]. The statement was about scale, not about beating the best classical method, but the work became the reference point for IBM's "quantum-centric supercomputing" programme and for the 12,000-atom protein demonstration that followed.

## Refutation

- Belagali et al. gave a polynomial-time classical algorithm for the energy of single-layer LUCJ circuits, which is the ansatz used in the experiment. They reproduced the largest experiment from [1] in under a minute on a laptop and, by optimising the circuit with the fast simulator, reached a lower ground-state energy than the hardware run [2]. The preprint appeared on 2026-07-23.
- The premise that quantum samples select a better subspace than classical heuristics had already been tested. Reinholdt et al. showed that sampling repeatedly returns configurations already seen while important ones have very low probability, so that heat-bath CI and CIPSI reach lower energies at equal determinant count, even for an ideal noiseless sampler [3]. Vaquero-Sabater et al. found that starting configuration recovery from uniformly random bitstrings gives the same accuracy as starting from hardware samples [4]. Gaberle and Jattana showed on Heisenberg and Hubbard lattices that the number of configurations needed grows exponentially with size even under optimal ordering [5].
- This repository's own ideal-sampler test on the 4×3 Hubbard model (`numerics/sqd_ideal_test.py`) agrees: exact sampling, top-|c| selection and HCI give the same energy-versus-K curve within a factor of 1.5.

The flag is set to refuted because both halves of the advantage argument failed: the quantum circuit is classically simulable, and the sampling step does not outperform classical selection.

## Lesson for the catalogue

An experiment that is "beyond exact diagonalization" is not beyond classical methods, since DMRG, SHCI and AFQMC routinely work far beyond ED. For SQD-type claims the catalogue asks for the four tests listed on the `sqd` method page: a variational bound below the best of SHCI/DMRG/NQS/AFQMC in the same active space, a random-bitstring ablation, a total-resource comparison, and a decisive instance. None had been met as of 2026-09-26.
