# HCP1304 — Feri to Jolánka Tóth: broke, waiting on work from the Moczárs, conscription and a mass strike

**Status: complete reading of all cipher text on the card, with small disclosed sign calls and no unread fragment. Review 1 verdict REVISE, all findings addressed below; closed with FINAL.** Claude Opus 5.5, 2026-10-30.

Credit: all of this reading is by Claude Opus 5.5, 2026-10-30, directly from the card's un-converted scan. There is no earlier work on this number. The key comes from the finished Jolánka family (HCP1216, 1212, 1213, 1217, 1218, 1243, 1301), established by the OpenAI GPT solver and Claude Opus 5.5 on those cards. The portal shows *Not solved* and attaches no transcription or solution; no published solution of this card turned up; the orchestrator's AI-register check of 2026-10-30 found no record. The transcription is manual, not OCR. It was made from pixels, but word sense guided it, so it is not blind.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the Jolánka postcard family; same key as HCP1216 and sisters, unchanged). Word spaces are partly kept; dots and double marks over vowels are written, acute marks mostly not.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | S / section shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma corner | t |
| long + short joined | d | two short strokes | n | short thick cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall + short (h/p near-homograph) | h / p | low descender | y |
| open loop + descender | g | crossed curve, dotted | i | crossed diagonal | z |
| inverted T | j | opposed bowls | cs | | |

## Layout of the text

Rows 1–24 fill the left half. Rows 25 and 26 run across the whole bottom edge. Row 26 turns the bottom-right corner and goes up the right edge to the top corner. Five more rows stand in the stamp box, under the removed stamp. The picture side is a printed photograph of a couple with a printed series number (3801/02 as far as it can be read) and no handwriting. The plain address reads *Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás*. Two cancels are on the address side. The one at the stamp box shows GYÖN (a further letter or more is not legible), and the fainter one shows …ÁS, which fits the destination Jászárokszállás. No date is readable, so the card is undated. Gyöngyös would fit GYÖN and *lemegyek* but is not proved.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1304/work/decode.py
```

It checks the SHA-256 of both `source/` scans and both `work/hires/` originals, decodes the sign ledger `work/ledger.txt` (603 tokens, one per written sign) with the key above, prints the literal letters row by row, and then prints `work/normalized.txt`.

## Literal decipherment (as printed by the command)

```
01 szeretetedesjolan              14 nekjolankatolugyen
02 kambecsessoraitmeg             15 elmenekavarosbolha
03 kahtammelyetköszö              16 sorozasnemlenneazt
04 nökszehenigazanmeg             17 megkelvarnom.megez
05 hatsoraimiböllatom             18 atömegsztrajkisakadajoz
06 milynemesszivevanön            19 akedvesmamajaelotres
07 nekedesjolankamamitta          20 tellemmagamhazudni
08 lannemiserdemlekmeg.           21 nemtudokigyjolankais
09 marmagamisrestelemhogy         22 tudjahogynehezahejze
10 igylevagyokegvehamo            23 temmoczarmegnemirt
11 czareknembiztatnanak           24 tala{n}aztgondoltahogy
12 munkavalegyszerüenugy          25 vasarlemegyekdenemmertemmertgyülesvoltatö
13 tennekminthamesszevol          26 megsztrajkmiattamazthiszemkedenkezdodikhava
                                   M lamithalmoczareknair{o|i}ameg  (up the right edge)
stamp box: istenvele | edesem | sirighü | kedvese | feri
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Becses sorait megkaptam, melyet köszönök szépen. Igazán meghat sorai, miből látom, mily nemes szíve van önnek, édes Jolánkám, amit talán nem is érdemlek meg. Már magam is restellem, hogy így le vagyok égve. Ha Moczárék nem biztatnának munkával, egyszerűen úgy tennék, mintha messze volnék Jolánkától. Úgy én elmennék a városból, ha sorozás nem lenne, azt meg kell várnom. Még ez a tömegsztrájk is akadályoz. A kedves mamája előtt restellem magam, hazudni nem tudok, így Jolánka is tudja, hogy nehéz a helyzetem. Moczár még nem írt. Talán azt gondolta, hogy vasár[nap] lemegyek, de nem mertem, mert gyűlés volt a tömegsztrájk miatt, ám azt hiszem, kedden kezdődik. Ha valamit hall Moczáréknál, írja meg.

Under the stamp: Isten vele, édesem! Sírig hű kedvese, Feri.

## English

My beloved, sweet Jolánka! I received your esteemed lines, for which I thank you very much. Your lines truly move me; from them I see what a noble heart you have, dear Jolánka, which perhaps I do not even deserve. I am already ashamed myself of being so broke. If the Moczárs were not encouraging me with work, I would simply act as if I were far away from Jolánka. So I would leave the city if there were no conscription; I have to wait for that. On top of that this mass strike is holding me back too. I am ashamed before your dear mother; I cannot lie, so Jolánka too knows that my situation is hard. Moczár has not written yet. Perhaps he thought that I would go down on Sunday, but I did not dare, because there was a meeting on account of the mass strike; but I believe it starts on Tuesday. If you hear anything at the Moczárs, write and tell me.

Under the stamp: Farewell, my darling! Your sweetheart, faithful unto the grave, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Vaše vzácne riadky som dostal, za čo Vám pekne ďakujem. Vaše riadky ma naozaj dojímajú; vidím z nich, aké ušľachtilé srdce máte, drahá Jolánka, čo si možno ani nezaslúžim. Sám sa už hanbím, že som taký bez peňazí. Keby ma Moczárovci nepovzbudzovali prácou, jednoducho by som sa správal, akoby som bol ďaleko od Jolánky. Tak by som ja odišiel z mesta, keby nebolo odvodov; na tie musím počkať. Navyše mi prekáža aj tento masový štrajk. Pred Vašou milou mamou sa hanbím, klamať neviem, a tak aj Jolánka vie, že moja situácia je ťažká. Moczár ešte nepísal. Možno si myslel, že v nedeľu prídem dole, ale neodvážil som sa, lebo kvôli masovému štrajku bolo zhromaždenie; myslím však, že sa to začne v utorok. Ak niečo počujete u Moczárovcov, napíšte mi to.

Pod známkou: S Bohom, drahá! Váš do hrobu verný milý, Feri.

## Uncertainties

Every sign is transcribed as written; the normalization is editorial.

1. **Row 25 end, `volta tö|meg`.** After *volt a* comes a t drawn with a pen lift: a thick stroke, then a separate long, nearly horizontal arc hooked down at its end. That is the gamma, not the short steep tick of the h/p sign. The loop after it has two marks to its upper right, a heavy stroke and a small tick, the same pattern as the ü of *gyülés* in this row. With row 26 `meg sztrajk` this gives *a tömegsztrájk*, the compound on row 18. The two marks are small, so the dots rest partly on that matching shape and on the resulting word. The row break falls inside the compound, as at *Mo|czárék* and *rest|ellem*.
2. **Row 26 margin, `ir{o|i}ameg` → *írja meg*.** On the card: dotted i, F (r), a loop without a dot, two bars, *meg*. No inverted-T j is written. *írja meg* ("write it") is chosen by sense and by the formal address; literally the signs give *iro a meg* or, with a dotless i, *iria meg*. *Írom meg* ("I shall write") is excluded because the two-bar sign stands before the m.
3. **Row 24 `tala{n}` → *talán*.** The sign is tall stroke + short tick, normally h/p, not two short strokes. Value n is from word sense only (*tala? azt gondolta*); this is a d/n/h stroke-length call.
4. **Row 20 `hazudni`.** The dot below the final sign belongs to row 21, but a dark mark stands directly above the sign and is not part of row 19's e. It is most likely this i's dot, though it could be accidental; *hazudni* is the only sense either way. The z here, in *azt*, *kezdődik* and *biztat-* is the near-upright variant of the crossed diagonal, close to f; z rests on word sense in those words.
5. **Row 3 `kahtam`.** A blot lies over the top of the h/p sign; the tall + short sign is visible beside it. Also h/p by sense in *kaptam*, *szépen* (`szehen`); the same h sign is real h in *hogy*, *hat*, *ha*, *hal*.
6. **Row 8 `talan`.** The second-syllable sign shows two bars and an ink spot below; read a, e not excluded by shape alone.
7. **Rows 14 and 22, j against f.** In row 14 `jolankatol` the j has a slight overshoot and looks a little like a low cross; *Jolánkától* fixes it. In row 22 `hejzetem` the crossbar stands low with a short tail below it, closer still to a cross; f is excluded only by word sense.
8. **Row 26 `miattamazt` → *miatt, ám azt*.** All signs are clear; the division is editorial. *Ám azt hiszem, kedden kezdődik* is ordinary Hungarian. What starts on Tuesday is not said; the strike is the only subject in the clause before it, but that is an inference.
9. **Row 5 `meghat`** spans rows 4/5 (`meg | hat`); a t-sign in this row has a dot beneath it that seems accidental. The present tense *meghat* is taken as written.
10. `ugyen` is taken as *úgy én*, two words, not as a misspelt *ugyan*: no a is written, and "so I would leave" follows *mintha messze volnék*. Writer's spellings normalized: *szeretet* → szeretett, *restelem* → restellem, *elmenek* → elmennék (one n written), *kel* → kell, *kedenkez-* → kedden kez-, *akadajoz* → akadályoz (j for ly), *hejzetem* → helyzetem, *elot* → előtt, *vasar* → vasár[nap] (abbreviation, omission, or the older form *vasár* for Sunday; *vásár[ra] lemegyek*, "go down to the fair", is possible with an assumed omission, and the translation keeps Sunday), *Moczareknal* written *Moczarekna* (final l omitted), *hal* → hall, *biztatnanak* → biztatnának. Accents are mostly unwritten and are supplied. *Le vagyok égve* is the idiom "I am broke"; *lemegyek* "I go down" presumably to the addressee's area; *sorozás* is military conscription.
11. *Moczár* is read as a surname from three independent occurrences (rows 10/11, 23, margin); no outside identification is claimed. *Mamája* is taken as the addressee's mother, and the third-person *Jolánka* as polite reference to the addressee, in the family's formal *Ön* style. The subject of *gondolta* is taken to be Moczár; that is interpretive.
12. The strike suggests a date around the Hungarian labour unrest of the 1910s, but the card itself gives no date and I claim none.

## Why it is correct

- The family key, unchanged, turns all 603 signs into Hungarian. No key change was needed, and no fragment stays without a word.
- Words recur identically in unrelated places: *Jolánkám/Jolánka* ×4, *hogy* ×3, *Moczár* ×3, *sztrájk* ×2, *restel-* ×2. *Tömegsztrájk* occurs twice, on row 18 and across rows 25/26.
- Grammar that was not expected from the guide works out on the signs: *köszönök szépen*, *biztatnának* (conditional, with the *-na-* written out), *le vagyok égve*, *kedden kezdődik*, *ha valamit hall*.
- The closing formula under the stamp (*Isten vele, édesem; sírig hű kedvese; Feri*) is the same as on HCP1216 and sisters. The address, recipient and hand match the family.

## Response to review 1

Verdict REVISE. I re-checked each point on the reviewer's crops and on my own (`work/crops2/`). All eight findings are accepted, the key is unchanged, and the command was re-run after the fixes (603 signs, all hashes OK).

1. **Row 25 end (major): fixed.** I confirm both points on `review/work/corner.png` and `end25.png`: the long hooked arc is the t bar, and the heavy stroke plus small tick stand to the upper right of the loop, matching the ü of *gyülés* (`review/work/c3.png`). Ledger `H? O` became `T O"`, and the `H?` key entry was removed from `work/decode.py`. Literal, normalized text, both translations, item 1 and "Why it is correct" are updated. The dots rest partly on sense, as item 1 says.
2. **`miatt, ám azt` (minor): fixed.** Normalized text and translations reworked; "That other one" is gone. The referent stays marked as an inference (item 8).
3. **`úgy én` (minor): fixed.** The emendation to *ugyan* is dropped (item 10) and the translations are changed.
4. **Row 20 dot (minor): fixed.** A dark mark stands above the sign (`review/work/r20b.png`). Ledger `I>i` became `I`; item 4 records that it could be accidental.
5. **Row 22 j (minor): fixed.** The low crossbar is visible on `review/work/r22.png`; disclosed in item 7.
6. **`vasár` (minor): fixed.** The alternative is in item 10.
7. **Postmarks (minor): fixed, and slightly stronger.** On my crop `work/crops2/pm-right.png`, rotated upright, GYÖN is legible, not only GYÖ. The other cancel shows …ÁS (`work/crops2/pm-left.png`). No date or town is claimed. Layout section updated.
8. **Margin end (minor): fixed.** Ledger `O>ja` became `O>o|i`, so the literal block shows `ir{o|i}a`. The normalized reading stays *írja meg*.

I also looked at the picture side, which the reviewer had not: a printed photograph of a couple with a printed series number and no handwriting.
