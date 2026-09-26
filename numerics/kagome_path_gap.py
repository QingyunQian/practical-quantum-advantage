"""
Quantum-easiness certificate for a frustrated-magnet ground-state instance.

Kagome Heisenberg antiferromagnet on periodic Lx x Ly unit-cell clusters (N = 3 Lx Ly spins).
Adiabatic path from a dimerized (valence-bond) Hamiltonian to the uniform model:
    H(lam) = sum_{dimer bonds} S_i.S_j + lam * sum_{other bonds} S_i.S_j ,  lam: 0 -> 1
At lam=0 the ground state is a unique product of singlets (gap = 1). We compute, by exact
diagonalization in the Sz=0 sector:
    E0(lam), gap(lam) = E1 - E0 (same Sz sector), and the overlap |<dimer|GS(lam)>|^2.
Outputs the minimum gap along the path and the final overlap vs N: the two numbers that decide
whether adiabatic/guided-QPE preparation is cheap.
"""
import sys, json, time, itertools
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

Lx = int(sys.argv[1]) if len(sys.argv) > 1 else 2
Ly = int(sys.argv[2]) if len(sys.argv) > 2 else 2
nlam = int(sys.argv[3]) if len(sys.argv) > 3 else 11
N = 3 * Lx * Ly


def idx(r, s, sub):
    return 3 * ((r % Lx) * Ly + (s % Ly)) + sub   # sub: 0=A, 1=B, 2=C


bonds = set()
for r in range(Lx):
    for s in range(Ly):
        A, B, C = idx(r, s, 0), idx(r, s, 1), idx(r, s, 2)
        # up triangle
        for b in [(A, B), (A, C), (B, C)]:
            bonds.add(tuple(sorted(b)))
        # down triangle
        for b in [(B, idx(r + 1, s, 0)), (C, idx(r, s + 1, 0)), (B, idx(r + 1, s - 1, 2))]:
            bonds.add(tuple(sorted(b)))
bonds = sorted(bonds)
assert len(bonds) == 2 * N, (len(bonds), 2 * N)

# a perfect matching (dimer covering) via networkx
import networkx as nx
G = nx.Graph(); G.add_edges_from(bonds)
M = nx.max_weight_matching(G, maxcardinality=True)
dimers = sorted(tuple(sorted(e)) for e in M)
assert len(dimers) == N // 2, "no perfect matching"
others = [b for b in bonds if b not in set(dimers)]

# Sz = 0 basis
states = np.array([s for s in range(1 << N) if bin(s).count("1") == N // 2], dtype=np.int64)
dim = len(states)
print(f"N={N}, bonds={len(bonds)}, dimers={len(dimers)}, dim(Sz=0)={dim}", flush=True)


def build(bond_list):
    """sparse Heisenberg sum over bonds, in the Sz=0 basis."""
    rows, cols, vals = [], [], []
    diag = np.zeros(dim)
    for (i, j) in bond_list:
        bi = (states >> i) & 1; bj = (states >> j) & 1
        same = bi == bj
        diag += np.where(same, 0.25, -0.25)
        flip = np.where(~same)[0]
        new = states[flip] ^ ((1 << i) | (1 << j))
        pos = np.searchsorted(states, new)
        rows.append(flip); cols.append(pos); vals.append(np.full(len(flip), 0.5))
    rows = np.concatenate(rows); cols = np.concatenate(cols); vals = np.concatenate(vals)
    H = sp.coo_matrix((vals, (rows, cols)), shape=(dim, dim)).tocsr()
    H = H + sp.diags(diag)
    return H


t0 = time.time()
Hd = build(dimers); Ho = build(others)
print(f"built in {time.time()-t0:.1f}s", flush=True)

# dimer product state (singlet on every dimer) in the Sz=0 basis
psi_d = np.zeros(dim)
for s_idx, s in enumerate(states):
    amp = 1.0
    for (i, j) in dimers:
        bi = (s >> i) & 1; bj = (s >> j) & 1
        if bi == bj:
            amp = 0.0; break
        amp *= (1 if bi == 1 else -1) / np.sqrt(2)   # (|up dn> - |dn up>)/sqrt2 with bit 1 = up
    psi_d[s_idx] = amp
psi_d /= np.linalg.norm(psi_d)
assert abs(psi_d @ (Hd @ psi_d) - (-0.75 * len(dimers))) < 1e-8

rows = []
rng = np.random.default_rng(1)
v0 = psi_d.copy()
for lam in np.linspace(0, 1, nlam):
    H = Hd + lam * Ho
    t1 = time.time()
    v0r = v0 + 0.3 * rng.standard_normal(dim); v0r /= np.linalg.norm(v0r)
    w, v = spla.eigsh(H, k=3, which="SA", v0=v0r, tol=1e-8, ncv=40)
    order = np.argsort(w); w = w[order]; v = v[:, order]
    gs = v[:, 0]; v0 = gs
    ov = float((psi_d @ gs) ** 2)
    rows.append(dict(lam=float(lam), E0=float(w[0]), gap=float(w[1] - w[0]), gap2=float(w[2] - w[0]), overlap=ov,
                     e_per_site=float(w[0] / N)))
    print(f"lam={lam:4.2f}  E0/N={w[0]/N:+.5f}  gap={w[1]-w[0]:.4f}  gap2={w[2]-w[0]:.4f}  |<dimer|GS>|^2={ov:.4f}  ({time.time()-t1:.0f}s)", flush=True)

out = dict(Lx=Lx, Ly=Ly, N=N, dim=dim, dimers=dimers, rows=rows,
           min_gap=min(r["gap"] for r in rows), final_overlap=rows[-1]["overlap"])
json.dump(out, open(f"results/kagome_{Lx}x{Ly}.json", "w"), indent=1)
print("min gap along path:", out["min_gap"], " final overlap:", out["final_overlap"])
