# 3. Interpretacija rezultata

U ovom se poglavlju detaljno tumače rezultati primjene AHP metode na problem
odabira optimalnog pametnog telefona za Ivanu (32), freelance grafičku
dizajnericu iz Rijeke. Za svaki se graf najprije objašnjava **što se mjeri i kako
(osi, mjerne jedinice, način izračuna)**, zatim **koji element grafa predstavlja
što (boje, oblici, stupci, linije, mreža, legenda)**, te se na kraju daje
**dubinska interpretacija podataka** s posljedicama za odluku.

## 3.0. Kako čitati vrijednosti („prioritete") na grafovima

Prije tumačenja pojedinih grafova nužno je razumjeti **što brojevi na osima
zapravo znače**, jer se isti pojam — *prioritet* — pojavljuje na svim grafovima.

- **Prioritet je bezdimenzijski relativni udio**, a ne apsolutna mjera. Ne mjeri
  se u eurima, megapikselima ni gigabajtima, nego u *udjelu važnosti* na skali
  od 0 do 1.
- **Lokalni prioritet alternative po jednom kriteriju** dobiven je „Data mode"
  postupkom (kako radi Expert Choice): stvarne se vrijednosti iz tablice
  normaliziraju. Za kriterije gdje je *više bolje* (kamera, RAM, baterija, ekran,
  pohrana) koristi se izravan udio: prioritet = vrijednost / zbroj svih
  vrijednosti. Za kriterije gdje je *manje bolje* (cijena, težina) koristi se
  recipročna vrijednost: prioritet = (1/vrijednost) / zbroj recipročnih
  vrijednosti. Zbog toga **lokalni prioriteti svih šest alternativa unutar bilo
  kojeg kriterija uvijek zbrajaju u točno 1,0**.
- **Težine kriterija** dobivene su drukčije — usporedbom u parovima na Saatyjevoj
  skali i izračunom glavnog svojstvenog vektora matrice usporedbi. I one zbrajaju
  u 1,0.
- **Ukupni prioritet alternative** = zbroj umnožaka (globalna težina kriterija ×
  lokalni prioritet alternative na tom kriteriju) po svim listovima hijerarhije.

**Ključna metodološka posljedica koju treba imati na umu kroz cijelu
interpretaciju:** budući da se za kameru i pohranu koristi *omjerna*
normalizacija, jedna ekstremno visoka vrijednost „pojede" velik dio udjela i
gurne sve ostale nisko. Honor 90 ima 200 MP, što je oko četiri puta više od
ostalih (48–50 MP), pa njegov lokalni prioritet po kameri iznosi 0,446, dok svih
pet uređaja s ~50 MP dobivaju tek po 0,112 (manje od ravnomjernih 1/6 = 0,167).
Isto vrijedi za pohranu (512 GB naspram 128–256 GB). Ova „dominacija omjerom"
glavni je pokretač rezultata i objašnjava zašto je Honorova prednost tako velika
na svim grafovima.

Stalna shema boja alternativa (vrijedi na svim grafovima osim Components):

| Alternativa | Boja | Ključne sirove vrijednosti |
|---|---|---|
| Honor 90 | **plava** | 200 MP, 512 GB, 12 GB RAM, 5000 mAh, 572 € |
| iPhone 16 | **zelena** | 48 MP, 128 GB, 8 GB RAM, 3561 mAh, 689 € |
| Samsung Galaxy A56 | **ljubičasta** | 50 MP, 128 GB, 8 GB RAM, 5000 mAh, 284 € |
| Samsung Galaxy A35 | **roza** | 50 MP, 256 GB, 8 GB RAM, 5000 mAh, 314 € |
| OnePlus 11 | **žuto-maslinasta** | 50 MP, 256 GB, 16 GB RAM, 5000 mAh, 705 € |
| Google Pixel 8 | **tirkizna** | 50 MP, 128 GB, 8 GB RAM, 4575 mAh, 480 € |

## 3.1. Težine kriterija i konačni poredak

Usporedbom kriterija s obzirom na cilj dobivene su globalne težine (zbroj = 1,0):

| Kriterij | Težina | Udio | Podkriteriji (lokalna težina) |
|---|---:|---:|---|
| Kvaliteta kamere | 0,357 | 35,7 % | — |
| Performanse | 0,226 | 22,6 % | RAM 0,667 · Baterija 0,333 |
| Pohrana podataka | 0,179 | 17,9 % | — |
| Cijena | 0,156 | 15,6 % | — |
| Fizičke karakteristike | 0,082 | 8,2 % | Ekran 0,750 · Težina 0,250 |

Množenjem težina po putu (cilj → kriterij → podkriterij) dobivaju se **globalne
težine listova**, tj. konačni „utezi" svake mjerljive značajke:

| List | Globalna težina |
|---|---:|
| Kvaliteta kamere | 0,357 |
| Pohrana podataka | 0,179 |
| Cijena | 0,156 |
| RAM | 0,151 |
| Baterija | 0,075 |
| Ekran | 0,061 |
| Težina | 0,020 |

Najvažniji kriterij je **kvaliteta kamere** (35,7 %), u skladu s Ivaninom
potrebom za profesionalnom fotografijom radova. Slijede **performanse** (22,6 %),
unutar kojih je RAM (multitasking u dizajnerskim aplikacijama) dvostruko važniji
od baterije. **Pohrana** (17,9 %) i **cijena** (15,6 %) srednje su važne, a
**fizičke karakteristike** najmanje (8,2 %); zanimljivo je da težina uređaja na
kraju nosi samo 2 % ukupne odluke, pa je praktički zanemariva.

Stupanj nekonzistentnosti usporedbi kriterija iznosi **CR = 0,0124**, daleko
ispod granice 0,10 — Ivanine prosudbe su logički dosljedne.

**Konačni poredak** (sinteza po oba načina koje nudi Expert Choice):

| Rang | Alternativa | Distributive | Ideal |
|---:|---|---:|---:|
| 1. | **Honor 90** | **0,3025** | **0,2640** |
| 2. | Samsung Galaxy A35 | 0,1565 | 0,1639 |
| 3. | OnePlus 11 | 0,1562 | 0,1633 |
| 4. | Samsung Galaxy A56 | 0,1445 | 0,1556 |
| 5. | Google Pixel 8 | 0,1260 | 0,1335 |
| 6. | iPhone 16 | 0,1145 | 0,1197 |

Honor 90 pobjeđuje s 0,3025 — gotovo dvostruko više od drugoplasiranog i 19,3
postotnih bodova ispred zadnjeg. Drugo i treće mjesto (A35: 0,1565; OnePlus:
0,1562) razlikuju se za samo 0,0003, dakle praktički su izjednačeni. Poredak je
**identičan u oba načina sinteze**, što je prvi i najjači znak robusnosti.

---

## 3.2. PERFORMANCE — `1_performance.png`

### Što se mjeri i kako
Graf istovremeno prikazuje **dvije veličine na dvije različite okomite osi**:
- **Lijeva os („Lokalni prioritet alternative", raspon 0,0–0,5)** mjeri koliko
  je svaka alternativa dobra *unutar* pojedinog kriterija. Vrijednosti su
  normalizirani udjeli koji unutar svakog kriterija zbrajaju u 1,0.
- **Desna os („Težina kriterija", raspon 0,0–0,5, ispisana plavo)** mjeri
  važnost samog kriterija u ukupnoj odluci.
- **Vodoravna os** nosi pet glavnih kriterija (Cijena, Kvaliteta kamere,
  Performanse, Fizičke karakteristike, Pohrana podataka).

Za kriterije s podkriterijima (Performanse, Fizičke) prioritet alternative
izračunat je kao težinski prosjek podkriterija — npr. Performanse = 0,667·RAM +
0,333·Baterija.

### Elementi grafa
- **Pet svijetloplavih (blijedih) stupaca** u pozadini = težine kriterija,
  očitavaju se na desnoj osi. Najviši je iznad „Kvaliteta kamere" (0,357),
  slijede „Performanse" (0,226) i „Pohrana" (0,179), pa „Cijena" (0,156), a
  najniži je iznad „Fizičke karakteristike" (0,082).
- **Šest obojenih linija s kružnim markerima** = po jedna alternativa; marker
  pokazuje točnu vrijednost na svakom kriteriju, linija samo spaja te točke radi
  preglednosti (nagib linije nema vlastito značenje).
- **Vodoravne crtkane sive linije** = pomoćna mreža za očitavanje vrijednosti na
  lijevoj osi (svakih 0,1).
- **Legenda** ispod grafa povezuje boje s alternativama i objašnjava da blijedi
  stupci predstavljaju težinu kriterija.

### Dubinska interpretacija
- **Plava linija (Honor 90)** crta dva oštra vrha: iznad kamere **0,446** (gotovo
  dvostruko više od idućeg najboljeg ikad na bilo kojem kriteriju) i iznad
  pohrane **0,364**. Oba vrha leže iznad srednje do visoko teških stupaca, što
  znači da se Honorova prednost *množi velikim težinama* i prelijeva u konačni
  rezultat. Istodobno Honor pada na **0,130** kod cijene (skuplji uređaj) — ali
  taj „gubitak" stoji iznad relativno niskog stupca (0,156), pa malo šteti.
- **Žuto-maslinasta linija (OnePlus 11)** ima jedini drugi izraziti vrh — iznad
  performansi **0,237** (16 GB RAM-a). No taj vrh stoji iznad stupca težine 0,226
  i nije dovoljan da nadoknadi zaostatak na kameri i pohrani.
- **Ljubičasta (A56) i roza (A35) linija** kreću visoko iznad cijene (0,263 i
  0,238 — najjeftiniji uređaji) pa naglo padaju na ~0,112 kod kamere i ostaju
  nisko. Njihova jedina prednost (niska cijena) leži iznad niskog stupca, pa se
  „gubi".
- **Tirkizna (Pixel 8) i zelena (iPhone 16) linija** uglavnom su pri dnu bez
  vrhova; iPhone je apsolutno najniži kod kamere (0,107, jer ima najmanje MP) i
  kod pohrane (0,091).
- **Glavni uvid:** pobjednika određuje poklapanje *visoke linije* s *visokim
  stupcem*. Samo Honor ima svoj najviši vrh točno iznad najvišeg stupca (kamera),
  što je sažeta vizualna „formula" njegove pobjede. Svi mjesta gdje se sve linije
  stišću zajedno (npr. fizičke karakteristike, gdje su svi oko 0,16–0,17)
  pokazuju kriterije koji *ne razlikuju* alternative i stoga ne utječu na odluku.

---

## 3.3. DYNAMIC — `2_dynamic_base.png`, `2_dynamic_scenarios.png`, `2_dynamic_components.png`

Dynamic analiza ispituje koliko je rješenje osjetljivo na promjene težina
kriterija i od čega se sastoji. Prikazana je s tri grafa.

### 3.3.1. Trenutno stanje — `2_dynamic_base.png`

**Što se mjeri:** lijevi panel mjeri težine kriterija, desni ukupne prioritete
alternativa; oba u istoj bezdimenzijskoj skali udjela (0–1).

**Elementi:**
- **Lijevi panel („Težine kriterija (trenutne)")** — pet vodoravnih *plavih*
  (steelblue) stupaca, jednake boje jer prikazuju istu veličinu (težinu). Uz
  svaki je ispisana vrijednost: Kvaliteta kamere 0,357 (najduži), Performanse
  0,226, Pohrana 0,179, Cijena 0,156, Fizičke 0,082 (najkraći). Vodoravna os je
  „tezina".
- **Desni panel („Ukupni prioriteti alternativa")** — šest vodoravnih stupaca, ovaj
  put *obojenih bojom svake alternative*, **poredanih od najboljeg (gore) prema
  najlošijem (dolje)**: plavi Honor 90 (0,302) izrazito strši, pa roza A35
  (0,156) i žuti OnePlus 11 (0,156) jednake duljine, ljubičasti A56 (0,144),
  tirkizni Pixel 8 (0,126), zeleni iPhone 16 (0,114).

**Interpretacija:** ovo je polazno („baseline") stanje. Dramatična razlika u
duljini između Honorovog stupca i ostalih vizualno potvrđuje da pobjeda nije
tijesna. Skupina od četiri uređaja u sredini (0,11–0,16) toliko je zbijena da
male promjene ulaza mogu lako mijenjati njihov međusobni redoslijed — što je
upravo predmet sljedećeg grafa.

### 3.3.2. Scenariji ±10 % — `2_dynamic_scenarios.png`

**Što se mjeri:** kako se ukupni prioriteti (okomita os „Ukupni prioritet")
mijenjaju kad jednom kriteriju namjerno povećamo ili smanjimo težinu za 10 %, uz
proporcionalnu preraspodjelu ostalih težina (da zbroj ostane 1,0).

**Elementi:**
- Za svaku od šest alternativa (vodoravna os) prikazane su **tri okomite stupca**
  čije značenje daje **legenda u gornjem desnom kutu**: **sivi** = Baseline
  (polazno), **plavi** = scenarij „Cijena −10 %", **narančasti** = scenarij
  „Performanse +10 %". (Ova dva scenarija program je sam izdvojio kao
  najzanimljivija jer jedina izazivaju promjenu poretka.)
- Vodoravne crtkane linije su pomoćna mreža.

**Interpretacija:** za svaku alternativu sve tri stupca gotovo su jednake visine
— promjene su sitne (reda 0,001–0,005). Honor ostaje nadmoćno najviši u sva tri
slučaja (~0,30). Jedina posljedica: u oba scenarija OnePlus 11 (0,158) za dlaku
prestigne Samsung A35 (0,156) i preuzme **drugo mjesto**, dok ostatak poretka
ostaje netaknut. Zaključak: model je vrlo otporan — pomak težina od 10 % ne dira
ni pobjednika ni opću strukturu, nego samo „prebacuje" dva ionako izjednačena
kandidata za drugo mjesto.

### 3.3.3. Components — `2_dynamic_components.png`

**Što se mjeri:** od kojih se „sastojaka" sastoji ukupni prioritet svake
alternative, tj. koliko svaki *kriterij* doprinosi konačnom rezultatu te
alternative. Okomita os je „Ukupni prioritet (po komponentama)".

**Elementi — pozor na boje:**
- Riječ je o **naslaganim (stacked) okomitim stupcima**, jedan po alternativi.
- **Boje segmenata ovdje označavaju KRITERIJE, a NE alternative** (drukčija
  paleta nego na ostalim grafovima!). Prema legendi u gornjem desnom kutu:
  **tirkizna = Cijena**, **crveno-narančasta (losos) = Kvaliteta kamere**,
  **zeleno-limeta = Performanse**, **ljubičasta = Fizičke karakteristike**,
  **žuta = Pohrana podataka**.
- Visina pojedinog segmenta = doprinos tog kriterija; ukupna visina stupca =
  ukupni prioritet alternative (pa je Honorov stupac najviši, 0,302).

**Interpretacija:** Honorov stupac dominira zahvaljujući **golemom losos-segmentu
(kamera ≈ 0,16)** i **istaknutom žutom segmentu (pohrana ≈ 0,065)**; ta dva
segmenta zajedno čine ~⅔ njegove ukupne vrijednosti. Time je vizualno dokazano da
Honorova pobjeda *gotovo u cijelosti počiva na dva kriterija*. Kod OnePlusa je
najuočljiviji zeleni segment (performanse), kod oba Samsunga tirkizni (cijena), a
iPhone ima najniži stupac s ujednačeno malim segmentima — nema niti jednog
kriterija na kojem se ističe. Components graf tako objašnjava *uzrok* poretka koji
desni panel base-grafa prikazuje samo kao rezultat.

---

## 3.4. GRADIENT — `3_gradient.png`

### Što se mjeri i kako
Gradient za **svaki kriterij zasebno** ispituje što bi se dogodilo s poretkom
kad bi se *samo težina tog kriterija* mijenjala kroz cijeli raspon od 0 do 1
(ostale težine se proporcionalno skaliraju). Graf čini **mreža 2×3** s pet panela
(po jedan kriterij) i šestim poljem (donji desni) koje sadrži **legendu** boja
alternativa.

U svakom panelu:
- **Vodoravna os (x)** = težina odabranog kriterija (0 → 1).
- **Okomita os (y)** = ukupni prioritet alternativa pri toj težini.
- **Šest obojenih linija** = alternative (iste boje kao drugdje).
- **Okomita crtkana crna linija** s oznakom „trenutno=" = stvarna, trenutna
  težina kriterija. Lijevo od nje je „što ako kriterij postane manje važan",
  desno „što ako postane važniji".
- **Sjecišta linija** = točke u kojima dvije alternative mijenjaju mjesta.

### Dubinska interpretacija po panelu
- **Cijena:** s porastom težine prema 1, plava linija (Honor) strmo pada s ≈ 0,30
  na ≈ 0,13, dok roza (A35) i ljubičasta (A56) rastu (najjeftiniji uređaji).
  Sjecište u kojem Honor gubi prvo mjesto nalazi se tek oko x ≈ 0,64 — daleko
  desno od trenutne težine (0,156). Tek ako cijena postane ubjedljivo najvažniji
  kriterij, Honor pada na drugo mjesto.
- **Kvaliteta kamere:** plava linija strmo raste prema 1, sve ostale ostaju niske
  i ravne; **nema sjecišta**. Što je kamera važnija, Honorova prednost samo
  raste — ovo je „najsigurniji" kriterij za njega.
- **Performanse:** žuta linija (OnePlus) i plava (Honor) rastu zajedno, ali pri
  vrlo visokim težinama (x → 1) žuta preteže plavu (OnePlusov prioritet po
  performansama 0,237 > Honorov 0,193). Dakle jedini realan način da OnePlus
  ugrozi Honora bio bi ekstremno naglašavanje performansi.
- **Fizičke karakteristike:** sve linije konvergiraju prema istoj vrijednosti
  (≈ 0,167) kako težina raste, jer su uređaji po ekranu i težini gotovo
  izjednačeni. Honorova plava pada, ali ostaje najviša pri trenutnoj (vrlo maloj)
  težini — ovaj kriterij praktički ne utječe na ishod.
- **Pohrana podataka:** plava linija raste prema 0,364, ostale ostaju niske;
  Honorovih 512 GB daje mu sve veću prednost s rastom važnosti pohrane.

**Povezanost s drugim grafovima:** gradient na kontinuirani način potvrđuje
statičnu sliku iz Performance i Components grafova — Honor dobiva na kameri i
pohrani, neutralan je na fizičkim karakteristikama, a ranjiv je jedino na cijeni
(i to tek u ekstremu) te potencijalno na performansama.

---

## 3.5. HEAD-TO-HEAD — `4_head_to_head.png`

### Što se mjeri i kako
Izravna usporedba dvije najbolje alternative — **Honor 90** i drugoplasiranog
**Samsung Galaxy A35** — po **svih sedam listnih (pokrivajućih) kriterija**. Za
svaki kriterij računa se *težinski doprinos razlike*: globalna težina lista ×
(lokalni prioritet Honora − lokalni prioritet A35). Tako se vidi ne samo *tko je
bolji* na svakom kriteriju, nego i *koliko to vrijedi* u konačnoj odluci.

### Elementi grafa
- **Okomita os** = sedam kriterija, **poredanih po globalnoj težini** od najveće
  (gore) prema najmanjoj (dolje), uz ispisanu težinu u zagradi: Kvaliteta kamere
  (gw=0,357), Pohrana (0,179), Cijena (0,156), RAM (0,151), Baterija (0,075),
  Ekran (0,061), Težina (0,020).
- **Središnja okomita crna crta** = nula (izjednačenost).
- **Vodoravna os** = doprinos razlike; oznaka ispod: lijevo „bolji Samsung Galaxy
  A35", desno „bolji Honor 90".
- **Zeleni stupci (seagreen) udesno** = Honor bolji; **crveni stupci (indianred)
  ulijevo** = A35 bolji. Duljina = veličina težinskog doprinosa, ispisana
  brojčano uz svaki stupac.

### Dubinska interpretacija
- **Kvaliteta kamere: +0,120** (velik zeleni stupac) — Honorova daleko najveća
  prednost, posljedica 200 MP naspram 50 MP, pomnožena najvećom težinom.
- **Pohrana: +0,032** (zeleno) — 512 GB naspram 256 GB.
- **Cijena: −0,017** (jedini crveni stupac) — A35 je jeftiniji (314 € naspram
  572 €), ali je doprinos malen zbog niske težine i jer recipročna normalizacija
  ublažava razliku.
- **RAM: +0,010** (malo zeleno) — 12 GB naspram 8 GB.
- **Baterija, Ekran, Težina: ≈ +0,000** — oba uređaja praktički izjednačena (oba
  5000 mAh, sličan ekran), pa ti kriteriji ne razlučuju.
- **Neto razlika: +0,146** u korist Honora. Graf jasno pokazuje da Honorova
  ukupna prednost gotovo isključivo dolazi iz kamere (uz manji doprinos pohrane i
  RAM-a), a jedina A35-ova „protuteža" — niža cijena — premala je da bi promijenila
  ishod. Time je head-to-head usporedba i kvantitativni dokaz zašto je razlika
  prvog i drugog mjesta tako velika.

---

## 3.6. 2D — `5_two_d.png`

### Što se mjeri i kako
2D graf smješta alternative u koordinatni sustav definiran **dvama odabranim
kriterijima** kako bi se odjednom vidjela uspješnost na obje dimenzije:
- **Vodoravna os (x)** = lokalni prioritet po **Kvaliteti kamere** (raspon
  0,10–0,50).
- **Okomita os (y)** = lokalni prioritet po **Performansama** (raspon
  0,13–0,26).

Ta su dva kriterija odabrana jer su, zajedno, najvažnija (35,7 % + 22,6 % =
58,3 % ukupne odluke).

### Elementi grafa
- **Šest obojenih točaka (kružića) s crnim obrubom** = alternative; svaka je
  označena nazivom.
- **Dvije sive crtkane crte** (okomita na x ≈ 0,167, vodoravna na y ≈ 0,167)
  postavljene su na *prosječne* vrijednosti i dijele ravninu na **četiri
  kvadranta**.
- **Gornji desni kvadrant osjenčan je svijetlozeleno i nosi natpis „NAJBOLJI"** —
  u njega pada alternativa iznadprosječna *na oba* kriterija.

### Dubinska interpretacija po položaju
- **Honor 90 (plava točka)** je krajnje desno (x = 0,446) i iznad prosjeka po
  performansama (y = 0,193) → **jedini u zelenom „najboljem" kvadrantu**. Njegova
  vodoravna udaljenost od svih ostalih vizualno ponavlja „dominaciju omjerom" iz
  poglavlja 3.0.
- **OnePlus 11 (žuta točka)** je najviše gore (y = 0,237, najbolje performanse)
  ali skroz lijevo (x = 0,112) → gornji lijevi kvadrant: vrhunski u
  performansama, slab u kameri. To je vizualni „profil specijalista".
- **Donji lijevi kvadrant (ispodprosječni na oba)** sadrži zbijenu skupinu:
  Samsung A56 (ljubičasta) i A35 (roza) **gotovo se preklapaju** jer dijele istu
  kameru (50 MP) i vrlo bliske performanse; uz njih su Pixel 8 (tirkizna) i
  iPhone 16 (zelena, najniže). Preklapanje dviju Samsungovih točaka izravno
  objašnjava zašto su u konačnom poretku gotovo izjednačene.

**Povezanost s ostalim grafovima:** Honorov položaj krajnje desno odgovara
njegovu vrhu na Performance grafu, velikom zelenom stupcu kamere na Head-to-head
grafu i golemom losos-segmentu na Components grafu. Činjenica da je *jedini* u
zelenom kvadrantu vizualno sažima cijelu analizu: Honor je nadmoćan upravo na
kombinaciji dvaju najvažnijih kriterija.

---

## 3.7. Sažetak interpretacije

Sve provedene analize neovisno vode istom zaključku:

1. **Honor 90 je stabilan pobjednik.** Prvo mjesto zadržava u oba načina sinteze
   (Distributive i Ideal), pri pomacima težina ±10 % (Dynamic) te kroz gotovo
   cijeli raspon težina svih kriterija (Gradient).
2. **Crossover analiza** kvantificira tu otpornost: Honor bi izgubio prvo mjesto
   tek kad bi težina cijene narasla s 0,156 na čak **0,643** — nijedan drugi
   kriterij ne može preokrenuti rezultat pri realnim vrijednostima.
3. **Izvor pobjede** dosljedno se vidi na Components, Performance, Head-to-head i
   2D grafu: Honorova prednost gotovo isključivo dolazi iz **kvalitete kamere
   (200 MP)** i **velike pohrane (512 GB)** — značajki koje su za Ivanu kao
   grafičku dizajnericu objektivno najvažnije.
4. **Jedina nestabilnost** u modelu je borba za *drugo* mjesto između Samsunga
   A35 i OnePlusa 11 (razlika 0,0003), koja se lako preokreće, ali ne utječe na
   preporuku.

Stoga se kao optimalan izbor za Ivanu nedvosmisleno i s visokom pouzdanošću
preporučuje **Honor 90**.
