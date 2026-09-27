---
type: problem
id: sparse-linear-systems
title: Sparse linear systems and quantum linear algebra
title_zh: 稀疏线性方程组与量子线性代数
summary: Matrix inversion has a BQP-complete quantum-native formulation, while polylog(N) linear-system algorithms need efficient input preparation, operator access, bounded condition number and limited output. Low-rank and specified constant-precision routes have classical counterparts; active-QRAM opportunity costs narrow many classical-data proposals without proving a universal no-go. No named industrial instance in the remaining window has a matched economic comparison.
summary_zh: 矩阵求逆在量子输入输出的定义下是 BQP 完全问题；线性方程组算法若要达到 polylog(N) 规模，还需要高效制备输入、访问算子、控制条件数并限制输出。低秩及特定常数精度任务已有经典对应算法；主动式 QRAM 的硬件机会成本削弱了许多经典数据方案，但未构成普遍不可能性证明。剩余窗口中尚无具名工业实例完成同任务的经济比较。
status: seed
last_verified: 2026-09-27
verdict: surviving
dimensions:
  classical_hardness: {level: reduction, note: "BQP-complete in the worst case (HHL), but only with quantum-native input and output; for the systems engineering produces, conjugate gradient and multigrid run in O(N √κ) or O(N) and are not obstructed"}
  quantum_easiness: {level: conditional, note: "needs a sparse or block-encodable A, a |b> preparable in polylog time, condition number κ = polylog(N), and a scalar functional of x as output; optimal query cost O(κ log 1/ε) (Costa et al.)"}
  willingness_to_pay: {level: second-hand, note: "engineering demand for faster large solves is universal; the only costed instance (radar cross-section) has no buyer statement, and structural FEM proposals claim no practical advantage"}
resources: {gates: "depth 1e25 (oracle excluded) to 1e29 (oracle included)", note: "the one compiled instance, 2D RCS with N=3.3e8 at accuracy 0.01 (Scherer et al.)"}
related:
  applications: [radar-cross-section, weather-forecasting, turbulence-cfd]
  problems: [pde-solving, classical-data-machine-learning, sorting-fft-storage]
  methods: [hhl-qsvt, qram]
references:
  - {arxiv: "0811.3171", title: "Quantum algorithm for solving linear systems of equations", authors: "A. W. Harrow, A. Hassidim, S. Lloyd", year: 2009, note: "Phys. Rev. Lett. 103, 150502; includes the BQP-completeness of matrix inversion"}
  - {doi: "10.1038/nphys3272", title: "Read the fine print", authors: "S. Aaronson", year: 2015, note: "Nature Physics 11, 291; the four conditions"}
  - {arxiv: "2111.08152", title: "Optimal scaling quantum linear systems solver via discrete adiabatic theorem", authors: "P. C. S. Costa, D. An, Y. R. Sanders, Y. Su, R. Babbush, D. W. Berry", year: 2022, note: "O(κ log 1/ε) query complexity"}
  - {arxiv: "1807.04271", title: "A quantum-inspired classical algorithm for recommendation systems", authors: "E. Tang", year: 2019, note: "STOC 2019; sampling-based dequantization of low-rank linear algebra"}
  - {arxiv: "1910.06151", title: "Sampling-based sublinear low-rank matrix arithmetic framework for dequantizing quantum machine learning", authors: "N.-H. Chia, A. Gilyén, T. Li, H.-H. Lin, E. Tang, C. Wang", year: 2020, note: "STOC 2020"}
  - {arxiv: "2111.09079", title: "Dequantizing the Quantum Singular Value Transformation: Hardness and Applications to Quantum Chemistry and the Quantum PCP Conjecture", authors: "S. Gharibian, F. Le Gall", year: 2023, note: "SIAM J. Comput. 52, 1009; constant-precision sparse QSVT dequantized, 1/poly precision BQP-complete"}
  - {arxiv: "2305.10310", title: "QRAM: A Survey and Critique", authors: "S. Jaques, A. G. Rattew", year: 2025, note: "Quantum 9, 1922; opportunity-cost argument against active QRAM"}
  - {arxiv: "1512.05903", title: "Quantum algorithms and the finite element method", authors: "A. Montanaro, S. Pallister", year: 2016, note: "Phys. Rev. A 93, 032324"}
  - {arxiv: "1505.06552", title: "Concrete resource analysis of the quantum linear system algorithm used to compute the electromagnetic scattering cross section of a 2D target", authors: "A. Scherer et al.", year: 2017, note: "Quantum Inf. Process. 16, 60"}
  - {arxiv: "2510.07280", title: "End-to-End Quantum Algorithm for Topology Optimization in Structural Mechanics", authors: "L. Hölscher, O. Ahrend, L. Karch, C. L'Estocq, M. Marfany Andreu, et al.", year: 2026, note: "Quantum Sci. Technol. 11, 025029; Grover outer loop plus QSVT inversion, no practical advantage claimed"}
---

## Best classical

For sparse symmetric positive-definite systems, conjugate gradient converges in O(√κ log 1/ε) matrix-vector products, each O(N s) for sparsity s; for the elliptic operators of engineering, multigrid preconditioning brings the whole solve to O(N) up to logarithms. These are the solvers behind every FEM and CFD code, and they output the full solution vector, which is what the caller usually wants. For low-rank or sampling-accessible matrices, Tang's algorithm and the Chia et al. framework compute the same quantities the quantum algorithms promise in time polylogarithmic in N, so the exponential separation vanishes [4, 5]. For sparse matrices Gharibian and Le Gall dequantize the singular-value transformation at constant precision [6]; only 1/poly precision remains BQP-complete.

## Best quantum

Harrow, Hassidim and Lloyd prepare |x⟩ ∝ A⁻¹|b⟩ in time polylog(N) × poly(κ, 1/ε) and show that matrix inversion (with quantum input and output) is BQP-complete [1]. Costa et al. bring the query complexity to O(κ log 1/ε) in their oracle model [3]. The "fine print" [2]: (i) |b⟩ must be preparable in polylog time, for example from an efficient circuit; an arbitrary length-N file does not supply this for free; (ii) A must be sparse or otherwise block-encodable with polylog cost; (iii) κ must be polylog(N) for a polylog overall bound; (iv) the output is a state, so reading all N components costs at least Ω(N), while a specified expectation value may be cheaper. Failure of one condition invalidates that *particular exponential end-to-end claim*, not every possible polynomial gain. For active QRAM, Jaques and Rattew show that accounting for control hardware and an equally resourced classical comparator removes most asymptotic advantage in the linear-algebra settings they analyse, with architectural qualifications [7].

## Where the conditions might hold

Discretised PDEs with a formula-defined source and a single response functional. Montanaro and Pallister analyse exactly this for FEM and find a polynomial speedup growing with dimension, with evidence against super-polynomial gains at fixed dimension for smooth solutions [8]. The one instance carried to gate level, the radar cross-section, gives circuit depth 1e25 without and 1e29 with the geometry oracle [9]. Structural compliance and topology optimisation (Hölscher et al.) wrap a QSVT inversion in a Grover outer loop and claim no practical advantage [10]. Circuit simulation (SPICE-type) fails condition (i) because each step's right-hand side is the previous step's full solution, which would have to be read out. Machine-learning uses fail (i) and (ii) through the QRAM argument and are catalogued under [classical-data machine learning](classical-data-machine-learning.html).

## Verdict

Surviving for a narrow input/output model, with no identified industrial advantage. BQP-completeness concerns quantum-native input and output at suitable precision; it cannot be transferred to a classical engineering file. The four algorithmic conditions and active-QRAM costs rule out many proposed exponential claims. A sparse, high-rank, well-conditioned, efficiently specified system with a limited output remains a possible target. The only compiled industrial example here has an uneconomic depth estimate under its assumptions [9]. A matched public instance and total cost curve could change this assessment; the existing dequantization results do not prove a universal no-go for every linear-system formulation.
