# 3. Interpretacija rezultata

U ovom poglavlju tumače se rezultati primjene AHP metode na problem odabira
optimalnog pametnog telefona za Ivanu (32), freelance grafičku dizajnericu iz
Rijeke. Najprije se interpretiraju izračunate težine kriterija i konačni poredak
alternativa, a zatim se detaljno opisuje svaki od grafova analize osjetljivosti
te se objašnjava kako su pojedini grafovi međusobno povezani.

Radi lakšeg praćenja, svakoj je alternativi kroz sve grafove dodijeljena ista,
stalna boja:

| Alternativa | Boja na grafovima |
|---|---|
| Honor 90 | **plava** |
| iPhone 16 | **zelena** |
| Samsung Galaxy A56 | **ljubičasta (purpurna)** |
| Samsung Galaxy A35 | **roza (magenta)** |
| OnePlus 11 | **žuto-maslinasta** |
| Google Pixel 8 | **tirkizna (cijan)** |

## 3.1. Težine kriterija i konačni poredak

Usporedbom kriterija s obzirom na cilj dobivene su sljedeće globalne težine:

| Kriterij | Težina |
|---|---:|
| Kvaliteta kamere | 0,357 |
| Performanse | 0,226 |
| Pohrana podataka | 0,179 |
| Cijena | 0,156 |
| Fizičke karakteristike | 0,082 |

Najvažniji kriterij za Ivanu je **kvaliteta kamere** (35,7 % ukupne važnosti), što
je u skladu s njezinom potrebom za profesionalnom fotografijom radova. Slijede
**performanse** (22,6 %), pri čemu je unutar tog kriterija RAM (težina 0,667)
dvostruko važniji od baterije (0,333). **Pohrana** (17,9 %) i **cijena** (15,6 %)
imaju srednju važnost, dok su **fizičke karakteristike** (8,2 %) najmanje važne;
unutar njih ekran (0,75) znatno nadmašuje težinu (0,25).

Stupanj nekonzistentnosti usporedbi kriterija iznosi **CR = 0,0124**, što je
znatno ispod granične vrijednosti 0,10. To znači da su Ivanine prosudbe logički
dosljedne i da se dobivenim težinama može vjerovati.

Sintezom lokalnih prioriteta i globalnih težina dobiven je konačni poredak
alternativa s obzirom na glavni cilj:

| Rang | Alternativa | Prioritet (Distributive) | Prioritet (Ideal) |
|---:|---|---:|---:|
| 1. | **Honor 90** | **0,3025** | **0,2640** |
| 2. | Samsung Galaxy A35 | 0,1565 | 0,1639 |
| 3. | OnePlus 11 | 0,1562 | 0,1633 |
| 4. | Samsung Galaxy A56 | 0,1445 | 0,1556 |
| 5. | Google Pixel 8 | 0,1260 | 0,1335 |
| 6. | iPhone 16 | 0,1145 | 0,1197 |

**Honor 90 je uvjerljivi pobjednik** s prioritetom 0,3025, što je gotovo
dvostruko više od drugoplasiranog. Poredak je identičan u oba načina sinteze
(Distributive i Ideal), što je prvi pokazatelj robusnosti rješenja. Drugo i treće
mjesto dijele Samsung Galaxy A35 (0,1565) i OnePlus 11 (0,1562) — razlika među
njima je tek 0,0003, pa se može reći da su praktički izjednačeni. iPhone 16 je
posljednji (0,1145), prvenstveno zbog niske rezolucije kamere (48 MP), male
pohrane (128 GB) i najviše cijene u kombinaciji s prosječnim ostalim
značajkama.

## 3.2. Performance (datoteka `1_performance.png`)

Performance graf prikazuje prioritete svih alternativa po pojedinom kriteriju i
povezuje ih s težinama kriterija.

**Što graf prikazuje:** Na vodoravnoj osi (x) nalazi se pet glavnih kriterija
poredanih slijeva nadesno: Cijena, Kvaliteta kamere, Performanse, Fizičke
karakteristike i Pohrana podataka. Lijeva okomita os („Lokalni prioritet
alternative") odnosi se na obojene linije, a desna okomita os („Težina
kriterija", ispisana plavom bojom) odnosi se na svijetloplave stupce u pozadini.

**Svijetloplavi stupci** u dnu grafa predstavljaju težine kriterija: najviši je
stupac iznad „Kvaliteta kamere" (0,357), zatim slijede Pohrana (0,179),
Performanse (0,226 — vizualno drugi po visini), Cijena (0,156), a najniži je
stupac iznad „Fizičke karakteristike" (0,082). Ti stupci govore koliko pojedini
kriterij „vuče" u konačnoj odluci.

**Šest obojenih linija** s kružnim markerima (točkama) prati svaku alternativu
kroz svih pet kriterija:

- **Plava linija (Honor 90)** ima izrazit vrh iznad „Kvaliteta kamere" (0,446) —
  daleko iznad svih ostalih — te drugi vrh iznad „Pohrana podataka" (0,364).
  Istovremeno pada nisko kod „Cijena" (0,130), jer je Honor relativno skup.
- **Žuto-maslinasta linija (OnePlus 11)** skače na drugi najviši vrh iznad
  „Performanse" (0,237), zahvaljujući 16 GB RAM-a; inače se drži nisko.
- **Ljubičasta (A56) i roza (A35) linija** najviše su iznad „Cijena" (0,263 i
  0,238) jer su to najjeftiniji uređaji, a drže se nisko na ostalim kriterijima.
- **Tirkizna (Pixel 8) i zelena (iPhone 16) linija** uglavnom su pri dnu, bez
  istaknutih vrhova; iPhone je najniži kod kamere i pohrane.

**Povezanost s konačnim rezultatom:** ključno je gdje se visoka linija poklapa s
visokim stupcem. Honor 90 ima najviši vrh (kamera) točno iznad najvišeg stupca
(kamera je najteži kriterij), pa taj uspjeh ulazi u konačni rezultat s najvećom
težinom — to je glavni razlog njegove pobjede. Nasuprot tome, OnePlusov vrh kod
performansi nalazi se iznad srednje visokog stupca, pa donosi manju korist, dok
prednost Samsunga kod cijene leži iznad relativno niskog stupca i stoga slabo
utječe na konačni poredak.

## 3.3. Dynamic (datoteke `2_dynamic_base.png`, `2_dynamic_scenarios.png`, `2_dynamic_components.png`)

Dynamic analiza pokazuje koliko su prioriteti alternativa osjetljivi na promjene
težina kriterija. Prikazana je kroz tri grafa.

### 3.3.1. Trenutno stanje — `2_dynamic_base.png`

Graf je podijeljen u dva panela. **Lijevi panel** („Težine kriterija (trenutne)")
sadrži vodoravne plave stupce za svih pet kriterija, uz ispisanu brojčanu
vrijednost na kraju svakog stupca: Kvaliteta kamere 0,357 (najduži), Performanse
0,226, Pohrana 0,179, Cijena 0,156 i Fizičke karakteristike 0,082 (najkraći).
**Desni panel** („Ukupni prioriteti alternativa") sadrži vodoravne stupce
obojene bojom svake alternative, poredane od najboljeg (gore) prema najlošijem
(dolje): plavi Honor 90 (0,302) izrazito strši udesno, zatim roza Samsung A35
(0,156) i žuti OnePlus 11 (0,156) gotovo jednake duljine, ljubičasti Samsung A56
(0,144), tirkizni Google Pixel 8 (0,126) i zeleni iPhone 16 (0,114). Ovaj graf
sažima polazno („baseline") stanje na koje se nadovezuju scenariji.

### 3.3.2. Scenariji ±10 % — `2_dynamic_scenarios.png`

Graf prikazuje grupirane okomite stupce: za svaku od šest alternativa (na
vodoravnoj osi) prikazane su tri stupca čije značenje objašnjava legenda u
gornjem desnom kutu — **sivi stupac** je Baseline (polazno stanje), **plavi**
prikazuje stanje kad se težina kriterija Cijena smanji za 10 %, a **narančasti**
kad se težina kriterija Performanse poveća za 10 %. Okomita os je „Ukupni
prioritet".

Vidljivo je da su sve tri varijante za svaku alternativu gotovo jednake visine —
promjene su minimalne. Honor 90 ostaje daleko najviši u sva tri scenarija (oko
0,30). Jedina zamjetna posljedica je da kod ova dva scenarija OnePlus 11 (0,158)
neznatno prestiže Samsung A35 (0,156) i preuzima drugo mjesto, dok ostatak
poretka ostaje nepromijenjen. To potvrđuje da je rješenje vrlo stabilno: ni
pomak od 10 % u težinama ne mijenja pobjednika ni opću sliku.

### 3.3.3. Components — `2_dynamic_components.png`

Components graf prikazuje od čega se sastoji ukupni prioritet svake alternative.
Riječ je o naslaganim (stacked) okomitim stupcima — jedan stupac po alternativi —
gdje je svaki stupac podijeljen u **pet obojenih segmenata**, po jedan za svaki
kriterij. **Važna napomena:** boje segmenata ovdje označavaju **kriterije**, a ne
alternative (kako pokazuje legenda u gornjem desnom kutu): tirkizna = Cijena,
crveno-narančasta (losos) = Kvaliteta kamere, zelena (limeta) = Performanse,
ljubičasta = Fizičke karakteristike, žuta = Pohrana podataka. Visina pojedinog
segmenta jednaka je doprinosu tog kriterija ukupnom prioritetu alternative, a
ukupna visina stupca jednaka je ukupnom prioritetu.

Stupac Honora 90 daleko je najviši (0,302). U njemu dominira velik
crveno-narančasti segment (kamera, ≈ 0,16) i istaknut žuti segment (pohrana,
≈ 0,065), dok su ostali segmenti manji. Kod ostalih alternativa stupci su niži i
ujednačeniji — npr. kod OnePlusa je zeleni segment (performanse) razmjerno velik,
a kod oba Samsunga je tirkizni segment (cijena) najveći među njima. Ovaj graf
zorno objašnjava *zašto* Honor pobjeđuje: gotovo cijela njegova prednost dolazi
iz kamere i pohrane, dvaju kriterija na kojima ima najveće vrijednosti (200 MP i
512 GB).

## 3.4. Gradient (datoteka `3_gradient.png`)

Gradient analiza za svaki kriterij zasebno ispituje kako njegova težina utječe na
poredak alternativa. Graf se sastoji od **šest panela** raspoređenih u mreži 2×3;
pet panela odgovara kriterijima, a šesti (donji desni) sadrži legendu s bojama
alternativa.

U svakom panelu vodoravna os (x) označava težinu odabranog kriterija (od 0 do 1),
a okomita os (y) prioritet alternativa. Šest obojenih linija prati alternative, a
**okomita crtkana crna linija** označava trenutnu (stvarnu) težinu tog kriterija,
uz oznaku „trenutno=". Sjecišta linija predstavljaju težine pri kojima dolazi do
promjene poretka.

- **Cijena:** kako težina cijene raste prema 1, plava linija (Honor) strmo pada
  (s ≈ 0,30 prema ≈ 0,13), dok roza (A35) i ljubičasta (A56) linija rastu jer su
  to najjeftiniji uređaji. Linije se sijeku tek znatno desno od trenutne težine
  (oko x ≈ 0,64), što znači da bi cijena morala postati daleko najvažniji
  kriterij da Honor izgubi prvo mjesto.
- **Kvaliteta kamere:** plava linija (Honor) strmo raste prema 1, a sve ostale
  ostaju niske i ravne. Što je kamera važnija, to je Honorova prednost veća —
  ovdje nema sjecišta, Honor samo jača.
- **Performanse:** žuta linija (OnePlus) i plava (Honor) rastu, pri čemu se pri
  vrlo visokim težinama (blizu x = 1) žuta linija približava plavoj i preteže je
  (OnePlusov prioritet po performansama 0,237 nadmašuje Honorov 0,193). To znači
  da bi jedino ekstremno naglašavanje performansi moglo dovesti OnePlus iznad
  Honora.
- **Fizičke karakteristike:** sve linije teže prema istoj vrijednosti (≈ 0,167)
  kako težina raste, jer su alternative po ekranu i težini gotovo izjednačene;
  Honorova plava linija pritom pada s 0,30, ali ostaje najviša pri trenutnoj
  težini.
- **Pohrana podataka:** plava linija (Honor) raste prema 0,364, dok ostale
  ostaju niske — Honorovih 512 GB daje mu sve veću prednost s rastom važnosti
  pohrane.

**Povezanost s ostalim grafovima:** gradient na detaljnoj razini potvrđuje ono
što Performance graf pokazuje statički — Honor dobiva na kamerama i pohrani, a
gubi jedino na cijeni i (potencijalno) na ekstremnim performansama.

## 3.5. Head-to-head (datoteka `4_head_to_head.png`)

Head-to-head graf izravno uspoređuje dvije najbolje alternative — **Honor 90** i
drugoplasirani **Samsung Galaxy A35** — po svih sedam listnih (pokrivajućih)
kriterija. Riječ je o divergentnom (dvosmjernom) grafu vodoravnih stupaca.

Na okomitoj osi nalazi se sedam kriterija, poredanih po globalnoj težini od
najveće (gore) prema najmanjoj (dolje), uz ispisanu težinu: Kvaliteta kamere
(gw=0,357), Pohrana podataka (0,179), Cijena (0,156), RAM (0,151), Baterija
(0,075), Ekran (0,061) i Težina (0,020). Središnja okomita crta označava
nulu/izjednačenost. Vodoravna os ispod nosi oznaku: lijevo „bolji Samsung Galaxy
A35", desno „bolji Honor 90".

**Zeleni stupci** usmjereni udesno znače da je Honor bolji na tom kriteriju, a
**crveni stupci** usmjereni ulijevo znače da je A35 bolji. Duljina stupca jednaka
je težinskom doprinosu razlike:

- **Kvaliteta kamere:** velik zeleni stupac udesno, +0,120 — Honorova najveća
  prednost (200 MP naspram 50 MP).
- **Pohrana podataka:** zeleni stupac +0,032 u korist Honora (512 GB naspram
  256 GB).
- **Cijena:** jedini crveni stupac, −0,017 u korist A35 (jeftiniji je: 314 €
  naspram 572 €).
- **RAM:** mali zeleni stupac +0,010 (12 GB naspram 8 GB).
- **Baterija, Ekran, Težina:** stupci su praktički nula (+0,000) — dva su uređaja
  na tim kriterijima gotovo izjednačena (oba 5000 mAh, sličan ekran).

Neto razlika iznosi **+0,146** u korist Honora. Graf jasno pokazuje da Honorova
ukupna prednost gotovo u cijelosti dolazi iz kamere, uz manji doprinos pohrane i
RAM-a, dok mu jedinu „protutežu" daje viša cijena — koja je, međutim, premala da
bi promijenila ishod.

## 3.6. 2D (datoteka `5_two_d.png`)

2D graf prikazuje uspješnost alternativa raspoređujući ih u jedan od četiri
kvadranta s obzirom na dva odabrana kriterija — ovdje **Kvaliteta kamere**
(vodoravna os) i **Performanse** (okomita os).

Svaka je alternativa prikazana kao **obojena točka (kružić) s crnim obrubom** i
pripadajućom oznakom (nazivom). Dvije sive crtkane crte (okomita na x ≈ 0,167 i
vodoravna na y ≈ 0,167) postavljene su na prosječne vrijednosti i dijele
prostor na četiri kvadranta. **Gornji desni kvadrant osjenčan je svijetlozeleno i
označen riječju „NAJBOLJI"** — u njega pada alternativa koja je istovremeno
iznadprosječna i po kameri i po performansama.

- **Honor 90 (plava točka)** smješten je krajnje desno (x = 0,446) i iznad
  prosjeka po performansama (y = 0,193) — jedini se nalazi u zelenom „najboljem"
  kvadrantu.
- **OnePlus 11 (žuta točka)** nalazi se visoko gore (y = 0,237, najviše po
  performansama) ali skroz lijevo (x = 0,112) — gornji lijevi kvadrant: odličan u
  performansama, slab u kameri.
- **Donji lijevi kvadrant** sadrži zbijenu skupinu: Samsung Galaxy A56
  (ljubičasta) i Samsung Galaxy A35 (roza) gotovo se preklapaju jer imaju jednaku
  kameru (50 MP) i vrlo slične performanse, a uz njih su Google Pixel 8
  (tirkizna) i iPhone 16 (zelena, najniže). Sve te alternative su ispodprosječne
  na oba kriterija.

**Povezanost s ostalim grafovima:** položaj Honora krajnje desno izravno
odgovara njegovu vrhu na Performance grafu i velikom zelenom stupcu kamere na
Head-to-head grafu. Činjenica da je jedini u zelenom kvadrantu vizualno sažima
cijelu analizu — Honor 90 nadmoćan je upravo na kombinaciji dvaju najvažnijih
kriterija (kamera i performanse zajedno nose 58,3 % odluke).

## 3.7. Sažetak interpretacije

Sve provedene analize osjetljivosti dosljedno upućuju na isti zaključak:

1. **Honor 90 je stabilan pobjednik.** Prvo mjesto zadržava u oba načina sinteze
   (Distributive i Ideal), pri pomacima težina od ±10 % (Dynamic), te kroz cijeli
   raspon težina svih kriterija osim u krajnostima (Gradient).
2. **Crossover analiza** pokazuje da bi Honor izgubio prvo mjesto u korist
   Samsunga A35 tek kad bi težina cijene narasla s trenutnih 0,156 na čak 0,643 —
   nijedan drugi kriterij ne može preokrenuti rezultat. Time je potvrđena
   iznimna otpornost rješenja.
3. **Izvor pobjede** jasno je vidljiv na Components, Performance i Head-to-head
   grafovima: Honorova prednost dolazi gotovo isključivo iz kvalitete kamere
   (200 MP) i velike pohrane (512 GB) — upravo onih značajki koje su za Ivanu kao
   grafičku dizajnericu najvažnije.

Stoga se kao optimalan izbor za Ivanu nedvosmisleno preporučuje **Honor 90**.
