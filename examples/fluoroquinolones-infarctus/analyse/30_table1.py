"""30 - Tableau 1 : caractéristiques à l'inclusion par bras, avec différences standardisées.

Lit output/cohorte_validee.csv, construit le Tableau 1 avec tableone (moyenne (ET)
ou médiane [IQR] pour les variables quantitatives, n (%) pour les binaires et
catégorielles), calcule les différences standardisées (SMD) FQ vs BL, masque
les cellules sous le seuil, et écrit output/30_table1.md et output/30_table1.csv.
"""
import re
from importlib import import_module

import pandas as pd
from tableone import TableOne

cfg = import_module("00_config")

LABELS = {
    "age": "Âge, années", "sexe": "Sexe", "indication": "Indication", "annee_t0": "Année du temps zéro",
    "diabete": "Diabète", "hta": "Hypertension artérielle", "dyslipidemie": "Dyslipidémie",
    "coronaropathie": "Coronaropathie (hors IDM)", "irc": "Insuffisance rénale chronique",
    "bpco": "BPCO", "statine": "Statine", "antiagregant": "Antiagrégant plaquettaire",
    "corticoide": "Corticoïde", "sepsis": "Sepsis au séjour index", "rea": "Passage en réanimation",
    "charlson": "Indice de Charlson", "nb_sejours_2ans": "Séjours dans les 2 ans",
    "duree_prescription_j": "Durée de prescription, jours",
}


def build_table1(df: pd.DataFrame) -> TableOne:
    columns = (cfg.COVARIATES_CONTINUOUS + ["duree_prescription_j"] + cfg.COVARIATES_BINARY
               + cfg.COVARIATES_CATEGORICAL)
    categorical = cfg.COVARIATES_BINARY + cfg.COVARIATES_CATEGORICAL
    nonnormal = ["charlson", "nb_sejours_2ans", "duree_prescription_j"]
    order = {c: ["1"] for c in cfg.COVARIATES_BINARY}   # modalité « oui » en premier
    limit = {c: 1 for c in cfg.COVARIATES_BINARY}     # n'afficher que cette modalité
    return TableOne(
        df, columns=columns, categorical=categorical, nonnormal=nonnormal, groupby=cfg.ARM_COL,
        pval=False, smd=True, order=order, limit=limit, rename=LABELS, decimals=1, missing=False,
        overall=True,
    )


def mask_cells(table: pd.DataFrame) -> pd.DataFrame:
    """Masque les n (%) dont l'effectif est sous le seuil ; laisse les moyennes intactes."""
    pattern = re.compile(r"^(\d+) \(")

    def f(cell):
        if isinstance(cell, str):
            m = pattern.match(cell)
            if m and 0 < int(m.group(1)) < cfg.SMALL_CELL:
                return f"<{cfg.SMALL_CELL} (masqué)"
        return cell

    return table.map(f)


if __name__ == "__main__":
    df = pd.read_csv(cfg.OUTPUT_DIR / "cohorte_validee.csv")
    t1 = build_table1(df)
    table = mask_cells(t1.tableone.copy())
    # Colonnes lisibles : « Grouped by bras » -> libellés des bras
    table.columns = [cfg.ARM_LABELS.get(c[1], c[1]) if isinstance(c, tuple) else c for c in table.columns]
    table.index = [" : ".join(str(x) for x in idx if str(x)) for idx in table.index]
    table.index = [i.replace(", mean (SD)", ", moyenne (ET)").replace(", median [Q1,Q3]", ", médiane [Q1, Q3]")
                   .replace(", n (%) : 1", ", n (%)") for i in table.index]
    table.columns = ["Ensemble" if c == "Overall" else c for c in table.columns]
    table.to_csv(cfg.OUTPUT_DIR / "30_table1.csv")
    md = ["# Tableau 1 : caractéristiques de la population par bras", "",
          "Moyenne (ET) ou médiane [Q1, Q3] pour les variables quantitatives ; n (%) sinon. "
          "SMD : différence standardisée fluoroquinolone vs bêta-lactamine (avant pondération). "
          f"Effectifs < {cfg.SMALL_CELL} masqués.", "", table.to_markdown(), ""]
    (cfg.OUTPUT_DIR / "30_table1.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))
    smd_col = [c for c in table.columns if "SMD" in str(c)]
    if smd_col:
        smd = pd.to_numeric(table[smd_col[0]], errors="coerce").abs()
        print(f"Covariables avec |SMD| > 0,1 avant pondération : {int((smd > 0.1).sum())}")
