# HCP1284 — Feri to Jolánka Tóth: writing from Szentjakab

**Status: complete reading; one small unresolved residue in row 17 (a letter i and a stroke before *nem*); reviewed, verdict REVISE, findings addressed (see Response to review 1).** 2026-11-01, Claude Opus 5.5. No earlier work existed on this number. The portal shows *Not solved* and attaches no transcription or solution; no published solution was seen. The key is transferred from finished sister cards (see below); no plaintext was taken from them. The transcription is my own, made from `work/hires/` and not blind to the expected family vocabulary.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (type label MASC): the Jolánka family key, unchanged, as tabulated in `ciphers/hcp-1216/SOLUTION.md`: a two bars, b six, c/cs bowls, d long+short stroke (here also written short+long, "4"-like), e three bars, f upright or tilted cross, g loop with descender, gy joined loop, h/p tall stroke+short, i dotted crossed curve, j inverted T, k S-shape, l wave, m three strokes, n two strokes, o cursive loop, r F-like, s right bowl, t gamma, u plain cross, v chevron, z crossed diagonal with curled top; dots over o/u give ö/ü. The family's accents are mostly left unmarked in the literal text and supplied in normalization. Row 13 "4 ½" is written in clear numerals. The word *kocsin* above row 14 is plain Latin script, inserted by the writer.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1284/work/decode.py
```

It checks SHA-256 of all four images, prints the manual sign ledger `work/ledger.txt` row by row and the normalized text `work/normalized.txt`. The ledger is a human-style reading of crops, not OCR.

## Literal decipherment

```
01 szeretetedesjolan            10 etanyafalutol
02 kambecsessorait              11 feloraja{R}asnyira
03 megka{p:d}tamigazan          12 esgyöngyöstol
04 örülökhogymeg                13 {#}pedig41/2orajara{s?}{-}
05 {#}egyszerolvashat           14 ra[kocsin]vanezazelet
06 tamsoraitahoszu              15 nemojonminöne
07 tavolletalat                 16 edesjolankama
08 mamarszentjakab              17 tanyani{|}{n-}emeszünk
09 roiromsorai{m?}              18 föteteltistenveleedesem
stamp: csokolom / szamta / lanszo / feri + r (the r of -szor, tilted, at the end of the last row)
```

## Hungarian (normalized)

Szeretet[t] édes Jolánkám! Becses sorait megkaptam. Igazán örülök, hogy még egyszer olvashattam sorait a hosszú távollét alat[t]. Ma már Szentjakabró[l] írom soraim. E tanya falutól félórajárásnyira és Gyöngyöstől pedig 4½ órajárásra kocsin van. Ez az élet nem ojon, min[t] öné, édes Jolánkám. A tanyán {i + stroke, unresolved} nem eszünk főt[t] ételt. Isten vele, édesem.

Under the stamp: Csókolom számtalanszor. Feri.

## English

My dear sweet Jolánka! I have received your esteemed lines. I am truly glad that I could read your lines once more during the long absence. Today I am already writing my lines from Szentjakab. This farmstead is half an hour's walk from the village and 4½ hours by cart from Gyöngyös. This life is not like yours, my sweet Jolánka. On the farmstead we do not eat cooked food. Farewell, my darling. Under the stamp: I kiss you countless times. Feri.

## Slovak

Moja drahá sladká Jolánka! Vaše vzácne riadky som dostal. Naozaj sa teším, že som si počas dlhej neprítomnosti mohol ešte raz prečítať Vaše riadky. Dnes už píšem svoje riadky zo Szentjakabu. Tento salaš je pol hodiny chôdze od dediny a od Gyöngyösu 4½ hodiny vozom. Tento život nie je taký ako Váš, moja sladká Jolánka. Na salaši nejeme varené jedlo. Zbohom, moja drahá. Pod známkou: Bozkávam Vás nesčíselne veľakrát. Feri.

## Plain (unenciphered) writing

Address, in clear: *Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás*. Lower right, in clear, partly under the HC Portal collection stamp: *Kelt 2 1 ?ra este* ("written ... in the evening"); the number and the word after it are not settled. The picture side bears a printed four-line verse, *Magácskánál mulat / Minden gondolatom . . . / Mennyire szeretem, / Azt ki sem mondhatom* ("With you my every thought lingers; how much I love you I cannot even say"), and a publisher's mark with the number 2523; it is printed, not cipher, and not part of the message. Reading the postmarks was tried on enlargements: the left one shows only fragments (at least *ÁSZ* and a numeral 2), the one on the stamp less, so the card is undated here.

## Uncertainties

1. **Row 17, residue before *nem*.** After *tanyán* stand a dotted i and a single stroke with no established value; a thin bar lies over the following pair of strokes (n) and is unexplained. The pair, e and the three strokes with a ticked first stroke (m, as in rows 2 and 3) give *nem*, directly before *eszünk*, which fits the sentence before it. The stroke is treated as an isolated stroke of no value, as in HCP1216 row 18. What i + stroke was meant to be (*tanyáni*, a false start, *i[s]*) is not settled. Alternative: stroke + pair as m, giving *imem eszünk*, which is no word; the pixels alone do not exclude that division. So the negation rests on word sense as well as on the signs.
2. **Row 13, sign before the hyphen:** an overwritten heavy loop with a top bar; the sign itself resembles a retraced o (curl, heavy loop, arm to the right) and nothing of an s form is visible, so the value s rests wholly **on word sense** (*órajárás-ra*), with the hyphen and *ra* on row 14 in support. Other values fixed by word sense are listed in items 4 to 8.
3. **Row 5 first sign and row 13 first sign** are heavy, retraced crosses and are treated as cancelled false starts with no value (*még [#] egyszer*, *[#] pedig*). If either had a value (f, or a z) it would make no word.
4. **Row 9, last sign:** three strokes with an arc joining the last two: m (*soraim*), possibly corrected from or to t (*sorait*). Word sense gives m: the writer's own lines.
5. **Row 11:** the *r* of *járás* lacks its middle bar and is literally a t (gamma); r by word sense. The final *a* has its two bars joined by a diagonal and is very Z-like; a by word sense.
6. **Row 18, first word:** a tilted cross with a hooked leg, read f (as the tilted f of HCP1216 row 21) by word sense; ő has two ticks; its arm ends in a long hook that could be a separate s (*főst*), but I take it as the arm. Literal *föt* = *főtt*.
7. **Row 15:** *ojon* for *olyan* (HCP1216 has *ojan*), with an o-sign where a is expected; *min* for *mint*; the final e of *öné* has its top two bars joined. Row 6 *hoszu* = hosszú; row 7 *tavollet alat* = távollét alatt (the second l has a form close to the chevron; l by word sense); row 9 *ro* = ról, with no l sign, possibly dialect; row 1 single t in *szeretet[t]*.
8. **h/p, d/n:** *hogy*, *olvashat*, *hoszu* (h) and *pedig* (p) are decided by word sense. The p of *megkaptam* (row 3, ledger `{p:d}`) is literally a d shape (short left tick + long right stroke), so the literal is *megkadtam*; p is word sense. d/n: *edes*, *pedig* vs *nem*, *van* are decided by stroke length and agree with sense.
9. **Stamp:** the final o of *-szo* is a doodled, overwritten loop and the r is a tilted F placed at the end of the name row; *számtalanszor* rests on sense and on the family's closing formula.
10. **Szentjakab** is taken as a place name; it is not identified here. The word division *E tanya falutól* supplies the subject of *van*; the cipher itself has no word spaces.

## Why it is correct

The family key, unchanged, turns every row into Hungarian without any fitting per card, except the points above. The text has the family's forms (*Szeretett édes Jolánkám*, *Isten vele*, *Csókolom számtalanszor*, signature Feri, as on HCP1216/1217), the writer's known habits (*ojan*, *mer[t]*-like dropped t), and specific new content that the key was not fitted to: *Szentjakab*, *tanya falutól*, *félórajárásnyira*, *Gyöngyöstől*, and the numerals 4½, plus the writer's own clear insertion *kocsin* which fits exactly after *órajárásra*. Gyöngyös is a real town in the region of the family's Vámosgyörk mention.

## Response to review 1

Verdict REVISE. All five findings were re-checked on the reviewer's crops and accepted. The letters change only in row 17; the sense changes in rows 10 and 17.

1. **Row 17, major: fixed.** On `review/work/crops/r17mid.png` the group after e is three evenly spaced strokes with a tick on the first, the same m as in rows 2 and 3 (`rows01L.png`). My `{t'} n` split had no parallel. Ledger now `i {|} {n-} e m e sz u: n k`; main reading *nem eszünk főtt ételt*; English, Slovak, normalized text and uncertainty 1 updated. The i + stroke and the bar stay disclosed as unresolved.
2. **Row 10, major: fixed.** Letters unchanged, division now *E tanya falutól*; Hungarian, English, Slovak, uncertainty 10 and the proof paragraph updated. The earlier English said the reverse of the plain sense.
3. **Row 3, minor: fixed.** The shape on `rows01L.png` is the d shape, as the reviewer says. Ledger token `{p:d}`; uncertainty 8 updated.
4. **Word-sense statement, minor: fixed.** "Only restoration-type reading" removed; uncertainty 2 describes the o-like shape and uncertainty 5 the Z-like final a.
5. **Side material, minor: fixed.** Verse, mark and the postmark attempt are in the plain-writing section.

Reproduction re-run after the edits: all four SHA-256 checks OK and the output matches the literal block and the normalized text above. The reading was not substantially changed beyond these findings, so no second review round is needed, as the review itself states.
