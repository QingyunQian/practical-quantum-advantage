# Practical Quantum Advantage

A living catalogue of quantum-computing application candidates, judged on three dimensions:

- **Classically hard**: is there a reduction, a cryptographic assumption, a lower bound, or only the observation that today's classical code is slow?
- **Quantumly easy**: does the quantum algorithm's precondition (initial-state overlap, adiabatic gap, decodable dual code) actually hold for the instances people care about?
- **Someone pays**: has a buyer said, in writing, that the extra accuracy or speed is worth money?

Entries are organised in two layers, because industry and algorithm researchers use the word "application" differently. An **application** is a scenario: electrolyte design, OLED emitters, weather forecasting, derivative pricing. A **problem** is the computational task behind it: ground-state energy, PDE solving, Monte Carlo expectation. The [matrix](https://yuchenguommm.github.io/practical-quantum-advantage/matrix.html) links the two layers.

The site also keeps a record of every published "quantum advantage" claim and how long it took a classical method to reproduce it, and a board of open questions that anyone (or any agent) can take on.

Site: https://yuchenguommm.github.io/practical-quantum-advantage/
Machine-readable: `index.json` and `llms.txt` at the site root.

## Contributing

Every page is a Markdown file under `content/`. Edit it and open a pull request. Agents are welcome; see [AGENTS.md](AGENTS.md) for the page format, the evidence rules, and the Claude Code skills shipped with the repo.

```
pip install -r requirements.txt
python tools/validate.py
python tools/build.py      # -> site/
```

## Provenance

Seeded in September 2026 by Yuchen Guo. Each entry lists its public references. Numerical experiments referenced by the pages, including scripts, raw results and figures, live under `numerics/`.

## License

Content: CC-BY-4.0. Code: MIT.
