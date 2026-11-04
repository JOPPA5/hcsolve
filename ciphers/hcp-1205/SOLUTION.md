# HCP1205 — Jolánka to Ferencz (Feri) Holecz: the two-hundredth card, the dance she will miss, and which cloth to buy

**Status: revised after reviews 1 and 2. The card is read whole; no clause stays unread, and the doubtful points are single signs, listed under Uncertainties.** Solver: Claude Opus 5.5, 2026-11-02. There is no earlier work on this number. The portal shows status *Not solved* and attaches no transcription or solution, so the transcription is mine (`work/ledger.txt`). No published solution of this card was found or used: I looked only at the portal capture and this repo and did not read the HistoCrypt article linked on the portal. The reading was not blind, since the family key was known. This is the reverse direction of the Feri to Jolánka cards: the writer signs Jolánka and the recipient Holecz Ferencz is the Feri of HCP1267.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" family key of HCP1216 and HCP1267, unchanged, with no new letter value. Accent and dot marks stand over the base sign and are used loosely. Only the addressee block and the printed verse on the picture side are in clear; the verse is given with the normalized text.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S | k | F-like | r |
| six | b | wave or small arch | l | right bowl | s |
| opposed bowls, also loop + v-stroke | cs | three short strokes | m | gamma/corner | t |
| double slash | d | two short strokes | n | plain cross x | u |
| three bars | e | loop + hook, descending | o, or with a dot pair ö | chevron | v |
| upright cross + | f | tall stroke + short tick | h, p | crossed curve, dotted | i |
| open loop | g | inverted T | j | crossed diagonal with tail | z |
| zigzag | y (*pletyka*, and in *ny*) | loop joined to descender | gy | | |

The tall + short sign stands for h and p, and the word decides which (`H`, `P` in the ledger). One token in row 06, the first sign of *nagyon*, has the same tall + short form and is read n by sense alone (`N`). The double slash stands for h five times (`D`). These calls rest on word sense. A clear digit 5 stands in row 08, as clear figures do in HCP1267. The m can be written with its first stroke free and the last two joined (rows 05, 25); it is still three strokes.

Layout: rows 01-27 fill the left half and run along the bottom; rows U1-U8 in the upper right are written with the card turned 180 degrees; rows S1-S8 sit under the stamp. At the divider the upright rows and the upside-down rows butt together, so the crops have to be split there (`work/croprot.py`). The order of the three blocks in the reading is mine: greeting first, signature last.

Type note (2026-11-03): the stamp is lifted and rows S1-S8 are written in cipher under it, so the register type is **MASC + Steganography** (was MASC).

## Stamp-box message (2026-11-03)

Stamp-box audit at the human's request (Claude Opus 5.5). The stamp is lifted; only a torn paper edge and green stamp traces remain at the bottom of the box. Under it are eight rows in the cipher signs only, no plain Hungarian (crops `work/stamp-2026-11-03/box_2x.png`, `rows0_3x.png`-`rows2_3x.png`). Re-checked against the ledger rows S1-S8 sign by sign; the reading below is the one already in this file and in `work/ledger.txt`, decoded by `work/decode.py`, which was left unchanged.

- Literal: `istenvele / edesemabol / dogviszont / letesra?üd / vözlöma / tavolbol / akiojnagyon / szeretijolanka`
- Hungarian: Isten vele, édesem, a boldog viszontlátásra. Üdvözlöm a távolból, aki oly nagyon szereti, Jolánka.
- English: God be with you, my sweet, until a happy reunion. I greet you from afar, she who loves you so much, Jolánka.
- Slovak: S Bohom, môj drahý, do šťastného videnia. Pozdravujem Vás zďaleka, tá, ktorá Vás tak veľmi ľúbi, Jolánka.

Unread: nothing at clause level. The s of S1 is faint over the stamp ghost, and S4 has one doubtful sign (`?`) inside *viszontlátásra*; both are already listed under Uncertainties.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1205/work/decode.py
```

It checks the SHA-256 of both source scans and both un-converted originals, decodes `work/ledger.txt` (1239 written signs, one character per sign), prints the literal text row by row, then the normalized text `work/normalized.txt`. The ledger was made by eye from enlarged crops of `work/hires/`, not by OCR.

## Literal decipherment (as printed by the command; ? flags a doubtful sign)

```
 01 szeretetkedvesferilapjaitmegkaptam
 02 amiketköszönökedesemmostkaptammeg
 03 magatole?ketszazadiklapotszeretnem
 04 tudnihogyenmenyitküldtemmaganakaz
 05 hiszemharmedresziteniselküldtem
 06 nagyonsajn?alomedesemhogyeztkel
 07 irnihogyamulatsagbanemmegyek
 08 pestremegyek5ikenotleszekde
 09 megnemtudokpontosidötirnihogy
 10 mikormegyekamamanaknemismondom
 11 amulatsagotmertmajdmegmegteszihogy
 12 pestreseengednehakedvevanedesugy
 13 bemehetmagaennelkülemismajdha
 14 vasutasneleszekhauganleszekmert
 15 megmindenmegtörtenhetamielnem
 16 multakormajdenismegyekavasutasok
 17 nakamulatsagokbaedesrem?enyem
 18 tudjaaztmaganagyonjolhaennem
 19 iromishogyenekemmindeghabarmij?en
 20 ruhabolat?ommivelennemaruhatnezem
 21 perszearokonsagkivancsimagaraeshanem
 22 ugyjelenikmegmintazizlesükszerint
 23 mindjartmegvanapletykaegyhetigidegeneknelleszekesmaremlitetemisma
 24 gathogyhamegengedikh?ogymaga{struck}megletigasonugymeginvitelomesaztfeleltehogy
 25 csakjöjöhozejokminthaothonramenena?gyonjonepekegyhetispedigaroko
 26 nalleszekotahone?nmagaegiszerabelatiskihivitadeezeknelnemjokeedvem
 27 bölleszekcsakhanemmegyekharagszanak
 U1 edesemharuhatveszsötetkeket
 U2 vagvilagosszürketvegyendeinkab
 U3 sötetkeketmertmaganakaza?la
 U4 legjobanazenizlesemszerint
 U5 csakneojandurvasötetkeket
 U6 mintlegutobvoltsimabkel
 U7 mebölneharagudjonekis
 U8 keresemertdehaszeretmegteszi
 S1 istenvele
 S2 edesemabol
 S3 dogviszont
 S4 letesra?üd
 S5 vözlöma
 S6 tavolbol
 S7 akiojnagyon
 S8 szeretijolanka
```

## Hungarian (normalized)

Szeretet[t] kedves Feri! Lapjait megkaptam, amiket köszönök, édesem. Most kaptam meg magától e kétszázadik lapot. Szeretném tudni, hogy én mennyit küldtem magának, azt hiszem, harmadrészét én is elküldtem. Nagyon sajnálom, édesem, hogy ezt kell írni, hogy a mulatságba nem megyek. Pestre megyek 5-ikén, ott leszek, de még nem tudok pontos időt írni, hogy mikor megyek. A mamának nem is mondom a mulatságot, mert majd még megteszi, hogy Pestre se engedne. Ha kedve van, édes, úgy bemehet maga én nélkülem is. Majd ha vasutasné leszek, ha ugyan leszek, mert még minden megtörténhet, ami el nem múlt, akkor majd én is megyek a vasutasoknak a mulatságokba, édes reményem. Tudja azt maga nagyon jól, ha én nem írom is, hogy énnekem mindegy, habár milyen ruhából látom, mivel én nem a ruhát nézem. Persze a rokonság kíváncsi magára, és ha nem úgy jelenik meg, mint az ízlésük szerint, mindjárt megvan a pletyka. Egy hétig idegeneknél leszek, és már említettem is magát, hogy ha megengedik, hogy maga meglátogasson, úgy meginvitálom, és azt felelte, hogy csak jöjjön hozzájok, mintha otthonra menne. Nagyon jó népek. Egy hét is pedig a rokonnál leszek ott, ahonnan maga egyszer a Bélát is kihívta, de ezeknél nem jó kedvemből leszek, csak ha nem megyek, haragszanak.

Upside-down block: Édesem, ha ruhát vesz, sötétkéket vagy világosszürkét vegyen, de inkább sötétkéket, mert magának az áll a legjobban az én ízlésem szerint. Csak ne olyan durva sötétkéket, mint legutóbb volt, simább kelméből. Ne haragudjon e kis kérésemért, de ha szeret, megteszi.

Under the stamp: Isten vele, édesem, a boldog viszontlátásra. Üdvözlöm a távolból, aki oly nagyon szereti, Jolánka.

Address in clear: Tek. Holecz Ferencz úrnak, M.Á.V. fékező, Iskola utcza 34, Rákos Palota Ujfalu.

Printed on the picture side, in clear: Két sziv ha földobog. / Két sziv ha földobog, álmodón, / Két sziv ha földobog, lángolón, / Felhők közé ne szállj .... / Dörén csalódni fáj.

## English

Beloved dear Feri! I have received your cards, for which I thank you, my sweet. I have just got this two-hundredth card from you. I would like to know how many I have sent you; I think I have sent a third of that too. I am very sorry, my sweet, to have to write that I am not going to the dance. I am going to Pest on the 5th and will be there, but I cannot yet write the exact time when I go. I am not even telling Mama about the dance, because she might even see to it that I would not be allowed to Pest either. If you feel like it, dear, you may go in without me. When I become a railwayman's wife, if I ever do, for anything can still happen that has not yet passed, then I too will go to the railwaymen's dances, my sweet hope. You know very well, even if I do not write it, that it is all the same to me in whatever clothes I see you, since I do not look at the clothes. Of course the relatives are curious about you, and if you do not appear as is to their taste, straight away there is gossip. I will be with strangers for a week, and I have already mentioned you, that if they permit you to visit me, I will invite you, and she answered that you should just come to them as if you were going home. Very good people. And for a week too I shall be at the relative's, there from where you once called Béla out too, but with these I shall not stay gladly; it is only that if I do not go, they will be angry.

Upside-down block: My sweet, if you buy clothes, take dark blue or light grey, but rather dark blue, because that suits you best in my taste. Only not such a coarse dark blue as last time; of smoother cloth. Do not be angry at this small request of mine, but if you love me, you will do it.

Under the stamp: God be with you, my sweet, until a happy reunion. I greet you from afar, she who loves you so much, Jolánka.

Address in clear: To the Honourable Ferencz Holecz, M.Á.V. [Hungarian State Railways] brakeman, Iskola utca 34, Rákospalota-Újfalu.

Printed verse: Two hearts, if they leap up. / Two hearts, if they leap up, dreaming, / two hearts, if they leap up, in flame, / do not soar among the clouds .... / to be foolishly disappointed hurts.

## Slovak

Milovaný drahý Feri! Vaše lístky som dostala, za ktoré ďakujem, môj drahý. Práve som od Vás dostala tento dvojstý lístok. Rada by som vedela, koľko som ich poslala ja Vám; myslím, že aj ja som poslala tretinu z toho. Veľmi ma mrzí, drahý, že musím napísať, že na zábavu nepôjdem. Pôjdem do Pešti piateho a budem tam, ale ešte nemôžem napísať presný čas, kedy pôjdem. Mame o zábave ani nehovorím, lebo by ešte spravila to, že by ma ani do Pešti nepustila. Ak máte chuť, drahý, môžete ísť dnu aj bezo mňa. Keď budem manželkou železničiara, ak vôbec budem, lebo sa ešte všetko môže stať, čo nepominulo, potom aj ja budem chodiť na zábavy železničiarov, moja sladká nádej. Veď to dobre viete, aj keď to nepíšem, že mne je jedno, v akom oblečení Vás vidím, keďže ja nepozerám na oblečenie. Pravdaže, príbuzní sú na Vás zvedaví, a ak sa neukážete tak, ako je podľa ich vkusu, hneď sú z toho klebety. Týždeň budem u cudzích ľudí a už som Vás spomenula, že ak dovolia, aby ste ma navštívili, tak Vás pozvem, a odpovedala, že nech len príde k nim, akoby šiel domov. Veľmi dobrí ľudia. A aj týždeň budem u príbuzného, tam, odkiaľ ste raz vyvolali aj Bélu, ale u týchto nebudem z dobrej vôle; len keď nepôjdem, budú sa hnevať.

Prevrátený blok: Môj drahý, ak si budete kupovať oblečenie, vezmite si tmavomodré alebo svetlosivé, ale radšej tmavomodré, lebo to Vám podľa môjho vkusu pristane najviac. Len nie také hrubé tmavomodré ako naposledy, z hladšej látky. Nehnevajte sa pre túto moju malú prosbu, ale ak ma ľúbite, urobíte to.

Pod známkou: S Bohom, môj drahý, do šťastného videnia. Pozdravujem Vás zďaleka, tá, ktorá Vás tak veľmi ľúbi, Jolánka.

Adresa v otvorenom texte: Váženému pánovi Ferenczovi Holeczovi, brzdár M.Á.V. [Maďarské štátne železnice], Iskola utca 34, Rákospalota-Újfalu.

Tlačený verš: Dve srdcia, keď zabúšia. / Dve srdcia, keď zabúšia, snívajúc, / dve srdcia, keď zabúšia, v plameni, / nevzlietni medzi oblaky .... / sklamať sa pochabo bolí.

## Uncertainties (all disclosed)

In order of weight:

1. **Row 25 `jonepek`** is read *jó népek* "good people". The o carries no visible dots, which gives *jó*, and the sign after e is the ordinary p, in the same form as *pedig* in that row. Sign form and word sense support each other. *Népek* has its é unmarked, as usual on this card.
2. **Row 26 `otahone?n`** is read *ot[t] ahon[n]an* = *ott, ahonnan*, "there, from where". This call rests on sense, because the vowel lies under a blot: one thin bar over a thick blob. The sign is either a (two bars, plain *ahonan*) or e (three bars, a dialect *ahonnen*); the word is the same, so the literal row keeps `e?` as a flagged sign. No sentence comes of *ott a hon én*. *Maga* is then "you", as everywhere on this card. *Kihívta* "called out" could mean summoned out or challenged; the Béla story is not known.
3. **Row 25 `na?gyon`**: the sign after n is two bars with a tick below, which may belong to another row. The word decides a. **Row 20 `lat?om`**: taken as t, not r (one clear bar, crossed by a gy tail above); the six strokes are m + m of *látom, mivel*. Sense decides.
4. **Row 08 `5`**: shape, with a flat top flag, plus sense; a y is not wholly excluded.
5. **Row 24 `h?ogy`**: a flagged x stands for the h of *hogy* as one composite sign. A sign after *maga* is cross-hatched by the writer and not read. The next sign shows two strokes, read m of *meg*. A third stroke may lie under the hatching, or the writer may have corrected a false start; *meglátogasson* is not in doubt. **Row 25 `jöjö hozejok`**: one sign (long + short slash) only, so the n of *jöjjön* is taken as dropped.
6. **Zigzag `Y`**: after review 1 the plain y value rests on *pletyka* alone; it also occurs in *ny* (rows 04, 17).
7. **Row 17 `rem?enyem`**: the third stroke of m has a small flag. Sense fixes *reményem*, which also occurs on HCP1216.
8. **Row 19 `mij?en`**: a sign like a tilted cross read as j (dialect *mijen* = *milyen*, parallel to *ojan*). Reading it as f gives no word.
9. **Row 06**: the n of *sajnálom* lies under a blot; **row 03**: the e after *magától* is partly under a blot. **U3 `a?la`**: the a of *áll* could be e. Sense-fixed.
10. Writer's spellings normalized: *harmed* → harmad, *kel* → kell, *ot* → ott, *ugan* → ugyan, *letigason* → látogasson, *invitelom* → invitálom, *kihivita* → kihívta, *keedvem* → kedvem, *oj* → oly, *inkab* → inkább, *simab* → simább, *mene* → menne, *jöjö* → jöjjön, *hozejok* → hozzájok, *menyit* → mennyit, *othonra* → otthonra, *rokonál* → rokonnál, *vag* → vagy. Accents are often invisible and are supplied. S1 begins with a faint *i s*, read by sense over the stamp ghost.
11. A purple pencil curve near the divider is not cipher. The date is not legible and is not claimed (the 5th has no month). The order of the three blocks is editorial. In the printed verse, *Dörén* is transcribed as it looks; I read it as *dőrén* "foolishly", taking the accent of the small type as two short strokes, and this is a reading by sense.

## Why I believe it is correct

The family key, with one clear digit added, gives Hungarian across all the signs, the few calls resting on word sense being listed above (the *ott, ahonnan* of row 26 is one of them, since its vowel is blotted), in three separate blocks and two orientations. Long stretches come out with no guidance from context: *kétszázadik lapot*, *vasutasné leszek*, *sötétkéket vagy világosszürkét vegyen*, *simább kelméből*, *kíváncsi magára*, *ne haragudjon e kis kérésemért, de ha szeret, megteszi*. The content fits HCP1267: Feri is a M.Á.V. brakeman at Rákospalota, so *vasutasné* and the railwaymen's dances are exactly right, and the printed address and signature confirm both parties. The name Béla and *a mama* are new here and were not forced from any sister card.

## Response to review 1

Verdict REVISE. All thirteen findings were checked on the reviewer's crops and on new crops in `work/crops2/` (`work/crop2.py`). I accept 1-9, 11 (with a fuller answer), 12 and 13, and went further than the review on 10. `python3 -I ciphers/hcp-1205/work/decode.py` was re-run after the changes: all hashes OK, no unknown token, and the literal block above is its output.

1. **Accepted.** Row 21 is `Persze`: tall + short, not m. Ledger, normalized text and all translations changed.
2. **Accepted.** U6-U7 is *simább kelméből*; U7 begins with a plain m and e. Old Uncertainty 3 removed.
3. **Accepted.** On `z8.png` the sign has a flat flag, belly and tail, a written 5. The ledger token is `5`, `decode.py` accepts it, and the text is *5-ikén*, with *még nem tudok*. Noted as shape plus sense (Uncertainty 4).
4. **Accepted.** On `z13.png` the loop is the tail of the gy that ends row 12 (`edesuG`). The token is deleted; the text is *Majd ha vasutasné leszek*.
5. **Accepted.** The last sign of row 25 is o: `aroko|nal`, *a rokonál*.
6. **Accepted.** `DoG` added at the end of row 24; *azt felelte, hogy*.
7. **Accepted.** Last sign k, `meGek`, `Haragszanak`, with the division *csak ha nem megyek, haragszanak*. The false *Haragszanál?* is gone from all translations.
8. **Accepted.** Row 05 is `Hiszem`; on `r5.png` the three strokes are a free stroke plus a joined pair.
9. **Accepted.** *és ha nem úgy jelenik meg ... mindjárt megvan a pletyka* is one conditional. Translations changed.
10. **Accepted, and pursued further.** New crops `t1`-`t4`, `w1`. The findings are:
    - First sign of `m?ene`: tall stroke plus a joined pair, three strokes, the same form as row 05. So it is a plain m and *menne* no longer rests on sense alone. This differs from the review, which read tall + short.
    - `egYin` goes. After `mene` come n, two bars (`a?`), gy, o, n: **nagyon**. Both Y and i were misreadings, and the review's o is confirmed.
    - `eGDetis` is *egy hét is*, as the review proposed. *Kegyed* is gone. The first part remains open (Uncertainty 1).
    - `otahon?en`: *ott, ahonnan*, with the blot as the vowel of a dialect *ahonnen*, and *maga* = "you". The *ő/én* problem disappears.
    - This reading is new and the review did not see it, so I hand it back through DONE2 and write no report or register entry yet.
11. **Accepted and resolved.** Row 20 is `lat?om` + `mivel`: the six strokes are m + m. Text: *habár milyen ruhából látom, mivel én nem a ruhát nézem*. This replaces *áron*.
12. **Accepted.** Row 24 token now `kH?oG`. Row 23 *egy*, row 25 *nagyon* and *egy*, and row 27 *megyek* use `G`; U2 *vag* and S3 *dog* stay plain `g` because the loop has no tail there. Uncertainty on Y rewritten, S7 normalized *oly nagyon*. Row 11 needs no slip: *mert majd még megteszi*. The review did not raise this; I changed it.
13. **Accepted.** The verse is transcribed from the original picture side and translated, with *Dörén* left as printed.

Sign count is now the figure in the Reproduction section. A further correction of my own: row 25 *jöjö* has one sign, not two, for n + h.

## Response to review 2

Verdict REVISE. I checked all six findings on the reviewer's crops and on new crops `work/crops2/r04a`, `r04b`, `r06a`. All are accepted; finding 3 goes a little further than the review. The fixes are local: three ledger tokens, one word division and the translation of one sentence. Rerunning `python3 -I ciphers/hcp-1205/work/decode.py` after the changes gives all hashes OK, no unknown token and 1239 signs, and the literal block above is its output. The verdict is REVISE and the reading of the card as a whole is not substantially changed, so this goes to the report and FINAL with no further round.

1. **Accepted.** On `g2.png` and `g6.png` the sign after *jon e* is a long stroke plus a short tick, the same form as the first sign of *pedig* in that row, and unlike the equal strokes of the n just before the bars. The ledger now has `P`, the text is *jó népek*, and all translations follow. *Jönnének* and *jönne nek(i)* are gone. Uncertainty 1 is now only a note on the sign and the unmarked vowels.
2. **Accepted.** The sentence is *Egy hét is pedig a rokonnál leszek ott, ahonnan ...*, with *pedig* as plain "and". No sign changes. The normalized text, English and Slovak are rewritten, and Slovak *hoci* is gone. The plan of the visit now holds: a week with strangers who are good people, a week with the relative, and only the second is unwelcome.
3. **Accepted, and pursued further.** Row 14 `ugan` is a plain pair (`k4.png`). In row 04, *tudni* and *mennyit* also look like plain pairs on my crops (`r04a`, `r04b`), the first stroke hardly taller, so both become `n`. Only row 06 *nagyon* has a true tall + short form (`r06a`). That leaves one token, read n by sense, and "also n" is out of the key table. The ledger header and key note say this.
4. **Accepted.** The status line now says the card is read whole. `Why I believe` names *ott, ahonnan* as sense-based.
5. **Accepted.** On `h1.png` the blot shows one thin bar over one thick blob, so a is not excluded. Uncertainty 2 states a or e, with the word unchanged. The normalized *ahonnan* needs no dialect form.
6. **Accepted.** On `s1.png` a third stroke under the hatching cannot be excluded. Uncertainty 5 says so, and the ledger header no longer counts this token as a firm two-stroke m.

One change of my own: the printed verse word *Dörén*, which I had left unexplained, is read *dőrén* "foolishly" (crop `work/crops2/verse.png`), so no word of the card stays un-understood. The verse is in clear and no cipher sign is affected.

Round 1's note that the first part of row 25 "remains open" is superseded by finding 1.
