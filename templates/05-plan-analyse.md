---
etude: <slug>
document: 05-plan-analyse
version: 1
date: <AAAA-MM-JJ>
auteur: <nom, sinon « à compléter »>
statut: brouillon | relu | validé
produit_par: /analysis-plan
---

# Plan d'analyse statistique

*« Rédigé avant toute analyse ; tout écart ultérieur est consigné dans 06-rapport. »*

## Estimand

| Attribut | Valeur |
|---|---|
| Population | |
| Exposition (stratégies comparées) | |
| Critère de jugement | |
| Contraste | *« ITT-like / per-protocol-like ; HR, RR, différence de risque à t »* |
| Évènements intercurrents | *« Décès, changement de traitement, sortie du territoire : stratégie (traitement, composite, hypothétique, tant que…) »* |
| Mesure | |

## Données

- **Jeu de données** :
- **Snapshot** :
- **Variables dérivées** : *« Définition et code de chaque variable construite à partir des phénotypes. »*

## Analyse principale

- **Modèle** :
- **Covariables** : *« Mesurées avant le temps zéro uniquement ; issues du graphe causal. »*
- **Gestion du temps immortel** : *« Temps zéro identique pour les bras ; ou exposition dépendante du temps. »*
- **Hypothèses à vérifier** : *« Proportionnalité des risques (Schoenfeld), linéarité, absence de sur-dispersion… »*

## Contrôle de la confusion

- **Méthode** : score de propension / appariement / IPTW / ajustement direct
- **Modèle du score** :
- **Diagnostic d'équilibre** : *« Différences standardisées < 0,1 sur toutes les covariables ; graphique love plot. »*
- **Zone de support commun** :

## Données manquantes

*« Description par bras, mécanisme supposé, méthode (imputation multiple avec le critère dans le modèle, m imputations) ; analyse en cas complets en sensibilité. »*

## Analyses secondaires

*« Une par objectif secondaire de 02-protocole, même structure que l'analyse principale. »*

## Analyses de sensibilité

*« Une ligne par biais marqué « concerné » dans la section 9 du protocole. »*

| Analyse | Biais visé | Méthode | Interprétation attendue |
|---|---|---|---|
| | | | |

## Sous-groupes et interactions

*« Pré-spécifiés uniquement ; test d'interaction, pas de comparaison de p entre strates. »*

## Multiplicité

*« Un critère primaire ; correction appliquée ou absence de correction déclarée pour les secondaires. »*

## Logiciels et versions

| Logiciel / paquet | Version |
|---|---|
| Python | |
| | |

## Table shells

### Tableau 1 : caractéristiques de la population par bras

| Caractéristique | Bras exposé (n = ) | Bras comparateur (n = ) | Différence standardisée |
|---|---|---|---|
| Âge, moyenne (ET) | | | |
| Sexe féminin, n (%) | | | |
| | | | |

### Tableau 2 : résultats principaux

| Critère | Évènements / n, bras exposé | Évènements / n, bras comparateur | Mesure brute (IC 95 %) | Mesure ajustée (IC 95 %) |
|---|---|---|---|---|
| | | | | |

### Figure 1 : diagramme de flux

*« Repris de 04-faisabilite, mis à jour sur le jeu final. »*

### Figure 2 : courbes de Kaplan-Meier / incidence cumulée

*« Par bras, avec effectifs à risque sous l'axe ; incidence cumulée avec risques concurrents si le décès est un évènement intercurrent. »*

## Historique

| Date | Auteur | Modification |
|---|---|---|
| <AAAA-MM-JJ> | <auteur> | Création |
