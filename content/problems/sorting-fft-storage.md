---
type: problem
id: sorting-fft-storage
title: Sorting, Fourier transforms and classical data storage
title_zh: 排序、傅里叶变换与经典数据存储
summary: Comparison sorting has a matching quantum Ω(N log N) comparison lower bound. For a full classical Fourier spectrum, input and output alone cost Ω(N), which defeats an exponential speedup inferred solely from the QFT circuit but does not prove a matching Ω(N log N) quantum lower bound. Holevo constrains complete classical-data recovery; QRAM costs depend on its architecture and the classical comparator.
summary_zh: 比较排序有与经典算法相同的 Ω(N log N) 量子比较下界。若要处理并输出完整的经典傅里叶谱，读写本身至少需要 Ω(N)；这排除了只凭 QFT 电路就声称指数加速的论证，但没有证明量子算法也需要 Ω(N log N)。Holevo 界约束经典数据的完整读取；QRAM 的成本还取决于架构与经典比较对象。
status: seed
last_verified: 2026-09-27
verdict: surviving
dimensions:
  classical_hardness: {level: none, note: "classical comparison sorting is Θ(N log N), full complex DFT has an O(N log N) FFT, and conventional storage is mature; no hard named workload is established here"}
  quantum_easiness: {level: conditional, note: "comparison sorting cannot improve its asymptotic comparison count; QFT is efficient on prepared quantum states, while arbitrary classical-array input and complete classical output each cost Ω(N). These facts do not establish an Ω(N log N) quantum lower bound for classical-array DFT."}
  willingness_to_pay: {level: unknown, note: "sorting, spectral analysis and storage have users, but this page does not cite a buyer target for a quantum replacement at matched output and cost"}
related:
  applications: [weather-forecasting]
  problems: [sparse-linear-systems, classical-data-machine-learning, monte-carlo-expectation]
  methods: [qram, grover-amplitude-estimation]
  questions: [classical-output-fourier-crossover]
references:
  - {url: "https://arxiv.org/abs/quant-ph/0102078", title: "Quantum complexities of ordered searching, sorting, and element distinctness", authors: "P. Høyer, J. Neerbek, Y. Shi", year: 2002, note: "Algorithmica 34, 429; Ω(N log N) comparisons for quantum sorting; ordered search lower bound (1/π)(ln N − 1)"}
  - {url: "https://arxiv.org/abs/quant-ph/9607014", title: "A Quantum Algorithm for Finding the Minimum", authors: "C. Dürr, P. Høyer", year: 1996, note: "O(√N) quantum queries for one minimum under coherent table access"}
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103; break-even analysis for quadratic speedups"}
  - {doi: "10.1038/nphys3272", title: "Read the fine print", authors: "S. Aaronson", year: 2015, note: "Nature Physics 11, 291; amplitude loading and readout are Ω(N)"}
  - {arxiv: "2606.18981", title: "Not Your Usual FFT: QFT→FFT via Classical Quantum-Circuit Simulation", authors: "S. Markidis, G. Netzer, L. Pennati, F. Larssen, I. Peng", year: 2026, note: "an FFT library implemented as classical simulation of the QFT circuit, on par with FFTW"}
  - {title: "Bounds for the quantity of information transmitted by a quantum communication channel", authors: "A. S. Holevo", year: 1973, note: "Problems Inform. Transmission 9, 177; accessible classical information bound under its communication model"}
  - {url: "https://arxiv.org/abs/quant-ph/9904093", title: "Optimal lower bounds for quantum automata and random access codes", authors: "A. Nayak", year: 1999, note: "(1-H(p))N qubit lower bound for random access to arbitrary bits with success probability p"}
  - {arxiv: "2305.10310", title: "QRAM: A Survey and Critique", authors: "S. Jaques, A. G. Rattew", year: 2025, note: "Quantum 9, 1922"}
  - {arxiv: "2503.19172", title: "Resource-state Quantum RAM for Fast and Error-Correctable Queries", authors: "F. Cesa, H. Bernien, H. Pichler", year: 2026, note: "Nat. Commun.; offline resource-state QRAM proposal and fault-tolerance analysis"}
---

## Best classical

Comparison sorting is Θ(N log N), and an FFT computes the full N-point discrete Fourier transform in O(N log N) arithmetic operations. These are well-developed classical baselines. A comparison lower bound for sorting says nothing about the arithmetic complexity of a Fourier transform. For storage, compare the number of recoverable classical bits, lifetime and access cost separately.

## Best quantum

Sorting. Høyer, Neerbek and Shi prove that quantum **comparison-based sorting** needs Ω(N log N) comparisons, matching the classical asymptotic bound [1]. Ordered search can still improve its constant factor [1]. The theorem does not cover non-comparison promises on keys or other data structures. Finding **one minimum** in an unsorted list takes O(√N) quantum queries given coherent value access [2]; that result must not be assigned to an arbitrary top-k output. Its oracle and hardware costs need a separate economic comparison [3].

Fourier transform. The QFT on n qubits uses O(n²) gates on an N = 2ⁿ dimensional **quantum state**. It is useful inside phase estimation and period finding when a circuit prepares the input and the algorithm reads a small amount of classical information. A task that instead starts with an arbitrary array of N classical numbers and asks for the entire complex spectrum must account for reading those numbers and producing N outputs. Each step costs at least Ω(N). This defeats a claimed *exponential end-to-end gain inferred from the QFT gate count alone* [4]. It does not establish that every quantum algorithm for the classical-array task needs Ω(N log N) work, nor does it rule out restricted-output tasks. A single QFT measurement samples a frequency according to its squared amplitude; it does not return the complex spectrum.

Markidis et al. implement a classical FFT library by simulating a QFT circuit [5]. Their AVX implementation is comparable with multithreaded FFTW on the **same CPU**. Their CUDA result is faster than the reported **CPU** runs; it is not a matched comparison against a GPU FFT library. The experiment demonstrates that this QFT-derived computation can be competitive as a classical implementation, not a quantum-hardware speedup or a general Fourier lower bound.

Storage. Holevo's bound limits the amount of classical information recoverable from n transmitted qubits to n bits under its communication assumptions [6]. For a weaker task, such as retrieving any *chosen* bit with a fixed success probability p > 1/2, quantum random-access codes can encode more than n bits into n qubits by a constant factor; Nayak's bound still requires memory linear in the input length [7]. Neither statement is a universal comparison of physical storage technologies. QRAM is an addressing mechanism for existing cells, not an exponential classical-data compression scheme. Its cost and opportunity-cost caveats are discussed on the [QRAM method page](../methods/qram.html) [8, 9].

## Verdict

Surviving as a **combined catalogue entry**, with different conclusions for its three tasks and no demonstrated practical advantage. There is a genuine no-go for an asymptotic comparison-count improvement in comparison sorting. Complete classical-array input and output prevent the QFT's polylogarithmic circuit size from becoming an exponential end-to-end Fourier speedup by itself; a matching quantum lower bound for the full DFT has not been shown here. Holevo and Nayak rule out exponential storage compression under their retrieval models, while QRAM remains an architecture and cost question. A narrower output, structured input, or new implementation could change the Fourier and QRAM assessments, provided it beats the best classical method on the same task.
