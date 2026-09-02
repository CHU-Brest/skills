---
name: setup-eds-skills
description: One-time setup of a working directory for EDS studies - interview to build CONTEXT.md (data sources, data model, coding conventions, privacy rules, optional SQL connection, glossary), create studies/ and the .gitignore. Run once per repository before the first /grill-question.
disable-model-invocation: true
---

All produced documents are written in **French**.

`CONTEXT.md` is the shared language between the warehouse and every skill. Skills read it instead of asking the user the same questions in every study.

## Steps

1. Check the working directory: if `CONTEXT.md` exists, read it and switch to update mode (only ask about what is missing or marked « à compléter »).
2. **Facts first.** Look for anything that already describes the warehouse: a data dictionary, DDL files, a schema export, existing SQL, a README. Read them and pre-fill the model from them; do not ask the user to retype what a file already says.
3. Run `grilling` on what remains:

   **Round 1: identity.** Hospital, who is responsible for the EDS, current snapshot date, period covered, order of magnitude of patients and stays, analysis environment (where code runs, whether Python is available there, whether internet is).

   **Round 2: sources.** For each source (PMSI MCO / SSR / HAD / psychiatry, prescriptions, administrations, laboratory, imaging reports, clinical notes, movements, vital status, community data if linked), whether it exists, its period, its granularity, and its known weaknesses. Ask specifically: is death outside the hospital known (INSEE linkage)? are community prescriptions available (SNDS linkage)? is anatomopathology structured?

   **Round 3: data model.** For each source: table name, primary key, patient identifier, stay identifier, date columns, code columns and their terminology, join keys to the patient table, and one known pitfall. If the user cannot answer table by table, record what they know and mark the rest « à compléter par l'équipe EDS ».

   **Round 4: conventions and rules.** ICD-10 version handling (ATIH year), position columns for DP/DR/DAS, drug coding (ATC, UCD, CIP), lab units and reference ranges, small-cell threshold for outputs (recommend 10), export rules, retention.

   **Round 5: connection (optional).** SQL engine, host, schema, authentication mode, the tool skills should use (a Python driver, an MCP server). Default is « non configuré »; explain that `/feasibility` runs its queries automatically once this is filled, and that credentials never go in the file (reference an environment variable).

4. Write `CONTEXT.md` from `templates/CONTEXT.md`, with the glossary seeded and extended with the terms that came up.
5. Create `studies/` with a `.gitkeep`, and add to `.gitignore`:
   ```
   studies/*/data/
   studies/*/analyse/output/*.csv
   studies/*/analyse/output/*.parquet
   .venv/
   ```
6. Tell the user the next step: `/grill-question` for the first study, and that `CONTEXT.md` is meant to be corrected by the EDS team over time (each skill that finds an error in it should propose a fix).

Done when `CONTEXT.md` exists with no section left silently empty (missing knowledge is marked « à compléter »), `studies/` and the `.gitignore` are in place.
