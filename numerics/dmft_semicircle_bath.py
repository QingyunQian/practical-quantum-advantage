"""Reproduce a finite-bath input check for the Kanamori Bethe-bath example.

Source: Eidelstein, Gull and Cohen, arXiv:1907.08570, Eq. (5), Figs. 2-3.
This calculates the noninteracting hybridisation function only. It does not
calculate the interacting Green's function or the cost of a quantum solver.

The fixed n-point Gauss-Chebyshev rule of the second kind is reproducible but
is not an optimised fit. Its errors are upper bounds achievable by this rule,
not lower bounds on the bath size required by any other representation.
"""

import argparse
import json
import math
from pathlib import Path


def semicircle_bath(n: int, half_bandwidth: float = 2.0):
    """Return nodes and normalized weights for a semicircular density."""
    if n < 1:
        raise ValueError("n must be positive")
    nodes = [half_bandwidth * math.cos(k * math.pi / (n + 1)) for k in range(1, n + 1)]
    weights = [2 * math.sin(k * math.pi / (n + 1)) ** 2 / (n + 1) for k in range(1, n + 1)]
    assert abs(sum(weights) - 1.0) < 1e-12
    return nodes, weights


def exact_delta(iw: float, half_bandwidth: float = 2.0) -> complex:
    """Stieltjes transform of 2 sqrt(D²-e²)/(pi D²), with t=1."""
    d = half_bandwidth
    return -2j / (iw + math.sqrt(iw * iw + d * d))


def discrete_delta(iw: float, nodes: list[float], weights: list[float]) -> complex:
    return sum(weight / (1j * iw - energy) for energy, weight in zip(nodes, weights))


def bath_error(n: int, beta: float, n_freq: int = 80) -> dict:
    nodes, weights = semicircle_bath(n)
    errors = []
    for k in range(n_freq):
        iw = (2 * k + 1) * math.pi / beta
        errors.append(abs(discrete_delta(iw, nodes, weights) - exact_delta(iw)))
    # At r=1 the 2x2 orbital hybridisation matrix has rank one for each spin.
    # A common bath for the two orbitals therefore needs n modes per spin.
    return {
        "bath_nodes_per_spin": n,
        "system_qubits_rank_one_bath": 4 + 2 * n,
        "lowest_matsubara_abs_error": errors[0],
        "max_abs_error_first_80_matsubara": max(errors),
    }


def run(beta: float = 64.0, n_freq: int = 80, max_nodes: int = 256) -> dict:
    sample_nodes = [1, 2, 4, 8, 16, 23, 32, 40, 48, 64, 96, 128, 192, 256]
    rows = [bath_error(n, beta, n_freq) for n in sample_nodes if n <= max_nodes]
    thresholds = {}
    for target in [0.1, 0.01, 0.001]:
        first = next(
            (bath_error(n, beta, n_freq) for n in range(1, max_nodes + 1)
             if bath_error(n, beta, n_freq)["max_abs_error_first_80_matsubara"] < target),
            None,
        )
        thresholds[str(target)] = first["bath_nodes_per_spin"] if first else None
    return {
        "source": "https://arxiv.org/abs/1907.08570",
        "model": "two spinful Kanamori orbitals, r=1, t=1, D=2 semicircular bath",
        "calculated_quantity": "bath hybridisation Delta_ij(iomega), not interacting G_ij(tau)",
        "method": "unoptimised Gauss-Chebyshev quadrature of the second kind",
        "beta": beta,
        "matsubara_frequencies": n_freq,
        "error_units": "absolute energy units with t=1; each matrix entry has the same error",
        "rows": rows,
        "first_bath_nodes_below_max_abs_error": thresholds,
        "caveat": "No lower bound on optimized bath size; no interacting-G convergence or quantum cost.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--beta", type=float, default=64.0)
    parser.add_argument("--n-freq", type=int, default=80)
    parser.add_argument("--max-nodes", type=int, default=256)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.beta, args.n_freq, args.max_nodes)
    content = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content)
