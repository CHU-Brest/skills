# Étude « fluoroquinolones-infarctus »

**Statut (2026-09-02).** Question cadrée (`01-question.md`), protocole écrit (`02-protocole.md`), phénotypes définis (`03-phenotypes.md`) et plan d'analyse pré-spécifié (`05-plan-analyse.md`), tous en version 1, statut « brouillon ». `/analyze` a déjà été exécuté sur le jeu de données **synthétique** de `data/` : les scripts, le journal et les sorties sont dans `analyse/`. Étape suivante : `/report` pour assembler `06-rapport.md`, puis `/review-study 06-rapport.md`. Avant toute exécution sur données réelles : `/feasibility` (voir ci-dessous), `/review-study 02-protocole.md` et `/review-study 05-plan-analyse.md`.

**Investigateur principal** : à compléter. **Méthodologiste** : à compléter. **Référent EDS** : à compléter.

**Question** : chez les adultes ayant reçu une première prescription hospitalière d'antibiotique au CHU de Brest entre 2015 et 2024, l'initiation d'une fluoroquinolone augmente-t-elle le risque d'infarctus du myocarde dans les 60 jours, par rapport à l'initiation d'une bêta-lactamine ? Question analytique, cohorte de nouveaux utilisateurs avec comparateur actif, émulation d'essai cible, grille STROBE + RECORD.

## Ce dossier est un exemple travaillé

Ce dossier illustre ce que produisent les skills `/grill-question`, `/study-design`, `/define-phenotype` et `/analysis-plan` sur une question réelle. Deux différences avec un dossier d'étude ordinaire :

- **`04-faisabilite.md` est absent** : l'exemple n'a pas d'accès à l'entrepôt, aucune requête de comptage n'a été exécutée. Les effectifs cités dans le protocole (§ 10) et le plan sont des hypothèses ; sur données réelles, `/feasibility` doit être lancé avant `/analysis-plan` et ses effectifs remplacent les hypothèses.
- **`data/` contient un jeu de données SYNTHÉTIQUE**, `cohorte_synthetique.csv`, généré par `analyse/make_synthetic.py`. Aucune ligne ne correspond à un patient réel ; les colonnes suivent le dictionnaire de `data/README.md`, qui est aussi celui que la requête de cohorte de `03-phenotypes.md` produit. Dans un dossier d'étude réel, `data/` n'est jamais versionné (voir `.gitignore` et le skill `study-folder`).

`CONTEXT.md` est également absent : le modèle de données utilisé dans le SQL indicatif de `03-phenotypes.md` est hypothétique et signalé comme tel.

## Documents

| Fichier | Produit par | Contenu |
|---|---|---|
| `01-question.md` | `/grill-question` | Question typée, utilité, PECO, objectifs, hypothèses, mesures |
| `02-protocole.md` | `/study-design` | Schéma, essai cible, population, variables, biais, DAG, taille, réglementaire |
| `03-phenotypes.md` | `/define-phenotype` | Codes, règles temporelles, algorithmes, SQL indicatif, validation |
| `05-plan-analyse.md` | `/analysis-plan` | Estimand, modèle, IPTW, sensibilité, table shells |
| `analyse/` | `/analyze` | Scripts Python, `make_synthetic.py`, journal, sorties |
| `data/` | utilisateur | Jeu synthétique et son dictionnaire |
