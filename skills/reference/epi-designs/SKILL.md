---
name: epi-designs
description: Reference for choosing an epidemiological study design and its measures from a typed research question (descriptive, analytic, predictive, diagnostic, quality of care) in a hospital data warehouse (EDS). Use when a skill must pick a design, define time zero, or name the right effect measure.
---

# Study designs for EDS questions

The design follows from the **type of question**. Settle the type first (that is `/grill-question`'s job), then read the matching section.

## 1. Question types

| Type | The question sounds like | Typical output | Reporting guideline |
|---|---|---|---|
| **Descriptive** | how many, how often, who, where, when, trend | counts, incidence, prevalence, age pyramid, distributions | STROBE + RECORD |
| **Analytic (causal)** | does X change the risk of Y | HR, RR, OR, risk difference, with confidence interval | STROBE + RECORD (+ target-trial table) |
| **Predictive / prognostic** | who will develop Y, can we score the risk | model, discrimination (AUC, C-index), calibration | TRIPOD |
| **Diagnostic accuracy** | does test T detect condition D | sensitivity, specificity, PPV, NPV, ROC | STARD |
| **Quality of care / process** | is guideline G followed, what delay between A and B | proportions, delays, variation between units | STROBE + RECORD |

A question that mixes types (describe *and* explain) is two questions: write both, rank them, keep the primary one.

## 2. Descriptive questions

Decide the **measure** and the **denominator** before anything else.

- **Prevalence** = patients with the condition at a point in time (or over a period) / population at risk at that time. In an EDS the denominator is usually *patients seen in the hospital over the period*, which is **not** the general population. Say it explicitly.
- **Incidence** = *new* cases over a period / population at risk at the start. Needs a **wash-out** (no code for the condition during the N years before) to separate new from prevalent cases; needs a **look-back** long enough (state it). Report as proportion (cumulative incidence) or as rate per person-years.
- **Age pyramid**: age at first occurrence, by sex, in 5- or 10-year bands. Mask small cells.
- **Trend**: by year of first occurrence; beware coding changes (new ICD-10 version, new department) that create artificial steps.

Design: **cross-sectional** for prevalence, **retrospective cohort** for incidence and trends.

## 3. Analytic (causal) questions

### 3.1 Choose the design

| Situation | Design | Effect measure |
|---|---|---|
| Exposure is a treatment started at an identifiable date, outcome occurs later | **New-user cohort** (exposed vs comparator) | HR (Cox), or cumulative incidence difference |
| Outcome is rare and exposure is common | **Nested case-control** inside the cohort | OR (approximates RR) |
| Exposure is transient and the outcome acute (drug and myocardial infarction within days) | **Self-controlled case series** or **case-crossover** | Incidence rate ratio |
| A policy or practice changed at a date | **Interrupted time series** or before/after with control | Level and slope change |
| Exposure is fixed at baseline (a diagnosis, a characteristic) | **Retrospective cohort** | HR, RR |

### 3.2 Emulate the target trial

For every causal question, fill in the **target trial** table before writing the protocol. It forces the decisions that prevent the classic biases.

| Component | What to decide | EDS pitfall it prevents |
|---|---|---|
| Eligibility | who is enrolled, defined at time zero only | conditioning on the future |
| Treatment strategies | exposed strategy vs comparator strategy | non-users as comparator (confounding by indication) → prefer an **active comparator** |
| Assignment | how we mimic randomisation: adjustment, propensity score, matching | unmeasured confounding |
| Time zero | the date eligibility is met **and** strategy is assigned, for both arms | **immortal time bias** |
| Follow-up | start (time zero), end (outcome, death, last contact, end of data), censoring rules | informative censoring |
| Outcome | precise phenotype (see `define-phenotype`), adjudication | detection bias |
| Causal contrast | intention-to-treat like (first exposure) vs per-protocol like (continuous exposure) | misclassification |
| Analysis plan | model, covariates, sensitivity analyses | p-hacking |

Rule: **new-user design** (exclude patients already exposed before time zero) with an **active comparator** (a drug used for the same indication) is the default for drug questions. Deviating from it must be justified in the protocol.

### 3.3 Effect measures

- **HR** (hazard ratio): time-to-event, Cox model. Assumes proportional hazards; check it (Schoenfeld) and, if violated, report cumulative incidence at fixed times instead.
- **RR** (risk ratio) and **risk difference**: fixed follow-up, log-binomial or standardisation. Easier to interpret for clinicians.
- **OR** (odds ratio): case-control or logistic regression. Overstates RR when the outcome is common (> 10 %).
- **Rate ratio**: person-time denominators, Poisson.
- Always report the **absolute** measure alongside the relative one (number needed to harm, cumulative incidence in each arm).

### 3.4 Confounding

Draw a **DAG** (Mermaid) with exposure, outcome, and every variable that plausibly causes both. Adjust on the minimal sufficient set; never on a variable caused by the exposure (mediator) or by the outcome (collider). Record in the protocol which confounders are **measurable** in the EDS and which are not (smoking, BMI, socio-economic status are often absent), because that decides the sensitivity analyses (E-value, negative control outcomes).

## 4. Predictive questions

- Define the **prediction time** (when the score is computed) and the **horizon** (predict at 30 days, 1 year).
- Predictors must be available *before* the prediction time. Anything recorded later leaks the outcome.
- Split: temporal (train on earlier years, test on later) beats random; external validation on another site if possible.
- Report discrimination (AUC / C-index), calibration (plot, slope, intercept), and clinical utility (decision curve) per TRIPOD.
- Sample size: at least 10 to 20 events per candidate predictor as a floor; use `pmsampsize`-type formulas when possible.

## 5. Diagnostic questions

- Index test, reference standard, and the population in whom the test would be used in practice, all defined a priori.
- Beware **verification bias** (only patients with a positive test get the reference standard) and **spectrum bias**.
- Report a 2×2 table with confidence intervals, per STARD.

## 6. Sample size and power

Compute it in Python and paste the code and result in the protocol:

- Two proportions: `statsmodels.stats.proportion.proportion_effectsize` + `NormalIndPower`.
- Survival (Cox): Schoenfeld's formula, number of events = (z_α + z_β)² / (p₁ p₂ (ln HR)²), then divide by the expected event probability to get patients.
- Precision of a proportion (descriptive): n = z² p(1-p) / d².

When the EDS population is fixed (all patients seen), reverse the calculation: report the **minimum detectable effect** for the available n.

## 7. Choosing quickly

```
descriptive ─┬─ point in time → cross-sectional, prevalence
             └─ over time     → retrospective cohort, incidence / trend
analytic   ──┬─ drug / intervention started at a date → new-user active-comparator cohort (target trial)
             ├─ acute outcome, transient exposure     → self-controlled case series
             ├─ rare outcome, costly covariates       → nested case-control
             └─ policy change                          → interrupted time series
predictive ── → cohort at prediction time, TRIPOD
diagnostic ── → cross-sectional vs reference standard, STARD
```
