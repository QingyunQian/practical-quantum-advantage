---
type: method
id: hhl-qsvt
title: Quantum linear-system solvers (HHL, QSVT)
title_zh: 量子线性方程组求解（HHL、QSVT）
summary: Apply a matrix function to a quantum state in time polylogarithmic in dimension. The exponential speedup survives only for matrices that are sparse (or efficiently block-encoded), well-conditioned, with a compactly preparable right-hand side and a single scalar functional as output. Low-rank inputs are dequantized (Tang; Chia et al.), constant-precision sparse QSVT is dequantized (Gharibian–Le Gall), and the one concrete industrial estimate, a radar cross-section calculation, needs circuit depth ~10²⁹ once the geometry oracle is counted.
summary_zh: 用多项式对数于维度的时间把矩阵函数作用在量子态上。指数加速只在矩阵稀疏（或有高效块编码）、条件数良好、右端项可紧凑制备、输出仅为单个标量泛函时幸存。低秩输入已被去量子化（Tang；Chia 等），常数精度的稀疏 QSVT 已被去量子化（Gharibian–Le Gall），唯一具体的工业估算是雷达散射截面计算，计入几何 oracle 后电路深度约 10²⁹。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: reduction, note: "the matrix-inversion problem is BQP-complete in the sparse, 1/poly-precision setting; but low-rank and constant-precision cases are classically polynomial, and no industrial instance is known to sit in the hard corner"}
  quantum_easiness: {level: conditional, note: "polylog(N) given sparsity, condition number κ = polylog, compact |b⟩ and scalar output; geometrically local linear dynamics is additionally dequantized at short times (Sakamoto–Fujii)"}
  willingness_to_pay: {level: second-hand, note: "radar and FEM users exist, but the only concrete estimate (Scherer et al.) was an academic resource count; RAND 2026 judges near-term use unlikely"}
resources: {logical_qubits: "~1e8 wide (RCS with oracle)", gates: "depth ~1e25 without the oracle, ~1e29 with it", note: "Scherer et al. 2017: 2D scattering target, N = 3.3e8 unknowns, precision 0.01"}
related:
  problems: [sparse-linear-systems, pde-solving, classical-data-machine-learning]
  applications: [radar-cross-section, turbulence-cfd, weather-forecasting]
  methods: [qram, grover-amplitude-estimation]
references:
  - {arxiv: "0811.3171", title: "Quantum algorithm for solving linear systems of equations", authors: "A. W. Harrow, A. Hassidim, S. Lloyd", year: 2009}
  - {arxiv: "1910.06151", title: "Sampling-based sublinear low-rank matrix arithmetic framework for dequantizing quantum machine learning", authors: "N.-H. Chia et al.", year: 2020, note: "STOC 2020"}
  - {arxiv: "2111.09079", title: "Dequantizing the Quantum Singular Value Transformation: Hardness and Applications to Quantum Chemistry and the Quantum PCP Conjecture", authors: "S. Gharibian, F. Le Gall", year: 2022, note: "STOC 2022; SIAM J. Comput. 52(4) (2023)"}
  - {arxiv: "1505.06552", title: "Concrete resource analysis of the quantum linear system algorithm used to compute the electromagnetic scattering cross section of a 2D target", authors: "A. Scherer et al.", year: 2017, note: "Quantum Inf. Process. 16, 60"}
  - {arxiv: "2505.10445", title: "On the quantum computational complexity of classical linear dynamics with geometrically local interactions: Dequantization and universality", authors: "K. Sakamoto, K. Fujii", year: 2026, note: "Quantum 10, 2182"}
  - {arxiv: "2307.09593", title: "Limitations for Quantum Algorithms to Solve Turbulent and Chaotic Systems", authors: "D. Lewis, S. Eidenbenz, B. Nadiga, Y. Subaşı", year: 2024, note: "Quantum 8, 1509"}
---

## How it works

Given a block encoding of a matrix A and a state |b⟩, HHL [1] and its successor, the quantum singular value transformation (QSVT), prepare a state proportional to f(A)|b⟩ for a polynomial approximation f of 1/x (or any bounded function) using O(κ · polylog(N/ε)) applications of the block encoding, where κ is the condition number. The output is a quantum state; a scalar ⟨b|A⁻¹|b⟩ or a few expectation values can then be estimated to precision ε with O(1/ε) further work. Reading out the full solution vector costs Ω(N).

## Preconditions

Aaronson's "fine print" from 2015 remains the checklist:

1. **Sparse or efficiently block-encodable A.** A d-sparse matrix given by an oracle, or a structured operator with a known circuit. A dense matrix stored as data needs QRAM and loses the speedup at loading time.
2. **Condition number κ = polylog(N).** Runtime is linear in κ (up to log factors); for finite-element or finite-difference discretisations κ grows as h⁻², i.e. polynomially in N.
3. **Compact input.** |b⟩ must be preparable in polylog time (a formula, not a data vector).
4. **Scalar output.** One functional of the solution, at inverse-polynomial precision. The last qualifier is not optional: at constant precision the sparse case is classically easy.

## Known limits

- **Low rank is dequantized.** Tang's 2018 recommendation-system algorithm and the general framework of Chia et al. [2] give classical algorithms polylogarithmic in dimension for low-rank matrices with sample-and-query access, which covers most quantum machine-learning proposals built on HHL.
- **Constant precision is dequantized even for sparse matrices.** Gharibian and Le Gall show that QSVT on sparse block encodings can be classically simulated in polynomial time at constant precision, and that the inverse-polynomial-precision case is BQP-complete [3]. The hard window is therefore high precision on sparse, high-rank operators.
- **Geometrically local linear dynamics is dequantized.** Sakamoto and Fujii prove that classical linear dynamics with geometrically local interactions (wave, heat, coupled oscillators on lattices) can be simulated classically in polynomial time for short evolution times, leaving at most a polynomial speedup in that setting [5]. Nonlinear and chaotic dynamics fare worse: Lewis et al. show any algorithm outputting the state |u(t)⟩ of a system with a positive Lyapunov exponent costs exp(Ω(T)) [6].
- **The one concrete industrial count is far out of reach.** Scherer et al. compiled the linear-system algorithm for the electromagnetic scattering cross section of a 2D target with N = 3.3 × 10⁸ unknowns at precision 0.01: circuit depth about 10²⁵ without the geometry oracle, and width about 10⁸ with depth about 10²⁹ once the oracle for the discretised geometry is included [4]. The oracle, not the solver, dominates. Heat and option PDEs in d ≥ 2 are known to gain at most a quadratic factor in ε; FEM compliance calculations stack a Grover outer loop on a QSVT inner loop and their authors claim no practical advantage.

## Verdict

Surviving, in a corner nobody has yet populated with an industrial problem. The BQP-completeness of sparse matrix inversion at inverse-polynomial precision is a genuine hardness result, and the algorithm is polynomial when the four preconditions hold. But every application examined for this catalogue fails at least one of them: dense or data-defined inputs (electronic circuits, ML), polynomial κ (FEM), full-field output (CFD), or an input oracle whose cost swamps the solver (radar). The closest match found is a single-receiver wave-equation response, where the medium is still data and Sakamoto–Fujii caps the gain at polynomial. What would change the verdict: a sparse, well-conditioned operator defined by a formula, whose one scalar output someone pays for at high precision, with a resource count under 10¹² gates.
