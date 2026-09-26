---
type: problem
id: integer-factoring-hidden-subgroup
title: Integer factoring, discrete logarithms and abelian hidden subgroup problems
title_zh: 整数分解、离散对数与交换群隐子群问题
summary: Shor's family is the one superpolynomial speedup whose classical hardness is backed by fifty years of number theory and the entire public-key ecosystem. Regev's lattice variant is now unconditionally correct (Pilatte 2024), Gidney's 2025 estimate breaks RSA-2048 with under one million noisy qubits in a week, and class groups, unit groups and S-units of number fields are polynomial too. The buyer is cryptanalysis; outside it there is no commercial use.
summary_zh: Shor 一族是唯一一个超多项式加速，其经典困难性有五十年数论研究和整个公钥密码生态背书。Regev 的格版本已被 Pilatte 无条件证明正确，Gidney 2025 年估计用不到一百万个含噪比特一周内破解 RSA-2048，数域的类群、单位群和 S-单位群也是多项式时间。买家是密码分析；此外没有商业用途。
status: seed
last_verified: 2026-09-26
verdict: promising
dimensions:
  classical_hardness: {level: crypto, note: "no reduction and no oracle separation; best classical is the number field sieve at exp(O~(n^1/3)); hardness is the assumption behind RSA, Diffie–Hellman and ECC"}
  quantum_easiness: {level: proven, note: "Shor 1994; Regev's O(n^3/2)-gate variant proven correct unconditionally by Pilatte; abelian HSP fully polynomial; unit and S-unit groups of arbitrary-degree number fields polynomial"}
  willingness_to_pay: {level: first-hand, note: "governments: NIST's 2024 post-quantum standards (FIPS 203) state that a cryptographically relevant quantum computer motivates migration; the paying customer is a security agency, not industry"}
resources: {logical_qubits: "~1,400 (RSA-2048)", gates: "~6.5e9 Toffoli", note: "Gidney 2025: under 1e6 physical qubits, under one week, surface code at 1e-3 physical error; number-field class-group instances need comparable counts and have no Gidney-level optimisation"}
related:
  applications: [cryptanalysis]
  problems: [combinatorial-optimization, representation-theory-multiplicities]
  methods: [phase-estimation, dqi]
  questions: [first-hand-payment-evidence]
references:
  - {arxiv: "2308.06572", title: "An Efficient Quantum Factoring Algorithm", authors: "O. Regev", year: 2023}
  - {arxiv: "2310.00899", title: "Space-Efficient and Noise-Robust Quantum Factoring", authors: "S. Ragavan, V. Vaikuntanathan", year: 2023}
  - {arxiv: "2404.16450", title: "Unconditional correctness of recent quantum algorithms for factoring and computing discrete logarithms", authors: "C. Pilatte", year: 2024, note: "Forum Math. Pi 14, e5 (2026)"}
  - {arxiv: "2505.15917", title: "How to factor 2048 bit RSA integers with less than a million noisy qubits", authors: "C. Gidney", year: 2025}
  - {arxiv: "2510.02280", title: "An efficient quantum algorithm for computing S-units and its applications", authors: "J.-F. Biasse, F. Song", year: 2025}
  - {title: "Module-Lattice-Based Key-Encapsulation Mechanism Standard (FIPS 203)", authors: "National Institute of Standards and Technology", year: 2024, doi: "10.6028/NIST.FIPS.203"}
---

## Best classical

The general number field sieve factors an n-bit integer in exp(Õ(n^{1/3})) time, and no 2048-bit RSA modulus has been factored classically. Discrete logarithms in prime fields sit at the same complexity; elliptic-curve discrete logarithms have only generic square-root algorithms, which is why 256-bit curves suffice classically. For number fields, Buchmann-type subexponential algorithms compute class groups and unit groups under GRH and degrade with degree; computer-algebra systems struggle beyond discriminants around 10⁶⁰. No lower bound exists for any of these problems. The hardness evidence is that fifty years of algorithmic number theory have not broken the subexponential wall, and that the world's public-key infrastructure is priced on that failure.

The one attempted classical-side surprise ran the other way: Yilei Chen's April 2024 claim of a polynomial quantum algorithm for approximate LWE had an unfixable bug found within nine days, so lattice cryptography remains quantum-safe and the post-quantum migration rests on it.

## Best quantum

Shor's algorithm (1994) factors and takes discrete logarithms in polynomial time via period finding, an instance of the abelian hidden subgroup problem, which is polynomial in full generality. Since 2023 the algorithm has been re-engineered. Regev's multidimensional variant uses O(n^{3/2}) gates per run at the cost of O(n^{3/2}) qubits and a number-theoretic heuristic [1]; Ragavan and Vaikuntanathan reduced the space to Õ(n) qubits and added noise robustness [2]; and Pilatte proved the heuristic unconditionally, so correctness no longer rests on a conjecture [3]. On the engineering side, Gidney's 2025 estimate breaks RSA-2048 with fewer than one million noisy physical qubits in under a week, a 20-fold reduction from the 2019 estimate, using approximate residue arithmetic, yoked surface codes and magic-state cultivation [4].

Beyond factoring, Hallgren (2002) and Eisenträger, Hallgren, Kitaev and Song (2014) gave polynomial-time algorithms for unit groups and class groups of number fields of arbitrary degree via a continuous hidden-subgroup problem, and Biasse and Song give an explicitly quantified polynomial algorithm for S-unit groups, the engine behind principal-ideal and class-group discrete-logarithm problems and the first step in attacks on Ideal-SVP lattice assumptions [5]. For a fault-tolerant machine these are the most directly useful results for pure mathematics: class-number tables, tests of Cohen–Lenstra heuristics, numerical evidence for Stark's conjectures. No Gidney-level resource optimisation exists for them; the gap is a concrete open task.

## Who pays

Security agencies and the organisations they oblige to migrate. NIST's FIPS 203 standard for post-quantum key encapsulation (August 2024) states in its own text that the prospect of a cryptographically relevant quantum computer motivates the transition [6]; that is a buyer speaking, though a buyer for defence rather than for the computation itself. Outside cryptanalysis, and outside computational number theory as a research tool, no commercial use is known.

## Verdict

Promising, in the narrow sense that hardness evidence (cryptographic), quantum easiness (proven, now unconditional) and a first-hand buyer (state cryptanalysis and the migration it forces) all exist. It is also the least interesting entry for a company looking for a market: the resource requirement is about 1,400 logical qubits and 6.5×10⁹ Toffoli gates for RSA-2048 [4], an order of magnitude beyond the 2029 roadmaps, and the value realised by everyone else is negative. What would change the page: a classical subexponential-to-polynomial breakthrough (none in sight), or a demonstrated commercial use of class-group computation.
