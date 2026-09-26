---
type: claim
id: qctrl-fermi-hubbard-2026
title: Q-CTRL 120-qubit 1D Fermi–Hubbard, "three orders of magnitude faster than TDVP"
title_zh: Q-CTRL 120 比特一维 Fermi–Hubbard，“比 TDVP 快近三个数量级”
summary: Hartnett et al. simulated one-dimensional Fermi–Hubbard quench dynamics on up to 120 superconducting qubits and reported the processor was nearly three orders of magnitude faster than tensor-network TDVP at equal evolution time. One month later, Rausch et al. converged the same window on GPUs with bond dimension around 62,000 in about 100 minutes, reducing the quoted 3000× to about 36×.
summary_zh: Hartnett 等在最多 120 个超导比特上模拟一维 Fermi–Hubbard 淬火动力学，宣称同等演化时间下处理器比张量网络 TDVP 快近三个数量级。一个月后，Rausch 等用 GPU 张量网络（键维约 62,000）在约 100 分钟内完全收敛同一窗口，把 3000 倍压到约 36 倍。
status: reviewed
last_verified: 2026-09-26
claim:
  claimant: Q-CTRL (Hartnett et al.)
  date: 2026-05
  statement: "Fast, accurate, high-resolution simulation of large-scale 1D Fermi–Hubbard dynamics on up to 120 qubits, beyond exact classical methods and nearly three orders of magnitude faster than classical tensor-network (TDVP) simulation at the same evolution time."
  hardware: IBM Heron (superconducting), with Q-CTRL error suppression
  qubits: 120
  refuted: true
  refutation_date: 2026-06
  refuted_by: "Rausch, Singh, Jahromi, Kshetrimayum, Orús (GPU tensor network with symmetries, χ≈62,000, fully converged in ~100 minutes)"
  time_to_refute: "one month"
related:
  problems: [quench-dynamics]
  methods: [error-mitigation]
  claims: [ibm-kicked-ising-utility-2023]
references:
  - {arxiv: "2605.04025", title: "Fast, accurate, high-resolution simulation of large-scale Fermi-Hubbard models on a digital quantum processor", authors: "G. S. Hartnett, K. S. Najafi, A. Khindanov, H. Liao, M. Schutzman, M. R. Hush, M. J. Biercuk, Y. Baum", year: 2026}
  - {arxiv: "2606.04771", title: "Pushing the Classical Frontier of 1D Fermi-Hubbard Quench Dynamics Beyond Current Quantum Simulations", authors: "R. Rausch, S. Singh, S. S. Jahromi, A. Kshetrimayum, R. Orús", year: 2026}
---

## Claim

Hartnett et al. ran Trotterized quench dynamics of the one-dimensional Fermi–Hubbard model on up to 120 qubits of a superconducting processor with Q-CTRL's error-suppression stack, and compared wall-clock time against a tensor-network TDVP simulation of the same evolution. They reported quantitative agreement with approximate classical results where those converge, dynamics beyond exact classical methods, and a speed advantage of nearly three orders of magnitude over the tensor-network reference at equal evolution time [1]. The TDVP reference took more than 160 hours.

## Refutation

- Rausch, Singh, Jahromi, Kshetrimayum and Orús reran the same 1D quench with a GPU-accelerated, symmetry-exploiting tensor network, reaching bond dimension χ ≈ 62,000 and fully converged results over the whole simulation window in about 100 minutes, which reduces the claimed 3000× to about 36× [2]. The preprint appeared on 2026-06-03, one month after the claim.
- The residual 36× is a wall-clock comparison between an error-suppressed sampling run and a single-GPU tensor-network run; it is not a scaling separation. In one dimension the classical cost of a quench is exponential in time but independent of system length (see this repository's calibration in `quench-dynamics`), so adding qubits along a chain does not add classical difficulty.

## Lesson for the catalogue

Qubit count on a chain is not a hardness parameter. The catalogue's standard for a dynamics claim is a two-dimensional (or three-dimensional) clean lattice at times where the entanglement entropy per boundary bond exceeds what any tensor network can hold; 1D Hubbard at 120 sites does not meet it, and the refutation needed no new idea, only a bigger bond dimension on a GPU.
