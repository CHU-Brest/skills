"""Génère un jeu de données SYNTHÉTIQUE pour tester la chaîne /analyze.

Aucun patient réel : toutes les lignes sont tirées au sort à partir de
distributions choisies pour ressembler à une cohorte de nouveaux utilisateurs
d'antibiotiques hospitaliers (fluoroquinolone vs bêta-lactamine) suivie 60 jours
pour un infarctus du myocarde. Les colonnes suivent data/README.md.

Le générateur introduit volontairement une confusion par indication (les
patients plus âgés, plus comorbides et plus sévères reçoivent plus souvent une
fluoroquinolone) et un effet causal HR ≈ 1,4, pour que les scripts aient quelque
chose à corriger et à estimer.

Usage : python make_synthetic.py [--n 12000]
"""
import argparse
from importlib import import_module

import numpy as np
import pandas as pd

cfg = import_module("00_config")


def simulate(n: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    age = np.clip(rng.normal(64, 16, n).round(), 18, 99).astype(int)
    sexe = rng.choice(["F", "M"], n, p=[0.52, 0.48])
    annee_t0 = rng.integers(2015, 2025, n)
    indication = rng.choice(["urinaire", "respiratoire", "autre"], n, p=[0.45, 0.35, 0.20])

    age_c = (age - 64) / 16
    p = lambda logit: 1 / (1 + np.exp(-logit))  # noqa: E731
    diabete = rng.binomial(1, p(-1.6 + 0.5 * age_c))
    hta = rng.binomial(1, p(-0.6 + 0.9 * age_c))
    dyslipidemie = rng.binomial(1, p(-1.3 + 0.5 * age_c))
    coronaropathie = rng.binomial(1, p(-2.3 + 0.8 * age_c))
    irc = rng.binomial(1, p(-2.4 + 0.7 * age_c))
    bpco = rng.binomial(1, p(-2.2 + 0.4 * age_c + 0.3 * (indication == "respiratoire")))
    statine = rng.binomial(1, p(-1.8 + 1.5 * dyslipidemie + 1.2 * coronaropathie))
    antiagregant = rng.binomial(1, p(-2.2 + 2.0 * coronaropathie + 0.3 * age_c))
    corticoide = rng.binomial(1, p(-2.5 + 0.8 * bpco))
    sepsis = rng.binomial(1, p(-2.6 + 0.4 * age_c + 0.5 * irc))
    rea = rng.binomial(1, p(-3.2 + 1.8 * sepsis + 0.3 * age_c))
    charlson = np.clip(
        diabete + hta * 0 + coronaropathie + irc * 2 + bpco + rng.poisson(0.6, n), 0, 12
    ).astype(int)
    nb_sejours_2ans = rng.poisson(0.8 + 0.6 * charlson, n)

    # Assignation du bras : confusion par indication et par sévérité
    logit_fq = (
        -0.9 + 0.25 * age_c + 0.4 * (indication == "urinaire") - 0.2 * (indication == "respiratoire")
        + 0.3 * irc + 0.3 * sepsis + 0.2 * bpco + 0.15 * charlson - 0.1 * (annee_t0 - 2015)
    )
    bras = np.where(rng.binomial(1, p(logit_fq)) == 1, cfg.ARM_EXPOSED, cfg.ARM_COMPARATOR)
    fq = (bras == cfg.ARM_EXPOSED).astype(int)

    duree_prescription_j = np.where(fq == 1, rng.integers(3, 15, n), rng.integers(5, 11, n))

    # Risque d'infarctus à 60 jours : risque de base ~0,6 %, HR causal 1,4 pour FQ
    lambda_idm = 0.006 / cfg.HORIZON_J * np.exp(
        0.7 * age_c + 0.5 * diabete + 0.4 * hta + 0.9 * coronaropathie + 0.5 * irc
        + 0.4 * sepsis + 0.3 * bpco - 0.3 * statine + np.log(1.4) * fq
    )
    lambda_deces = 0.010 / cfg.HORIZON_J * np.exp(0.8 * age_c + 0.3 * charlson + 0.9 * sepsis + 0.6 * rea)
    t_idm = rng.exponential(1 / lambda_idm)
    t_deces = rng.exponential(1 / lambda_deces)
    # Dernier contact (perte de vue) : 3 % des patients, uniforme
    t_contact = np.where(rng.random(n) < 0.03, rng.integers(1, cfg.HORIZON_J, n), np.inf)

    t = np.minimum.reduce([t_idm, t_deces, t_contact, np.full(n, float(cfg.HORIZON_J))])
    evenement_idm = ((t == t_idm) & (t_idm <= cfg.HORIZON_J)).astype(int)
    deces_sans_idm = ((t == t_deces) & (evenement_idm == 0)).astype(int)
    delai_jours = np.clip(np.ceil(t), 1, cfg.HORIZON_J).astype(int)

    # Changement de groupe (per-protocol) chez ~8 % des patients, avant la fin du suivi
    switch = rng.random(n) < 0.08
    switch_j = pd.array(
        np.where(switch, np.minimum(rng.integers(2, 30, n), delai_jours), pd.NA), dtype="Int64"
    )

    date_t0 = pd.to_datetime(
        {"year": annee_t0, "month": rng.integers(1, 13, n), "day": rng.integers(1, 29, n)}
    ).dt.strftime("%Y-%m-%d")

    return pd.DataFrame(
        {
            "patient_id": np.arange(1, n + 1),
            "bras": bras, "date_t0": date_t0, "annee_t0": annee_t0, "age": age, "sexe": sexe,
            "indication": indication,
            "diabete": diabete, "hta": hta, "dyslipidemie": dyslipidemie,
            "coronaropathie": coronaropathie, "irc": irc, "bpco": bpco, "statine": statine,
            "antiagregant": antiagregant, "corticoide": corticoide, "sepsis": sepsis, "rea": rea,
            "charlson": charlson, "nb_sejours_2ans": nb_sejours_2ans,
            "duree_prescription_j": duree_prescription_j,
            "evenement_idm": evenement_idm, "deces_sans_idm": deces_sans_idm,
            "delai_jours": delai_jours, "switch_j": switch_j,
        }
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=12000, help="nombre de patients synthétiques")
    parser.add_argument("--seed", type=int, default=cfg.SEED)
    args = parser.parse_args()

    df = simulate(args.n, args.seed)
    cfg.DATA_DIR.mkdir(exist_ok=True)
    df.to_csv(cfg.EXTRACT, index=False)
    print(f"Écrit {cfg.EXTRACT} : {len(df)} patients synthétiques, graine {args.seed}")
    print(df[cfg.ARM_COL].value_counts().rename("n par bras").to_string())
    print("Évènements IDM :", int(df["evenement_idm"].sum()), "| décès sans IDM :", int(df["deces_sans_idm"].sum()))
