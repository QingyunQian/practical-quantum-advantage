---
type: problem
id: sparse-linear-systems
title: Sparse linear systems and quantum linear algebra
title_zh: 稀疏线性方程组与量子线性代数
summary: Matrix inversion is BQP-complete and the HHL family solves it in polylog(N) time, but only under four conditions on input preparation, block encoding, condition number and output. Low-rank cases are dequantized (Tang, Chia et al.), constant-precision sparse QSVT is dequantized (Gharibian–Le Gall), and active QRAM removes the rest of the asymptotic advantage. The surviving window is sparse, high-rank, well-conditioned systems with formula-defined input and a scalar output, and no industrial instance in it has an economic resource estimate.
summary_zh: 矩阵求逆是 BQP 完全问题，HHL 一族能以 polylog(N) 时间求解，但要满足输入制备、块编码、条件数、输出这四个条件。低秩情形已被去量子化（Tang、Chia 等），常数精度的稀疏 QSVT 已被去量子化（Gharibian–Le Gall），主动式 QRAM 抹掉了其余的渐近优势。幸存的窗口是稀疏、高秩、良态、输入由公式定义、输出为标量的方程组，其中没有一个工业实例有经济的资源估计。
status: seed
last_verified: 2026-09-26
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

Harrow, Hassidim and Lloyd prepare |x⟩ ∝ A⁻¹|b⟩ in time polylog(N) × poly(κ, 1/ε) and show that matrix inversion (with quantum input and output) is BQP-complete [1]. Costa et al. bring the query complexity to the optimal O(κ log 1/ε) [3]. The "fine print" [2]: (i) |b⟩ must be preparable in polylog time, so b must come from a formula, not a file; (ii) A must be sparse or otherwise block-encodable with polylog cost; (iii) κ must be polylog(N), since κ enters at least linearly; (iv) the output is the state, so reading x costs Ω(N) and only a scalar functional ⟨x|M|x⟩ is cheap. Any one of these failing removes the exponential advantage. Jaques and Rattew add that if the input is loaded through active QRAM, the control hardware that operates the QRAM could instead run a highly parallel classical algorithm equally fast, and they prove that most asymptotic advantage in quantum linear algebra disappears under active QRAM [7].

## Where the conditions might hold

Discretised PDEs with a formula-defined source and a single response functional. Montanaro and Pallister analyse exactly this for FEM and find a polynomial speedup growing with dimension, with evidence against super-polynomial gains at fixed dimension for smooth solutions [8]. The one instance carried to gate level, the radar cross-section, gives circuit depth 1e25 without and 1e29 with the geometry oracle [9]. Structural compliance and topology optimisation (Hölscher et al.) wrap a QSVT inversion in a Grover outer loop and claim no practical advantage [10]. Circuit simulation (SPICE-type) fails condition (i) because each step's right-hand side is the previous step's full solution, which would have to be read out. Machine-learning uses fail (i) and (ii) through the QRAM argument and are catalogued under [classical-data machine learning](classical-data-machine-learning.html).

## Verdict

Surviving, in the narrowest sense the catalogue allows. Classical hardness holds only for the quantum-native formulation (BQP-completeness with 1/poly precision), which no engineering caller uses; the quantum precondition is a conjunction of four conditions that real problems violate one at a time; willingness to pay is generic rather than stated. Nothing forbids an instance that is sparse, high-rank, well-conditioned, formula-defined and scalar-output, but the only compiled candidate is uneconomic by many orders of magnitude, and the polynomial gains that remain do not pay under error correction. The page would move to promising if such an instance were exhibited with an end-to-end estimate; it would move to no-go if the remaining sparse, 1/poly-precision window were dequantized for the operator classes engineering produces.
