---
name: ask-eds
description: Ask which EDS study skill or flow fits your situation. A router over the skills in this repository.
disable-model-invocation: true
---

Answer in **French**. You do not remember every skill, so ask.

Read the user's situation, find where they are on the map below, and tell them the next skill, why, and what it will produce. If they are mid-study, read `studies/<slug>/README.md` first: it says where the study stands.

## The main flow: question → report

Every study travels this road. Each skill reads the previous documents of `studies/<slug>/` and writes the next one, so the study survives across sessions.

1. **`/setup-eds-skills`** once per repository: builds `CONTEXT.md`, the description of the warehouse every other skill relies on.
2. **`/grill-question`** turns the wish into a typed, PECO-formulated question → `01-question.md`. The type (descriptive, analytic, predictive, diagnostic, quality) decides the rest of the road.
3. **`/study-design`** writes the protocol: design, target trial emulation, time zero, variables, DAG, anticipated biases, sample size, regulatory section → `02-protocole.md`.
4. **`/define-phenotype`** turns each variable into exact code lists, temporal rules, algorithm, indicative SQL and a validation plan → `03-phenotypes.md`.
5. **`/feasibility`** counts: selection flow, arm sizes, events, data quality, go / no-go → `04-faisabilite.md`. Queries run automatically if `CONTEXT.md` declares a connection; otherwise the user runs them.
6. **`/analysis-plan`** pre-specifies the statistics: estimand, model, confounding control, missing data, sensitivity analyses, table shells → `05-plan-analyse.md`.
7. **`/analyze`** executes the plan in Python on the extract → `analyse/` (scripts, tables, figures, deviation journal).
8. **`/report`** assembles the IMRaD report with the filled checklist and abstracts → `06-rapport.md`.

**`/review-study <document>`** runs at every milestone (protocol, plan, report at least) and writes `revue-<document>.md`. Do not move to data work with a blocking finding open.

## Shortcuts by question type

- **Descriptive** (how many, incidence, prevalence, age pyramid, trend): `/grill-question` → `/study-design` (light) → `/define-phenotype` → `/feasibility` → `/report`. The feasibility tables are the results; `/analysis-plan` and `/analyze` are needed only if the description needs modelling (trends, standardised rates).
- **Analytic / causal** (does X change the risk of Y): the full road. Do not skip `/feasibility`: an analytic study on an empty column fails silently.
- **Predictive** (who will develop Y): the full road with TRIPOD; `/analysis-plan` carries the split, validation and calibration decisions.
- **Diagnostic** (does T detect D): `/grill-question` → `/study-design` → `/define-phenotype` → `/feasibility` → `/analysis-plan` → `/analyze` → `/report` with STARD.

## Context hygiene

- Keep `/grill-question` → `/study-design` → `/define-phenotype` in **one session**: the design decisions feed each other.
- `/clear` before `/analyze`: it needs the plan and the data, not the conversation that produced them.
- Each skill re-reads the folder, so a new session can start at any step.

## Vocabulary underneath

Model-invoked references the skills pull in; call them directly when the *words* are the problem:

- **`grilling`**: the interview primitive (rounds, frontier, facts vs decisions).
- **`epi-designs`**: question type → design → measure; target trial table; sample size.
- **`epi-biases`**: the bias catalogue with EDS examples, parades and quantifications.
- **`reporting-guidelines`**: STROBE, RECORD, TRIPOD, STARD checklists and how to fill them.
- **`terminologies`**: CIM-10 ATIH, ATC, CCAM, NABM/LOINC, PMSI conventions, code-list rules.
- **`regulatory-fr`**: MR-004, CNIL, CSE, Health Data Hub, patient information.
- **`study-folder`**: the folder layout, document headers, data hygiene.

## Standalone situations

- « J'ai déjà un protocole écrit ailleurs » → put it in `studies/<slug>/02-protocole.md` with the header from `study-folder`, then `/review-study 02-protocole.md`; the review tells you which upstream document to write.
- « J'ai un résultat et je dois écrire l'article » → `/report` needs the folder; at minimum write `01-question.md` and `02-protocole.md` from what exists, then `/report`.
- « Je dois répondre au comité scientifique / à la CNIL » → `/study-design` round 6, or read `regulatory-fr` directly.
- « Quels codes pour … ? » → `/define-phenotype` on a single concept, or read `terminologies`.
