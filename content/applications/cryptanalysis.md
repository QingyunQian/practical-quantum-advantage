---
type: application
id: cryptanalysis
title: Cryptanalysis of RSA and elliptic-curve cryptography
title_zh: RSA 与椭圆曲线密码的破解
summary: Shor gives a proven polynomial-time quantum algorithm for factoring and discrete logarithms; a superpolynomial separation from classical algorithms remains unproved and rests on cryptographic hardness assumptions. Gidney's 2025 RSA-2048 estimate is conditional on a hardware error and speed model. NIST's migration guidance documents defensive demand, not a purchase of quantum attacks.
summary_zh: Shor 已证明量子计算机可以在多项式时间内分解整数、求离散对数；与经典算法之间是否存在超多项式分离尚未证明，困难性依赖密码学假设。Gidney 对 RSA-2048 的 2025 年估计依赖硬件误差率和速度假设。NIST 的迁移指南证明防御需求存在，不能证明有人采购量子攻击。
status: seed
last_verified: 2026-09-27
tags: [out-of-scope-commercial]
verdict: surviving
dimensions:
  classical_hardness: {level: crypto, note: "best known general classical factoring uses subexponential number-field sieve; no unconditional superpolynomial classical lower bound is known"}
  quantum_easiness: {level: proven, note: "Shor's algorithm; Gidney–Ekerå 2019 gives 3n + 0.002 n lg n logical qubits and 0.3 n^3 Toffolis for n-bit RSA; Regev 2023 improves the asymptotics"}
  willingness_to_pay: {level: unknown, note: "NIST IR 8547 is a draft migration plan and documents demand for defensive replacement of vulnerable cryptography. It does not document a buyer or price for running a quantum factoring attack."}
resources: {logical_qubits: "~6,200 (abstract circuit, n=2048)", gates: "~2.6e9 Toffoli", note: "Gidney 2025: under 1e6 physical qubits, under one week, assuming 0.1% gate error, 1 μs surface-code cycle, 10 μs reaction time; Gidney–Ekerå 2019: 2e7 physical qubits, 8 hours"}
related:
  problems: [integer-factoring-hidden-subgroup]
  methods: [phase-estimation]
references:
  - {arxiv: "2505.15917", title: "How to factor 2048 bit RSA integers with less than a million noisy qubits", authors: "C. Gidney", year: 2025}
  - {arxiv: "1905.09749", title: "How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits", authors: "C. Gidney, M. Ekerå", year: 2021, note: "Quantum 5, 433; logical-qubit and Toffoli formulas in n"}
  - {arxiv: "2308.06572", title: "An Efficient Quantum Factoring Algorithm", authors: "O. Regev", year: 2023}
  - {arxiv: "1706.06752", title: "Quantum resource estimates for computing elliptic curve discrete logarithms", authors: "M. Roetteler, M. Naehrig, K. M. Svore, K. Lauter", year: 2017}
  - {url: "https://arxiv.org/abs/quant-ph/9508027", title: "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer", authors: "P. W. Shor", year: 1997, note: "SIAM J. Comput. 26, 1484"}
  - {url: "https://csrc.nist.gov/pubs/ir/8547/ipd", title: "Transition to Post-Quantum Cryptography Standards (NIST IR 8547, initial public draft)", authors: "NIST", year: 2024, note: "proposed defensive transition timeline; not evidence of an offensive buyer"}
---

## Who needs it

Potential offensive users include intelligence and security agencies, but this page has no public procurement record or price for a quantum attack. The defensive customers are visible: operators of public-key infrastructure must prepare to replace vulnerable schemes. NIST IR 8547, still an initial public draft, proposes deprecating 112-bit-strength vulnerable algorithms after 2030 and disallowing them after 2035 [6]. That is evidence of migration demand, not a purchase order for a factoring computation.

## Bottleneck

The best known general-purpose classical factoring algorithm, the number field sieve, has subexponential asymptotic cost; RSA-2048 has not been factored. No theorem excludes a polynomial-time classical factoring algorithm. The task has compact input and output, avoiding the data-loading and readout obstacles of many other proposed applications. Elliptic-curve discrete logarithm is a distinct problem with its own classical algorithms and quantum circuit estimates.

## Computational problems

- [Integer factoring and the hidden subgroup problem](../problems/integer-factoring-hidden-subgroup.html): Shor's algorithm [5] and its descendants; the same period-finding machinery covers finite-field and elliptic-curve discrete logarithms [4].

## Best quantum

Gidney and Ekerå estimate roughly 6,200 logical qubits and 2.6 billion Toffoli gates for RSA-2048 in an abstract circuit, then about 20 million physical qubits and eight hours under their specified surface-code hardware model [2]. Gidney's 2025 revision estimates fewer than one million physical qubits and under one week under comparable assumptions: 0.1% physical gate error, a 1 μs code cycle and 10 μs control reaction time [1]. Neither estimate is an unconditional prediction of when hardware will exist. Regev's algorithm uses Õ(n^{3/2}) gates per run and roughly √n runs; Pilatte later proved the number-theoretic correctness condition, without establishing a classical lower bound or a better practical circuit [3]. Roetteler et al. separately estimate elliptic-curve discrete-logarithm circuits [4].

## Algorithmic result and commercial demand

Quantum polynomial time is proven; classical superpolynomial hardness is a long-standing cryptographic assumption, and engineering studies give concrete circuit estimates. These are unusually strong **algorithmic** facts. The site's third dimension asks a different question: who will pay for the quantum computation? NIST's documents answer a defensive procurement question, not an offensive one [6]. No direct buyer evidence is cited here.

The migration to post-quantum cryptography is a real economic response, but migration can proceed without a quantum computer. The market for an actual quantum factoring service is unknown. Factoring remains central to this catalogue because it is the clearest benchmark for a useful quantum algorithm with a strong classical hardness assumption, even though its customer story differs from chemistry or optimisation.

## Verdict

Surviving under this catalogue's three-dimension commercial rubric: quantum easiness is proven and classical hardness has strong cryptographic evidence, while **direct willingness to pay for an attack is unverified**. This label does not downgrade Shor's theorem. The page would move to `promising` if a public buyer requirement for the computation itself were documented; NIST's defensive transition plan cannot supply that evidence [6].
