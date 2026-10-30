# HCP 1304 (cpc_--04_HU__HU_Jasz Arokszalas_jolanka-82): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (603 of 603 written signs; no unread fragment, a few sign calls disclosed below); independent review 1 verdict REVISE, all findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1304 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1304), portal name cpc_--04_HU__HU_Jasz Arokszalas_jolanka-82, part of Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a printed photograph of a couple embracing, with a printed series number and no handwriting. The message is on the address side, in purple ink, in invented signs. Rows 1 to 24 fill the left half of the card. Rows 25 and 26 run along the whole bottom edge, and row 26 turns the bottom-right corner and climbs the right edge to the top. Five more rows stand in the stamp box, hidden under the stamp, which has since been removed.

The address is in plain writing: Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás ("To the promising young lady Jolánka Tóth, Jászárokszállás"). Two cancels are on this side. The one at the stamp box shows GYÖN, with nothing legible after it. The fainter one shows …ÁS, which fits Jászárokszállás. No date can be read. Gyöngyös would fit GYÖN, and also the writer's lemegyek ("I go down"), but this is not proved. The card is undated.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the two cancels and the empty stamp box (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards to Jolánka Tóth, signed by Feri, several of which are deciphered in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery. No earlier work exists on this number, and no reading of this card was supplied or consulted.

## Method

The key was taken unchanged from HCP 1216 and its sisters. The work was the transcription. Claude Opus 5.5 read every row from 2x to 6x enlargements of the un-converted scan and recorded a ledger with one token per written sign (603 tokens, `work/ledger.txt`). The transcription is manual, not OCR, and not blind: word sense helped to settle close signs, and those places are listed below.

Reviewer and solver were separate Claude Opus 5.5 agents. The reviewer read all 26 rows, the margin and the stamp box from its own crops in a separate stroke notation, and compared the result by script. The two readings now agree in every row, apart from notation at the two written stops and the two sense-based signs (row 24 and the margin).

The writer spells loosely, so the literal decipherment is kept as written and the normalized Hungarian is editorial.

To reproduce the decoding from the repository root:

```sh
python3 -I ciphers/hcp-1304/work/decode.py
```

The script checks the SHA-256 of both scans in `source/` and both originals in `work/hires/`, decodes the ledger with the key, and prints the literal rows and the normalized text. It does not read the image; the transcription step is manual.

## Key

Hungarian simple monoalphabetic substitution with invented signs. Word spaces are partly kept; dots and double marks over vowels are written, acute marks mostly not. The names are conventional descriptions of the handwritten shapes.

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

One sign serves for both h and p. On this card gy is written as two signs (g + y), not as the family's joined sign. The letters q, w and x do not occur.

## Plaintext

Literal decipherment (`{n}` = value taken from word sense, `{o|i}` = sign read either way):

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

Normalized Hungarian:

**Szeretett édes Jolánkám! Becses sorait megkaptam, melyet köszönök szépen. Igazán meghat sorai, miből látom, mily nemes szíve van önnek, édes Jolánkám, amit talán nem is érdemlek meg. Már magam is restellem, hogy így le vagyok égve. Ha Moczárék nem biztatnának munkával, egyszerűen úgy tennék, mintha messze volnék Jolánkától. Úgy én elmennék a városból, ha sorozás nem lenne, azt meg kell várnom. Még ez a tömegsztrájk is akadályoz. A kedves mamája előtt restellem magam, hazudni nem tudok, így Jolánka is tudja, hogy nehéz a helyzetem. Moczár még nem írt. Talán azt gondolta, hogy vasár[nap] lemegyek, de nem mertem, mert gyűlés volt a tömegsztrájk miatt, ám azt hiszem, kedden kezdődik. Ha valamit hall Moczáréknál, írja meg.**

**Under the stamp: Isten vele, édesem! Sírig hű kedvese, Feri.**

English translation:

**My beloved, sweet Jolánka! I received your esteemed lines, for which I thank you very much. Your lines truly move me; from them I see what a noble heart you have, dear Jolánka, which perhaps I do not even deserve. I am already ashamed myself of being so broke. If the Moczárs were not encouraging me with work, I would simply act as if I were far away from Jolánka. So I would leave the city if there were no conscription; I have to wait for that. On top of that this mass strike is holding me back too. I am ashamed before your dear mother; I cannot lie, so Jolánka too knows that my situation is hard. Moczár has not written yet. Perhaps he thought that I would go down on Sunday, but I did not dare, because there was a meeting on account of the mass strike; but I believe it starts on Tuesday. If you hear anything at the Moczárs, write and tell me.**

**Under the stamp: Farewell, my darling! Your sweetheart, faithful unto the grave, Feri.**

Slovak translation:

**Moja milovaná, sladká Jolánka! Vaše vzácne riadky som dostal, za čo Vám pekne ďakujem. Vaše riadky ma naozaj dojímajú; vidím z nich, aké ušľachtilé srdce máte, drahá Jolánka, čo si možno ani nezaslúžim. Sám sa už hanbím, že som taký bez peňazí. Keby ma Moczárovci nepovzbudzovali prácou, jednoducho by som sa správal, akoby som bol ďaleko od Jolánky. Tak by som ja odišiel z mesta, keby nebolo odvodov; na tie musím počkať. Navyše mi prekáža aj tento masový štrajk. Pred Vašou milou mamou sa hanbím, klamať neviem, a tak aj Jolánka vie, že moja situácia je ťažká. Moczár ešte nepísal. Možno si myslel, že v nedeľu prídem dole, ale neodvážil som sa, lebo kvôli masovému štrajku bolo zhromaždenie; myslím však, že sa to začne v utorok. Ak niečo počujete u Moczárovcov, napíšte mi to.**

**Pod známkou: S Bohom, drahá! Váš do hrobu verný milý, Feri.**

Notes on the sense: le vagyok égve is the idiom "I am broke". Sorozás is military conscription. The third-person Jolánka is a polite reference to the addressee, in the family's formal Ön style. The letter says Feri cannot leave town because of the coming conscription, that he depends on work promised by the Moczárs, and that the mass strike is in his way.

## Uncertainties

1. **Row 25 end, volta tö|meg.** After volt a comes a t drawn with a pen lift: a thick stroke, then a separate long, nearly horizontal arc hooked down at its end. That is the gamma, not the short steep tick of the h/p sign. The loop after it has two marks to its upper right, a heavy stroke and a small tick, the same pattern as the ü of gyülés in this row. With row 26 `meg sztrajk` this gives a tömegsztrájk, the compound on row 18. The two marks are small, so the dots rest partly on that matching shape and on the resulting word. The row break falls inside the compound, as at Mo|czárék and rest|ellem.
2. **Row 26 margin, ir{o|i}ameg → írja meg.** On the card: dotted i, F (r), a loop without a dot, two bars, meg. No inverted-T j is written. írja meg ("write it") is chosen by sense and by the formal address; literally the signs give iro a meg or, with a dotless i, iria meg. Írom meg ("I shall write") is excluded because the two-bar sign stands before the m.
3. **Row 24 tala{n} → talán.** The sign is tall stroke + short tick, normally h/p, not two short strokes. Value n is from word sense only (tala? azt gondolta); this is a d/n/h stroke-length call.
4. **Row 20 hazudni.** The dot below the final sign belongs to row 21, but a dark mark stands directly above the sign and is not part of row 19's e. It is most likely this i's dot, though it could be accidental; hazudni is the only sense either way. The z here, in azt, kezdődik and biztat- is the near-upright variant of the crossed diagonal, close to f; z rests on word sense in those words.
5. **Row 3 kahtam.** A blot lies over the top of the h/p sign; the tall + short sign is visible beside it. Also h/p by sense in kaptam, szépen (`szehen`); the same h sign is real h in hogy, hat, ha, hal.
6. **Row 8 talan.** The second-syllable sign shows two bars and an ink spot below; read a, e not excluded by shape alone.
7. **Rows 14 and 22, j against f.** In row 14 `jolankatol` the j has a slight overshoot and looks a little like a low cross; Jolánkától fixes it. In row 22 `hejzetem` the crossbar stands low with a short tail below it, closer still to a cross; f is excluded only by word sense.
8. **Row 26 miattamazt → miatt, ám azt.** All signs are clear; the division is editorial. Ám azt hiszem, kedden kezdődik is ordinary Hungarian. What starts on Tuesday is not said; the strike is the only subject in the clause before it, but that is an inference.
9. **Row 5 meghat** spans rows 4/5 (`meg | hat`); a t-sign in this row has a dot beneath it that seems accidental. The present tense meghat is taken as written.
10. `ugyen` is taken as úgy én, two words, not as a misspelt ugyan: no a is written, and "so I would leave" follows mintha messze volnék. Writer's spellings normalized: szeretet → szeretett, restelem → restellem, elmenek → elmennék (one n written), kel → kell, kedenkez- → kedden kez-, akadajoz → akadályoz (j for ly), hejzetem → helyzetem, elot → előtt, vasar → vasár[nap] (abbreviation, omission, or the older form vasár for Sunday; vásár[ra] lemegyek, "go down to the fair", is possible with an assumed omission, and the translation keeps Sunday), Moczareknal written Moczarekna (final l omitted), hal → hall, biztatnanak → biztatnának. Accents are mostly unwritten and are supplied. Le vagyok égve is the idiom "I am broke"; lemegyek "I go down" presumably to the addressee's area; sorozás is military conscription.
11. Moczár is read as a surname from three independent occurrences (rows 10/11, 23, margin); no outside identification is claimed. Mamája is taken as the addressee's mother, and the third-person Jolánka as polite reference to the addressee, in the family's formal Ön style. The subject of gondolta is taken to be Moczár; that is interpretive.
12. The strike suggests a date around the Hungarian labour unrest of the 1910s, but the card itself gives no date and I claim none.

![The end of row 25 at the corner, with row 26 below: the stroke with its hooked arc (t), the loop with two marks at its upper right (ö), and at the right the wave of va|lamit turned with the margin (review/work/corner.png)](../review/work/corner.png)

Other limits: the sender is known only as Feri, Moczár is not identified, and it is not known which strike is meant. The transcription of faint signs was made with the sense in view. No prior publication of this card turned up; the check rests on the portal status and the AI Decipherment Register (2026-10-30), not on a wider literature search.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It ran the command, confirmed the key against HCP 1216, and made an independent sign-by-sign reading. It found the decipherment sound and raised eight points, all accepted after re-checking the crops:

- **Row 25 end (major).** The first version left `a {h|t}o` unread. The reviewer showed a t with a pen lift and two overlooked marks of ö, giving a tö|megsztrájk, the compound of row 18. This is the only change of a sign value, and it resolved the sentence.
- **Word division.** `miattamazt` is miatt, ám azt ("but I believe"), not miatt. Amazt. `ugyen` is úgy én, not a misspelt ugyan.
- **Sign notes.** The dot of the final i of hazudni, the cross-like j of hejzetem and the undotted loop in ir?a meg are now recorded accurately.
- **Vasár.** The alternative vásár[ra] is stated.
- **Postmarks.** The partial legends are recorded; the first version called them too faint to read. The solver's own crop shows GYÖN, one letter more than the review gave.

No key sign changed. The reading of the whole letter stands, with one sentence made clear.

## Sources

- HC Portal record 1304, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1304 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3972/conversions/cpc_--04_HU__HU_Jasz-Arokszalas_jolanka-82_pic-large.jpg, original https://api.hcportal.eu/media/3972/cpc_--04_HU__HU_Jasz-Arokszalas_jolanka-82_pic.jpg.
- Address side: https://api.hcportal.eu/media/3973/conversions/cpc_--04_HU__HU_Jasz-Arokszalas_jolanka-82_adr-large.jpg, original https://api.hcportal.eu/media/3973/cpc_--04_HU__HU_Jasz-Arokszalas_jolanka-82_adr.jpg.
- Family key: ciphers/hcp-1216 and sister cards in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30, no record for this card.
