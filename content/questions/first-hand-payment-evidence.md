---
type: question
id: first-hand-payment-evidence
title: Which buyers have written down an accuracy or speed target? Collect the first-hand evidence.
title_zh: 哪些买方写下了精度或速度目标？收集一手证据
summary: A company can co-author a benchmark without stating the accuracy or price at which it would buy a computation. The OLED paper reports an achieved 0.0501 eV mean absolute error, not a written 0.05 eV acceptance target. Audit each application for the buyer's own quantitative requirement, current alternative, decision affected and source; distinguish these from co-authorship or an algorithm paper's estimate.
summary_zh: 企业可以参与基准研究，却未必写明愿意以什么精度或价格购买计算。OLED 论文报告的是已实现的 0.0501 eV 平均误差，不是书面的 0.05 eV 验收目标。本问题逐一核对应用页的买方定量要求、现有替代方案、受影响的决策及原始来源，并与共同署名或算法论文的估计区分。
status: seed
last_verified: 2026-09-27
question:
  what_would_settle_it: "A table with one row per application page: buyer, whether their own document states an accuracy/speed/price threshold, the current alternative, the decision affected, and the exact public source. Separate documented interest or co-authorship from a quantified purchase requirement; separate achieved method error from a buyer target. Correct the willingness_to_pay note and level on each page when its source has been checked."
  difficulty: month
  resolved: false
related:
  applications: [oled-emitters, battery-electrolyte-design, homogeneous-catalysis, p450-drug-metabolism, protein-ligand-binding, rare-earth-permanent-magnets, battery-cathode-spectroscopy, nuclear-fuel-actinide-spectra, weather-forecasting, derivative-pricing, radar-cross-section, turbulence-cfd, automotive-pricing-integer-programming, cryptanalysis]
  questions: [dmrg-vs-qpe-cost-accuracy-oled]
references:
  - {arxiv: "2512.13657", title: "Towards Quantum Advantage in Chemistry", authors: "S. N. Genin, O. Kwon et al. (OTI Lumionics, Samsung SAIT)", year: 2026, note: "v2; achieved MAE 0.0501 eV, no explicit buyer acceptance threshold"}
  - {arxiv: "2406.06335", title: "Feasibility of accelerating homogeneous catalyst discovery with fault-tolerant quantum computers", authors: "N. Bellonzi et al. (Zapata AI, University of Toronto)", year: 2024, note: "$200k is an author-derived research-utility estimate; 400,000 DMRG CPU-hours are extrapolated"}
  - {arxiv: "2509.08328", title: "Towards solving industrial integer linear programs with Decoded Quantum Interferometry", authors: "J. Sabater et al.", year: 2026, note: "automotive option-package pricing; QST 11, 025054 (2026); no claim of beating Gurobi"}
  - {arxiv: "2012.03819", title: "A Threshold for Quantum Advantage in Derivative Pricing", authors: "S. Chakrabarti et al. (Goldman Sachs, IBM)", year: 2021, note: "Quantum 5, 463 (2021); ~8k logical qubits, T-depth 5.4e7, needs 10 MHz logical clock"}
  - {arxiv: "2510.07273", title: "End-to-end quantum algorithms for tensor problems", authors: "M. Fontana et al. (JPMorgan)", year: 2025, note: "900 logical qubits, 1e15 gates, depth 1e12"}
  - {arxiv: "1505.06552", title: "Concrete resource analysis of the quantum linear system algorithm used to compute the electromagnetic scattering cross section of a 2D target", authors: "A. Scherer et al.", year: 2017, note: "QIP 16, 60 (2017); circuit depth ~1e29 with the geometry oracle"}
  - {arxiv: "2605.01138", title: "Crossing the 12,000-atom barrier with heterogeneous quantum-classical supercomputing: quantum chemistry of protein-ligand complexes", authors: "L. Merz, B. Shajan, D. Kaliakin et al. (Cleveland Clinic, RIKEN, IBM)", year: 2026, note: "co-authored by a clinical institution but states no accuracy target"}
---

## Why it matters

For a direct application, the catalogue's `promising` verdict requires a documented buyer requirement alongside a credible same-task classical bottleneck and an end-to-end quantum route. Foundational computational problems have a separate algorithmic route to that verdict, so this question concerns **application pages**. The OLED study by OTI Lumionics and Samsung SAIT provides a concrete *achieved* accuracy benchmark, 0.0501 eV MAE across 14 emitters [1]. It does not say the companies would reject predictions above 0.05 eV or buy calculations below it. The Zapata catalyst study gives an **author-derived** $200,000 utility estimate, based on a $25 million public grant and expected paper counts, and a roughly 400,000-core-hour **extrapolation** for DMRG [2]. The paper does not quote a catalyst buyer or report that full DMRG run. These studies motivate further inquiry; neither supplies a buyer-defined purchase requirement.

Some finance and engineering pages have bank or contractor co-authors with resource estimates [4, 5, 6]; co-authorship must be distinguished from a buyer-defined performance threshold. The automotive ILP paper does not claim to beat Gurobi [3]. The 12,000-atom protein paper is co-authored by a clinic and states no quantitative buyer target [7].

## What is known

| application | first-hand document | number | status |
|---|---|---|---|
| oled-emitters | Genin et al. 2026 (OTI Lumionics, Samsung SAIT) [1] | achieved T1-to-S0 MAE 0.0501 eV; buyer threshold unstated | first-hand interest, target unknown |
| homogeneous-catalysis | Bellonzi et al. 2024 (Zapata and academic authors) [2] | $200k inferred research utility; DMRG ~4e5 CPU-h extrapolated | second-hand; buyer target unknown |
| derivative-pricing | Chakrabarti et al. 2021 (Goldman Sachs) [4] | about one second to beat the studied classical pricing workflow; no procurement price | first-hand technical crossover, purchase unknown |
| automotive-pricing-integer-programming | Sabater et al. 2026 (BMW coauthors) [3] | no buyer-defined solve-time or objective threshold | first-hand interest, target unknown |
| protein-ligand-binding | Merz et al. 2026 (Cleveland Clinic) [7] | none stated | second-hand |
| radar-cross-section | Scherer et al. 2017 [6] | none; RAND 2026 says not practical short-term | second-hand |
| all others | none found | | unknown |

## What would settle it

See the front matter. Search primary buyer-side documents such as public RFPs, published validation requirements, industrial co-authored studies and procurement records. Record the exact claim and link for each row. A method's achieved error, an industrial co-author and a buyer's acceptance threshold are three different facts; the OLED row demonstrates why the distinction matters.

## Who could take it

Anyone with library access and patience; no computation. The result will help assess direct application pages. A foundational problem such as factoring can have a strong algorithmic verdict while this commercial question remains open.
