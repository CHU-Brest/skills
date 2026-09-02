---
name: terminologies
description: French health terminologies and PMSI coding conventions (CIM-10 ATIH, ATC, CCAM, NABM, LOINC, GHM) for defining phenotypes in a hospital data warehouse. Use when a skill needs exact codes, code positions, or must explain what a code in the warehouse actually means.
---

# Terminologies and PMSI conventions

A code in the warehouse is not a clinical fact: it is an entry made by someone, in a given terminology version, for a given purpose (mostly billing). This skill says which terminology codes what, where it shows up in an EDS, and how to write a code list that another person can check. Real code lists go into `03-phenotypes.md` (see `study-folder`) and are written in French.

Which terminologies the CHU's EDS actually stores, in which column and with which formatting, is in `CONTEXT.md`. When it disagrees with this skill, `CONTEXT.md` wins.

## Terminologies

| Terminology | Codes what | Structure | Where it appears in an EDS | Main pitfalls |
|---|---|---|---|---|
| **CIM-10 FR (ATIH)** | Diagnoses (PMSI MCO, SMR, psychiatry, HAD) | Letter + 2 digits, optional 4th character after the dot (`C18.7`), and ATIH-only extensions to a 5th/6th character on some categories | PMSI: DP, DR, DAS of each RUM/RSS; sometimes also in the EHR problem list | French version differs from ICD-10-CM; annual version; codes stored with or without the dot (`I21.0` vs `I210`); extensions break exact matching |
| **ATC (OMS)** | Drugs by anatomical/therapeutic/chemical class | 5 levels: `C` → `C10` → `C10A` → `C10AA` → `C10AA05` (statins → atorvastatin) | Prescription and administration systems, often via a local drug code mapped to ATC | Hospital prescriptions are coded in UCD or CIP, not ATC: the mapping is a step to document; one substance can have several ATC codes (route, combination) |
| **CCAM** | Medical and surgical procedures (actes techniques) | 7 characters: 4 letters + 3 digits, e.g. `DZQM006` = échographie-doppler transthoracique du cœur; letters 1–2 = topography, 3 = action, 4 = technique/approach; plus activité, phase, modificateurs | PMSI RSS (actes) and the operating-room / activity systems | Only *technical* procedures; consultations are NGAP, not CCAM; "descriptive" CCAM in PMSI vs "tarifante" version; codes must be checked in the CCAM reference (ATIH/Ameli), never guessed |
| **NABM** | Biology procedures for billing (nomenclature des actes de biologie médicale) | Numeric codes with a coefficient B | Billing of external biology; rarely the lab result tables | Codes an *act*, not a result; do not use it to find values |
| **LOINC** | Lab observations (and some clinical measures) | Numeric code with check digit, e.g. `2160-0` creatinine (à vérifier in the local catalogue) | Lab results in warehouses whose LIS is mapped to LOINC; else local lab codes | Several LOINC codes for one analyte (method, specimen, units); mapping coverage is partial; units must be checked, never assumed |
| **GHM** | Groupes homogènes de malades: output of the PMSI grouping of an MCO stay | 6 characters: CMD (2 digits) + type (`C` surgical, `M` medical, `K` interventional, `Z` undifferentiated) + number (2 digits) + severity (1–4) or `J`/`T`/`Z` for ambulatory / very short / unsegmented (other letters exist, see the manual) | PMSI RSS/RSA, one per stay | Not a diagnosis; depends on the grouping version (changes yearly); useful as a severity proxy (level 1–4) and for cost |
| **CSARR** | Rehabilitation acts in SMR (ex-SSR) | Alphanumeric catalogue specific to SMR | PMSI SMR (RHS) | Not comparable to CCAM; SMR diagnosis coding uses CIM-10 with a different structure (manifestation morbide principale, affection étiologique, finalité) |
| **RIM-P / CIM-10** | Psychiatry stays and acts | CIM-10 diagnoses (chapter F mostly), EDGAR acts in ambulatory psychiatry | PMSI psychiatry | Diagnosis coding often less exhaustive; sector-based organisation |
| **ADICAP** | Anatomopathology (organ, technique, lesion) | Alphanumeric, 8 positions | Pathology system, when integrated in the EDS | Rarely structured; often only in free-text reports |
| **UCD / CIP** | Drugs: UCD (unité commune de dispensation, hospital), CIP (community presentation) | 7 digits (UCD), 13 digits (CIP-13) | Hospital pharmacy, prescription, administration | Need a mapping table to ATC (BDPM, Thériaque, local pharmacy table); document its version |

### CIM-10 FR: what "French version" means

- ATIH publishes the **CIM-10 FR à usage PMSI** every year (new version with the March PMSI campaign; check the exact date for each year). Codes appear, disappear or change meaning; record which version was in force during the study period, and beware that a stay is coded with the version of *its* year (see "coding drift" in `epi-biases`).
- It is **not ICD-10-CM** (United States). ICD-10-CM has up to 7 characters and subcodes that do not exist in France. Example for acute myocardial infarction: ICD-10-CM has `I21.01`, `I21.02`, `I21.A1` (type 2 MI), `I21.B`; ATIH has `I21.0`–`I21.4`, `I21.9` and its **own extensions**: a 5th character for the type of care (`I21.x0` prise en charge initiale, `I21.x8` autre prise en charge) and a 6th character for duration (`I21.x00` infarctus de 24 heures ou moins). The full list is in the ATIH annex "codes de la CIM-10 étendus"; check it before writing an exact-match list.
- The **ICD-10 MCP server** available in some sessions serves ICD-10-CM/PCS. It is fine for finding a category and its English label; every code then has to be checked against the ATIH version (libellé, existence, extensions) before entering a phenotype. Say so in the code list's `source` column.
- Other French particularities: dagger/asterisk pairs (`†` étiologie / `*` manifestation) that produce two codes for one condition; Z codes used as DP for sessions and follow-up; a warehouse may store the code with the dot, without it, or padded, so **prefix matching must be done on the normalised string**.

## PMSI conventions

- **RUM** (résumé d'unité médicale): one per medical unit visited during a stay. **RSS** (résumé de sortie standardisé): the set of RUMs of one stay; the hospital's EDS holds RSS with unit, dates and identifiers. **RSA**: the anonymised RSS sent to ATIH, which is what the SNDS contains. Published SNDS algorithms are written on RSA; check that the EDS field names map to them.
- **DP** (diagnostic principal): the condition that **mobilised the main part of the care effort during the stay**, not the patient's main disease. A diabetic admitted for a hip fracture has DP = fracture; diabetes may or may not be a DAS. In a multi-RUM stay the DP of the RSS is selected by the grouping rules from the RUMs' DPs, not by clinical importance.
- **DR** (diagnostic relié): used only when the DP is a Z code (or similar) that does not express the disease: chemotherapy session `Z51.1` with DR = the cancer; dialysis `Z49.*`; radiotherapy `Z51.0`. A cancer phenotype that ignores the DR misses most chemotherapy sessions.
- **DAS** (diagnostics associés significatifs): conditions that required care or changed the management during the stay. **Chronic conditions appear as DAS inconsistently**: coding is driven by their effect on the GHM severity level (CMA list), so a comorbidity is more likely coded when it "pays" and by units that code carefully. Absence of a DAS is weak evidence of absence of the disease.
- **Séances** (sessions): stays of less than a day for chemotherapy, dialysis, radiotherapy, transfusion, coded with a Z DP and a DR. They inflate stay counts: count them separately or require one full hospitalisation.
- **Guide méthodologique** (ATIH): the coding rules change every year (published for the March campaign). A rule valid in 2019 may not hold in 2024; cite the guide of the study years.
- MCO is the best-coded field. SMR, psychiatry and HAD have their own summaries and rules; do not reuse an MCO phenotype there without checking.

### What a phenotype definition must specify

Every phenotype in `03-phenotypes.md` states the five items below; a definition missing one of them cannot be programmed nor reviewed.

1. **Code list** — the exact codes or prefixes, with libellés (table format below).
2. **Accepted positions** — `DP seul` / `DP ou DR` / `DP, DR ou DAS` (any position); for procedures and drugs, the source system.
3. **Count required** — 1 stay, ≥ 2 stays, ≥ 2 occurrences separated by ≥ 30 days, etc.
4. **Time window** — look-back before time zero (e.g. 2 years for incidence), follow-up window for outcomes, and how sessions are counted.
5. **Confirming source** — procedure (CCAM), lab (LOINC/local), pathology, drug, or "aucune" (state it), with the expected PPV if a validation exists.

## Code-list writing rules

- List codes as a Markdown table with columns **code | libellé | position acceptée | source**. Add a `version` line above the table (terminology, version year, date checked).
- Use **explicit prefix notation**: write `C18.* = tous les codes commençant par C18` once, then use `C18.*`. Never rely on an implicit "and subcodes".
- Prefer prefixes to exhaustive lists where the ATIH extensions make exact matching fragile (`I21.*` rather than `I21.0, I21.1, …`), and say why.
- Cite the **published validated algorithm** when one exists, with its PPV/sensitivity and population. Good starting points, public and documented: the Cnam **cartographie des pathologies** (SNDS algorithms for ~60 conditions), the REDSIAM working groups, ATIH coding fascicles, HAS/INCa definitions for cancers. Adapt them (they are written on RSA and on community dispensing) and say what was changed.
- Record the **terminology version and date** for every table, and the mapping table used for UCD/CIP → ATC.
- **Never state a code as certain if it was not checked** in the reference of the terminology (ATIH CIM-10 FR, CCAM, WHO ATC index). Mark unchecked codes `à vérifier` in the `source` column, and keep the mark until someone has checked. A code found only through the ICD-10-CM server counts as unchecked.
- Do not paste codes from memory into an analysis script: the script reads the table in `03-phenotypes.md` (or a CSV derived from it), so that the list is checked once.

## Worked examples

Both examples are written the way they would appear in `03-phenotypes.md` (French, table, five items). Codes marked `à vérifier` were not checked against the ATIH/WHO references at writing time.

### Cancer du côlon (phénotype d'événement)

Version : CIM-10 FR ATIH, année du séjour ; CCAM version de l'année ; date de vérification : à compléter.

| Code | Libellé | Position acceptée | Source |
|---|---|---|---|
| `C18.*` | Tumeur maligne du côlon (C18.0 cæcum à C18.9 côlon SAI) | DP, DR ou DAS | CIM-10 FR, à vérifier |
| `C19` | Tumeur maligne de la jonction recto-sigmoïdienne | DP, DR ou DAS | CIM-10 FR, à vérifier |
| `C20` | Tumeur maligne du rectum | DP, DR ou DAS | CIM-10 FR, à vérifier |
| `Z51.1` avec DR ∈ liste ci-dessus | Séance de chimiothérapie pour tumeur | DP (séance) + DR | CIM-10 FR |
| Codes CCAM de colectomie | Exérèse du côlon (sous-chapitre côlon de la CCAM) | Acte du séjour | CCAM, codes exacts à vérifier dans le référentiel |

Decisions the user must take, not the skill:

- **Côlon vs colorectal**: `C18.*` alone is colon; adding `C19` and `C20` gives colorectal, the usual epidemiological unit (Cnam cartographie and registries mostly use C18–C20). `C18.1` (appendix) is sometimes excluded. State the choice and its reason.
- **Positions**: `DP ou DR` gives specific stays for the cancer (surgery, chemotherapy sessions); adding `DAS` catches cancers mentioned during stays for something else, at the cost of specificity. Recommend the primary definition `DP ou DR`, and `any position` as the broad sensitivity definition.
- **Incident case**: first stay with a code of the list, with **no code of the list in the previous 2 years** and at least 2 years of observed history (any contact) before that stay; otherwise the case is prevalent or left-truncated (`epi-biases`).
- **Confirmation**: a CCAM colectomy code within ±6 months, or a pathology record (ADICAP or report) of colonic adenocarcinoma when the pathology system is in the EDS; the confirmed subset is the narrow definition. Cancer registries (Finistère has one, access to be checked) are the gold standard if a matching is authorised (see `regulatory-fr`).

### Exposition aux fluoroquinolones et infarctus du myocarde

Version : ATC OMS index de l'année ; table de correspondance UCD → ATC de la pharmacie (version à noter) ; CIM-10 FR ATIH.

Exposition :

| Code | Libellé | Position acceptée | Source |
|---|---|---|---|
| `J01MA.*` | Fluoroquinolones (tous) | Prescription hospitalière validée (ou administration si disponible) | ATC OMS |
| `J01MA01` | Ofloxacine | idem | ATC OMS |
| `J01MA02` | Ciprofloxacine | idem | ATC OMS |
| `J01MA06` | Norfloxacine | idem | ATC OMS |
| `J01MA12` | Lévofloxacine | idem | ATC OMS |
| `J01MA14` | Moxifloxacine | idem | ATC OMS |

Comparateurs actifs (même indication, effet cardiaque non attendu), to be restricted to the chosen indication:

| Code | Libellé | Indication comparable | Source |
|---|---|---|---|
| `J01CA04` | Amoxicilline | infections respiratoires, urinaires | ATC OMS |
| `J01CR02` | Amoxicilline + acide clavulanique | idem | ATC OMS |
| `J01DD.*` | Céphalosporines de 3e génération (ex. `J01DD04` ceftriaxone, `J01DD08` céfixime) | infections urinaires, respiratoires | ATC OMS |
| `J01EE01` | Sulfaméthoxazole + triméthoprime (cotrimoxazole) | infections urinaires | ATC OMS |
| `J01XX01` | Fosfomycine | cystite | ATC OMS, à vérifier |
| `J01XE01` | Nitrofurantoïne | cystite | ATC OMS, à vérifier |

Note: cotrimoxazole is `J01EE01`; `J01EA` is trimethoprim alone and `J01XX` is "other antibacterials" (fosfomycin), so neither is a synonym for cotrimoxazole. Exposure rules to state: new-user (no antibiotic of either group in the previous 6 months), exposure window = prescription days + grace period (e.g. 7 days), time zero = first prescription date, and the fact that **community prescriptions are not seen** (misclassification, `epi-biases`).

Critère de jugement :

| Code | Libellé | Position acceptée | Source |
|---|---|---|---|
| `I21.*` | Infarctus aigu du myocarde (toutes extensions ATIH incluses) | DP | CIM-10 FR |
| `I22.*` | Infarctus du myocarde à répétition | DP | CIM-10 FR |
| Troponine élevée | Résultat de laboratoire (code LOINC ou code local, seuil du laboratoire) | dans les 48 h du séjour | LIS, code et seuil à vérifier dans `CONTEXT.md` |

`DP` only: a myocardial infarction that mobilised the stay. Confirmation: troponin above the lab's threshold during the stay (narrow definition); state the lag (ignore events in the first 0–7 days if protopathic bias is suspected) and the follow-up window (e.g. 60 days after time zero).

## How skills use this list

- `/define-phenotype` → one table per phenotype with the five items; codes not checked against the reference stay marked `à vérifier`.
- `/study-design` → the section « Définition des variables » references the phenotype tables and the terminology versions.
- `/analysis-plan` → narrow vs broad definitions become sensitivity analyses; the analysis script reads the code table rather than hard-coding codes.
- `/review-study` → check that every code list has libellés, positions, count, window, confirming source, version, and that no code is stated as certain without a source.
