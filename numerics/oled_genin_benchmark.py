"""Recompute the 14-emitter errors in Genin et al., arXiv:2512.13657v2.

Input is transcribed from the paper's SI.1 Tables SI.1-2 and SI.1-3:
https://arxiv.org/html/2512.13657 . All gaps are eV. The Q1 classical
runtime and active-space data below are from Tables SI.2-2 and SI.3-1.
Run: python numerics/oled_genin_benchmark.py

This reproduces published aggregate errors, not the electronic-structure
calculation. No QPE cost is inferred from these data.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "results" / "oled_genin2026_si1.csv"
OUTPUT = ROOT / "results" / "oled_genin2026_reanalysis.json"
FIGURE = ROOT / "figs" / "oled_genin2026_accuracy.png"
SOURCE = "https://arxiv.org/html/2512.13657"
METHODS = ["td_b3lyp", "ccsd", "cr_cc_2_3", "iqcc", "iqcc_pt"]
LABELS = ["TD-B3LYP", "CCSD", "CR-CC(2,3)", "iQCC", "iQCC+PT"]
REPORTED_MAE = {"td_b3lyp": .1209, "ccsd": .2200,
                "cr_cc_2_3": .2912, "iqcc": .1180, "iqcc_pt": .0501}
# SI.2-2: Q1 *singlet-state solver* wall time, not a complete emission-gap run.
Q1_SINGLET_HOURS = {50: 87.02, 70: 107.10, 100: 199.37}
# SI.3-1: Q1 uncorrected iQCC emission gap by active-space orbital count.
Q1_IQCC_GAP = {50: 1.999, 70: 1.988, 100: 1.932}


def main():
    with DATA.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    assert len(rows) == 14 and [r["material"] for r in rows] == [f"Q{i}" for i in range(1, 15)]
    mae = {method: mean(abs(float(r[method]) - float(r["experiment"])) for r in rows)
           for method in METHODS}
    # Source tables round individual gaps to 0.001 eV; published MAEs have 4 decimals.
    for method in METHODS:
        assert abs(mae[method] - REPORTED_MAE[method]) < .001, (method, mae[method])
    q1 = rows[0]
    q1_error = {method: abs(float(q1[method]) - float(q1["experiment"])) for method in METHODS}
    result = {
        "source": SOURCE, "source_version": "arXiv:2512.13657v2", "n_emitters": len(rows),
        "units": "eV", "mae_from_rounded_supplement": mae,
        "reported_mae": REPORTED_MAE,
        "q1_experiment": float(q1["experiment"]), "q1_absolute_error": q1_error,
        "q1_singlet_solver_hours_by_orbitals": Q1_SINGLET_HOURS,
        "q1_uncorrected_iqcc_gap_by_orbitals": Q1_IQCC_GAP,
        "limitations": [
            "The per-molecule gaps are rounded to 0.001 eV in the source tables.",
            "The Q1 runtime is for one singlet-state classical solver run, not the full emission-gap workflow.",
            "The paper provides no same-Hamiltonian quantum phase-estimation cost or DMRG/SHCI cost curve.",
            "The 0.0501 eV cohort MAE is an achieved result, not a stated buyer acceptance threshold.",
            "SI.3-1 and SI.1-2 list different Q1 uncorrected iQCC gaps at CAS(70,70); the active-space series is not joined to the benchmark series.",
        ],
    }
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6), sharey=True)
    for ax, values, title in zip(axes, [mae, q1_error], ["14 emitters: mean absolute error", "Q1: absolute error"]):
        colors = ["#7b8fa1"] * 3 + ["#3b82a0", "#c45a3a"]
        ax.bar(range(len(METHODS)), [values[m] for m in METHODS], color=colors)
        ax.set_xticks(range(len(METHODS)), LABELS, rotation=35, ha="right")
        ax.set_title(title)
        ax.grid(axis="y", alpha=.18)
    axes[0].set_ylabel("Error in T1 → S0 gap (eV)")
    fig.suptitle("Classical calculations reported in Genin et al. (2026)")
    fig.text(.5, -.02, "iQCC and iQCC+PT were run on classical processors; Q1 gap data use CAS(70,70).", ha="center", fontsize=9)
    fig.tight_layout()
    FIGURE.parent.mkdir(exist_ok=True)
    fig.savefig(FIGURE, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print("Recomputed MAEs:", {k: round(v, 4) for k, v in mae.items()})
    print("Q1 errors:", {k: round(v, 4) for k, v in q1_error.items()})
    print(f"Wrote {OUTPUT} and {FIGURE}")


if __name__ == "__main__":
    main()
