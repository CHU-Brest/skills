---
name: study-design
description: Turn a framed question (01-question.md) into a study protocol for the hospital data warehouse (EDS) - design choice, target trial emulation, time zero, eligibility, variables, confounders and DAG, anticipated biases, sample size, regulatory section - written to studies/<slug>/02-protocole.md.
disable-model-invocation: true
---

All produced documents are written in **French**.

You write the protocol. Every choice must be traceable to `01-question.md` or to a decision the user made during this skill.

## Steps

1. Follow `study-folder`: read `CONTEXT.md`, `01-question.md`, and `02-protocole.md` if it exists (then you update it).
2. Read `epi-designs`, `epi-biases` and `regulatory-fr`. Read the checklist named in `01-question.md` (via `reporting-guidelines`): the protocol is structured on its methods items.
3. Run `grilling`. The design tree:

   **Round 1: design.** Propose the design from `epi-designs` § 7 with its justification, and the alternative you rejected. For an analytic question, present the **target trial table** pre-filled with your recommendations (eligibility, strategies, assignment, time zero, follow-up, outcome, contrast, analysis) and ask the user to confirm or amend each row. For a descriptive question, a lightweight protocol is enough: measure, denominator, look-back, period.

   **Round 2: population and time.** Eligibility criteria one by one; **time zero** (the same event for both arms); look-back required before time zero; wash-out for new-user designs; end of follow-up and censoring rules; calendar period and why (coding stability, data availability from `CONTEXT.md`).

   **Round 3: variables.** For exposure, comparator, outcome, and each candidate confounder: role, clinical definition, when it is measured (before time zero only for confounders), and whether `CONTEXT.md` shows a plausible source. Draw the **DAG** in Mermaid, show it, and ask the user to add or remove arrows. Derive the minimal adjustment set; list the confounders that are **not measurable** (smoking, BMI, socio-economic status) because they drive the sensitivity analyses.

   **Round 4: biases.** Go through every bias in `epi-biases`. For each, state your verdict (concerned / not concerned, why) and the parade. Ask the user only where the verdict depends on a fact you cannot check (e.g. whether death outside the hospital is captured). Immortal time, confounding by indication and outcome misclassification must always have an explicit answer.

   **Round 5: size.** Compute the sample size or the minimum detectable effect in Python (formulas in `epi-designs` § 6) with the assumptions the user gives (baseline risk, expected effect, alpha, power, ratio of arms). Run the code, keep it and the result for the protocol.

   **Round 6: regulatory.** Apply the decision tree of `regulatory-fr`. Ask what the user already has (CSE opinion, HDH declaration, DPO registration) and fill the section with what is missing marked « à faire ».

4. Confirm the summary with the user.
5. Write `studies/<slug>/02-protocole.md` from `templates/02-protocole.md`. Every STROBE (or TRIPOD/STARD) methods item has content or an explicit « non applicable, car … ». The bias table has one row per bias in `epi-biases`. The DAG is a Mermaid block. The sample-size code is a fenced Python block followed by its output.
6. Update the study README; next step is `/define-phenotype`, then `/review-study 02-protocole.md` before any data work.

## Rules

- New-user design with an active comparator is the default for drug questions; a deviation is written with its reason.
- Time zero is written as one sentence that holds for both arms. If you cannot write that sentence, the design has immortal time.
- Confounders are measured before time zero. A variable measured after it is a mediator or a collider, and is listed as such, not adjusted for.
- Do not define codes in the protocol; reference `03-phenotypes.md` for each variable.
- Do not leave a section empty; write « à compléter : … » with what is missing and who decides.

Done when `02-protocole.md` is complete, the user has confirmed, and the README points to `/define-phenotype`.
