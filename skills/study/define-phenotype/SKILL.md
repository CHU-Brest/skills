---
name: define-phenotype
description: Define the computable phenotypes (exposure, outcome, covariates) of an EDS study as exact code lists, temporal rules, algorithms, indicative SQL and a validation plan, written to studies/<slug>/03-phenotypes.md. Use after the protocol, before any feasibility or analysis.
disable-model-invocation: true
---

All produced documents are written in **French**.

A phenotype is the bridge between a clinical concept in the protocol ("infarctus du myocarde") and rows in the warehouse (`I21.*` in DP of an MCO stay, plus a troponin above threshold). Most EDS errors live on that bridge.

## Steps

1. Follow `study-folder`: read `CONTEXT.md` (data model, coding conventions, terminology versions), `01-question.md`, `02-protocole.md` (its variables table is your to-do list), and `03-phenotypes.md` if it exists.
2. Read `terminologies` for the coding conventions and the code-list writing rules.
3. For **each variable** of the protocol, in this order: outcome, exposure, comparator, confounders, then eligibility criteria:
   - **Facts first.** Look up candidate codes yourself: `terminologies`, published validated algorithms (SNDS "cartographie des pathologies", literature), the ICD-10 MCP server when available (it serves the US ICD-10-CM: use it to find the chapter, then check the ATIH version), and `CONTEXT.md` for which tables hold them. Never present a code as certain if it was not checked; mark it « à vérifier ».
   - **Then grill** (via `grilling`) the decisions only the user can make: colon vs colorectal (C18 alone or with C19-C20); DP only or any position; one stay or two; look-back length; whether a confirming source is required (procedure, lab, pathology, text); the grace period and window for drug exposure; the definition of "new user".
   - Write the **algorithm** as pseudo-code with explicit temporal logic (first occurrence, no occurrence in the N previous years, within X days of time zero).
   - Write **indicative SQL** derived from the tables in `CONTEXT.md`. Mark it « à valider sur l'entrepôt ». If `CONTEXT.md` has no model for that source, write the SQL against a described-but-hypothetical table and say so.
   - Write two variants when the choice is uncertain: **narrow** (high PPV) and **broad** (high sensitivity), and say which is primary.
   - Write the **validation plan**: how many charts to review, who reviews, the target PPV, and what happens if it is not met.
4. Fill the synthesis table (concept, role, one-line definition, PPV target/measured).
5. Write `studies/<slug>/03-phenotypes.md` from `templates/03-phenotypes.md`, with the terminology versions and dates at the top.
6. Update the study README; next step: `/feasibility`.

## Rules

- Every code list is a table: code, label, terminology, accepted position, source table. Prefix notation is explicit (« C18.* »).
- Temporal rules are written relative to **time zero** as defined in the protocol; no phenotype introduces a new time zero.
- Confounders are assessed **before** time zero; the look-back window is stated per confounder.
- Small-cell and privacy rules from `CONTEXT.md` apply to any counts you quote.
- Cite the source of each reused algorithm.

Done when every variable of the protocol has a phenotype block, the synthesis table is complete, and the README points to `/feasibility`.
