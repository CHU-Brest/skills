---
name: report
description: Write the study report (IMRaD in French, STROBE/RECORD or TRIPOD/STARD checklist filled, structured abstract in French and English, limitations derived from the bias catalogue) to studies/<slug>/06-rapport.md from the study folder and the analysis outputs.
disable-model-invocation: true
---

All produced documents are written in **French** (the abstract is also given in English).

The report is assembled from the study folder: nothing in it is new. Methods come from the protocol, phenotypes and plan; results come from `analyse/output/`; limitations come from the bias table. If something is missing upstream, say so and stop rather than inventing it.

## Steps

1. Follow `study-folder`: read every document of the study in order, `analyse/output/tables.md`, `analyse/output/results.json`, `analyse/journal.md`, and `06-rapport.md` if it exists.
2. Read the checklist named in `01-question.md` (via `reporting-guidelines`) and `epi-biases`.
3. Write the sections of `templates/06-rapport.md`:
   - **Introduction**: context and justification from the protocol, the question in one sentence, the primary objective.
   - **Méthodes**: one sub-section per checklist methods item, in the checklist's order. Phenotypes are summarised with a pointer to the full code lists (RECORD requires the code lists to be published: put them in an appendix or cite `03-phenotypes.md`). The regulatory paragraph comes from the protocol.
   - **Résultats**: selection flow with the final counts; Tableau 1; the primary result in words and numbers (absolute and relative, with CI); secondary and sensitivity results, each tied to the bias it tested; every table and figure from `analyse/output/` inserted, numbered and captioned.
   - **Discussion**: main result in one paragraph; comparison with the literature (ask the user for references or dispatch a sub-agent to find them, and cite them); strengths; **limitations** written per residual bias: for every bias marked *concerned* in the protocol, what the parade was, what the sensitivity analysis showed, and what remains; implications; conclusion answering the question.
   - **Résumé structuré** (≤ 300 words) and **Abstract** (English).
   - **Checklist**: the filled table (item, description, section of the report). An item without a section is a gap: fix the report, do not leave the row blank.
   - **Écarts**: copy the journal's deviations table.
4. Re-read the report against the quality bar below, then write `06-rapport.md`.
5. Update the README; next step: `/review-study 06-rapport.md`. Offer conversion to `.docx` (pandoc, or the `docx` skill when available) only after the review.

## Quality bar

- Every number in the report exists in `results.json` or `tables.md`.
- No causal language for a descriptive or a confounded result: « associé à » unless the design supports « entraîne ».
- The primary result is reported with its absolute measure (risk difference, number needed to harm) next to the relative one.
- Small cells are masked in every table.
- Each limitation names a bias from `epi-biases` and its quantification; « les données de l'EDS ont des limites » is not a limitation.

Done when `06-rapport.md` is complete with a fully filled checklist and the README points to `/review-study`.
