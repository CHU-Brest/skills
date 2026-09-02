---
etude: <slug>
document: 02-protocole
version: 1
date: <AAAA-MM-JJ>
auteur: <nom, sinon « à compléter »>
statut: brouillon | relu | validé
produit_par: /study-design
---

# Protocole

*« Numérotation alignée sur les items 1 à 12 de STROBE (+ RECORD). Chaque décision prise dans 01-question est reprise, pas rediscutée. »*

## 1. Titre et résumé

*« Titre indiquant le schéma d'étude ; résumé de 150 mots maximum. »*

## 2. Contexte et justification

*« Indiquer l'état des connaissances, ce qui manque, et pourquoi l'EDS peut répondre. »*

## 3. Objectifs

- **Primaire** :
- **Secondaires** :

## 4. Schéma d'étude

*« Indiquer le schéma choisi (cohorte de nouveaux utilisateurs, transversal, cas-témoins niché, séries de cas auto-contrôlées, série temporelle interrompue…) et le justifier d'après le type de question. »*

*« Pour une question causale, remplir le tableau d'émulation de l'essai cible ; le supprimer sinon. »*

| Composante | Essai cible | Émulation dans l'EDS |
|---|---|---|
| Éligibilité | | |
| Stratégies comparées | | |
| Assignation | | |
| Temps zéro | | |
| Suivi | | |
| Critère de jugement | | |
| Contraste causal | | |
| Analyse | | |

## 5. Cadre

| Élément | Valeur |
|---|---|
| Établissement | |
| Période d'inclusion | |
| Fin de suivi | |
| Snapshot de l'EDS | |

## 6. Population

- **Critères d'inclusion** : *« Vérifiables au temps zéro uniquement. »*
- **Critères d'exclusion** :
- **Temps zéro** : *« Date à laquelle l'éligibilité est vérifiée et le bras assigné, identique pour tous les bras. »*
- **Look-back** : *« Durée d'historique observée exigée avant le temps zéro. »*
- **Wash-out** : *« Durée sans exposition ni évènement exigée avant le temps zéro. »*

## 7. Variables

| Variable | Rôle (exposition / critère / confondant / modificateur) | Définition opérationnelle | Référence vers 03-phenotypes |
|---|---|---|---|
| | | | |

## 8. Sources de données et mesure

*« Pour chaque variable, la source dans l'EDS (table, colonne), le moment de mesure par rapport au temps zéro, et la comparabilité entre bras. »*

## 9. Biais anticipés et parades

*« Parcourir la liste complète de epi-biases ; une ligne par biais, concerné ou non, avec la raison. Aucune ligne ne peut être omise. »*

| Biais | Concerné ? | Pourquoi | Parade | Quantification prévue |
|---|---|---|---|---|
| Sélection (référence hospitalière) | | | | |
| Troncature à gauche | | | | |
| Perte de vue hors territoire | | | | |
| Utilisateurs prévalents | | | | |
| Utilisateur en bonne santé | | | | |
| Mauvaise classification du critère | | | | |
| Mauvaise classification de l'exposition | | | | |
| Détection / surveillance | | | | |
| Protopathique | | | | |
| Dérive du codage | | | | |
| Temps immortel | | | | |
| Fenêtre temporelle | | | | |
| Temps non mesurable | | | | |
| Confusion par le temps calendaire | | | | |
| Confusion par indication | | | | |
| Confusion non mesurée | | | | |
| Collision / ajustement sur une conséquence | | | | |
| Comparaisons multiples | | | | |
| Données manquantes non aléatoires | | | | |
| Petits effectifs | | | | |

## 10. Taille d'étude

*« Indiquer les hypothèses (risque de base, effet attendu, alpha, puissance) ; coller le code Python et son résultat. Si la population de l'EDS est fixe, donner l'effet minimal détectable pour le n disponible. »*

```python
# calcul de taille d'étude
```

Résultat : *« Indiquer n par bras ou effet minimal détectable. »*

## 11. Variables quantitatives

*« Indiquer comment chaque variable quantitative est traitée : continue, catégorisée (seuils justifiés), transformée. »*

## 12. Méthodes statistiques

*« Résumé en un paragraphe : modèle principal, gestion de la confusion, données manquantes, analyses de sensibilité. Le détail est dans 05-plan-analyse. »*

## Graphe causal

*« Exposition, critère, et toute variable qui cause plausiblement les deux ; distinguer les confondants mesurables dans l'EDS de ceux qui ne le sont pas. »*

```mermaid
graph LR
```

## Aspects réglementaires et éthiques

- **Référentiel applicable** : *« MR-004, MR-005, ou autorisation CNIL spécifique. »*
- **Finalité** :
- **Données traitées et minimisation** :
- **Information des patients** : *« Modalité (note d'information, site web) et gestion de l'opposition. »*
- **Durée de conservation** :
- **Responsable de traitement et DPO** :
- **Avis du CSE** : *« Comité scientifique et éthique de l'EDS : date, numéro. »*
- **Déclaration HDH** : *« Répertoire public des études, date. »*
- **Sécurité** : *« Environnement d'analyse, export, journalisation. »*

## Calendrier et responsabilités

| Étape | Responsable | Échéance |
|---|---|---|
| Faisabilité | | |
| Plan d'analyse | | |
| Analyse | | |
| Rapport | | |

## Historique

| Date | Auteur | Modification |
|---|---|---|
| <AAAA-MM-JJ> | <auteur> | Création |
