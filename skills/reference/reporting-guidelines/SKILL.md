---
name: reporting-guidelines
description: Reporting checklists (STROBE, RECORD, TRIPOD, STARD) for observational, routinely-collected-data, prediction and diagnostic studies. Use when structuring a protocol or report, or when reviewing one.
---

# Reporting guidelines for EDS studies

A protocol or report is complete when every item of the relevant checklist can be pointed to in the document. The checklists below are paraphrased in French, one line per item, with an **« En EDS »** column saying what to write concretely for a hospital data-warehouse study (PMSI codes, prescriptions, labs, snapshot dates, small-cell masking).

## Which checklist

The question type comes from `01-question.md` (see `epi-designs`).

| Question type | Checklist(s) | File(s) |
|---|---|---|
| Descriptive | STROBE + RECORD | `checklists/strobe.md`, `checklists/record.md` |
| Analytic (causal) | STROBE + RECORD | `checklists/strobe.md`, `checklists/record.md` |
| Quality of care / process | STROBE + RECORD | `checklists/strobe.md`, `checklists/record.md` |
| Predictive / prognostic | TRIPOD | `checklists/tripod.md` |
| Diagnostic accuracy | STARD | `checklists/stard.md` |

RECORD is an *extension* of STROBE: it never replaces it. A study on the EDS always uses STROBE and RECORD together, with RECORD items interleaved after the STROBE item they extend (1.1–1.3 after item 1, 6.1–6.3 after item 6, and so on). A predictive study whose cohort is built from PMSI codes should also fill RECORD 6.1, 6.2, 7.1 and 13.1 in addition to TRIPOD, because those items are about how the warehouse data were turned into a study population.

## How a skill uses a checklist

1. Read the checklist file(s) for the question type.
2. Write the document so that every item has a home section. The « En EDS » column tells what the section must contain; the study's own documents (`03-phenotypes.md`, `05-plan-analyse.md`, `CONTEXT.md`) provide the values.
3. End the document with a filled table, in French, under the heading **« Checklist de rapport »** of the template (one sub-heading per grid: « Grille STROBE », « Grille RECORD », …), with exactly these columns:

   ```
   | Item | Description | Section du rapport |
   ```

   - **Item**: the number and letter as in the checklist (`1a`, `6.1`, `10b`, `21a`).
   - **Description**: the short paraphrase from the checklist (may be shortened further).
   - **Section du rapport**: the heading of the section (or table/figure number) where the item is answered.
4. An item that does not apply is not left blank: the third column reads **« NA, car … »** with the reason (e.g. `NA, car étude transversale sans suivi`, `NA, car aucun chaînage entre bases`). The reason must be checkable against the design.
5. Never delete or renumber an item. If the document uses a different structure (e.g. a protocol has no Results yet), the item still appears with `À rapporter dans 06-rapport.md` in the third column.

## What each skill does with it

- `/study-design` → the protocol's structure follows the Methods items; the grid at the end of `02-protocole.md` maps Methods items to sections and marks Results/Discussion items as `À rapporter dans 06-rapport.md`.
- `/analysis-plan` → items on statistical methods, missing data, sensitivity analyses (STROBE 12a–e, TRIPOD 8–10, STARD 14–18) must each have a subsection in `05-plan-analyse.md`.
- `/report` → `06-rapport.md` ends with the full grid; every row points to an existing section or gives a `NA, car …`.
- `/review-study` → checks the grid line by line against the document. **A missing item, an empty third column, a `NA` without a reason, or a section that does not actually contain what the item asks for is a blocking finding** (`bloquant`), not a suggestion. The review file lists each such item with its number.

## Checklist files

- `checklists/strobe.md` — STROBE, 22 items, combined cohort / case-control / cross-sectional version.
- `checklists/record.md` — RECORD extension, 13 items (1.1–1.3, 6.1–6.3, 7.1, 12.1–12.3, 13.1, 19.1, 22.1).
- `checklists/tripod.md` — TRIPOD 2015, 22 items with sub-items; the D/V column says whether the item concerns development, validation or both.
- `checklists/stard.md` — STARD 2015, 30 items.

The wording in these files is a paraphrase. When a journal asks for the official checklist, fill the official form from the grid; the numbering is identical.
