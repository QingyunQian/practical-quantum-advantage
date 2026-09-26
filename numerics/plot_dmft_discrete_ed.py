"""Visual audit of reconstructed discrete-band ED against Fig. 2 endpoints."""

import json
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
FIGURE = ROOT / "figs" / "dmft_discrete_ed_audit.png"


def read(filename):
    return json.loads((RESULTS / filename).read_text(encoding="utf-8"))


def main():
    figure_data = read("dmft_fig2_digitized_endpoints.json")
    printed = read("dmft_discrete_kanamori_ed_printed_level0.json")
    shifted = read("dmft_discrete_kanamori_ed_level_minus1.json")
    fig, axes = plt.subplots(2, 2, figsize=(8.5, 6.2), sharex=True, sharey=True,
                             layout="constrained")
    for index, ax in enumerate(axes.flat):
        original = figure_data["rows"][index]
        direct = printed["variants"]["printed_eq5"][index]
        sensitivity = shifted["variants"]["printed_eq5"][index]
        ax.plot(direct["tau_over_beta"], direct["G_00"], color="#bc5749",
                ls="--", label="printed Eq. 5, level 0")
        ax.plot(sensitivity["tau_over_beta"], sensitivity["G_00"], color="#176c92",
                label="same model, level -1")
        ax.scatter([0, 1], [original["G_tau_0"]["G"], original["G_tau_beta"]["G"]],
                   marker="o", facecolors="white", edgecolors="black", s=38,
                   zorder=4, label="paper Fig. 2 plotted endpoints")
        ax.set_title(f"inverse temperature βt = {original['beta']}")
        ax.set_xlim(-0.02, 1.02)
        ax.set_ylim(-1.03, 0.03)
        ax.grid(alpha=0.15)
    for ax in axes[:, 0]:
        ax.set_ylabel("Imaginary-time G00")
    for ax in axes[1, :]:
        ax.set_xlabel("τ / β")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, -0.04), ncol=3,
               fontsize=8)
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE, dpi=180, bbox_inches="tight")
    print(FIGURE)


if __name__ == "__main__":
    main()
