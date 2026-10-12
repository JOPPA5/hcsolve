# HC374: madridský telegram

Obnovené telo správy a pracovný kľúč Kryha. Dešifrovaných je 80 znakov; úvodných KIDAH zostáva zachovaným rámcom s neznámym významom. Ide o čiastočné historické tvrdenie s výslovne označenými neistotami.

## Pôvod a obsah

MZV80174/1944, 20. máj1944, Šulík pre slovenské vyslanectvo v Madride. Slovenský národný archív, MZV, škatuľa42. Portál pri získaní uvádzal Not solved. Sken obsahuje počet85 a17 skupín po5 písmen. Názov opisuje žiadosť o opakovanie15 posledných skupín80172; nový80-znakový blok nie je vyhlásený za presne rovnaký75-znakový výrez.

Zverejnený vyriešený telegram373 (80172/1944, 17. máj1944) poskytol archívny otvorený návrh a šifrotext. Jeho záverečná veta slúžila ako známy text na obnovu strojového kľúča. Obchodný obsah je týmto zdrojom doložený a už bol zverejnený; nové je získanie kľúča a jeho prenos na374.

## Doslovný výstup z nezávislého prepisu

```text
AUPOZORNUIESPANLELSKEPROTIBODVVKYUZPEVNEKUPENENAZAKLADEPOVODNYCHCIENCELULOZYXXXX
```

Samostatný zachovaný rámec: KIDAH. Pri alternatíve35N sa PROTIBODVVKY zmení na PROTIBODAVKY. SPANLELSKE a písmeno B v PROTIBOD... zostávajú doslovnými nezrovnalosťami; zdroj sa neupravuje podľa správnych slov. XXXX pomenúva štyri opakované súradnice19 hypotézou výplne X.

## Čitateľný obsah doložený návrhom373

A upozorňuje španielské protidodávky už pevne kúpené na základe pôvodných cien celulózy.

Význam: španielske protidodávky sú už pevne kúpené podľa pôvodných cien celulózy. Anglicky: And points out that the Spanish counter-deliveries have already been firmly purchased on the basis of the original cellulose prices. Toto je obsahová obnova podľa zverejneného návrhu, nie doslovný strojový výstup bez chýb.

## Ako sa kľúč získal

Posledná186-písmenová veta373 neobsahuje čísla. Jej posúvanie cez celý šifrotext a skúšanie periód2-52 dáva jeden výsledok z94 656 prípadov: J na I, bez Q, posun462, perióda23. Všetkých183 neistotami nevynechaných rovníc súhlasí. Tri nezávislé fyzické kontrolné správy sa obnovia celé. Dva odlišné audity potvrdili jednu kompatibilnú23-stopovú masku na52-otvorovom kolese.

Pri374 bol zo598 dvojíc fázy a posunu jednoznačne najlepší prenos3/8: pred novým prepisom71 zo76 publikovaných obsahových písmen, ďalší kandidát iba21. Nový prepis bol vytvorený z obrazu pred konzultáciou tohto výstupu.

## Pracovný fyzický kľúč

P a O určujú súradnicu písmena0-25; O(c)=P(p)+d modulo26. P(A)=O(A)=0 je súradnicová konvencia. Tabuľka dopĺňa nepoužité F/G/J/Q/W do permutácie; tieto historické názvy sa nezískali. M24 pochádza z nezávislého známeho MADRID v373, X19 je hypotéza výplne. Nepoužité doplnenia nemenia telo374.

| Písmeno | A | B | C | D | E | F | G | H | I | J | K | L | M |
| P | 0 | 11 | 14 | 1 | 20 | 4 | 9 | 2 | 13 | 15 | 16 | 3 | 24 |
| O | 0 | 4 | 1 | 21 | 8 | 3 | 19 | 15 | 13 | 18 | 25 | 10 | 22 |

| Písmeno | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| P | 7 | 17 | 25 | 18 | 21 | 10 | 5 | 12 | 6 | 22 | 19 | 8 | 23 |
| O | 16 | 2 | 12 | 5 | 23 | 7 | 20 | 11 | 14 | 17 | 24 | 9 | 6 |

Vybrané otvory v poradí od prvého znaku tela, NULOVÉ indexovanie0-51 (pre čísla1-52 pripočítajte1):

```text
34 37 40 42 44 45 47 48 49 51 2 4 5 8 11 13 17 20 21 24 26 29 31
```

Počiatočný posun1 modulo26 (ekvivalent27). Po každom znaku sa ide k nasledujúcemu vybranému otvoru po susedných hranách. Ich52 vzdialeností:

```text
4 3 4 3 3 3 4 3 4 4 3 3 3 3 4 4 3 3 4 3 3 4 3 3 4 3 3 4 4 4 3 3 4 3 3 3 4 3 4 3 3 4 5 3 3 3 3 4 3 3 4 5
```

Súčet jedného obehu je179. Pri dekódovaní sa od O odčíta aktuálny posun a v P sa vyhľadá výsledná súradnica. Historická poloha ručičky, význam úvodného hesla a každý nepoužitý názov abecedy zostávajú nepreukázané. Jedinečnosť masky platí iba pre uvedenú geometriu a obnovený rozvrh.

## Opakovateľnosť a nezávislé overenie

```text
python3 ciphers/hcp-374/work/decrypt.py
```

Spustiť z koreňa repozitára. Python overí hash pôvodného JPEG a ručného prepisu; nerobí OCR. Vráti všetkých80 písmen a rámec zvlášť. --alternate-35-n volí druhé čítanie. Samostatné verify.py používa absolútne súradnice a počet obehov. Interný Sol6.1 audit použil vlastný priebežný mechanický algoritmus bez importu týchto funkcií: obe80-písmenové verzie presne reprodukujú skutočný prepis.

## Recenzia a hranice výsledku

Externá recenzia prebieha. Tento pracovný návrh nie je konečný report ani potvrdenie úplného historického riešenia.

Zdroj9/25/60 nezávislý čitateľ preferuje G/Q/V. Zdroj35 má spor M/N. Zdroj21S a32L sa nemenia na W/A len na získanie správnych slov. Príčina doslovných chýb nie je určená. Záznam do registra sa nevytvára pre toto čiastočné tvrdenie odvodené zo zverejneného kontextu.

Zdroje: crypto.hcportal.eu/dashboard/cryptograms/374 a /373, všetky tri pôvodne zobrazené záložky a prílohy zaznamenané v SOURCES.md; Antal/Zajac/Grošek, Diplomatic Ciphers Used by Slovak Attaché During the WW2, HistoCrypt2020; geometria Callimahos, Military Cryptanalytics Part III, §52. Hlavný solver OpenAI GPT, matematická obnova a interné audity GPT-6.1 Sol; externý reviewer podľa REVIEW1.md.

## Pôvodný dokument374

Nezmenený archívny obraz zo zaznamenanej portálovej prílohy. Ručný prepis a alternatívy sú od obrazu oddelené.

![Pôvodný sken](../source/cryptogram.jpg)
