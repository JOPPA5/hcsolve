# HCP1258 — Feri to Jolánka Tóth: a rainy Sunday and a promise of marriage

**Status: main text and under-stamp text read in full. The closing of row 29 is read as a formula with disclosed doubts (Uncertainty 1). Updated after review 1 (REVISE).** Written 2026-11-01 by Claude Opus 5.5. There was no earlier work on this number. The portal row shows *Not solved* with no attached solution or transcription (the detail page timed out in capture, see source/metadata.md); no published solution of this card was found, and the orchestrator's AI-register check (2026-11-01) found no record.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka family key, transferred unchanged from the finished cards HCP1216, 1212, 1213, 1217, 1218, 1243, 1301. The hand is the same writer's (Feri).

| sign class (ledger token) | letter | sign class (ledger token) | letter | sign class (ledger token) | letter |
|---|---|---|---|---|---|
| two bars (BAR2) | a | section mark (SECT) | k | F-like (FLIKE) | r |
| six (SIX) | b | wave (WAVE) | l | right bowl (RBOWL) | s |
| left bowl (LBOWL) | c | three short strokes (STROKE3) | m | gamma/corner (GAMMA) | t |
| long stroke + short tick (TICK) | d | two short strokes (STROKE2) | n | plain cross x (XPLAIN) | u |
| three bars (BAR3) | e | cursive loop (LOOP) | o | chevron (CHEV) | v |
| cross, upright or tilted (CROSS) | f | tall stroke + short (TALL) | h / p | low descender (DESC) | y |
| open loop with descender (GLOOP) | g | dotted crossed curve (CURVE) | i | crossed diagonal, x with tail (XTAIL) | z |
| inverted T (INVT) | j | joined loop + descender (LOOPDESC) | gy | opposed bowls (OPPBOWL) | cs |

Dots over o/u give ö/ü; a double mark gives ű; acute marks are faint and mostly supplied in normalization. JOINTY is the joined ty sign seen only in row 22.

Variants seen on this card:

- k is an S/8 shape; g is a ς shape with a descender; the two lie close, see Uncertainty 6.
- gy, and once ty, are written as joined signs.
- j is an inverted T, often tilted so that it looks like a slanted k (rows 27, s7).
- f is a cross, upright or tilted. In s7 it is tilted so far that it resembles j.
- Digits stand as digits: 2 (row 12) and 1 (row 29).

Register type label: MASC.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1258/work/decode_opus.py
```

It checks the SHA-256 of both `source/` scans and both `work/hires/` originals, maps `work/ledger-signs.txt` (one sign-class token per written sign: 29 rows, 7 stamp rows, 787 tokens, 796 letters) through the key table above, and prints the literal rows and `work/normalized-opus.txt`. The ledger is a manual transcription from enlarged crops of the hi-res original (`work/crops/`, `work/crops2/`, made by `work/crop.py`, `work/cropr.py`, `work/crop2.py`); it is not OCR and not blind, because each sign was assigned to a class while reading with the key in hand. The normalized text is an editor's file, typed by hand. `work/ledger-opus.txt` is the round 1 ledger in letter labels, kept as a record; `work/make_sign_ledger.py` made the sign ledger from it and applies the round 2 corrections. Layout: rows 1–25 fill the left block; rows 26–29 run across the whole foot of the card; s1–s7 are in the box drawn at the stamp place.

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvébe találja soraim. Hogy telt a vasárnap, édesem? De szeretném már a viszontlátás örömeit élvezni, de sajnos le vagyok kötve: nem akkor csinálok szabadot, amikor akarok. Odahaza van még a Béla, most van a kimulatása. Nekem nem a legjobb vasárnapom van, mert esik az eső, és éjjel 2 órától délig folyton áztam. Most meg lefekszek, átalszom a vasárnapot. Ez az én vasárnapom. Itt, édesem, azt se tudja az ember sokszor, hogy mikor van vasárnap, édesem, igazán. Örülö[k], hogy újra szórakozhatom magával, édesem. Csak arra kérem magát, édesem, ne hallgasson semmiféle pletykára, ne zavarja semmi a bo[l]dogságunkat. Teljes bizalommal legyen ir[á]ntam: mihelyt olyan helyzetbe leszek, hogy feleségemmé tehessem, rögtön ott leszek, mert én jobban várom azt a helyzet[et], mint talán maga, édesem, mert maga többször mondta, hogy ráér még, elég fiatal, ahogy szüksé[g] esetén legtöbb 1 évet várjon. Csó[k]olja kedvese, Fe[ri].

Under the stamp: Isten vele, édesem! Maradok hű kedvese és sír[ig] hű imádója, Feri.

## English

My beloved sweet Jolánka! I hope my lines find you in the best of spirits. How was your Sunday, my darling? How I would love to enjoy the joys of seeing you again, but sadly I am tied down: I cannot make free time when I want to. Béla is still at home; he is having his fling now. Mine is not the best of Sundays, because it is raining, and from 2 at night until noon I was getting soaked the whole time. Now I shall lie down and sleep through Sunday. That is my Sunday. Here, my darling, one often does not even know when it is Sunday, truly, my darling. I am glad that I can enjoy your company again, my darling. I ask only this of you, my darling: do not listen to any gossip, let nothing disturb our happiness. Have complete trust in me: as soon as I am in a position to make you my wife, I shall be there at once, for I long for that state of things more than perhaps you do, my darling, since you have said several times that there is still time, that you are young enough to wait a year at most if need be. Kisses you, your sweetheart, Fe[ri].

Under the stamp: Farewell, my darling! I remain your faithful sweetheart and, unto the grave, your faithful admirer, Feri.

## Slovak

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšej nálade. Ako prebehla nedeľa, drahá? Ako rád by som si už užil radosti z opätovného stretnutia, ale žiaľ som viazaný: nemôžem si urobiť voľno, kedy chcem. Doma je ešte Béla, teraz si užíva. Ja nemám najlepšiu nedeľu, lebo prší, a od 2 v noci do poludnia som stále mokol. Teraz si ľahnem a nedeľu prespím. To je moja nedeľa. Tu, drahá, človek často ani nevie, kedy je nedeľa, naozaj, drahá. Teším sa, že sa môžem znova zabávať s Vami, drahá. Prosím Vás len o to, drahá, nepočúvajte žiadne klebety, nech nič nekazí naše šťastie. Dôverujte mi úplne: len čo budem v takom postavení, aby som Vás mohol urobiť svojou manželkou, hneď tam budem, lebo ja na ten stav čakám viac než možno Vy, drahá, veď ste viackrát povedali, že ešte je čas, že ste dosť mladá na to, aby ste v prípade potreby počkali najviac 1 rok. Bozkáva Vás Váš milý Fe[ri].

Pod známkou: S Bohom, drahá! Zostávam Vaším verným milým a až do hrobu verným ctiteľom, Feri.

## Uncertainties

1. **Closing of row 29 (the least secure place).** After *várjon* the literal signs are c-s, o, o, l, j, a, k, e, d, v, e, s, s, e, cross, dot, e, and the row ends at the worn corner (`work/crops2/r29tail.png`, `work/crops2/xe.png`). The reading is *Csó[k]olja kedvese, Fe[ri]*, a family closing (HCP1213, 1301: *Csókolja … kedvese Feri*).
   - *csó[k]olja*: both middle signs have the loop-with-tail outline of this writer's hurried o (compare *hogy* at the end of row 28, `work/crops2/hogy28.png`). The second is overinked and looks written over something (`work/crops2/blr.png`). A k cannot be seen. Either it is under the blot or it was omitted, as this writer often omits letters. *csalja* is excluded by the o signs.
   - *kedvese*: written k e d v e s s e. The second s is a right bowl with a hooked top, the same form as the s that opens row 29 (`work/crops2/r29start.png`). It is not k: the k of *szükség* in the same row and of *kedves* are section marks. So the reviewer's *kedves kezé[t]* fails at that sign. Doubled s for single is this writer's habit (row 12 *essö*, and doubled letters in row 10 *kimulattása*).
   - *Fe[ri]*: the small cross is the one soft call. By shape alone it could be plain x (u) or a tilted f, and it lacks the long tail of z. It is close to the tilted f of *fiatal* in row 28 just above (`work/crops2/f28.png`), and only f gives a word. The dot beside it has no value here (stray, or a point after an initial). The last sign is a squeezed three-bar e at the corner, its bottom bar detached. The letters *ri* are not on the card: nothing continues on the right edge, so they ran out of room or were dropped. This word rests on sense and the formula, not on clean signs. The full signature *Feri* stands in the box. If it is rejected, one word of the closing stays unread and the message is not affected.
2. **Restorations of physically hidden signs.**
   - Row 26 at the tear: *feleség[e][m]é*. A fragment of one sign and the last stroke of m are visible. The tear leaves room for about two signs, so the writer probably wrote single m, as he usually does.
   - Row 28 final *hogy*: the g and the y are both visible on `work/crops2/hogy28.png`. The y runs heavily into the worn corner. Round 1 said the g was in the tear; that was wrong, and the ledger is right to show it unbracketed.
   - Row 29: the t of *évet* is in the tear; the end of its bar is visible.
   - s3: *marad[o][k]*. One small wedge and a vertical trace survive in a green smear, so two signs are restored here, which is more than the one-letter rule allows. *maradok* is chosen from sense with *hű kedvese*; literally only *marad* is certain. The wedge resembles the wedge-shaped ó of s6 *imádója*, which supports the o.
   - s4: the final e of *kedve[se]* is in the smear; the *se* that follows opens s5.
3. **Wiped and blotted places.**
   - Row 12: *az eső* and *és* lie in a wiped patch. *és* is a ghost three-bar with its accent plus a ghost s, read only under enhancement.
   - Row 14: a solid blot stands between *át* and *alszom*. It is taken as covering no letter of the word, or a slip; *átalszom* does not need a further sign.
   - Row 9: the a of *Béla* has its top bar clear and its lower bar under a blot.
   - Row 17: the n of *van* is a faded, smudged shape at the right edge, read from sense and the ghost of two strokes.
   - Row 18: the é sits under a heavy blot; its bars can be seen around it. Row 22: the o-n of *halgason* is blotted.
   - Row 6: the y of *vagyok* is smudged and postmarked. Rows 7–9 near x 1500 are under a green wash but legible.
4. **Readings resting on word sense.**
   - h/p: p in *vasárnap* (rows 4, 11, 14, 15, 18), and *pletykára*; h elsewhere. Row 26: the sign before *ögtön* is the clear h/p sign (stroke plus separate dot), where sense wants r: literal *högtön*, normalized *rögtön*. This is the writer's slip or an unusual form, not a clean sign match.
   - d/n: *n* in row 29 *esetén* and *d* in row 12 *délig* are by word sense.
   - Row 13: the first sign of *folyton* is a tilted cross taken as f (u gives no word).
   - s6: the sign written for ű of *hű* is the cross without visible dots; i of *imádója* has its dot lost in the smear; the ó is an unusual small sign with a wedge; s7 opens with tilted j.
   - s1: *Isten* shows two bars under the long t stroke (literal *istan*), the third bar being merged or omitted.
   - Row 22: the *ty* of *pletykára* is a joined sign seen only here.
5. **The writer's spellings, normalized.** *ojan/mihejt/hejzet* (j for ly), *fojton*, *éjel*, *akor*, *semi*, *halgason*, *ara*, *tehesem*, *ot*, *itédesem* (*itt*), *essö* (eső), *kimulattása*, *kedvébe* (for -ben), *örülö* (k omitted), *bodog-* (l omitted), *irntam* (á omitted), *helyzet* (acc. -et omitted in row 27), *szüksé* (g omitted), *siri* (g omitted: *sír[ig]*, a shortening noted on sister cards). The small two-dot a in row 5 (*már a*) sits squeezed between r and v. Most accents are not visible and are supplied.
6. **Row 28 *ahogy*.** After *fiatal* the card has a separate two-bar a before *hogy* (`work/crops2/hogy28.png`), so the literal text is *fiatalahogy*. Round 1 missed this sign. It is printed as *ahogy*. As a plain word that means "as", which fits poorly; the sense wanted is *ahhoz, hogy* ("young enough to …"), so this is taken as a telescoped form of that phrase or a slip. The translation follows that sense. The sentence does not change otherwise.
7. **k/g.** In row 24 *-ságunkat* the k-position sign looks like g; it is kept as literal g and normalized k. In row 13 the s of *most* has a longer stem than usual.
8. **Not part of the cipher.** The address (Tóth Jolánka, Jászárokszállás) is in plain hand; its first line is not read here. The picture side has a printed verse beginning *Messze vagyok de sohasem feledlek*. The postmark shows a line with 91 and C, not a date. The stamp is missing. The print number 6432 at the foot is a printer's mark overlaid by row 26's last sign.

## Why it is correct

- The family key, unchanged, turns all 29 rows and the 7 box rows into running Hungarian, with no invented value. All 796 letters take a key value; the softest call is the small cross of *Fe[ri]* (Uncertainty 1).
- The text is coherent and specific: rain, a soaked night, the sleep-through Sunday, the plea to ignore gossip, and the marriage promise answered by her earlier remark about waiting a year. The numerals 2 and 1 fit their phrases exactly.
- Family formulae and habits match: *Kívánom, hogy a legjobb kedvében találja soraim* (HCP1213, 1218), *Isten vele, édesem*, *sírig hű*, *imádója*, *Feri*, and j for ly.
- Repeated words decode identically: *édesem* ×7, *vasárnap-* ×5, *hogy* ×7, *helyzet* ×2. Round 1's automatic comparison of literal text and normalization showed only disclosed changes, but it could not see a sign missing from both, which is how row 28's a went unnoticed. The sign count now rests on the review's pass and the recheck of the row 28 and 29 ends.

Credit: transcription, key transfer and decipherment on this card by Claude Opus 5.5. The key itself was established on the family cards listed above, partly by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), with later work by Claude Opus 5.5.

## Response to review 1

Verdict REVISE. All five findings are addressed. The message body is unchanged except for one sign in row 28; the closing of row 29 is now read. I re-ran the command after the changes: all 4 hashes OK, 36 rows, 787 tokens, 796 letters. The new closing reading of finding 2 was made after the review, so no reviewer has checked it; this is stated here and in the report.

1. **Row 28 omitted sign: fixed.** The sign is on the card (`work/crops2/hogy28.png`). Added as a token: literal *fiatalahogy*, normalized *ahogy*, with the sense discussed in Uncertainty 6. English and Slovak adjusted. The sense of the sentence stands. The 792-letter count was wrong and is corrected.
2. **End of row 29: fixed, reviewer's hypothesis partly adopted.**
   - *First word*: agreed. Both middle signs are o, now in the ledger; printed *Csó[k]olja*.
   - *Second word*: tested, and I disagree that the hooked sign could be k. It has the form of the s that opens row 29 (`work/crops2/r29start.png`), and k on this card is the section mark. So it stays s, and *kedvesse* is read as *kedvese* by the writer's doubled-s habit, now with the reason given.
   - *Tail*: tested z. The cross has no z tail, so *kezé[t]* is not adopted. Read instead as tilted f, as in *fiatal* just above, giving *Fe[ri]*, with the doubt stated in Uncertainty 1.
   - Completeness: at worst one word (*Fe[ri]*) rests on sense. The rest reads, so the card counts as complete.
3. **Command does not really decode: fixed.** The ledger now holds sign-class tokens (`work/ledger-signs.txt`), and `decode_opus.py` applies a key table, which is also copied into this file. SOLUTION.md says plainly that the classes were assigned by hand with the key in view and that the normalization is an editor's file.
4. **Ledger and disclosure gaps: fixed.** The row 28 g note was wrong and is corrected: g and y are both visible on the enlargement, so I did not bracket them. Row 17 n, row 18 é and row 22 o-n are added to Uncertainty 3.
5. **Support for s3: adopted.** The resemblance is cited in Uncertainty 2. The literal text stays *marad*.

Not changed: the portal's detail tabs remain unread (see `source/metadata.md`), so "no attached solution or transcription" rests on the catalogue row and sister cards. The address first line and postmark date remain unread.
