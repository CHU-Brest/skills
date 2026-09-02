---
etude: cancer-colon-incidence
document: 01-question
version: 1
date: 2026-09-02
auteur: à compléter
statut: brouillon
produit_par: /grill-question
---

# Question d'étude

## Question en une phrase

« Parmi les patients ayant eu au moins un séjour MCO au CHU de Brest entre 2015 et 2024, combien ont un cancer colorectal, quelle est l'incidence annuelle des cas nouvellement pris en charge, la prévalence des cas suivis, et quelle est la répartition par âge et par sexe ? »

Souhait initial de l'utilisateur, tel qu'exprimé : « combien de patients ont un cancer du côlon ? incidence, prévalence, pyramide des âges ».

## Type de question

- [x] Descriptive
- [ ] Analytique (causale)
- [ ] Prédictive / pronostique
- [ ] Diagnostique
- [ ] Qualité des soins / processus

Justification : la question demande « combien », « quelle incidence », « quelle prévalence », « qui » (âge, sexe) et « quand » (par année). Il n'y a **aucune exposition** dont on voudrait estimer l'effet et **aucun comparateur** : rien n'est mis en regard d'autre chose pour en tirer une mesure d'association. L'évolution du nombre de cas entre 2017 et 2024 est une **tendance descriptive** (un comptage par année avec son intervalle de confiance), pas une question causale : on ne cherche pas à expliquer pourquoi le nombre varie, et aucune interprétation causale (effet du dépistage, de la pandémie de COVID-19, d'un changement d'organisation) ne sera revendiquée. Si une telle question apparaît, elle fera l'objet d'une étude séparée (série temporelle interrompue). La question n'est pas non plus prédictive (pas de score) ni diagnostique (pas de test index contre une référence).

## Utilité

Trois usages, énoncés par l'utilisateur pendant l'interview :

1. **Dimensionner la filière d'oncologie digestive** du CHU : nombre de dossiers présentés en réunion de concertation pluridisciplinaire (RCP), capacité d'endoscopie (coloscopies diagnostiques et de surveillance) et de chirurgie colorectale, en fonction du nombre annuel de nouveaux cas pris en charge et de leur répartition par âge.
2. **Répondre à une demande de la direction du CHU et à une sollicitation du registre des cancers du Finistère**, qui souhaitent connaître le nombre de cas vus au CHU par année et leur structure d'âge et de sexe, pour les mettre en regard de l'activité du territoire. La comparaison avec le territoire se fera dans la discussion, sans jamais présenter les effectifs du CHU comme une incidence de population.
3. **Servir de base à une étude analytique ultérieure** (par exemple les délais entre diagnostic et chirurgie, ou entre RCP et premier traitement) : la population de cas incidents et la définition du temps zéro construites ici seront réutilisées telles quelles.

## PECO / PICOT

| Population | Exposition ou facteur | Comparateur | Critère de jugement | Temps | Lieu |
|---|---|---|---|---|---|
| Patients de tout âge ayant eu au moins un séjour MCO (hospitalisation complète, ambulatoire ou séance) au CHU de Brest entre le 2015-01-01 et le 2024-12-31 ; c'est une population **hospitalière**, pas la population du Finistère | Condition comptée : **cancer colorectal** (tumeur maligne du côlon, de la jonction recto-sigmoïdienne ou du rectum), avec le cancer du côlon seul en unité secondaire ; il n'y a pas d'exposition au sens causal | **Aucun** ; les comparaisons entre années, tranches d'âge et sexes sont descriptives | Nombre de cas incidents par année civile ; prévalence annuelle des cas suivis ; âge au diagnostic et sexe des cas incidents ; en secondaire, confirmation chirurgicale ou anatomopathologique et mode d'entrée par les urgences | Période d'observation 2015-01-01 → 2024-12-31 ; les cas incidents sont comptés de **2017 à 2024**, les années 2015–2016 servant de look-back de deux ans | CHU de Brest, séjours et séances MCO enregistrés dans l'entrepôt de données de santé |

### Décisions prises pendant l'interview

Résumé des rounds de `grilling`, confirmé par l'utilisateur ; chaque décision est reprise sans être rediscutée dans `02-protocole.md`.

**Round 1 : type et utilité.**
1. Question de type descriptif (voir ci-dessus) ; le souhait « incidence, prévalence, pyramide des âges » ne contient pas de question causale cachée.
2. Utilité : dimensionnement de la filière, réponse à la direction et au registre, base d'une étude analytique ultérieure.
3. Investigateur et échéance : à compléter.

**Round 2 : PECO.**
4. Population : patients avec au moins un séjour MCO au CHU de Brest sur la période ; tous âges (le cancer colorectal avant 40 ans est rare mais existe, et une pyramide des âges tronquée serait moins utile) ; l'utilisateur a explicitement reconnu qu'il s'agit d'une population hospitalière.
5. Unité clinique primaire : **cancer colorectal** (côlon, jonction recto-sigmoïdienne, rectum), unité habituelle des registres et de la cartographie des pathologies de la Cnam ; **côlon seul** en unité secondaire, parce que le souhait initial disait « côlon » et que la filière chirurgicale distingue côlon et rectum. Le cancer de l'appendice (côlon, sous-site appendice) reste inclus dans le colorectal ; la question d'exclure ce sous-site sera reposée dans `/define-phenotype`.
6. Comparateur : aucun.
7. Critère : le cancer tel qu'un clinicien le confirmerait, c'est-à-dire par une histologie ou une exérèse ; dans l'entrepôt, le cancer sera d'abord identifié par ses codes de séjour, et la confirmation par acte de colectomie ou compte rendu d'anatomopathologie sera la définition étroite.
8. Temps : 2015–2024, dix années disponibles ; les deux premières années sont consommées par le look-back.

**Round 3 : spécifique au descriptif.**
9. **Cas incident** (« nouvellement pris en charge ») : premier séjour MCO portant un code de la liste, sans aucun code de la liste dans les deux années précédentes, et avec au moins deux années d'historique observé (n'importe quel contact avec le CHU) avant ce séjour ; sans cet historique, le cas est indéterminé (tronqué à gauche) et n'est pas compté comme incident.
10. **Cas prévalent suivi** : au moins un séjour ou une séance portant un code de la liste dans l'année civile ; les séances (chimiothérapie, radiothérapie) comptent pour la prévalence mais ne créent pas de nouveau cas.
11. **Positions des codes** : diagnostic principal (DP) ou diagnostic relié (DR) en définition primaire ; toute position, diagnostics associés (DAS) compris, en définition large de sensibilité.
12. **Dénominateurs** : (a) patients ayant au moins un séjour MCO au CHU dans l'année (population hospitalière annuelle) pour les proportions ; (b) population du Finistère (INSEE) **uniquement** pour une mise en perspective dans la discussion, jamais comme dénominateur d'un taux, parce que le CHU ne voit qu'une partie des cas du territoire (cliniques privées de Brest pratiquant la chirurgie colorectale, autres établissements du département).
13. **Pyramide des âges** : âge au diagnostic (au temps zéro) des cas incidents, tranches de cinq ans, par sexe ; cellules de moins de dix patients masquées, années regroupées si nécessaire.
14. **Tendance** : nombre de cas incidents par année de 2017 à 2024, avec un contrôle de la dérive du codage (tendance de l'ensemble des codes du chapitre C des tumeurs malignes).
15. **Mesures secondaires** : proportion de cas confirmés par chirurgie ou anatomopathologie ; proportion de cas dont le premier séjour est une admission par les urgences (mode d'entrée), indicateur d'un diagnostic tardif ou en urgence.

**Round 4 : disponibilité des données (faits).** `CONTEXT.md` n'existait pas ; l'utilisateur a accepté de poursuivre sans lui. Les sources ci-dessous sont donc présumées d'après les conventions PMSI (référence `terminologies`) et à confirmer.

## Objectifs

- **Primaire** : dénombrer, pour chaque année civile de 2017 à 2024, les patients ayant un cancer colorectal nouvellement pris en charge au CHU de Brest (cas incidents selon la définition du round 3), avec un intervalle de confiance à 95 % de Poisson, et rapporter ce nombre à la population hospitalière de l'année.
- **Secondaires** :
  1. Prévalence annuelle des cas suivis (au moins un séjour ou une séance avec un code de la liste dans l'année), rapportée à la population hospitalière de l'année, 2015–2024.
  2. Répartition des cas incidents par tranche d'âge de cinq ans et par sexe (pyramide des âges), âge médian, sex-ratio, années 2017–2024 regroupées.
  3. Tendance du nombre annuel de cas incidents 2017–2024, avec contrôle de la dérive du codage.
  4. Mêmes mesures pour le cancer du côlon seul (C18.*), puis pour le rectum et la jonction recto-sigmoïdienne par différence.
  5. Proportion de cas incidents confirmés par un acte de colectomie ou un compte rendu d'anatomopathologie (définition étroite).
  6. Proportion de cas incidents dont le premier séjour est une admission par les urgences.
  7. Mise en perspective avec l'incidence publiée pour le Finistère (registre, INSEE), en discussion seulement.

Tout ce qui n'est pas dans cette liste est exploratoire.

## Hypothèses

Aucune hypothèse causale : la question est descriptive. Attentes d'ordre de grandeur, utiles pour lire les résultats et non pour les tester : quelques centaines de cas incidents par an au CHU (à confirmer dans `04-faisabilite.md`) ; âge médian au diagnostic autour de 70 ans et légère prédominance masculine, comme dans les registres français ; creux du nombre de cas en 2020 lié à la pandémie de COVID-19 (moins de coloscopies et de dépistages), suivi d'un rattrapage ; part croissante de cas chez les moins de 50 ans, décrite dans la littérature internationale, qui restera peut-être invisible à l'échelle d'un seul CHU (petits effectifs).

## Mesures attendues

| Mesure | Dénominateur ou référence | Précision attendue |
|---|---|---|
| Nombre de cas incidents par année civile, 2017–2024 | Aucun (comptage) ; IC 95 % exact de Poisson | Demi-largeur relative d'environ ± 12 % pour 300 cas dans l'année (calcul dans `02-protocole.md` § 10) |
| Proportion de cas incidents parmi les patients avec ≥ 1 séjour MCO dans l'année | Population hospitalière annuelle | IC 95 % de Wilson ; ± 0,03 point pour une proportion de 0,3 % sur 100 000 patients (hypothèse) |
| Prévalence annuelle des cas suivis, 2015–2024 | Population hospitalière annuelle | IC 95 % de Wilson |
| Pyramide des âges des cas incidents (tranches de 5 ans × sexe) | Cas incidents 2017–2024 regroupés | Effectifs bruts ; cellules < 10 masquées ; regroupement des tranches jeunes si nécessaire |
| Âge médian au diagnostic, sex-ratio | Cas incidents | Médiane et intervalle interquartile ; ratio hommes/femmes |
| Tendance annuelle 2017–2024 | Régression de Poisson sur l'année, contrôle par l'ensemble des codes du chapitre C | Variation annuelle moyenne en % avec IC 95 % |
| Proportion de cas confirmés (colectomie CCAM ou anatomopathologie) | Cas incidents | IC 95 % de Wilson ; ± 5,5 points pour 60 % de 300 cas |
| Proportion de cas incidents admis par les urgences | Cas incidents | IC 95 % de Wilson ; ± 4,5 points pour 20 % de 300 cas |
| Mise en perspective avec l'incidence du Finistère | Registre des cancers du Finistère, population INSEE | Pas de taux calculé ; comparaison qualitative en discussion |

## Données pressenties dans l'EDS

`CONTEXT.md` étant absent, les sources sont présumées d'après les conventions PMSI de la référence `terminologies` ; toutes sont à confirmer dans `03-phenotypes.md` (tables, colonnes, format des codes) et `04-faisabilite.md` (complétude par année).

| Concept | Source pressentie | Disponibilité présumée | À confirmer dans 03-phenotypes |
|---|---|---|---|
| Séjours MCO et séances, avec dates d'entrée et de sortie | PMSI MCO (RSS), un enregistrement par séjour | Élevée : le MCO est le champ le mieux codé | oui |
| Diagnostics de séjour (DP, DR, DAS) en CIM-10 FR | PMSI MCO (RUM/RSS), codes avec ou sans point selon l'entrepôt | Élevée ; la version CIM-10 ATIH change chaque année | oui |
| Séances de chimiothérapie ou radiothérapie avec le cancer en DR | PMSI MCO, séjours en séance (Z51.1, Z51.0 en DP, à vérifier) | Élevée | oui |
| Actes de colectomie et de proctectomie (confirmation) | Actes CCAM du RSS | Élevée pour les actes réalisés au CHU | oui |
| Compte rendu d'anatomopathologie (confirmation) | Système d'anatomopathologie, codes ADICAP ou texte libre | Incertaine : dépend de l'intégration du système dans l'entrepôt | oui |
| Âge à l'entrée, sexe | PMSI MCO | Élevée, rarement manquants | oui |
| Mode d'entrée et provenance (urgences, transfert, domicile) | PMSI MCO | Élevée | oui |
| Identifiant patient chaîné entre séjours et années | Table patients de l'entrepôt (IPP pseudonymisé) | Élevée ; à vérifier : fusions d'identifiants | oui |
| Tout contact avec le CHU (pour le look-back) | Séjours MCO, consultations externes, passages aux urgences | Séjours : élevée ; consultations et urgences : à vérifier | oui |
| Commune de résidence (Finistère ou non) | Code géographique de résidence du PMSI | Élevée, au niveau du code géographique PMSI et non de la commune exacte | oui |
| Statut vital | Décès intra-hospitalier (mode de sortie) ; chaînage INSEE incertain | Partielle ; non nécessaire au primaire | non |
| Versions CIM-10 ATIH et règles de codage par année | Guide méthodologique ATIH de chaque année | Externe à l'entrepôt ; à documenter | oui |

## Grille de rapport applicable

**STROBE** (version combinée, cohorte pour l'incidence et la tendance, transversale répétée pour la prévalence) **complétée par RECORD** (extension pour les données de soins courants), telles que paraphrasées dans `skills/reference/reporting-guidelines/checklists/strobe.md` et `record.md`. Items particulièrement attendus : STROBE 5 (date de début de l'entrepôt et snapshot, troncature à gauche), RECORD 6.1 et 7.1 (codes et algorithme complets), RECORD 12.2 (nettoyage : identifiants fusionnés, séjours en cours au snapshot), RECORD 19.1 (données non créées pour la recherche : codage orienté par la facturation).

## Investigateurs et calendrier

| Rôle | Nom | Contact |
|---|---|---|
| Investigateur principal | à compléter (oncologie digestive, gastro-entérologie ou chirurgie digestive) | à compléter |
| Méthodologiste | à compléter | à compléter |
| Data scientist / EDS | à compléter (équipe de l'entrepôt de données de santé du CHU de Brest) | à compléter |

Calendrier : protocole (`02-protocole.md`) rédigé le 2026-09-02 ; relecture méthodologique (`/review-study`) et dépôt au comité scientifique et éthique de l'EDS : à compléter ; phénotypes (`03-phenotypes.md`) : à compléter ; faisabilité (`04-faisabilite.md`), qui tient lieu de résultats pour cette question descriptive : après déclaration au Health Data Hub, à compléter ; rapport (`06-rapport.md`) : à compléter. Échéance demandée par la direction et le registre : à compléter.

## Historique

| Date | Auteur | Modification |
|---|---|---|
| 2026-09-02 | à compléter | Création |
