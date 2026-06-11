# Odabir optimalnog pametnog telefona primjenom AHP metode

> Napomena o strukturi: ovaj dokument sadrži poglavlja **1. Uvod**, **2. Analiza
> problema** (2.1–2.3), **4. Zaključak** i **5. Literatura**. Poglavlje **3.
> Interpretacija rezultata** nalazi se u zasebnoj datoteci
> `Interpretacija_rezultata.md` i umeće se između poglavlja 2 i 4.

---

# 1. Uvod

Odabir pametnog telefona na prvi se pogled čini jednostavnom potrošačkom
odlukom, no u stvarnosti je riječ o **složenom problemu odlučivanja s više
međusobno sukobljenih kriterija**. Tržište nudi velik broj uređaja koji se
razlikuju po cijeni, kvaliteti kamere, performansama, kapacitetu pohrane i
fizičkim karakteristikama, pri čemu poboljšanje jedne značajke najčešće povlači
nagodbu (engl. *trade-off*) kod druge — jeftiniji uređaji obično imaju slabiju
kameru, snažniji uređaji veću masu i cijenu, a uređaji s vrhunskom kamerom nisu
nužno najbolji u pohrani ili autonomiji baterije. Donositelj odluke stoga ne može
jednostavno odabrati „najbolji" telefon jer ne postoji uređaj koji je istovremeno
najbolji po svim kriterijima; potrebno je **odvagnuti relativnu važnost kriterija
i pronaći najbolji kompromis** s obzirom na konkretne potrebe korisnika.

Za rješavanje ovakvih problema primjenjuje se metoda **analitičkog hijerarhijskog
procesa (AHP, engl. *Analytic Hierarchy Process*)**, koju je razvio Thomas L.
Saaty. AHP složeni problem razlaže na hijerarhiju — cilj na vrhu, kriterije i
podkriterije u sredini te alternative na dnu — i omogućuje da se elementi na
svakoj razini **uspoređuju u parovima** na Saatyjevoj ljestvici od 1 do 9. Iz tih
se usporedbi izračunavaju težinski koeficijenti (lokalni prioriteti), provjerava
se njihova dosljednost (stupanj nekonzistentnosti) te se konačno sintezom dobiva
poredak alternativa s obzirom na glavni cilj. Glavna prednost metode jest što
**objedinjuje objektivne, mjerljive podatke** (cijena, megapikseli, gigabajti) **i
subjektivne prosudbe o važnosti** kriterija u jedinstven, transparentan i provjerljiv
model.

## 1.1. Opis problema i donositelja odluke

Problem se promatra iz perspektive konkretnog korisnika kako bi prosudbe o
važnosti kriterija bile utemeljene i dosljedne. Donositeljica odluke je **Ivana
(32)**, freelance grafička dizajnerica iz Rijeke koja vodi malu grafičku
agenciju. Njezin posao i svakodnevica postavljaju specifične zahtjeve pred
uređaj:

- **profesionalna fotografija radova** (kataloga, ambalaže, tiskovina) — traži
  kameru visoke rezolucije i kvalitete;
- **video pozivi s klijentima** — traže pouzdane performanse i dobru autonomiju;
- **upravljanje društvenim mrežama agencije** — uključuje obradu fotografija i
  videa „u hodu", što opterećuje procesor, RAM i bateriju;
- **svakodnevna privatna komunikacija** — uređaj mora biti praktičan za
  cjelodnevno nošenje i korištenje.

Budući da kao samostalna poduzetnica sama financira opremu, **cijena je važna ali
ne i presudna**: spremna je platiti više za uređaj koji će izravno doprinijeti
kvaliteti njezina rada, prije svega kroz kameru i performanse.

## 1.2. Kriteriji i podkriteriji

Na temelju Ivaninih potreba definirano je **pet glavnih kriterija**, od kojih
**dva imaju po dva podkriterija**:

1. **Cijena** — nabavna cijena uređaja u eurima. Kriterij je *troškovni* (manja
   vrijednost je poželjnija).
2. **Kvaliteta kamere** — izražena rezolucijom senzora u megapikselima (MP), kao
   ključnom mjerljivom pokazateljem za fotografiju radova. *Korisni* kriterij
   (više je bolje).
3. **Performanse** — sposobnost uređaja za multitasking i cjelodnevni rad, kroz
   dva podkriterija:
   - **RAM memorija (GB)** — radna memorija, ključna za multitasking i obradu
     (više je bolje);
   - **Kapacitet baterije (mAh)** — autonomija i izdržljivost (više je bolje).
4. **Fizičke karakteristike** — ergonomija i praktičnost uređaja, kroz dva
   podkriterija:
   - **Ekran (inč)** — veličina zaslona, važna za pregled i ocjenu dizajnerskih
     radova (veći je bolji);
   - **Težina (g)** — masa uređaja za cjelodnevno nošenje (manja je bolja).
5. **Pohrana podataka** — kapacitet interne memorije u gigabajtima, za pohranu
   velikih grafičkih i video datoteka. *Korisni* kriterij (više je bolje).

## 1.3. Alternative i sumirana tablica vrijednosti

Razmatra se **šest alternativa** — aktualnih uređaja iz različitih cjenovnih i
funkcionalnih razreda. Sve vrijednosti prikupljene su s navedenih maloprodajnih
izvora:

| Alternativa | Cijena (EUR) | Kamera (MP) | RAM (GB) | Baterija (mAh) | Ekran (inč) | Težina (g) | Pohrana (GB) | Izvor |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Honor 90 | 571,92 | 200 | 12 | 5000 | 6,7 | 183 | 512 | Amazon.com |
| iPhone 16 | 689,40 | 48 | 8 | 3561 | 6,1 | 170 | 128 | TechnoStore.hr |
| Samsung Galaxy A56 | 284,00 | 50 | 8 | 5000 | 6,7 | 198 | 128 | Amazon.com |
| Samsung Galaxy A35 | 314,06 | 50 | 8 | 5000 | 6,6 | 209 | 256 | Amazon.com |
| OnePlus 11 | 704,71 | 50 | 16 | 5000 | 6,7 | 205 | 256 | Masquerade.hr |
| Google Pixel 8 | 480,00 | 50 | 8 | 4575 | 6,2 | 187 | 128 | NeutrinoMobile.hr |

Već se iz tablice vidi sukob kriterija: najjeftiniji uređaji (Samsung A56 i A35)
imaju prosječnu kameru i pohranu, uređaj s najboljom kamerom i najvećom pohranom
(Honor 90) je u višem cjenovnom razredu, a najskuplji uređaji (OnePlus 11, iPhone
16) ne dominiraju nužno u svim ostalim kategorijama. Upravo zato je za odabir
optimalnog uređaja potrebna sustavna metoda kakva je AHP.

---

# 2. Analiza problema

## 2.1. Razvoj hijerarhijskog modela problema odlučivanja

Problem je strukturiran u **četverorazinski hijerarhijski model**:

- **1. razina — Cilj:** odabir optimalnog pametnog telefona za Ivanu.
- **2. razina — Kriteriji:** pet glavnih kriterija.
- **3. razina — Podkriteriji:** dva podkriterija unutar Performansi i dva unutar
  Fizičkih karakteristika (ostala tri kriterija nemaju podkriterije pa su ujedno
  i listovi).
- **4. razina — Alternative:** šest pametnih telefona, povezanih sa svakim
  listnim kriterijem.

```
                          CILJ: Optimalni pametni telefon za Ivanu
                                          │
        ┌──────────────┬──────────────────┼───────────────────┬──────────────┐
        │              │                  │                   │              │
     Cijena      Kvaliteta kamere     Performanse      Fizičke karakt.    Pohrana
     (EUR,        (MP, korisni)           │                   │          podataka
     troškovni)                    ┌──────┴──────┐      ┌─────┴─────┐    (GB, korisni)
                                   RAM        Baterija  Ekran    Težina
                                  (GB)         (mAh)    (inč)     (g)
                                                          
        └──────────────┴──────────────────┴───────────────────┴──────────────┘
                                          │
              Alternative: Honor 90 · iPhone 16 · Samsung Galaxy A56 ·
                  Samsung Galaxy A35 · OnePlus 11 · Google Pixel 8
```

Model ima ukupno **sedam listnih (pokrivajućih) kriterija** na kojima se ocjenjuju
alternative: Cijena, Kvaliteta kamere, RAM, Baterija, Ekran, Težina i Pohrana
podataka.

## 2.2. Usporedbe

Usporedbe se rade u skladu s temeljnim načelom AHP-a: **kriteriji se uspoređuju
međusobno prema tome koliko je jedan važniji od drugoga za postizanje cilja**, a
**alternative se uspoređuju prema tome koliko jedna ima prednost nad drugom s
obzirom na zadani kriterij**. Korištena je Saatyjeva ljestvica:

| Ocjena | Značenje |
|---:|---|
| 1 | jednako važni |
| 3 | umjereno važniji |
| 5 | jako važniji |
| 7 | vrlo jako važniji |
| 9 | ekstremno važniji |
| 2, 4, 6, 8 | međuvrijednosti |
| recipročne (1/3, …) | obrnuti odnos važnosti |

### 2.2.1. Usporedba kriterija s obzirom na cilj

Polazeći od Ivaninih potreba (kamera je najvažnija, slijede performanse, zatim
pohrana i cijena, a fizičke su karakteristike najmanje važne), dobivena je
sljedeća matrica usporedbi u parovima:

| | Cijena | Kamera | Performanse | Fizičke | Pohrana |
|---|---:|---:|---:|---:|---:|
| **Cijena** | 1 | 1/2 | 1/2 | 2 | 1 |
| **Kvaliteta kamere** | 2 | 1 | 2 | 4 | 2 |
| **Performanse** | 2 | 1/2 | 1 | 3 | 1 |
| **Fizičke karakteristike** | 1/2 | 1/4 | 1/3 | 1 | 1/2 |
| **Pohrana podataka** | 1 | 1/2 | 1 | 2 | 1 |

Izračunom glavnog svojstvenog vektora matrice dobiveni su **težinski
koeficijenti (lokalni prioriteti) kriterija**:

| Kriterij | Težina |
|---|---:|
| Kvaliteta kamere | 0,3573 |
| Performanse | 0,2258 |
| Pohrana podataka | 0,1787 |
| Cijena | 0,1563 |
| Fizičke karakteristike | 0,0819 |

Provjera dosljednosti: najveća svojstvena vrijednost λmax = 5,0554, indeks
nekonzistentnosti CI = 0,0139, a **stupanj nekonzistentnosti CR = 0,0124**.
Budući da je CR < 0,10, usporedbe se smatraju logički dosljednima i prihvatljivima.

### 2.2.2. Usporedba podkriterija

**Performanse** (RAM nasuprot Bateriji): RAM je za Ivanin multitasking i obradu
ocijenjen umjereno važnijim od baterije (ocjena 2).

| Performanse | RAM | Baterija |
|---|---:|---:|
| **RAM** | 1 | 2 |
| **Baterija** | 1/2 | 1 |

→ lokalne težine: **RAM 0,6667**, **Baterija 0,3333**.

**Fizičke karakteristike** (Ekran nasuprot Težini): veličina ekrana, važna za
pregled radova, ocijenjena je umjereno do jako važnijom od težine (ocjena 3).

| Fizičke | Ekran | Težina |
|---|---:|---:|
| **Ekran** | 1 | 3 |
| **Težina** | 1/3 | 1 |

→ lokalne težine: **Ekran 0,7500**, **Težina 0,2500**.

Matrice dimenzije 2×2 uvijek su savršeno konzistentne (CR = 0).

### 2.2.3. Usporedba alternativa s obzirom na kriterije

Za usporedbu alternativa korišten je postupak temeljen na **stvarnim
izmjerenim vrijednostima** (kako to omogućuje i Expert Choice u načinu „Data"):
umjesto subjektivnog ocjenjivanja svakog para, lokalni prioriteti alternativa
izvedeni su izravno iz tablice vrijednosti. Za **korisne** kriterije (više je
bolje) prioritet je razmjeran vrijednosti (vrijednost / zbroj vrijednosti), a za
**troškovne** kriterije (manje je bolje) razmjeran je recipročnoj vrijednosti.
Ovakvi su lokalni prioriteti **inherentno konzistentni** (izvedeni iz omjerne
ljestvice), pa za njih nema nekonzistentnosti. Unutar svakog kriterija prioriteti
šest alternativa zbrajaju u 1,0.

Dobivene **lokalne prioritete alternativa po svakom listnom kriteriju**:

| Alternativa | Cijena | Kamera | RAM | Baterija | Ekran | Težina | Pohrana |
|---|---:|---:|---:|---:|---:|---:|---:|
| Honor 90 | 0,1304 | 0,4464 | 0,2000 | 0,1777 | 0,1718 | 0,1740 | 0,3636 |
| iPhone 16 | 0,1082 | 0,1071 | 0,1333 | 0,1266 | 0,1564 | 0,1873 | 0,0909 |
| Samsung Galaxy A56 | 0,2626 | 0,1116 | 0,1333 | 0,1777 | 0,1718 | 0,1608 | 0,0909 |
| Samsung Galaxy A35 | 0,2375 | 0,1116 | 0,1333 | 0,1777 | 0,1692 | 0,1523 | 0,1818 |
| OnePlus 11 | 0,1058 | 0,1116 | 0,2667 | 0,1777 | 0,1718 | 0,1553 | 0,1818 |
| Google Pixel 8 | 0,1554 | 0,1116 | 0,1333 | 0,1626 | 0,1590 | 0,1703 | 0,0909 |

Iz tablice je vidljivo kako svaki kriterij favorizira drugu alternativu: po
cijeni vode jeftini Samsungovi (A56: 0,2626), po kameri i pohrani izrazito Honor
90 (0,4464 i 0,3636), po RAM-u OnePlus 11 (0,2667), dok su po bateriji četiri
uređaja s 5000 mAh izjednačena (0,1777).

## 2.3. Izračun prioriteta i alternativa

Konačni prioriteti alternativa izračunavaju se **sintezom**: gledajući od
najniže razine prema najvišoj, lokalni se prioriteti množe težinama svih čvorova
kojima alternativa pripada, a zatim zbrajaju.

**Korak 1 — globalne težine listova** (umnožak težina po putu od cilja do lista):

| List | Izračun | Globalna težina |
|---|---|---:|
| Kvaliteta kamere | 0,3573 | 0,3573 |
| Pohrana podataka | 0,1787 | 0,1787 |
| Cijena | 0,1563 | 0,1563 |
| RAM | 0,2258 × 0,6667 | 0,1505 |
| Baterija | 0,2258 × 0,3333 | 0,0753 |
| Ekran | 0,0819 × 0,7500 | 0,0614 |
| Težina | 0,0819 × 0,2500 | 0,0205 |

(Zbroj globalnih težina = 1,0.)

**Korak 2 — ukupni prioritet alternative** = Σ (globalna težina lista × lokalni
prioritet alternative na tom listu). Primjerice, za Honor 90:

```
0,3573·0,4464 + 0,1787·0,3636 + 0,1563·0,1304 + 0,1505·0,2000
   + 0,0753·0,1777 + 0,0614·0,1718 + 0,0205·0,1740 ≈ 0,3025
```

**Korak 3 — rang alternativa s obzirom na glavni cilj.** Izračun je proveden u
oba načina sinteze koje nudi Expert Choice — *Distributive* (normalizacija po
zbroju) i *Ideal* (normalizacija po najboljoj alternativi, otpornija na pojavu
obrtanja ranga):

| Rang | Alternativa | Prioritet (Distributive) | Prioritet (Ideal) |
|---:|---|---:|---:|
| 1. | **Honor 90** | **0,3025** | **0,2640** |
| 2. | Samsung Galaxy A35 | 0,1565 | 0,1639 |
| 3. | OnePlus 11 | 0,1562 | 0,1633 |
| 4. | Samsung Galaxy A56 | 0,1445 | 0,1556 |
| 5. | Google Pixel 8 | 0,1260 | 0,1335 |
| 6. | iPhone 16 | 0,1145 | 0,1197 |

Oba načina daju **identičan poredak**, s Honorom 90 kao uvjerljivim pobjednikom.
Ukupna nekonzistentnost modela iznosi 0,0139, što potvrđuje pouzdanost rezultata.
Detaljna analiza osjetljivosti i tumačenje svih grafova nalaze se u poglavlju 3.

---

# 4. Zaključak

Cilj ovog rada bio je odabir **optimalnog pametnog telefona** za Ivanu, freelance
grafičku dizajnericu iz Rijeke, kojoj uređaj služi za profesionalnu fotografiju
radova, video pozive s klijentima, upravljanje društvenim mrežama i privatnu
komunikaciju. Problem je riješen metodom analitičkog hijerarhijskog procesa
(AHP), koja je omogućila da se objektivni tehnički podaci i subjektivna procjena
važnosti kriterija objedine u jedinstven, transparentan model.

Izgrađen je četverorazinski hijerarhijski model s pet glavnih kriterija (cijena,
kvaliteta kamere, performanse, fizičke karakteristike i pohrana), od kojih
performanse i fizičke karakteristike imaju po dva podkriterija, te sa šest
alternativa. Usporedbom kriterija na Saatyjevoj ljestvici utvrđeno je da je za
Ivanu **najvažnija kvaliteta kamere (35,7 %)**, a slijede performanse (22,6 %),
pohrana (17,9 %), cijena (15,6 %) i fizičke karakteristike (8,2 %), uz vrlo nizak
stupanj nekonzistentnosti (CR = 0,0124).

Sintezom lokalnih prioriteta i težina kriterija dobiven je konačan poredak u
kojem **Honor 90 uvjerljivo pobjeđuje s prioritetom 0,3025**, gotovo dvostruko
ispred drugoplasiranog Samsunga Galaxy A35 (0,1565) i OnePlusa 11 (0,1562), koji
su međusobno gotovo izjednačeni. Slijede Samsung Galaxy A56, Google Pixel 8 i,
posljednji, iPhone 16. Analiza osjetljivosti (Performance, Dynamic, Gradient,
Head-to-head i 2D) pokazala je da je rješenje **vrlo robusno**: poredak je
identičan u oba načina sinteze, ne mijenja se pri promjenama težina od ±10 %, a
Honor bi izgubio prvo mjesto tek kad bi važnost cijene narasla s 0,156 na čak
0,643. Prednost Honora 90 gotovo u cijelosti proizlazi iz njegove izvrsne kamere
(200 MP) i velike pohrane (512 GB) — upravo onih značajki koje su za Ivanin posao
najvažnije.

Zaključno, AHP metoda potvrdila se kao učinkovit alat za rješavanje ovog složenog
problema odlučivanja te se kao **optimalan izbor za Ivanu nedvosmisleno
preporučuje Honor 90**. Treba napomenuti da rezultat ovisi o ulaznim prosudbama
važnosti: korisnik kojemu bi cijena ili kompaktnost bili znatno važniji mogao bi
dobiti drukčiji poredak, što je upravo i snaga AHP-a — prilagodljivost
specifičnim potrebama donositelja odluke.

---

# 5. Literatura

Saaty, T. L. (1980). *The Analytic Hierarchy Process: Planning, Priority Setting,
Resource Allocation*. McGraw-Hill.

Saaty, T. L. (1990). How to make a decision: The Analytic Hierarchy Process.
*European Journal of Operational Research, 48*(1), 9–26.
https://doi.org/10.1016/0377-2217(90)90057-I

Saaty, T. L. (2008). Decision making with the Analytic Hierarchy Process.
*International Journal of Services Sciences, 1*(1), 83–98.
https://doi.org/10.1504/IJSSCI.2008.017590

Saaty, T. L., & Vargas, L. G. (2012). *Models, Methods, Concepts & Applications
of the Analytic Hierarchy Process* (2. izd.). Springer.

Expert Choice Inc. (2024). *Expert Choice: Comparion software for decision
making*. https://www.expertchoice.com

Amazon.com. (2026). *Honor 90 i Samsung Galaxy A56 — specifikacije i cijene*.
Preuzeto 2026. s https://www.amazon.com

TechnoStore.hr. (2026). *iPhone 16 — specifikacije i cijena*. Preuzeto 2026.

Masquerade.hr. (2026). *OnePlus 11 — specifikacije i cijena*. Preuzeto 2026.

NeutrinoMobile.hr. (2026). *Google Pixel 8 — specifikacije i cijena*. Preuzeto
2026.
