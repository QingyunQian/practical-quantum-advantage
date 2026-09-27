# Publication audit, 27 September 2026

The website is already public. This audit distinguishes what is ready for an open beta from what should be checked before a broad announcement. Counts are from the current repository, not estimates.

## Current inventory

| Layer | Count | Meaning |
| --- | ---: | --- |
| Assessed catalogue pages | 65 | 14 applications, 17 computational problems, 10 methods, 8 claims, 16 open questions |
| Reviewed pages | 9 | A prior source/claim check is recorded; the rest are `seed` |
| Seed pages | 56 | Public drafts awaiting complete source and claim review |
| Unassessed ideas | 48 | Leads without a verdict or evidence grade |
| Reproducible cases | 1 | A negative fixed-input automotive-pricing case; its independent review is still pending |
| Open GitHub issues at audit | 6 | Review queue and selected research invitations |

The only `promising` verdict is on integer factoring as a foundational computational problem. The site does not currently demonstrate an industrial quantum advantage at 50–100 logical qubits. That is a research finding, and the homepage must not imply otherwise.

## What the Quantum Advantage Tracker does well

The [Quantum Advantage Tracker](https://quantum-advantage-tracker.github.io/) groups submissions under fixed circuit or Hamiltonian **instances**, displays subsequent quantum and classical results together, and distinguishes active, superseded and baseline benchmarks. Its [participation instructions](https://quantum-advantage-tracker.github.io/participate) specify the instance file, method, runtime, hardware and public GitHub review path. That structure makes a classical counter-result easy to discover next to the original claim.

Our scope is broader: an application such as OLED design links to a computational problem such as ground-state energy. We retain those two layers and add a separate [case index](https://yuchenguommm.github.io/practical-quantum-advantage/cases.html) for fixed inputs. Tracker categories apply to individual benchmark instances; they should not be copied onto broad application pages. Our `seed/reviewed/disputed` labels describe **review state**, while `surviving/uneconomic/no-go/promising` describe a **scientific assessment**. A case is an evidence artifact, not a third status scale.

The tracker also exposed a relevant content update: its [P9 peaked-circuit CPU submission and review](https://github.com/quantum-advantage-tracker/quantum-advantage-tracker.github.io/issues/153) reports a 734-second correct-peak run on an M5 Pro. The discussion records an independent cutoff-sensitive stall. The [BlueQubit claim page](../content/claims/bluequbit-peaked-circuits-2025.md) now states both facts and keeps the original A100 and H2 submissions distinct.

## Changes made in this audit

- Replaced the duplicated full README on the homepage with a concise application-to-problem map, evidence questions, a prominent negative case, and explicit review-status counts.
- Reworked navigation, typography, cards, tables and mobile layout. The design uses original CSS and a simple local SVG icon; it does not import the reference site's code or analytics.
- Added `cases.html`, `cases.json`, a per-case manifest and a contributor format, so later fixed-input comparisons have a stable home and search entry.
- Added per-entry descriptions and an on-page section list for long entries.
- Strengthened the site check to catch broken local fragments, duplicate IDs and images without alt text. Markdown output is sanitized before publication to prevent active HTML or unsafe link protocols from contributor text.
- Kept the community path through issues and pull requests; the public JSON feeds remain read-only.

## Ready now

- Static source and build are public; GitHub Actions checks page schema, references, unit tests, build and local links before deploying `main`.
- The application/problem distinction, review queue, idea pool and contribution instructions are visible.
- The first case has pinned public input, executable code, a classical certificate, compiled quantum route and machine-readable output. It gives a negative conclusion without claiming a hardware run.

## Before a broad announcement

1. **Review the most visible scientific pages.** Fifty-six of sixty-five pages remain `seed`. Prioritize the homepage-linked OLED, weather/PDE, derivative/Monte Carlo and automotive pages, plus any claim cited in an announcement. Record checked passages, strongest competing classical results and unresolved assumptions. Do not turn `seed` into `reviewed` merely because a date or reference exists.
2. **Independently rerun the case.** The automotive result was produced by the project code. A second clean environment should confirm the input hash, exact optimum, source encoder output and circuit checks. The full five-iteration circuit was compiled but not executed; its success rate is an ideal formula. Keep that boundary in the headline.
3. **Do real visual QA.** Local build and structural checks pass, but this audit did not obtain a browser screenshot of desktop or mobile rendering. Inspect widths around 375, 768 and 1440 pixels, keyboard search, the `Explore` menu, long tables, dark mode and the application × problem matrix before promotion. Fix any overflow or contrast issue found there.
4. **Sample external links and figure provenance.** The strict reference check validates arXiv identifiers and titles, not every external web URL or every statement attributed to a paper. Review the prominent case, homepage-linked pages and claim sources manually. Figures must continue to have a public script/result source and permission to publish.
5. **State the community review capacity honestly.** Issues and PRs work, but there is no account-free submission form or agent write API. Maintainer direct pushes can bypass the PR rule while CI still runs; independent review is a process expectation, not an enforced guarantee on every page.

The site can be described as a **public beta and open research catalogue** now. It should not yet be promoted as a fully peer-reviewed benchmark database or as evidence that a practical industrial advantage has been found.
