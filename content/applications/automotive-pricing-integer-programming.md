---
type: application
id: automotive-pricing-integer-programming
title: Vehicle option-package pricing as an integer program (DQI case study)
title_zh: 汽车选装包定价的整数规划（DQI 案例）
summary: The only public attempt to apply decoded quantum interferometry to an industrial problem, co-authored by BMW Group and BCG. The pricing ILP is converted to max-XORSAT through AND and CARRY gadgets, which inflate the variable count and, unless avoided, drop the dual code's distance to 2. The authors benchmark against Gurobi and do not claim to beat it; at tested sizes Gurobi wins clearly.
summary_zh: 唯一公开的把解码量子干涉（DQI）用于工业问题的尝试，由宝马集团与 BCG 合著。定价整数规划要经过 AND 和 CARRY gadget 转成 max-XORSAT，变量数膨胀，且若不加处理对偶码的码距会降到 2。作者与 Gurobi 做了对比，没有声称超过它；在测试规模上 Gurobi 明显领先。
status: seed
last_verified: 2026-09-26
verdict: surviving
dimensions:
  classical_hardness: {level: none, note: "Gurobi returns optimal solutions for the tested instances; the authors' own benchmark shows a significant gap in DQI's disfavour; no hardness evidence for this ILP family"}
  quantum_easiness: {level: conditional, note: "DQI needs the dual of the constraint matrix to be an efficiently decodable code with large distance; the ILP-to-max-XORSAT reduction does not naturally supply one, and the naive reduction gives distance 2"}
  willingness_to_pay: {level: first-hand, note: "BMW Group researchers co-authored the study and supplied the problem; no accuracy or speed target is stated"}
resources: {note: "worked circuit example is m=3 constraints, n=2 variables with two belief-propagation iterations; no fault-tolerant estimate for an industrial instance"}
related:
  problems: [combinatorial-optimization]
  methods: [dqi]
  questions: [first-hand-payment-evidence]
references:
  - {arxiv: "2509.08328", title: "Towards solving industrial integer linear programs with Decoded Quantum Interferometry", authors: "F. Sabater, O. El Harzli, G.-J. Besjes, M. Erdmann, J. Klepsch, J. Hiltrop, J.-F. Bobier, Y. Cao, C. A. Riofrío (BMW Group, BCG, TUM)", year: 2026, note: "Quantum Sci. Technol. 11, 025054"}
  - {arxiv: "2408.08292", title: "Optimization by Decoded Quantum Interferometry", authors: "S. P. Jordan, N. Shutty, M. Wootters, A. Zalcman, A. Schmidhuber, R. Babbush, et al.", year: 2025, note: "Nature 646, 831; the algorithm and its decodability precondition"}
  - {arxiv: "2509.14509", title: "Spin Glass Transitions Obstruct Decoded Quantum Interferometry", authors: "E. R. Anschuetz, D. Gamarnik, J. Z. Lu", year: 2025, note: "random sparse instances blocked by the overlap-gap property"}
  - {arxiv: "2603.04540", title: "Tight inapproximability of max-LINSAT and implications for decoded quantum interferometry", authors: "M. J. Kramer, C. Schubert, J. Eisert", year: 2026, note: "beating the trivial r/q fraction on general max-LINSAT is NP-hard, so any advantage must come from structure"}
---

## Who needs it

Car makers price option packages (trim levels, bundles of features) to maximise margin subject to demand, production and consistency constraints. BMW Group posed the problem and co-authored the study with Boston Consulting Group [1]. It stands in for a class of mid-sized integer linear programs (ILPs) that every large manufacturer solves routinely with commercial solvers.

## Bottleneck

There is none on the classical side that the paper identifies. The ILP is solved by Gurobi, and the paper's benchmark uses Gurobi's optimal solutions as the reference against which DQI is measured [1]. The study is an existence test: can an industrial ILP be put into the form that decoded quantum interferometry (DQI) requires, and does the algorithm do anything on it?

## Computational problems

- [Combinatorial optimization](../problems/combinatorial-optimization.html): integer programming; the specific structured sub-family DQI targets is max-LINSAT / max-XORSAT with a decodable dual code.

## What DQI requires

DQI maximises the number of satisfied linear constraints Bx ∈ F over a finite field, and its advantage comes from decoding the code whose parity-check matrix is Bᵀ: the better the decoder (more errors corrected, up to a large fraction of the code distance), the better the objective value reached [2]. Two 2025–26 results fence the method in. Anschuetz, Gamarnik and Lu show that on random sparse instances the overlap-gap property obstructs DQI, so the structure must be non-random [3]. Kramer, Schubert and Eisert show that exceeding the trivial r/q satisfaction fraction on general max-LINSAT is NP-hard, so whatever DQI gains has to come from an instance family with a good decoder, not from the algorithm in general [4].

## What the case study found

Sabater et al. formulate the pricing problem as an ILP, then reduce it to max-XORSAT over F₂ [1]. The reduction encodes pseudo-Boolean constraints through AND and CARRY gadgets (auxiliary variables with weighted clauses, hard clauses for the constraints and soft clauses for the objective), which inflates the number of variables. The reduction has to be designed so that Bᵀ is the parity-check matrix of a code of reasonably high distance; the authors note that the simplest encoding, which repeats rows of B, produces repeated columns in Bᵀ and hence a code of distance 2, disqualifying it. They implement belief propagation as the quantum decoder and give the full circuit for a toy instance with m = 3 constraints and n = 2 variables over two iterations. On the benchmark, DQI consistently beats random sampling, but "compared to the state-of-the-art classical solver Gurobi, the performance gap remains significant", and the average DQI performance decreases with problem size toward an asymptotic value. The authors observe favourable scaling of quantum resources and note that classical methods are expected to scale exponentially, but they make no claim of beating Gurobi on any instance.

The gap between what DQI needs and what the ILP supplies is structural. DQI's precondition is a code with an efficient decoder and distance close to what the semicircle law needs; the reduction produces a matrix whose code properties are whatever the gadgets happen to leave, and the paper spends its effort keeping the distance above 2 rather than making it large. Belief propagation, the decoder chosen, is heuristic and its success rate on LDPC codes falls quickly with error weight, which caps the achievable objective.

## Verdict

Surviving, in the weak sense that no theorem forbids an industrial ILP whose constraint matrix happens to have a decodable dual code; this instance is not one, and the study does not claim it is. Classical hardness is absent (Gurobi solves it), the quantum precondition is not met by the reduction, and the willingness to pay is first-hand only for the study, not for an outcome. The page is here because it is the single public data point on whether DQI's structural requirement occurs in industry, and the answer so far is no. It would move to promising if an ILP family arising in practice were shown to reduce to max-XORSAT with a dual code of distance growing with size and a decoder that approaches it; it would move to no-go if such reductions were shown to always collapse the distance.
