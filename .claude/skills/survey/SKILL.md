---
name: survey
description: Research a quantum-advantage candidate (application, problem, or method) and write or update its page in content/, following AGENTS.md.
---

You are adding or updating one page in this catalogue. Read `AGENTS.md` first.

Argument: `$ARGUMENTS` is a topic (e.g. "OLED emitters", "derivative pricing", "DQI").

Steps:

1. Decide the page type. If people would pay for the answer, it is an `application`; if it is a
   computational task, it is a `problem`; if it is an algorithmic approach, it is a `method`.
   Check `content/` for an existing page with `grep -ril "<topic>" content/` before creating one.
2. Research with web search. Find, at minimum: the best classical method and its cost today; the
   best quantum proposal and its resource estimate (logical qubits, T or Toffoli count); any
   dequantization or hardness result; and any first-hand statement from a buyer about accuracy or
   speed targets. Record every arXiv ID you rely on.
3. Grade the three dimensions using the levels in AGENTS.md. Be conservative: `first-hand`
   requires the buyer's own words; `empirical` hardness is the default when no proof exists.
4. Write the page with the required sections for its type. Keep it under 1,200 words. Every
   number gets a reference. Link related pages through `related:` (ids must exist).
5. Run `python tools/validate.py` and `python tools/verify_refs.py`. Fix every error.
6. Report: the page path, the verdict, the one sentence that justifies it, and the sources you
   rejected and why.
