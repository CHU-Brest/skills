---
name: feasibility
description: Descriptive exploration of the EDS to validate a study population before analysis - selection flow with counts, arm sizes, age/sex distribution, data quality, go/no-go - written to studies/<slug>/04-faisabilite.md. Runs the counting queries itself when CONTEXT.md declares a connection, otherwise hands them to the user.
disable-model-invocation: true
---

All produced documents are written in **French**.

Before any model, prove that the population exists, is large enough, and that the key variables are populated. This is the « validation par exploration descriptive » that protects the study from a null result caused by an empty column.

## Two execution modes

Read the `## Connexion` section of `CONTEXT.md`.

- **Connected** (a SQL engine, host and schema are declared and reachable): run the queries yourself with the tool the section names (a Python script with the declared driver, or an MCP SQL tool). Only `SELECT` statements, only aggregates; never pull patient-level rows into the conversation.
- **Not configured** (the default until the CHU sets it up): write each query in a numbered fenced `sql` block, ask the user to run them in the secure environment and paste the aggregated results, then interpret. Tell the user once that the section « Connexion » of `CONTEXT.md` can be filled to make this automatic.

## Steps

1. Follow `study-folder`: read `CONTEXT.md`, `02-protocole.md`, `03-phenotypes.md`, and `04-faisabilite.md` if it exists.
2. Build the **selection flow** from the protocol's eligibility criteria, in order, one query per step, each returning a count. Steps typically: patients in the warehouse over the period → with the required look-back → meeting eligibility → with exposure or comparator → after wash-out → after exclusions. Write the Mermaid flowchart with `n = …` placeholders.
3. Write the **arm queries**: patients per arm, events per arm, person-time per arm, crude rate per arm. From these, compute the crude effect estimate and confidence interval in Python and compare with the sample-size assumptions of the protocol.
4. Write the **description queries**: age bands × sex, calendar year of time zero, department, per arm. Mask cells below the threshold in `CONTEXT.md`.
5. Write the **data-quality queries** (Kahn framework) for each key variable: completeness (share of non-null), plausibility (value ranges, dates in order, age at event between 0 and 110), conformity (codes present in the terminology). Include a query that plots the outcome's yearly count to detect coding steps.
6. Run (connected) or collect (not configured) the results. Paste every result under its query.
7. Write the **decision** with the user: **go** (population and events match the assumptions), **no-go** (too few events, a key variable empty), or **redefine** (which part of the protocol or phenotype must change and why). A no-go is a valid, useful outcome; say so.
8. Write `studies/<slug>/04-faisabilite.md` from `templates/04-faisabilite.md`. Update the README; next step: `/analysis-plan` (go) or back to `/study-design` / `/define-phenotype` (redefine).

## Rules

- Aggregates only. If a query would return fewer than the small-cell threshold, the document shows « <10 » (or the threshold from `CONTEXT.md`).
- Every count in the flowchart has its query in the document.
- Compare what you find with what the protocol assumed (expected n, expected event rate). A mismatch is a finding, not a footnote.
- A descriptive study may stop here: its results *are* the feasibility tables. Say it, and go to `/report`.

Done when `04-faisabilite.md` holds the flow with counts, the quality table, the decision, and the README points to the next skill.
