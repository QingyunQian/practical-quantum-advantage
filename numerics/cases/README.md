# Contribute a reproducible case

A case records evidence for a **fixed instance**. It is separate from a catalogue page's review status and verdict. Positive, negative and inconclusive results can all be useful. The [nine-option automotive example](automotive_pricing/README.md) is the current template; it is a negative classical-baseline case.

Create `numerics/cases/<short-folder>/` and include:

- `case.json` with a unique ID, public title and summary, related application and problem IDs, a plain-language finding, review status, check date, and names of the four files below.
- A versioned input with its original public source and hash. If input data cannot be shared, state the exact missing fields and keep the case in an issue rather than presenting it as complete.
- A protocol (`README.md`) fixing the observable or objective, accuracy, success criterion, classical baseline, quantum route, assumptions and limitations.
- Executable code and machine-readable results. Record library versions and random seeds where relevant. Distinguish executed measurements from formulas and estimates.

Add a link from the relevant catalogue page. Run `python tools/validate.py`, `python tools/build.py` and `python tools/check_site.py`. The build automatically adds a valid `case.json` to `cases.html` and `cases.json`. A full case is still `seed` until its source and claim checks receive independent review; mark it `reviewed` only under the [contributor review rule](../../CONTRIBUTING.md).
