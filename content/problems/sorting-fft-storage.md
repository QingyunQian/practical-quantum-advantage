---
type: problem
id: sorting-fft-storage
title: Sorting, Fourier transforms and classical data storage
title_zh: 排序、傅里叶变换与经典数据存储
summary: Three primitives that industry lists and that information theory rules out. Sorting needs Ω(N log N) comparisons on a quantum computer too, and the output alone is Ω(N). The quantum Fourier transform acts on amplitudes; loading or reading N classical numbers costs Ω(N), and the classical simulation of the QFT circuit is the FFT. The Holevo bound caps n qubits at n retrievable classical bits, and QRAM is an addressing structure whose controller could run a parallel classical algorithm equally fast.
summary_zh: 产业界常列、信息论却排除的三个原语。排序在量子计算机上同样需要 Ω(N log N) 次比较，仅输出就是 Ω(N)。量子傅里叶变换作用在振幅上，读入或读出 N 个经典数都要 Ω(N)，QFT 电路的经典模拟就是 FFT。Holevo 界规定 n 个量子比特最多可靠取出 n 个经典比特，而 QRAM 只是寻址结构，其控制硬件拿来跑并行经典算法一样快。
status: seed
last_verified: 2026-09-26
verdict: no-go
dimensions:
  classical_hardness: {level: none, note: "O(N log N) sorting and FFT are optimal or near-optimal classically and run at memory bandwidth; storage density is a hardware question"}
  quantum_easiness: {level: no, note: "Ω(N log N) comparisons for sorting (Høyer–Neerbek–Shi); Ω(N) to load or read N classical numbers; Holevo bound n bits per n qubits; no passive cheap QRAM (Jaques–Rattew)"}
  willingness_to_pay: {level: none, note: "no buyer has asked for quantum sorting or FFT; QRAM is demanded only as a component of other quantum algorithms"}
related:
  applications: [weather-forecasting]
  problems: [sparse-linear-systems, classical-data-machine-learning, monte-carlo-expectation]
  methods: [qram, grover-amplitude-estimation]
references:
  - {url: "https://arxiv.org/abs/quant-ph/0102078", title: "Quantum complexities of ordered searching, sorting, and element distinctness", authors: "P. Høyer, J. Neerbek, Y. Shi", year: 2002, note: "Algorithmica 34, 429; Ω(N log N) comparisons for quantum sorting; ordered search lower bound (1/π)(ln N − 1)"}
  - {doi: "10.1038/nphys3272", title: "Read the fine print", authors: "S. Aaronson", year: 2015, note: "Nature Physics 11, 291; amplitude loading and readout are Ω(N)"}
  - {arxiv: "2606.18981", title: "Not Your Usual FFT: QFT→FFT via Classical Quantum-Circuit Simulation", authors: "S. Markidis, G. Netzer, L. Pennati, F. Larssen, I. Peng", year: 2026, note: "an FFT library implemented as classical simulation of the QFT circuit, on par with FFTW"}
  - {title: "Bounds for the quantity of information transmitted by a quantum communication channel", authors: "A. S. Holevo", year: 1973, note: "Problems Inform. Transmission 9, 177; n qubits carry at most n classical bits"}
  - {arxiv: "2305.10310", title: "QRAM: A Survey and Critique", authors: "S. Jaques, A. G. Rattew", year: 2025, note: "Quantum 9, 1922"}
  - {arxiv: "2503.19172", title: "Resource-state Quantum RAM for Fast and Error-Correctable Queries", authors: "F. Cesa, H. Bernien, H. Pichler", year: 2026, note: "Nat. Commun.; a fault-tolerant QRAM construction that does not overturn the opportunity-cost argument"}
  - {url: "https://arxiv.org/abs/quant-ph/9701001", title: "Strengths and Weaknesses of Quantum Computing", authors: "C. H. Bennett, E. Bernstein, G. Brassard, U. Vazirani", year: 1997, note: "SIAM J. Comput. 26, 1510; Ω(√N) for unstructured search"}
  - {arxiv: "2011.04149", title: "Focus beyond quadratic speedups for error-corrected quantum advantage", authors: "R. Babbush, J. R. McClean, M. Newman, C. Gidney, S. Boixo, H. Neven", year: 2021, note: "PRX Quantum 2, 010103; why the quadratic remnants (min-finding, top-k) do not pay"}
---

## Best classical

Comparison sorting is Θ(N log N) and the FFT is O(N log N); both are memory-bandwidth-bound in practice and have decades of optimised libraries. Classical storage density is set by device physics, not by algorithms. None of the three has a classical bottleneck in the complexity sense; they are listed as quantum targets only because "quantum computers process exponentially many amplitudes" is misread as a statement about classical data.

## Best quantum

Sorting. Høyer, Neerbek and Shi prove that any quantum comparison-based sorting algorithm needs Ω(N log N) comparisons, matching the classical bound, and that ordered search on N sorted items needs at least (1/π)(ln N − 1) queries, a constant-factor improvement over log₂ N only [1]. Independently of the comparison model, emitting the sorted list is Ω(N) output. What survives is quadratic: finding the minimum or the top k of N unsorted items in O(√N) queries (Dürr–Høyer), bounded below by the BBBV Ω(√N) for unstructured search [7], and uneconomic for the reasons Babbush et al. give [8].

Fourier transform. The QFT on n qubits uses O(n²) gates and acts on 2ⁿ amplitudes, which is exponentially fewer operations than the FFT on 2ⁿ numbers. The speedup is real and is the engine of phase estimation and Shor's algorithm, where the input state is produced by a quantum circuit and only a few frequencies are read out. For classical signals it disappears at both ends: encoding N numbers into amplitudes takes Ω(N) operations, and a measurement returns one random frequency, so recovering the full spectrum takes Ω(N) repetitions [2]. Markidis et al. make the point in code: they build an FFT library that computes the discrete Fourier transform by classically simulating the QFT circuit, and it performs on par with multithreaded FFTW on a CPU and faster on a GPU [3]. The classical simulation of the QFT circuit is the FFT. Only a few Fourier coefficients or spectral statistics can be estimated with a quadratic gain by amplitude estimation, and that is again uneconomic.

Storage. Holevo's bound limits the classical information retrievable from n qubits to n bits [4]; a quantum memory does not hold more data than a classical one of the same size, and it decoheres. QRAM, the structure that would let a quantum algorithm address N classical cells in superposition, is not a storage device but an addressing tree of N components. Jaques and Rattew separate active QRAM (controlled at every query) from passive QRAM (ballistic, no external control) and give the opportunity-cost argument: the control hardware of an active QRAM, or the qubits themselves, could run an extremely parallel classical algorithm and get the same results just as fast, which removes most asymptotic advantage in quantum linear algebra; cheap, scalable passive QRAM they judge unlikely under existing proposals [5]. Fault-tolerant constructions (bucket-brigade with polylog overhead, the resource-state QRAM of Cesa, Bernien and Pichler [6]) improve the constant but do not answer the opportunity-cost argument, because they still require N physical components to be built and controlled.

## Verdict

No-go. All three are information-theoretic: the bounds hold for any quantum algorithm and do not move with hardware or with algorithmic progress. The remaining quadratic fragments (min-finding, a few spectral coefficients) inherit the Grover economics and are uneconomic. Nothing on this page can change; it exists so that the catalogue can say why "quantum databases", "quantum FFT" and "quantum sorting" do not appear elsewhere in it.
