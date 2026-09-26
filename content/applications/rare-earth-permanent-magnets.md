---
type: application
id: rare-earth-permanent-magnets
title: Rare-earth permanent magnets (Ce-for-Nd substitution)
title_zh: 稀土永磁（以 Ce 替代 Nd）
summary: Ce substitution in Nd2Fe14B is a real materials-design problem with experimental and classical modelling results. A published DFT+Hubbard-I study predicts composition and site-occupancy effects while approximating mixed-valent Ce. A separate DFT+QMC study treats Kondo screening in other Ce-Fe magnets. Neither establishes a classically failed Ce-for-Nd impurity at a buyer-defined accuracy target.
summary_zh: 在 Nd2Fe14B 中以 Ce 替代 Nd 是有实验和经典计算结果的材料设计问题。已发表的 DFT+Hubbard-I 研究预测了成分与占位的影响，但对混合价 Ce 作了近似；另一项 DFT+QMC 研究处理了其他 Ce-Fe 磁体中的近藤屏蔽。现有证据没有给出在买方指定精度下经典方法失败的 Ce 替代杂质实例。
status: seed
last_verified: 2026-09-27
verdict: surviving
dimensions:
  classical_hardness: {level: unknown, note: "A direct Ce-substituted Nd2Fe14B study completed its magnetic-anisotropy model classically but approximated mixed-valent Ce; a separate Ce-Fe study solved a dynamical Ce impurity with DFT+QMC. No measured failure on the target alloy and observable is documented."}
  quantum_easiness: {level: unknown, note: "A chosen seven-orbital f impurity plus a short discrete bath can occupy 56–98 system qubits, but no bath-converged Ce-alloy Hamiltonian, state preparation or compiled full-loop cost is published here."}
  willingness_to_pay: {level: second-hand, note: "Ce substitution has clear supply and performance motivation and measured magnet properties, but no manufacturer target for a quantum-improved anisotropy calculation is cited."}
resources: {logical_qubits: "56–98 system qubits in an illustrative 7-orbital impurity with 3–6 bath sites per spin orbital", gates: "unknown for a named Ce alloy", note: "Bath convergence, temperature, observable error, state preparation and the DMFT loop have not been compiled. The illustrative T-gate multiplication on the method page is not an application estimate."}
related:
  applications: [battery-cathode-spectroscopy, nuclear-fuel-actinide-spectra]
  problems: [linear-response-spectral-functions, ground-state-energy]
  methods: [dmft-impurity-solver, embedding-divide-and-conquer]
  questions: [dmft-impurity-cost-vs-ctqmc-sign-problem]
references:
  - {arxiv: "2206.15093", title: "Ce and Dy substitutions in Nd$_{2}$Fe$_{14}$B: site-specific magnetic anisotropy from first-principles", authors: "J. Boust et al.", year: 2022, note: "Sections II.6 and IV.3; direct alloy calculation, Ce treatment and comparison with magnetic measurements"}
  - {arxiv: "1508.07792", title: "Growth and Characterization of Ce- Substituted Nd2Fe14B Single Crystals", authors: "M. A. Susner et al.", year: 2015, note: "Measured magnetisation, anisotropy field and Curie temperature at x=0.38"}
  - {arxiv: "2006.01792", title: "Intrinsically weak magnetic anisotropy of cerium in potential hard-magnetic intermetallics", authors: "A. Galler et al.", year: 2020, note: "DFT+QMC study of CeFe12 and CeFe11Ti compounds, not the Nd2Fe14B alloy"}
  - {arxiv: "1510.03859", title: "Hybrid quantum-classical approach to correlated materials", authors: "B. Bauer et al.", year: 2016, note: "general quantum-impurity proposal, not a Ce-alloy benchmark"}
---

## Who needs it

Magnet manufacturers want to reduce dependence on Nd while preserving useful magnetic properties. The target here is partial Ce substitution in (Nd,Ce)₂Fe₁₄B. At Ce fraction x=0.38, a single-crystal study measured at 400 K a decrease in anisotropy field from 5.5 to 4.7 T and in Curie temperature from 586 to 543 K relative to Nd₂Fe₁₄B [2]. These measurements give a concrete decision context. No cited manufacturer has said that more accurate impurity calculations would change an acceptance decision at a specified tolerance or price.

## Bottleneck

The direct alloy study [1] calculated site-dependent rare-earth crystal fields and magnetic anisotropy with DFT plus a quasi-atomic Hubbard-I treatment for localised 4f shells. For the mixed-valent Ce ion, it used an approximate LSDA treatment and an experimentally informed sublattice model. The authors explain that a quantitative treatment of Ce intermediate valence would require a more demanding many-body solver [1, Section II.6]. Their comparison with measured magnetisation curves and substitution scenarios nevertheless produced usable predictions. The missing Ce dynamics has not been shown to alter a composition decision or to defeat the best classical solver on this alloy.

A related study treated Kondo screening and temperature-dependent anisotropy in CeFe₁₂ and CeFe₁₁Ti compounds using DFT+QMC [3]. Those are **different materials**. Its successful classical calculation prevents us from inferring a universal f-shell solver failure, while its comparison of Hubbard-I and dynamical results identifies the physical correction that a Ce-alloy benchmark could test.

## Computational problems

- [Impurity Green's functions and spectral response](../problems/linear-response-spectral-functions.html) for a specified Ce site, hybridisation and temperature inside an embedding calculation.
- [Ground-state and crystal-field quantities](../problems/ground-state-energy.html) feeding an anisotropy model. Coercivity also depends on microstructure, so an improved local 4f calculation addresses only part of the magnet design task.

## Best classical today

The starting baseline is the completed DFT+Hubbard-I and sublattice calculation on the **same Ce-substituted alloy** [1], assessed against measured anisotropy and magnetisation [1, 2]. For a dynamical extension, CT-QMC and the DFT+QMC treatment demonstrated on other Ce-Fe compounds [3] must be tried on the target alloy. A small average sign in one basis would not prove classical intractability; basis optimisation and other impurity solvers need to be compared at equal error.

## Best quantum today

Bauer et al. proposed using a quantum computer as the impurity solver within a classical DMFT loop [4]. A seven-orbital 4f shell with three to six discrete bath sites per spin orbital occupies 56–98 **system** qubits. This arithmetic does not show that the bath converges the Ce-site anisotropy, that an appropriate state can be prepared, or that an algorithm returns the finite-temperature quantity used by [1]. No quantum circuit or end-to-end cost is available for the alloy in [1].

## Verdict

Surviving as a candidate application, with **no demonstrated quantum opportunity on the named alloy**. The Ce substitution problem is real; the cited direct calculation is classical and approximates Ce, while a dynamical classical treatment has been performed on related Ce-Fe compounds. Progress requires a public Ce-alloy hybridisation function and anisotropy observable, a measured error-versus-cost curve for classical dynamical solvers at the relevant temperature, and a compiled quantum calculation on that identical impurity. The resulting improvement must then be tested against the uncertainty from site occupancy and microstructure and against a manufacturer-defined decision threshold.
