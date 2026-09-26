---
type: question
id: dmrg-vs-qpe-cost-accuracy-oled
title: Cost–accuracy curve of DMRG, SHCI and early fault-tolerant phase estimation on one OLED emitter
title_zh: 在一个 OLED 发光体上比较 DMRG、SHCI 与早期容错相位估计的成本-精度曲线
summary: OLED emitters are the one chemistry application with a written buyer accuracy target (T1/S1 within 0.05 eV). Nobody has measured, on a single named Ir/Pt phosphor or MR-TADF emitter at 70 to 100 active orbitals, how DMRG bond dimension and SHCI determinant count grow with target accuracy, against the samples and circuit depth an early fault-tolerant phase-estimation run would need at the same accuracy. The crossover point, if any, is the number that decides whether the application page is surviving or uneconomic.
summary_zh: OLED 发光体是唯一有买方书面精度目标（T1/S1 在 0.05 eV 内）的化学应用。还没有人在一个具名的 Ir/Pt 磷光体或 MR-TADF 发光体上，以 70 到 100 个活性轨道，测量 DMRG 键维和 SHCI 行列式数随目标精度的增长，并与早期容错相位估计在同等精度下所需的采样数和电路深度对照。交叉点（若存在）就是决定该应用页是“幸存”还是“不划算”的数字。
status: seed
last_verified: 2026-09-26
question:
  what_would_settle_it: "For one emitter (e.g. fac-Ir(ppy)3 or a DABNA-type MR-TADF core) with CAS(70–100 electrons, 70–100 orbitals) after orbital optimisation: DMRG energy versus bond dimension up to D = 8,000–18,000 and SHCI energy versus determinant count, both extrapolated, for the T1 and S1 states; and for the same active space the Trotter or qubitisation depth, the number of samples at the Lin–Izmaylov overlap bound, and the logical error rate that Lin–Tong / QETU phase estimation needs to reach 0.05 eV. Plot cost against accuracy on one axis. A crossover below 0.05 eV within a 10^9–10^10 T-gate budget keeps the application alive; classical convergence to 0.02 eV at under 10^5 core-hours closes it."
  difficulty: month
  resolved: false
related:
  applications: [oled-emitters]
  problems: [ground-state-energy, excited-states]
  methods: [phase-estimation]
  questions: [first-hand-payment-evidence]
references:
  - {arxiv: "2512.13657", title: "Towards Quantum Advantage in Chemistry", authors: "S. N. Genin, O. Kwon, S. M. Hosseini Jenab et al. (OTI Lumionics, Samsung SAIT)", year: 2025, note: "iQCC+PT MAE 0.05 eV versus TD-B3LYP 0.12 eV; classically tractable to ~200 logical qubits"}
  - {arxiv: "2603.08883", title: "Parallel iQCC Enables 200 Qubit Scale Quantum Chemistry on Accelerated Computing Platforms Surpassing Classical Benchmarks in Ruthenium Catalysts", authors: "S. M. Hosseini Jenab, B. Henderson, S. N. Genin", year: 2026}
  - {arxiv: "2601.04621", title: "Classical computational simulation of the FeMo-cofactor model to chemical accuracy and its implications", authors: "H. Zhai, C. Li, X. Zhang et al.", year: 2026, note: "DMRG D = 18,000 plus CC extrapolation, ±0.3 kcal/mol, 2.8e6 core-hours"}
  - {arxiv: "2603.28648", title: "Hunting for quantum advantage in electronic structure calculations is a highly non-trivial task", authors: "Ö. Legeza, A. Menczer, M. A. Werner et al.", year: 2026, note: "GPU-DMRG benchmarks up to CAS(89,102)"}
  - {arxiv: "2208.02199", title: "Is there evidence for exponential quantum advantage in quantum chemistry?", authors: "S. Lee, J. Lee, H. Zhai et al.", year: 2023, note: "Nat. Commun. 14, 1952 (2023)"}
  - {arxiv: "2603.19081", title: "Utility-scale quantum computational chemistry", authors: "D. Castaldo, M. Reiher", year: 2026}
---

## Why it matters

Among nine industrial chemistry domains scanned for this repository, OLED emitters are the only one where a company states an accuracy target in a paper it co-authored: OTI Lumionics and Samsung SAIT want T1 and S1 energies within 0.05 eV, TD-DFT sits at 0.12 to 0.26 eV, and their own iQCC with perturbative correction reaches a mean absolute error of 0.05 eV on classical GPUs [1]. The same group finds the systems classically tractable up to about 200 logical qubits' worth of orbitals [1, 2]. On the other side, DMRG with bond dimension 18,000 plus coupled-cluster extrapolation has reached ±0.3 kcal/mol on the FeMo cofactor at 2.8 million core-hours [3], and Legeza et al. insist DMRG benchmarks be the classical reference for any advantage claim [4]. Lee et al. argued that classical heuristics converge polynomially in practice and that generic exponential advantage in chemistry has no evidence [5]. Every one of these is a point on a cost–accuracy plane; none of them is on the same molecule, and none includes the quantum side's cost at the same accuracy.

The application page `oled-emitters` is `surviving` only because this curve has not been drawn. If DMRG converges the T1 gap of a 100-orbital emitter to 0.02 eV at 10^5 core-hours, the application is uneconomic no matter what a phase-estimation resource estimate says.

## What is known

- Classical: iQCC+PT at 0.05 eV MAE on organometallic emitters [1]; parallel iQCC on 100 to 124 qubit Ru catalysts in 1.2 to 45 GPU-hours, exceeding DMRG accuracy at the bond dimensions tried [2]; GPU-DMRG to CAS(89,102) [4]. Spin–orbit coupling, needed for Ir/Pt phosphors, is not yet routine in DMRG excited-state workflows.
- Quantum: no end-to-end estimate exists for a named emitter; the generic numbers for CAS(70–100) are 140 to 200 system qubits and 10^9 to 10^10 T gates for full phase estimation, with the total logical count in the thousands once ancillas are included. Early fault-tolerant variants (Lin–Tong, QETU) trade depth for samples and need an overlap lower bound, which the Lin–Izmaylov moment method can certify.
- Castaldo and Reiher argue that any quantum method must slot into a high-throughput pipeline to matter industrially [6], which for OLED screening means hundreds of candidates, not one.

## What would settle it

See the front matter. Practical route: PySCF integrals for the emitter, orbital optimisation (the FeMoco lesson is that unoptimised orbitals overstate hardness by orders of magnitude), block2 DMRG sweeps with D = 500 to 18,000 and SHCI with increasing ε, both for T1 and S1; then a Trotter-error and sampling-count estimate for QETU at the same active space with the moment-bound overlap. A month of work on a workstation with a GPU for the DMRG part; the cluster time is the only real cost. Deliverable: one figure, cost (core-hours or T gates) versus error in the T1 energy, with the 0.05 eV line drawn.

## Who could take it

A computational chemistry group with block2 or ORCA-DMRG experience, ideally with the OTI Lumionics benchmark set so that the numbers are comparable to [1]. The result is publishable either way and is the deciding input for the `oled-emitters` verdict.
