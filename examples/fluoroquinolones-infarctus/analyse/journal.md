# Journal d'analyse

| Élément | Valeur |
|---|---|
| Étude | fluoroquinolones-infarctus |
| Date d'exécution | 2026-09-02 |
| Snapshot de l'EDS | sans objet : jeu de données **synthétique** |
| Extrait | `data/cohorte_synthetique.csv`, généré par `make_synthetic.py` (graine 20240901, n = 12 000) |
| Empreinte SHA-256 de l'extrait | `f5ca25e482908b94d0090b3201cf05bc6ceeb5d960cd3fc89e24f8d09c2e3a18` (à recalculer après toute régénération : `sha256sum data/cohorte_synthetique.csv`) |
| Environnement | Python 3.11, versions figées dans `requirements.txt` |
| Exécution | `python make_synthetic.py && python 10_import.py && python 30_table1.py && python 40_primary.py` |

## Objet de cet exemple

Vérifier que la chaîne `/analyze` (import validé, Tableau 1 avec différences standardisées, score de propension et IPTW, Cox pondéré, incidence cumulée, love plot, export des tableaux) s'exécute sans erreur sur un extrait conforme au dictionnaire de `data/README.md`. Le générateur simule une confusion par indication (les patients plus âgés, plus comorbides et plus sévères reçoivent plus souvent une fluoroquinolone) et un effet causal de HR = 1,4. Aucun résultat de ce dossier ne concerne des patients réels.

## Scripts exécutés

| Script | Rôle | Sorties |
|---|---|---|
| `make_synthetic.py` | Génère l'extrait synthétique | `data/cohorte_synthetique.csv` (non versionné) |
| `00_config.py` | Chemins, graine, seuil des petits effectifs, covariables du DAG | — |
| `10_import.py` | Validation contre le dictionnaire (identifiants uniques, dates, bornes, cohérence des évènements) | `output/10_validation.md`, `output/cohorte_validee.csv` (non versionné) |
| `30_table1.py` | Tableau 1 par bras, SMD avant pondération, cellules masquées | `output/30_table1.md`, `output/30_table1.csv` (non versionné) |
| `40_primary.py` | Score de propension, IPTW stabilisé tronqué (1er–99e percentile), équilibre, Cox brut et pondéré (erreurs robustes), test de Schoenfeld, incidence cumulée 1 − KM pondérée, différence de risque à 60 jours | `output/40_resultats.md`, `output/results.json`, `output/fig2_incidence_cumulee.{png,svg}`, `output/fig3_love_plot.{png,svg}`, `output/tables.md` |

Non exécutés dans l'exemple (à écrire sur l'extrait réel) : `20_flow.py` (diagramme de sélection : il n'y a pas de `04-faisabilite.md` dans cet exemple), `50_secondary.py`, `60_sensitivity.py`, `90_export.py` (l'export des tableaux est fait par `40_primary.py` faute d'analyses secondaires).

## Écarts au plan

| Écart | Pourquoi | Impact |
|---|---|---|
| Pas de diagramme de flux (`20_flow.py`) | L'extrait synthétique est déjà la cohorte finale ; aucune faisabilité à reproduire | Aucun sur le test de la chaîne ; obligatoire sur données réelles |
| Analyses secondaires et de sensibilité non exécutées | Hors périmètre du test à blanc | Le Tableau 3 du plan reste vide |
| Variance de l'incidence cumulée pondérée = variance naïve de lifelines | lifelines ne fournit pas d'estimateur robuste pour le KM pondéré ; les IC de la Figure 2 sont indicatifs | Sur données réelles : bootstrap (200 réplicats) pour l'IC de la différence de risque, comme prévu au plan |
| Non-linéarité de l'âge dans le score de propension (terme quadratique) | Ajout à la lecture du love plot sur la première exécution (SMD de l'âge > 0,1 avant, < 0,1 après) | Conforme au plan (« diagnostics d'équilibre puis enrichissement du modèle du score ») |

## Lecture critique des sorties

- Équilibre : 12 covariables avec |SMD| > 0,1 avant pondération, 0 après (Figure 3). Poids stabilisés entre 0,49 et 2,03 ; 2 % tronqués. Support commun satisfaisant (scores de propension entre 0,05 et 0,81 dans les deux bras).
- Effet : HR brut 2,43 (IC 95 % 1,81 à 3,27) ; HR pondéré 1,75 (IC 95 % 1,28 à 2,37). L'intervalle contient la valeur simulée (1,4) ; la surestimation résiduelle tient à la forme non linéaire du risque simulé (interactions non modélisées dans le score), ce qui illustre l'intérêt de l'analyse de sensibilité « ajustement direct en plus de l'IPTW » prévue au plan.
- Hypothèse de proportionnalité : p de Schoenfeld = 0,03 dans le modèle pondéré. Sur données réelles, ce signal impose de rapporter aussi la différence de risque à 60 jours (déjà prévue) et un HR par période (0–7 j, 8–60 j).
- Effectifs à risque à 60 jours affichés à 0 : artefact de la censure administrative exactement au jour 60 ; sans conséquence.
- Aucune cellule sous le seuil de 10 dans les sorties versionnées.

## Analyses exploratoires

Aucune.

## Historique

| Date | Auteur | Modification |
|---|---|---|
| 2026-09-02 | à compléter | Création, test à blanc sur données synthétiques |
