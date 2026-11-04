# HCP1226 — Feri to Jolánka Tóth: "I take your request as a command"

**Status: complete reading of the message. Every sign of row 27 is clear, but one clause there rests on two supplied endings, *modorom[mal]* and *elége[dve]* (item 1). Final after review 2, which asked for this one change to the clause.** Written 2026-11-02 by Claude Opus 5.5. There is no earlier work on this number. No external plaintext was used; the portal shows status Not solved and attaches no transcription or solution, and I searched for no published solution of this card beyond that (the orchestrator's AI-register check found no record).

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family.

*Type note (2026-11-03): register type is now **MASC + Steganography**: seven rows of the message are written in the stamp box, under the (now lifted) stamp; see "Stamp-box message (2026-11-03)" below.* The key was transferred unchanged from the finished card HCP1216 (also 1213, 1217, 1218, 1243, 1301); nothing was reconstructed here. The card has no word division. Accents stand above the signs as marks.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S-shape | k | F-like | r |
| six | b | wave | l | right bowl (also a heavy 9-shape, rows 7, 21) | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| short tick + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short (h/p near-homograph) | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | opposed bowls | cs | | |

Dots over o/u give ö/ü and ő. Here gy is written as two signs g + y, and old-style "cz" as left bowl + z (*piczi*).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1226/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (one token per written sign: 28 main rows, the turn up the right edge, 7 rows on the stamp) and prints the literal rows, then `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the un-converted scan `work/hires/*_adr.jpg`; `work/crop.py` makes such crops. The printed triangle and the HC Portal mark were separated from the ink by colour channel. It is not OCR, and word expectations did guide me on the near-homographs named below.

## Literal decipherment (as printed by the command)

`{x}` is a value taken from word sense, `[#]` a scribbled sign. Plain h in the output stands for the h/p sign, so *szépen* prints as *szehen*.

```
01 szeretetedesegyetlenre          15 viszacsokolni{d}esa{j}nosezt
02 menyembecsessoraitmeg           16 megsokatehetemijameg
03 ka{p}tammitköszonoksze           17 edesemmikorjönhalehetki
04 hensajnalatomatkelki            18 megyekelejeb[#]azalloma
05 fejeznemhogynemjönmulat         19 sonkedvesemekeresetmin
06 sagba{d}eigyisjocsakazafö       20 digharancsnakveszemmertcsak
07 hogyviszontlathatom             21 maganakelekesörülaszivem
08 higyjeeledesemmikorso           22 hamagaszavaitteljesithe
09 raitolvasomkimondhatat          23 temlegjobszeretnemmar
10 lanerzesfogtaelszive            24 haszavaithalhatomes
11 metmiterzekenmagairant          25 teljesithetnemdemaj{d}
12 aztleirninemlehetlegjob         26 eljöazazidömitaligaligvarokamitarokonaitil
13 benszetnemmarkeblemreölel       27 letimodorommeglesznekelegetalanamugyismegaztirja
14 niedesemahiczinyszajatosze      28 megedesemhogymicsodafoglakozastmondmajdrokonin
E1 ak (up the right edge, continues row 28)
on the stamp: istenve | leedes | semabol | d{o}gvi | szont | latasra | {f}eri
```

## Hungarian (normalized)

Szeretett édes egyetlen reményem! Becses sorait megkaptam, mit köszönök szépen. Sajnálatomat kell kifejeznem, hogy nem jön mulatságba, de így is jó, csak az a fő, hogy viszontláthatom. Higgye el, édesem, mikor sorait olvasom, kimondhatatlan érzés fogta el szívemet. Mit érzek én maga iránt, azt leírni nem lehet. Legjobban szeretném már keblemre ölelni, édesem, a piczíny száját összevissza csókolni, de sajnos ezt még soká tehetem. Írja meg, édesem, mikor jön, ha lehet, kimegyek eléjébe az állomáson. Kedvesem e kérését mindig parancsnak veszem, mert csak magának élek, és örül a szívem, ha maga szavait teljesíthetem. Legjobban szeretném már, ha szavait hallhatom és teljesíthetném, de majd eljő az az idő, mit alig-alig várok. Ami a rokonait illeti, modorom[mal] meg lesznek elége[dve] talán. Amúgy is még azt írja meg, édesem, hogy micsoda foglalkozást mond majd rokon[a]inak.

On the stamp: Isten vele, édesem, a boldog viszontlátásra. Feri

Plain handwriting, address: Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás. Printed on the picture side: Szerelmi üzenet. / Nem sokára nálad leszek drága kincsem! / Jöjj édesem vágyom utánad.

## English

My beloved sweet only hope! I have received your dear lines, for which I thank you very much. I must express my regret that you are not coming to the dance party, but it is fine this way too; the main thing is that I can see you again. Believe me, my darling, when I read your lines an inexpressible feeling took hold of my heart. What I feel for you cannot be written down. Most of all I would like to clasp you to my breast now, my darling, and kiss your tiny mouth all over, but sadly it will be a long time before I can do that. Write to me, darling, when you are coming; if possible I will come out to meet you at the station. Dear one, I always take your request as a command, for I live only for you, and my heart rejoices when I can carry out your words. Most of all I would like to hear your words now and carry them out, but the time will come that I can hardly, hardly wait for. As for your relatives, they will perhaps be satisfied with my manners [two endings supplied, item 1]. Anyway, do also write to me, darling, what occupation you will tell your relatives.

On the stamp: God be with you, my darling, until the happy reunion. Feri

Address: To the promising young lady Jolánka Tóth, Jászárokszállás. Printed: Love message. / Before long I shall be with you, my precious treasure! / Come, my sweet, I long for you.

## Slovak

Moja milovaná sladká jediná nádej! Vaše milé riadky som dostal, za čo veľmi pekne ďakujem. Musím vyjadriť ľútosť, že neprídete na zábavu, ale aj tak je to dobré, hlavné je, že Vás znova uvidím. Verte mi, drahá, keď čítam Vaše riadky, zmocnil sa môjho srdca nevysloviteľný pocit. Čo k Vám cítim, to sa nedá opísať. Najradšej by som Vás už privinul na hruď, drahá, a celé Vaše maličké ústa pobozkával, ale žiaľ, to ešte dlho nebudem môcť. Napíšte mi, drahá, kedy prídete, ak sa dá, vyjdem Vám v ústrety na stanicu. Moja milá, Vašu prosbu vždy beriem ako rozkaz, lebo žijem len pre Vás a moje srdce sa raduje, keď môžem splniť Vaše slová. Najradšej by som už počúval Vaše slová a plnil ich, ale príde ten čas, na ktorý sotva, sotva čakám. Čo sa týka Vašich príbuzných, s mojimi spôsobmi budú azda spokojní [dve koncovky sú doplnené, bod 1]. Aj tak mi ešte napíšte, drahá, aké zamestnanie poviete svojim príbuzným.

Na známke: S Bohom, drahá, do šťastného zhľadania. Feri

Adresa: Sľubnej slečne Jolánke Tóthovej, Jászárokszállás. Tlačený text: Ľúbostný odkaz. / Onedlho budem u teba, môj drahý poklad! / Príď, moja milá, túžim po tebe.

## Uncertainties

1. **Row 27, the one clause with supplied endings.** Every sign is clear; the literal run is `modorommeglesznekelegetalan`, and it ends in the plain word *talán*, "perhaps". I read (a) *modorom[mal] meg lesznek elége[dve] talán*, "they will perhaps be satisfied with my manners". *-mal* and *-dve* are not on the card; they are supplied, and this division is an editorial reading of the sense, not something the card shows. In its favour: *lesznek* stands complete and its plural fits the relatives as subject, *meg* stands where the resultative needs it (*meg lesznek elégedve*), the instrumental is the regular government with this verb, the same construction occurs on HCP1275 row 25 (*meg lesz örökítve*), and this writer often drops letters and syllables (*szetném*, *ija*, *foglakozást*, *rokon[a]in*, *legjob*). Alternatives: (b) the idiom *elege lesz*, "they will perhaps have had enough of them", the opposite drift, which the card alone cannot exclude, but it needs *lesznek* broken as *lesz nek[ik]*; (c) *modorom meg lesz nek[ik] elege talán*, taken as "will be enough for them", which I held at review 2 and now withdraw: "enough for them" would be *elég lesz nekik*, and *elege* does not mean that. No parallel for the words *modor* or *elégedve* turned up in the SOLUTION.md files of other cards.
2. **S4 *boldog***: the first o is partial under the printed stamp, its lower loop is lost; d, g, v, i are legible. The word sense and the closing on HCP1248 and HCP1251 (*a boldog viszontlátásra*, same writer) support it.
3. **S7 *Feri***: the first sign is a tilted cross, between f and u; f from word sense, as on HCP1216, whose signature is the same name. No identification of the two writers is claimed beyond the name and the shared key.
4. **Row 18 scribble**: after *b* one sign is inked over solid. It has the size and bar structure of a three-bar sign; e is by sense and gives *eléjébe* ("go to meet"). The ledger keeps it as `[#]`. *az állomáson* "at the station" is what is written (*az állomásra* would also be expected). The row ends in *alloma* and row 19 starts *son*; the double wave of *áll-* is merged but legible.
5. **Word-sense calls among near-homographs** (all h/p and d/n as the task asked to state). *szépen*, *parancsnak*, *piczíny*: p decided by sense, the sign is h/p. Row 3 *kaptam*: the sign is a separate tick above-left of a long stroke, the d form, so ledger token `D/p`; p is by sense only. Rows 6 and 15 *de* are written with the h/p sign, not the tick + long d. Row 25 *majd*: last sign is two long strokes, read d, not n. Row 15 *sajnos*: the sign is an upright cross (the f sign), not the inverted T; only j gives a word. Row 12 *leírni*: the first i has its dot, the second i (before *nem*) shows none, so that one could be taken as o. Row 19 *kérését*: the t is heavily overwritten and may have started as F. Row 28 *foglalkozást*: the s has a hook and looks like a reversed bowl. Row 17 *jön*: the strokes after ö are thick and run together (n by sense).
6. **Row 16** reads `megsokatehetem`; I take the single t with *tehetem* (*még soká tehetem*). The negative *nem* one might expect is not written. An ö/ő distinction is not made by the hand. Dots over o are marked `:d` only where seen; in row 3 only the first o of *köszönök* has them. Review 1 did not note others, but I did not re-audit every o.
7. **Writer's spellings normalized**: *szeretetedes* (t dropped), *higyje* → higgye, *kel* → kell (row 4, single l), *legjob-ben* → legjobban (row 12–13) and *legjob* → legjobban (row 23), *szetném* → szeretném (row 13, re dropped), *ija* → írja (row 16, r not written), *szájat* → száját, *oszevisza* → összevissza, *viszontlathatom* with the heavy s, *foglakozást* → foglalkozást, *rokonin+ak* → rokonainak (a not written), *amit* → ami (row 26), *hallhatom* written *halhatom*, *maj{d}*, *eljö* → eljő, *modorom[mal]* and *elége[dve]* (row 27, supplied, item 1), *édes|sem* → édesem (S2–S3, the s is doubled across the row break). Acute accents are mostly visible but not transcribed; they are supplied.
8. **Row 28 → right edge**: *ak* stands rotated up the right edge about 250 px (of 2210) above row 28; on my reading it completes *rokon(a)inak*. The wave at the corner is the upright end of row 26 (*il*, continued as *leti* on row 27), not part of the edge run.
9. **Address and postmark**: *Szépreményű* runs into the postmark, so its ending is by sense; *úrleánynak* is partly under the portal's mark. The left postmark begins ÉRSEK…; Érsekújvár is likely but unproved, and the date (a "17" is visible) gives no year.

## Why it is correct

- The key comes from other cards without change, and yields continuous Hungarian across all 28 rows and the stamp block: 724 signs, of which only the row 18 scribble is transcribed without a sign value.
- No key parameter was fitted here, so a coherent text cannot be an artifact of fitting. Long, unforeseeable words come out letter by letter: *kimondhatatlan*, *sajnálatomat*, *összevissza*, *teljesíthetném*, *parancsnak*, *foglalkozást*, *mulatságba*.
- Repeated words decode identically (*édesem* ×5, one of them written *édes|sem*; *viszontlát-* ×2, *teljesíthe-* ×2, *hogy*, *szavait* ×2).
- The text fits the family: formal *maga/Ön* address, love-letter formulas, the closing *Isten vele, édesem, a boldog viszontlátásra* and the name Feri (word for word on HCP1248 and HCP1251), and the addressee Tóth Jolánka of Jászárokszállás.

## Response to review 1

1. **S3 and S4: fixed, confirmed on my own crops.** `work/crop2.py` makes a green-suppressed view (`work/crops2/stamp_ink.png`). It shows S3 right bowl, three bars, three strokes, two faint bars, six, loop, wave, and S4 tick + long stroke, the top of a loop, a descender with hook, chevron, dotted curve. My earlier "j stem" is the stem of the six. Ledger: `S3 ) E M A 6 O L`, `S4 D O? G V I`. The text is now *Isten vele, édesem, a boldog viszontlátásra*; "Jol[…]" is gone from all versions, the old items 2 and 3 are deleted, and the new item 2 marks the partial o.
2. **Row 27: sign fixed; the reviewer's division only partly taken.** The sign is two bars (`review/work/a27.png`, `r27b.png`), so the run is `elegetalan`. I agree the old supplied *-mal* and *-ek* must go. I do not adopt *elégetalan = elégtelen*, "insufficient": with the corrected a, the end splits into plain *talán*, "perhaps", which needs no emendation, and the remainder is *elege*. This turns my earlier "dissatisfied" and the reviewer's "insufficient" into a neutral or positive sense, though item 1 keeps the opposite idiom open. The division is new and no reviewer has seen it, which is why this goes to review 2 rather than FINAL.
3. **Row 18: fixed.** Sign stays `[#]` in the ledger; normalized text now *eléjébe az állomáson*; item 4 updated. The English does not change. The "awkward *be*" remark is gone.
4. **Dots and *kaptam*: fixed.** Row 3 second and third o are now plain O (`köszonok` in the literal row, ö in the normalized text). The *kaptam* sign is now token `D/p`, value by sense, and item 5 says so.
5. **Doubled s: fixed.** Item 7 and the *édesem* count state *édes|sem*.
6. **"Why it is correct": updated.** 724 signs stands (S3 +1, S4 −1).

The reviewer's question on *leírni* is settled by `work/crops2/r12.png`: the first i has the dot, the second has none; item 5 now says which.

Re-ran `python3 -I ciphers/hcp-1226/work/decode.py`: four hashes OK, output matches the literal block above.

## Response to review 2

Verdict REVISE. I checked the signs of row 27 again on `review/work/r2/m2627.png`: `...m o d o r o m | m e g | l e s z n e k | e l e g e | t a l a n...`, as both of us read them.

1. **Row 27: fixed, reviewer's reading adopted.** The reviewer is right that I had equated *elege* with *elég* without counting that as a change, and that my division broke the complete word *lesznek*. The clause now reads *modorom[mal] meg lesznek elége[dve] talán*, "they will perhaps be satisfied with my manners", in `work/normalized.txt`, the Hungarian, English and Slovak texts and the status line. Brackets are kept, and item 1 says that the two endings are supplied and that this is a reading of the sense. The idiom *elege lesz* stays as a stated alternative. The signs, the ledger and the literal row do not change, and the drift is the one already in the earlier alternative, so this is not a substantial change to the reading.
2. **"No parallel": fixed.** Item 1 now limits this to the words *modor* and *elégedve* and cites the construction on HCP1275 row 25, confirmed by grep of its SOLUTION.md.
3. **Spelling list: fixed.** Item 7 now lists *kel* → kell (row 4) and the two supplied endings.

Re-ran `python3 -I ciphers/hcp-1226/work/decode.py`: four hashes OK; the literal rows are unchanged and the normalized text prints the new clause.

## Stamp-box message (2026-11-03)

Stamp-box audit by Claude Opus 5.5 on 2026-11-03, from crops of `work/hires/*_adr.jpg` (`work/stamp-2026-11-03/stamp_2x.png`, `stamp_rows_4x.png`). The stamp has been **lifted**. Green paper fragments with perforation traces remain at its lower left and bottom edge, and the ÉRSEK… postmark breaks off where the stamp edge was. The stamp box holds a printed green triangle (letters N, B, C around a sun), and over it, where the stamp covered them, are **seven short rows in violet cipher signs** (no plain Hungarian). This writing was hidden under the stamp, so the card is steganographic as well as enciphered.

The rows were already read in full as S1–S7 of `work/ledger.txt` (decoded by the reproduction command above, after reviews 1 and 2). Today's crops agree with the ledger (S1 `) T E N V E` after the first sign, S6 `L A T A ) F A`, S7 tilted cross, three bars, F, dotted curve). The ledger and script are unchanged.

- Literal: istenve | leedes | semabol | d{o}gvi | szont | latasra | {f}eri
- Hungarian (normalized): Isten vele, édesem, a boldog viszontlátásra. Feri
- English: God be with you, my darling, until the happy reunion. Feri
- Slovak: S Bohom, drahá, do šťastného zhľadania. Feri

Unread: nothing. Two signs remain soft, as disclosed earlier: the first o of *boldog* (S4) is partly lost under the printed triangle, and the S7 tilted cross is read f (*Feri*).
