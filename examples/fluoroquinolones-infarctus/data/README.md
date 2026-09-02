# Données de l'étude « fluoroquinolones-infarctus »

**Ce dossier ne contient jamais de données réelles.** Dans un dossier d'étude ordinaire, `data/` reçoit l'extrait fourni par l'équipe EDS et n'est jamais versionné (`.gitignore`, skill `study-folder`). Ici, il contient uniquement un jeu **synthétique**.

## `cohorte_synthetique.csv`

Généré par `../analyse/make_synthetic.py` (graine 20240901). Une ligne par patient, une cohorte fictive de nouveaux utilisateurs FQ vs BL dont les distributions imitent les hypothèses du protocole (§ 10) : aucune ligne ne correspond à un patient réel, aucun identifiant, aucune date n'a de contrepartie dans l'EDS. Le fichier sert à tester `/analyze` et à illustrer les table shells de `05-plan-analyse.md`.

Les colonnes sont exactement celles que produit la requête de cohorte de `03-phenotypes.md` (bloc « Cohorte finale ») et que les scripts de `analyse/` attendent.

## Dictionnaire des données

| Colonne | Type | Définition | Phénotype (03-phenotypes.md) |
|---|---|---|---|
| `patient_id` | entier | Pseudonyme du patient, unique dans le fichier | — |
| `bras` | texte : `FQ` ou `BL` | Bras assigné au temps zéro : `FQ` = fluoroquinolone, `BL` = bêta-lactamine comparatrice | Exposition ; Comparateur |
| `date_t0` | date `AAAA-MM-JJ` | Temps zéro : date de début de la première prescription hospitalière validée de l'antibiotique index | Critères d'éligibilité |
| `annee_t0` | entier | Année civile de `date_t0` (2015 à 2024) | — |
| `age` | entier | Âge en années révolues à `date_t0` (≥ 18) | Critères d'éligibilité |
| `sexe` | texte : `F` ou `M` | Sexe administratif | — |
| `indication` | texte : `urinaire`, `respiratoire`, `autre` | Indication de l'antibiotique index | Indication |
| `diabete` | 0/1 | Diabète (E10–E14) codé dans le look-back de 2 ans ou sur le séjour index avant T0 | Comorbidités CIM-10 |
| `hta` | 0/1 | Hypertension artérielle (I10–I15) | Comorbidités CIM-10 |
| `dyslipidemie` | 0/1 | Dyslipidémie (E78) | Comorbidités CIM-10 |
| `coronaropathie` | 0/1 | Coronaropathie hors infarctus (I20, I25) | Comorbidités CIM-10 |
| `irc` | 0/1 | Insuffisance rénale chronique (N18) | Comorbidités CIM-10 |
| `bpco` | 0/1 | BPCO (J44), proxy du tabagisme | Comorbidités CIM-10 |
| `statine` | 0/1 | Prescription hospitalière de statine (C10AA) dans le look-back ou à T0 | Co-médications |
| `antiagregant` | 0/1 | Prescription hospitalière d'antiagrégant plaquettaire (B01AC) | Co-médications |
| `corticoide` | 0/1 | Prescription hospitalière de corticoïde systémique (H02AB) | Co-médications |
| `sepsis` | 0/1 | Code de sepsis (A41.*, R65.*) sur le séjour index | Sévérité de l'infection index |
| `rea` | 0/1 | Passage en réanimation ou soins intensifs débuté au plus tard le jour de T0 | Sévérité de l'infection index |
| `charlson` | entier | Indice de Charlson (Quan 2011) calculé sur le look-back de 2 ans | Comorbidités CIM-10 |
| `nb_sejours_2ans` | entier | Nombre de séjours MCO (hors séances) dans les 2 ans avant T0, séjour index exclu | Recours aux soins |
| `duree_prescription_j` | entier | Durée en jours de la prescription index (date_fin − date_debut + 1) | Exposition ; Comparateur |
| `evenement_idm` | 0/1 | Infarctus du myocarde (définition principale) entre J1 et J60 après T0 | Infarctus du myocarde |
| `deces_sans_idm` | 0/1 | Décès sans infarctus préalable entre J1 et J60 (évènement intercurrent) | Décès |
| `delai_jours` | entier, 1 à 60 | Délai depuis T0 jusqu'au premier des évènements : IDM, décès, dernier contact, J60 | — |
| `switch_j` | entier ou vide | Jour (depuis T0) de la première prescription de l'autre groupe d'antibiotique dans les 60 jours ; vide si aucun changement | Exposition ; Comparateur |

Toutes les variables de confusion (`diabete` à `nb_sejours_2ans`) sont mesurées **avant ou au temps zéro** ; l'absence de code vaut 0 (voir « Données manquantes » dans `05-plan-analyse.md`).
