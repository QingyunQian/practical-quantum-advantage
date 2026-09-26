# Practical Quantum Advantage

A living catalogue of quantum-computing application candidates, judged on three dimensions:

- **Classically hard**: is there a reduction, a cryptographic assumption, a lower bound, or only the observation that today's classical code is slow?
- **Quantumly easy**: does the quantum algorithm's precondition (initial-state overlap, adiabatic gap, decodable dual code) actually hold for the instances people care about?
- **Someone pays**: for a direct application, has a buyer stated a requirement in writing? For a foundational computational problem, what independent scientific or mathematical use does its output have?

Entries are organised in two layers, because industry and algorithm researchers use the word "application" differently. An **application** is a scenario: electrolyte design, OLED emitters, weather forecasting, derivative pricing. A **problem** is the computational task behind it: ground-state energy, PDE solving, Monte Carlo expectation. The [matrix](https://yuchenguommm.github.io/practical-quantum-advantage/matrix.html) links the two layers.

The overall verdict uses the layers differently. A direct application needs a documented buyer
requirement and a matched classical/quantum comparison to become `promising`. A foundational
problem such as integer factoring may be `promising` because its quantum polynomial-time
algorithm is proved, its output matters independently and the classical hardness assumption is
explicit. This does not claim an unconditional quantum–classical separation. The separate
`willingness_to_pay` field still records whether someone would buy the computation itself.

The site also keeps a record of every published "quantum advantage" claim and how long it took a classical method to reproduce it, and a board of open questions that anyone (or any agent) can take on.

Site: https://yuchenguommm.github.io/practical-quantum-advantage/
Machine-readable: `index.json` and `llms.txt` at the site root.
Review tasks: [`review-queue.html`](https://yuchenguommm.github.io/practical-quantum-advantage/review-queue.html) and [`review-queue.json`](https://yuchenguommm.github.io/practical-quantum-advantage/review-queue.json). A scheduled workflow keeps one GitHub issue up to date each month.

## Contributing

Start at the [contribution page](https://yuchenguommm.github.io/practical-quantum-advantage/contribute.html) to propose a new candidate, submit evidence, report a claim or suggest a research question. You can open an issue without writing code, or edit a page and open a pull request. The [contributor guide](CONTRIBUTING.md) explains review and page creation; [AGENTS.md](AGENTS.md) gives agents the schema and evidence rules.

```
pip install -r requirements.txt
python tools/new_entry.py application my-candidate --title "My candidate"
python tools/validate.py
python tools/build.py      # -> site/
```

## Provenance

Seeded in September 2026 by Yuchen Guo. Each entry lists its public references. Numerical experiments referenced by the pages, including scripts, raw results and figures, live under `numerics/`.

## License

Content: CC-BY-4.0. Code: MIT.
