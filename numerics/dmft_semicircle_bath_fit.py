"""Fit a symmetric finite bath on the Matsubara axis; requires NumPy/SciPy.

Run: python numerics/dmft_semicircle_bath_fit.py --output numerics/results/dmft_semicircle_bath_fit.json
The optimized objective is an L2 fit to 80 Matsubara values. Reported errors
include a separate 81-point imaginary-time bath check against high-order
quadrature. No interacting-G accuracy is implied.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import least_squares

from dmft_semicircle_bath import exact_delta, semicircle_bath


def delta_tau_from_pairs(tau, energy, weight, beta):
    """Imaginary-time hybridisation from symmetric +/- pole pairs."""
    return -float(np.sum(weight * (
        np.exp(-energy * tau) + np.exp(-energy * (beta - tau))
    ) / (1 + np.exp(-beta * energy))))


def fit_bath(n_pairs: int, beta: float = 64.0, n_freq: int = 80) -> dict:
    nodes, weights = semicircle_bath(2 * n_pairs)
    positive = [(e, w) for e, w in zip(nodes, weights) if e > 0]
    energies0 = np.array([e for e, _ in positive])
    logs0 = np.log(np.array([w for _, w in positive]) * 2)
    omega = (2 * np.arange(n_freq) + 1) * np.pi / beta
    target = np.array([exact_delta(float(w)).imag for w in omega])

    def pair_weights(logits):
        shifted = logits - np.max(logits)
        e = np.exp(shifted)
        return 0.5 * e / np.sum(e)

    def residual(params):
        energy, logits = params[:n_pairs], params[n_pairs:]
        pair_weight = pair_weights(logits)
        got = -2 * omega * np.sum(
            pair_weight[None, :] / (omega[:, None] ** 2 + energy[None, :] ** 2), axis=1
        )
        return got - target

    result = least_squares(
        residual,
        np.r_[energies0, logs0],
        bounds=(np.r_[np.zeros(n_pairs), np.full(n_pairs, -30.0)],
                np.r_[np.full(n_pairs, 2.0), np.full(n_pairs, 30.0)]),
        max_nfev=2000,
        ftol=1e-12,
        xtol=1e-12,
        gtol=1e-12,
    )
    energy = result.x[:n_pairs]
    weight = pair_weights(result.x[n_pairs:])
    errors = np.abs(residual(result.x))

    # A high-order positive quadrature supplies an independent bath-kernel
    # reference. Compare 2048 and 4096 nodes to verify its numerical precision.
    def exact_tau_reference(n_nodes):
        high_nodes, high_weights = semicircle_bath(n_nodes)
        pairs = [(e, w) for e, w in zip(high_nodes, high_weights) if e > 0]
        e = np.array([x[0] for x in pairs])
        w = np.array([x[1] for x in pairs])
        return np.array([delta_tau_from_pairs(t, e, w, beta) for t in tau_grid])

    tau_grid = np.linspace(0.0, beta, 81)
    reference_tau = exact_tau_reference(2048)
    refinement_error = float(np.max(np.abs(reference_tau - exact_tau_reference(4096))))
    assert refinement_error < 1e-11
    fitted_tau = np.array([delta_tau_from_pairs(t, energy, weight, beta) for t in tau_grid])
    tau_errors = np.abs(fitted_tau - reference_tau)
    return {
        "bath_nodes_per_spin": 2 * n_pairs,
        "system_qubits_rank_one_bath": 4 + 4 * n_pairs,
        "lowest_matsubara_abs_error": float(errors[0]),
        "max_abs_error_first_80_matsubara": float(np.max(errors)),
        "max_abs_error_81_imaginary_time_points": float(np.max(tau_errors)),
        "imaginary_time_reference_refinement_error": refinement_error,
        "positive_bath_energies": [float(x) for x in energy],
        "weight_at_each_positive_and_negative_energy": [float(x) for x in weight],
        "converged": bool(result.success),
        "function_evaluations": int(result.nfev),
    }


def run(beta: float = 64.0):
    rows = []
    for n_pairs in range(1, 6):
        row = fit_bath(n_pairs, beta=beta)
        rows.append(row)
        if row["converged"] and row["max_abs_error_first_80_matsubara"] < 1e-3:
            break
    return {
        "source": "https://arxiv.org/abs/1907.08570",
        "model": "two spinful Kanamori orbitals, r=1, t=1, D=2 semicircular bath",
        "calculated_quantity": "bath hybridisation Delta_ij(iomega), not interacting G_ij(tau)",
        "method": "bounded nonlinear least squares, symmetric positive-energy pole pairs and positive normalized weights, initialized by Gauss-Chebyshev nodes",
        "numpy_version": np.__version__,
        "scipy_version": scipy.__version__,
        "beta": beta,
        "matsubara_frequencies": 80,
        "rows": rows,
        "stopping_rule": "first tested even-node fit with optimizer success and maximum Matsubara error below 1e-3, or five pole pairs",
        "caveat": "These are achieved errors, not lower bounds or a global optimum; the interacting Green's function and quantum cost are untested.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--beta", type=float, default=64.0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = json.dumps(run(args.beta), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content)
