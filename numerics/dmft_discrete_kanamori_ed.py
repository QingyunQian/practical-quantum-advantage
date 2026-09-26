"""Finite-temperature ED of the 12-mode discrete Kanamori check in arXiv:1907.08570.

This is an independent reconstruction from the printed Eq. (5) and the
discrete-bath paragraph. The paper's prose mentions pair hopping, but the
printed equation does not contain that operator. Run both variants explicitly.
No digitized paper data are used, so this is not yet a quantitative replication.
"""

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np


SITES_PER_SPIN = 6  # two impurity orbitals, four bath orbitals
MODE_COUNT = 12
U = 2.0
J = 0.2
BATH_LEVEL = 2.3
OFFDIAGONAL_RATIO = 0.5
IMPURITY_LEVEL = 0.0  # printed Eq. (5) has no explicit one-body impurity term


def mode(spin, site):
    return spin * SITES_PER_SPIN + site


def occupancy(state, index):
    return (state >> index) & 1


def fermion_op(state, index, creation):
    occupied = occupancy(state, index)
    if occupied == creation:
        return None
    sign = -1 if bin(state & ((1 << index) - 1)).count("1") % 2 else 1
    return state ^ (1 << index), sign


def apply_monomial(state, creators, annihilators):
    """Apply c†...c† c...c in the stated left-to-right order."""
    sign = 1
    for index in reversed(annihilators):
        step = fermion_op(state, index, False)
        if step is None:
            return None
        state, factor = step
        sign *= factor
    for index in reversed(creators):
        step = fermion_op(state, index, True)
        if step is None:
            return None
        state, factor = step
        sign *= factor
    return state, sign


def sector_states(n_up, n_down):
    def masks(count):
        return [sum(1 << i for i in indices)
                for indices in itertools.combinations(range(SITES_PER_SPIN), count)]

    return [up | (down << SITES_PER_SPIN)
            for up in masks(n_up) for down in masks(n_down)]


def terms(include_pair_hopping):
    """Return off-diagonal (coefficient, creators, annihilators) terms."""
    result = []
    for spin in (0, 1):
        # At each energy +/-2.3, symmetric and antisymmetric channels give
        # Delta_ij = [[1, r], [r, 1]] * sum_{e=+/-2.3} 1/(z-e).
        for energy_position in (0, 1):
            for channel in (0, 1):
                bath_site = 2 + 2 * energy_position + channel
                strength = math.sqrt(1 + (OFFDIAGONAL_RATIO if channel == 0 else -OFFDIAGONAL_RATIO)) / math.sqrt(2)
                for orbital in (0, 1):
                    coupling = strength * (1 if channel == 0 or orbital == 0 else -1)
                    impurity = mode(spin, orbital)
                    bath = mode(spin, bath_site)
                    result.append((coupling, (impurity,), (bath,)))
                    result.append((coupling, (bath,), (impurity,)))

    # The i!=j sum and explicit h.c. in the printed Eq. (5) include each
    # spin-exchange operator twice. Keep that literal coefficient here.
    for i, j in ((0, 1), (1, 0)):
        result.append((2 * J, (mode(0, i), mode(1, j)),
                       (mode(1, i), mode(0, j))))
        if include_pair_hopping:
            result.append((J, (mode(0, i), mode(1, i)),
                           (mode(1, j), mode(0, j))))
    return result


def diagonal_energy(state):
    n = lambda spin, orbital: occupancy(state, mode(spin, orbital))
    energy = IMPURITY_LEVEL * sum(n(spin, orbital)
                                  for spin in (0, 1) for orbital in (0, 1))
    energy += U * (n(0, 0) * n(1, 0) + n(0, 1) * n(1, 1))
    energy += (U - 2 * J) * (n(1, 0) * n(0, 1) + n(1, 1) * n(0, 0))
    energy += (U - 3 * J) * (n(0, 0) * n(0, 1) + n(1, 0) * n(1, 1))
    for spin in (0, 1):
        for site in (2, 3):
            energy -= BATH_LEVEL * occupancy(state, mode(spin, site))
        for site in (4, 5):
            energy += BATH_LEVEL * occupancy(state, mode(spin, site))
    return energy


def diagonalize_all(include_pair_hopping):
    hopping = terms(include_pair_hopping)
    blocks = {}
    for n_up in range(SITES_PER_SPIN + 1):
        for n_down in range(SITES_PER_SPIN + 1):
            states = sector_states(n_up, n_down)
            position = {state: index for index, state in enumerate(states)}
            h = np.diag([diagonal_energy(s) for s in states])
            for column, state in enumerate(states):
                for coefficient, creators, annihilators in hopping:
                    applied = apply_monomial(state, creators, annihilators)
                    if applied is not None:
                        end, sign = applied
                        h[position[end], column] += coefficient * sign
            if not np.allclose(h, h.T, atol=1e-12):
                raise AssertionError(f"non-Hermitian sector {(n_up, n_down)}")
            values, vectors = np.linalg.eigh(h)
            blocks[(n_up, n_down)] = (states, values, vectors)
    return blocks


def green_function(blocks, beta, orbital=0, spin=0, points=21):
    minimum = min(float(values[0]) for _, values, _ in blocks.values())
    tau_fractions = np.linspace(0, 1, points)
    partition = sum(float(np.sum(np.exp(-beta * (values - minimum))))
                    for _, values, _ in blocks.values())
    green = np.zeros(points)
    for n_up in range(SITES_PER_SPIN + (spin != 0)):
        for n_down in range(SITES_PER_SPIN + (spin != 1)):
            sector_a = (n_up, n_down)
            sector_b = (n_up + (spin == 0), n_down + (spin == 1))
            states_a, energy_a, vec_a = blocks[sector_a]
            states_b, energy_b, vec_b = blocks[sector_b]
            where_b = {state: index for index, state in enumerate(states_b)}
            d_dag = np.zeros((len(states_b), len(states_a)))
            for column, state in enumerate(states_a):
                applied = fermion_op(state, mode(spin, orbital), True)
                if applied is not None:
                    final_state, sign = applied
                    d_dag[where_b[final_state], column] = sign
            transition = vec_b.T @ d_dag @ vec_a
            strength = transition ** 2
            for k, fraction in enumerate(tau_fractions):
                tau = beta * fraction
                wa = np.exp(-(beta - tau) * (energy_a - minimum))
                wb = np.exp(-tau * (energy_b - minimum))
                green[k] -= float(wb @ strength @ wa) / partition
    if abs(green[0] + green[-1] + 1) > 1e-10:
        raise AssertionError("fermionic equal-time sum rule failed")
    return {"beta": beta, "tau_over_beta": tau_fractions.tolist(),
            "G_00": green.tolist(), "impurity_occupation": float(-green[-1]),
            "ground_energy": minimum}


def noninteracting_self_check():
    """Compare the Lehmann implementation to a six-by-six one-body solution."""
    global U, J
    old_u, old_j = U, J
    try:
        U, J = 0.0, 0.0
        blocks = diagonalize_all(False)
        h_one = np.diag([IMPURITY_LEVEL, IMPURITY_LEVEL, -BATH_LEVEL, -BATH_LEVEL,
                         BATH_LEVEL, BATH_LEVEL])
        for coefficient, creators, annihilators in terms(False):
            if len(creators) == 1 and creators[0] < SITES_PER_SPIN:
                h_one[creators[0], annihilators[0]] += coefficient
        energies, vectors = np.linalg.eigh(h_one)
        weights = vectors[0, :] ** 2
        beta = 64.0
        many_body = green_function(blocks, beta)
        one_body = []
        for fraction in many_body["tau_over_beta"]:
            tau = beta * fraction
            terms_at_tau = []
            for energy, weight in zip(energies, weights):
                if energy >= 0:
                    kernel = math.exp(-tau * energy) / (1 + math.exp(-beta * energy))
                else:
                    kernel = math.exp(-(beta - tau) * (-energy)) / (1 + math.exp(-beta * (-energy)))
                terms_at_tau.append(weight * kernel)
            one_body.append(-sum(terms_at_tau))
        discrepancy = max(abs(a - b) for a, b in zip(many_body["G_00"], one_body))
        if discrepancy > 1e-10:
            raise AssertionError(f"noninteracting Lehmann check failed: {discrepancy}")
        return discrepancy
    finally:
        U, J = old_u, old_j


def main():
    global IMPURITY_LEVEL
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--impurity-level", type=float, default=0.0)
    args = parser.parse_args()
    IMPURITY_LEVEL = args.impurity_level
    output = {"source": "https://arxiv.org/abs/1907.08570",
              "model": "two spinful impurity orbitals, discrete +/-2.3 bath, r=0.5, t=1, U=2, J=0.2",
              "bath_construction": "two symmetric/antisymmetric channels at each +/-2.3 energy and per spin; unit spectral weight per energy in each orbital diagonal",
              "impurity_level": IMPURITY_LEVEL,
              "scope": "independent finite-temperature exact diagonalization; source Hamiltonian ambiguity is not resolved. Level -1 is a sensitivity check inferred from plotted endpoints, not a documented paper parameter. The added pair-hopping variant is illustrative, not a claim about the authors' implementation.",
              "numpy_version": np.__version__,
              "noninteracting_self_check_max_abs_error": noninteracting_self_check(),
              "variants": {}, "low_energy_spectrum": {}}
    for name, include_pair_hopping in (("printed_eq5", False), ("printed_eq5_plus_pair_hopping", True)):
        blocks = diagonalize_all(include_pair_hopping)
        ordered_energies = sorted(float(energy) for _, values, _ in blocks.values()
                                  for energy in values)
        multiplicity = sum(abs(energy - ordered_energies[0]) < 1e-10
                           for energy in ordered_energies)
        output["low_energy_spectrum"][name] = {
            "ground_state_degeneracy": multiplicity,
            "gap_above_ground_manifold": ordered_energies[multiplicity] - ordered_energies[0],
        }
        output["variants"][name] = [green_function(blocks, beta) for beta in (8, 16, 32, 64)]
    content = json.dumps(output, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content)


if __name__ == "__main__":
    main()
