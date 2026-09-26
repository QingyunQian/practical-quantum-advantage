"""Plot finite-bath input errors from the committed JSON results.

Requires matplotlib. This is a bath-representation comparison, not a plot of
interacting Green's-function error or quantum versus classical runtime.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
FIGURE = ROOT / "figs" / "dmft_bath_input_fit.png"


def read(name):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def main():
    fixed = read("dmft_semicircle_bath.json")
    fitted = read("dmft_semicircle_bath_fit_beta64.json")
    betas = [16, 32, 64, 128, 256]
    scaling = [read(f"dmft_semicircle_bath_fit_beta{b}.json") for b in betas]

    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.8), layout="constrained")
    ax = axes[0]
    fx = [r["system_qubits_rank_one_bath"] for r in fixed["rows"] if r["system_qubits_rank_one_bath"] <= 132]
    fy = [r["max_abs_error_first_80_matsubara"] for r in fixed["rows"] if r["system_qubits_rank_one_bath"] <= 132]
    ox = [r["system_qubits_rank_one_bath"] for r in fitted["rows"]]
    oy = [r["max_abs_error_first_80_matsubara"] for r in fitted["rows"]]
    ax.semilogy(fx, fy, "o-", color="#808895", label="fixed quadrature")
    ax.semilogy(ox, oy, "s-", color="#176c92", label="fitted bath")
    ax.axhline(1e-3, ls="--", lw=1, color="#ac6036", label="input-error target")
    ax.axvspan(50, 100, color="#dbe7eb", alpha=0.55)
    ax.set_xlim(0, 135)
    ax.set_ylim(1e-5, 30)
    ax.set_xlabel("System qubits (four impurity + bath)")
    ax.set_ylabel("Max |bath Δ error| on 80 Matsubara points")
    ax.set_title("Same continuous bath, βt = 64")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.15)

    ax = axes[1]
    required = [d["rows"][-1]["system_qubits_rank_one_bath"] for d in scaling]
    ax.plot(betas, required, "o-", color="#176c92")
    ax.set_xscale("log", base=2)
    ax.set_xticks(betas, [str(b) for b in betas])
    ax.set_ylim(12, 28)
    ax.set_yticks([16, 20, 24])
    ax.set_xlabel("Inverse temperature βt")
    ax.set_ylabel("Qubits at first tested fit below 1e-3")
    ax.set_title("Exploratory bath-input sweep")
    ax.grid(alpha=0.15)
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE, dpi=180)
    print(FIGURE)


if __name__ == "__main__":
    main()
