# HC374: madridský telegram

Obnovené telo správy a pracovný kľúč Kryha. Dešifrovaných je 80 znakov. KIDAH je spoločný indikátor rovnakého štartu ako v 373; spôsob kódovania nastavenia jeho písmenami zostáva otvorený. Historické neistoty sú výslovne označené.

## Pôvod a obsah

MZV 80174/1944, 20. máj 1944, Šulík pre slovenské vyslanectvo v Madride. Slovenský národný archív, MZV, škatuľa 42. Portál pri získaní uvádzal Not solved. Sken obsahuje počet 85 a 17 skupín po 5 písmen. Názov opisuje žiadosť o opakovanie 15 posledných skupín 80172; nový 80-znakový blok nie je vyhlásený za presne rovnaký 75-znakový výrez.

Zverejnený vyriešený telegram 373 (80172/1944, 17. máj 1944) poskytol archívny otvorený návrh a šifrotext. Jeho záverečná veta slúžila ako známy text na obnovu strojového kľúča. Obchodný obsah je týmto zdrojom doložený a už bol zverejnený; nové je získanie kľúča a jeho prenos na 374.

## Doslovný výstup z nezávislého prepisu

```text
AUPOZORNUIESPANLELSKEPROTIBODAVKYUZPEVNEKUPENENAZAKLADEPOVODNYCHCIENCELULOZYXXXX
```

Samostatný indikátor: KIDAH, spoločný s 373 a rovnakým štartom stroja. Recenzovaný znak 35 je N; alternatíva M dáva PROTIBODVVKY. SPANLELSKE a PROTIBODAVKY zachovávajú dve chybné písmená tejto kópie. Zdroj sa neupravuje podľa správnych slov. XXXX je výplň X doložená vetnými X a záverečnými XX v 373.

## Čitateľný obsah doložený návrhom 373

A upozorňuje španielské protidodávky už pevne kúpené na základe pôvodných cien celulózy.

Význam: španielske protidodávky sú už pevne kúpené podľa pôvodných cien celulózy. Anglicky: And points out that the Spanish counter-deliveries have already been firmly purchased on the basis of the original cellulose prices. Toto je obsahová obnova podľa zverejneného návrhu, nie doslovný strojový výstup bez chýb.

## Ako sa kľúč získal

Posledná 186-písmenová veta 373 neobsahuje čísla. Jej posúvanie cez celý šifrotext a skúšanie periód 2-52 dáva jeden výsledok z 94 656 prípadov: J na I, bez Q, posun 462, perióda 23. Všetkých 183 neistotami nevynechaných rovníc súhlasí. Tri nezávislé fyzické kontrolné správy sa obnovia celé. Dva odlišné audity potvrdili jednu kompatibilnú 23-stopovú masku na 52-otvorovom kolese.

Pri 374 je zo 598 dvojíc fázy a posunu jednoznačne najlepší prenos 3/8: recenzované čítanie súhlasí v 74 zo 76 obsahových písmen; ďalší kandidát iba 21, medián 3. Nezávislé čítania vznikli pred znalosťou kľúča. Ten istý kľúč otvára celý 645-znakový šifrovaný blok 373:459 znakov mimo použitého 186-znakového úseku. Súvislá slovenčina s vypísanými číslami a vetnými X je silné nezávislé potvrdenie; jednotlivé zdrojové chyby sú zachované.

## Pracovný fyzický kľúč

P a O určujú súradnicu písmena 0-25; O(c)=P(p)+d modulo 26. P(A)=O(A)=0 je súradnicová konvencia. Tabuľka dopĺňa nepoužité F/G/J/Q/W do permutácie; tieto historické názvy sa nezískali. M 24 pochádza z nezávislého známeho MADRID v 373, X 19 potvrdzujú tamojšie vetné hranice a výplň XX. Nepoužité doplnenia nemenia telo 374.

| Písmeno | A | B | C | D | E | F | G | H | I | J | K | L | M |
| P | 0 | 11 | 14 | 1 | 20 | 4 | 9 | 2 | 13 | 15 | 16 | 3 | 24 |
| O | 0 | 4 | 1 | 21 | 8 | 3 | 19 | 15 | 13 | 18 | 25 | 10 | 22 |

| Písmeno | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| P | 7 | 17 | 25 | 18 | 21 | 10 | 5 | 12 | 6 | 22 | 19 | 8 | 23 |
| O | 16 | 2 | 12 | 5 | 23 | 7 | 20 | 11 | 14 | 17 | 24 | 9 | 6 |

Vybrané otvory v poradí od prvého znaku tela, NULOVÉ indexovanie 0-51 (pre čísla 1-52 pripočítajte 1):

```text
34 37 40 42 44 45 47 48 49 51 2 4 5 8 11 13 17 20 21 24 26 29 31
```

Počiatočný posun 1 modulo 26 (ekvivalent 27). Po každom znaku sa ide k nasledujúcemu vybranému otvoru po susedných hranách. Ich 52 vzdialeností:

```text
4 3 4 3 3 3 4 3 4 4 3 3 3 3 4 4 3 3 4 3 3 4 3 3 4 3 3 4 4 4 3 3 4 3 3 3 4 3 4 3 3 4 5 3 3 3 3 4 3 3 4 5
```

Súčet jedného obehu je 179. Pri dekódovaní sa od O odčíta aktuálny posun a v P sa vyhľadá výsledná súradnica. Historická poloha ručičky, význam úvodného hesla a každý nepoužitý názov abecedy zostávajú nepreukázané. Jedinečnosť masky platí iba pre uvedenú geometriu a obnovený rozvrh.

## Opakovateľnosť a nezávislé overenie

```text
python3 ciphers/hcp-374/work/decrypt.py
```

Spustiť z koreňa repozitára. Python overí hash pôvodného JPEG a ručného prepisu; nerobí OCR. Vráti všetkých 80 písmen a indikátor zvlášť. --alternate-35-m volí druhé čítanie. Samostatné verify.py používa absolútne súradnice a počet obehov. Interný audit GPT-6.1 Sol použil vlastný priebežný mechanický algoritmus bez importu týchto funkcií: obe 80-písmenové verzie presne reprodukujú skutočný prepis.

## Recenzia a hranice výsledku

Claude Opus 5.5: ACCEPT, bez potreby druhého kola. Vlastný decoder overil celé telo, 598 nastavení a celý blok 373 mimo prvého rámca. Zapracované: N na 35 so zachovaným M, silný test 459 znakov mimo fitu, doložené X a dve chyby tejto kópie. Pôvodné 15 skupín sa pri opakovaní rozšíria na slovo a zaokrúhlia na 16; ide o vysvetľujúci úsudok. Plné odpovede sú v SOLUTION.md.

Zdroj 9/25/60 čitatelia preferujú G/Q/V. Na 35 je predvolené staršie nezávislé N, novší čitateľ M zostáva alternatívou. Zdroj 21 S a 32 L sa nemenia na W/A: ide o chyby tejto kópie, s neurčeným pôvodom. Aktualizovaná recenzia potvrdzuje KIDAH a spoločný štart (prvá vybraná stopa, posun 1). V 373 veta začína až po 567 znakoch, v 374 znova od štartu: z 76 šifrových písmen nesúhlasí žiadne, z otvorených 74. Text bol zašifrovaný znova, nie prekopírovaný; kódovanie indikátora zostáva otvorené. Register bez osobitného súhlasu človeka nevzniká, obsah už bol publikovaný.

Zdroje: crypto.hcportal.eu/dashboard/cryptograms/374 a /373, všetky tri pôvodne zobrazené záložky a prílohy zaznamenané v SOURCES.md; Antal/Zajac/Grošek, Diplomatic Ciphers Used by Slovak Attaché During the WW 2, HistoCrypt 2020; geometria Callimahos, Military Cryptanalytics Part III, §52. Hlavný solver OpenAI GPT, matematická obnova a interné audity GPT-6.1 Sol; externý reviewer podľa REVIEW 1.md.

## Pôvodný dokument 374

Nezmenený archívny obraz zo zaznamenanej portálovej prílohy. Ručný prepis a alternatívy sú od obrazu oddelené.

![Pôvodný sken](/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-374/source/cryptogram.jpg)
