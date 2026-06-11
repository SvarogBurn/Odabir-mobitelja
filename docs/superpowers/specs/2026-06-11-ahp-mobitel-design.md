# AHP – Odabir optimalnog pametnog telefona (Expert Choice u Pythonu)

**Datum:** 2026-06-11
**Cilj seminara:** Riješiti složeni problem odlučivanja AHP metodom — odabir
optimalnog pametnog telefona iz perspektive Ivane (32), freelance grafičke
dizajnerice iz Rijeke koja vodi malu grafičku agenciju (profesionalna
fotografija radova, video pozivi s klijentima, društvene mreže, privatna
komunikacija).

Ovaj dokument pokriva **prvi dio**: definicija hijerarhije, unos usporedbi i
izračun **lokalnih težina**. Drugi dio (sinteza/rang alternativa i analiza
osjetljivosti) dolazi nakon što je prvi dio gotov.

## 1. Hijerarhijski model

```
Cilj: Optimalni pametni telefon za Ivanu
├── 1. Cijena                       (EUR,   cost  → manje je bolje)
├── 2. Kvaliteta kamere             (MP,    benefit → više je bolje)
├── 3. Performanse
│     ├── RAM                       (GB,    benefit)
│     └── Baterija                  (mAh,   benefit)
├── 4. Fizičke karakteristike
│     ├── Ekran                     (inch,  benefit → veći je bolji)
│     └── Težina                    (gram,  cost  → manje je bolje)
└── 5. Pohrana podataka             (GB,    benefit)
```

Točno 2 od 5 kriterija imaju podkriterije (Performanse, Fizičke karakteristike),
što zadovoljava zahtjev zadaće. Svaki list mapira na jedan stupac podataka.

## 2. Alternative i podaci

| Alternativa        | Cijena (EUR) | Kamera (MP) | RAM (GB) | Baterija (mAh) | Ekran (inch) | Težina (g) | Pohrana (GB) | Izvor             |
|--------------------|-------------:|------------:|---------:|---------------:|-------------:|-----------:|-------------:|-------------------|
| Honor 90           | 571.92       | 200         | 12       | 5000           | 6.7          | 183        | 512          | Amazon.com        |
| iPhone 16          | 689.40       | 48          | 8        | 3561           | 6.1          | 170        | 128          | TechnoStore.hr    |
| Samsung Galaxy A56 | 284.00       | 50          | 8        | 5000           | 6.7          | 198        | 128          | Amazon.com        |
| Samsung Galaxy A35 | 314.06       | 50          | 8        | 5000           | 6.6          | 209        | 256          | Amazon.com        |
| OnePlus 11         | 704.71       | 50          | 16       | 5000           | 6.7          | 205        | 256          | Masquerade.hr     |
| Google Pixel 8     | 480.00       | 50          | 8        | 4575           | 6.2          | 187        | 128          | NeutrinoMobile.hr |

## 3. Metoda (kako to radi Expert Choice)

**Kriteriji i podkriteriji — Pairwise Numerical Comparison (Saaty 1–9):**
Sudac (Ivana) ručno ocjenjuje koliko je jedan element važniji od drugog za
postizanje cilja. Iz recipročne matrice usporedbi računaju se:
- **lokalne težine** = normirani glavni (desni) svojstveni vektor matrice;
- **Inconsistency Ratio (CR)** = CI / RI, gdje CI = (λmax − n)/(n − 1), a RI je
  Saatyjev random index. Upozorenje ako CR > 0.10.

Ručnih usporedbi ima ukupno **12**: 10 za 5 kriterija (n=5 → 10 parova),
1 za RAM/Baterija, 1 za Ekran/Težina.

**Alternative — Data mode:** ne uspoređuju se ručno. Za svaki list-kriterij
uzimaju se stvarne vrijednosti iz tablice i normaliziraju prema smjeru:
- benefit (više je bolje): `p_i = v_i / Σ v`;
- cost (manje je bolje): `p_i = (1/v_i) / Σ (1/v)`.
Ovako dobivene lokalne težine su inherentno konzistentne (ratio skala), pa se za
njih ne računa CR — jednako kao u Expert Choiceu.

## 4. Struktura programa (`ahp.py` + `config.py`)

- **`config.py`** — uređivačka datoteka s 12 Saaty ocjena (matrice ili
  gornje-trokutaste liste) za: kriterije (vs. cilj), Performanse-podkriterije,
  Fizičke-podkriterije. Ovdje korisnik mijenja prosudbe i ponovno pokreće.
- **Hijerarhija + podaci** — hard-kodirani u programu (stablo s oznakama
  benefit/cost i nazivom stupca; tablica 6×7).
- **`local_weights(matrix)`** — glavni svojstveni vektor (numpy), vraća
  normirane težine.
- **`consistency_ratio(matrix)`** — λmax, CI, CR uz Saatyjev RI; zastavica
  CR > 0.10.
- **`priorities_from_data(column, direction)`** — normalizacija stupca po smjeru
  (Data mode) → lokalne težine 6 alternativa.
- **Ispis** — za svaki čvor: matrica usporedbi, lokalne težine, te CR gdje je
  primjenjiv (kriteriji/podkriteriji). Za listove: lokalni prioriteti 6
  telefona iz podataka.

## 5. Opseg

**U opsegu (prvi dio):** hijerarhija, unos usporedbi iz configa, lokalne težine
kriterija/podkriterija + CR, lokalni prioriteti alternativa iz podataka, ispis.

**Izvan opsega (drugi dio, kasnije):** sinteza globalnih težina i rang
alternativa s obzirom na cilj; analize osjetljivosti (Performance, Dynamic,
Gradient, Head-to-head, 2D).

## 6. Tehnologija

Python 3, numpy. Pokretanje: `python ahp.py`. Ovisnosti minimalne.
