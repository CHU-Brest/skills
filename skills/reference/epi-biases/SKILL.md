---
name: epi-biases
description: Catalogue of biases specific to studies on routinely collected hospital data (EDS), each with an EDS example, how to detect it and how to prevent or quantify it. Use when writing a protocol's "biais anticipés" section, an analysis plan's sensitivity analyses, a report's limitations, or when reviewing any of them.
---

# Biases in EDS studies

For each bias: **what it is**, **how it shows up in an EDS**, **parade** (prevention in design or analysis), **quantify** (sensitivity analysis to report). A protocol must go through the whole list and say, for each, "concerned / not concerned, because".

## Selection

**Selection bias (référence hospitalière)**
The EDS only contains patients who came to *this* hospital. Prevalence, severity and case-mix differ from the general population.
Parade: state the source population precisely ("patients ayant eu au moins un séjour au CHU entre …"); never extrapolate rates to the territory without an external denominator.
Quantify: compare age/sex structure with the territory's census.

**Left truncation (troncature à gauche)**
History before the warehouse's start date (or before the patient's first contact) is invisible: a "new" case may be an old one.
Parade: require a minimum **look-back** of observed history (e.g. 2 years with at least one contact) before time zero; wash-out for new-user designs.
Quantify: vary the look-back (1, 2, 3 years).

**Loss to follow-up outside the territory (perte de vue)**
Patients treated elsewhere or who move disappear silently; death outside the hospital may be unknown unless a death registry (INSEE/CépiDc) is linked.
Parade: define end of follow-up as *last contact* for patients without event; check `CONTEXT.md` for a vital-status source.
Quantify: sensitivity analysis censoring at last contact vs at end of study.

**Prevalent-user bias**
Including patients already on the drug selects survivors and tolerant patients.
Parade: **new-user design** with wash-out.

**Healthy-user / healthy-adherer bias**
Patients who start or continue a preventive treatment differ in health behaviours.
Parade: active comparator; adjust on markers of health-seeking behaviour (number of visits, vaccinations).

## Information (measurement)

**Outcome misclassification (phénotype imparfait)**
An ICD-10 code in a hospital stay is not a diagnosis: it is billing-driven, position-dependent (DP/DR/DAS) and coder-dependent.
Parade: phenotype algorithm validated by chart review with a target PPV; prefer codes + a confirming source (procedure, lab, pathology); state the algorithm in the report (RECORD item 6.1).
Quantify: analyse with a narrow and a broad definition; quantitative bias analysis with the measured PPV.

**Exposure misclassification**
Prescription ≠ dispensing ≠ intake. Hospital prescriptions miss the community prescriptions.
Parade: state which source (prescription, administration record, community dispensing if linked); define exposure windows with a grace period.
Quantify: vary the grace period.

**Detection / surveillance bias**
Exposed patients are seen more often, so more outcomes are *found* in them.
Parade: outcomes that require no active search (death, myocardial infarction with troponin); adjust on healthcare use before time zero.
Quantify: negative control outcome (one that the exposure cannot cause).

**Protopathic bias (causalité inversée)**
The drug is prescribed for early symptoms of the outcome itself (an antibiotic for chest pain later coded as infarction).
Parade: lag period: ignore outcomes in the first days/weeks after exposure start; check the indication.
Quantify: vary the lag (0, 7, 30 days).

**Coding drift over time**
Coding rules, ICD-10 versions and software change; a trend may be a coding artefact.
Parade: check ATIH version dates in `CONTEXT.md`; plot the trend of *all* codes in the chapter as a control.

## Time-related

**Immortal time bias (biais de temps immortel)**
Follow-up starts before exposure is assigned; the time between the two is "immortal" for the exposed (they had to survive to be exposed) and is counted in their favour.
Parade: time zero = the date exposure status is *known*, identical for both arms; or model exposure as time-varying.
Quantify: re-run with exposure as time-dependent covariate; if results change, the original was biased.

**Time-window bias**
Cases and controls (or arms) have windows of different lengths in which exposure can be observed.
Parade: same window length for everyone, anchored on time zero.

**Immeasurable time**
Time spent in hospital where community prescriptions are not recorded.
Parade: exclude or model hospital days when exposure comes from community data.

**Calendar-time confounding**
Practices change over years; exposed and comparator patients recruited in different periods.
Parade: adjust or match on calendar year; restrict to a period with stable practice.

## Confounding

**Confounding by indication (confusion par indication)**
The reason the drug is prescribed is itself a risk factor for the outcome (fluoroquinolones for severe infection, infection raises infarction risk).
Parade: **active comparator** with the same indication; restrict to one indication; adjust on severity markers; propensity score.
Quantify: E-value; negative control exposure (a drug with the same indication but no plausible effect).

**Unmeasured confounding**
Smoking, BMI, alcohol, socio-economic status, frailty are often missing or unreliable in an EDS.
Parade: proxies (COPD codes for smoking, obesity codes, nursing-home addresses); instrumental variable if one exists.
Quantify: **E-value** for the point estimate and the CI bound; quantitative bias analysis with plausible prevalence of the confounder.

**Collider / adjustment on a consequence of exposure**
Adjusting on a variable caused by the exposure (a lab value measured after treatment) opens a spurious path.
Parade: DAG; covariates measured **before** time zero only.

## Analysis

**Multiple comparisons** many outcomes or subgroups, one is significant by chance.
Parade: one pre-specified primary outcome; the rest exploratory; correct or state that no correction was made.

**Missing data not at random** labs measured only in sicker patients.
Parade: describe missingness by arm; multiple imputation with the outcome in the model; complete-case as sensitivity.

**Small cells and privacy** counts < 10 cannot be published.
Parade: pool categories a priori; mask in outputs.

## How skills use this list

- `/study-design` → section « Biais anticipés et parades » : one line per bias, concerned or not, why.
- `/analysis-plan` → sensitivity analyses come from the « quantify » column of every bias marked *concerned*.
- `/report` → « Limites » of the discussion: the biases that remain after the parades, with the sensitivity-analysis results.
- `/review-study` → check that every bias marked *concerned* has a parade and a quantification, and that none was silently skipped.
