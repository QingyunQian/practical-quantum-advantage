"""Figure: ideal-limit SQD vs classical selection on 4x3 Hubbard."""
import json, glob, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))
C = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
TXT, TXT2, GRID, SURF = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "axes.edgecolor": GRID, "axes.labelcolor": TXT,
                     "xtick.color": TXT2, "ytick.color": TXT2, "text.color": TXT, "grid.color": GRID, "axes.grid": True,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 10, "lines.linewidth": 2,
                     "legend.frameon": False, "figure.dpi": 130})

files = sorted(glob.glob("results/sqd_ideal_4x3_U*.json"), key=lambda f: json.load(open(f))["U"])
fig, ax = plt.subplots(1, len(files) + 1, figsize=(4.6 * (len(files) + 1), 3.8))
for i, f in enumerate(files):
    d = json.load(open(f)); N = d["N"]
    a = ax[i]
    for key, lab, col, mk in [("topc", "top-|c| oracle", C[0], "o"), ("sqd", "SQD (ideal sampling of exact GS)", C[1], "s"),
                              ("hci", "classical HCI from single det", C[2], "^")]:
        rows = sorted(d[key], key=lambda r: r["K"])
        a.loglog([r["K"] for r in rows], [max(r["err"], 1e-6) / N for r in rows], mk + "-", color=col, label=lab, markersize=4)
    a.axhline(1e-3, color=TXT2, ls=":", lw=0.8); a.text(12, 1.3e-3, "1e-3 t per site", color=TXT2, fontsize=8)
    a.set(xlabel="subspace size K (determinants)", ylabel="energy error per site (t)",
          title=f"4×3 Hubbard, U/t={d['U']:g}, dim={d['dim']:,}")
    if i == 0: a.legend(fontsize=8, loc="upper right")
# shots vs distinct
a = ax[-1]
for i, f in enumerate(files):
    d = json.load(open(f))
    rows = sorted(d["sqd"], key=lambda r: r["M"])
    a.loglog([r["M"] for r in rows], [r["K"] for r in rows], "s-", color=C[i], label=f"U/t={d['U']:g}", markersize=4)
M = np.logspace(2, 6, 10); a.loglog(M, M, "--", color=TXT2, lw=1); a.text(2e2, 3e2, "K = M", color=TXT2, fontsize=8)
a.set(xlabel="shots M", ylabel="distinct determinants K", title="Shots needed per distinct determinant"); a.legend(fontsize=8)
fig.tight_layout(); fig.savefig("figs/fig5_sqd_ideal.png"); plt.close(fig)
print("ok")
