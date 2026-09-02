# Étude « cancer-colon-incidence »

**Statut au 2026-09-02.** Dossier d'étude pour une question **descriptive** : incidence, prévalence et répartition par âge et par sexe du cancer colorectal chez les patients du CHU de Brest, 2015–2024. Existent : `01-question.md` (question typée, PECO, objectifs, mesures attendues ; produit par `/grill-question`) et `02-protocole.md` (protocole allégé pour une question descriptive : schéma, cadre, population, variables, tableau complet des biais, précision attendue, aspects réglementaires ; produit par `/study-design`). **Prochaine étape** : `/define-phenotype` pour écrire `03-phenotypes.md` (listes de codes exactes avec libellés et positions, règles temporelles, algorithme, SQL indicatif, plan de validation par relecture de dossiers), puis `/feasibility`, dont les tableaux (flux de sélection, effectifs par année, âge × sexe, qualité des données) **sont les résultats** d'une question descriptive, puis `/report`. `/review-study 02-protocole.md` est recommandé avant tout travail sur les données. Investigateur principal : à compléter.

Ce dossier est l'**exemple travaillé du flux descriptif** décrit dans le README du dépôt (`/grill-question` → `/study-design` allégé → `/define-phenotype` → `/feasibility` → `/report`). Il a été écrit sans `CONTEXT.md` (l'utilisateur a accepté de poursuivre sans description de l'entrepôt) : les sources de données sont présumées d'après les conventions PMSI de la référence `terminologies` et doivent être confirmées dans `03-phenotypes.md` et `04-faisabilite.md`. Les codes CIM-10 et CCAM cités sont marqués « à vérifier » tant qu'ils n'ont pas été contrôlés dans les référentiels ATIH.

## Documents

| Document | Produit par | État |
|---|---|---|
| `01-question.md` | `/grill-question` | brouillon, version 1 |
| `02-protocole.md` | `/study-design` | brouillon, version 1 |
| `03-phenotypes.md` | `/define-phenotype` | à faire |
| `04-faisabilite.md` | `/feasibility` | à faire |
| `06-rapport.md` | `/report` | à faire |

## Pièces réglementaires

| Pièce | État |
|---|---|
| Cadre applicable (MR-004) confirmé par le DPO | à faire |
| Avis du comité scientifique et éthique de l'EDS | à faire |
| Inscription au registre des traitements du DPO | à faire |
| Note d'information des patients (note individuelle et page du site web du CHU) | à vérifier auprès du DPO |
| Déclaration au répertoire public du Health Data Hub | à faire, avant toute requête sur données individuelles |

Aucune requête de `/feasibility` sur données individuelles ne doit être lancée avant que la déclaration au Health Data Hub soit faite ou que le DPO ait confirmé que les comptages demandés relèvent de la formalité propre de l'entrepôt.
