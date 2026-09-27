---
type: question
id: classical-output-fourier-crossover
title: Can a quantum Fourier algorithm beat an FFT on the same classical-output task?
title_zh: 量子傅里叶算法能否在相同的经典输出任务上超越 FFT？
summary: A QFT transforms a prepared quantum state efficiently, whereas a full N-point classical DFT requires N input values and N complex outputs. The resulting Ω(N) input/output floor does not establish an Ω(N log N) quantum lower bound. Define a matched exact or sparse-spectrum task, count data access and output accuracy, then test any claimed advantage against the best classical algorithm for that same task.
summary_zh: QFT 能高效变换已经制备好的量子态，但完整的 N 点经典 DFT 需要读入 N 个数并输出 N 个复数。由此得到的 Ω(N) 读写下界并未证明量子算法也需要 Ω(N log N)。需要先固定完整或稀疏频谱任务、数据访问方式和输出精度，再与同任务的最佳经典算法比较。
status: seed
last_verified: 2026-09-27
question:
  what_would_settle_it: "Specify a family of classical arrays, input interface, spectral promise, output format and error metric. For the full spectrum, count all N input reads and N complex outputs, then either prove a stronger quantum lower bound in the stated model or give an end-to-end quantum algorithm below the best matched FFT cost. For a sparse or top-m spectrum, count construction and queries to coherent data access, inner-product and selection oracles, repetitions, and classical output of indices and amplitudes; compare with tuned classical sparse-FFT and streaming methods at the same success probability and error. Report work, depth, memory, preprocessing and hardware separately, including how they scale with N and m."
  difficulty: phd
  resolved: false
related:
  problems: [sorting-fft-storage]
  methods: [qram]
references:
  - {doi: "10.1145/321752.321761", title: "Note on a Lower Bound on the Linear Complexity of the Fast Fourier Transform", authors: "J. Morgenstern", year: 1973, note: "Ω(N log N) for the unnormalized DFT in the bounded-coefficient linear-circuit model"}
  - {arxiv: "1403.1307", title: "An n\\log n Lower Bound for Fourier Transform Computation in the Well Conditioned Model", authors: "N. Ailon", year: 2014, note: "Ω(N log N) for constant R under a well-conditioned linear-circuit model; not a general quantum lower bound"}
  - {arxiv: "0706.2451", title: "Quantum Discrete Fourier Transform with Classical Output for Signal Processing", authors: "C.-Y. Pang, B.-Q. Hu", year: 2007, note: "claims O(sqrt(N)) for selected large coefficients using preloaded data and parallel oracles; not a full-output bound"}
  - {arxiv: "1201.2501", title: "Nearly Optimal Sparse Fourier Transform", authors: "H. Hassanieh, P. Indyk, D. Katabi, E. Price", year: 2012, note: "classical O(k log N) for exact k-sparse spectra and O(k log N log(N/k)) for general signals under their access model"}
---

## Why it matters

Fourier analysis is used in signal processing, imaging and scientific computing. The quantum Fourier transform acts on N amplitudes using a circuit of size polynomial in log N, but that circuit produces a quantum state. It does not by itself implement the same interface as a classical FFT. A full classical N-point spectrum requires N input values and N complex outputs, giving an Ω(N) input/output floor. This floor alone leaves an asymptotic interval between linear work and the FFT's O(N log N) arithmetic cost.

Classical lower bounds already illustrate why the computational model must be named. Morgenstern proved Ω(N log N) for the *unnormalized* transform using bounded-coefficient linear circuits [1]. Ailon obtained an Ω(N log N) bound for a normalized transform in an R-well-conditioned linear-circuit model when R is constant [2]. Neither result applies automatically to arbitrary quantum algorithms with classical input and output.

There are also claims with a different output contract. Pang and Hu describe a quantum procedure that reports selected large Fourier coefficients and claim O(sqrt(N)) time when their number is small [3]. Their paper assumes a classical-data loading unitary and a parallel inner-product oracle, treating the latter's depth as approximately constant; the cost of building those resources and the weaker sparse-spectrum output need to be included. Classical sparse Fourier algorithms already run in O(k log N) time for exactly k-sparse spectra and O(k log N log(N/k)) for general signals under their sampling model [4]. Thus even an oracle-cost-corrected quantum procedure must beat a sparse-spectrum baseline on the same error and access model. The phrase “classical output” in [3] should not be read as all N complex coefficients.

## What would settle it

The front matter states two distinct tests. A full-spectrum result would need either an end-to-end quantum algorithm with less than O(N log N) work in a specified realistic model or a lower bound that closes that possibility in that model. A sparse-spectrum result could be valuable sooner, but it must compare against classical algorithms that return the same m frequencies and amplitudes with the same error guarantee. The first reproducible contribution is a cost table for one public signal family: input preparation, oracle construction, query count, depth, memory, output size, error and classical baseline. Report each quantity for both methods and show how it scales rather than citing only QFT gate count.
