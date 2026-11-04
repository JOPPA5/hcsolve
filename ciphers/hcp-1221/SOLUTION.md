# HCP1221 — Feri (?) to Jolánka Tóth: too busy to write, settling with the master on Saturday

**Status: complete reading, corrected after review 1 (REVISE). One sign in rows 7–8 rests on word sense (Uncertainty 1); the unenciphered sender line has unresolved words (Uncertainty 13).** Claude Opus 5.5, 2026-11-02.

Credit: transcription and reading of this card are by Claude Opus 5.5 from the portal's un-converted scan (`work/hires/`). The key was not rebuilt here: it is the Jolánka-family key reconstructed on the finished cards HCP1216, 1212, 1213, 1217, 1218, 1243, 1301 (earlier work by the OpenAI GPT solver, completed by Claude Opus 5.5). The portal shows status Not solved and attaches no transcription or solution; no published solution of this card was found. The portal links the HistoCrypt paper as its general collection source; that paper was not consulted for this reading.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC, Jolánka family); word divisions are not marked. Key as in `ciphers/hcp-1216/SOLUTION.md`:

*Type note (2026-11-03):* the card hides a 7-row enciphered message in the stamp box, under the (now lifted) stamp, so the type is **MASC + Steganography** (register label); see "Stamp-box message (2026-11-03)".

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / 8 / open S | k | F-like | r |
| six | b | wave | l | right bowl (also with small top loop) | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| long stroke + tick LEFT | d | two strokes | n | plain bold X | u |
| three bars | e | crossed curve, no dot | o | chevron | v |
| upright cross | f | long stroke + tick RIGHT | h / p (one sign) | low descender | y |
| open hook with descender | g | crossed curve, dot | i | X with tail / crossed diagonal | z |
| inverted T | j | | | | |

Accents are small ticks over the sign (á, é, í, ó), two ticks give ö/ő/ü. This writer spells gy as separate g + y. New on this card: nothing; every sign fits the family key. Word-sense calls: every h versus p on this card is chosen by word sense, because they are one sign; one d in row 7 has the tick on the right (Uncertainty 1); n versus d is otherwise decided by stroke length and tick, with the kinked n of row 10 *nem* read by sense.

The picture side is a printed photograph (publisher number 1012) with no writing, so all ciphertext is on the address side: 20 rows at the left and 7 rows under the (lost) stamp.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1221/work/decode.py
```

It checks the SHA-256 of both `source/` scans and both `work/hires/` originals, decodes the sign ledger `work/ledger.txt` (one token per written sign, a manual transcription from enlarged crops, not OCR), prints the literal letters row by row, then the normalized text `work/normalized.txt`.

## Literal decipherment (as printed by the command)

```
01 szeretetedesjolan              12 lennimegmostnem
02 kamneharagudjonhogy            13 tud[o]kírnisemi
03 ojritkanirókmert               14 ujsakotmertcsak
04 nagyonelvagyok                 15 szombatonegyezek
05 foglalvameeste                 16 amesterrelhat
06 8oraigdolgozok                 17 jolakaéknalmiuj
07 mertaholdolgo                  18 ságvasár[na]pbemegyek
08 zoksürgősamun                  19 pestremegnezemlatogatomapesti
09 kaésojkésőidegen               20 eket
10 haznalnemle                    under stamp: istenve / leavi / szont /
11 hetojkesőnfel                  latas / igmely / barso / kalesz
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Ne haragudjon, hogy oly ritkán írok, mert nagyon el vagyok foglalva. Még este 8 óráig dolgozok, mert ahol dolgozok sürgős a munka, és oly késő; idegen háznál nem lehet oly későn fel lenni. Még most nem tudok írni semmi újságot, mert csak szombaton egyezek a mesterrel. Hát Jolá[n]káéknál mi újság? Vasárnap bemegyek Pestre, megnézem, látogatom a pestieket.

Under the stamp: Isten vele a viszontlátásig, mely bár soká lesz.

## English

My beloved sweet Jolánka! Do not be angry that I write so rarely, for I am very busy. I work until 8 in the evening, because where I work the job is urgent, and it is so late; in a stranger's house one cannot stay up so late. I cannot yet write any news, because only on Saturday do I come to terms with the master. So what is new at Jolánka's family? On Sunday I am going in to Pest; I will look up and visit the people from Pest.
Under the stamp: God be with you until we meet again, though that will be long (or, if *bár* is a wish here: which I wish were not so long; see Uncertainty 14).

## Slovak

Moja milovaná, sladká Jolánka! Nehnevajte sa, že píšem tak zriedka, ale som veľmi zaneprázdnený. Pracujem až do 8 hodiny večer, lebo tam, kde pracujem, je práca súrna, a je tak neskoro; v cudzom dome nemožno byť tak neskoro hore. Zatiaľ Vám neviem napísať nijaké novinky, lebo až v sobotu sa dohodnem s majstrom. Tak čo je nové u Jolánkiných? V nedeľu idem do Pešti, pozriem si a navštívim Peštianov.
Pod známkou: Boh s Vami, do videnia, hoci to bude ešte dlho.

Addressee and sender (unenciphered, see below): Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás. Sender line: Rákos Szent Mihály, "Emocn(?) Telep(?)", Bocskai utcza 3.

## Stamp-box message (2026-11-03)

Stamp-box audit at the request of Tomáš Pavuk (register type for the Tóth Jolánka cards). The stamp is lifted; under it, in the stamp box at the upper right, are 7 short rows in the same red ink and the same cipher signs (not plain Hungarian), crossing an old grey postmark ring. Crops of the un-converted original (`work/hires/*_adr.jpg`): `work/stamp-2026-11-03/stamp_box.png`, `stamp_top_3x.png`, `stamp_bot_3x.png`. I re-read every sign on these crops with the family key; the reading agrees sign for sign with ledger rows S1–S7 of 2026-11-02, so nothing was added and `decode.py` / `work/ledger.txt` were left unchanged (they already print these rows).

- Literal: `istenve / leavi / szont / latas / igmely / barso / kalesz`
- Hungarian: Isten vele a viszontlátásig, mely bár soká lesz.
- English: God be with you until we meet again, though that will be long.
- Slovak: Boh s Vami, do videnia, hoci to bude ešte dlho.

Nothing stays unread. Restorations: none; the only soft points are the two i signs without a certain dot (*Isten*, *-ig*) and the sense of *bár* (Uncertainties 11 and 14). There is no signature in the box.

## Uncertainties

1. **Rows 7–8, `ahol dolgozok`.** The signs are clear: a, long stroke with tick right, o, l, the same stroke with tick right, o, l, g, o, z, o, k, with no accent. The first is the ordinary h (*ahol*). The second has to be d in *dolgozok*, with the tick on the unusual side: the five other d on this card (rows 1, 2, 6, 9, 13) have it on the left. This one sign is a word-sense call; the same anomaly occurs on HCP1216 (*de*). The word itself is not in doubt: the clause is plain grammar and repeats *dolgozok* of row 6.
2. **Row 6, first sign.** A tall 8 with a long tail. It has the shape of the k sign (row 14 *csak*) but *k óráig* gives nothing; it is read as the digit 8 from sense. Also in this word the i of *óráig* shows no dot (word sense; *-oig* is not possible).
3. **Row 5, `me este`.** Two signs of three bars, read m-e e-s-t-e; normalized *még este* with the g **not on the card** (the same writer omits it on HCP1216, row 4).
4. **Row 10, blot in `ház▓nál`.** A heavily inked rectangular blot between z and n, with an underlying grey spot. *háznál* (blot deleted, chosen) or *házánál* (blot = á) are both possible; only *háznál* is idiomatic with *idegen*. The meaning is the same. The n of *nem* in the same row has a kinked first stroke, read n by sense.
5. **Row 13, `tud[o]k`.** The sign between d and k is overwritten: a bold X body with two horns. Exactly one letter gives a word (*tudok*); this is a restoration, disclosed.
6. **Row 18, `vasár[na]p`.** After r comes a dark # blot whose bars and strokes fit an overwritten two bars + two strokes; it is restored as *na* from *vasárnap*. Also the g of *ság* in this row has a pink blot over its top; the visible tail fits g. The a before it carries a visible acute.
7. **Row 14, `ujsakot`.** The sign is k (open S), not the g of this card; normalized *újságot* (writer's slip). Same word in rows 17–18 has a true g. Rows 3, 4 and 15 confirm the S form as k.
8. **Row 17, `jolakaéknal`.** Written without n; normalized *Jolá[n]káéknál* ("at Jolánka's family"). The third bar of é is short and sits low; an acute lies above it. *Jolánkáék* appears on HCP1296. The writer referring to the addressee's household in the third person is not unusual for the family.
9. **Row 16, `mesterrel`.** The sign after r r has three bars (e), so there is no slip. *hat* (two bars, clear) = *hát*. *egyezek* (row 15) is taken as "I come to terms" (presumably about pay or a post); the reason is not stated on the card.
10. **Row 19.** *megnézem, látogatom*: two verbs without a conjunction, as written. The wave before *átogatom* looks like a Latin a with a doubled stroke but is the l wave. The sign t in *látogatom* (second t) has its bar detached.
11. **Under the stamp.** Rows S1–S4 cross an old stamp-area postmark, S3 is faint; all signs were readable. The first i of *Isten* is smudged and shows no certain dot; the i of *-ig* also shows no dot. *mely* has wave + y (ly); there is no signature. The sentence stops at *lesz*. "Feri" in the title is inferred from the hand, key and sister cards (HCP1309: Holes Feri, formerly at Szentmihály), not written here.
12. Other spellings normalized: *szeretet* → szeretett, *oj* → oly, *semi* → semmi, *nezem* → nézem; word division and most accents are editorial.
13. **Sender line (plain Latin script).** "Rakos Szent Mihaly", then a word that I can read only as "Emocn" (E-m-o-c-n or -u), then an overwritten word best fitting "Telep", then "Bocskai utcza 3". Neither word is resolved. It may be a locality or a person ("care of"); the card does not settle which. It is reported literally. The cancellation shows only "C 12" (no date legible), so the card is undated.
14. **Stamp block, `mely bár soká lesz`.** The signs are clear, but *bár* leaves the sentence slightly hanging. The main sense taken is concessive ("though that will be long"); a wish sense of *bár*, or a dropped *nem* ("which I wish would not be long"), is also possible. The farewell is the same either way.

## Why it is correct

- The family key, transferred unchanged, turns every sign of all 27 rows into Hungarian; no new sign values were needed, and the key was not adjusted to fit.
- The text is coherent colloquial Hungarian with the family's address (*Ön* forms) and opening, and its phrases recur on sister cards (*mi újság*, *oj*, *viszontlátásig*, *szombaton*, *vasárnap ... Pest*).
- Details fit the correspondence: HCP1309 has Feri leaving Szentmihály for Rákospalota; this card is sent from Rákosszentmihály and speaks of a master and a job, and of living in a stranger's house.
- Repeated words decode identically (*mert* ×3, *oj* ×3, *most/nem*, *dolgoz-*, *újság* ×2).

## Response to review 1

Verdict REVISE. I rechecked each point on the reviewer's crops and scan before changing anything. All seven are addressed; the reading of the card stands, with one clause corrected.

1. **Rows 7–8 (major): fixed.** Crop `review/work/z7.png` shows the two stroke-with-right-tick signs as described. `ahol dolgozok` removes the false start and gives grammar. Ledger row 7 is now `H ... D?` (new token `D?`, decoded by `decode.py`, marks the one word-sense d). Normalized text, English, Slovak and Uncertainty 1 changed. The translation now reads "because where I work the job is urgent".
2. **Row 16 (major): fixed.** Crop `review/work/z16c.png` shows three bars. I reran `review/work/profile.py`: three bands, against two for the a of *hat*. The ledger token is now E, `mesterrel` needs no normalizing, and Uncertainty 9 no longer claims a slip. NOTES.md keeps its first entry as history, with a correction added.
3. **False accent (minor): fixed.** The normalized text is now *dolgozok*; ledger and literal text always had `zok`.
4. **Row 18 acute (minor): fixed.** Crop `review/work/z18a.png` shows the tick. Ledger token now `A:acute`, literal `ság`. The text is unchanged. Uncertainty 6 notes it.
5. **Miscount (minor): fixed.** Uncertainty 1 now says five other d, rows 1, 2, 6, 9, 13.
6. **Sender line (minor): addressed.** Crop `review/work/sender.png` shows what the reviewer saw. Uncertainty 13 now says `Emocn`, drops my guesses (Émócsán, Fülöp), and leaves open whether it is a locality or a person. It is an address, not a clause of the message.
7. **`mely bár soká lesz` (minor): addressed.** Alternative recorded in the English and in Uncertainty 14.

The reproduction command was rerun after these changes: all four hashes OK, and its literal output matches the block above.
