---
name: analysis-plan
description: Write the pre-specified statistical analysis plan of an EDS study - estimand, primary model, confounding control, missing data, sensitivity analyses derived from the anticipated biases, multiplicity, software, table shells - to studies/<slug>/05-plan-analyse.md, before any data is analysed.
disable-model-invocation: true
---

All produced documents are written in **French**.

The plan is written **before** the outcome data is looked at, and `/analyze` will be held to it: any deviation goes into the analysis journal. This is what makes the result credible.

## Steps

1. Follow `study-folder`: read `CONTEXT.md`, `01-question.md`, `02-protocole.md`, `03-phenotypes.md`, `04-faisabilite.md` (actual n and event counts), and `05-plan-analyse.md` if it exists.
2. Read `epi-designs` (§ 3.3 for measures, § 4 for prediction) and `epi-biases` (the « quantify » lines of every bias marked *concerned* in the protocol are your sensitivity analyses).
3. Run `grilling` on the decisions:

   **Round 1: estimand.** Population, exposure contrast, outcome, handling of intercurrent events (death before outcome, treatment switch, discontinuation: treatment-policy, hypothetical, or composite), summary measure (HR, risk difference at 1 year, rate ratio). Recommend one.

   **Round 2: primary analysis.** Model (Cox, Fine-Gray if competing risk of death matters, Poisson, logistic, log-binomial); covariates from the DAG's minimal adjustment set; confounding control (propensity score: matching, IPTW, or covariate adjustment; recommend based on arm sizes from `04-faisabilite.md`); balance diagnostic (standardised differences < 0.1); handling of time (time-varying exposure if the protocol requires it); assumption checks (proportional hazards, overlap).

   **Round 3: missing data.** For each variable with completeness below 95 % in `04-faisabilite.md`: mechanism assumed, method (multiple imputation with the outcome in the imputation model, missing indicator for « never measured » labs, complete case as sensitivity).

   **Round 4: sensitivity and secondary.** One sensitivity analysis per concerned bias (lag periods for protopathic bias, look-back variations, narrow vs broad phenotype, negative control outcome, E-value, time-varying exposure for immortal time, censoring at last contact). Secondary outcomes and subgroups, each with its expected direction. Multiplicity policy.

   **Round 5: prediction (if predictive).** Split strategy (temporal), candidate predictors, penalisation, discrimination, calibration, decision curve, internal validation (bootstrap), per TRIPOD.

4. Write the **table shells**: Tableau 1 (baseline characteristics by arm, with standardised differences), Tableau 2 (primary and secondary results: n, events, person-time, crude and adjusted measures with 95 % CI), Figure 1 (selection flow), Figure 2 (Kaplan-Meier or cumulative incidence), plus one table per sensitivity analysis. Rows and columns are named; cells are empty.
5. Write `studies/<slug>/05-plan-analyse.md` from `templates/05-plan-analyse.md`, including the software section: Python version, packages with pinned versions (pandas, numpy, statsmodels, lifelines, tableone, matplotlib), seed.
6. Update the README; next step: `/review-study 05-plan-analyse.md`, then `/clear` and `/analyze`.

## Rules

- One primary analysis. Everything else is labelled secondary or sensitivity.
- Every sensitivity analysis names the bias it addresses and what result would change the conclusion.
- No p-value-driven variable selection for causal questions; the covariates come from the DAG.
- Table shells respect the small-cell rule (categories pooled in advance).

Done when `05-plan-analyse.md` is complete, the user has confirmed, and the README points to `/analyze`.
