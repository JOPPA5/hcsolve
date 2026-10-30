# HCP1290 — to Jolánka Tóth: a travelling man thanks for her letter

**Status: deciphered; review 1 corrections applied. Residuals: one ink bar (row 6), the torn end of the text where the stamp was, and a few restored letters listed below.** Written 2026-10-30 by Claude Opus 5.5 as solver. No earlier work exists on this number. The portal shows status *Not solved* and attaches no transcription or solution; no published solution was met. The orchestrator's AI-register check (2026-10-30) found no record of this card.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" family key of finished cards HCP1216 (sign table in its SOLUTION.md), 1212, 1213, 1217, 1218, 1243, 1301. The key was taken over unchanged; no new letter value was needed. Picture side: only the printed verse "Kis házikóm ablakánál…" (no cipher). Address side: plain address, *Szépreményű(?) Tóth Jolánka úrleánynak, Jász Árokszállás*; first word reading not relied on.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark, also 5- and 8-shaped | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c (seen only in cs) | three short strokes | m | gamma/corner | t |
| short tick + long stroke | d | two strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + tick | h / p | low descender | y (in gy) |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1290/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (one token per written sign, 27 rows, 5 read rows where the stamp was and one `[UNREAD]` row S6) and prints the literal text and `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of `work/hires/*_adr.jpg` (`work/crop.py`, `work/rows.py`, output in `work/crops/`). Not OCR.

## Literal decipherment (as printed by the command)

```
01 szeretetédesjolankámbecsesso      15 csapatbanutazokéselőre
02 raitmegkaptammitnagyon            16 tudomhomejiknapmikor
03 szenköszönökkedvesemhigy          17 kelelutaznomszerdan
04 jeelédenojanjokedveluta           18 egesznapszabadleszek
05 zokmostismintmikor                19 esmajdelmegyekapaszto
06 elkezdtemcsakajoisten[blot]       20 rinehozishogyhagytudjam
07 egyetlenkérésemminelelőb          21 meghogyvanazendragacsila
08 teljesitseaztmagaistudja          22 gomameliktőlo{j}tavolva
09 edesemhogymiazkedvesem            23 gyokdenemsokakozelehoz
10 nempanaszkodniakartamcsak         24 zaasorskezedemostbezaro
11 azértirtamhogynevegyrosz          25 msoraimmertmenem
12 nevenhogyijenritkanirok           26 kelholnapfojtatom
13 majdebbenahonapbangyak            27 {i}stenveledesem
14 rabbanirokmertrendes              stamp: csok | lom | szam | talan | szor | [unread]
```

Row 24 from the final e of *keze* onward, rows 25 to 27 and the stamp rows are in darker ink: the writer changed pen or ink at that point.

## Hungarian (normalized)

Szeretet[t] édes Jolánkám! Becses sorait megkaptam, mit nagyon szé[pe]n köszönök, kedvesem. Higgye el, éde[s], [é]n olyan jókedvvel utazok most is, mint mikor elkezdtem. Csak a jó Isten [tintafolt] egyetlen kérésem minél előbb teljesítse, azt maga is tudja, édesem, hogy mi az, kedvesem. Nem panaszkodni akartam, csak azért írtam, hogy ne vegy[e] rossz néven, hogy ilyen ritkán írok. Majd ebben a hónapban gyakrabban írok, mert rendes csapatban utazok, és előre tudom, ho[gy] melyik nap, mikor kell elutaznom. Szerdán egész nap szabad leszek, és majd elmegyek a Pásztorinéhoz is, hogy hadd tudjam meg, hogy van az én drága csillagom, amelyiktől oly távol vagyok, de nemsoká közelé[be] hozza a sors keze. De most bezárom soraim, mert mennem kell, holnap folytatom. Isten vele, [é]desem.
Csók[o]lom számtalanszor. [rest unreadable]

## English

My beloved sweet Jolánka! I have received your valued lines, for which I thank you very much, my dear. Believe me, my sweet, I am travelling in as good a mood now as when I started. May the good God only [blot] fulfil my one request as soon as possible; you yourself know, my sweet, what it is, my dear. I did not mean to complain; I wrote only so that you would not take it amiss that I write so rarely. This month I will write more often, because I am travelling in a regular crew and I know in advance which day, when, I have to leave. On Wednesday I shall be free all day, and I will also go over to Mrs Pásztori's, so that I may find out how my dear star is, from whom I am so far away, but before long the hand of fate will bring me near her. But now I close my lines because I have to go; I will continue tomorrow. God be with you, my sweet.
I kiss you countless times. [rest unreadable]

## Slovak

Moja milovaná sladká Jolánka! Dostal som Vaše vzácne riadky, za ktoré Vám veľmi pekne ďakujem, drahá. Verte mi, sladká, cestujem teraz v takej dobrej nálade, ako keď som začínal. Len nech dobrý Boh [atramentová škvrna] čo najskôr splní moju jedinú prosbu; Vy sama viete, sladká, čo to je, drahá. Nechcel som sa sťažovať, napísal som len preto, aby ste mi nezazlievali, že píšem tak zriedka. V tomto mesiaci budem písať častejšie, lebo cestujem v riadnej partii a vopred viem, ktorý deň a kedy musím odcestovať. V stredu budem mať celý deň voľno a pôjdem aj k Pásztoriovej, aby som sa dozvedel, ako sa má moja drahá hviezdička, od ktorej som tak ďaleko, ale čoskoro ma ruka osudu privedie do jej blízkosti. Ale teraz končím svoje riadky, lebo musím ísť; zajtra budem pokračovať. S Bohom, sladká.
Bozkávam Vás nespočetnekrát. [zvyšok nečitateľný]

## Uncertainties

1. **Rows 3–4 `higy|jeeléden`.** Read *Higgye el, …* ("believe me"), the writer's own formula (HCP1308 `higyjeedesem`, HCP1300 `higyje`, HCP1216 `higgyjeel edesem`). The word division is firm. The tail `éden` is a restoration: most likely *éde[s], [é]n olyan…* (one s and one é dropped), which agrees with first-person *utazok*. *édesem* with a slip is possible but further from the signs. The sense of the sentence does not depend on this choice.
2. **Row 6, ink bar.** After *jóisten* a heavy horizontal ink bar about three signs wide ends the row. It may be a deletion. Nothing under it can be read, and a small tick above it stays uninterpreted. The sentence runs on without it.
3. **Row 19/20 *Pásztorinéhoz*.** The name runs over the row break. It is read as a surname from sense (Mrs Pásztori); *pásztor* words were considered and give no sentence. It occurs on no other Jolánka card in this repository.
4. **Stamp area.** The stamp was torn off the card, exposing writing done under it. Five rows read: *csok | lom | szam | talan | szor*. A sixth row (`[UNREAD]` in the ledger) shows only a stroke with a foot, a short bar and a low curve, then the torn stamp remnant covers the card. Any closing or signature there is lost, so the sender is unnamed. The dark slanted strokes over the printed FILLÉR are on top of the remnant and taken for postmark, not cipher.
5. **Row 22 blotted sign** between *o* and *t*: a retouched sign with an upright, a heavy foot and a top flag. Read `j` (*oj* = oly, as in *ojan*, *ijen*, *mejik*) from sense; a k-shape is not excluded by the pixels. Marked `{j}`.
6. **Row 20 `hagy`** (= hadd). The sign after `ha` is a doubled, retouched g with a dot-like mark to its right, before the y tail. *hagy* is the best reading and fits *hadd tudjam meg*, but this sign is not clean.
7. **Row 27 `veledesem`.** Both *vele, [é]desem* and *veled, [é]desem* drop one é and cost the same. Only the formal address on this card (*sorait, maga*) favours *vele*, which is printed here. The first sign of the row shows no dot and looks like an open loop; `{i}` for *Isten* is from sense.
8. **Row 24 first sign** is heavy, but its body matches the z at the end of row 23 and differs from the clean + of *fojtatom*, so z is secure. Rows 23–24 literal *kozelehoz|za*; *közelé[be]* is a normalization.
9. **h/p calls rest on word sense**: p in *megkaptam, panaszkodni, hónapban, nap* (×3 with *holnap*), *csapatban, Pásztori-*; h elsewhere. **d/n**: *drága* (row 21) has two strokes then tick + stroke; the division n + d is from sense. Row 3 *szen*: two long strokes with no p tick, so n; normalized *szé[pe]n* as a dropped syllable.
10. **Writer's spelling, normalized**: *szeretet, szen, higy, vegy, rosz, ho mejik* (ho[gy] melyik; ly always as j), *előb, kel, kelelutaznom, menem, soká* (*sokakozele*), *mit* (= amit), *csók lom*. Accents are given in the ledger only where seen; the rest are supplied.
11. *rendes csapatban utazok* suggests a work crew or troupe; the writer's trade is not established. The date is unknown: a figure 16 was seen, and the circular postmark at the stamp shows letters including S and E on its left arc, but I could not resolve a place name (the reviewer's …PEST is a hypothesis only). None of this touches the plaintext.

## Why it is correct

- The family key, transferred unchanged, turns all 27 rows and 5 stamp rows into Hungarian, with only the items above open.
- The text is coherent across row breaks (*so|rait, uta|zok, gyak|rabban, csila|gom, va|gyok, hoz|za, bezáro|m*). These joins follow from the signs, not from any division I imposed.
- Repeated words decode identically (*hogy* ×5, *kedvesem* ×2, *utazok* ×2, *mikor* ×2, *nap* ×2).
- Formal address (*sorait, maga, vele*), the addressee, the opening and closing formulas, and *higgye el* match the family. The sign shapes and the writing under the stamp also match it.
- Word sense decided the h/p and d/n calls, the `{j}` and `{i}` signs, *Pásztori-*, the row 27 division and the restorations marked in the text. The key was not altered to fit.

Credit: solved by Claude Opus 5.5 using the family key established on the finished cards named above, whose work is credited in their own directories.

## Response to review 1

Verdict REVISE. All eight findings were checked against the enlargements (`review/work/crops/`) and addressed. I re-ran `python3 -I ciphers/hcp-1290/work/decode.py` afterwards: hashes OK, 585 tokens (584 signs and marks read, plus the new `[UNREAD]` token), and the output matches this file.

1. **Row 3 `higy` (major): fixed.** `r3end.jpg` shows a round dot over the narrow crossed curve, so this is i, not o. Ledger `H I GY`. *Higgye el* now replaces the unresolved `jeeléden`, and translations, uncertainty 1 and the *hogy* count (×5) are updated. `r4start.jpg` confirms the signs of row 4. The ending is stated as a restoration.
2. **Row 20 `i` (major): fixed.** `r20o.jpg` shows the narrow triangular-loop body of i, not the round hooked o two signs to the right. The mark above is an elongated dot. Ledger `I`, text *Pásztorinéhoz is, hogy…*; the `ó` puzzle is gone.
3. **Row 24 single m (major): fixed.** `r24m.jpg` shows exactly three strokes between e and o; the second m in my ledger had no ink behind it. The literal is `kezedemost`, read *keze, de most* with nothing supplied. *[É]de[s]em* is withdrawn from the text and all translations, and the ink-change statement is corrected.
4. **Overstated claims (minor): fixed.** "Why it is correct" is rewritten and now lists what word sense decided.
5. **Row 27 alternatives (minor): fixed.** Uncertainty 7 gives both divisions at equal cost, with formal address as the only argument for *vele*.
6. **Row 20 `hagy` retouch (minor): disclosed.** Seen in crop `s06R`; now uncertainty 6.
7. **Sixth stamp row (minor): fixed.** The ledger has row S6 `[UNREAD]`, and decode.py prints it.
8. **Second postmark (minor): addressed.** I looked at `pm2.jpg`: S and E are visible on the left arc, but no name can be resolved. Stated in uncertainty 11, without adopting …PEST.
