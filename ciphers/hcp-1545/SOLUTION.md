# HCP1545 / pc_hcp_226 — complete reading (one non-key mark disclosed)

> **Current status (2026-10-29, after review 1, verdict ACCEPT):** complete reading of all 362 key signs; one small dotted oval after PŘIJEDE (U01) is an unidentified mark, probably not a letter. The Slovak sections below are the earlier solver's (OpenAI GPT) record and describe the state before the completion section; where they say "partial", "nevyriešené" or "no marker/PDF/register", they are superseded by the completion section and by "Response to review 1" at the end.


Ide o monoalfabetickú substitúciu zo skupiny pohľadníc Anne Tichej. Základný text je čitateľný vo všetkých 15 riadkoch (12 hlavného textu a 3 otočeného okrajového dodatku). Koniec slova v R08 zostáva nevyriešený; preto toto nie je bezvýhradné úplné rozlúštenie. Zdrojový nezvyčajný tvar `KOLUBENKU` ani oslovenie `ANUNKO` sa neopravujú podľa gramatického očakávania.

## Pôvod a hranice tvrdenia

Portál označoval pohľadnicu `Not solved`, čeština, súkromná zbierka, dátum 8. 8. 1903, príjemkyňa Anna Tichá. General, Description a Attachments prečítal hlavný riešiteľ v zobrazenom rozhraní; priložené nebolo individuálne riešenie ani transkripcia. Register bol kontrolovaný v rozsahu opísanom v SOURCES.md; neprítomnosť cieľa nie je dôkaz svetovej novosti.

Kľúč NIE JE nový objav na tomto texte. Pred transkripciou bol dostupný verejný **čiastočný** výskum [Anna Tichá postcards](https://maxim-egorov.dev/research/anna-ticha-postcards/) a rodinný kľúč už použitý pri HCP1527. Ich zachované súbory, verejný fotografický referenčný pc199 a provenance.json majú v work/reference-sha256.json kontrolné odtlačky. Pc199 obsahuje v publikovanom čítaní RUDOLFINA; tento cieľ nevyžaduje nový zriedkavý znak F. Nejde o slepé objavenie kľúča ani nezávislú kontrolu iným poskytovateľom. Cieľový plaintext vopred poskytnutý nebol. Hlavný riešiteľ a pomocný riešiteľ spolupracovali na riešení; žiadny recenzent ani watcher sa nespustil.

Adresa mimo šifry znie: „Velectěná Slečna / slečna Anna Tichá / učitelka t. č. / v Pelhřimově.“ Osobitne „Vlastnoručně dodati!“ Na obrazovej strane je bežným písmom dátum 8./VIII.1903. Z textu podpisu sa neodvodzuje občianske meno odosielateľa.

## Kľúč a postup

Znakové menovky sú pracovný prepis tvarov rukopisu. Tlačené písmeno vľavo nie je plaintext.

| Znak | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | b | c | d |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Čítanie | Y | U | O | I | E | A | J | L | P | S | T |

| Znak | f | g | h | m | n | p | q | r | s | t | ř |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Čítanie | V | K | R | N | M | B | Z | H | C | D | CH |

`7` je dohodnutá menovka J, `ř` dohodnutá menovka zvýrazneného CH; ide o tie isté menovky ako v predchádzajúcom rodinnom kľúči. Vo výpočte nie sú prípustné ďalšie voľné aliasy. Jediný znak `ř` dáva dvojicu CH. Zachytené čiarky a háčiky sa neprenášajú automaticky na modernú diakritiku. Základné čítanie a redakčná čeština sú preto oddelené.

Originál sa nemení. Manuálna transkripcia má zdrojové obdĺžniky a orientácie v work/transcription.json, obrázky všetkých riadkov R01–R12/M01–M03 a oba indexed-*.png. Hlavný text používa ROTATE_270, okrajový dodatok ROTATE_180. Obdĺžniky sa prekrývajú tam, kde do susedného riadka zasahujú horné a dolné slučky. work/positions.csv indexuje každý prepísaný znak a zvlášť nevyriešenú oblasť; nejde o automatické OCR ani o tvrdenie individuálnych presných pixelových rámčekov každého znaku.

Jeden príkaz z koreňa repozitára:

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1545/work/decode.py
```

Číta nemenný zdroj, vopred pevný kľúč a manuálnu transkripciu; vypíše celé dostupné základné čítanie. Kontroluje odtlačky 3 zdrojov a 4 referencií, zhodu kľúča s predcieľovým kľúčom, všetkých 15 výrezov opätovným vytvorením v pamäti, všetky indexy, uložený plaintext a skutočné kódovanie celého dekódovaného reťazca pevným inverzným kľúčom (CH ako dvojpísmeno). Reverzné overenie si neučí prevod z jednotlivých cieľových pozícií. Tieto kontroly dokazujú konzistentnosť záznamu, samy osebe nedokazujú správnosť manuálneho čítania z obrazu.

## Doslovný základný český plaintext

Interpunkcia, medzery a nedokončené úvodzovky sú manuálne prečítané, nepočítajú sa medzi aktívne znaky. `UPRIM- / NYCH` je rozdelené na hrane dvoch okrajových riadkov. `[U01]` nie je jeden domyslený znak: je to nevyriešená koncová oblasť s odhadom rozsahu **1 až 2 šifrové jednotky**, pozri nižšie.

```text
TISICERY DIK, ZLATO
MOJE, ZA DRAHY LISTEK.
ZAJISTE DOSTALA JIZ V PATEK
MUJ LISTEK, JENZ SE KRIZOVAL
S TVYM "NEZAPOMINAM, DRAHOUSKU,
ANI CHVILKU, NYBRZ STALE NA SVOJI
KOLUBENKU VRELE VZPOMINAM. JAK
STOJI VASE ZALEZITOST? PRIJEDE[U01]
DO PRAHY? MNE TAKE, ANUNKO, CAS
LETEM UBIHA. PRACUJI VE
VOLNYCH CHVILICH PILNE NA DEJINACH
CECILIE, ABYCH JE MOHL JESTE DO
KONCE PRAZDNIN K TISKU PRIPRAVITI. TISIC UPRIM-
NYCH PUS POSILA TVUJ PEPOUS, TESICI SE NA OPETNY
DRAHY LISTEK.
```

## Redakčné české čítanie

Nasledujúca verzia dopĺňa bežnú českú diakritiku, veľké písmená a spája riadky. Ide o redakciu, nie druhý nezávislý dešifrovací výsledok. Neopravuje KOLUBENKU, ANUNKO ani U01. Koncové úvodzovky nie sú doplnené, pretože ich zdrojové umiestnenie nie je zreteľné.

Tisícerý dík, zlato moje, za drahý lístek. Zajisté dostala již v pátek můj lístek, jenž se křižoval s tvým „Nezapomínám, drahoušku, ani chvilku, nýbrž stále na svoji kolubenku [sic] vřele vzpomínám. Jak stojí vaše záležitost? Přijede[U01] do Prahy? Mně také, Anunko, čas letem ubíhá. Pracuji ve volných chvílích pilně na dějinách Cecilie, abych je mohl ještě do konce prázdnin k tisku připraviti. Tisíc upřímných pus posílá tvůj Pepouš, těšící se na opětný drahý lístek.

## Slovenský preklad

Tisícoraké vďaka, zlato moje, za drahý lístok. Iste si už v piatok dostala môj lístok, ktorý sa skrížil s tvojím „Nezabúdam, miláčik, ani na chvíľu, ale stále vrúcne spomínam na svoju kolubenku [zdrojový tvar]. Ako stojí vaša záležitosť? Príde[U01] do Prahy? Aj mne, Anunko, čas letí. Vo voľných chvíľach usilovne pracujem na dejinách Cecilie, aby som ich mohol ešte do konca prázdnin pripraviť do tlače. Tisíc úprimných bozkov posiela tvoj Pepouš, ktorý sa teší na ďalší drahý lístok.

Slovo „Cecilie“ sa bez ďalšieho historického dôkazu neurčuje ako osoba, časopis ani konkrétne dielo. Pri U01 nemožno s istotou preložiť osobu a číslo slovesa; doslovný čiastočný preklad to zachováva.

## Neistoty a kontrola kritických miest

1. **R08, U01:** za jasným `bh475t5` = PRIJEDE je zaokrúhlená koncová skupina (približne x605–623,y824–843 v ROTATE_270). Tvar nebol spoľahlivo prečítaný ako jeden ani dva znaky. `d5` by dalo TE a slovo PRIJEDETE, ale jazyková pravdepodobnosť nedovoľuje túto sekvenciu vložiť do doslovnej transkripcie. Údaj o rozsahu nie je presný počet znakov. Výrez R08.png a focused-controls.png umožňujú ďalšie čítanie.
2. **R07 KOLUBENKU:** prepis `g382p5mg2` dáva týmto kľúčom KOLUBENKU. Začiatočný g/K je porovnaný s posledným znakom v `t4g` = DIK a s `gh4q3f68` = KRIZOVAL. Holubenku je jazykovo príťažlivá oprava, ale nie doslovný výsledok použitého prepisu. Toto miesto zostáva paleograficky citlivé.
3. **R09 ANUNKO:** `6m2mg3` má jasnú tretiu jednotku 2/U; nevkladá sa I, aby vzniklo Aninko. Ide o čítanie zdrojového oslovenia, nie občianske meno.
4. **M02 PEPOUS:** `b5b32c` je PEPOUS, redakčne Pepouš. Rovnakokartové kontroly 5/E, 6/A a c/S sú uložené vo focused-controls.png/.json. Tvar sa neopravuje na Papouš. Podpis sám neurčuje osobu odosielateľa.
5. Listy tlačenej kytice prekrývajú časti niektorých slov. Nie je prípustné označiť celé dotknuté riadky za nečitateľné; zvyšné časti slučiek boli ručne sledované. Prepis nie je tvrdením, že tlač prekrýva všetky znaky alebo že nejasné ťahy sú zrušené znaky. Žiadne zrušenie šifrového znaku nie je založené.
6. Diakritika, interpunkcia a prípadné uzavretie citácie nie sú v základnom písmenovom výstupe kryptograficky dokázané. Všetky zachované hlavné aj okrajové riadky sú zahrnuté; presný čistý úplný text sa netvrdí.

Výpočet overil 362 mapovaných šifrových jednotiek, z nich 7 CH, a jednu zvlášť indexovanú nevyriešenú oblasť. Súlad dlhého textu, kontextu adresátky, bežného dátumu, podoby listu a podpisu výrazne podporuje prenos kľúča. Kontroly nenahrádzajú potrebné dočítanie U01 ani nezávislé odborné paleografické overenie. Nevznikol stavový marker, PDF ani zápis do registra.

## Root source QA and register refresh - 2026-10-28

Root inspected both original sides, the twelve body rows and three margin rows, complete message regions, R08 and focused same-card K/E/A/nickname/signature controls. The initial loop in KOLUBENKU supports the recorded g/K class; HOLUBENKU is not inserted. The final R08 oval remains unassigned with unknown exact extent. Its locator was expanded down to y847 to avoid clipping its lower edge; the full R08 crop already included it. No plaintext, count or source pixel changed. The result remains partial.

Fresh rendered register check now has 193 contributions and 159 distinct HC Portal source IDs; this target is still absent. Ten new pc420–429 registrations are excluded in skip.txt. The current snapshot is batches/easy-2026-10-28/register-snapshot-193.json. This supersedes only the earlier register count, not source metadata or a global novelty claim. Root/helper checks are solver collaboration, not independent provider review. Hashes and inverse checks test record consistency, not automatic handwriting accuracy. No watcher or reviewer was launched.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading of the message, handed to review (DONE1).** Every
word of the 15 rows decodes with the fixed family key; one small mark is not
a key letter and is disclosed below. No plaintext changed.

**U01 (R08, after `bh475t5` = PRIJEDE).** In work/R08-detail.png the closing
group is one small oval with a dot inside (⊙). None of the 22 family key
signs has this shape, and no family card (1525–1556) assigns it a letter.
The reading **PŘIJEDE do Prahy?** (3rd person: “Will [she] come to Prague?”)
is grammatical as it stands, and this card addresses Anna in the 3rd person
elsewhere (“Zajisté dostala již v pátek můj lístek”, without *jsi*); sibling
card HCP1535 has “Anunka mi určitě slíbila, že … přijede do Prahy”. So no
letter is missing. The oval is treated as a non-letter mark. *PŘIJEDEŠ*
would need an Š sign that the key does not have.

Editorial Czech of the sentence therefore reads: “Jak stojí vaše záležitost?
Přijede do Prahy?” The decoder still prints `[U01]` so that the mark stays
visible in the literal output. KOLUBENKU (literal; probably *holoubenku*,
“little dove”) and ANUNKO stay as written.

Reproduce (from the repo root):

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1545/work/decode.py
```

Credit: the family key comes from earlier family cards and from the published
partial study by Maxim Egorov (see above). It was not discovered on this card.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) verdict **ACCEPT**, four minor findings. Response by Claude Opus 5.5 as solver, 2026-10-29. No decoded letter changed.

1. **U01 is a non-letter by interpretation, not proof — agreed, wording fixed.** Re-checked on review/work/r08_end.png (8x): after `bh475t5` = PRIJEDE there is one small closed oval with a dot inside; it matches none of the 22 key signs. The final report and the decoder now call it "unidentified mark; probably not a letter" and keep `[U01]` visible in the literal output. The alternative PŘIJEDEŠ is mentioned as not excluded, with the counter-evidence that Š is written with the ordinary S sign `c` elsewhere on this card (PEPOUŠ = `b5b32c`). The meaning ("will [you/she] come to Prague?") is the same either way.
2. **Contradictory status — fixed.** A status note at the top of this file now states the single harmonized status (complete reading of all key letters, one unidentified non-key mark) and marks the earlier "partial / no marker" statements as superseded. The two summary lines printed by work/decode.py were changed to the same wording (only the printed messages; no transcription, key, index or hashed record file changed). The positions.csv status label `unknown_region_1-2_units` is hashed in work/record-sha256.json and was left as a legacy label; the decoder output says so. Re-ran `python3 -I ciphers/hcp-1545/work/decode.py`: exit 0, the same 15 plaintext lines, 362 mapped units, 7 CH.
3. **Háček on E in KOLUBENKU — agreed.** review/work/r07_start.png clearly shows a háček over the `5` of `p5`. The editorial Czech now reads *koluběnku* [sic] (the writer apparently meant *holoubě / holoubek* "little dove"); the cipher letters are unchanged.
4. **"Cecilie" — noted.** The report mentions, as a possibility only, that "dějiny Cecilie" could refer to a history of a St Cecilia (Cecilian church-music) society or similar; it is not asserted.
