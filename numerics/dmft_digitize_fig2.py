"""Read the exact-discrete-band curve endpoints from the author's vector Fig. 2.

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


def digitize():
    response = requests.get(SOURCE_URL, timeout=45)
    response.raise_for_status()
    with tarfile.open(fileobj=BytesIO(response.content), mode="r:gz") as archive:
        figure = archive.extractfile("kanamori_gf.pdf").read()
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
    return {"source": SOURCE_URL, "figure": "kanamori_gf.pdf, dashed ED curves in the left panels",
            "extraction": "vector path coordinates calibrated to each panel's 0 and -1 y-axis ticks",
            "warning": "Plot-derived approximate values; no underlying numeric dataset or error bars. A midpoint is omitted when no vector-path point lies within 0.02 of tau/beta=0.5.",
            "rows": rows}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = json.dumps(digitize(), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content)
