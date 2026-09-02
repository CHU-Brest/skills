---
document: CONTEXT
version: 1
date: <AAAA-MM-JJ>
auteur: <nom, sinon « à compléter »>
statut: brouillon | relu | validé
produit_par: /setup-eds-skills
---

# Contexte de l'EDS

*« Ce document décrit l'entrepôt tel qu'il est réellement, pas tel qu'il devrait être. Toute étude le lit en premier ; chaque piège connu y a sa place. »*

## Identité

| Élément | Valeur |
|---|---|
| Établissement | *« Indiquer le nom et le type d'établissement (CHU, CH, ESPIC…) »* |
| Responsable de l'EDS | *« Indiquer le nom, la fonction et le contact »* |
| Date du snapshot courant | *« Indiquer la date du dernier chargement (AAAA-MM-JJ) »* |
| Période couverte | *« Indiquer la première et la dernière date de données exploitables »* |
| Volumétrie patients | *« Indiquer le nombre de patients distincts »* |
| Volumétrie séjours | *« Indiquer le nombre de séjours (MCO / SSR / PSY / HAD) »* |

## Sources de données

*« Une ligne par source. La colonne fiabilité connue résume ce que les utilisateurs de l'EDS savent déjà (retards de codage, ruptures, doublons). »*

| Source | Contenu | Période | Granularité | Fiabilité connue |
|---|---|---|---|---|
| PMSI MCO | | | séjour / RUM | |
| PMSI SSR | | | semaine | |
| PMSI PSY (RIM-P) | | | séquence | |
| Prescriptions | | | ligne de prescription | |
| Administrations | | | administration horodatée | |
| Biologie | | | résultat d'analyse | |
| Comptes rendus texte | | | document | |
| Mouvements | | | passage par unité | |
| Décès | | | patient | |

## Modèle de données

*« Un bloc par table. Reprendre les noms exacts du schéma ; le champ pièges est le plus important. »*

### Table : `<nom>`

| Élément | Valeur |
|---|---|
| Clé | *« Indiquer la clé primaire »* |
| Colonnes clés | *« Lister les colonnes utiles aux études, avec leur type et leur signification »* |
| Liens vers les autres tables | *« Indiquer les clés étrangères et les jointures usuelles »* |
| Pièges | *« Indiquer les doublons, valeurs sentinelles, dates approximatives, changements de format »* |

## Conventions de codage

| Élément | Convention en vigueur |
|---|---|
| CIM-10 | *« Indiquer la version ATIH et les dates de changement de version »* |
| Positions diagnostiques | *« Indiquer comment DP / DR / DAS sont stockés (colonne, valeurs) et au niveau RUM ou RSS »* |
| Actes | *« Indiquer CCAM, version, position »* |
| Médicaments | *« Indiquer si le codage est ATC, UCD, CIP, ou plusieurs ; table de correspondance disponible ? »* |
| Unités de biologie | *« Indiquer les unités par défaut et les conversions connues (mg/L vs mmol/L…) »* |
| Dates | *« Indiquer la précision (jour, heure), le fuseau, et les dates fictives »* |

## Règles de confidentialité

| Règle | Valeur |
|---|---|
| Seuil des petits effectifs | *« Indiquer le seuil de masquage (défaut : effectifs < 10 affichés « <10 ») »* |
| Environnement d'analyse | *« Indiquer où les données patient peuvent être manipulées (bulle sécurisée, poste dédié…) »* |
| Export | *« Indiquer ce qui peut sortir de l'environnement (agrégats seulement, validation par qui) »* |
| Pseudonymisation | *« Indiquer le mécanisme et ce qui reste identifiant (dates exactes, codes postaux) »* |

## Connexion

*« Non configuré par défaut. Ne jamais écrire de mot de passe ici. »*

| Élément | Valeur |
|---|---|
| Moteur SQL | non configuré |
| Hôte | non configuré |
| Schéma | non configuré |
| Mode d'accès | non configuré (agent / humain qui exécute les requêtes) |

```yaml
# Exemple (commenté) :
# moteur: postgresql
# hote: eds-db.interne.chu.fr
# port: 5432
# base: eds
# schema: omop
# mode_acces: humain   # l'agent écrit les requêtes, un humain les exécute et colle les résultats
```

## Glossaire

*« Compléter et corriger selon l'usage local. Les synonymes servent à retrouver le bon terme dans les questions des cliniciens. »*

| Terme | Définition | Synonymes |
|---|---|---|
| Séjour | Hospitalisation complète d'un patient dans l'établissement, de l'entrée à la sortie | hospitalisation, RSS (en MCO) |
| RUM | Résumé d'unité médicale : fragment du séjour correspondant au passage dans une unité | résumé d'UM |
| RSS | Résumé de sortie standardisé : ensemble des RUM d'un séjour MCO | séjour MCO |
| DP | Diagnostic principal : motif ayant mobilisé l'essentiel des soins du RUM | diagnostic principal |
| DR | Diagnostic relié : précise le DP quand celui-ci est un code Z | diagnostic relié |
| DAS | Diagnostic associé significatif : comorbidité ou complication ayant eu un impact sur la prise en charge | diagnostic associé, comorbidité codée |
| GHM | Groupe homogène de malades : classe médico-économique du séjour | groupage |
| UM | Unité médicale : unité de soins identifiée dans le PMSI | service, unité |
| Patient index | Patient de la cohorte à partir duquel le suivi est compté | patient inclus, cas index |
| Nouvel utilisateur | Patient sans exposition au traitement pendant la période de wash-out précédant le temps zéro | new user, initiateur |
| Temps zéro | Date à laquelle l'éligibilité est vérifiée et le bras assigné ; début du suivi | date index, T0, baseline |
| Petit effectif | Cellule d'un tableau dont l'effectif est inférieur au seuil de confidentialité et doit être masquée | small cell, effectif masqué |
| Look-back | Durée d'historique observée exigée avant le temps zéro | période d'observation antérieure |
| Wash-out | Période sans exposition ni évènement exigée avant le temps zéro | période de lavage |

## Historique

| Date | Auteur | Modification |
|---|---|---|
| <AAAA-MM-JJ> | <auteur> | Création |
