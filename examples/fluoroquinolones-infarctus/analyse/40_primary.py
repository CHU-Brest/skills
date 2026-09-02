"""40 - Analyse principale : Cox pondéré par IPTW, courbe d'incidence cumulée, love plot.

Conformément à 05-plan-analyse.md :
1. score de propension par régression logistique sur l'ensemble d'ajustement minimal ;
2. poids IPTW stabilisés, tronqués aux 1er et 99e percentiles ;
3. diagnostic d'équilibre : différences standardisées avant / après pondération (love plot) ;
4. HR brut et HR pondéré (Cox, erreurs robustes), test de Schoenfeld ;
5. incidence cumulée (1 - KM) par bras, brute et pondérée, avec effectifs à risque ;
6. différence de risque à 60 jours (KM pondéré).
Sorties : output/40_resultats.md, output/results.json, output/fig2_incidence_cumulee.{png,svg},
          output/fig3_love_plot.{png,svg}, output/tables.md (Tableau 2 rempli).
"""
import json
import warnings
from importlib import import_module

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from lifelines import CoxPHFitter, KaplanMeierFitter
from lifelines.plotting import add_at_risk_counts
from lifelines.statistics import proportional_hazard_test

cfg = import_module("00_config")
np.random.seed(cfg.SEED)
# lifelines avertit que la variance naïve du KM pondéré est biaisée : connu, documenté dans journal.md
warnings.filterwarnings("ignore", category=UserWarning, module="lifelines")
warnings.filterwarnings("ignore", message=".*weights are not integers.*")


def design_matrix(df: pd.DataFrame) -> pd.DataFrame:
    X = df[cfg.COVARIATES_CONTINUOUS + cfg.COVARIATES_BINARY].astype(float).copy()
    X["age2"] = (X["age"] - X["age"].mean()) ** 2 / 100  # non-linéarité de l'âge
    dummies = pd.get_dummies(df[cfg.COVARIATES_CATEGORICAL].astype(str), drop_first=True, dtype=float)
    return pd.concat([X, dummies], axis=1)


def propensity_and_weights(df: pd.DataFrame) -> tuple[pd.Series, pd.Series, float]:
    X = sm.add_constant(design_matrix(df))
    treated = (df[cfg.ARM_COL] == cfg.ARM_EXPOSED).astype(float)
    ps = sm.Logit(treated, X).fit(disp=0).predict(X)
    p_treated = treated.mean()
    w = np.where(treated == 1, p_treated / ps, (1 - p_treated) / (1 - ps))
    lo, hi = np.percentile(w, [1, 99])
    w_trim = np.clip(w, lo, hi)
    return pd.Series(ps, index=df.index), pd.Series(w_trim, index=df.index), float((w != w_trim).mean())


def smd(x: pd.Series, treated: pd.Series, w: pd.Series | None = None) -> float:
    w = pd.Series(1.0, index=x.index) if w is None else w
    m, v = {}, {}
    for g in (1, 0):
        sel = treated == g
        ww, xx = w[sel], x[sel]
        m[g] = np.average(xx, weights=ww)
        v[g] = np.average((xx - m[g]) ** 2, weights=ww)
    pooled = np.sqrt((v[1] + v[0]) / 2)
    return 0.0 if pooled == 0 else (m[1] - m[0]) / pooled


def balance_table(df: pd.DataFrame, w: pd.Series) -> pd.DataFrame:
    treated = (df[cfg.ARM_COL] == cfg.ARM_EXPOSED).astype(int)
    X = design_matrix(df).drop(columns=["age2"])
    rows = [(c, smd(X[c], treated), smd(X[c], treated, w)) for c in X.columns]
    return pd.DataFrame(rows, columns=["covariable", "SMD brute", "SMD pondérée"]).set_index("covariable")


def love_plot(bal: pd.DataFrame) -> None:
    b = bal.reindex(bal["SMD brute"].abs().sort_values().index)
    fig, ax = plt.subplots(figsize=(8, 0.32 * len(b) + 1.5))
    y = np.arange(len(b))
    ax.scatter(b["SMD brute"].abs(), y, label="Avant pondération", marker="o", color="#888888")
    ax.scatter(b["SMD pondérée"].abs(), y, label="Après IPTW", marker="D", color="#1f5fa8")
    ax.axvline(0.1, ls="--", color="black", lw=0.8)
    ax.set_yticks(y, b.index)
    ax.set_xlabel("Différence standardisée absolue")
    ax.set_title("Figure 3 : équilibre des covariables avant / après IPTW")
    ax.legend(loc="lower right")
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(cfg.OUTPUT_DIR / f"fig3_love_plot.{ext}", dpi=150)
    plt.close(fig)


def cox(df: pd.DataFrame, weights: pd.Series | None) -> tuple[CoxPHFitter, float]:
    d = pd.DataFrame({
        "T": df["delai_jours"].astype(float), "E": df["evenement_idm"].astype(int),
        "fq": (df[cfg.ARM_COL] == cfg.ARM_EXPOSED).astype(int),
    })
    kw = {}
    if weights is not None:
        d["w"] = weights.values
        kw = {"weights_col": "w", "robust": True}
    cph = CoxPHFitter().fit(d, duration_col="T", event_col="E", **kw)
    ph = proportional_hazard_test(cph, d, time_transform="rank")
    return cph, float(ph.summary["p"].iloc[0])


def cumulative_incidence(df: pd.DataFrame, w: pd.Series) -> dict:
    fig, ax = plt.subplots(figsize=(8, 6))
    fitters, risk_60 = [], {}
    for arm, color in ((cfg.ARM_EXPOSED, "#c0392b"), (cfg.ARM_COMPARATOR, "#1f5fa8")):
        sel = df[cfg.ARM_COL] == arm
        km = KaplanMeierFitter(label=cfg.ARM_LABELS[arm])
        km.fit(df.loc[sel, "delai_jours"], df.loc[sel, "evenement_idm"], weights=w[sel])
        (1 - km.survival_function_).rename(columns={km._label: cfg.ARM_LABELS[arm]}).plot(
            ax=ax, drawstyle="steps-post", color=color)
        ci = 1 - km.confidence_interval_
        ax.fill_between(ci.index, ci.iloc[:, 1], ci.iloc[:, 0], step="post", alpha=0.15, color=color)
        risk_60[arm] = float(1 - km.predict(cfg.HORIZON_J))
        fitters.append(km)
    add_at_risk_counts(*fitters, ax=ax, rows_to_show=["At risk"])
    ax_risk = fig.axes[-1]  # axe secondaire créé par lifelines pour les effectifs à risque
    labels = [t.get_text().replace("At risk", "À risque") for t in ax_risk.get_xticklabels()]
    ax_risk.set_xticks(ax_risk.get_xticks())
    ax_risk.set_xticklabels(labels, ha="right", va="top")
    ax.set_xlabel("Jours depuis le temps zéro (première prescription)")
    ax.set_ylabel("Incidence cumulée d'infarctus du myocarde (pondérée IPTW)")
    ax.set_title("Figure 2 : incidence cumulée d'infarctus du myocarde à 60 jours, par bras")
    ax.set_xlim(0, cfg.HORIZON_J)
    ax.legend(loc="upper left")
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(cfg.OUTPUT_DIR / f"fig2_incidence_cumulee.{ext}", dpi=150)
    plt.close(fig)
    return risk_60


def fmt_hr(cph: CoxPHFitter) -> str:
    s = cph.summary.loc["fq"]
    return f"{s['exp(coef)']:.2f} (IC 95 % {s['exp(coef) lower 95%']:.2f} à {s['exp(coef) upper 95%']:.2f})"


if __name__ == "__main__":
    df = pd.read_csv(cfg.OUTPUT_DIR / "cohorte_validee.csv")
    treated = df[cfg.ARM_COL] == cfg.ARM_EXPOSED

    ps, w, trimmed = propensity_and_weights(df)
    bal = balance_table(df, w)
    love_plot(bal)
    n_unbalanced_after = int((bal["SMD pondérée"].abs() > 0.1).sum())

    crude, p_ph_crude = cox(df, None)
    weighted, p_ph = cox(df, w)
    risk_60 = cumulative_incidence(df, w)
    rd = risk_60[cfg.ARM_EXPOSED] - risk_60[cfg.ARM_COMPARATOR]

    counts = {a: int((df[cfg.ARM_COL] == a).sum()) for a in cfg.ARM_LABELS}
    events = {a: int(df.loc[df[cfg.ARM_COL] == a, "evenement_idm"].sum()) for a in cfg.ARM_LABELS}
    deaths = {a: int(df.loc[df[cfg.ARM_COL] == a, "deces_sans_idm"].sum()) for a in cfg.ARM_LABELS}
    ptime = {a: int(df.loc[df[cfg.ARM_COL] == a, "delai_jours"].sum()) for a in cfg.ARM_LABELS}

    results = {
        "n": counts, "evenements_idm": events, "deces_sans_idm": deaths, "personne_jours": ptime,
        "hr_brut": fmt_hr(crude), "hr_iptw": fmt_hr(weighted),
        "hr_iptw_valeur": float(weighted.summary.loc["fq", "exp(coef)"]),
        "p_schoenfeld_iptw": p_ph, "risque_60j": risk_60, "difference_risque_60j": rd,
        "poids_tronques_pct": 100 * trimmed,
        "poids_min_max": [float(w.min()), float(w.max())],
        "covariables_desequilibrees_apres_iptw": n_unbalanced_after,
        "ps_overlap": {"FQ_min_max": [float(ps[treated].min()), float(ps[treated].max())],
                       "BL_min_max": [float(ps[~treated].min()), float(ps[~treated].max())]},
    }
    (cfg.OUTPUT_DIR / "results.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

    E, C = cfg.ARM_EXPOSED, cfg.ARM_COMPARATOR
    t2 = [
        "## Tableau 2 : résultats principaux (critère primaire : infarctus du myocarde à 60 jours)", "",
        "| Critère | Évènements / n (personne-jours), fluoroquinolone | Évènements / n (personne-jours), bêta-lactamine | HR brut (IC 95 %) | HR pondéré IPTW (IC 95 %) | Risque à 60 j FQ vs BL (pondéré) | Différence de risque |",
        "|---|---|---|---|---|---|---|",
        f"| Infarctus du myocarde (DP I21.*/I22.*) | {cfg.mask(events[E])} / {counts[E]} ({ptime[E]}) | {cfg.mask(events[C])} / {counts[C]} ({ptime[C]}) | {results['hr_brut']} | {results['hr_iptw']} | {100 * risk_60[E]:.2f} % vs {100 * risk_60[C]:.2f} % | {100 * rd:+.2f} points |",
        "",
        f"Décès sans infarctus (évènement intercurrent, censuré) : {cfg.mask(deaths[E])} vs {cfg.mask(deaths[C])}. "
        f"Test de Schoenfeld (modèle pondéré) : p = {p_ph:.2f}. "
        f"Poids IPTW stabilisés : min {w.min():.2f}, max {w.max():.2f}, {100 * trimmed:.1f} % tronqués. "
        f"Covariables avec |SMD| > 0,1 après pondération : {n_unbalanced_after}.", "",
    ]
    bal_md = ["## Tableau 3a : équilibre des covariables (différences standardisées)", "",
              bal.round(3).to_markdown(), ""]
    (cfg.OUTPUT_DIR / "40_resultats.md").write_text("\n".join(t2 + bal_md), encoding="utf-8")

    table1 = (cfg.OUTPUT_DIR / "30_table1.md").read_text(encoding="utf-8") if (cfg.OUTPUT_DIR / "30_table1.md").exists() else ""
    tables = ["# Tableaux et figures de l'analyse (exemple sur données synthétiques)", "",
              "> Généré par les scripts 30_table1.py et 40_primary.py sur `data/cohorte_synthetique.csv` "
              "(jeu SYNTHÉTIQUE : aucun patient réel, effet causal simulé HR = 1,4). "
              "Aucun chiffre n'est saisi à la main.", "",
              table1.replace("# Tableau 1", "## Tableau 1"), ""] + t2 + bal_md + [
              "## Figure 2 : incidence cumulée d'infarctus du myocarde à 60 jours", "",
              "![Figure 2](fig2_incidence_cumulee.png)", "",
              "## Figure 3 : love plot", "", "![Figure 3](fig3_love_plot.png)", ""]
    (cfg.OUTPUT_DIR / "tables.md").write_text("\n".join(tables), encoding="utf-8")
    print("\n".join(t2))
    print(json.dumps(results, indent=2, ensure_ascii=False))
