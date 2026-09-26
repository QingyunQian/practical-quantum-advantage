---
name: verify-refs
description: Run the arXiv reference checker across all pages and fix unresolved IDs or mismatched titles.
---

1. Run `python tools/verify_refs.py`.
2. For every `UNRESOLVED` line, search arXiv for the title in the entry and correct the ID, or
   remove the reference and any sentence that depended on it.
3. For every `TITLE MISMATCH`, open the arXiv page, decide whether the entry's title is a typo
   (fix it) or the ID points to a different paper (find the right one). Never "fix" a mismatch by
   copying the wrong paper's title.
4. Re-run until it prints `0 problems`, then run `python tools/validate.py`.
