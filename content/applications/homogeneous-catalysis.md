---
type: application
id: homogeneous-catalysis
title: Homogeneous transition-metal catalyst design
title_zh: 均相过渡金属催化剂设计
summary: The original "killer application" narrative (Reiher et al. 2017) now has a price tag. Zapata and industrial partners valued the most valuable catalyst instance at about $200k, priced the DMRG calculation of the same instance at roughly 400,000 CPU-hours, and estimated the quantum version at 8,478 logical qubits and 1.4e12 Toffoli gates. Open-shell Fe/Co/Ni/Mo centres remain hard for DFT, but the mainstream Pd/Rh/Ru chemistry is single-reference.
summary_zh: 这是最早的“杀手级应用”叙事（Reiher 等 2017），现在有了价格标签。Zapata 与产业伙伴给最有价值的催化剂实例标价约 20 万美元，同一实例的 DMRG 计算约 40 万 CPU 核时，而量子版本需要 8,478 个逻辑比特和 1.4e12 个 Toffoli 门。开壳层的 Fe/Co/Ni/Mo 中心对 DFT 仍然困难，但工业主流的 Pd/Rh/Ru 化学是单参考的。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: empirical, note: "DFT spin-state and barrier errors of 5–30 kcal/mol on open-shell 3d and multinuclear centres; DLPNO-CCSD(T) to 1–2 kcal/mol for single-reference Pd/Rh/Ru; DMRG-NEVPT2 routine to 50–100 orbitals; GPU DMRG at CAS(89,102) on Fe–S clusters"}
  quantum_easiness: {level: conditional, note: "phase estimation with double-factorised or THC block encodings; needs initial-state overlap, which is unverified for multinuclear open-shell clusters; resource estimates at 8,478 logical qubits and 1.4e12 Toffoli for the most valuable instance"}
  willingness_to_pay: {level: first-hand, note: "Bellonzi et al. elicited utility values from industrial partners: the top instance is valued at about $200k, which is small against the quantum resources and comparable to the classical DMRG cost"}
resources: {logical_qubits: "8,478 (Mo nitrogen-fixation instance)", gates: "1.4e12 Toffoli", note: "Bellonzi et al. 2024; single-centre Fe active spaces of 30–70 orbitals need 60–140 system qubits, plus ancillas and distillation"}
related:
  applications: [oled-emitters, p450-drug-metabolism, protein-ligand-binding]
  problems: [ground-state-energy, excited-states]
  methods: [phase-estimation, embedding-divide-and-conquer, sqd]
  questions: [dmrg-vs-qpe-cost-accuracy-oled, first-hand-payment-evidence]
references:
  - {arxiv: "2406.06335", title: "Feasibility of accelerating homogeneous catalyst discovery with fault-tolerant quantum computers", authors: "N. Bellonzi et al. (Zapata AI, University of Toronto)", year: 2024, note: "$200k utility, 400,000 CPU-h DMRG, 8,478 logical qubits, 1.4e12 Toffoli for the top instance"}
  - {arxiv: "1605.03590", title: "Elucidating Reaction Mechanisms on Quantum Computers", authors: "M. Reiher, N. Wiebe, K. M. Svore, D. Wecker, M. Troyer", year: 2016, note: "origin of the nitrogen-fixation catalysis narrative"}
  - {arxiv: "2208.02199", title: "Is there evidence for exponential quantum advantage in quantum chemistry?", authors: "S. Lee, J. Lee, H. Zhai, Y. Tong, et al.", year: 2022}
  - {arxiv: "2603.28648", title: "Hunting for quantum advantage in electronic structure calculations is a highly non-trivial task", authors: "Ö. Legeza et al.", year: 2026, note: "GPU DMRG at CAS(89,102) on an Fe–S cluster; argues advantage claims must be benchmarked against DMRG"}
  - {arxiv: "2603.08883", title: "Parallel iQCC Enables 200 Qubit Scale Quantum Chemistry on Accelerated Computing Platforms Surpassing Classical Benchmarks in Ruthenium Catalysts", authors: "S. M. Hosseini Jenab, T. Henderson, S. N. Genin (OTI Lumionics)", year: 2026, note: "classically simulated iQCC at 100–124 qubits on Ru catalysts; authors place the advantage threshold beyond 200 qubits"}
  - {arxiv: "2601.04621", title: "Classical computational simulation of the FeMo-cofactor model to chemical accuracy and its implications", authors: "H. Zhai et al., G. K.-L. Chan", year: 2026}
---

## Who needs it

Fine-chemical and pharmaceutical process groups (BASF, Dow, Merck, Novartis), and the catalyst vendors that supply them. The decisions are which ligand and metal to try next for a cross-coupling, hydrogenation, olefin metathesis or C–H activation, and which of several competing mechanisms controls selectivity. Each experimental iteration costs days to weeks; a computed barrier or spin-state ordering that is wrong by 5 kcal/mol corresponds to a room-temperature rate error of about four orders of magnitude, which is enough to send the experiment in the wrong direction.

## Bottleneck

Accuracy can be a bottleneck in open-shell transition-metal and multinuclear catalysts. Reiher et al. use nitrogenase-type iron and molybdenum chemistry to motivate fault-tolerant quantum simulation [2]. Establishing an advantage requires identifying a specific reaction and comparing against converged classical multireference calculations on the same Hamiltonian [3, 4]. A difficult catalyst family alone does not establish that its industrial decision needs a quantum calculation.

The economic picture was quantified by Bellonzi et al. with industrial partners [1]. They elicited a utility value for each of a set of catalyst instances; the most valuable one, a Mo nitrogen-fixation catalyst with a CAS(101e,75o) active space, was valued at about $200,000. The DMRG calculation of the same instance was priced at about 400,000 CPU-hours, roughly $16,000 at $0.04 per core-hour (the paper's $2,800 figure is an average over all instances). The fault-tolerant estimate for the same instance is 8,478 logical qubits and 1.4×10^12 Toffoli gates. The value of the answer is therefore an order of magnitude above the classical cost and far below any plausible cost of the quantum calculation, which is why this study is cited as evidence against, not for, near-term catalysis applications.

## Computational problems

- [Ground-state energy](../problems/ground-state-energy.html) of intermediates and transition states in 30–150 orbital active spaces, plus dynamic correlation outside the space.
- [Excited states](../problems/excited-states.html): spin-state orderings, which decide the reactive surface for 3d metals.
- Geometry optimisation and free-energy corrections, which remain classical.

## Best classical today

DLPNO-CCSD(T) for single-reference systems; DMRG-NEVPT2 to 50–100 orbitals; phaseless AFQMC at about 2 kcal/mol on 3d systems. GPU DMRG now handles CAS(89,102) on an Fe₅S₁₂ cluster, and Legeza et al. argue that any claimed quantum advantage must be benchmarked against such DMRG runs [4]. The FeMoco model that anchored the 2017 narrative was solved to chemical accuracy classically in 2026 [6]. Lee et al. argue that the single-determinant overlap decays with the number of metal centres (about 0.9 for Fe₂S₂, 0.1–0.2 for Fe₄S₄) but that classical cost at fixed energy-density error grows only polynomially in the same regime [3]. On the quantum-inspired side, OTI Lumionics report classically simulated iQCC at 100–124 qubits on Ru catalysts and place the classical ceiling beyond 200 qubits [5].

## Verdict

Surviving, not promising. The buyer exists and has stated a value, which is rare, but the stated value ($200k) is small and the classical route to the same answer costs about $16k, so willingness to pay for the quantum route is weak in practice. Hardness is empirical and shrinking: single-reference catalysts are solved, and the multinuclear open-shell ones are being reached by DMRG at 100 orbitals. The quantum precondition (initial-state overlap for multinuclear clusters) is unverified. What would change the verdict is an instance family where DMRG bond dimension demonstrably diverges past 100 orbitals after orbital optimisation, where the spin-state ordering matters to a named process, and where the process owner values the answer at more than the cost of the fault-tolerant run. The Zapata numbers set the bar: any proposal must explain why its instance is worth more than $200k and costs more than 400,000 CPU-hours classically.
