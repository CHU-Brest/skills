---
name: grilling
description: Interview the user relentlessly about a research question, protocol or analysis decision until nothing is left implicit. Use when a study skill needs decisions from the user, or when the user says "grill me", "cuisine-moi", "challenge ma question".
---

Interview the user until you reach a **shared understanding**. Map the subject as a **design tree**: every decision branches into the decisions that hang off it (the study type decides the design, the design decides the exposure definition, the exposure definition decides the codes, and so on).

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask *now* without guessing at answers you have not heard yet. Ask the whole frontier in one round, numbered, each with your recommended answer. Then stop and wait for the user.

Format a round like so (questions and recommendations are written in **French**):

```
❓ **Q1** - **<titre de la question>** : <corps de la question, éventuellement plusieurs paragraphes ou un choix multiple>

➡️ <votre réponse recommandée, avec la raison en une phrase>

---

❓ **Q2** - ...
```

Rules:

- **Facts are your job, decisions are the user's.** If a question can be answered by reading a file in the study folder, `CONTEXT.md`, a terminology, a reporting checklist or the literature, find the answer yourself (dispatch a sub-agent if it takes more than one lookup) and do not ask. Put every genuine *decision* to the user and wait.
- **Never re-ask what is already settled.** Before the first round, read the study folder (see `study-folder`) and treat every recorded decision as answered.
- **One round, one frontier.** A question whose answer depends on another question still open in this round belongs to a later round.
- **Always recommend.** A question without a recommendation forces the user to think from scratch; a recommendation lets them accept or correct in one word.
- **Name the trade-off.** When two options are defensible (a broader phenotype with better sensitivity vs a narrower one with better positive predictive value), say what each costs.
- **Push back once.** If the user's answer contradicts something recorded earlier or a known methodological rule (e.g. an exposure window that creates immortal time), say so in one sentence and offer the alternative. Their second answer is final.

Each round the user answers reshapes the tree: settled decisions push the frontier outward. Recompute the frontier and ask the next round.

Done when the frontier is empty: every branch visited, nothing silently assumed. Summarise the settled decisions as a numbered list in French and ask the user to confirm before the calling skill writes its document.
