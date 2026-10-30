# HCP1297 — Feri to Jolánka Tóth: "your parents are not angry", a Népszava festival, three weeks to wait

**Status: whole card read; review 1 (REVISE) addressed, see the last section; a few interpretive points stay open (Uncertainties 1, 2, 7).** Claude Opus 5.5, 2026-10-30.

Credit: all work on this card is by Claude Opus 5.5 (2026-10-30); there was no earlier work on this number. The key is the shared Jolánka family key established on earlier cards by the OpenAI GPT solver and completed by Claude Opus 5.5 (see HCP1216, 1212, 1213, 1217, 1218, 1243, 1301). The portal shows status *Not solved* and attaches no transcription or solution; no published solution was met.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs, the Jolánka family key used unchanged (same sign classes as HCP1216):

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S-loop (both forms occur) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl + right bowl | cs | three short strokes | m | gamma/corner | t |
| short stroke + long stroke | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short tick | h / p (one sign) | dotted crossed curve | i |
| open loop with descender | g | inverted T | j | cross with hook/tail | z |
| joined loop + descender | gy | | | | |

Two dots over o/u give ö/ü. On this card the chevron (v) and the short+long d are particularly clear: *kedves* occurs three times and proves them (rows 1, 4, 23).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1297/work/decode_opus.py
```

It checks the SHA-256 of the four scan files, decodes `work/ledger-opus.txt` (460 signs, one token per written sign) and prints the literal rows, then `work/normalized-opus.txt`. The ledger is a manual transcription of enlarged crops of the un-converted scan `work/hires/..._adr.jpg` (not OCR); `work/crop.py` and `work/crop2.py` remake the crops. The transcription of the card was made here; none is attached on the portal.

## Literal decipherment

```
01 kedvesjolankam           14 mindenbajtol{|}ede
02 becsessoraitmegkap       15 semaligvaromazt
03 tammejetangyon           16 azidöthogyjolan
04 köszönokkedvesjo         17 kavalujrmulathas
05 önnagyonroszul           18 sakharomhetmulva
06 erteteteszedemet         19 leszegynepszava
07 haazgondoljahogy         20 ünepejmajerölszoval
08 szüleimtalanmaga         21 bövebbenjomulatast
09 ragszonakeztaigy         22 kivanovasarnapabela{/}ak
10 gondoljaamiaz            23 vasarna{|}pirokistenveletisztelemakedvesmamajat
11 utazstiletiatol          24 atavolbolimadojaferi
12 nemfelekmermeg           25 sajnalomhogynemjötbe
13 vedamagaszeleme
under the stamp: csokolom | szamta | lanszor | hükedve | senferi
```

Rows 1–21 are on the left; rows 22–25 run across the bottom of the card (23 and 25 to the right edge).

## Hungarian (normalized)

Kedves Jolánkám! Becses sorait megkaptam, melyet [n]agyon köszönök, kedves jó! Ön nagyon rosszul értette [be]szédemet, ha az[t] gondolja, hogy szüleim talán magá[ra ha]ragszanak; ezt a így gondolja {sense unresolved}. Ami az utaz[á]st illeti, attól nem félek, mer[t] megvéd a maga szelleme minden bajtól. Édesem, alig várom azt az időt, hogy Jolánkával újr[a] mulathassak. Három hét múlva lesz egy Népszava-ünnepély; majer[r]ől szóval bővebben. Jó mulatást kívánó[k] vasárnap[r]a {Béladak?}. Vasárnap írok. Isten vele. Tisztelem a kedves mamáját. A távolból imádója Feri. Sajnálom, hogy nem jött be.

Under the stamp: Csókolom számtalanszor. Hű kedvese[n?] Feri.

Square brackets = not on the card, supplied in normalization. Braces = open point.

## English

Dear Jolánka! I received your esteemed lines, for which I thank you very much, my dear good one! You understood my words very badly if you think that my parents may perhaps be angry with you; [rows 9–10 unresolved: literally "this ... thus you think", the expected sense is probably "do not think of it this way", but no negation is on the card]. As for the journey, I am not afraid of it, because your spirit protects me from every harm. My sweet, I can hardly wait for the time when I can have fun with Jolánka again. In three weeks there will be a Népszava festival; about *majer* more by word of mouth. I wish good fun for Sunday {Béladak?}. I shall write on Sunday. God be with you. My respects to your dear mother. From afar, your adorer, Feri. I am sorry that you did not come in.
Under the stamp: I kiss you countless times. Faithfully and lovingly [?], Feri.

## Slovak

Milá Jolánka! Vaše vážené riadky som dostal, za čo veľmi ďakujem, moja milá dobrá! Veľmi zle ste pochopili moje slová, ak si myslíte, že moji rodičia sa na Vás azda hnevajú; [riadky 9–10 nevyriešené: doslova „toto ... takto si myslíte“, očakávaný zmysel je asi „tak to neberte“, no zápor na lístku nie je]. Čo sa týka cesty, tej sa nebojím, lebo Váš duch ma ochráni pred každým zlom. Moja sladká, sotva sa dočkám času, keď sa budem môcť znova zabávať s Jolánkou. O tri týždne bude slávnosť Népszavy; o *majeri* viac ústne. Želám dobrú zábavu na nedeľu {Béladak?}. V nedeľu napíšem. S Bohom. Pozdravujem Vašu milú mamu. Z diaľky Váš ctiteľ Feri. Ľutujem, že ste neprišli dnu.
Pod známkou: Bozkávam Vás nespočetnekrát. Verne a láskyplne [?] Feri.

## Uncertainties

Open points (the signs are read; the sense is not settled):

1. **Row 22 `bela{/}ak`.** b e l a, a single slash, a k: all clear on the pixels, but no secure word results. The slash is taken as the reduced d known from HCP1216 (*Béladak*); it may be a name or a family form of *Béla* ("Béláék", the Bélas?). This is reported literally, not forced. The preceding *vasarnapa* is normalized *vasárnap[r]a* (r omitted), which is itself tentative. Alternative, not proven: *vasárnap a Bélának* ("on Sunday, to Béla") needs no omitted r and takes the slash as a reduced n, but the sign is a single stroke, unlike n everywhere else on the card. Point kept open.
2. **Row 20 `majerol`.** Signs m a j e r ö l are clear (the mark over the o is a single tick). *majer* may be a dialect form of *major* (farmstead/grove, perhaps a place name) or a surname Majer; *-ről* = "about" (written with one r; no article is on the card). Left untranslated.
3. **Row 25 `jöt be`.** Signs j, o with two marks, t, b e. *Sajnálom, hogy nem jött be* ("I am sorry that you did not come in"; t written once, as with many doubles here). The call j rests on shape plus sense, not shape alone: the bar sits low on the stem, as on the inverted T, unlike true f with its bar at mid-height, but a tiny foot shows below the bar, and the loop's right stroke is rather straight for an o. The subject is not written; "you" follows the formal address. First read *föt be* and forced to *fért be*: withdrawn after review 1.

Word-sense calls and writer's slips:

4. **Row 3 `angyon`.** a, two short strokes, gy, o, n: literal *angyon*, normalized *nagyon* (transposed a/n). Inferred from *melyet … köszönök*.
5. **Row 6 `erteteteszedemet`.** Literal é r t e t e t e sz e d e m e t. Normalized *értette [be]szédemet* ("understood my words"), which assumes that the writer wrote *-te-* a second time where *be-* should stand, or dropped *be*. This is the weakest whole phrase after items 1–3. The last sign sits on the black postmark: its top and stem are visible, a middle bar cannot be excluded, so *t* (not *r*) is by sense.
6. **Rows 8–9 `maga | ragszonak`.** Normalized *magá[ra ha]ragszanak*: the writer skipped from one *ra* to the next and wrote *-szonak* for *-szanak*. The third stroke of *m* is curved but counted; the g-sign and final a are clear; the final a carries an accent tick, which supports *magá[ra]*.
7. **Rows 9–10 `ezta igy gondolja`.** Signs e z t a i gy confirmed, but the clause gives no good sense as written. The expected sense is probably "do not think of it this way"; no negation is on the card, so the translations mark it unresolved and offer no smooth rendering. *Ez talán így* is not on the card. A blot-like dot in row 10 after *gondolja* is taken as a full stop.
8. **Row 7 `haaz`.** The cross after the two a-signs has a small hook and is read as z (*ha az[t]*), not u, by sense.
9. **Omitted letters, as written:** *utazst* (utazást), *mer* (mert), *ujr* (újra), *roszul*, *ileti*, *atol*, *szeleme*, *ünep-*, *mulathassak* written *mulathas|sak*, *haragszonak*, *jöt* (jött), *majeröl* (majerről). Also *mejet* = melyet (ly as j, as *ojan* on HCP1216).
10. **Row 19 `nepszava`.** The h/p sign is p by sense. *Népszava* was the Social Democratic daily; a Népszava festival fits *jó mulatást* ("have fun") but is my inference, and the card does not capitalize. *nép szava* ("voice of the people") would be the same letters.
11. **Row 20, the sign j of `ünepej`, and row 24, the j of `imadoja`.** In both, a heavily inked inverted T overlies a gamma top (t): the writer seems to have corrected t to j (or the reverse). Read j: *ünnepély* (ly as j) and *imádója*. If both signs count, row 24 would be *imádotja*, row 20 *ünepetj*, with no gain in sense.
12. **Row 24, `a` of `imadoja`.** A pink blot sits on the long stroke of d; bars crossing it are read as a. Disclosed as a blot-affected reading.
13. **Row 14, the mark before `ede`.** A small smudged stroke lies in the pink stain; it has no letter value (`{|}`). *…édesem* continues across the row break.
14. **Row 23.** The second sign is blotted (two or three bars, a/e): *vasárnap* by sense. A blot before the p has no value (`{|}`). In *kedves* the e shows two clear bars in the scan and the third is uncertain.
14a. **Row 20, last a of `szoval`.** The sign has two bars and a tiny third dash below (a/e); read a by sense.

15. **row 21 `jo`, row 4 `köszönok`.** No dots seen on the o of *jó*, or on the third o of *köszönök*. Acute accents are faint throughout and are supplied.
16. **Under the stamp.** The block has five lines. s1 is washed out and blurred, like the top of the stamp area: *csókolom* fits the visible outlines (bowls, o, section mark, o, wave, o, three strokes), but only *csokol* is firm and the first sign is a blur. The *sz* of *számta-* (s2) is a restoration: the s is only a pink smear, the z legible. Lines s3–s5 are readable. s4–s5 read *hű kedve|sen*; I do not decide between *hű kedvesen* and a slip for *hű kedvese*. The order of the under-stamp text within the letter is not known.
17. The sender is "Feri" (twice). No identity with Feri of HCP1216 is claimed, though key, hand style, ink and closing formulas agree. The date comes from the portal (1912-07-07); the postmark is not fully legible.

## Why it is correct

- The family key was transferred unchanged and gives Hungarian across all 460 signs; only two marks have no letter value and one (the slash in row 22) has only a tentative value.
- Long independent words are unforced: *becses sorait megkaptam, köszönök, nagyon, gondolja hogy, szüleim, ami az utazást illeti, nem félek, megvéd, szelleme, minden bajtól, alig várom, Jolánkával, három hét múlva, bővebben, Isten vele, tisztelem a kedves mamáját, a távolból, sajnálom hogy, nem jött be, számtalanszor*.
- Repeats decode alike: *kedves* ×3 plus row s3, *gondolja* ×2, *hogy* ×3, *maga* ×2, *Feri* ×2, *vasárnap* ×2.
- The writer's habits match family spelling (dropped letters, ly as j, formal *Ön/maga* address, closing formulas). The address side is plaintext to Tóth Jolánka, Jászárokszállás, as on the sister cards.

## Response to review 1

Verdict REVISE, Claude Opus 5.5 reviewer. All seven findings accepted after I looked at the reviewer's crops myself. The ledger, normalized text, translations and uncertainties are updated; the reading is not substantially changed (two signs in 459, one sentence).

1. **Row 25 j, not f: fixed.** Checked on `review/work/crops/fot.png` against j in `mamat.png`: the bar sits low on the stem, as on inverted T. Ledger token changed from + to J, literal `jötbe`, normalized *nem jött be*, three translations and Uncertainty 3 rewritten, with the call disclosed as shape plus sense because of the tiny foot below the bar. *fért be* withdrawn.
2. **Row 20 final wave: fixed.** Clear on `r20w.png`; my crop stopped short of it. Token L added, row ends *szoval*, brackets removed, *szova* off the omitted-letters list, count now 460. The third dash under the a-sign is disclosed (Uncertainty 14a).
3. **Row 20 additions: fixed.** Normalization is now *Népszava-ünnepély; majer[r]ől szóval bővebben*: no article, and the second r in brackets. The same convention is applied to *vasárnap[r]a*. *ezt [a] így* is now *ezt a így*, since that a is on the card.
4. **Row 22 alternative: added** to Uncertainty 1. Point stays open.
5. **Rows 4–5 punctuation: fixed.** Now *köszönök, kedves jó! Ön nagyon rosszul értette*, with no letters added; all translations follow. *Kedves Jó[lánkám]* remains possible, but would need supplied letters.
6. **Rows 9–10: fixed.** Marked unresolved in the normalized text, the translations and Uncertainty 7.
7. **Ledger layout and legend: fixed.** s1 split, so the block has lines s1–s5; token `S` added to the legend.

The reviewer's further note, the accent tick on the final a of row 8, is added to Uncertainty 6.

Re-run after the fixes: `python3 -I ciphers/hcp-1297/work/decode_opus.py` gives 4 hashes OK and 460 signs; see NOTES.md.
