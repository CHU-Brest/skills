---
etude: fluoroquinolones-infarctus
document: 01-question
version: 1
date: 2026-09-02
auteur: à compléter
statut: brouillon
produit_par: /grill-question
---

# Question d'étude

## Question en une phrase

« Chez les adultes ayant reçu une première prescription hospitalière d'antibiotique au CHU de Brest entre 2015 et 2024, l'initiation d'une fluoroquinolone augmente-t-elle le risque d'infarctus du myocarde dans les 60 jours, par rapport à l'initiation d'une bêta-lactamine (amoxicilline ± acide clavulanique, céphalosporine de 3e génération) ? »

## Type de question

- [ ] Descriptive
- [x] Analytique (causale)
- [ ] Prédictive / pronostique
- [ ] Diagnostique
- [ ] Qualité des soins / processus

Justification : la question porte sur l'effet d'un traitement (initiation d'une fluoroquinolone) sur le risque d'un évènement clinique (infarctus du myocarde), par rapport à une alternative thérapeutique ; elle appelle une mesure d'association ajustée avec une interprétation causale, donc un schéma de cohorte émulant un essai cible. La formulation initiale de l'utilisateur (« est-ce que les fluoroquinolones donnent des infarctus ? ») contenait aussi une composante descriptive (« combien d'infarctus après fluoroquinolone ? ») ; elle a été classée secondaire et se lit dans l'incidence cumulée par bras.

## Utilité

Trois conséquences attendues de la réponse :

1. **Pharmacovigilance.** Les restrictions ANSM/EMA de 2019 sur les fluoroquinolones reposent sur les tendinopathies, les atteintes neurologiques et l'anévrisme aortique ; le signal cardiaque (infarctus, arythmie par allongement du QT) reste débattu, avec des cohortes taïwanaises et danoises discordantes (HR de 1,0 à 1,7 ; littérature, à vérifier). Un résultat local sur données de soins courants alimente ce signal.
2. **Bon usage des anti-infectieux au CHU.** La commission des anti-infectieux du CHU de Brest arbitre les recommandations de première intention (infections urinaires, pneumonies) ; un excès de risque cardiaque mesuré sur la population de l'établissement pèse dans l'arbitrage fluoroquinolone vs bêta-lactamine.
3. **Publication.** Étude mono-centrique sur EDS avec émulation d'essai cible, publiable si la validation des phénotypes est faite.

## PECO / PICOT

| Population | Exposition ou facteur | Comparateur | Critère de jugement | Temps | Lieu |
|---|---|---|---|---|---|
| Adultes (≥ 18 ans) ayant une première prescription hospitalière d'antibiotique d'un des deux groupes, validée par la pharmacie, sans antibiotique de l'un ou l'autre groupe dans les 180 jours précédents (nouveaux utilisateurs) et avec ≥ 2 ans d'historique observé dans l'EDS ; sans infarctus dans les 2 ans précédents | Initiation d'une fluoroquinolone systémique (orale ou IV) : ofloxacine, ciprofloxacine, norfloxacine, lévofloxacine, moxifloxacine | Initiation d'une bêta-lactamine systémique de même indication : amoxicilline, amoxicilline-acide clavulanique, céphalosporine de 3e génération | Infarctus du myocarde hospitalisé (séjour MCO avec DP I21.* ou I22.*) survenant entre J1 et J60 après le temps zéro ; définition étroite : avec troponine au-dessus du seuil du laboratoire dans les 48 h de l'admission | Inclusion du 2015-01-01 au 2024-12-31 ; suivi 60 jours ; fin de suivi 2025-03-01 | CHU de Brest, entrepôt de données de santé (PMSI MCO, prescriptions, biologie, décès) |

## Objectifs

- **Primaire** : estimer l'effet de l'initiation d'une fluoroquinolone, par rapport à l'initiation d'une bêta-lactamine comparatrice, sur le risque d'infarctus du myocarde à 60 jours, mesuré par le hazard ratio ajusté par pondération sur le score de propension (IPTW) et par la différence de risque à 60 jours.
- **Secondaires** :
  1. Estimer le même effet en analyse « per-protocol-like » (censure au changement de groupe d'antibiotique).
  2. Estimer l'effet sur le critère composite infarctus du myocarde ou décès à 60 jours.
  3. Estimer l'effet par indication (urinaire, respiratoire, autre) et par classe d'âge (< 65 ans, ≥ 65 ans), avec test d'interaction.
  4. Décrire l'incidence cumulée d'infarctus à 60 jours dans chaque bras (composante descriptive de la question initiale).

Tout ce qui n'est pas listé ici est exploratoire.

## Hypothèses

Hypothèse clinique : les fluoroquinolones augmentent le risque d'infarctus du myocarde à court terme, par allongement de l'intervalle QT et par dégradation du collagène de la paroi artérielle (mécanisme invoqué pour l'anévrisme aortique, extrapolé à l'instabilité de plaque). L'effet attendu est **aigu** (semaines), d'où l'horizon de 60 jours et l'absence de latence longue ; l'effet attendu est un HR d'environ 1,3 à 1,5 (littérature, à vérifier). L'hypothèse nulle (HR = 1) est plausible : les cohortes publiées sont discordantes et une partie de l'association pourrait relever de la confusion par indication (les fluoroquinolones sont prescrites à des patients plus graves ou allergiques aux bêta-lactamines).

## Mesures attendues

| Mesure | Dénominateur ou référence | Précision attendue |
|---|---|---|
| Hazard ratio ajusté (IPTW) fluoroquinolone vs bêta-lactamine, IDM à 60 j | Bras bêta-lactamine (référence) | IC 95 % ; largeur dépendante du nombre d'évènements, à quantifier dans 02-protocole § 10 (effet minimal détectable) |
| Différence de risque à 60 j (Kaplan-Meier pondéré) | Bras bêta-lactamine | IC 95 % par bootstrap ou variance de Greenwood pondérée |
| Incidence cumulée d'IDM à 60 j par bras | Patients inclus dans le bras, personnes-jours | IC 95 % ; effectifs < 10 masqués |
| HR per-protocol-like ; HR sur le composite IDM ou décès | Bras bêta-lactamine | IC 95 % |
| HR par sous-groupe (indication, âge) | Bras bêta-lactamine dans la strate | IC 95 % et p d'interaction |

## Données pressenties dans l'EDS

`CONTEXT.md` est absent dans cet exemple : les sources ci-dessous sont celles d'un EDS hospitalier générique, à confirmer dans 03-phenotypes puis 04-faisabilite.

| Concept | Source pressentie | Disponibilité présumée | À confirmer dans 03-phenotypes |
|---|---|---|---|
| Prescription hospitalière d'antibiotique (molécule, voie, dates) | Logiciel de prescription, prescriptions validées par la pharmacie, codées en UCD puis mappées en ATC | Bonne depuis 2015 pour les séjours MCO ; couverture des urgences et de l'ambulatoire à vérifier | oui |
| Prescriptions de ville (avant et après le séjour) | Aucune (pas de chaînage SNDS) | Absente : source de mauvaise classification de l'exposition | oui (limite documentée) |
| Infarctus du myocarde | PMSI MCO, DP I21.* / I22.* | Bonne ; extensions ATIH des codes à gérer | oui |
| Troponine | Résultats de biologie (LOINC ou code local), seuil du laboratoire | Bonne pour les séjours du CHU ; changement de dosage (troponine ultrasensible) au cours de la période à dater | oui |
| Décès | Table décès de l'EDS (décès intra-hospitaliers) ; statut vital INSEE si chaîné | Intra-hospitalier : bonne ; hors hôpital : à vérifier | oui |
| Comorbidités (diabète, HTA, dyslipidémie, coronaropathie, IRC, BPCO), Charlson | PMSI MCO, DP/DR/DAS des séjours du look-back | Sous-codage attendu des DAS chroniques | oui |
| Co-médications (statine, antiagrégant, corticoïde) | Prescriptions hospitalières du look-back et du séjour index | Partielle (prescriptions hospitalières seulement) | oui |
| Indication de l'antibiotique | DP du séjour index ; champ « indication » de la prescription s'il existe | DP : bonne ; champ indication : à vérifier | oui |
| Sévérité de l'infection index | Codes sepsis (A41, R65.*) du séjour index ; passage en réanimation (mouvements) | Bonne pour les mouvements ; codes sepsis dépendants du codage | oui |
| Recours aux soins | Nombre de séjours MCO dans les 2 ans (PMSI) | Bonne | oui |
| Tabac, IMC, niveau socio-économique | Absents ou en texte libre non exploité | Non mesurables (limite, E-value) | non |

## Grille de rapport applicable

STROBE (version combinée cohorte, 22 items) + RECORD (13 items), d'après `reporting-guidelines` ; le protocole ajoute le tableau d'émulation de l'essai cible (`epi-designs` § 3.2).

## Investigateurs et calendrier

| Rôle | Nom | Contact |
|---|---|---|
| Investigateur principal | à compléter | à compléter |
| Méthodologiste | à compléter | à compléter |
| Data scientist / EDS | à compléter | à compléter |

Calendrier (indicatif) : protocole et phénotypes en septembre 2026 ; avis du CSE de l'EDS et déclaration HDH en octobre 2026 ; faisabilité en novembre 2026 ; validation des phénotypes (relecture de dossiers) en décembre 2026 ; plan d'analyse relu en janvier 2027 ; analyse en février 2027 ; rapport en mars 2027.

## Historique

| Date | Auteur | Modification |
|---|---|---|
| 2026-09-02 | à compléter | Création |
