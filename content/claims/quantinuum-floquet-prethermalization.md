---
type: claim
id: quantinuum-floquet-prethermalization
title: Quantinuum 56-qubit digital Ising dynamics and Floquet prethermalization (H2, 2025)
title_zh: Quantinuum H2 上的 56 比特数字化 Ising 动力学与 Floquet 预热化（2025）
summary: Haghshenas et al. ran digitized transverse-field Ising dynamics on all 56 qubits of Quantinuum's H2 with circuits of up to about 2,240 two-qubit gates, observed Floquet prethermalization and emergent diffusive hydrodynamics, and stated that MPS at bond dimension 4,000 and other classical methods do not reach these time scales. As of 2026-09-26 no full classical reproduction exists; Mandrà et al. report an MPS heuristic in excellent agreement on the 7×8 TFIM, and a 2026 follow-up on 74 qubits pushes the same physics further.
summary_zh: Haghshenas 等在 Quantinuum H2 的全部 56 个比特上运行数字化横场 Ising 动力学，电路最多约 2,240 个两比特门，观测到 Floquet 预热化与涌现的扩散型流体力学，并称键维 4,000 的 MPS 等经典方法达不到这些时间尺度。截至 2026-09-26 没有完整的经典复现；Mandrà 等报告了在 7×8 TFIM 上与实验高度一致的 MPS 启发式方法，2026 年一项 74 比特的后续工作把同类物理推得更远。
status: reviewed
last_verified: 2026-09-26
claim:
  claimant: Quantinuum (Haghshenas et al.)
  date: 2025-03
  statement: "Digital quantum magnetism at the frontier of classical simulations: digitized Ising dynamics on 56 trapped-ion qubits with two-qubit gate fidelity 99.94% suppresses Trotter error enough to observe Floquet prethermalization and thermalization on time scales that severely challenge current classical methods."
  hardware: Quantinuum System Model H2 (trapped ions)
  qubits: 56
  refuted: false
  refuted_by: "No full classical reproduction as of 2026-09-26; partial agreement from an MPS heuristic (Mandrà et al.) on the 7×8 transverse-field Ising instance"
related:
  problems: [quench-dynamics]
  claims: [ibm-kicked-ising-utility-2023, dwave-beyond-classical-2025]
references:
  - {arxiv: "2503.20870", title: "Digital quantum magnetism on a trapped-ion quantum computer", authors: "R. Haghshenas, E. Chertkov, M. Mills et al.", year: 2026, note: "Nature 653, 56 (2026); preprint title 'Digital quantum magnetism at the frontier of classical simulations'"}
  - {arxiv: "2511.23438", title: "A Heuristic for Matrix Product State Simulation of Out-of-Equilibrium Dynamics of Two-Dimensional Quantum Spin Systems", authors: "S. Mandrà, B. Ware, N. Astrakhantsev, S. Isakov, B. Villalonga, T. Westerhout, K. Kechedzhi", year: 2025}
  - {arxiv: "2607.24937", title: "Resolving Structure in Prethermal Floquet Dynamics with Precision Quantum Computation", authors: "(IBM Heron r3 with QESEM; Quantinuum H2 and Helios; up to 74 qubits)", year: 2026}
  - {arxiv: "2306.14887", title: "Efficient tensor network simulation of IBM's Eagle kicked Ising experiment", authors: "J. Tindall, M. Fishman, E. M. Stoudenmire, D. Sels", year: 2024}
  - {arxiv: "2511.19340", title: "Simulating dynamics of the two-dimensional transverse-field Ising model: a comparative study of large-scale classical numerics", authors: "J. Vovrosh et al.", year: 2026}
---

## Claim

Identification: the paper behind this entry is Haghshenas et al., arXiv:2503.20870 (March 2025), published as Nature 653, 56 (2026). It is the Quantinuum experiment that the phrase "Floquet prethermalization" in the seed list refers to; the July 2026 paper on prethermal Floquet dynamics with QESEM error mitigation [3] uses H2 and Helios as well but is centred on an IBM Heron r3 run and is treated here as a follow-up, not as the claim.

Haghshenas et al. ran Trotterized transverse-field Ising dynamics on a 7×8 grid embedded in the 56 all-to-all qubits of H2, with circuits of up to about 2,240 two-qubit gates at native partial-entangler fidelity 99.94(1)%. Because the digitisation error is small, the Floquet system behaves for a long time as if energy were conserved (prethermalization), and relaxation of an inhomogeneous initial state shows diffusive hydrodynamics from which a diffusion constant is extracted. The authors benchmarked against MPS with bond dimension up to 4,000, PEPS with belief-propagation compression and related methods, and stated that the late-time results are not accessible to these techniques at comparable resources [1]. The claim is phrased as "at the frontier of classical simulations", weaker than a beyond-classical statement.

## Refutation

No full classical reproduction as of 2026-09-26. Searched: arXiv quant-ph and cond-mat listings for "digital quantum magnetism", "Floquet prethermalization" and "H2 56 qubits" through September 2026; the citing literature of [1]; this repository's classical counter-results survey. What exists:

- Mandrà et al. (a Google-affiliated team) proposed an MPS heuristic for out-of-equilibrium 2D spin dynamics and report excellent agreement with the 7×8 TFIM results of [1] [2]. The abstract does not state that every Trotter step and observable of the experiment is covered, so this is recorded as partial, not as a refutation. If the full time window is reproduced at the experiment's accuracy, this flag should change.
- The reasons to expect eventual classical coverage are the same as for `ibm-kicked-ising-utility-2023`: 20 Trotter steps on a 7×8 open grid is a modest depth, and belief-propagation methods handle such geometries well [4]. The reason to expect it to stand is the independent benchmark of Vovrosh et al., which finds that for the clean 2D TFIM on 10×10 to 14×14 grids all large-scale classical methods deviate for tJ ≳ 2 [5]; whether the H2 circuits sit past that boundary at their measured accuracy is the open question.
- The 2026 follow-up [3] reaches 74 qubits with percent-level precision on magnetisation and reports that state-of-the-art classical methods including Fugaku runs did not reproduce the late-time results; it is subject to the same caveat that "did not reproduce" is a statement about the methods tried.

## Lesson for the catalogue

This is the dynamics claim with the most careful classical benchmarking on the claimant's side, and it still lands in the region where neither side can verify: the quantum result is error-mitigated, the classical result is truncated. The `quench-dynamics` page states what would resolve it, namely an entropy-per-bond measurement at the experiment's parameters.
