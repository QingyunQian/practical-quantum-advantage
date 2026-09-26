"""
Ideal-limit test of sample-based quantum diagonalization (SQD/QSCI) on a strongly correlated model.

Model: 2D Hubbard Lx x Ly (open BC), half filling, Sz=0. Exact ground state by Lanczos.
Compare, as a function of subspace size K (number of determinants):
  (a) SQD-ideal : sample M shots from |c_i|^2 of the EXACT ground state (best case: no noise,
                  perfect state), subspace = distinct sampled determinants, diagonalize H in it.
  (b) top-|c|   : oracle selection of the K largest-|c| determinants (the best any weight-based
                  selection can do).
  (c) HCI-like  : classical heat-bath selected CI starting from the HF determinant, thresholds eps.
Outputs energy error vs K for each, and for (a) the number of shots needed to reach K distinct dets.
"""
import sys, json, time, itertools
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

Lx = int(sys.argv[1]) if len(sys.argv) > 1 else 4
Ly = int(sys.argv[2]) if len(sys.argv) > 2 else 3
U = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
t = 1.0
N = Lx * Ly; nup = ndn = N // 2
rng = np.random.default_rng(0)

bonds = []
for x in range(Lx):
    for y in range(Ly):
        i = x * Ly + y
        if y + 1 < Ly: bonds.append((i, i + 1))
        if x + 1 < Lx: bonds.append((i, i + Ly))

# spin-sector basis (bit strings with nup ones)
sec = np.array([s for s in range(1 << N) if bin(s).count("1") == nup], dtype=np.int64)
ns = len(sec); pos = {int(s): k for k, s in enumerate(sec)}
dim = ns * ns
print(f"N={N} U/t={U} sector={ns} dim={dim}", flush=True)


def hop_matrix():
    """single-spin hopping matrix T (ns x ns) with fermionic signs."""
    rows, cols, vals = [], [], []
    for k, s in enumerate(sec):
        for (i, j) in bonds:
            for a, b in ((i, j), (j, i)):
                if (s >> a) & 1 and not (s >> b) & 1:
                    s2 = s ^ (1 << a) ^ (1 << b)
                    lo, hi = min(a, b), max(a, b)
                    nbetween = bin(s & (((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1))).count("1")
                    rows.append(k); cols.append(pos[int(s2)]); vals.append(-t * (-1) ** nbetween)
    return sp.csr_matrix((vals, (rows, cols)), shape=(ns, ns))


T = hop_matrix()
I = sp.identity(ns, format="csr")
# double occupancy: n_up(i) n_dn(i) summed -> diag over (up, dn) pairs
bits = np.array([[(s >> i) & 1 for i in range(N)] for s in sec], dtype=np.float64)
Udiag = U * (bits @ bits.T)          # ns x ns matrix: number of doubly occupied sites for (up, dn)
H = sp.kron(T, I) + sp.kron(I, T) + sp.diags(Udiag.reshape(-1))
H = H.tocsr()
t0 = time.time()
w, v = spla.eigsh(H, k=1, which="SA", tol=1e-9)
E0 = float(w[0]); c = v[:, 0]; c /= np.linalg.norm(c)
print(f"E0={E0:.6f} (E0/N={E0/N:.5f})  in {time.time()-t0:.1f}s", flush=True)
p = c ** 2
order = np.argsort(-p)
print(f"weight of top 1/10/100/1000 dets: {p[order[0]]:.3e} {p[order[:10]].sum():.3f} {p[order[:100]].sum():.3f} {p[order[:1000]].sum():.3f}")


def subspace_energy(idx):
    idx = np.unique(idx)
    Hs = H[idx][:, idx]
    if len(idx) < 1500:
        return float(np.linalg.eigvalsh(Hs.toarray())[0]), len(idx)
    ws = spla.eigsh(Hs, k=1, which="SA", tol=1e-9, ncv=40)[0]
    return float(ws[0]), len(idx)


results = dict(N=N, U=U, E0=E0, dim=dim, topc=[], sqd=[], hci=[])

# (b) top-|c| oracle
for K in [10, 30, 100, 300, 1000, 3000, 10000, 30000]:
    if K > dim: break
    E, k = subspace_energy(order[:K])
    results["topc"].append(dict(K=k, err=E - E0))
    print(f"top-|c|  K={k:6d}  err={E-E0:.4e}", flush=True)

# (a) SQD-ideal: shots M
for M in [100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000]:
    shots = rng.choice(dim, size=M, p=p)
    E, k = subspace_energy(shots)
    results["sqd"].append(dict(M=M, K=k, err=E - E0))
    print(f"SQD      M={M:8d} shots -> K={k:6d} distinct  err={E-E0:.4e}", flush=True)

# (c) HCI-like selected CI from the HF-like determinant (Neel-ish product: choose lowest-U det = most probable? no:
#     use the classical starting point: the single determinant with lowest diagonal energy)
diag = H.diagonal()
start = int(np.argmin(diag))
Hcoo = H.tocoo()
for eps in [1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002]:
    V = {start}
    for it in range(30):
        idx = np.array(sorted(V))
        Hs = H[idx][:, idx]
        if len(idx) < 1500:
            ws, vs = np.linalg.eigh(Hs.toarray()); cv = vs[:, 0]
        else:
            ws, vs = spla.eigsh(Hs, k=1, which="SA", tol=1e-9, ncv=40); cv = vs[:, 0]
        # heat-bath criterion: add j if max_i |H_ji c_i| > eps
        sub = H[:, idx].tocsc()
        contrib = sub.multiply(np.abs(cv)[None, :])        # |H_ji| |c_i|
        contrib.data = np.abs(contrib.data)
        mx = contrib.max(axis=1).toarray().ravel()
        new = set(np.where(mx > eps)[0].tolist()) - V
        if not new or len(V) > 60000:
            break
        V |= new
    E, k = subspace_energy(np.array(sorted(V)))
    results["hci"].append(dict(eps=eps, K=k, err=E - E0))
    print(f"HCI      eps={eps:6.3f} -> K={k:6d}  err={E-E0:.4e}", flush=True)

json.dump(results, open(f"results/sqd_ideal_{Lx}x{Ly}_U{U:g}.json", "w"), indent=1)
