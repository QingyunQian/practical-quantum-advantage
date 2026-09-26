# Reproducing the DMFT bath-input check

The scripts `dmft_semicircle_bath.py` and `dmft_semicircle_bath_fit.py` examine the *input bath* of the two-orbital Kanamori model in [Eidelstein, Gull and Cohen, arXiv:1907.08570](https://arxiv.org/abs/1907.08570), Eqs. 5 and the continuous-band paragraph following it. The parameters are `t=1`, `D=2`, `r=1`. The model has four interacting spin orbitals; at `r=1`, its orbital hybridisation matrix has rank one for each spin.

The first script uses the fixed Gauss-Chebyshev rule for the semicircular spectral density. It is a useful check of the analytic transform, **not** an optimized fit. The second fits symmetric pairs of finite-bath poles with positive normalized weights to the first 80 fermionic Matsubara values. It then checks the imaginary-time bath kernel at 81 points against 2048-node quadrature; 4096-node quadrature checks the numerical reference. The fitted kernel is the noninteracting hybridisation `Delta`. It is **not** the interacting impurity Green's function `G`, a DMFT result or a quantum-algorithm benchmark.

The fixed quadrature script uses the Python standard library. For the fit, install NumPy and SciPy, then run from the repository root:

```sh
python numerics/dmft_semicircle_bath.py --output numerics/results/dmft_semicircle_bath.json
python numerics/dmft_semicircle_bath_fit.py --beta 64 --output numerics/results/dmft_semicircle_bath_fit_beta64.json
```

The other published JSON files use `--beta 16`, `32`, `128` and `256`. The optimization stops at the first tested even number of bath nodes with maximum Matsubara error below `1e-3`, or at ten nodes. Results are achieved errors for this local optimizer, not global optima or lower bounds on the number of bath sites. A quantum comparison still needs convergence of `G` at the same temperature and output error, plus state preparation and full workflow costs.

With matplotlib installed, `python numerics/plot_dmft_bath_fit.py` regenerates the [figure](figs/dmft_bath_input_fit.png). The shaded 50–100-qubit region is a register-size reference, not a crossover claim.
