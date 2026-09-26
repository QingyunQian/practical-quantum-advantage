"""Compare finite-bath thermal ED with approximate vector-figure readouts.

The arXiv curves have no released numerical values in this repository.
Differences smaller than the plotted line thickness are not resolved.
"""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "results"
REFERENCE = json.loads((ROOT / "dmft_kanamori_fig2_digitized.json").read_text(encoding="utf-8"))
rows = []
for beta, nodes in ((16, 2), (16, 4), (32, 4), (64, 4)):
    name = f"dmft_semicircle_interacting_ed_beta{beta}_n{nodes}_levelminus1.json"
    ed = json.loads((ROOT / name).read_text(encoding="utf-8"))
    curve = next(row for row in REFERENCE["continuous_bath_inchworm"]["rows"]
                 if row["beta"] == beta)
    for variant, data in ed["variants"].items():
        values = [data[0]["G_00"][i] for i in (0, 5, 10, 15, 20)]
        reference = [point["G"] for point in curve["points"]]
        differences = [value - target for value, target in zip(values, reference)]
        rows.append({"beta": beta, "bath_nodes_per_spin": nodes,
                     "system_modes": 4 + 2 * nodes,
                     "hamiltonian_variant": variant,
                     "impurity_level": ed["impurity_level"],
                     "bath_fit_max_matsubara_input_error": ed["bath_input_fit_max_matsubara_abs_error"],
                     "figure_line_half_width_G": curve["plotted_line_half_width_G"],
                     "tau_over_beta": [point["tau_over_beta"] for point in curve["points"]],
                     "ed_G": values, "figure_G": reference,
                     "mean_absolute_plot_difference": sum(map(abs, differences)) / len(differences),
                     "maximum_absolute_plot_difference": max(map(abs, differences))})

output = {"scope": "finite-temperature interacting ED against approximate published plot coordinates; no quantum runtime or bath-convergence claim",
          "source": "https://arxiv.org/abs/1907.08570",
          "warning": "The impurity level -1 is inferred from a different panel, not specified by the paper. Figure line thickness is a visual ambiguity, not an error bar. All finite baths are below the 1e-3 input-fit threshold at beta=32 or 64.",
          "rows": rows}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path)
args = parser.parse_args()
content = json.dumps(output, indent=2) + "\n"
if args.output:
    args.output.write_text(content, encoding="utf-8")
else:
    print(content)
