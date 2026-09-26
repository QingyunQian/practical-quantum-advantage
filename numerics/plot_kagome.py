"""Figure: quantum-easiness certificate for the kagome AFM instance (dimer -> uniform path)."""
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

paths = {json.load(open(f))["N"]: json.load(open(f)) for f in glob.glob("results/kagome_[0-9]x[0-9].json")}
covs = {json.load(open(f))["N"]: json.load(open(f)) for f in glob.glob("results/kagome_cov_*.json")}

fig, ax = plt.subplots(1, 3, figsize=(13, 3.8))
for i, N in enumerate(sorted(paths)):
    d = paths[N]; lam = [r["lam"] for r in d["rows"]]
    ax[0].plot(lam, [r["gap"] for r in d["rows"]], "o-", color=C[i], label=f"N={N}", markersize=4)
    ax[1].semilogy(lam, [max(r["overlap"], 1e-6) for r in d["rows"]], "o-", color=C[i], label=f"N={N}", markersize=4)
ax[0].set(xlabel="path parameter λ  (0 = dimerized, 1 = uniform kagome)", ylabel="gap E1−E0 in Sz=0 sector (J)",
          title="Gap along dimer→uniform path")
ax[1].set(xlabel="path parameter λ", ylabel="|<dimer|GS(λ)>|²", title="Guiding-state overlap (one fixed covering; floor 1e-6)")
ax[0].legend(); ax[1].legend()

Ns = sorted(covs); best = [covs[N]["best_overlap"] for N in Ns]; med = [float(np.median(covs[N]["overlaps"])) for N in Ns]
ax[2].semilogy(Ns, best, "o-", color=C[0], label="best covering")
ax[2].semilogy(Ns, med, "s-", color=C[1], label="median covering")
if len(Ns) >= 2:
    a, b = np.polyfit(Ns, np.log(best), 1)
    NN = np.array([Ns[0], 100])
    ax[2].semilogy(NN, np.exp(b + a * NN), "--", color=C[0], lw=1)
    ax[2].text(0.97, 0.9, f"best ~ exp({a:.3f} N)  →  N=100: {np.exp(b + a*100):.1e}", transform=ax[2].transAxes,
               ha="right", fontsize=9, color=C[0])
ax[2].set(xlabel="N (sites = qubits)", ylabel="|<dimer|GS>|² at λ=1", title="Overlap decay with size", xlim=(10, 102))
ax[2].legend(loc="lower left")
fig.tight_layout(); fig.savefig("figs/fig4_kagome_certificate.png"); plt.close(fig)
print({N: dict(min_gap=paths[N]["min_gap"], final_overlap=paths[N]["final_overlap"]) for N in paths})
print({N: dict(best=covs[N]["best_overlap"], n_cov=covs[N]["n_cov"]) for N in covs})
