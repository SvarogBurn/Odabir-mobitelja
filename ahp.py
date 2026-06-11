# -*- coding: utf-8 -*-
"""
AHP - Odabir optimalnog pametnog telefona za Ivanu (freelance graficka dizajnerica).

Pokretanje:  python ahp.py

Radi (Expert Choice stil):
  1. Hijerarhija: Cilj -> 5 kriterija -> podkriteriji -> 7 listova.
  2. Kriteriji i podkriteriji: rucne Saaty usporedbe iz config.py
     -> lokalne tezine (glavni svojstveni vektor) + Inconsistency Ratio (CR).
  3. Alternative: "Data mode" - stvarne vrijednosti normalizirane po smjeru
     (benefit / cost) -> lokalni prioriteti (inherentno konzistentni).
  4. Sinteza: globalne tezine listova -> ukupni prioriteti i rang alternativa.
  5. Analiza osjetljivosti (sensitivity.py): Performance, Dynamic, Gradient,
     Head-to-head, 2D.
"""

import numpy as np
import config

# ---------------------------------------------------------------------------
# 1. ALTERNATIVE I PODACI (iz sumirane tablice)
# ---------------------------------------------------------------------------
ALTERNATIVES = [
    "Honor 90",
    "iPhone 16",
    "Samsung Galaxy A56",
    "Samsung Galaxy A35",
    "OnePlus 11",
    "Google Pixel 8",
]

# Svaki LIST-kriterij -> ({alternativa: vrijednost}, smjer, mjerna jedinica)
#   "benefit" = vise je bolje, "cost" = manje je bolje
DATA = {
    "Cijena":           ({"Honor 90": 571.92, "iPhone 16": 689.40, "Samsung Galaxy A56": 284.00,
                          "Samsung Galaxy A35": 314.06, "OnePlus 11": 704.71, "Google Pixel 8": 480.00},
                         "cost", "EUR"),
    "Kvaliteta kamere": ({"Honor 90": 200, "iPhone 16": 48, "Samsung Galaxy A56": 50,
                          "Samsung Galaxy A35": 50, "OnePlus 11": 50, "Google Pixel 8": 50},
                         "benefit", "MP"),
    "RAM":              ({"Honor 90": 12, "iPhone 16": 8, "Samsung Galaxy A56": 8,
                          "Samsung Galaxy A35": 8, "OnePlus 11": 16, "Google Pixel 8": 8},
                         "benefit", "GB"),
    "Baterija":         ({"Honor 90": 5000, "iPhone 16": 3561, "Samsung Galaxy A56": 5000,
                          "Samsung Galaxy A35": 5000, "OnePlus 11": 5000, "Google Pixel 8": 4575},
                         "benefit", "mAh"),
    "Ekran":            ({"Honor 90": 6.7, "iPhone 16": 6.1, "Samsung Galaxy A56": 6.7,
                          "Samsung Galaxy A35": 6.6, "OnePlus 11": 6.7, "Google Pixel 8": 6.2},
                         "benefit", "inch"),
    "Tezina":           ({"Honor 90": 183, "iPhone 16": 170, "Samsung Galaxy A56": 198,
                          "Samsung Galaxy A35": 209, "OnePlus 11": 205, "Google Pixel 8": 187},
                         "cost", "g"),
    "Pohrana podataka": ({"Honor 90": 512, "iPhone 16": 128, "Samsung Galaxy A56": 128,
                          "Samsung Galaxy A35": 256, "OnePlus 11": 256, "Google Pixel 8": 128},
                         "benefit", "GB"),
}

# Hijerarhija: kriterij -> lista podkriterija (ili None ako je list)
HIERARCHY = {
    "Cijena": None,
    "Kvaliteta kamere": None,
    "Performanse": config.SUBCRITERIA["Performanse"],
    "Fizicke karakteristike": config.SUBCRITERIA["Fizicke karakteristike"],
    "Pohrana podataka": None,
}

# Saatyjev Random Index
RI = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}


# ---------------------------------------------------------------------------
# 2. OSNOVNE AHP FUNKCIJE
# ---------------------------------------------------------------------------
def build_matrix(items, judgments):
    """Gradi recipročnu matricu usporedbi iz gornje-trokutastih ocjena."""
    n = len(items)
    idx = {name: i for i, name in enumerate(items)}
    M = np.ones((n, n))
    for (a, b), v in judgments.items():
        i, j = idx[a], idx[b]
        M[i, j] = v
        M[j, i] = 1.0 / v
    return M


def local_weights(M):
    """Lokalne tezine = normirani glavni (desni) svojstveni vektor."""
    vals, vecs = np.linalg.eig(M)
    k = int(np.argmax(vals.real))
    w = np.abs(vecs[:, k].real)
    return w / w.sum()


def consistency(M):
    """Vraca (lambda_max, CI, CR)."""
    n = M.shape[0]
    vals = np.linalg.eigvals(M)
    lmax = float(np.max(vals.real))
    ci = (lmax - n) / (n - 1) if n > 2 else 0.0
    cr = ci / RI[n] if RI.get(n, 0) > 0 else 0.0
    return lmax, ci, cr


def data_priorities(leaf):
    """Data mode: normaliziraj stvarne vrijednosti po smjeru -> lokalni prioriteti."""
    values, direction, _unit = DATA[leaf]
    arr = np.array([values[a] for a in ALTERNATIVES], dtype=float)
    if direction == "cost":
        arr = 1.0 / arr
    return arr / arr.sum()


# ---------------------------------------------------------------------------
# 3. IZRACUN CIJELE HIJERARHIJE
# ---------------------------------------------------------------------------
def compute():
    """Vraca rjecnik sa svim medjurezultatima AHP-a."""
    res = {"alternatives": ALTERNATIVES}

    # 3a. Kriteriji vs cilj
    Mc = build_matrix(config.CRITERIA, config.CRITERIA_JUDGMENTS)
    wc = local_weights(Mc)
    res["criteria"] = config.CRITERIA
    res["criteria_matrix"] = Mc
    res["criteria_weights"] = dict(zip(config.CRITERIA, wc))
    res["criteria_cr"] = consistency(Mc)

    # 3b. Podkriteriji vs pripadajuci kriterij
    res["sub_weights"] = {}      # crit -> {sub: w}
    res["sub_matrix"] = {}
    res["sub_cr"] = {}
    for crit, subs in config.SUBCRITERIA.items():
        Ms = build_matrix(subs, config.SUBCRITERIA_JUDGMENTS[crit])
        ws = local_weights(Ms)
        res["sub_weights"][crit] = dict(zip(subs, ws))
        res["sub_matrix"][crit] = Ms
        res["sub_cr"][crit] = consistency(Ms)

    # 3c. Globalne tezine listova (umnozak tezina po putu od cilja do lista)
    leaf_global = {}
    for crit in config.CRITERIA:
        subs = HIERARCHY[crit]
        if subs is None:
            leaf_global[crit] = res["criteria_weights"][crit]
        else:
            for s in subs:
                leaf_global[s] = res["criteria_weights"][crit] * res["sub_weights"][crit][s]
    res["leaf_global"] = leaf_global

    # 3d. Lokalni prioriteti alternativa po svakom listu (Data mode)
    res["alt_local"] = {leaf: data_priorities(leaf) for leaf in leaf_global}

    # 3e. Ukupni prioriteti alternativa - DISTRIBUTIVE mod (EC default):
    #     normalizacija po zbroju (vec napravljeno u alt_local), zatim suma.
    overall = np.zeros(len(ALTERNATIVES))
    for leaf, gw in leaf_global.items():
        overall += gw * res["alt_local"][leaf]
    res["overall"] = overall

    # 3e'. Ukupni prioriteti - IDEAL mod (EC alternativa): svaki list se dijeli
    #      s najboljom alternativom (max -> 1.0), pa se tezinski zbraja i normira.
    overall_ideal = np.zeros(len(ALTERNATIVES))
    for leaf, gw in leaf_global.items():
        col = res["alt_local"][leaf]
        overall_ideal += gw * (col / col.max())
    res["overall_ideal"] = overall_ideal / overall_ideal.sum()

    # 3f. Lokalni prioriteti alternativa po GLAVNOM kriteriju (za grafove)
    alt_by_crit = {}
    for crit in config.CRITERIA:
        subs = HIERARCHY[crit]
        if subs is None:
            alt_by_crit[crit] = res["alt_local"][crit]
        else:
            v = np.zeros(len(ALTERNATIVES))
            for s in subs:
                v += res["sub_weights"][crit][s] * res["alt_local"][s]
            alt_by_crit[crit] = v
    res["alt_by_crit"] = alt_by_crit

    # 3g. Ukupna nekonzistentnost (tezinski zbroj CI-jeva cvorova - EC stil)
    num = res["criteria_cr"][1]  # CI cilja (tezina 1)
    for crit, (_, ci, _) in res["sub_cr"].items():
        num += res["criteria_weights"][crit] * ci
    res["overall_inconsistency"] = num

    return res


# ---------------------------------------------------------------------------
# 4. ISPIS
# ---------------------------------------------------------------------------
def _fmt_matrix(items, M):
    w = max(len(s) for s in items)
    head = " " * (w + 2) + "".join(f"{s[:10]:>12}" for s in items)
    lines = [head]
    for i, name in enumerate(items):
        row = f"{name:<{w}}  " + "".join(f"{M[i, j]:>12.3f}" for j in range(len(items)))
        lines.append(row)
    return "\n".join(lines)


def print_report(res):
    line = "=" * 78
    print(line)
    print("AHP - ODABIR OPTIMALNOG PAMETNOG TELEFONA (Ivana, Rijeka)")
    print(line)

    # --- Kriteriji ---
    print("\n[1] USPOREDBA KRITERIJA S OBZIROM NA CILJ (Saaty, rucno iz config.py)\n")
    print(_fmt_matrix(res["criteria"], res["criteria_matrix"]))
    lmax, ci, cr = res["criteria_cr"]
    print("\nLokalne tezine kriterija:")
    for c in res["criteria"]:
        print(f"   {c:<26} {res['criteria_weights'][c]:.4f}")
    print(f"\n   lambda_max = {lmax:.4f}   CI = {ci:.4f}   CR = {cr:.4f}"
          f"   -> {'OK (konzistentno)' if cr <= 0.10 else 'UPOZORENJE: CR > 0.10'}")

    # --- Podkriteriji ---
    for crit, subs in config.SUBCRITERIA.items():
        print(f"\n[2] USPOREDBA PODKRITERIJA ZA '{crit}' (Saaty, rucno)\n")
        print(_fmt_matrix(subs, res["sub_matrix"][crit]))
        lmax, ci, cr = res["sub_cr"][crit]
        print("\nLokalne tezine podkriterija:")
        for s in subs:
            print(f"   {s:<26} {res['sub_weights'][crit][s]:.4f}")
        print(f"   (CR = {cr:.4f} - 2 elementa su uvijek konzistentna)")

    # --- Globalne tezine listova ---
    print("\n[3] GLOBALNE TEZINE LISTOVA (umnozak po putu cilj -> list)\n")
    for leaf, gw in sorted(res["leaf_global"].items(), key=lambda x: -x[1]):
        unit = DATA[leaf][2]
        print(f"   {leaf:<26} {gw:.4f}   ({DATA[leaf][1]}, {unit})")
    print(f"   {'SUMA':<26} {sum(res['leaf_global'].values()):.4f}")

    # --- Lokalni prioriteti alternativa po listu (Data mode) ---
    print("\n[4] LOKALNI PRIORITETI ALTERNATIVA PO KRITERIJU (Data mode)\n")
    leaves = list(res["leaf_global"].keys())
    header = f"{'Alternativa':<20}" + "".join(f"{l[:9]:>11}" for l in leaves)
    print(header)
    for i, a in enumerate(res["alternatives"]):
        row = f"{a:<20}" + "".join(f"{res['alt_local'][l][i]:>11.4f}" for l in leaves)
        print(row)

    # --- Ukupni prioriteti i rang (DISTRIBUTIVE) ---
    print("\n[5] UKUPNI PRIORITETI I RANG ALTERNATIVA (s obzirom na cilj)")
    print("    Sinteza: DISTRIBUTIVE mod (EC default)\n")
    order = np.argsort(-res["overall"])
    for rank, i in enumerate(order, 1):
        bar = "#" * int(round(res["overall"][i] * 100))
        print(f"   {rank}. {res['alternatives'][i]:<20} {res['overall'][i]:.4f}  {bar}")

    # --- Usporedna sinteza IDEAL mod ---
    print("\n    Sinteza: IDEAL mod (EC alternativa, otpornija na rank reversal)\n")
    order_i = np.argsort(-res["overall_ideal"])
    for rank, i in enumerate(order_i, 1):
        flag = "" if res["alternatives"][i] == res["alternatives"][order[rank - 1]] \
            else "  <- razlika u poretku"
        print(f"   {rank}. {res['alternatives'][i]:<20} {res['overall_ideal'][i]:.4f}{flag}")
    same = list(order) == list(order_i)
    print(f"\n   Poredak distributive vs ideal: "
          f"{'ISTI (robustan rezultat)' if same else 'RAZLIKUJE SE'}")

    print(f"\n   Ukupna nekonzistentnost modela (EC-stil): {res['overall_inconsistency']:.4f}")
    print(f"   POBJEDNIK: {res['alternatives'][order[0]]}")
    print(line)


def main():
    res = compute()
    print_report(res)
    try:
        import sensitivity
        sensitivity.run_all(res)
        print("\nGrafovi analize osjetljivosti spremljeni u mapu 'output/'.")
    except Exception as e:  # pragma: no cover
        print(f"\n[!] Analiza osjetljivosti preskocena: {e}")


if __name__ == "__main__":
    main()
