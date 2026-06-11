# AHP - Odabir optimalnog pametnog telefona

AHP (Analytic Hierarchy Process) rjesenje slozenog problema odlucivanja:
**odabir optimalnog pametnog telefona** iz perspektive Ivane (32), freelance
graficke dizajnerice iz Rijeke koja vodi malu graficku agenciju (profesionalna
fotografija radova, video pozivi, drustvene mreze, privatna komunikacija).

Implementira ono sto radi Expert Choice, u Pythonu.

## Hijerarhija

```
Cilj: Optimalni pametni telefon
├── 1. Cijena                       (EUR,  manje je bolje)
├── 2. Kvaliteta kamere             (MP,   vise je bolje)
├── 3. Performanse
│     ├── RAM                       (GB)
│     └── Baterija                  (mAh)
├── 4. Fizicke karakteristike
│     ├── Ekran                     (inch, veci je bolji)
│     └── Tezina                    (g,    manje je bolje)
└── 5. Pohrana podataka             (GB)
```

## Metoda

- **Kriteriji i podkriteriji** se usporedjuju rucno na **Saaty skali (1-9)**
  (Pairwise Numerical Comparison). Ocjene se unose u `config.py`. Lokalne tezine
  = glavni svojstveni vektor; izvjestava se **Inconsistency Ratio (CR)**.
- **Alternative** se boduju iz stvarnih vrijednosti (**Data mode**): svaki
  stupac se normalizira po smjeru (benefit / cost). Inherentno konzistentno.
- **Sinteza**: globalna tezina lista = umnozak tezina po putu; ukupni prioritet
  alternative = suma (globalna tezina x lokalni prioritet). Racunaju se i
  ispisuju **oba EC moda**: *Distributive* (normalizacija po zbroju) i *Ideal*
  (normalizacija po najboljoj alternativi, otpornije na rank reversal).

## Pokretanje

```bash
pip install -r requirements.txt
python ahp.py
```

Ispis daje sve matrice usporedbi, lokalne i globalne tezine, CR, te konacni
rang alternativa. Grafovi analize osjetljivosti spremaju se u `output/`.

## Analiza osjetljivosti

Pet grafova (Expert Choice stil) u `output/`:

| Datoteka | Analiza | Opis |
|---|---|---|
| `1_performance.png` | Performance | prioriteti alternativa po kriterijima + tezine |
| `2_dynamic_*.png`   | Dynamic     | utjecaj +/-10% tezina, Components (udjeli) |
| `3_gradient.png`    | Gradient    | poredak kao funkcija tezine svakog kriterija |
| `4_head_to_head.png`| Head-to-head| usporedba dvije najbolje alternative po svih 7 listnih kriterija |
| `5_two_d.png`       | 2D          | alternative u 4 kvadranta po 2 kriterija |

Uz grafove, u konzoli se ispisuje i **crossover analiza** (numericki): tezina
koju pojedini kriterij mora dosegnuti da prvi pratitelj prestigne pobjednika -
odgovor na EC Dynamic pitanje "kolika tezina za prestizanje".

## Datoteke

- `config.py` - uredive Saaty ocjene i postavke grafova
- `ahp.py` - hijerarhija, podaci, izracun, ispis
- `sensitivity.py` - pet analiza osjetljivosti
- `docs/superpowers/specs/` - dizajn dokument
