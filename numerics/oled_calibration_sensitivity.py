"""A small-cohort calibration sensitivity check for the Genin OLED data.

Source: arXiv:2512.13657v2, Tables SI.1-2 and SI.1-3. This is not an
external prospective validation or a like-for-like wall-time comparison.
"""

import argparse
import csv
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent / "results"
DFT = ROOT / "oled_genin2026_dft_si1.csv"
MAIN = ROOT / "oled_genin2026_si1.csv"
REPORTED_DFT_MAE = {
    "ro_b3lyp": 0.1974, "ro_cam_b3lyp": 0.1161,
    "ro_wpbeh": 0.1457, "ro_wb97x": 0.2194,
    "td_b3lyp": 0.1209, "td_cam_b3lyp": 0.2555,
}


def mean_absolute_error(prediction, target):
    return float(np.mean(np.abs(prediction - target)))


def fit_predict(train_x, train_y, test_x, calibration):
    if calibration == "offset":
        return test_x + float(np.mean(train_y - train_x))
    if calibration == "affine":
        design = np.column_stack((train_x, np.ones(len(train_x))))
        slope, intercept = np.linalg.lstsq(design, train_y, rcond=None)[0]
        return slope * test_x + intercept
    raise ValueError(calibration)


def evaluate(x, y, calibration):
    loo = np.empty(len(x))
    group = np.empty(len(x))
    for index in range(len(x)):
        training = np.arange(len(x)) != index
        loo[index] = fit_predict(x[training], y[training], x[index], calibration)
    # Q1-Q7 are Ir(III); Q8-Q14 are Pt(II), per Fig. 2 of the paper.
    for testing in (np.arange(len(x)) < 7, np.arange(len(x)) >= 7):
        group[testing] = fit_predict(x[~testing], y[~testing], x[testing], calibration)
    return {"leave_one_out_mae_ev": mean_absolute_error(loo, y),
            "leave_one_scaffold_family_out_mae_ev": mean_absolute_error(group, y),
            "ir_test_mae_ev": mean_absolute_error(group[:7], y[:7]),
            "pt_test_mae_ev": mean_absolute_error(group[7:], y[7:])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    with MAIN.open(newline="", encoding="utf-8") as source:
        main_rows = list(csv.DictReader(source))
    with DFT.open(newline="", encoding="utf-8") as source:
        dft_rows = list(csv.DictReader(source))
    if [r["material"] for r in main_rows] != [r["material"] for r in dft_rows]:
        raise ValueError("molecular rows do not match")
    y = np.array([float(r["experiment"]) for r in main_rows])
    rows = []
    for method in list(REPORTED_DFT_MAE) + ["ccsd", "cr_cc_2_3", "iqcc", "iqcc_pt"]:
        source = dft_rows if method in REPORTED_DFT_MAE else main_rows
        x = np.array([float(r[method]) for r in source])
        raw = mean_absolute_error(x, y)
        if method in REPORTED_DFT_MAE and abs(raw - REPORTED_DFT_MAE[method]) > .001:
            raise AssertionError(f"{method} transcription differs from paper's Table 2")
        rows.append({"method": method, "raw_mae_ev": raw,
                     "offset_calibration": evaluate(x, y, "offset"),
                     "affine_calibration": evaluate(x, y, "affine")})
    result = {"source": "https://arxiv.org/html/2512.13657",
              "source_tables": ["SI.1-2", "SI.1-3", "Table 2"],
              "n_molecules": 14, "groups": {"Ir(III)": "Q1-Q7", "Pt(II)": "Q8-Q14"},
              "calibration": "Within each training fold, offset fits mean(y-x); affine fits y=a*x+b by least squares. Every held-out prediction excludes its own measured target.",
              "limitations": [
                  "The 14 molecules are a small curated cohort, not a prospective test set.",
                  "The method set and calibration forms were inspected using this same publication; the apparent best result would be selection-biased.",
                  "Leaving out one molecule does not break structural similarity within its Ir/Pt family.",
                  "The two-family holdout trains on only seven molecules and is a stress test, not a future product-domain forecast.",
                  "Calculated gaps are rounded to 0.001 eV; calibration does not address physical-model errors or runtime.",
                  "All iQCC predictions in the paper were calculated on classical processors."
              ], "rows": rows}
    content = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content)


if __name__ == "__main__":
    main()
