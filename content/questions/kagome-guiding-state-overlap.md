---
type: question
id: kagome-guiding-state-overlap
title: Can symmetry-selected guiding states keep the kagome ground-state overlap ≥ 1/poly?
title_zh: 按对称扇区挑选的引导态能否让 kagome 基态重叠保持在 1/poly 以上？
summary: The spin-1/2 kagome Heisenberg antiferromagnet on 48 to 108 sites is the smallest natural candidate for a guided ground-state problem in BQP. Exact diagonalisation on 12/18/24-site periodic clusters shows a naive dimer guiding state hits a symmetry-sector level crossing at 24 sites (overlap exactly zero) and the best dimer covering's overlap decays as exp(−0.13N), about 1e-6 at 100 sites. Does choosing the guiding state by symmetry sector, or using RVB/Gutzwiller states, keep the overlap at 1/poly so that filtering phase estimation is polynomial?
summary_zh: 48 到 108 格点的自旋 1/2 kagome 海森堡反铁磁体是引导基态问题落入 BQP 的最小自然候选。12/18/24 格点周期团簇的精确对角化表明，随手选的二聚体引导态在 24 格点处遇到对称扇区能级交叉（重叠严格为零），最优覆盖的重叠按 exp(−0.13N) 衰减，100 格点时约 1e-6。按对称扇区挑选引导态或改用 RVB/Gutzwiller 态，能否把重叠保持在 1/poly，使滤波相位估计保持多项式？
status: seed
last_verified: 2026-09-26
question:
  what_would_settle_it: "Overlap |<φ|ψ0>|² versus N for N = 12, 18, 24, 27, 36 (and 48 with symmetry-reduced Lanczos) for three guiding families: best dimer covering restricted to the ground-state momentum and point-group sector, nearest-neighbour RVB, and Gutzwiller-projected Dirac spin liquid. A fitted decay rate α with αN ≤ 20 at N = 100 (overlap ≥ 1e-9, amplitude amplification affordable) settles it positively; α ≥ 0.1 for all three families settles it negatively. The Lin–Izmaylov moment bound should be reported alongside the exact overlap so that the certificate is computable when ED is not."
  difficulty: phd
  resolved: false
related:
  problems: [ground-state-energy]
  methods: [phase-estimation]
  questions: [ideal-sqd-vs-classical-selection]
references:
  - {arxiv: "2111.09079", title: "Dequantizing the Quantum Singular Value Transformation: Hardness and Applications to Quantum Chemistry and the Quantum PCP Conjecture", authors: "S. Gharibian, F. Le Gall", year: 2022}
  - {arxiv: "2207.10250", title: "Improved Hardness Results for the Guided Local Hamiltonian Problem", authors: "C. Cade, M. Folkertsma, S. Gharibian et al.", year: 2023}
  - {arxiv: "2411.16163", title: "A Dequantized Algorithm for the Guided Local Hamiltonian Problem", authors: "Y. Zhang, Y. Wu, X. Yuan", year: 2024}
  - {arxiv: "2503.12224", title: "Bounding Eigenstate Overlap from Hamiltonian Moments: Success Probability Guarantees for Quantum Phase Estimation", authors: "J. Lin, A. F. Izmaylov", year: 2025}
  - {arxiv: "1011.6114", title: "Spin Liquid Ground State of the S=1/2 Kagome Heisenberg Model", authors: "S. Yan, D. A. Huse, S. R. White", year: 2011, note: "Science 332, 1173 (2011)"}
  - {arxiv: "1611.06990", title: "The S=1/2 Kagome Heisenberg Antiferromagnet Revisited", authors: "A. M. Läuchli, J. Sudan, R. Moessner", year: 2019, note: "PRB 100, 155142 (2019); 48-site ED in sectors of dimension 5e11"}
---

## Why it matters

Guided local Hamiltonian problems are BQP-complete at inverse-polynomial precision [1, 2] and classically approximable only at constant precision [3]. The theorems do not say which physical Hamiltonians are hard; they say that a quantum computer solves any instance whose guiding state has overlap ≥ 1/poly with the ground state. The kagome antiferromagnet is the natural place to test this: one qubit per site, so 48 to 108 sites fits a 50 to 100 logical-qubit machine; a sign problem blocks QMC; DMRG cylinders are limited to circumference about 17 [5]; exact diagonalisation stops at 48 sites [6]; and the nature of the ground state (Z2 versus U(1) Dirac spin liquid) is still argued. The classical-hardness certificate is as good as any empirical one in the catalogue. The missing half is the quantum-easiness certificate, i.e. the overlap.

## What is known

This repository's exact diagonalisation (`numerics/kagome_path_gap.py`, `numerics/kagome_covering_scan.py`; figure `numerics/figs/fig4_kagome_certificate.png`) followed the path H(λ) = Σ_dimer S·S + λ Σ_other S·S from a dimer product state (λ = 0) to the uniform kagome Heisenberg model (λ = 1) on periodic clusters of 12, 18 and 24 sites (Sz = 0 sector, dimension 2.7×10^6 at 24 sites):

| N | E0/N at λ=1 | minimum gap along path (J) | overlap of the naive covering | best of all coverings (32/119/230 scanned) |
|---|---|---|---|---|
| 12 | −0.45374 | 0.116 | 0.125 | 0.125 |
| 18 | −0.44713 | 0.034 | 0.0010 | 0.069 |
| 24 | −0.44833 | 0.054 (0.065 at λ=0.9) | 0 (level crossing) | 0.026 |

Energies agree with published ED values (thermodynamic limit −0.4386). Three observations. (i) At 24 sites the tracked state undergoes a level crossing with a state in a different symmetry sector for λ ∈ (0.9, 1); the end overlap is exactly zero. This is a discrete orthogonality catastrophe, set by symmetry, not a continuous one. (ii) The best covering's overlap decays as roughly exp(−0.13N): 0.125 → 0.069 → 0.026, extrapolating to about 1e-6 at N = 100, which amplitude amplification could absorb at about 10^3 repetitions, provided the best covering can be identified without knowing the ground state. (iii) The path gap is 0.03 to 0.12 J and non-monotonic in N, consistent with the known singlet sea of finite kagome spectra; if the gap closes in the thermodynamic limit (Dirac scenario), adiabatic preparation is out and filtering phase estimation with a guiding state is the only route.

![Kagome path gaps and guiding-state overlaps on small clusters](../figs/fig4_kagome_certificate.png)

[Scripts and raw results](https://github.com/yuchenguommm/practical-quantum-advantage/tree/main/numerics) are included in this repository. These small-cluster data do not establish asymptotic scaling.

## What would settle it

See the front matter. The concrete work: (a) extend to 27 and 36 sites (Sz sector 2×10^7 and 9×10^9; the latter needs matrix-free Lanczos with translation and point-group reduction, as in [6]), (b) restrict the covering scan to the ground-state momentum and point-group sector and report the decay rate of the best in-sector covering, (c) repeat for nearest-neighbour RVB and Gutzwiller-projected states, whose overlap may decay more slowly, (d) report the Lin–Izmaylov moment bound [4] next to the exact overlap at every size, since that bound is what one could compute at 100 sites. Repeat for the breathing path (J_up/J_down) to see whether it keeps a larger gap than the dimerisation path. Scripts in `numerics/` can be extended; 36 sites needs a cluster.

## Who could take it

A PhD student with a 16-core node and access to a larger machine for 36 sites. The negative result (all three families decay with α ≥ 0.1) is publishable and would remove the kagome ground state from the list of minimal-qubit BQP candidates; the positive result gives the first natural Hamiltonian family with both certificates.
