---
name: study-folder
description: Conventions for the per-study folder (studies/<slug>/) that every EDS study skill reads and writes. Use whenever a study skill needs to locate, create or update a study document.
---

Every study lives in **one folder** so that any session can pick it up where the last one stopped. The folder is the memory; the conversation is not.

## Layout

```
CONTEXT.md                     shared: data model of the EDS + glossary (built by /setup-eds-skills)
studies/<slug>/
  README.md                    one-paragraph status: what exists, what is next, who is the investigator
  01-question.md               /grill-question
  02-protocole.md              /study-design
  03-phenotypes.md             /define-phenotype
  04-faisabilite.md            /feasibility
  05-plan-analyse.md           /analysis-plan
  analyse/                     /analyze : scripts, requirements.txt, journal.md, output/
  06-rapport.md                /report
  revue-<document>.md          /review-study (one per reviewed document, e.g. revue-02-protocole.md)
  data/                        extracts provided by the user; NEVER committed (see .gitignore)
```

`<slug>` is a short kebab-case name derived from the question (e.g. `fluoroquinolones-infarctus`, `cancer-colon-incidence`).

## Starting a study skill

1. Read `CONTEXT.md` at the repository root. If it does not exist, say so and propose `/setup-eds-skills`; continue only if the user accepts to work without it.
2. Locate the study folder: the user names it, or there is exactly one folder under `studies/`, or ask. Create it (and `README.md`) if the skill is `/grill-question`.
3. Read every existing numbered document in order. Their decisions are settled: do not re-ask them, build on them. If a later document contradicts an earlier one, flag it before proceeding.
4. Write the document the skill owns. If it already exists, propose to update it in place (keeping its `version` and adding a line to its `historique`) rather than creating a duplicate.
5. Update `studies/<slug>/README.md`: current status and the suggested next skill.

## Document header

Every numbered document starts with a YAML header:

```yaml
---
etude: <slug>
document: 02-protocole
version: 1
date: 2026-09-02
auteur: <name given by the user, else "à compléter">
statut: brouillon | relu | validé
produit_par: /study-design
---
```

Followed by a `## Historique` section at the end (one line per version: date, author, change).

## Data hygiene

- Patient-level data never enters git. On first write into a study folder, make sure the repository `.gitignore` contains:
  ```
  studies/*/data/
  studies/*/analyse/output/*.csv
  studies/*/analyse/output/*.parquet
  ```
- Aggregated outputs (tables, figures) may be committed only if every cell respects the small-cell rule from `CONTEXT.md` (default: counts below 10 are masked as `<10`).
- Never write a real patient identifier, name or date of birth into any document, even as an example.

## Language

All documents in the study folder are written in **French**. Section titles, tables and figure captions included. Code comments may be in English.
