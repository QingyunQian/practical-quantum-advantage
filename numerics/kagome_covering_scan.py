"""
Does the choice of dimer covering matter? Sample many random perfect matchings of the periodic
kagome cluster and compute |<dimer covering | GS(lam=1)>|^2 for each. Also report the energy
of each dimer state (a variational quality measure) and the best covering found.
"""
import sys, json, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import networkx as nx

Lx = int(sys.argv[1]); Ly = int(sys.argv[2]); nsamp = int(sys.argv[3]) if len(sys.argv) > 3 else 200
N = 3 * Lx * Ly
rng = np.random.default_rng(0)


def idx(r, s, sub):
    return 3 * ((r % Lx) * Ly + (s % Ly)) + sub


bonds = set()
for r in range(Lx):
    for s in range(Ly):
        A, B, C = idx(r, s, 0), idx(r, s, 1), idx(r, s, 2)
        for b in [(A, B), (A, C), (B, C), (B, idx(r + 1, s, 0)), (C, idx(r, s + 1, 0)), (B, idx(r + 1, s - 1, 2))]:
            bonds.add(tuple(sorted(b)))
bonds = sorted(bonds)
states = np.array([s for s in range(1 << N) if bin(s).count("1") == N // 2], dtype=np.int64)
dim = len(states)


def build(bond_list):
    rows, cols, vals = [], [], []
    diag = np.zeros(dim)
    for (i, j) in bond_list:
        bi = (states >> i) & 1; bj = (states >> j) & 1
        same = bi == bj
        diag += np.where(same, 0.25, -0.25)
        flip = np.where(~same)[0]
        new = states[flip] ^ ((1 << i) | (1 << j))
        rows.append(flip); cols.append(np.searchsorted(states, new)); vals.append(np.full(len(flip), 0.5))
    H = sp.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(dim, dim)).tocsr()
    return H + sp.diags(diag)


H = build(bonds)
w, v = spla.eigsh(H, k=2, which="SA", tol=1e-8)
gs = v[:, np.argmin(w)]
print(f"N={N} dim={dim} E0/N={w.min()/N:.5f} gap(Sz=0)={abs(w[1]-w[0]):.4f}", flush=True)

bits = np.array([[(s >> i) & 1 for i in range(N)] for s in states], dtype=np.int8)


def dimer_state(dimers):
    amp = np.ones(dim)
    for (i, j) in dimers:
        bi, bj = bits[:, i], bits[:, j]
        amp *= np.where(bi == bj, 0.0, np.where(bi == 1, 1.0, -1.0) / np.sqrt(2))
    return amp / np.linalg.norm(amp)


seen = {}
G = nx.Graph(); G.add_edges_from(bonds)
for k in range(nsamp):
    for (a, b) in G.edges:
        G[a][b]["weight"] = rng.random()
    M = nx.max_weight_matching(G, maxcardinality=True)
    key = tuple(sorted(tuple(sorted(e)) for e in M))
    if len(key) != N // 2 or key in seen:
        continue
    psi = dimer_state(key)
    seen[key] = dict(overlap=float((psi @ gs) ** 2), energy=float(psi @ (H @ psi)) / N)

ovs = np.array([x["overlap"] for x in seen.values()]); ens = np.array([x["energy"] for x in seen.values()])
print(f"distinct coverings sampled: {len(seen)}")
print(f"overlap^2: min={ovs.min():.2e} median={np.median(ovs):.2e} max={ovs.max():.2e}")
print(f"dimer-state energy/N: min={ens.min():.4f} median={np.median(ens):.4f}  (GS {w.min()/N:.4f})")
best = max(seen, key=lambda k: seen[k]["overlap"])
json.dump(dict(N=N, E0=float(w.min()), n_cov=len(seen), overlaps=ovs.tolist(), energies=ens.tolist(),
               best_cov=[list(b) for b in best], best_overlap=seen[best]["overlap"]),
          open(f"results/kagome_cov_{Lx}x{Ly}.json", "w"), indent=1)
