"""Configuration partagée par les scripts d'analyse (exemple fluoroquinolones-infarctus).

Chemins, graine aléatoire, seuil des petits effectifs, horizon de suivi.
Toutes les valeurs sont celles du plan d'analyse (05-plan-analyse.md).
"""
from pathlib import Path

ETUDE = "fluoroquinolones-infarctus"
ANALYSE_DIR = Path(__file__).resolve().parent
STUDY_DIR = ANALYSE_DIR.parent
DATA_DIR = STUDY_DIR / "data"
OUTPUT_DIR = ANALYSE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Extrait analysé (synthétique dans cet exemple : aucun patient réel)
EXTRACT = DATA_DIR / "cohorte_synthetique.csv"

SEED = 20240901
SNAPSHOT = "à compléter (exemple : données synthétiques)"
SMALL_CELL = 10          # effectifs < 10 masqués « <10 » (CONTEXT.md, valeur par défaut)
HORIZON_J = 60           # horizon de suivi du critère primaire, en jours

ARM_COL = "bras"
ARM_EXPOSED = "FQ"       # fluoroquinolone
ARM_COMPARATOR = "BL"    # bêta-lactamine (comparateur actif)
ARM_LABELS = {ARM_EXPOSED: "Fluoroquinolone", ARM_COMPARATOR: "Bêta-lactamine"}

# Covariables du score de propension (ensemble d'ajustement minimal du DAG, 02-protocole.md)
COVARIATES_CONTINUOUS = ["age", "charlson", "nb_sejours_2ans"]
COVARIATES_BINARY = [
    "diabete", "hta", "dyslipidemie", "coronaropathie", "irc", "bpco",
    "statine", "antiagregant", "corticoide", "sepsis", "rea",
]
COVARIATES_CATEGORICAL = ["sexe", "indication", "annee_t0"]

# Dictionnaire de l'extrait (data/README.md) : colonne -> type attendu
DICTIONARY = {
    "patient_id": "int", "bras": "cat", "date_t0": "date", "annee_t0": "int",
    "age": "int", "sexe": "cat", "indication": "cat",
    "diabete": "bin", "hta": "bin", "dyslipidemie": "bin", "coronaropathie": "bin",
    "irc": "bin", "bpco": "bin", "statine": "bin", "antiagregant": "bin",
    "corticoide": "bin", "sepsis": "bin", "rea": "bin",
    "charlson": "int", "nb_sejours_2ans": "int", "duree_prescription_j": "int",
    "evenement_idm": "bin", "deces_sans_idm": "bin", "delai_jours": "int",
    "switch_j": "int_nullable",
}


def mask(n: int) -> str:
    """Applique la règle du secret statistique à un effectif."""
    return f"<{SMALL_CELL}" if 0 < n < SMALL_CELL else str(n)
