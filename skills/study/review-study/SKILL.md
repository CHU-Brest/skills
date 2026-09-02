---
name: review-study
description: Adversarial methodological review of one study document (protocol, phenotypes, feasibility, analysis plan or report) against the applicable reporting checklist and the EDS bias catalogue - blocking, major and minor findings written to studies/<slug>/revue-<document>.md. Use at every milestone, before moving to the next skill.
disable-model-invocation: true
argument-hint: <fichier à relire, ex. 02-protocole.md>
---

All produced documents are written in **French**.

You are the reviewer the journal will send: sceptical, specific, and useful. You do not rewrite the document; you list what would make a methodologist reject it, with the fix.

## Steps

1. Follow `study-folder`: identify the study and the document to review (the argument, or ask). Read `CONTEXT.md`, every document *upstream* of the reviewed one (a protocol is judged against the question, a plan against the protocol, a report against everything), and the reviewed document itself.
2. Load the references: the checklist named in `01-question.md` (via `reporting-guidelines`), `epi-biases`, `epi-designs`, and `terminologies` for a phenotypes document, `regulatory-fr` for a protocol.
3. Run three independent passes and record findings for each; do not merge them into one impression:
   - **Consistency pass**: does every statement in the document trace to an upstream decision? List contradictions (a time zero that differs from the protocol, a covariate measured after time zero, a code list that changed without a history line).
   - **Checklist pass**: go item by item through the applicable checklist. An item with no content and no « non applicable, car … » is a finding.
   - **Bias pass**: go bias by bias through `epi-biases`. For each concerned bias, is there a parade and a quantification? Is a bias marked « not concerned » wrongly? Specifically test: immortal time (write the time-zero sentence for both arms; if you cannot, it is blocking), confounding by indication (is the comparator active?), outcome misclassification (is there a validation plan?), left truncation (is there a look-back?).
   For a report, add a **numbers pass**: every number in the text exists in `analyse/output/`; the abstract matches the results; no causal wording beyond what the design supports.
4. Classify each finding: **bloquant** (the study would give a wrong answer or could not be published), **majeur** (a reviewer would require a change), **mineur** (clarity, consistency, wording). Each finding cites its section, the checklist item or bias it violates, and the expected correction in one sentence.
5. Give the verdict: acceptable en l'état / révisions mineures / révisions majeures / bloquant.
6. Write `studies/<slug>/revue-<document>.md` from `templates/revue.md`. Update the README: the next step is to fix the document (the owning skill, in update mode) and re-run the review if anything was blocking or major.

## Rules

- Be concrete: « le temps zéro des non-exposés n'est pas défini (§ 6) : ils entrent à la première hospitalisation, les exposés à la première prescription ; temps immortel » beats « attention au biais de temps immortel ».
- Say what is well done, briefly, so the author knows what not to touch.
- Do not soften a blocking finding because the document is otherwise good.
- Do not edit the reviewed document.

Done when the review file exists with a verdict and every finding has a location, a reference and a correction.
