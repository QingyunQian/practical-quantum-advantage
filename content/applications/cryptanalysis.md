---
type: application
id: cryptanalysis
title: Cryptanalysis of RSA and elliptic-curve cryptography
title_zh: RSA 与椭圆曲线密码的破解
summary: The one application with a provable super-polynomial speedup, a proven algorithm and a buyer. Gidney's 2025 estimate puts RSA-2048 within reach of fewer than one million physical qubits running under a week. The buyer is a government or security agency, and the economic activity it drives is the migration away from the broken schemes, so this page is tagged out of scope for commercial quantum advantage.
summary_zh: 唯一同时具备可证超多项式加速、已证明的算法和明确买家的应用。Gidney 2025 年的估计是不到一百万物理比特、一周之内破解 RSA-2048。买家是政府和安全机构，它带动的经济活动是从被攻破的方案迁移出去，因此本页标注为商业量子优势范围之外。
status: seed
last_verified: 2026-09-26
tags: [out-of-scope-commercial]
verdict: promising
dimensions:
  classical_hardness: {level: crypto, note: "factoring and discrete logarithm are the assumptions RSA and ECC rest on; best classical is sub-exponential (number field sieve) and has not moved for RSA-2048"}
  quantum_easiness: {level: proven, note: "Shor's algorithm; Gidney–Ekerå 2019 gives 3n + 0.002 n lg n logical qubits and 0.3 n^3 Toffolis for n-bit RSA; Regev 2023 improves the asymptotics"}
  willingness_to_pay: {level: first-hand, note: "NIST IR 8547 sets a timeline to deprecate RSA and ECC at 112-bit security by 2030 and disallow them by 2035; the buyer of the attack itself is a government"}
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
  - {url: "https://csrc.nist.gov/pubs/ir/8547/ipd", title: "Transition to Post-Quantum Cryptography Standards (NIST IR 8547, initial public draft)", authors: "NIST", year: 2024, note: "deprecation timeline for RSA and ECC"}
---

## Who needs it

Governments and their signals-intelligence and security agencies, for offence; everyone who operates a public-key infrastructure, for defence. The offensive buyer does not publish targets, but the defensive side does: NIST's transition plan deprecates RSA and elliptic-curve schemes at 112-bit security by 2030 and disallows them by 2035 [6], a written statement that the threat is being paid for. Commercial value flows to the migration (post-quantum standards, hardware refresh, certificate infrastructure), not to the quantum computer.

## Bottleneck

Factoring an n-bit RSA modulus classically takes sub-exponential time (the number field sieve); RSA-2048 has not been factored and is not expected to be by classical means. Elliptic-curve discrete logarithms at 256 bits are harder still classically. The task is well defined, the input is a few kilobits and the output a few kilobits, so none of the I/O objections that sink other applications apply.

## Computational problems

- [Integer factoring and the hidden subgroup problem](../problems/integer-factoring-hidden-subgroup.html): Shor's algorithm [5] and its descendants; the same period-finding machinery covers finite-field and elliptic-curve discrete logarithms [4].

## Best quantum

Gidney and Ekerå's 2019 construction is the reference point: in the abstract circuit model it uses 3n + 0.002 n lg n logical qubits, 0.3 n³ + 0.0005 n³ lg n Toffolis and 500 n² + n² lg n measurement depth for an n-bit modulus, which for n = 2048 is about 6,200 logical qubits and 2.6e9 Toffolis; with surface-code overheads on a planar grid at 0.1% gate error, 1 μs cycle and 10 μs reaction time, they estimate 20 million physical qubits and 8 hours [2]. Gidney's 2025 update keeps the same physical assumptions and brings the count under one million physical qubits at a run time under one week, using approximate residue arithmetic, yoked surface codes for idle logical qubits and magic-state cultivation in place of most distillation; the longer run time comes from more Toffolis and fewer factories [1]. Regev's 2023 algorithm improves the asymptotic gate count from Õ(n²) to Õ(n^{3/2}) per run at the price of more runs and more space, and has not yet displaced the Gidney–Ekerå line in concrete estimates [3]. For ECC, Roetteler et al. give the corresponding logical estimates for P-256 and other curves [4].

## Why it is promising and why it is out of scope

On the three dimensions this is the only entry in the catalogue that clears every bar. Classical hardness is the cryptographic assumption itself. Quantum easiness is proven, with concrete compiled circuits rather than asymptotic claims. The buyer has written its timeline down. That is what "promising" means here, and the catalogue records it so that the contrast with every commercial candidate is explicit.

It is out of scope for commercial advantage for two reasons. The buyer of the attack is a state, and the price it will pay is not a market signal. And the value it creates for everyone else is negative: the rational commercial response is to stop relying on the broken primitive, which the standards bodies have already scheduled. Nobody will sell factoring as a service. The number-theoretic machinery has no other documented commercial use; class-group and unit-group computations (Biasse–Song and predecessors) have mathematical and cryptanalytic interest but no industrial customer.

## Verdict

Promising, and tagged out of scope. The remaining uncertainty is engineering (whether a million-qubit machine at 0.1% error and 1 μs cycle exists by the 2030–35 deprecation window), not algorithmic or economic. For this catalogue the entry serves as the calibration point: it shows what a candidate looks like when all three dimensions are satisfied, and every other page is measured against it.
