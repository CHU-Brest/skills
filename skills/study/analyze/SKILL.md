---
name: analyze
description: Execute the pre-specified analysis plan of an EDS study in Python on the extract provided by the user - numbered reproducible scripts, Table 1, models, figures, deviation journal - in studies/<slug>/analyse/. Use after /analysis-plan, in a fresh session.
disable-model-invocation: true
---

All produced documents are written in **French**; code comments may be in English.

You run the plan, you do not improvise it. The plan (`05-plan-analyse.md`) is the specification; the journal records every deviation and why.

## Inputs

- The extract(s) the user places in `studies/<slug>/data/` (CSV or Parquet, one row per patient or per patient-period). Ask for the data dictionary of the extract if column names are not self-explanatory; never guess a column's meaning.
- If no extract exists yet, write the extraction specification instead: the columns needed (from the phenotypes and the plan), one row per what, the SQL from `03-phenotypes.md` assembled into a cohort query, and stop. Say clearly that the analysis needs the extract.

## Steps

1. Follow `study-folder`: read `CONTEXT.md`, `02-protocole.md`, `03-phenotypes.md`, `05-plan-analyse.md`. Make sure the repository `.gitignore` excludes `studies/*/data/` and patient-level outputs.
2. Set up `studies/<slug>/analyse/`:
   - `requirements.txt` with pinned versions matching the plan's software section; install them in a virtual environment.
   - `00_config.py`: paths, seed, small-cell threshold from `CONTEXT.md`, snapshot date.
   - `journal.md`: date, snapshot, extract file name and hash, and a « Écarts au plan » table (what, why, impact).
3. Write and run the scripts **in this order**, each idempotent, each writing to `analyse/output/`:
   - `10_import.py`: load, type, validate the extract against the data dictionary (dates parse, ages plausible, no duplicated patient id, time zero before outcome). Print a validation report; stop on a hard failure.
   - `20_flow.py`: reproduce the selection flow with counts (must match `04-faisabilite.md` within explanation; a mismatch goes in the journal).
   - `30_table1.py`: baseline characteristics by arm with standardised differences (tableone), masked cells, saved as Markdown and CSV.
   - `40_primary.py`: the primary analysis exactly as planned (propensity score with balance diagnostics if planned, model, assumption checks, effect with 95 % CI), and the primary figure (Kaplan-Meier / cumulative incidence with number at risk).
   - `50_secondary.py`, `60_sensitivity.py`: one block per pre-specified analysis, each named as in the plan.
   - `90_export.py`: assemble every table shell of the plan filled with the results, as `output/tables.md`, plus a `output/results.json` with the key numbers for `/report`.
4. After each script, read the output critically: implausible effect sizes, empty strata, convergence warnings, proportional-hazards violations. Fix the code, or record the deviation, never silently.
5. Update `journal.md` and the study README; next step: `/report`.

## Rules

- **Never** print or save patient-level rows in the conversation or in `output/`. Aggregates only, small cells masked.
- The primary result is computed once, as planned. Exploring alternatives is allowed only under « analyses exploratoires » in the journal, clearly labelled.
- Every figure has a title, axis labels in French, the number at risk, and is saved as PNG and SVG.
- Every number in `output/tables.md` comes from a script; nothing is typed by hand.
- Use `dataviz` for figure style when it is available.
- If a planned method cannot run (package missing, model does not converge), record it, use the closest pre-specified fallback, and flag it for the report.

Done when every planned table shell is filled in `output/tables.md`, `results.json` exists, the journal is up to date, and the README points to `/report`.
