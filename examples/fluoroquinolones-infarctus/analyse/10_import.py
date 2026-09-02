"""10 - Import et validation de l'extrait contre le dictionnaire des données.

Charge data/cohorte_synthetique.csv, type les colonnes, vérifie les règles
dures (identifiants uniques, dates valides, âges plausibles, délais dans
l'horizon, cohérence des indicateurs d'évènement) et écrit un rapport de
validation. S'arrête (code de sortie 1) sur une violation dure.
Sortie : output/10_validation.md, output/cohorte_validee.csv (jamais versionné).
"""
import sys
from importlib import import_module

import pandas as pd

cfg = import_module("00_config")


def load() -> pd.DataFrame:
    if not cfg.EXTRACT.exists():
        sys.exit(f"Extrait absent : {cfg.EXTRACT}. Générer un jeu synthétique avec make_synthetic.py.")
    df = pd.read_csv(cfg.EXTRACT, dtype={"switch_j": "Int64"})
    df["date_t0"] = pd.to_datetime(df["date_t0"], format="%Y-%m-%d", errors="coerce")
    return df


def validate(df: pd.DataFrame) -> tuple[list[str], list[str]]:
    hard, soft = [], []
    missing = [c for c in cfg.DICTIONARY if c not in df.columns]
    extra = [c for c in df.columns if c not in cfg.DICTIONARY]
    if missing:
        hard.append(f"Colonnes manquantes : {missing}")
    if extra:
        soft.append(f"Colonnes hors dictionnaire (ignorées) : {extra}")
    if missing:
        return hard, soft

    if df["patient_id"].duplicated().any():
        hard.append("patient_id dupliqués")
    if df["date_t0"].isna().any():
        hard.append(f"{df['date_t0'].isna().sum()} date_t0 invalides")
    if not df[cfg.ARM_COL].isin([cfg.ARM_EXPOSED, cfg.ARM_COMPARATOR]).all():
        hard.append("valeurs de bras hors {FQ, BL}")
    if not df["age"].between(18, 110).all():
        hard.append("âges hors [18, 110]")
    if not df["delai_jours"].between(1, cfg.HORIZON_J).all():
        hard.append(f"delai_jours hors [1, {cfg.HORIZON_J}]")
    if ((df["evenement_idm"] == 1) & (df["deces_sans_idm"] == 1)).any():
        hard.append("patients à la fois IDM et décès sans IDM")
    for c, t in cfg.DICTIONARY.items():
        if t == "bin" and not df[c].isin([0, 1]).all():
            hard.append(f"{c} non binaire")
    if (df["annee_t0"] != df["date_t0"].dt.year).any():
        hard.append("annee_t0 incohérente avec date_t0")
    sw = df["switch_j"].dropna()
    if (sw > df.loc[sw.index, "delai_jours"]).any():
        soft.append("switch_j postérieur à la fin du suivi chez certains patients (ignoré en per-protocol)")
    if (df["age"] > 100).sum() > 0:
        soft.append(f"{(df['age'] > 100).sum()} patients de plus de 100 ans : à vérifier")
    return hard, soft


def report(df: pd.DataFrame, hard: list[str], soft: list[str]) -> str:
    counts = df[cfg.ARM_COL].value_counts()
    lines = ["# Rapport de validation de l'extrait", "",
             f"- Fichier : `{cfg.EXTRACT.name}`", f"- Snapshot : {cfg.SNAPSHOT}",
             f"- Lignes : {len(df)} ; colonnes : {df.shape[1]}", ""]
    lines += ["| Bras | n |", "|---|---|"]
    lines += [f"| {cfg.ARM_LABELS[a]} | {cfg.mask(int(counts.get(a, 0)))} |" for a in (cfg.ARM_EXPOSED, cfg.ARM_COMPARATOR)]
    lines += ["", "## Complétude", "", "| Colonne | % renseigné |", "|---|---|"]
    lines += [f"| {c} | {100 * df[c].notna().mean():.1f} |" for c in cfg.DICTIONARY]
    lines += ["", "## Violations dures", ""] + ([f"- {h}" for h in hard] or ["Aucune."])
    lines += ["", "## Avertissements", ""] + ([f"- {s}" for s in soft] or ["Aucun."]) + [""]
    return "\n".join(lines)


if __name__ == "__main__":
    df = load()
    hard, soft = validate(df)
    text = report(df, hard, soft)
    (cfg.OUTPUT_DIR / "10_validation.md").write_text(text, encoding="utf-8")
    print(text)
    if hard:
        sys.exit("Validation échouée : corriger l'extrait avant de poursuivre.")
    df.to_csv(cfg.OUTPUT_DIR / "cohorte_validee.csv", index=False)
    print("OK : extrait validé.")
