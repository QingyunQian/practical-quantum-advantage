---
type: question
id: first-hand-payment-evidence
title: Which buyers have written down an accuracy or speed target? Collect the first-hand evidence.
title_zh: 哪些买方写下了精度或速度目标？收集一手证据
summary: A verdict of promising requires willingness_to_pay at the first-hand level, meaning a company or agency stated an accuracy or speed target in writing or co-authored the study. Across the fourteen application pages, only OLED emitters (OTI Lumionics and Samsung SAIT, 0.05 eV on T1/S1) currently meet that bar; everything else is second-hand argument from the algorithms literature. The task is to search buyer-side documents in each industry and build a table of who said what, at what number, in which document.
summary_zh: “有戏”的判定要求 willingness_to_pay 达到一手证据级别，即企业或机构在书面材料中给出精度或速度目标，或署名参与研究。在十四个应用页中，目前只有 OLED 发光体（OTI Lumionics 与三星 SAIT，T1/S1 精度 0.05 eV）达到这一标准；其余都是算法文献里的二手论证。任务是在各行业的买方文档中检索，建成一张“谁、说了什么数字、在哪份文件里”的表。
status: seed
last_verified: 2026-09-26
question:
  what_would_settle_it: "A table with one row per application page: buyer (company or agency), the quantitative target (accuracy in eV or kcal/mol, or speed in hours per instance, or cost per instance), the document (co-authored paper, RFP, roadmap, regulatory filing, patent, earnings call transcript) with a resolvable link, and whether the document says what they do today and why it is insufficient. Rows are accepted only where the buyer speaks; a survey by a quantum vendor or a national-lab roadmap counts as second-hand. The deliverable is merged into the willingness_to_pay note of each application page and moves the level from second-hand to first-hand where a row exists."
  difficulty: month
  resolved: false
related:
  applications: [oled-emitters, battery-electrolyte-design, homogeneous-catalysis, p450-drug-metabolism, protein-ligand-binding, rare-earth-permanent-magnets, battery-cathode-spectroscopy, nuclear-fuel-actinide-spectra, weather-forecasting, derivative-pricing, radar-cross-section, turbulence-cfd, automotive-pricing-integer-programming, cryptanalysis]
  questions: [dmrg-vs-qpe-cost-accuracy-oled]
references:
  - {arxiv: "2512.13657", title: "Towards Quantum Advantage in Chemistry", authors: "S. N. Genin, O. Kwon, S. M. Hosseini Jenab et al. (OTI Lumionics, Samsung SAIT)", year: 2025, note: "the one first-hand chemistry target found so far: 0.05 eV"}
  - {arxiv: "2406.06335", title: "Feasibility of accelerating homogeneous catalyst discovery with fault-tolerant quantum computers", authors: "N. Bellonzi, A. Kunitsa et al. (Zapata, with industrial co-authors)", year: 2024, note: "prices the highest-value instance at $200k; DMRG on the same instance about 400,000 CPU-hours"}
  - {arxiv: "2509.08328", title: "Towards solving industrial integer linear programs with Decoded Quantum Interferometry", authors: "J. Sabater et al.", year: 2026, note: "automotive option-package pricing; QST 11, 025054 (2026); no claim of beating Gurobi"}
  - {arxiv: "2012.03819", title: "A Threshold for Quantum Advantage in Derivative Pricing", authors: "S. Chakrabarti et al. (Goldman Sachs, IBM)", year: 2021, note: "Quantum 5, 463 (2021); ~8k logical qubits, T-depth 5.4e7, needs 10 MHz logical clock"}
  - {arxiv: "2510.07273", title: "End-to-end quantum algorithms for tensor problems", authors: "M. Fontana et al. (JPMorgan)", year: 2025, note: "900 logical qubits, 1e15 gates, depth 1e12"}
  - {arxiv: "1505.06552", title: "Concrete resource analysis of the quantum linear system algorithm used to compute the electromagnetic scattering cross section of a 2D target", authors: "A. Scherer et al.", year: 2017, note: "QIP 16, 60 (2017); circuit depth ~1e29 with the geometry oracle"}
  - {arxiv: "2605.01138", title: "Crossing the 12,000-atom barrier with heterogeneous quantum-classical supercomputing: quantum chemistry of protein-ligand complexes", authors: "L. Merz, B. Shajan, D. Kaliakin et al. (Cleveland Clinic, RIKEN, IBM)", year: 2026, note: "co-authored by a clinical institution but states no accuracy target"}
---

## Why it matters

The catalogue's rule (AGENTS.md) is that `promising` needs classical hardness at least at the lower-bound level, quantum easiness at least conditional, and documented demand from a buyer. The OLED study by OTI Lumionics and Samsung SAIT provides a concrete accuracy benchmark [1]. The Zapata catalyst study offers a different kind of evidence: it estimates a value of $200,000 for its highest-value instance and compares quantum costs with a classical DMRG calculation of about 400,000 CPU-hours [2]. These are useful starting points for collecting public, application-specific evidence; they do not establish that other sectors have no demand.

Some finance and engineering pages have bank or contractor co-authors with resource estimates [4, 5, 6] but no stated speed or accuracy target; the automotive ILP paper is the only public industrial optimisation case and does not claim to beat Gurobi [3]. The 12,000-atom protein paper is co-authored by a clinic and states no target [7]. These are second-hand until a document says "we need X".

## What is known

| application | first-hand document | number | status |
|---|---|---|---|
| oled-emitters | Genin et al. 2025 (OTI Lumionics, Samsung SAIT) [1] | T1/S1 within 0.05 eV | first-hand |
| homogeneous-catalysis | Bellonzi et al. 2024 (Zapata with industry) [2] | $200k value; DMRG 4e5 CPU-h | first-hand, negative |
| derivative-pricing | Chakrabarti et al. 2021 (Goldman Sachs) [4] | none stated; resource estimate only | second-hand |
| automotive-pricing-integer-programming | Sabater et al. 2026 [3] | none stated | second-hand |
| protein-ligand-binding | Merz et al. 2026 (Cleveland Clinic) [7] | none stated | second-hand |
| radar-cross-section | Scherer et al. 2017 [6] | none; RAND 2026 says not practical short-term | second-hand |
| all others | none found | | unknown |

## What would settle it

See the front matter. Where to look, by industry: pharma (FDA/EMA modelling guidance, company model-validation SOPs, published "accuracy needed for go/no-go" statements in J. Med. Chem. perspectives), batteries (Battery500, Faraday Institution and CATL/BYD/LG roadmaps with property tolerances), magnets (ESICMM and Toyota-linked reports, which state the anisotropy accuracy needed for Ce substitution), nuclear fuel (DOE NEAMS validation targets), weather (ECMWF and NOAA procurement documents state time-to-solution per forecast cycle), finance (bank model-risk documents rarely public; look for regulator-mandated pricing tolerances), defence (RCS: contractor RFPs specify dB accuracy), CFD (aerospace certification tolerances). Each row should quote the sentence. A month of desk research; the OLED row shows the form.

## Who could take it

Anyone with library access and patience; no computation. This is also the item most useful to the repository's maintainers, since every `promising` verdict depends on it.
