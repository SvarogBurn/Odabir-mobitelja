# -*- coding: utf-8 -*-
"""
Analiza osjetljivosti (Expert Choice stil). Pet grafova:
    1. Performance   - prioriteti alternativa po svim kriterijima + ukupno
    2. Dynamic       - promjena poretka pri +/-10% tezine kriterija (+ Components)
    3. Gradient      - poredak alternativa kao funkcija tezine jednog kriterija
    4. Head-to-head  - usporedba dvije alternative po svim kriterijima
    5. 2D            - alternative u 4 kvadranta s obzirom na 2 kriterija

Svi grafovi se spremaju kao PNG u mapu 'output/'.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")  # bez GUI-a
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import config
from ahp import ALTERNATIVES, DATA, HIERARCHY

OUTDIR = "output"
# Stabilna paleta boja po alternativi
_COLORS = plt.cm.tab10(np.linspace(0, 1, len(ALTERNATIVES)))
COLOR = {a: _COLORS[i] for i, a in enumerate(ALTERNATIVES)}


# ---------------------------------------------------------------------------
# Pomocno: ukupni prioriteti za proizvoljne tezine GLAVNIH kriterija
# ---------------------------------------------------------------------------
def overall_with_weights(res, crit_weights):
    """crit_weights: dict glavni_kriterij -> tezina (ne mora biti normirano)."""
    w = np.array([crit_weights[c] for c in res["criteria"]], dtype=float)
    w = w / w.sum()
    cw = dict(zip(res["criteria"], w))
    overall = np.zeros(len(ALTERNATIVES))
    for crit in res["criteria"]:
        subs = HIERARCHY[crit]
        if subs is None:
            overall += cw[crit] * res["alt_local"][crit]
        else:
            for s in subs:
                gw = cw[crit] * res["sub_weights"][crit][s]
                overall += gw * res["alt_local"][s]
    return overall


def _ensure_outdir():
    os.makedirs(OUTDIR, exist_ok=True)


def _save(fig, name):
    path = os.path.join(OUTDIR, name)
    fig.savefig(path, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"   - {path}")


# ---------------------------------------------------------------------------
# 0. HIJERARHIJSKI MODEL (dijagram)
# ---------------------------------------------------------------------------
def hierarchy_diagram(res=None):
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    def box(cx, cy, w, h, text, fc, fs=10, bold=False, tc="black"):
        ax.add_patch(mpatches.FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0.004,rounding_size=0.012",
            linewidth=1.2, edgecolor="#33415c", facecolor=fc, zorder=3))
        ax.text(cx, cy, text, ha="center", va="center", fontsize=fs,
                fontweight="bold" if bold else "normal", color=tc, zorder=4)
        return cx, cy, w, h

    def line(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color="#8d99ae", lw=1.0, zorder=1)

    # Cilj
    box(0.5, 0.92, 0.52, 0.1,
        "CILJ\nOdabir optimalnog pametnog telefona za Ivanu",
        "#1f4e79", 11, True, "white")

    # Glavni kriteriji
    crit = [("Cijena\n(EUR)", 0.10), ("Kvaliteta\nkamere (MP)", 0.30),
            ("Performanse", 0.50), ("Fizičke\nkarakteristike", 0.70),
            ("Pohrana\npodataka (GB)", 0.90)]
    for name, cx in crit:
        box(cx, 0.68, 0.165, 0.1, name, "#9ec5e8", 9.5, True)
        line(0.5, 0.87, cx, 0.73)

    # Podkriteriji
    subs = [("RAM\n(GB)", 0.44, 0.50), ("Baterija\n(mAh)", 0.54, 0.50),
            ("Ekran\n(inč)", 0.66, 0.70), ("Težina\n(g)", 0.76, 0.70)]
    leaf_bottoms = [(0.10, 0.63), (0.30, 0.63), (0.90, 0.63)]  # listni glavni kriteriji
    for name, cx, parent in subs:
        box(cx, 0.46, 0.095, 0.09, name, "#cfe3f5", 9, False)
        line(parent, 0.63, cx, 0.505)
        leaf_bottoms.append((cx, 0.415))

    # Alternative
    box(0.5, 0.13, 0.9, 0.12,
        "ALTERNATIVE\nHonor 90  ·  iPhone 16  ·  Samsung Galaxy A56  ·  "
        "Samsung Galaxy A35  ·  OnePlus 11  ·  Google Pixel 8",
        "#e9ecef", 9.5, False)
    for x, y in leaf_bottoms:  # svaki list -> alternative
        line(x, y, 0.5, 0.19)

    ax.set_title("Hijerarhijski model problema odlučivanja", fontsize=13, pad=4)
    _save(fig, "0_hijerarhija.png")


# ---------------------------------------------------------------------------
# 1. PERFORMANCE
# ---------------------------------------------------------------------------
def performance(res):
    crits = res["criteria"]
    x = np.arange(len(crits))
    fig, ax = plt.subplots(figsize=(12, 6.5))

    # Donji stupci: tezine kriterija
    cw = [res["criteria_weights"][c] for c in crits]
    ax2 = ax.twinx()
    ax2.bar(x, cw, width=0.6, color="lightsteelblue", alpha=0.55,
            label="Tezina kriterija", zorder=0)
    ax2.set_ylabel("Tezina kriterija", color="steelblue")
    ax2.set_ylim(0, max(cw) * 1.6)
    ax2.tick_params(axis="y", colors="steelblue")

    # Linije: prioritet svake alternative po kriteriju
    for i, a in enumerate(ALTERNATIVES):
        y = [res["alt_by_crit"][c][i] for c in crits]
        ax.plot(x, y, marker="o", linewidth=2, color=COLOR[a], label=a, zorder=3)

    ax.set_xticks(x)
    ax.set_xticklabels([c.replace(" ", "\n") for c in crits], fontsize=9)
    ax.set_ylabel("Lokalni prioritet alternative")
    ax.set_ylim(0, max(max(res["alt_by_crit"][c]) for c in crits) * 1.15)
    ax.set_title("PERFORMANCE - prioriteti alternativa po kriterijima\n"
                 "(stupci = tezine kriterija, linije = alternative)", fontsize=12)
    ax.grid(True, axis="y", linestyle=":", alpha=0.5)

    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper center", bbox_to_anchor=(0.5, -0.12),
              ncol=4, fontsize=9, frameon=True)
    _save(fig, "1_performance.png")


# ---------------------------------------------------------------------------
# 2. DYNAMIC (+/-10%) + COMPONENTS
# ---------------------------------------------------------------------------
def _rank_str(res, overall):
    order = np.argsort(-overall)
    return " > ".join(ALTERNATIVES[i] for i in order)


def dynamic(res):
    base = res["overall"]
    base_order = np.argsort(-base)
    base_rank = _rank_str(res, base)

    # Glavni Dynamic graf: dva panela (tezine kriterija | prioriteti alternativa)
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(13, 6))
    crits = res["criteria"]
    yc = np.arange(len(crits))
    cw_vals = [res["criteria_weights"][c] for c in crits]
    axL.barh(yc, cw_vals, color="steelblue")
    axL.set_yticks(yc)
    axL.set_yticklabels(crits, fontsize=9)
    axL.invert_yaxis()
    axL.set_title("Tezine kriterija (trenutne)")
    axL.set_xlabel("tezina")
    axL.set_xlim(0, max(cw_vals) * 1.22)  # prostor za oznake vrijednosti
    for i, c in enumerate(crits):
        axL.text(res["criteria_weights"][c] + max(cw_vals) * 0.015, i,
                 f"{res['criteria_weights'][c]:.3f}", va="center", fontsize=8)

    ya = np.arange(len(ALTERNATIVES))
    cols = [COLOR[ALTERNATIVES[i]] for i in base_order]
    axR.barh(ya, base[base_order], color=cols)
    axR.set_yticks(ya)
    axR.set_yticklabels([ALTERNATIVES[i] for i in base_order], fontsize=9)
    axR.invert_yaxis()
    axR.set_title("Ukupni prioriteti alternativa")
    axR.set_xlabel("prioritet")
    axR.set_xlim(0, base.max() * 1.18)  # prostor za oznake vrijednosti
    for i, idx in enumerate(base_order):
        axR.text(base[idx] + base.max() * 0.012, i, f"{base[idx]:.3f}",
                 va="center", fontsize=8)
    fig.suptitle("DYNAMIC - trenutno stanje modela", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    _save(fig, "2_dynamic_base.png")

    # Scenariji +/-10% za svaki kriterij; detekcija promjene poretka
    findings = []
    scenarios = {}
    for c in crits:
        for sign, tag in [(+0.10, "+10%"), (-0.10, "-10%")]:
            w = dict(res["criteria_weights"])
            w[c] = max(1e-6, w[c] * (1 + sign))
            ov = overall_with_weights(res, w)
            scenarios[(c, tag)] = ov
            if _rank_str(res, ov) != base_rank:
                findings.append((c, tag, _rank_str(res, ov)))

    # Graf: ukupni prioriteti, baseline vs najzanimljiviji scenariji
    interesting = findings[:3] if findings else [
        (crits[1], "+10%", None), (crits[1], "-10%", None), (crits[0], "+10%", None)]
    fig, ax = plt.subplots(figsize=(12, 6.5))
    nbars = 1 + len(interesting)
    width = 0.8 / nbars
    xa = np.arange(len(ALTERNATIVES))
    ax.bar(xa - 0.4 + width / 2, base, width, label="Baseline", color="dimgray")
    for k, (c, tag, _r) in enumerate(interesting, 1):
        ov = scenarios[(c, tag)]
        ax.bar(xa - 0.4 + width / 2 + k * width, ov, width, label=f"{c} {tag}")
    ax.set_xticks(xa)
    ax.set_xticklabels([a.replace(" ", "\n") for a in ALTERNATIVES], fontsize=8)
    ax.set_ylabel("Ukupni prioritet")
    ax.set_title("DYNAMIC - utjecaj promjene tezine kriterija (+/-10%) na prioritete")
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", linestyle=":", alpha=0.5)
    _save(fig, "2_dynamic_scenarios.png")

    # COMPONENTS: stacked bar - doprinos svakog kriterija ukupnom prioritetu
    fig, ax = plt.subplots(figsize=(12, 6.5))
    bottom = np.zeros(len(ALTERNATIVES))
    cmap = plt.cm.Set3(np.linspace(0, 1, len(crits)))
    for ci, c in enumerate(crits):
        subs = HIERARCHY[c]
        if subs is None:
            contrib = res["criteria_weights"][c] * res["alt_local"][c]
        else:
            contrib = np.zeros(len(ALTERNATIVES))
            for s in subs:
                gw = res["criteria_weights"][c] * res["sub_weights"][c][s]
                contrib += gw * res["alt_local"][s]
        ax.bar(xa, contrib, bottom=bottom, label=c, color=cmap[ci])
        bottom += contrib
    ax.set_xticks(xa)
    ax.set_xticklabels([a.replace(" ", "\n") for a in ALTERNATIVES], fontsize=8)
    ax.set_ylabel("Ukupni prioritet (po komponentama)")
    ax.set_title("DYNAMIC / COMPONENTS - udio tezina kriterija u prioritetu alternativa")
    ax.legend(fontsize=8, ncol=2)
    _save(fig, "2_dynamic_components.png")

    # Tekstualni nalazi
    print("\n   DYNAMIC nalazi (promjene poretka pri +/-10%):")
    if findings:
        for c, tag, rank in findings:
            print(f"      * {c} {tag}: novi poredak -> {rank}")
    else:
        print("      * Poredak je stabilan na +/-10% promjene svih kriterija "
              "(robustno rjesenje).")
    return findings


# ---------------------------------------------------------------------------
# 3. GRADIENT
# ---------------------------------------------------------------------------
def gradient(res):
    crits = res["criteria"]
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    axes = axes.ravel()
    ts = np.linspace(0.001, 0.999, 60)

    for ax, c in zip(axes, crits):
        cur = res["criteria_weights"][c]
        curves = {a: [] for a in ALTERNATIVES}
        for t in ts:
            # postavi tezinu kriterija c na t, ostale skaliraj proporcionalno
            others = [k for k in crits if k != c]
            rest = 1 - t
            base_rest = sum(res["criteria_weights"][k] for k in others)
            w = {c: t}
            for k in others:
                w[k] = rest * res["criteria_weights"][k] / base_rest
            ov = overall_with_weights(res, w)
            for i, a in enumerate(ALTERNATIVES):
                curves[a].append(ov[i])
        for a in ALTERNATIVES:
            ax.plot(ts, curves[a], color=COLOR[a], linewidth=1.8, label=a)
        ax.axvline(cur, color="black", linestyle="--", linewidth=1)
        ymin, ymax = ax.get_ylim()
        ax.text(cur + 0.01, ymin + (ymax - ymin) * 0.5, f"trenutno={cur:.2f}",
                fontsize=7, va="center", rotation=90, color="black")
        ax.set_title(c, fontsize=10)
        ax.set_xlabel("tezina kriterija")
        ax.set_ylabel("prioritet alternative")
        ax.grid(True, linestyle=":", alpha=0.5)

    # zadnji prazni panel -> legenda
    if len(crits) < len(axes):
        axes[-1].axis("off")
        handles = [plt.Line2D([0], [0], color=COLOR[a], lw=2) for a in ALTERNATIVES]
        axes[-1].legend(handles, ALTERNATIVES, loc="center", fontsize=11,
                        title="Alternative")
    fig.suptitle("GRADIENT - kako tezina pojedinog kriterija mijenja poredak alternativa",
                 fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    _save(fig, "3_gradient.png")


# ---------------------------------------------------------------------------
# 4. CROSSOVER (numericki - EC Dynamic "koja tezina za prestizanje")
# ---------------------------------------------------------------------------
def crossover_analysis(res):
    order = np.argsort(-res["overall"])
    a1, a2 = order[0], order[1]  # pobjednik, prvi pratitelj
    crits = res["criteria"]
    ts = np.linspace(1e-4, 1 - 1e-4, 2000)
    print(f"\n   CROSSOVER - tezina kriterija pri kojoj '{ALTERNATIVES[a2]}' "
          f"prestigne pobjednika '{ALTERNATIVES[a1]}':")
    for c in crits:
        others = [k for k in crits if k != c]
        base_rest = sum(res["criteria_weights"][k] for k in others)
        ds = []
        for t in ts:
            w = {c: t}
            for k in others:
                w[k] = (1 - t) * res["criteria_weights"][k] / base_rest
            ov = overall_with_weights(res, w)
            ds.append(ov[a1] - ov[a2])  # >0 -> pobjednik ispred
        ds = np.array(ds)
        sign = np.sign(ds)
        idx = np.where(np.diff(sign) != 0)[0]
        cur = res["criteria_weights"][c]
        if len(idx) == 0:
            print(f"      * {c:<24} nema prestizanja (pobjednik ostaje ispred; "
                  f"trenutna tezina={cur:.3f})")
        else:
            pts = []
            for j in idx:  # linearna interpolacija nultocke
                t0, t1, d0, d1 = ts[j], ts[j + 1], ds[j], ds[j + 1]
                pts.append(t0 + (t1 - t0) * d0 / (d0 - d1))
            pts_s = ", ".join(f"{p:.3f}" for p in pts)
            print(f"      * {c:<24} prestizanje pri tezini = {pts_s} "
                  f"(trenutna={cur:.3f})")


# ---------------------------------------------------------------------------
# 5. HEAD-TO-HEAD (po svim listnim/pokrivajucim kriterijima - EC stil)
# ---------------------------------------------------------------------------
def head_to_head(res):
    if config.HEAD_TO_HEAD:
        a1, a2 = config.HEAD_TO_HEAD
    else:
        order = np.argsort(-res["overall"])
        a1, a2 = ALTERNATIVES[order[0]], ALTERNATIVES[order[1]]
    i1, i2 = ALTERNATIVES.index(a1), ALTERNATIVES.index(a2)

    # po svim LISTNIM kriterijima, sortirano po globalnoj tezini
    leaves = sorted(res["leaf_global"], key=lambda l: -res["leaf_global"][l])
    diffs = [res["leaf_global"][l] * (res["alt_local"][l][i1] - res["alt_local"][l][i2])
             for l in leaves]

    fig, ax = plt.subplots(figsize=(11, 7))
    y = np.arange(len(leaves))
    colors = ["seagreen" if d >= 0 else "indianred" for d in diffs]
    ax.barh(y, diffs, color=colors)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels([f"{l} (gw={res['leaf_global'][l]:.3f})" for l in leaves], fontsize=9)
    ax.invert_yaxis()
    lim = max(abs(d) for d in diffs) * 1.35 + 1e-6
    ax.set_xlim(-lim, lim)
    ax.set_xlabel(f"<--- bolji {a2}        |        bolji {a1} --->")
    tot1, tot2 = res["overall"][i1], res["overall"][i2]
    ax.set_title(f"HEAD-TO-HEAD: {a1} ({tot1:.3f})  vs  {a2} ({tot2:.3f})\n"
                 f"(tezinski doprinos razlike po listnom kriteriju)", fontsize=12)
    for i, d in enumerate(diffs):
        ax.text(d + lim * 0.02 * (1 if d >= 0 else -1), i, f"{d:+.3f}",
                va="center", ha="left" if d >= 0 else "right", fontsize=8)
    _save(fig, "4_head_to_head.png")
    net = sum(diffs)
    print(f"\n   HEAD-TO-HEAD: {a1} vs {a2}  (ukupno {tot1:.3f} vs {tot2:.3f}, "
          f"neto razlika {net:+.3f})")


# ---------------------------------------------------------------------------
# 5. 2D
# ---------------------------------------------------------------------------
def two_d(res):
    cx, cy = config.TWO_D_CRITERIA
    xs = res["alt_by_crit"][cx]
    ys = res["alt_by_crit"][cy]
    mx, my = xs.mean(), ys.mean()

    fig, ax = plt.subplots(figsize=(9.5, 8.5))
    ax.axvline(mx, color="gray", linestyle="--", linewidth=1)
    ax.axhline(my, color="gray", linestyle="--", linewidth=1)
    ax.fill_between([mx, xs.max() * 1.1], my, ys.max() * 1.1,
                    color="honeydew", zorder=0)  # gornji desni = najbolji

    for i, a in enumerate(ALTERNATIVES):
        ax.scatter(xs[i], ys[i], s=180, color=COLOR[a], edgecolor="black", zorder=3)
        ax.annotate(a, (xs[i], ys[i]), textcoords="offset points",
                    xytext=(8, 6), fontsize=9)
    ax.set_xlabel(f"Prioritet po: {cx}")
    ax.set_ylabel(f"Prioritet po: {cy}")
    ax.set_title(f"2D - alternative s obzirom na '{cx}' i '{cy}'\n"
                 f"(najbolji = gornji desni kvadrant)", fontsize=12)
    ax.text(xs.max() * 1.02, ys.max() * 1.05, "NAJBOLJI", color="green",
            fontsize=10, ha="right", fontweight="bold")
    ax.grid(True, linestyle=":", alpha=0.4)
    _save(fig, "5_two_d.png")


# ---------------------------------------------------------------------------
def run_all(res):
    _ensure_outdir()
    print("\n[6] ANALIZA OSJETLJIVOSTI - generiranje grafova:")
    hierarchy_diagram(res)
    performance(res)
    dynamic(res)
    gradient(res)
    crossover_analysis(res)
    head_to_head(res)
    two_d(res)
