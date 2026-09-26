"""Read selected curve points from the author's vector Fig. 2.

Requires requests and PyMuPDF. Downloads arXiv:1907.08570v2 source at runtime;
does not redistribute the figure. Curve coordinates are approximate because
they were read from the plotted path, not from the authors' raw numerical data.
"""

import argparse
from io import BytesIO
import json
from pathlib import Path
import tarfile

import fitz
import requests


SOURCE_URL = "https://export.arxiv.org/src/1907.08570v2"


def digitize(figure_path=None):
    if figure_path is None:
        response = requests.get(SOURCE_URL, timeout=45)
        response.raise_for_status()
        with tarfile.open(fileobj=BytesIO(response.content), mode="r:gz") as archive:
            figure = archive.extractfile("kanamori_gf.pdf").read()
    else:
        figure = Path(figure_path).read_bytes()
    page = fitz.open(stream=figure, filetype="pdf")[0]
    drawings = page.get_drawings()
    exact = sorted(
        (d for d in drawings if d["color"] == (0.0, 0.0, 0.0)
         and d["dashes"] != "[] 0" and len(d["items"]) > 20),
        key=lambda d: d["rect"].y0,
    )
    if len(exact) != 4:
        raise ValueError(f"expected four dashed ED curves, found {len(exact)}")
    x0, x1 = exact[0]["rect"].x0, exact[0]["rect"].x1
    axes = sorted({round(d["rect"].y0, 5) for d in drawings
                   if d["color"] == (0.0, 0.0, 0.0)
                   and d["width"] is not None and d["width"] < 0.6
                   and d["rect"].width > 70 and d["rect"].height < 0.1
                   and abs(d["rect"].x0 - x0) < 0.01})
    if len(axes) != 5:
        raise ValueError(f"expected five horizontal panel edges, found {len(axes)}")
    green = sorted((d for d in drawings if d["color"] is not None
                    and d["color"][1] > 0.5
                    and d["color"][1] > 1.3 * d["color"][0]
                    and d["color"][1] > 1.3 * d["color"][2]
                    and len(d["items"]) > 20
                    and d["rect"].x0 > x1), key=lambda d: d["rect"].y0)
    if len(green) != 4:
        raise ValueError(f"expected four green continuous-bath curves, found {len(green)}")
    right_x0, right_x1 = green[0]["rect"].x0, green[0]["rect"].x1
    right_ticks = sorted({round(d["rect"].y0, 5) for d in drawings
                          if d["color"] == (0.0, 0.0, 0.0)
                          and d["rect"].height < 0.1
                          and 3 < d["rect"].width < 5
                          and abs(d["rect"].x1 - right_x1) < 0.01})
    if len(right_ticks) != 8:
        raise ValueError(f"expected two right-panel ticks per row, found {len(right_ticks)}: {right_ticks}")
    rows = []
    for index, drawing in enumerate(exact):
        points = []
        for item in drawing["items"]:
            points.extend(value for value in item[1:] if isinstance(value, fitz.Point))

        def value_at(fraction):
            wanted_x = x0 + fraction * (x1 - x0)
            nearest = min(points, key=lambda point: abs(point.x - wanted_x))
            return {"G": -(nearest.y - axes[index]) / (axes[index + 1] - axes[index]),
                    "tau_fraction_error": abs(nearest.x - wanted_x) / (x1 - x0)}

        midpoint = value_at(0.5)
        rows.append({"beta": [8, 16, 32, 64][index],
                     "G_tau_0": value_at(0),
                     "G_tau_half": midpoint if midpoint["tau_fraction_error"] < 0.02 else None,
                     "G_tau_beta": value_at(1)})
    continuous = []
    for index, drawing in enumerate(green):
        points = []
        for item in drawing["items"]:
            points.extend(value for value in item[1:] if isinstance(value, fitz.Point))
        y_zero = right_ticks[2 * index]
        y_minus_one = right_ticks[2 * index + 1]
        values = []
        for fraction in (0, 0.25, 0.5, 0.75, 1):
            wanted_x = right_x0 + fraction * (right_x1 - right_x0)
            nearest = min(points, key=lambda point: abs(point.x - wanted_x))
            values.append({"tau_over_beta": fraction,
                           "G": -(nearest.y - y_zero) / (y_minus_one - y_zero),
                           "tau_fraction_error": abs(nearest.x - wanted_x) / (right_x1 - right_x0)})
        continuous.append({"beta": [8, 16, 32, 64][index], "points": values,
                           "plotted_line_half_width_G": drawing["width"] / (2 * (y_minus_one - y_zero))})
    return {"source": SOURCE_URL, "figure": "kanamori_gf.pdf, dashed ED in left panels and green Inchworm in right panels",
            "extraction": "vector path coordinates calibrated to each panel's 0 and -1 y-axis ticks",
            "warning": "Plot-derived approximate values; no underlying numeric dataset or error bars. A midpoint is omitted when no vector-path point lies within 0.02 of tau/beta=0.5.",
            "rows": rows,
            "continuous_bath_inchworm": {"figure": "green curves in the right panels",
                                          "calibration": "right-panel 0 and -1 y-axis ticks; nearest vector-path vertex",
                                          "warning": "Approximate plotted curves, without author raw data or error bars; line half-width in G units and nearest-vertex x-offset are reported. Line width is a visualization ambiguity, not a statistical confidence interval.",
                                          "rows": continuous}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--figure", type=Path, help="locally cached original kanamori_gf.pdf")
    args = parser.parse_args()
    content = json.dumps(digitize(args.figure), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content)
