# -*- coding: utf-8 -*-
"""
Uredive Saaty ocjene (Pairwise Numerical Comparison).

Ovdje mijenjate prosudbe vaznosti i ponovno pokrecete `python ahp.py`.
Skala (Saaty 1-9):
    1   = jednako vazni
    3   = umjereno vazniji
    5   = jako vazniji
    7   = vrlo jako vazniji
    9   = ekstremno vazniji
    2,4,6,8 = medjuvrijednosti
    reciprocne vrijednosti (1/3, 1/5, ...) za obrnuti smjer

Za svaki par (A, B) vrijednost znaci "koliko je A vazniji od B za postizanje cilja".
Program automatski popunjava reciprocne vrijednosti, pa unosite samo gornji trokut.
"""

# --- 5 glavnih kriterija (usporedba s obzirom na CILJ) ---
CRITERIA = [
    "Cijena",
    "Kvaliteta kamere",
    "Performanse",
    "Fizicke karakteristike",
    "Pohrana podataka",
]

# Koliko je kriterij-redak vazniji od kriterija-stupca (gornji trokut).
CRITERIA_JUDGMENTS = {
    ("Cijena", "Kvaliteta kamere"): 1 / 2,
    ("Cijena", "Performanse"): 1 / 2,
    ("Cijena", "Fizicke karakteristike"): 2,
    ("Cijena", "Pohrana podataka"): 1,
    ("Kvaliteta kamere", "Performanse"): 2,
    ("Kvaliteta kamere", "Fizicke karakteristike"): 4,
    ("Kvaliteta kamere", "Pohrana podataka"): 2,
    ("Performanse", "Fizicke karakteristike"): 3,
    ("Performanse", "Pohrana podataka"): 1,
    ("Fizicke karakteristike", "Pohrana podataka"): 1 / 2,
}

# --- Podkriteriji (usporedba s obzirom na PRIPADAJUCI kriterij) ---
SUBCRITERIA = {
    "Performanse": ["RAM", "Baterija"],
    "Fizicke karakteristike": ["Ekran", "Tezina"],
}

SUBCRITERIA_JUDGMENTS = {
    # RAM (multitasking za dizajn) vs Baterija (terenski rad, video pozivi)
    "Performanse": {
        ("RAM", "Baterija"): 2,
    },
    # Ekran (pregled radova) vs Tezina (prijenosnost)
    "Fizicke karakteristike": {
        ("Ekran", "Tezina"): 3,
    },
}

# --- Postavke analize osjetljivosti ---
# 2D graf: dva kriterija na osima (koristi nazive glavnih kriterija)
TWO_D_CRITERIA = ("Kvaliteta kamere", "Performanse")
# Head-to-head: ako je None, uzimaju se dvije najbolje alternative automatski
HEAD_TO_HEAD = None  # npr. ("Honor 90", "OnePlus 11")
