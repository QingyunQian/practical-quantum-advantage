---
type: question
id: ideal-sqd-vs-classical-selection
title: Does ideal SQD sampling ever beat classical determinant selection?
title_zh: 理想的 SQD 采样有没有可能胜过经典行列式选择？
summary: Given a perfect sampler of the exact ground state, is there any Hamiltonian family for which the sampled subspace reaches a target accuracy with fewer determinants than HCI/CIPSI selection or than sorting exact amplitudes, by a margin that grows with system size?
summary_zh: 假设有完美的精确基态采样器，是否存在某类哈密顿量，使采样子空间达到目标精度所需的行列式数量比 HCI/CIPSI 选择或按精确振幅排序更少，且差距随体系增大？
status: seed
last_verified: 2026-09-26
question:
  what_would_settle_it: "A size-scan (e.g. Hubbard cylinders 4×L, Heisenberg ladders, or Fe–S model Hamiltonians up to ~30 orbitals) reporting K(ε) for exact sampling, top-|c| selection and HCI at equal K. A single family where the ratio K_HCI / K_sample grows with size would revive the method; a null result across families closes it."
  difficulty: month
  resolved: false
related:
  methods: [sqd]
  problems: [ground-state-energy]
---

## Why it matters

SQD is the method behind IBM's quantum-centric supercomputing programme and its 12,000-atom protein demonstration. Every argument for it assumes the quantum sampler finds a better subspace than classical selection. The ideal-sampler test is the cleanest way to check the premise independently of hardware noise and circuit quality.

## What is known

- This repository's test on the 4×3 half-filled Hubbard model (`numerics/sqd_ideal_test.py`): exact sampling, top-|c| selection and HCI give the same energy-vs-K curve at U/t = 4 and U/t = 8; at U/t = 4 the state is diffuse enough that 16% of the full space still leaves 0.04 t per site of error.
- Gaberle and Jattana (arXiv:2605.02494) sample exact ground states of Heisenberg and Hubbard lattices and find K(ε) grows exponentially with size even under optimal ordering. They do not compare to HCI.

## What would settle it

See the front matter. The comparison must be at equal K and equal ε, after symmetry-adapted configuration recovery on both sides, on at least three sizes per family. Plots of K(ε, N) for the three selection rules, plus the ratio, are the deliverable. Code in `numerics/` can be extended; Hubbard models are handled with `quimb` + sparse Lanczos, and molecular Hamiltonians would need PySCF integrals.

## Who could take it

Anyone with a workstation. A full scan is a month of work; a PRB-style negative result is publishable.
