---
name: grill-question
description: Sharpen a research question on the hospital data warehouse (EDS) by relentless interview, until it is typed (descriptive, analytic, predictive, diagnostic, quality), formulated as PECO, and written to studies/<slug>/01-question.md. Start of every study.
disable-model-invocation: true
---

All produced documents are written in **French**.

You turn a vague wish ("combien de patients ont un cancer du côlon ?", "est-ce que les fluoroquinolones donnent des infarctus ?") into a question precise enough that the study design follows from it.

## Steps

1. Follow `study-folder`: read `CONTEXT.md` (propose `/setup-eds-skills` if missing), create `studies/<slug>/` from the user's wording, and read `01-question.md` if it already exists (then you are refining, not starting).
2. Read `epi-designs` § 1 to hold the five question types in mind.
3. Run `grilling`. The design tree for a question, round by round:

   **Round 1: type and utility.**
   - Which type is the question: descriptive / analytic (causal) / predictive / diagnostic / quality of care? If the user's sentence mixes types ("how many, and is it caused by…"), split it and ask which one is primary.
   - What changes if the answer is known (a clinical practice, a resource, a publication, a grant)? A question with no consequence is usually not the real question.
   - Who is the investigator and what is the deadline?

   **Round 2: PECO / PICOT.** One question per component, each with a recommendation:
   - Population: which patients, seen where, over which period, which age range. In an EDS the population is *patients who had contact with this hospital*: make the user say so.
   - Exposure / factor (analytic), or the condition to count (descriptive), or the predictors (predictive).
   - Comparator (analytic only): non-users are almost never the right comparator; propose an **active comparator** and explain confounding by indication in one sentence.
   - Outcome: the clinical event, not the code. How would a clinician confirm it?
   - Time: the window between exposure and outcome, the follow-up horizon, the calendar period.

   **Round 3: type-specific.**
   - Descriptive: which measures (prevalence, incidence, age pyramid, trend, length of stay, mortality) and which denominator; incident vs prevalent cases; need for a look-back.
   - Analytic: the causal hypothesis and its mechanism (this decides the latency and the lag), the confounders the user already suspects, whether the outcome is acute (self-controlled designs become possible).
   - Predictive: prediction time, horizon, intended use of the score.
   - Diagnostic: index test, reference standard, population in whom the test would be used.

   **Round 4: data availability (facts first).** For each concept in the PECO, look up `CONTEXT.md` yourself and state whether a source plausibly exists (PMSI codes, prescriptions, labs, text). Ask the user only about what `CONTEXT.md` cannot tell (e.g. whether community prescriptions are linked). Do not define codes here: that is `/define-phenotype`.

4. When the frontier is empty, summarise the decisions and get the user's confirmation.
5. Write `studies/<slug>/01-question.md` from `templates/01-question.md`: the question in one sentence, type with justification, utility, PECO table, primary and secondary objectives, hypotheses, expected measures, presumed data sources, applicable reporting guideline (from `reporting-guidelines`), investigators and calendar, history line.
6. Update `studies/<slug>/README.md` and tell the user the next step: `/study-design`.

## Quality bar

- The one-sentence question names population, factor, outcome and period. "Les fluoroquinolones augmentent-elles le risque d'infarctus du myocarde dans les 60 jours, par rapport à l'amoxicilline, chez les adultes hospitalisés au CHU de Brest entre 2015 et 2024 ?" passes. "Les fluoroquinolones donnent-elles des infarctus ?" does not.
- Exactly one primary objective.
- The type is stated and the reporting guideline follows from it.
- Nothing in the document was assumed without being asked or looked up.

Done when `01-question.md` exists, the user has confirmed the summary, and the README points to `/study-design`.
