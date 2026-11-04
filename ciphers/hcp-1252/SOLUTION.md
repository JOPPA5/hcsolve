# HCP1252 — Feri to Jolánka Tóth: thanks for her letter, "we should say *te*", and a pay sum (railway work inferred)

**Status: complete reading of the cipher block (8 rows, 180 tokens); the plain handwriting below it is also read, with one small itinerary phrase not understood. Review 1 verdict ACCEPT; see the response at the end.** Claude Opus 5.5, 2026-11-01.

Credit: all reading here is by Claude Opus 5.5 on 2026-11-01. There is no earlier work on this number. The key is the Jolánka-family key established on finished cards (hcp-1216 and sisters; earlier work there by the OpenAI GPT solver and Claude Opus 5.5). The portal shows status Not solved and attaches no transcription or solution; I found no published solution. The ledger is a manual transcription from the pixels (not OCR).

## The card

Filename date 1913-06-13 (the postmarks are not legible enough to confirm it). Address side has three parts: a **cipher block** (top left, 8 rows), then **plain Hungarian handwriting** in the same green ink running on under it and across the bottom of the card, then the plain address and a plain greeting written inside the stamp box, under the (now lifted) stamp. The picture side (a couple, printed song text "Cigányprímás / Lári-Fári", Amag 60681/5) has no handwriting. So only part of the message is enciphered.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC), key transferred unchanged from hcp-1216. 

**Type update (2026-11-03): MASC + Steganography.** The stamp was stuck over a plain Hungarian greeting written inside the stamp box; the stamp is now lifted and the greeting is exposed (see "Stamp-box message (2026-11-03)").

Sign classes used on this card:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left + right bowl pair | cs | three short strokes | m | gamma/corner | t |
| stroke + tick to its left | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| open hook with descender | g | stroke + tick to its right | h/p | low descender | y |
| dotted crossed curve | i | inverted T | j | crossed diagonal | z |

No f, c alone, or digraph gy sign occurs: this writer spells gy as g + y (*hogy, így, egymást*), and *melyet* shows the y sign alone. Dots over o/u mark ö/ü. The digits **10** are written plain inside the cipher block (row 7).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1252/work/decode_opus.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger-opus.txt` with the key, and prints the literal rows and then `work/normalized-opus.txt` (editorial; includes the plain parts).

## Literal decipherment

```
1 szeretetetedesjolankam
2 becsessoraitmegkahtammelyet
3 igenkoszönök.igazanorü-
4 lökhogyigyszolimarne
5 künktegeznikeleneegymast
6 edesem,kedvesemneharagudjon
7 hogyrövidenirokde10re
8 rendezonkellenni.
```

## Plain handwriting, as written

```
9 án indultam 4·30 p kor Érsek
ujvára érk. 10 én éjel 1ó
30 p vigas in. 18 ól. u 1ó 11 p
rendezőre érk. 11 éjel 1ó 30 p
Kedvesem számítsa
ki mit kerestem csináltam
23[7?] km fizetne 6 tized fil
kilométerenkint és 33 órát
a 8 fil és 2 korona napi
díj most mást nem irok
men/mer menem kel 10 órára rendezö(i)nkbe lenem
majd legközelebb bővebben isten vele édesem
más külömben jó dolgom van
```
In the stamp box, under the lifted stamp: *Csókolom számtalanszor Feri*. Address: *Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás*.

## Hungarian (normalized)

Cipher: Szeretett édes Jolánkám! Becses sorait megkaptam, melyet igen köszönök. Igazán örülök, hogy így szólí[t]. Már nekünk tegezni kellene egymást, édesem, kedvesem! Ne haragudjon, hogy röviden írok, de 10-re rendezőn kell lenni.

Plain: 9-én indultam 4.30 p-kor Érsekújvárra, érk. 10-én éjjel 1 ó 30 p. {vigas} in. {18 ól. u} 1 ó 11 p. rendezőre érk. 11[-én] éjjel 1 ó 30 p. Kedvesem, számítsa ki, mit kerestem! Csináltam 23[7?] km-t, fizetne 6 tized fillért kilométerenkint, és 33 órát a 8 fillér, és 2 korona napidíj. Most mást nem írok, mer[t] mennem kell, 10 órára rendezőnkbe lennem. Majd legközelebb bővebben. Isten vele, édesem. Máskülönben jó dolgom van.

In the stamp box (under the stamp): Csókolom számtalanszor. Feri

## English

Cipher: Beloved sweet Jolánka of mine! I have received your precious lines, for which I thank you very much. I am truly glad that you address me like this. We ought to be saying *te* to each other by now, my sweet, my darling! Do not be angry that I write briefly, but by 10 I have to be at the marshalling yard.

Plain: I left on the 9th at 4.30 for Érsekújvár, arrived on the 10th at 1.30 at night; {vigas} dep.(?) {18 ól. u} 1.11, arrived at the yard on the 11th at 1.30 at night. Darling, work out what I earned! I did 23[7?] km; it would pay six tenths of a fillér per kilometre, and 33 hours at 8 fillér, and a 2-crown daily allowance. I write nothing else now, because I have to go, I must be at our yard by 10 o'clock. More next time. Farewell, my sweet. Otherwise I am doing well.

In the stamp box (under the stamp): I kiss you countless times. Feri

## Slovak

Šifra: Milovaná sladká moja Jolánka! Vaše vzácne riadky som dostal, za čo veľmi ďakujem. Naozaj sa teším, že ma takto oslovujete. My by sme si už mali tykať, drahá moja, milá moja! Nehnevajte sa, že píšem stručne, ale do desiatej treba byť na zoraďovacej stanici.

Nezašifrované: Deviateho som odišiel o 4.30 do Nových Zámkov, prišiel som desiateho v noci o 1.30; {vigas} odch.(?) {18 ól. u} 1.11, na zoraďovaciu stanicu som prišiel jedenásteho v noci o 1.30. Drahá, vypočítajte, čo som zarobil! Urobil som 23[7?] km, platili by šesť desatín halierika (fillér) za kilometer, a 33 hodín po 8 fillérov, a 2 koruny denné. Teraz viac nepíšem, lebo musím ísť, o desiatej musím byť na našej stanici. Nabudúce viac. S Bohom, drahá. Inak sa mám dobre.

V políčku na známku (pod známkou): Bozkávam Vás nespočetnekrát. Feri

## Uncertainties

Cipher block:

1. **Row 1 *szeretetet édes***: the signs are clearly e-t-e-t-e-t-e-d, one *-et-* too many for *szeretett*. Normalized *Szeretett* as on hcp-1216; the card literally has *szeretetet* (a slip, or accusative "love"). No effect on the sense.
2. **Row 4 *szoli már***: the letters after *o* are l, i, then three strokes m, a, r. Normalized *szólí[t] már*, with an unwritten final t. Support for a dropped final t comes from *mer* on hcp-1216, where *mer[t]* is on record; the *mer* on this card is itself a reading (uncertainty 13) and is not independent evidence. Sense-based; whether *már* closes this clause or opens the next is editorial. The t is **not** on the card.
3. **Row 7 "10"**: a flagged upright stroke plus a filled ring, then *re*. Read as digits by shape (it is not the d or h sign, which have a separate tick) and from the plain text's *10 órára rendező…*. Without the digits *h o r e* gives no word.
4. **Row 8 *rendezon***: the o has no visible dots and is thick with ink; *ö* in *rendezőn* is supplied, the plain text has *rendezőre* with dots.
5. **Row 8 *kel lenni***: two waves then *enni*: k-e-l-l-e-n-n-i. Read as *kell lenni* with one l shared, the writer's *kel* spelling (cf. plain *kel*, row 5 *kelene*). *Kell enni* ("one must eat") is the alternative division; the plain text's *rendezőnkbe lenem* decides for *lenni*.
6. **Row 3 *köszönök***: final sign is the section mark k, followed by a dot; normal grammar would want *köszönöm* with *melyet*. Transcribed as written. The first o shows no dots; ö supplied.
7. **Row 2 blot**: the sign after *sorai* is overwritten into a dark blot, but its top bar and form fit the gamma t; *sorait* is the only fit. Row 2 *p* of *megkaptam* is also heavily inked.
8. **Calls resting on word sense**: h vs p uses the same sign (h in *hogy* ×2, *haragudjon*; p in *megkaptam*). d vs h was decided by the side of the tick (left: *édes, édesem, kedvesem, haragudjon, röviden, de, rendezőn*; right: h/p), which held throughout, and d vs n were never confused here because the n strokes are short and equal. z vs u follows the tail on the cross (z in *köszönök, igazán, szólí, tegezni, szeretett, rendező*; ü in *örülök, nekünk*), with dots on both ü.
9. **Spellings normalized**: *kelene* → kellene. Accents on a, e, i, o, u are invisible and supplied.

Plain handwriting (not enciphered; an ordinary cursive reading):

10. **{vigas} in. {18 ól. u}** (third plain row): letters read as v-i-g/z-o/a-s, "in.", 18, "ol.", "u", but I do not understand this short itinerary phrase; *in.* as *indultam/indulás* is a guess. It looks like a place or a time note between 1.30 and 1.11. Reported literally and left untranslated. Open hypothesis, not adopted: *vissza in[dultam]* ("started back"), because the sequence wants a return leg (out to Érsekújvár, then arrival back at the yard on the 11th). The pixels are v, i, a descending z/g-like letter, then a/o and s; I could not confirm *vissza* on them. The cipher block is unaffected, and this phrase is the one limit on the claim of a complete reading of the card.
11. **23[7?] km**: the third digit is a crossed sign with a faded streak above; 7 is likely (a continental crossed 7), not certain.
12. **indultam** ends in a flourish and could be seen as *-tara*; only *indultam* makes a word. **ujvára** has one r (Érsekújvárra).
13. **men/mer**: the word opening that row looks like *men*; read *mer[t]*, because the writer's r and n are close and *mer* is his form on hcp-1216 (that is the only support; the word on this card looks like *men*). Then *menem kel* = *mennem kell*, *lenem* = *lennem*.
14. **rendezö(i)nkbe**: partly under the HCPortal stamp; the letters after *rendez* could be *-ő-nk-* or *-öi-nk-*. *Rendezőnkbe* ("to our yard") is normalized. Marshalling yard for *rendező* is an inference from km pay, hours and arrival times, plus the plain use of *rendezőre érk.*; the writer's job is not stated.
15. **fizetne** is literal; **csináltam** could be *csináltan*.
16. **Máskülönben jó dolgom van**: the last row is faint and the final word runs into a blot; *dolgom* uses his *cl*-shaped d, and *van* is the best fit for a smudged word.

The sender is "Feri" (signature in the stamp box, under the stamp), matching the name on hcp-1216; I claim nothing further. The portal lists Sender Unknown.

## Why it is correct

- The hcp-1216 key, transferred unchanged, gives Hungarian for all 174 key signs among the 180 tokens (the other six are 2 digits, 2 dots, 1 comma and 1 hyphen), with no sign left without a value and no invented sign.
- The text is idiomatic and fits itself: the writer switches to plain to give dry details that the cipher mentions (cipher *10re rendezőn kel lenni* = plain *10 órára rendező…*). The plain text was read after the cipher hypothesis but independently of the key.
- Repeats decode identically: *hogy* ×2, *így/egymást* with g + y, *édes/édesem*, and the word split across rows 3–5 with a written hyphen (*örü-lök*) and *ne-künk* at a row end.
- The address, hand, ink and signature agree with the Jolánka family.

## Response to review 1

Verdict ACCEPT, four minor findings, all in the wording. All are addressed here and in the report. The ledger, key, script and reading are unchanged; `python3 -I ciphers/hcp-1252/work/decode_opus.py` was re-run and prints all four hash checks OK and the same eight rows.

1. **Unread itinerary phrase (accepted).** Uncertainty 10 now states this phrase as the limit on the claim of completeness and records *vissza in[dultam]* as an open hypothesis. I re-read the row from a fresh enlargement (work/crops/report-row3.png) and also cannot confirm *vissza*, so the phrase stays untranslated and the gloss stays "dep.(?)". The report keeps it outside the complete reading.
2. **Circular *mer* (accepted).** Uncertainties 2 and 13 now rest the dropped t on hcp-1216 only.
3. **Title (accepted).** The heading no longer asserts a railwayman; the report marks the railway job as an inference, as uncertainty 14 does.
4. **"Every one of the 180 tokens" (accepted).** "Why it is correct" now says 174 key signs plus 6 digits and punctuation marks.

Not verifiable, as the reviewer notes: the third digit of 23[7?], the date 1913-06-13 (from the filename only), and the supplied accents. All three stay disclosed.

## Stamp-box message (2026-11-03)

Audit by Claude Opus 5.5 on 2026-11-03 at the request of Tomáš Pavuk, from the original work/hires/cpc_1913-06-13_HU__HU_Jasz-Arokszalas_jolanka-37_adr.jpg (crops at 2x, 3x and 5x red channel in work/stamp-2026-11-03/).

- **State of the stamp box:** the stamp has been lifted. Torn perforated fragments of it still stick to the card (the top-left corner with the green frame and lattice, a strip at the top, small pieces at the right edge and the bottom corners), and the red printed circle of the card's stamp box shows through. The greeting lies inside the outline of the stamp, so it was covered by the stamp when the card was posted. The first letters of rows 1 and 2 run under the curled left fragment.
- **Script:** plain Hungarian in the same green ink, no cipher signs.
- **Literal reading (4 rows):** `[C]sokolom / szamta / lanszor / Feri`
- **Normalized Hungarian:** Csókolom számtalanszor. Feri
- **English:** I kiss you countless times. Feri
- **Slovak:** Bozkávam Vás nespočetnekrát. Feri
- **Restoration disclosed:** the initial *C* of *Csókolom* is mostly under the stamp fragment; only its entry stroke is visible before the *s*. *Cs* is the only letter that makes a word here. The accent of *ó* is not visible.
- **Unread:** nothing else; the four rows are read in full.

This greeting was already read on 2026-11-01 but recorded as "beside the stamp"; the audit corrects its position to under the stamp. The reading itself is unchanged. The reproduction script (work/decode_opus.py) covers only the cipher block and is not changed; the stamp-box text is read by eye.
