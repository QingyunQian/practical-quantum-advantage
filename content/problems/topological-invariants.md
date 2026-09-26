---
type: problem
id: topological-invariants
title: Topological invariants (Jones polynomial, Turaev–Viro, Witten–Reshetikhin–Turaev)
title_zh: 拓扑不变量（Jones 多项式、Turaev–Viro、Witten–Reshetikhin–Turaev）
summary: Additive approximation of the Jones polynomial at roots of unity (plat closure) and of Turaev–Viro 3-manifold invariants is BQP-complete; exact evaluation is #P-hard for everyone. Quantinuum ran an end-to-end Fibonacci-braid algorithm on H2-2 in 2025 and estimates that about 2,800 crossings at gate fidelity above 99.99% would exceed classical reach. The additive approximation is not what knot theorists need, and no buyer exists.
summary_zh: 单位根处 Jones 多项式（plat 闭包）与 Turaev–Viro 三维流形不变量的加性逼近是 BQP 完全的；精确计算对谁都是 #P 难。Quantinuum 2025 年在 H2-2 上跑了端到端的 Fibonacci 辫子算法，估计门保真度高于 99.99% 时约 2,800 个交叉即可超出经典范围。加性逼近不是纽结理论家需要的量，也没有买家。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: reduction, note: "BQP-complete for plat-closure Jones at roots of unity and for Turaev–Viro invariants; DQC1-complete for trace closure; exact evaluation #P-hard"}
  quantum_easiness: {level: proven, note: "Aharonov–Jones–Landau polynomial-time algorithm; end-to-end compiled and run on Quantinuum H2-2 with verifiable topologically equivalent braids"}
  willingness_to_pay: {level: none, note: "mathematicians want exact values or structural results; additive approximation at the precision the algorithm gives is of little use; no company or agency involved"}
resources: {logical_qubits: "O(number of strands)", gates: "O(crossings)", note: "Quantinuum estimate: ~2,800 crossings beyond classical at >99.99% gate fidelity, NISQ-style with error mitigation; fault-tolerant counts not published"}
related:
  problems: [representation-theory-multiplicities, quench-dynamics]
  methods: [error-mitigation]
  claims: [google-random-circuit-sampling]
references:
  - {url: "https://arxiv.org/abs/quant-ph/0511096", title: "A Polynomial Quantum Algorithm for Approximating the Jones Polynomial", authors: "D. Aharonov, V. Jones, Z. Landau", year: 2006}
  - {url: "https://arxiv.org/abs/quant-ph/0605181", title: "The BQP-hardness of approximating the Jones Polynomial", authors: "D. Aharonov, I. Arad", year: 2006}
  - {arxiv: "0707.2831", title: "Estimating Jones polynomials is a complete problem for one clean qubit", authors: "P. W. Shor, S. P. Jordan", year: 2008}
  - {arxiv: "1003.0923", title: "Approximating Turaev-Viro 3-manifold invariants is universal for quantum computation", authors: "G. Alagic, S. P. Jordan, R. Koenig, B. W. Reichardt", year: 2010}
  - {arxiv: "2503.05625", title: "End-to-End Quantum Algorithms for the Jones Polynomial", authors: "T. Laakkonen, E. Rinaldi, C. N. Self, E. Chertkov, M. DeCross, et al.", year: 2026, note: "PRX Quantum 7, 020355; Quantinuum H2-2"}
  - {arxiv: "2512.19028", title: "Classical and Quantum Algorithms for Topological Invariants of Torus Bundles", authors: "N. A. Colón Vargas, C. Ortiz Marrero", year: 2025}
---

## Best classical

Exact evaluation of the Jones polynomial of a link at a generic root of unity is #P-hard (Jaeger, Vertigan and Welsh 1990), with the known exceptions at the trivial points t ∈ {±1, ±i, e^{±2πi/3}, e^{±πi/3}} where it is polynomial. Practical knot software (Kauffman-bracket state sums, tensor-network contractions of the braid representation) handles knots with tens to a few hundred crossings depending on treewidth; the cost is exponential in the cut width of the diagram, not in the number of crossings, so knots with low-width diagrams remain easy at any size. For 3-manifold invariants the picture is the same: Turaev–Viro and Witten–Reshetikhin–Turaev invariants are #P-hard exactly, and their approximation under topological restrictions (for example torus bundles) can fall back to classical algorithms; Colón Vargas and Ortiz Marrero give both an O(log N)-qubit quantum algorithm and an O(N²) classical one for the torus-bundle case [6], illustrating that the hardness is fragile under restriction.

## Best quantum

Aharonov, Jones and Landau gave a polynomial-time quantum algorithm for the additive approximation of the Jones polynomial at roots of unity, by representing the braid group in the Temperley–Lieb algebra and estimating a matrix element with a Hadamard test [1]. Aharonov and Arad showed the plat-closure version is BQP-complete [2], and Shor and Jordan that the trace-closure version is complete for DQC1, the one-clean-qubit class [3]. Alagic, Jordan, Koenig and Reichardt showed that approximating Turaev–Viro 3-manifold invariants is BQP-complete as well [4]. These are unconditional reductions: a classical polynomial algorithm for plat-closure Jones at these precisions would imply BPP = BQP.

Laakkonen et al. compiled the whole pipeline, from braid word through Fibonacci anyon representation to error-mitigated Hadamard tests, and ran it on Quantinuum's H2-2, using topologically equivalent braids as a built-in verification: two different braid words with the same closure must give the same value. They estimate that knots with roughly 2,800 crossings, at two-qubit gate fidelities above 99.99%, would put the quantum estimate beyond classical simulation [5].

## What survives

The complexity theory is as hard as it gets and the algorithm is demonstrated; the difficulty is precision and demand. The additive error the algorithm guarantees is relative to a normalisation that is exponentially large in the number of strands, so for most knots the approximation carries little information about the polynomial itself; this criticism has been standing since 2006. Knot theorists want exact polynomials or structural theorems, and the connection to Chern–Simons topological field theory, quantum groups and conformal field theory, though real, does not produce a computational customer. Restricted manifold classes where the invariant is classically tractable [6] show the hardness is in the general case, and no natural family of "hard but interesting" knots has been identified.

## Verdict

Surviving, with willingness to pay set to none. Reduction-level hardness and a proven, hardware-demonstrated algorithm [5] make this one of the few problems where the first two dimensions are settled; the third is absent. The page would change if a mathematical or physical question were shown to reduce to a Jones or Turaev–Viro estimate at the precision the quantum algorithm actually provides, on a knot family with no low-width diagram.
