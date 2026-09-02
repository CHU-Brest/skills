# Skills EDS du CHU de Brest

Des skills pour agents de code (Claude Code, et tout agent compatible avec le format `SKILL.md`) qui mènent une **étude scientifique sur l'entrepôt de données de santé (EDS)** de bout en bout : cadrer la question, écrire le protocole, définir les phénotypes, vérifier la faisabilité, pré-spécifier l'analyse, l'exécuter en Python, rédiger le rapport, et le faire relire.

La méthode est adaptée de [mattpocock/skills](https://github.com/mattpocock/skills) : des skills **petits et composables**, des skills **invoqués par l'utilisateur** (`/grill-question`) qui orchestrent des **primitives invoquées par le modèle** (`grilling`, `epi-biases`), un **routeur** (`/ask-eds`) qui décrit les flux, un **`CONTEXT.md`** comme vocabulaire partagé, et une **trace écrite** à chaque étape.

Les instructions des skills sont en anglais (le modèle les lit mieux). **Tout ce qu'ils produisent est en français.**

## Pourquoi

Quatre façons classiques de rater une étude sur EDS, et le skill qui les vise :

1. **La question est floue.** « Est-ce que les fluoroquinolones donnent des infarctus ? » n'est pas une question d'étude. `/grill-question` cuisine l'utilisateur jusqu'à obtenir population, exposition, comparateur, critère, période, et le *type* de question (descriptive, analytique, prédictive, diagnostique, qualité), dont tout le reste découle.
2. **Le schéma crée le biais.** Temps immortel, confusion par indication, troncature à gauche : ces biais naissent dans le protocole. `/study-design` impose l'émulation d'essai cible et passe le catalogue `epi-biases` en revue, biais par biais.
3. **Le code n'est pas le diagnostic.** Un `C18` en DAS d'un séjour n'est pas un cancer du côlon incident. `/define-phenotype` écrit des listes de codes exactes, des règles temporelles et un plan de validation.
4. **Le résultat n'est pas reproductible.** `/analysis-plan` fixe l'analyse avant de voir les données ; `/analyze` l'exécute en scripts numérotés et journalise chaque écart ; `/report` remplit la grille STROBE/RECORD ; `/review-study` relit comme un reviewer de revue.

## Installation

**Plugin Claude Code** (géré, mise à jour automatique) :

```
/plugin marketplace add CHU-Brest/skills
/plugin install chu-brest-eds-skills@chu-brest
```

**Autres agents, ou version modifiable** :

```
npx skills@latest add CHU-Brest/skills
```

Puis, une fois par répertoire de travail : `/setup-eds-skills`.

## Le flux : question → rapport

```
/setup-eds-skills      une fois : décrit l'entrepôt dans CONTEXT.md
        │
/grill-question   ──▶  studies/<slug>/01-question.md      la question typée, en PECO
        │
/study-design     ──▶  02-protocole.md                   schéma, essai cible, temps zéro, DAG, biais, taille, réglementaire
        │
/define-phenotype ──▶  03-phenotypes.md                  codes, règles temporelles, SQL indicatif, validation
        │
/feasibility      ──▶  04-faisabilite.md                 diagramme de sélection, effectifs, qualité, go / no-go
        │
/analysis-plan    ──▶  05-plan-analyse.md                estimand, modèle, sensibilité, table shells
        │
/analyze          ──▶  analyse/                          scripts Python, tableaux, figures, journal des écarts
        │
/report           ──▶  06-rapport.md                     IMRaD, grille remplie, résumé et abstract
        
/review-study <doc> ─▶ revue-<doc>.md                    à chaque jalon
```

Chaque skill relit les documents précédents du dossier d'étude et écrit le suivant : une étude se reprend dans une nouvelle session sans rien réexpliquer. `/ask-eds` explique où vous en êtes et quoi lancer.

Une question **descriptive** (incidence, prévalence, pyramide des âges) s'arrête souvent à `/feasibility`, dont les tableaux sont les résultats, puis passe à `/report`.

## Les skills

### Étude (invoqués par l'utilisateur)

| Skill | Produit | Rôle |
|---|---|---|
| `/ask-eds` | une réponse | Routeur : quel skill pour ma situation |
| `/setup-eds-skills` | `CONTEXT.md` | Décrit l'entrepôt : sources, modèle, conventions de codage, seuil des petits effectifs, connexion SQL optionnelle, glossaire |
| `/grill-question` | `01-question.md` | Cadre la question par interview : type, utilité, PECO, objectifs, grille de rapport |
| `/study-design` | `02-protocole.md` | Protocole : schéma, tableau d'émulation d'essai cible, temps zéro, variables, DAG, biais et parades, taille d'étude, aspects réglementaires |
| `/define-phenotype` | `03-phenotypes.md` | Phénotypes calculables : codes et positions, règles temporelles, algorithme, SQL indicatif, plan de validation |
| `/feasibility` | `04-faisabilite.md` | Exploration descriptive : flux de sélection, effectifs, qualité des données, décision |
| `/analysis-plan` | `05-plan-analyse.md` | Plan d'analyse pré-spécifié : estimand, modèle, confusion, données manquantes, sensibilité, table shells |
| `/analyze` | `analyse/` | Exécution Python reproductible sur l'extrait fourni |
| `/report` | `06-rapport.md` | Rapport IMRaD, checklist remplie, limites par biais résiduel, résumés |
| `/review-study` | `revue-<doc>.md` | Relecture méthodologique adversariale : bloquant, majeur, mineur |

### Références (invoquées par le modèle)

| Skill | Contenu |
|---|---|
| `grilling` | La primitive d'interview : rounds, frontière, les faits sont pour l'agent, les décisions pour l'utilisateur |
| `study-folder` | Convention du dossier `studies/<slug>/`, en-têtes YAML, hygiène des données |
| `epi-designs` | Type de question → schéma → mesure ; tableau d'essai cible ; taille d'échantillon |
| `epi-biases` | Catalogue des biais en données de soins courants, avec exemple EDS, parade et quantification |
| `reporting-guidelines` | STROBE, RECORD, TRIPOD, STARD, et comment remplir la grille |
| `terminologies` | CIM-10 ATIH, ATC, CCAM, NABM, LOINC, conventions PMSI, règles d'écriture des listes de codes |
| `regulatory-fr` | RGPD, référentiel EDS, MR-004, CSE, Health Data Hub, information des patients |

## Accès aux données

Les skills n'ont pas besoin d'accès direct à l'entrepôt. `/feasibility` écrit les requêtes de comptage, l'utilisateur les exécute dans l'environnement sécurisé et colle les agrégats. `/analyze` travaille sur un extrait déposé dans `studies/<slug>/data/` (jamais versionné).

Quand la section `## Connexion` de `CONTEXT.md` est renseignée, `/feasibility` exécute ses requêtes lui-même. Uniquement des `SELECT` agrégés ; aucune ligne patient ne transite par la conversation ; les effectifs sous le seuil sont masqués.

## Glossaire

- **Grilling** : interview serrée par séries de questions numérotées, chacune avec une réponse recommandée, jusqu'à ce que rien ne reste implicite.
- **EDS** : entrepôt de données de santé. **PMSI** : programme de médicalisation des systèmes d'information. **DP / DR / DAS** : diagnostic principal, relié, associé. **RUM / RSS** : résumés d'unité médicale et de sortie standardisé. **GHM** : groupe homogène de malades.
- **PECO / PICOT** : Population, Exposition ou Intervention, Comparateur, Outcome (critère de jugement), Temps.
- **IMRaD** : Introduction, Méthodes, Résultats, Discussion.
- **STROBE** : grille des études observationnelles. **RECORD** : son extension pour les données de soins courants. **TRIPOD** : grille des modèles de prédiction. **STARD** : grille des études diagnostiques.
- **HR / OR / RR** : hazard ratio, odds ratio, risque relatif. **IPTW** : pondération par l'inverse de la probabilité de traitement. **E-value** : force qu'un confondant non mesuré devrait avoir pour annuler le résultat.
- **DAG** : graphe causal exposition, critère, confondants.
- **Émulation d'essai cible** : concevoir l'étude observationnelle comme l'essai randomisé idéal. **Biais de temps immortel** : période où l'évènement est impossible comptée à tort dans un bras. **Nouvel utilisateur** : patient sans exposition pendant la fenêtre de wash-out avant le temps zéro. **Comparateur actif** : traitement de la même indication, pour limiter la confusion par indication.
- **Phénotype** : définition calculable d'un concept clinique à partir des données de l'entrepôt. **VPP** : valeur prédictive positive d'un phénotype.
- **Cadre Kahn** : qualité des données en conformité, complétude, plausibilité.
- **CIM-10, ATC, CCAM, NABM, LOINC** : terminologies des diagnostics, médicaments, actes, biologie.
- **MR-004** : méthodologie de référence CNIL pour la recherche sur données sans consentement individuel. **CSE** : comité scientifique et éthique de l'EDS. **HDH** : Health Data Hub.
- **Estimand** : quantité précise à estimer, fixée avant l'analyse. **Table shells** : tableaux vides préparés avant de voir les données.

## Exemples

`examples/` contient deux dossiers d'étude remplis à partir des questions qui ont motivé ce dépôt :

- `fluoroquinolones-infarctus/` : question analytique, cohorte de nouveaux utilisateurs avec comparateur actif, jusqu'au plan d'analyse et un jeu de données synthétique pour tester `/analyze`.
- `cancer-colon-incidence/` : question descriptive, jusqu'au protocole.

## Contribuer

`scripts/check-skills.sh` vérifie les frontmatters, les références croisées entre skills, gabarits et checklists. Les skills sont faits pour être modifiés : si un skill pose une question dont la réponse est dans `CONTEXT.md`, corrigez le skill.

Licence MIT. Méthode et primitive `grilling` adaptées de [mattpocock/skills](https://github.com/mattpocock/skills) (MIT).
